import mock

from sxapi.publicV2 import PublicAPIV2

@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.events.get("test_organisation_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/events"
    assert call_args.kwargs["json"] == {
        "organisation_id": "test_organisation_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_by_id(get_mock):
    test_api = PublicAPIV2()
    test_api.events.get_by_id("test_event_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/events/by_id"
    assert call_args.kwargs["json"] == {
        "event_id": "test_event_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_categories(get_mock):
    test_api = PublicAPIV2()
    test_api.events.get_categories(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/events/categories"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }