import argparse
import sys

from setuptools import setup


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


def cli_run():
    """Start CLI"""
    cli().run()
