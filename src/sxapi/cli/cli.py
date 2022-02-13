import argparse
import sys

from setuptools import setup

from . import user_credentials
from .cli_sub_parser import create_gsd_parser
from .helper import (
    handle_clear_token,
    handle_get_token,
    handle_set_token,
)


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
        """Parse arguments from the CLI."""

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
            "-e",
            "--environment",
            action="store_true",
            default=False,
            help="Using the keyring as credential source!",
        )
        main_parser.add_argument(
            "-k",
            "--keyring",
            action="store_true",
            default=False,
            help="Using the keyring as credential source!",
        )
        main_parser.add_argument(
            "-u",
            "--user",
            type=str,
            help="User email. (Stored in keyring!)",
        )
        main_parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="User password. (Stored in keyring!)",
        )
        main_parser.add_argument(
            "-t",
            "--token",
            type=str,
            help="Access Token. (Stored in keyring!)",
        )
        main_parser.add_argument(
            "-n",
            "--new_token",
            action="store_true",
            default=False,
            help="Reqeust new token. (Stored in keyring!)",
        )
        main_parser.add_argument(
            "--clear_token",
            action="store_true",
            default=False,
            help="This will remove the token from keyring!",
        )
        main_parser.add_argument(
            "--get_token",
            action="store_true",
            default=False,
            help="Shows you the current_token (-e, -k), "
            "or a new one in combination with -n.",
        )
        main_parser.add_argument(
            "--set_token",
            action="store_true",
            default=False,
            help="Stores the given token in keyring!",
        )

        # gsd_parser
        subparsers = main_parser.add_subparsers(help="sub-command help")
        create_gsd_parser(subparsers)

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

        if args.get_token and args.set_token:
            print("You cant use --get_token and --set_token together!")
            return 0

        if args.get_token:
            handle_get_token(args)

        if args.set_token:
            handle_set_token(args)

        if args.clear_token:
            handle_clear_token(args)

        if args.keyring:
            user_credentials.token = user_credentials.get_token_keyring()

        if args.token:
            user_credentials.token = args.token

        # run set_defaults for subparser
        if hasattr(args, "func"):
            args.func(args)


def cli_run():
    """Start CLI"""
    Cli().run()
