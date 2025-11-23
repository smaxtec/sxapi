from sxapi.cli.parser.subparser.aborts.create import SxApiAbortsCreateSubparser
from sxapi.cli.parser.subparser.aborts.delete import SxApiAbortsDeleteSubparser
from sxapi.cli.parser.subparser.aborts.update import SxApiAbortsUpdateSubparser


class SxApiAbortsSubparser:
    @classmethod
    def register_as_subparser(cls, parent_subparser):
        return cls(parent_subparser)

    def __init__(self, parent_subparser, subparsers=True):
        self._parser = parent_subparser.add_parser(
            "aborts",
            help="Working on aborts",
            usage="sxapi [base_options] aborts [abort_sub_commands]",
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
        pass

    def _add_subparser(self):
        SxApiAbortsUpdateSubparser.register_as_subparser(self._subparsers)
        SxApiAbortsCreateSubparser.register_as_subparser(self._subparsers)
        SxApiAbortsDeleteSubparser.register_as_subparser(self._subparsers)

    def _set_default_func(self):

        self._parser.set_defaults(func=lambda args: self._parser.print_help())
