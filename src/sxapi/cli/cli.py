import argparse
import configparser
import os
import sys
from os.path import (
    abspath,
    expanduser,
)

from setuptools import setup

from sxapi.cli import cli_user
from sxapi.cli.subparser.token import create_token_parser


class Cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        self.config_file_paths = ["/etc/sxapi.conf", "~/.config/sxapi.conf"]

    @staticmethod
    def update_config_with_env(config_dict):
        config_dict["user"] = os.getenv("SXAPI_USER", config_dict["user"])
        config_dict["pwd"] = os.getenv("SXAPI_PASSWORD", config_dict["pwd"])
        config_dict["orga"] = os.getenv("SXAPI_ORGA", config_dict["orga"])
        config_dict["api_public_v2_path"] = os.getenv(
            "SXAPI_API_PUBLIC_V2_PATH", config_dict["api_public_v2_path"]
        )
        config_dict["api_integration_v2_path"] = os.getenv(
            "SXAPI_API_INTEGRATION_V2_PATH", config_dict["api_integration_v2_path"]
        )

    def read_config_from_file(self, config_file_path):
        config_dict = {
            "user": None,
            "pwd": None,
            "orga": None,
            "api_public_v2_path": None,
            "api_integration_v2_path": None,
        }

        if config_file_path:
            self.config_file_paths.append(config_file_path)

        parsable_files = []
        for config_file in self.config_file_paths:
            config_file = expanduser(config_file)
            config_file = abspath(config_file)
            parsable_files.append(config_file)

        try:
            config = configparser.ConfigParser(interpolation=None)
            config.read(parsable_files)

            config_dict["user"] = config.get("SXAPI", "USER")
            config_dict["pwd"] = config.get("SXAPI", "PASSWORD")
            config_dict["orga"] = config.get("SXAPI", "ORGA")
            config_dict["api_public_v2_path"] = config.get(
                "SXAPI", "API_PUBLIC_V2_PATH"
            )
            config_dict["api_integration_v2_path"] = config.get(
                "SXAPI", "API_INTEGRATION_V2_PATH"
            )
        except (
            KeyError,
            configparser.NoSectionError,
            configparser.MissingSectionHeaderError,
        ) as e:
            if config_file_path:
                print(f"Error while reading config file: {e}")
                return
                # we should raise custom exception here

        return config_dict

    @staticmethod
    def api_status():
        """
        Print online status of api/v2 and integration/v2
        """

        if not cli_user.api_access_token:
            print("No credentials set. Use --help for more information.")
            return

        pub_resp = cli_user.public_v2_api.get("/service/status")
        int_resp = cli_user.integration_v2_api.get("/service/status")

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
            ),
            usage="%(prog)s [options] <sub_command> [sub_command_options] [<args>]",
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
            "--access_token",
            type=str,
            help="Access Token",
        )
        main_parser.add_argument(
            "-k",
            "--use_keyring",
            action="store_true",
            help="Use keyring as token source!",
        )
        main_parser.add_argument(
            "-c", "--configfile", type=str, help="Path to config file"
        )
        main_parser.add_argument(
            "--print-configfile",
            action="store_true",
            help="Print example config file and exits",
        )

        subparsers = main_parser.add_subparsers(title="sub_commands")
        # create_gsd_parser(subparsers)
        create_token_parser(subparsers)

        if not args:
            main_parser.print_help()
            return

        # check if subparser is called with arguments
        # otherwise print help for subparser
        elif args[0] in subparsers.choices.keys() and len(args) == 1:
            subparsers.choices[args[0]].print_help()
            return

        return main_parser.parse_args(args)

    def run(self):
        """Call sxapi functions based on passed arguments."""
        args = self.parse_args(sys.argv[1:])
        if not args:
            return 0

        if args.print_configfile:
            with open("./src/sxapi/cli/example-config.conf", "r") as f:
                print(f.read())
            return

        config_dict = self.read_config_from_file(args.configfile or None)

        self.update_config_with_env(config_dict)

        cli_user.init_user(config_dict, args.access_token, args.use_keyring)

        if args.status:
            self.api_status()

        if args.version:
            self.version_info()

        if args.use_keyring and args.access_token:
            print("Choose either -k (keyring), -t (argument) or no flag (environment)!")
            return

        # run set_defaults for subparser
        if hasattr(args, "func"):
            args.func(args)


def cli_run():
    """Start CLI"""
    Cli().run()
