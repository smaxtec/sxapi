import os

import mock

from sxapi.cli import (
    cli_user,
    configuration,
)
from tests import CliTest

obj = mock.MagicMock

ConfigTest = configuration.Config


@mock.patch("sxapi.cli.parser.main_parser.version_info")
@mock.patch("builtins.print")
@mock.patch("sxapi.cli.cli_user.get_token_keyring", return_value="keyring-token")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token", return_value="keyring-token")
def test_func(get_token_mock, keyring_mock, print_mock, version_mock):
    cli = CliTest()
    with mock.patch("sys.argv", ["sxapi", "--version"]):
        assert version_mock.call_count == 0
        CliTest().run()
        assert version_mock.call_count == 1
    print_mock.reset_mock()

    with mock.patch("sys.argv", ["sxapi", "-k", "-t", "test"]):
        cli.run()
        call_args = print_mock.call_args_list[0]
        assert (
            call_args.args[0] == "Choose either -k (keyring), -t (argument)"
            " or no flag (environment/config)!"
        )
        print_mock.reset_mock()

    with mock.patch("sys.argv", ["sxapi", "-k"]):
        cli.run()
        assert cli_user.api_access_token == "keyring-token"

    with mock.patch("sys.argv", ["sxapi", "-t", "args_token"]):
        cli.run()
        assert cli_user.api_access_token == "args_token"


@mock.patch("sxapi.cli.parser.main_parser.version_info")
@mock.patch("sxapi.cli.cli_user.get_token_keyring", return_value="keyring-token")
def test_config(keyring_mock, version_mock):
    # test config file default
    cli = CliTest()
    ConfigTest._config_file_paths = ["./tests/cli_tests/test-config.conf"]
    cli.sx_main_parser.config = ConfigTest()
    with mock.patch("sys.argv", ["sxapi", "--version"]):
        with mock.patch("sxapi.cli.cli_user.init_user") as iu_mock:
            cli.run()
            res = iu_mock.call_args_list[0][0][0]

            assert res.user == "test@example.com"
            assert res.password == "smaxtec_test_user_pwd"
            assert res.orga == "smaxtec_test_organisation_id"
            assert res.api_public_v2_path == "https://test_path_test"
            assert res.api_integration_v2_path == "https://test_path_integration"

    # test config_file_path override
    with mock.patch(
        "sys.argv",
        ["sxapi", "--version", "-c", "./tests/cli_tests/test-config_param.conf"],
    ):
        with mock.patch("sxapi.cli.cli_user.init_user") as iu_mock:
            cli.run()
            res = iu_mock.call_args_list[0][0][0]

            assert res.user == "test2@example.com"
            assert res.password == "smaxtec_test2_user_pwd"
            assert res.orga == "smaxtec_test2_organisation_id"
            assert res.api_public_v2_path == "test2_path_test"
            assert res.api_integration_v2_path == "test2_path_integration"

    # test override with env_vars
    os.environ["SXAPI_USER"] = "testenv@example.com"
    os.path.abspath("")
    with mock.patch(
        "sys.argv",
        ["sxapi", "--version", "-c", "./tests/cli_tests/test-config_param.conf"],
    ):
        with mock.patch("sxapi.cli.cli_user.init_user") as iu_mock:
            cli.run()
            res = iu_mock.call_args_list[0][0][0]

            assert res.user == "testenv@example.com"
            assert res.password == "smaxtec_test2_user_pwd"
            assert res.orga == "smaxtec_test2_organisation_id"
            assert res.api_public_v2_path == "test2_path_test"
            assert res.api_integration_v2_path == "test2_path_integration"


@mock.patch("sxapi.cli.parser.main_parser.version_info")
@mock.patch("sxapi.cli.cli_user.get_token_keyring", return_value="keyring-token")
@mock.patch("sxapi.publicV2.PublicAPIV2.get_token", return_value="api-token")
def test_init_user(api_mock, k_mock, version_mock):
    cli = CliTest()
    with mock.patch(
        "sys.argv",
        [
            "sxapi",
            "--version",
            "-c",
            "./tests/cli_tests/test-config_param.conf",
            "-t",
            "atoken",
        ],
    ):
        cli.run()
        assert cli_user.api_access_token == "atoken"
        assert cli_user.public_v2_api and cli_user.integration_v2_api
        cli_user.public_v2_api = cli_user.integration_v2_api = None

    with mock.patch(
        "sys.argv",
        ["sxapi", "--version", "-c", "./tests/cli_tests/test-config_param.conf", "-k"],
    ):
        cli.run()
        assert cli_user.api_access_token == "keyring-token"
        assert cli_user.public_v2_api and cli_user.integration_v2_api
        cli_user.public_v2_api = cli_user.integration_v2_api = None

    with mock.patch(
        "sys.argv",
        ["sxapi", "--version", "-c", "./tests/cli_tests/test-config_param.conf"],
    ):
        os.environ["SMAXTEC_API_ACCESS_TOKEN"] = "env_token"
        cli.run()
        assert cli_user.api_access_token == "env_token"
        assert cli_user.public_v2_api and cli_user.integration_v2_api
        os.environ.pop("SMAXTEC_API_ACCESS_TOKEN")
        cli_user.public_v2_api = cli_user.integration_v2_api = None

    with mock.patch(
        "sys.argv",
        ["sxapi", "--version", "-c", "./tests/cli_tests/test-config_param.conf"],
    ):
        cli.run()
        assert cli_user.api_access_token == "api-token"
        assert cli_user.public_v2_api and cli_user.integration_v2_api
        cli_user.public_v2_api = cli_user.integration_v2_api = None
