import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(post_mock):
    test_api = PublicAPIV2()
    test_api.shares.post(
        "test_email",
        "test_organisation_id",
        kwarg1="1",
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/shares"
    assert call_args.kwargs["json"] == {
        "email": "test_email",
        "organisation_id": "test_organisation_id",
        "kwarg1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.shares.get("test_share_id", kwarg1="1", kwarg2="2")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/shares/test_share_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "1",
        "kwarg2": "2",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.shares.put("test_share_id", "test_role", kwarg1="1", kwarg2="2")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/shares/test_share_id"
    assert call_args.kwargs["json"] == {
        "role": "test_role",
        "kwarg1": "1",
        "kwarg2": "2",
    }

    
@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete(delete_mock):
    test_api = PublicAPIV2()
    test_api.shares.delete("test_share_id", kwarg1="1", kwarg2="2")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/shares/test_share_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "1",
        "kwarg2": "2",
    }