import mock
import pytest
from requests import HTTPError

from sxapi.cli.parser import main_parser
from sxapi.errors import (
    SxapiAuthorizationError,
    SxapiCliArgumentError,
)

test_parser = main_parser.SxApiMainParser(True)
args_parser = test_parser.parse_args


class MockHTTPError(HTTPError):
    def __str__(self):
        return "401"


@mock.patch("builtins.print")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token", return_value="api_token")
def test_handle_print_token(_, print_mock):
    namespace = args_parser(["token", "-p"])
    assert namespace.print_token == "ek"
    assert print_mock.call_count == 1
    call_args = print_mock.call_args_list[0]
    assert call_args.args[0] == "\nKeyring: None\n\nEnvironment: None"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "ek"])
    assert namespace.print_token == "ek"
    assert print_mock.call_count == 1
    call_args = print_mock.call_args_list[0]
    assert call_args.args[0] == "\nKeyring: None\n\nEnvironment: None"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "k"])
    assert namespace.print_token == "k"
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "\nKeyring Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "e"])
    assert namespace.print_token == "e"
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "\nEnvironment Token: None\n"
    print_mock.reset_mock()

    with pytest.raises(SxapiCliArgumentError) as e:
        args_parser(["token", "-p", "a"])
    assert (
        e.value.message
        == "Invalid arguments. Only use 'e' for environment, 'k' for keyring or 'ek' for both."
    )
    print_mock.reset_mock()

    with pytest.raises(SxapiCliArgumentError) as e:
        args_parser(["token", "-p", "notvalid"])
    assert (
        e.value.message
        == "Invalid number of arguments. Use --help for usage information."
    )
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.cli_user.set_token_keyring", return_value="api_token")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token")
def test_handle_set_token(get_mock, cred_mock, print_mock):
    namespace = args_parser(["token", "-s", "api_token"])
    assert namespace.set_keyring == ["api_token"]
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token is stored in keyring!"
    assert cred_mock.call_count == 1
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.cli_user.clear_token_keyring", return_value="api_token")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token")
def test_handle_clear_token(get_mock, user_mock, print_mock):
    namespace = args_parser(["token", "-c"])
    assert namespace.clear_keyring is True
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token was deleted from keyring!"
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.parser.subparser.token.getpass.getpass", return_value=None)
@mock.patch("sxapi.cli.parser.main_parser.cli_user")
@mock.patch(
    "sxapi.cli.parser.subparser.token.PublicAPIV2.get_token",
    side_effect=MockHTTPError(),
)
def test_handle_new_token(a, user_mock, getpass_mock, print_mock):
    print_mock.reset_mock()

    with mock.patch("builtins.input", lambda _: "marco_no_at_test"):

        with pytest.raises(SxapiCliArgumentError) as e:
            args_parser(["token", "-n"])
        assert e.value.message == "Username must be a email!"
        print_mock.reset_mock()

    with mock.patch("builtins.input", lambda _: "marco@test"):
        with pytest.raises(SxapiAuthorizationError) as e:
            args_parser(["token", "-n"])
        assert e.value.message == "Username or Password is wrong!"
        print_mock.reset_mock()

    with mock.patch("sxapi.publicV2.PublicAPIV2.get_token", return_value="api_token"):
        with mock.patch("builtins.input", lambda _: "marco@test"):
            namespace = args_parser(["token", "-n"])
            assert namespace.new_token is True
            assert getpass_mock.call_count == 2
            call_args = print_mock.call_args_list[0]
            assert print_mock.call_count == 1
            assert call_args.args[0] == "SMAXTEC_API_ACCESS_TOKEN=api_token"
            print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token", return_value="api_token")
def test_token_sub_func(_, print_mock):
    with pytest.raises(SxapiCliArgumentError) as e:
        args_parser(["token", "-c", "-s", "api_token"])

    assert (
        e.value.message
        == "Invalid Combination! Please use just one out of these parameters "
        "[--print_token, --set_keyring, --new_token, --clear_keyring]"
    )
    print_mock.reset_mock()
