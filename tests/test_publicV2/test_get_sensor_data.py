import datetime

import mock

from sxapi.integrationV2 import IntegrationAPIV2
from sxapi.publicV2 import PublicAPIV2
from sxapi.publicV2.sensordata import get_sensor_data_from_animal


@mock.patch("builtins.print")
@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_sensor_data(get_mock, print_mock):
    get_sensor_data_from_animal(IntegrationAPIV2(), "animal_id")
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "This function is only available to PublicAPIV2!"
    print_mock.reset_mock()

    get_sensor_data_from_animal(
        PublicAPIV2(), "1233455", metrics="act", to_date=["21-12-2"]
    )
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "to_date has not the right format YYYY-MM-DD!"
    print_mock.reset_mock()

    get_sensor_data_from_animal(
        PublicAPIV2(),
        "1233455",
        metrics="act",
        to_date=["2001-12-2"],
        from_date=["0334"],
    )
    call_args = print_mock.call_args_list[0]
    assert print_mock.call_count == 1
    assert call_args.args[0] == "from_date has not the right format YYYY-MM-DD!"
    print_mock.reset_mock()

    get_sensor_data_from_animal(
        PublicAPIV2(),
        "1233455",
        metrics="act",
        to_date=["2001-12-02"],
        from_date=["2001-11-02"],
    )

    get_mock.assert_called_once_with(
        "/data/animals/1233455.json",
        json={
            "metrics": "act",
            "from_date": datetime.datetime(2001, 11, 2, 0, 0).isoformat(),
            "to_date": datetime.datetime(2001, 12, 2, 0, 0).isoformat(),
        },
    )
