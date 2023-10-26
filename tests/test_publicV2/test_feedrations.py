import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(post_mock):
    test_api = PublicAPIV2()
    test_api.feedrations.post("test_name", "test_organisation_id", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/feedrations"
    assert call_args.kwargs["json"] == {
        "name": "test_name",
        "organisation_id": "test_organisation_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.feedrations.put(
        "test_feedration_id",
        "test_name",
        "test_organisation_id",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/feedrations/test_feedration_id"
    assert call_args.kwargs["json"] == {
        "name": "test_name",
        "organisation_id": "test_organisation_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.feedrations.get("test_feedration_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/feedrations/test_feedration_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete(delete_mock):
    test_api = PublicAPIV2()
    test_api.feedrations.delete("test_feedration_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/feedrations/test_feedration_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}
