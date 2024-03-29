import mock
import pytest

from sxapi.cli.cli import Cli
from sxapi.publicV2 import PublicAPIV2

args_parser = Cli.parse_args


@mock.patch(
    "sxapi.cli.subparser.get_sensor_data.get_sensor_data_from_animal", return_value={}
)
@mock.patch("sxapi.cli.cli_user.check_credentials_set", return_value=True)
@mock.patch("sxapi.cli.cli_user.public_v2_api", PublicAPIV2())
@pytest.mark.skip()
def test_get_sensor_data_parser(creds_mock, get_data_mock):
    namespace = args_parser(
        [
            "get_sensor_data",
            "12378479238",
            "-m",
            "act",
            "--from_date",
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
