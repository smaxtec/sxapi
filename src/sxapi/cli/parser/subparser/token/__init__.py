import getpass

import requests

from sxapi.cli import cli_user
from sxapi.errors import (
    SxapiAuthorizationError,
    SxapiCliArgumentError,
)
from sxapi.publicV2 import PublicAPIV2


def handle_print_token(args):
    """
    Logic behind the token subparser --print_token flag.

    Prints the token from the desired source (environment or keyring) to stdout.
    """
    keyring = str(cli_user.get_token_keyring())
    env = str(cli_user.get_token_environment())

    if args.print_token == "ek":
        print(f"\nKeyring: {keyring}\n\nEnvironment: {env}")
        return 0
    elif len(args.print_token) > 2:
        raise SxapiCliArgumentError(
            "Invalid number of arguments. Use --help for usage information."
        )

    if "e" != args.print_token and "k" != args.print_token:
        raise SxapiCliArgumentError(
            "Invalid arguments. Only use 'e' for environment, 'k' for keyring or 'ek' for both."
        )

    if "e" == args.print_token:
        print(f"\nEnvironment Token: {env}\n")
        return 0
    elif "k" == args.print_token:
        print(f"\nKeyring Token: {keyring}\n")
        return 0


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


def handle_new_token():
    """
    Logic behind the token subparser --new_token flag.

    Parses the args, creates an PublicAPIV2 instance to get new token and
    print the new token to stdout.
    """

    username = input("Username: ")

    if "@" not in username:
        raise SxapiCliArgumentError("Username must be a email!")

    pwd = getpass.getpass()

    try:
        token = str(PublicAPIV2(email=username, password=pwd).get_token())
        print("SMAXTEC_API_ACCESS_TOKEN=" + token)
        return 0
    except requests.HTTPError as e:
        if "401" in str(e) or "422" in str(e):
            raise SxapiAuthorizationError("Username or Password is wrong!")


class SxApiTokenSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=False):
        self._parser = parent_subparser.add_parser(
            "token",
            help="Get/Set credentials aka 'SMAXTEC_API_ACCESS_TOKEN' from/to specified "
            "storage location or create new one",
            usage="sxapi [base_options] token [options]",
        )

        self._add_arguments()
        self._set_default_func()

        if subparsers:
            self.reg_subparsers = []
            self._subparsers = self._parser.add_subparsers(
                title="Sub Commands",
                description="Available subcommands:",
                dest="main_sub_commands",
            )

            self._add_subparser("naf")

    def _add_arguments(self):
        self._parser.add_argument(
            "--print_token",
            "-p",
            nargs="?",
            const="ek",
            help="Print the current token stored in keyring/environment to stdout. "
            "One argument required. Possible args 'e' environment | "
            "'k' keyring | ek for printing both.",
            metavar="SOURCE",
        )
        self._parser.add_argument(
            "--set_keyring",
            "-s",
            nargs=1,
            help="Store the given token in keyring! Requires one argument <token>.",
            metavar="TOKEN",
        )
        self._parser.add_argument(
            "--new_token",
            "-n",
            action="store_true",
            help="Reqeust new token",
        )
        self._parser.add_argument(
            "--clear_keyring",
            "-c",
            action="store_true",
            default=False,
            help="Remove the token from keyring!",
        )

    def _add_subparser(self, name, **kwargs):
        raise NotImplementedError

    def _set_default_func(self):
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
                print(number_op)
                raise SxapiCliArgumentError(
                    "Invalid Combination! Please use just one out of these parameters "
                    "[--print_token, --set_keyring, --new_token, --clear_keyring]"
                )

            if args.print_token:
                return handle_print_token(args)
            elif args.set_keyring:
                return handle_set_token(args)
            elif args.clear_keyring:
                return handle_clear_token()
            elif args.new_token:
                return handle_new_token()

            self._parser.print_help()

        self._parser.set_defaults(func=token_sub_function)
