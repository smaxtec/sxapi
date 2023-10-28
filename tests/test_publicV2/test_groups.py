import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_actions(put_mock):
    test_api = PublicAPIV2()
    test_api.groups.put_actions("test_group_id", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/groups/test_group_id/actions"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_actions(get_mock):
    test_api = PublicAPIV2()
    test_api.groups.get_actions("test_group_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/groups/test_group_id/actions"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_actions(delete_mock):
    test_api = PublicAPIV2()
    test_api.groups.delete_actions("test_group_id", "test_action_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/groups/test_group_id/actions/test_action_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}
