import argparse
import json
import sys

from setuptools import setup

from sxapi.publicV2.sensordata import get_sensor_data_for_animal


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
            help="print version info and exit.",
        )

        # gsd_parser
        subparsers = parser.add_subparsers(help="sub-command help")
        gsd_parser = subparsers.add_parser(
            "get_sensor_data",
            aliases=["gsd"],
            help="get sensor data from animal(by its ID)",
        )
        gsd_parser.set_defaults(func=gsd_sub_function)

        gsd_parser.add_argument("animal_id", help="animal you want get data from")
        gsd_parser.add_argument(
            "--metrics",
            "-m",
            nargs="*",
            default=None,
            help="metrics for sensordata",
        )
        gsd_parser.add_argument(
            "--from_date",
            "-fd",
            default=None,
            nargs=1,
            help="from_date format: YYYY-MM-DD",
        )
        gsd_parser.add_argument(
            "--to_date", "-td", default=None, nargs=1, help="to_date format: YYYY-MM-DD"
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
        else:
            args.func(args)


def gsd_sub_function(args):
    """
    function which gets call if the arguments were parsed
    with get_sensor_data sub-parser
    """
    id = args.animal_id
    metrics = args.metrics
    from_date = args.from_date
    to_date = args.to_date
    resp = get_sensor_data_for_animal(
        id, metrics=metrics, from_date=from_date, to_date=to_date
    )
    if resp is not None:
        print(json.dumps(resp, indent=0))


def cli_run():
    """Start CLI"""
    cli().run()
