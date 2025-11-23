from sxapi.cli.parser.subparser.animals.create import SxApiAnimalsCreateSubparser
from sxapi.cli.parser.subparser.animals.get import SxApiAnimalsGetSubparser
from sxapi.cli.parser.subparser.animals.update import SxApiAnimalsUpdateSubparser


class SxApiAnimalsSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=True):
        self._parser = parent_subparser.add_parser(
            "animals",
            help="Working on animals",
            usage="sxapi [base_options] animals [animals_sub_commands]",
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
        pass

    def _add_subparser(self):
        SxApiAnimalsGetSubparser.register_as_subparser(self._subparsers)
        SxApiAnimalsCreateSubparser.register_as_subparser(self._subparsers)
        SxApiAnimalsUpdateSubparser.register_as_subparser(self._subparsers)

    def _set_default_func(self):

        self._parser.set_defaults(func=lambda args: self._parser.print_help())
