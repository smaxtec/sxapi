import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_check_activatable(get_mock):
    test_api = PublicAPIV2()
    test_api.devices.get_check_activatable(
        "test_device_id", "test_activation_code", kwarg1="kwarg1"
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/devices/test_device_id/check_activatable"
    assert call_args.kwargs["json"] == {
        "activation_code": "test_activation_code",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_move(put_mock):
    test_api = PublicAPIV2()
    test_api.devices.put_move(
        "test_device_id",
        "test_organisation_id",
        "test_target_organisation_id",
        True,
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/devices/test_device_id/move"
    assert call_args.kwargs["json"] == {
        "organisation_id": "test_organisation_id",
        "target_organisation_id": "test_target_organisation_id",
        "archive": True,
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_update_name(put_mock):
    test_api = PublicAPIV2()
    test_api.devices.put_update_name("test_device_id", "test_name", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/devices/test_device_id/update_name"
    assert call_args.kwargs["json"] == {
        "name": "test_name",
        "kwarg1": "kwarg1",
    }
