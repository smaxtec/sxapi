import argparse
import sys

from .base import PublicAPIV2, IntegrationAPIV2
from .credentials import UserCredentials

from setuptools import setup

class cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        self.credentials = UserCredentials()

    @staticmethod
    def version_info():
        """Print version info."""
        setup(use_scm_version={"version_scheme": "no-guess-dev"})

    @staticmethod
    def parse_args(args):
        """Parse arguments from the CLI."""
        parser = argparse.ArgumentParser(
            description=(
                "Issue calls to the smaXtec system API to import and export data."
            )
        )
        parser.add_argument(
            "--version",
            action="store_true",
            default=False,
            help="""print version info and exit.""",
        )
        parser.add_argument(
            "-u",
            "--user",
            type=str,
            help="User email",
        )
        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="User password",
        )
        parser.add_argument(
            "-t",
            "--token",
            type=str,
            help="Access Token",
        )
        parser.add_argument(
            "--show_credentials",
            action="store_true",
            default=False,
            help="This will show your PLAINTEXT credentials!",
        )
        parser.add_argument(
            "--clean",
            action="store_true",
            default=False,
            help="This will remove all stored credentials!",
        )

        if not args:
            parser.print_help()
            return
        return parser.parse_args(args)

    def run(self):
        """Call sxapi functions based on passed arguments."""
        args = self.parse_args(sys.argv[1:])
        if not args:
            return 0

        if args.version:
            self.version_info()

        if args.token:
            self.credentials.set(token=args.token)

        elif bool(args.user) != bool(args.password):
            print("Please use -u and -p together!")
            return 0

        elif args.user and args.password:
            self.credentials.set(username=args.user, password=args.password)
            api = PublicAPIV2(email=args.user, password=args.password)
            self.credentials.set(token=api.get_token)

        if args.clean:
            self.credentials.clean()

        if args.show_credentials:
            user_credentials = self.credentials.get()
            for key, value in user_credentials.items():
                print(f"{key}={value}")

def cli_run():
    """Start CLI"""
    cli().run()
