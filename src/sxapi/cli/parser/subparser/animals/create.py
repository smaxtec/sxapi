import argparse
import json
import sys

from sxapi.cli import cli_user
from sxapi.errors import (
    SxapiAuthorizationError,
    SxapiFileNotFoundError,
    SxapiInvalidJsonError,
    SxapiMissingOrgaIDError,
)

DESCRIPTION = """
    Create animals for the given organisation.

    Basic Example:
    {
        "mark": "123456",
        "organisation_id": "123456",
        "official_id": "123456",
        "birthday": "2018-01-01",
        "name": "Bella",
    }

    All available fields can be found here: https://api.smaxtec.com/api/v2/animals

    If the call was successful the whole animal is returned.
"""


class SxApiAnimalsCreateSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=False):
        self._parser = parent_subparser.add_parser(
            "create",
            help="create animals",
            usage="sxapi [base_options] animals create [options] ANIMAL_JSON_FILE",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=DESCRIPTION,
        )

        self._add_arguments()
        self._set_default_func()

        if subparsers:
            self.reg_subparsers = []
            self._subparsers = self._parser.add_subparsers(
                title="Sub Commands",
                description="Available subcommands:",
                dest="animals_sub_commands",
            )

            self._add_subparser()

    def _add_arguments(self):
        self._parser.add_argument(
            "animal_json",
            nargs="?",
            type=argparse.FileType("r"),
            default=sys.stdin,
            help="Path to json file containing animal data. (default: stdin)",
            metavar="ANIMAL_JSON_FILE",
        )
        self._parser.add_argument(
            "--organisation_id",
            nargs="?",
            type=str,
            help="ID of the organisation to retrieve animals from",
            metavar="ORGANISATION_ID",
        )

    def _add_subparser(self):
        pass

    def _set_default_func(self):
        def animals_sub_function(args):
            if not cli_user.check_credentials_set():
                raise SxapiAuthorizationError()

            organisation_id = cli_user.organisation_id

            if args.organisation_id:
                organisation_id = args.organisation_id

            if organisation_id is None:
                raise SxapiMissingOrgaIDError()

            if args.animal_json.isatty():
                raise SxapiFileNotFoundError()

            try:
                animal_json = json.load(args.animal_json)

                res = cli_user.public_v2_api.animals.post(
                    organisation_id, **animal_json
                )

            except json.JSONDecodeError:
                raise SxapiInvalidJsonError()

            print(res)

        self._parser.set_defaults(func=animals_sub_function)
