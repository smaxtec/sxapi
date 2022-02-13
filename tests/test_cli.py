import keyring
import mock
from keyring import backend

from sxapi.base import PublicAPIV2


# this call needs to create before importing form the cli package
# in order to avoid NoKeyringError()
class TestKeyring(backend.KeyringBackend):
    """A test keyring which always outputs same password"""

    priority = 1

    def set_password(self, servicename, username, password):
        return "None"

    def get_password(self, servicename, username):
        return "None"

    def delete_password(self, servicename, username):
        return "None"


keyring.set_keyring(TestKeyring())

from sxapi.cli.cli import Cli
from sxapi.cli.helper import (
    handle_clear_token,
    handle_get_token,
    handle_set_token,
)

args_parser = Cli.parse_args


@mock.patch("sxapi.cli.cli_sub_parser.get_sensor_data_from_animal", return_value={})
@mock.patch("sxapi.cli.user_credentials.check_credentials_set", return_value=True)
def test_get_sensor_data_parser(creds_mock, get_data_mock):
    namespace = args_parser(
        [
            "get_sensor_data",
            "12378479238",
            "-m",
            "act",
            "-fd",
            "2012-12-12",
            "--to_date",
            "2012-12-13",
        ]
    )
    assert namespace.animal_id == "12378479238"
    assert namespace.metrics == ["act"]
    assert namespace.from_date == ["2012-12-12"]
    assert namespace.to_date == ["2012-12-13"]

    namespace.func(namespace)
    assert get_data_mock.call_count == 1
    call_args = get_data_mock.call_args_list[0].kwargs
    assert len(call_args) == 5
    assert call_args["animal_id"] == "12378479238"
    assert call_args["metrics"] == ["act"]
    assert call_args["from_date"] == ["2012-12-12"]
    assert call_args["to_date"] == ["2012-12-13"]
    assert isinstance(call_args["api"], PublicAPIV2)

    namespace = args_parser(
        [
            "get_sensor_data",
            "23454",
        ]
    )
    assert namespace.animal_id == "23454"

    namespace.func(namespace)
    assert get_data_mock.call_count == 2
    call_args = get_data_mock.call_args_list[1].kwargs
    assert len(call_args) == 5
    assert call_args["animal_id"] == "23454"
    assert call_args["metrics"] is None
    assert call_args["from_date"] is None
    assert call_args["to_date"] is None
    assert isinstance(call_args["api"], PublicAPIV2)


@mock.patch("builtins.print")
@mock.patch("sxapi.base.PublicAPIV2.get_token", return_value="api_token")
def test_handle_get_token(api_mock, print_mock):
    namespace = args_parser(
        [
            "--get_token",
        ]
    )
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Environment Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["--get_token", "-k"])
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Keyring Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["--get_token", "-ek"])
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 2
    assert call_args.args[0] == "Keyring Token: None\n"
    call_args = print_mock.call_args_list[1]
    assert call_args.args[0] == "Environment Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["--get_token", "-nek"])
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "You cant use -k or -e in combination with -n!"
    print_mock.reset_mock()

    namespace = args_parser(["--get_token", "-n"])
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0]
        == "To get new Token please give username <-u> AND password <-p>!"
    )
    print_mock.reset_mock()

    namespace = args_parser(["--get_token", "-n", "-u", "test", "-p", "test"])
    assert namespace.get_token is True
    handle_get_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token: api_token"


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.user_credentials.set_token_keyring", return_value="api_token")
def test_handle_set_token(cred_mock, print_mock):
    namespace = args_parser(
        [
            "--set_token",
            "-e",
        ]
    )
    assert namespace.set_token is True
    assert namespace.environment is True
    handle_set_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0]
        == "This application can only store/delete things in keyring <-k>. "
        "Changes to the environment must be done manually!"
    )
    print_mock.reset_mock()

    namespace = args_parser(
        [
            "--set_token",
            "-k",
        ]
    )
    assert namespace.set_token is True
    assert namespace.keyring is True
    handle_set_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Please specify the token <-t> you want to set!"
    print_mock.reset_mock()

    namespace = args_parser(
        [
            "--set_token",
            "-t",
            "api_token",
        ]
    )
    assert namespace.set_token is True
    assert namespace.keyring is False
    handle_set_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token is stored in keyring!"
    assert cred_mock.call_count == 1
    assert cred_mock.call_args.kwargs["token"] == "api_token"
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.user_credentials.clear_token_keyring", return_value="api_token")
def test_handle_clear_token(creds_mock, print_mock):
    namespace = args_parser(
        [
            "--clear_token",
            "-e",
        ]
    )
    assert namespace.clear_token is True
    assert namespace.environment is True
    handle_clear_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0]
        == "This application can only store/delete things in keyring <-k>. "
        "Changes to the environment must be done manually!"
    )
    print_mock.reset_mock()

    namespace = args_parser(
        [
            "--clear_token",
        ]
    )
    assert namespace.clear_token is True
    handle_clear_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token was deleted from keyring!"
    assert creds_mock.called_once()


def test_credentials():
    pass
