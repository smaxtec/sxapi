import mock

from sxapi.integrationV2 import IntegrationAPIV2


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get(get_mock):
    test_api = IntegrationAPIV2()
    test_api.users.get(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.post")
def test_post_session_token(post_mock):
    test_api = IntegrationAPIV2()
    test_api.users.post_session_token("test_user", "test_password", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/session_token"
    assert call_args.kwargs["json"] == {
        "user": "test_user",
        "password": "test_password",
        "kwarg1": "kwarg1",
    }
