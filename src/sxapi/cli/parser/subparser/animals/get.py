import json

from sxapi.cli import cli_user
from sxapi.errors import (
    SxapiAuthorizationError,
    SxapiMissingOrgaIDError,
)

DESCRIPTION = """
    Get animals from the smaXtec system.

    If no optional flags are set, get all animals from the specified organisation.

    If the call was successful the whole animal is returned.
"""


class SxApiAnimalsGetSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=False):
        self._parser = parent_subparser.add_parser(
            "get",
            help="Get animals",
            usage="sxapi [base_options] animals get [options]",
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
            "--ids",
            nargs="+",
            help="ID's of the animals to retrieve",
            metavar="ANIMAL_IDS",
        )
        self._parser.add_argument(
            "--official-ids",
            action="store_true",
            help="The given ANIMAL_IDS are animals official_ids\
             instead of internal_ids",
        )
        self._parser.add_argument(
            "-o",
            "--organisation_id",
            nargs="?",
            type=str,
            help="ID of the organisation to retrieve animals from",
            metavar="ORGANISATION_ID",
        )
        self._parser.add_argument(
            "--limit",
            "-l",
            default=0,
            type=int,
            help="Limit the number of animals to retrieve.",
            metavar="NUMBER_OF_ANIMALS",
        )
        self._parser.add_argument(
            "--archived",
            action="store_true",
            default=False,
            help="Include archived animals. default = False.\
             (only active if --all is set)",
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

            animals = []

            if args.ids:
                if args.official_ids:
                    # there is no endpoint to get a list of animals by official id
                    for official_id in args.ids:
                        animal = cli_user.public_v2_api.animals.get_by_official_id(
                            organisation_id, official_id
                        )

                        if (
                            not animal["archived"]
                            or animal["archived"]
                            and args.archived
                        ):
                            animals.append(animal)
                else:
                    for animal in cli_user.public_v2_api.animals.get_by_ids(args.ids):
                        if animal["archived"] and args.archived:
                            animals.append(animal)
            else:
                animals = cli_user.integration_v2_api.organisations.get_animals(
                    organisation_id,
                    include_archived=args.archived,
                )

            if args.limit > 0:
                animals = animals[: args.limit]

            print(json.dumps(animals))

        self._parser.set_defaults(func=animals_sub_function)
