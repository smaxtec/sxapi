import argparse
import sys

from setuptools import setup

from sxapi.cli_sub_parser import create_gsd_parser


class cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        pass

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
        else:
            args.func(args)


def cli_run():
    """Start CLI"""
    cli().run()
