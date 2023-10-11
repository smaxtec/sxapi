import getpass

import requests

from sxapi.base import PublicAPIV2
from sxapi.cli import cli_user


def create_token_parser(subparsers):
    """
    Token subparser for cli_tests.
    Responsible for managing tokens/credentials.

    The --print_token/-p Flag prints the token, stored in keyring or in
    environment, to stdout. It expects exactly only one argument -> 'e'
    for printing the token stored in the environment, 'k' for printing
    the token stored in keyring and 'ek' for printing both at the same time.

    The --set_keyring/-s flag stores the token (given as argument) in the keyring.
    It expects exactly one argument -> the token you want to store.

    The --clear_keyring/-c Flag deletes the token from the keyring.
    This flag doesn't expect any argument.

    The --new_token/-n Flag calls api to get new token and prints it to stdout.
    It expects exactly two arguments -> smaxtec-username and smaxtec-password.

    It is not possible to use more than one of those flags at the same time
    """
    token_parser = subparsers.add_parser(
        "token",
        help="Get/Set credentials aka 'SMAXTEC_TOKEN' from/to specified "
        "storage location or create new one",
    )

    token_parser.add_argument(
        "--print_token",
        "-p",
        nargs="?",
        const="ek",
        help="Print the current token stored in keyring/environment to stdout. "
        "One argument required. Possible args 'e' environment | "
        "'k' keyring | ek for printing both.",
    )
    token_parser.add_argument(
        "--set_keyring",
        "-s",
        nargs=1,
        help="Store the given token in keyring! Requires one argument <token>",
    )
    token_parser.add_argument(
        "--new_token",
        "-n",
        nargs="+",
        help="Reqeust new token. Requires one argument <username>, "
        "second argument <password> is optional!",
    )
    token_parser.add_argument(
        "--clear_keyring",
        "-c",
        action="store_true",
        default=False,
        help="Remove the token from keyring!",
    )

    token_parser.set_defaults(func=token_sub_function)


def token_sub_function(args):
    """
    The token subparser default function.
    This function gets called if token subparser is used.

    Checks args and calls the specific helper function (see below) according to
    the present flag.
    """
    number_op = (
        bool(args.print_token)
        + bool(args.set_keyring)
        + bool(args.new_token)
        + bool(args.clear_keyring)
    )

    if number_op > 1:
        print(
            "Invalid Combination! Please use just one out of these parameters "
            "[--print_token, --set_keyring, --new_token, --clear_keyring]"
        )
        return

    if args.print_token:
        handle_print_token(args)
    elif args.set_keyring:
        handle_set_token(args)
    elif args.clear_keyring:
        handle_clear_token()
    elif args.new_token:
        handle_new_token(args)


# Flag helper functions
def handle_print_token(args):
    """
    Logic behind the token subparser --print_token flag.

    Prints the token from the desired source (environment or keyring) to stdout.
    """
    keyring = str(cli_user.get_token_keyring())
    env = str(cli_user.get_token_environment())

    if args.print_token == "ek":
        print(f"\nKeyring: {keyring}\n\nEnvironment: {env}")
        return
    elif len(args.print_token) > 2:
        print("Invalid number of arguments. Use --help for usage information.")
        return

    if "e" != args.print_token and "k" != args.print_token:
        print(
            "Invalid arguments. Only use 'e' for environment, 'k' for keyring "
            "or 'ek' for both."
        )
        return

    if "e" == args.print_token:
        print(f"\nEnvironment Token: {env}\n")
    elif "k" == args.print_token:
        print(f"\nKeyring Token: {keyring}\n")


def handle_set_token(args):
    """
    Logic behind the token subparser --set_keyring flag.

    Parses the args and stores the token in the keyring.
    """
    token = args.set_keyring[0]
    cli_user.set_token_keyring(token=token)
    print("Token is stored in keyring!")


def handle_clear_token():
    """
    Logic behind the token subparser --clear_keyring flag.

    Deletes the token from the keyring.
    """
    cli_user.clear_token_keyring()
    print("Token was deleted from keyring!")


def handle_new_token(args):
    """
    Logic behind the token subparser --new_token flag.

    Parses the args, creates an PublicAPIV2 instance to get new token and
    print the new token to stdout.
    """
    if len(args.new_token) == 2:
        username = args.new_token[0] if "@" in args.new_token[0] else args.new_token[1]
        pwd = args.new_token[1] if "@" not in args.new_token[1] else args.new_token[0]

    if len(args.new_token) == 1:
        username = args.new_token[0]
        pwd = getpass.getpass()

    if "@" not in username:
        print("Username must be a email!")
        return

    try:
        token = str(PublicAPIV2(email=username, password=pwd).get_token())
        print("SMAXTEC_TOKEN=" + token)
    except requests.HTTPError as e:
        if "401" in str(e) or "422" in str(e):
            print("Username or Password is wrong!")
    except Exception as e:
        print(e)
