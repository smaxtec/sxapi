import argparse
import os
import sys

from setuptools import setup

from sxapi.base import (
    IntegrationAPIV2,
    PublicAPIV2,
)
from sxapi.cli import user_credentials
from sxapi.cli.subparser.get_sensor_data import create_gsd_parser
from sxapi.cli.subparser.token import create_token_parser


class Cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        self.public_api = None
        self.integration_api = None

    @staticmethod
    def api_status():
        """
        Print online status of api/v2 and integration/v2
        """

        # TODO: this part is just a hacky trick, this should be moved
        #       when its finalized where to locate them!!!
        email = os.environ.get("SMAXTEC_USER")
        password = os.environ.get("SMAXTEC_PASSWORD")
        api_token = os.environ.get("SMAXTEC_TOKEN")

        if not api_token and not (password and email):
            print("No credentials set. Use --help for more information.")
            return

        public_api = PublicAPIV2(email=email, password=password, api_token=api_token)
        integration_api = IntegrationAPIV2(
            email=email, password=password, api_token=api_token
        )
        # hacky part end

        pub_resp = public_api.get("/service/status")
        int_resp = integration_api.get("/service/status")

        exit_code = 0

        if not (pub_resp["result"] == "ok" and int_resp["result"] == "ok"):
            exit_code = 1

        print(f"PublicV2 status: {pub_resp['result']}")
        print(f"IntegrationV2 status: {int_resp['result']}")

        exit(exit_code)

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
            "--status",
            action="store_true",
            default=False,
            help="prints status of api/V2 and integration/v2",
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

        if args.status:
            self.api_status()

        if args.version:
            self.version_info()

        if args.use_keyring and args.arg_token:
            print("Choose either -k (keyring), -t (argument) or no flag (environment)!")
            return

        if args.use_keyring:
            user_credentials.token = user_credentials.get_token_keyring()
        elif args.arg_token:
            user_credentials.token = args.arg_token

        # run set_defaults for subparser
        if hasattr(args, "func"):
            args.func(args)


def cli_run():
    """Start CLI"""
    Cli().run()
