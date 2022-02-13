from ..base import PublicAPIV2
from . import user_credentials


def handle_get_token(args):
    """logic behind the --get_token flag"""
    if not args.new_token:
        if args.keyring:
            print("Keyring Token: " + str(user_credentials.get_token_keyring()) + "\n")
        if args.environment or (args.keyring is args.environment is False):
            print(
                "Environment Token: "
                + str(user_credentials.get_token_environment())
                + "\n"
            )
    else:
        if args.keyring or args.environment:
            print("You cant use -k or -e in combination with -n!")
            return
        if args.user and args.password:
            print(
                "Token: "
                + PublicAPIV2(email=args.user, password=args.password).get_token()
            )
        else:
            print("To get new Token please give username <-u> AND password <-p>!")


def handle_set_token(args):
    """logic behind the --set_token flag"""
    if args.environment:
        print(
            "This application can only store/delete things in keyring <-k>. "
            "Changes to the environment must be done manually!"
        )
        return

    if not args.token:
        print("Please specify the token <-t> you want to set!")
        return

    user_credentials.set_token_keyring(token=args.token)
    print("Token is stored in keyring!")


def handle_clear_token(args):
    """logic behind the --clear_token flag"""
    if args.environment:
        print(
            "This application can only store/delete things in keyring <-k>. "
            "Changes to the environment must be done manually!"
        )
        return

    user_credentials.clear_token_keyring()
    print("Token was deleted from keyring!")
