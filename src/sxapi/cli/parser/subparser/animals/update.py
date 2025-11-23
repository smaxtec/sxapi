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
    Update an animal for the given organisation.

    Provide an dict containing the fields to update.
    1. The animal_id must be contained in the update dict.
    2. If you want to move the animal to another organisation,
        the mark needs to be unique in the new organisation.

    Basic Example:
    {
        "animal_id": "123456", # REQUIRED
        ...
        "organisation_id": "1234bdc234d
        "mark": "123456",
        "official_id": "AT000123456",
        "official_id_rule": "AT",
        "birthday": "2018-01-01",
        "name": "Bella",
        ...
    }

    All available fields can be found here:
    POST https://api.smaxtec.com/api/v2/animals/{animal_id}

    If the call was successful the whole animal is returned.
"""


class SxApiAnimalsUpdateSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=False):
        self._parser = parent_subparser.add_parser(
            "update",
            help="Update animal",
            usage="sxapi [base_options] animals update [options]",
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
            "update_dict",
            nargs="?",
            type=argparse.FileType("r"),
            default=sys.stdin,
            help="Path to file containing animal update dict. (default: stdin)",
            metavar="ANIMAL_UPDATE_DICT",
        )
        self._parser.add_argument(
            "-o",
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

            if args.update_dict.isatty():
                raise SxapiFileNotFoundError()

            try:
                update_dict = json.load(args.update_dict)
                animal_id = update_dict.pop("animal_id", None)
                print(update_dict)
                res = cli_user.public_v2_api.animals.put(animal_id, **update_dict)

            except json.JSONDecodeError:
                raise SxapiInvalidJsonError()

            print(res)

        self._parser.set_defaults(func=animals_sub_function)
