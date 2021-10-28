import mock

from sxapi.cli import cli


@mock.patch("sxapi.cli_sub_parser.get_sensor_data_for_animal", return_value={})
@mock.patch("requests.Session.get")
def test_get_sensor_data_parser(get_call_mock, get_data_mock):
    args_parser = cli.parse_args
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
    assert get_data_mock.call_args[0] == ("12378479238",)
    assert get_data_mock.call_args[1] == {
        "metrics": ["act"],
        "from_date": ["2012-12-12"],
        "to_date": ["2012-12-13"],
    }
