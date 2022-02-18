import argparse
import sys

from setuptools import setup

from sxapi.cli import user_credentials
from sxapi.cli.subparser.get_sensor_data import create_gsd_parser
from sxapi.cli.subparser.token import create_token_parser


class Cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        self.public_api = None
        self.integration_api = None

    @staticmethod
    def version_info():
        """Print version info."""
        setup(use_scm_version={"version_scheme": "no-guess-dev"})

    @staticmethod
    def parse_args(args):
        """
        Parse arguments from the CLI and initializes subparsers.
        """
        main_parser = argparse.ArgumentParser(
            description=(
                "Issue calls to the smaXtec system API to import and export data."
            )
        )
        main_parser.add_argument(
            "--version",
            action="store_true",
            default=False,
            help="print version info and exit.",
        )

        main_parser.add_argument(
            "-t",
            "--arg_token",
            type=str,
            help="Access Token",
        )
        main_parser.add_argument(
            "-k",
            "--use_keyring",
            action="store_true",
            help="Use keyring as token source!",
        )

        # gsd_parser
        subparsers = main_parser.add_subparsers(help="sub-command help")
        create_gsd_parser(subparsers)
        create_token_parser(subparsers)

        if not args:
            main_parser.print_help()
            return
        return main_parser.parse_args(args)

    def run(self):
        """Call sxapi functions based on passed arguments."""
        args = self.parse_args(sys.argv[1:])
        if not args:
            return 0

        if args.version:
            self.version_info()

        if args.use_keyring and args.arg_token:
            print("Choose either -k (keyring), -t (argument) or no flag (environment)!")
            return

        if args.use_keyring:
            user_credentials.token = user_credentials.get_token_keyring()
        elif args.arg_token:
            user_credentials.token = args.token

        # run set_defaults for subparser
        if hasattr(args, "func"):
            args.func(args)


def cli_run():
    """Start CLI"""
    Cli().run()
