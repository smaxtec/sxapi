import mock

from sxapi.integrationV2 import IntegrationAPIV2


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_events(get_mock):
    test_api = IntegrationAPIV2()
    test_api.translations.get_events("en", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/translations/en/events"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_event_types(get_mock):
    test_api = IntegrationAPIV2()
    test_api.translations.get_event_types("en", "test_event_type", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/translations/en/events/test_event_type"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }
