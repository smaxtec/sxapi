import sys

from requests.exceptions import HTTPError

from sxapi.cli.parser.main_parser import SxApiMainParser
from sxapi.errors import (
    SxapiAuthorizationError,
    SxapiCliArgumentError,
    SxapiConfigurationFileError,
    SxapiFileNotFoundError,
    SxapiInvalidJsonError,
    SxapiMissingOrgaIDError,
    SxapiUnprocessableContentError,
)


def handle_cli_return_values(func):
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except SxapiAuthorizationError as e:
            error_msg = e
            exit_code = 1
        except SxapiUnprocessableContentError as e:
            error_msg = e
            exit_code = 2
        except SxapiConfigurationFileError as e:
            error_msg = e
            exit_code = 3
        except SxapiInvalidJsonError as e:
            error_msg = e
            exit_code = 4
        except SxapiFileNotFoundError as e:
            error_msg = e
            exit_code = 5
        except SxapiMissingOrgaIDError as e:
            error_msg = e
            exit_code = 6
        except SxapiCliArgumentError as e:
            error_msg = e
            exit_code = 7
        except HTTPError as e:
            error_msg = e
            exit_code = 98
        except Exception as e:
            error_msg = e
            exit_code = 99

        if error_msg:
            print(error_msg)

        exit(exit_code)

    return wrapper


class Cli:
    """CLI class for handling arguments and calling the API."""

    sx_main_parser = SxApiMainParser(subparsers=True)

    @handle_cli_return_values
    def run(self):
        """Call sxapi functions based on passed arguments."""

        return self.sx_main_parser.parse_args(sys.argv[1:])


def cli_run():
    """Start CLI"""
    Cli().run()


if __name__ == "__main__":
    cli_run()
