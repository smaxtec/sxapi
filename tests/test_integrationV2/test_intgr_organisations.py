import mock

from sxapi.integrationV2 import IntegrationAPIV2


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.post")
def test_post(post_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.post("test_name", "test_timezone", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/organisations"
    assert call_args.kwargs["json"] == {
        "name": "test_name",
        "timezone": "test_timezone",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_odoo_organisations(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_odoo_organisations(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/odoo_organisations"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animal_ids(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animal_ids("test_organisation_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/animal_ids"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put_animals(put_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.put_animals(
        "test_organisation_id",
        [
            {"animal_id": "test_animal_id", "animal_name": "test_animal_name"},
            {"animal_id": "test_animal_id2", "animal_name": "test_animal_name2"},
        ],
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/animals"
    assert call_args.kwargs["json"] == {
        "body": [
            {"animal_id": "test_animal_id", "animal_name": "test_animal_name"},
            {"animal_id": "test_animal_id2", "animal_name": "test_animal_name2"},
        ],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animals(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animals("test_organisation_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/animals"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put_animals_by_official_id(put_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.put_animals_by_official_id(
        "test_organisation_id",
        "test_official_id",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animals_by_official_id(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animals_by_official_id(
        "test_organisation_id",
        "test_official_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animals_data_by_official_id(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animals_data_by_official_id(
        "test_organisation_id",
        "test_official_id",
        ["metric1", "metric2"],
        "10-10-2020",
        "10-11-2020",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id/data.json"
    )
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "10-10-2020",
        "to_date": "10-11-2020",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put_animals_events_by_official_id(put_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.put_animals_events_by_official_id(
        "test_organisation_id",
        "test_official_id",
        [
            {
                "event_type": "test_event_type",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value",
            },
            {
                "event_type": "test_event_type2",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value2",
            },
        ],
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id/events"
    )
    assert call_args.kwargs["json"] == {
        "events": [
            {
                "event_type": "test_event_type",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value",
            },
            {
                "event_type": "test_event_type2",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value2",
            },
        ],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animals_events_by_official_id(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animals_events_by_official_id(
        "test_organisation_id",
        "test_official_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id/events"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_animals_metrics_by_official_id(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_animals_metrics_by_official_id(
        "test_organisation_id",
        "test_official_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/animals/test_official_id/metrics"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put_animals_events(put_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.put_animals_events(
        "test_organisation_id",
        [
            {
                "event_type": "test_event_type",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value",
            },
            {
                "event_type": "test_event_type2",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value2",
            },
        ],
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/animals_events"
    assert call_args.kwargs["json"] == {
        "events": [
            {
                "event_type": "test_event_type",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value",
            },
            {
                "event_type": "test_event_type2",
                "event_datetime": "10-10-2020",
                "event_value": "test_event_value2",
            },
        ],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_devices(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_devices("test_organisation_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/devices"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_devices_data(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_devices_data(
        "test_organisation_id",
        "test_device_id",
        ["metric1", "metric2"],
        "10-10-2020",
        "10-11-2020",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/devices/test_device_id/data.json"
    )
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "10-10-2020",
        "to_date": "10-11-2020",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_devices_readouts_latest(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_devices_readouts_latest(
        "test_organisation_id",
        "test_device_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_organisation_id/devices/test_device_id/readouts/latest"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_events(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_events(
        "test_organisation_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/events"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_simple_animals(get_mock):
    test_api = IntegrationAPIV2()
    test_api.organisations.get_simple_animals(
        "test_organisation_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_organisation_id/simple_animals"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }
