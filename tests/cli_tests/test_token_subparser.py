import mock

from sxapi.cli.cli import Cli
from sxapi.cli.subparser.token import (
    handle_clear_token,
    handle_new_token,
    handle_print_token,
    handle_set_token,
)

args_parser = Cli.parse_args


@mock.patch("builtins.print")
@mock.patch("sxapi.base.PublicAPIV2.get_token", return_value="api_token")
def test_handle_print_token(api_mock, print_mock):
    namespace = args_parser(["token", "-p"])
    assert namespace.print_token == "ek"
    handle_print_token(namespace)
    assert print_mock.call_count == 1
    call_args = print_mock.call_args_list[0]
    assert call_args.args[0] == "\nKeyring: None\n\nEnvironment: None"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "ek"])
    assert namespace.print_token == "ek"
    handle_print_token(namespace)
    assert print_mock.call_count == 1
    call_args = print_mock.call_args_list[0]
    assert call_args.args[0] == "\nKeyring: None\n\nEnvironment: None"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "k"])
    assert namespace.print_token == "k"
    handle_print_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "\nKeyring Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "e"])
    assert namespace.print_token == "e"
    handle_print_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "\nEnvironment Token: None\n"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "a"])
    assert namespace.print_token == "a"
    handle_print_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0] == "Invalid arguments. Only use 'e' for environment, "
        "'k' for keyring or 'ek' for both."
    )
    print_mock.reset_mock()

    namespace = args_parser(["token", "-p", "notvalid"])
    assert namespace.print_token == "notvalid"
    handle_print_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0]
        == "Invalid number of arguments. Use --help for usage information."
    )
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.cli_user.set_token_keyring", return_value="api_token")
def test_handle_set_token(cred_mock, print_mock):
    namespace = args_parser(["token", "-s", "api_token"])
    assert namespace.set_keyring == ["api_token"]
    handle_set_token(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token is stored in keyring!"
    assert cred_mock.call_count == 1
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.cli_user.clear_token_keyring", return_value="api_token")
def test_handle_clear_token(creds_mock, print_mock):
    namespace = args_parser(["token", "-c"])
    assert namespace.clear_keyring is True
    handle_clear_token()
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Token was deleted from keyring!"
    print_mock.reset_mock()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.subparser.token.getpass.getpass", return_value=None)
@mock.patch("sxapi.cli.cli_user")
def test_handle_new_token(creds_mock, getpass_mock, print_mock):
    print_mock.reset_mock()

    namespace = args_parser(["token", "-n", "no_at"])
    assert namespace.new_token == ["no_at"]
    handle_new_token(namespace)
    assert getpass_mock.call_count == 1
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Username must be a email!"
    print_mock.reset_mock()

    namespace = args_parser(["token", "-n", "marco@test"])
    assert namespace.new_token == ["marco@test"]
    handle_new_token(namespace)
    assert getpass_mock.call_count == 2
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "Username or Password is wrong!"
    print_mock.reset_mock()

    with mock.patch("sxapi.base.PublicAPIV2.get_token", return_value="api_token"):
        namespace = args_parser(["token", "-n", "marco@test", "pwd"])
        assert namespace.new_token == ["marco@test", "pwd"]
        handle_new_token(namespace)
        assert getpass_mock.call_count == 2
        call_args = print_mock.call_args_list[0]
        assert print_mock.call_count == 1
        assert call_args.args[0] == "SMAXTEC_API_ACCESS_TOKEN=api_token"
        print_mock.reset_mock()


@mock.patch("builtins.print")
def test_token_subfunc(print_mock):
    namespace = args_parser(["token", "-c", "-s", "api_token"])

    namespace.func(namespace)
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert (
        call_args.args[0]
        == "Invalid Combination! Please use just one out of these parameters "
        "[--print_token, --set_keyring, --new_token, --clear_keyring]"
    )
    print_mock.reset_mock()
