import argparse

from sxapi.cli import cli_user
from sxapi.errors import SxapiAuthorizationError

DESCRIPTION = """
    Delete abort for the given animal.

    All available fields can be found here: https://api.smaxtec.com/api/v2/

    If the call was successful the updated animal is returned.
"""


class SxApiAbortsDeleteSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=False):
        self._parser = parent_subparser.add_parser(
            "delete",
            help="delete abort",
            usage="sxapi [base_options] aborts update ANIMAL_ID ABORT_ID",
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
                dest="abort_sub_commands",
            )

            self._add_subparser()

    def _add_arguments(self):
        self._parser.add_argument(
            "animal_id",
            nargs="?",
            type=str,
            help="ID of the animal to delete the abort for",
            metavar="ANIMAL_ID",
        )
        self._parser.add_argument(
            "abort_id",
            nargs="?",
            type=str,
            help="ID of the abort to delete",
            metavar="ABORT_ID",
        )

    def _add_subparser(self):
        pass

    def _set_default_func(self):
        def animals_sub_function(args):
            if not cli_user.check_credentials_set():
                raise SxapiAuthorizationError()

            res = cli_user.public_v2_api.animals.delete_aborts(
                animal_id=args.animal_id,
                abort_id=args.abort_id,
            )

            print(res)

        self._parser.set_defaults(func=animals_sub_function)
