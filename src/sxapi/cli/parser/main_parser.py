import argparse

from setuptools import setup

from sxapi.cli import cli_user
from sxapi.cli.configuration import Config
from sxapi.cli.parser.subparser import (
    SxApiAbortsSubparser,
    SxApiAnimalsSubparser,
    SxApiTokenSubparser,
)


def version_info():
    """Print version info."""
    setup(use_scm_version={"version_scheme": "no-guess-dev"})


def api_status():
    """
    Print online status of api/v2 and integration/v2
    """

    if not cli_user.api_access_token:
        print("No credentials set. Use --help for more information.")
        return

    pub_resp = cli_user.public_v2_api.get("/service/status")
    int_resp = cli_user.integration_v2_api.get("/service/status")

    print(f"PublicV2 status: {pub_resp['result']}")
    print(f"IntegrationV2 status: {int_resp['result']}")


class SxApiMainParser:
    def __init__(self, subparsers=False):

        self.config = Config()

        self._parser = argparse.ArgumentParser(
            description=(
                "Issue calls to the smaXtec system API to import and export data."
            ),
            usage="%(prog)s [options] <sub_command> [sub_command_options] [<args>]",
        )

        self._add_arguments()

        if subparsers:
            self.reg_subparsers = []
            self._subparsers = self._parser.add_subparsers(
                title="Sub Commands",
                description="Available subcommands:",
                dest="main_sub_commands",
            )

            self._add_subparser()

    def _add_arguments(self):
        # add arguments to the parser
        self._parser.add_argument(
            "--version",
            action="store_true",
            default=False,
            help="print version info and exit.",
        )
        self._parser.add_argument(
            "--status",
            action="store_true",
            default=False,
            help="prints status of api/V2 and integration/v2",
        )
        self._parser.add_argument(
            "-t",
            "--access_token",
            type=str,
            help="Access Token",
        )
        self._parser.add_argument(
            "-k",
            "--use_keyring",
            action="store_true",
            help="Use keyring as token source!",
        )
        self._parser.add_argument(
            "-c", "--configfile", type=str, help="Path to config file"
        )
        self._parser.add_argument(
            "--print-configfile",
            action="store_true",
            help="Print example config file and exits",
        )
        self._parser.add_argument(
            "-o",
            "--organisation_id",
            type=str,
            default=None,
            help="ID of working organisation",
        )

    def _add_subparser(self):
        # Initiate other subparsers here
        SxApiTokenSubparser.register_as_subparser(self._subparsers)
        SxApiAnimalsSubparser.register_as_subparser(self._subparsers)
        SxApiAbortsSubparser.register_as_subparser(self._subparsers)

    def parse_args(self, args):
        if len(args) == 0:
            self._parser.print_help()
            return

        args = self._parser.parse_args(args)

        if not args:
            return

        if args.print_configfile:
            with open("./src/sxapi/cli/example-config.conf", "r") as f:
                print(f.read())
            return

        if args.configfile:
            self.config = Config(args.configfile)

        cli_user.init_user(
            self.config, args.access_token, args.use_keyring, args.organisation_id
        )

        if args.status:
            api_status()

        if args.version:
            version_info()

        if args.use_keyring and args.access_token:
            print(
                "Choose either -k (keyring), -t (argument) or"
                " no flag (environment/config)!"
            )
            return

        # run set_defaults for subparser
        if hasattr(args, "func"):
            args.func(args)

        return args
