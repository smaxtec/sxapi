import mock

from sxapi.cli import user_credentials
from sxapi.cli.cli import Cli

cli = Cli()


@mock.patch("sxapi.cli.cli.Cli.version_info")
@mock.patch("builtins.print")
@mock.patch(
    "sxapi.cli.user_credentials.get_token_keyring", return_value="keyring-token"
)
def test_func(keyring_mock, print_mock, version_mock):
    with mock.patch("sys.argv", ["sx_api", "--version"]):
        assert version_mock.call_count == 0
        cli.run()
        assert version_mock.call_count == 1
    print_mock.reset_mock()

    with mock.patch("sys.argv", ["sx_api", "-k", "-t", "test"]):
        cli.run()
        call_args = print_mock.call_args_list[0]
        assert (
            call_args.args[0]
            == "Choose either -k (keyring), -t (argument) or no flag (environment)!"
        )
        print_mock.reset_mock()

    with mock.patch("sys.argv", ["sx_api", "-k"]):
        cli.run()
        assert user_credentials.token == "keyring-token"

    with mock.patch("sys.argv", ["sx_api", "-t", "args_token"]):
        cli.run()
        assert user_credentials.token == "args_token"
