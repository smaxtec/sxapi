import argparse
import os
import sys

from setuptools import setup

from sxapi.base import (
    IntegrationAPIV2,
    PublicAPIV2,
)


class cli:
    """CLI class for handling arguments and calling the API."""

    def __init__(self):
        pass

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
            "--status",
            action="store_true",
            default=False,
            help="prints status of api/V2 and integration/v2",
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

        if args.status:
            self.api_status()

        if args.version:
            self.version_info()


def cli_run():
    """Start CLI"""
    cli().run()
