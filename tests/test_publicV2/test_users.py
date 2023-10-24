import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_activate(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_activate("test_user_secret", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/activate"
    assert call_args.kwargs["json"] == {
        "secret": "test_user_secret",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_credentials(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_credentials("test_user", "test_password", firestore=True)

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/credentials"
    assert call_args.kwargs["json"] == {
        "user": "test_user",
        "password": "test_password",
        "firestore": True,
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_credentials(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get_credentials(firestore=True, support=True)

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/credentials"
    assert call_args.kwargs["json"] == {"firestore": True, "support": True}


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_reset_password(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_reset_password(
        secret="test_secret", new_password="new_test_password", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/reset_password"
    assert call_args.kwargs["json"] == {
        "secret": "test_secret",
        "new_password": "new_test_password",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_reset_password_request(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get_reset_password_request(email="test_user_email", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/reset_password_request"
    assert call_args.kwargs["json"] == {"email": "test_user_email", "kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get("test_user_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_account(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get_account("test_user_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/account"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_alarms(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get_alarms("test_user_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/alarms"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_change_password(put_mock):
    test_api = PublicAPIV2()
    test_api.users.put_change_password(
        "test_user_id",
        "test_old_password",
        "test_new_password",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/change_password"
    assert call_args.kwargs["json"] == {
        "old_password": "test_old_password",
        "new_password": "test_new_password",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_password_strength(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_password_strength(
        "test_user_id", "test_email", "test_password", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/password_strength"
    assert call_args.kwargs["json"] == {
        "email": "test_email",
        "password": "test_password",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_shares(get_mock):
    test_api = PublicAPIV2()
    test_api.users.get_shares("test_user_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/shares"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_test_email(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_test_email("test_user_id", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/test_email"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_test_push(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_test_push("test_user_id", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/test_push"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_tokens(put_mock):
    test_api = PublicAPIV2()
    test_api.users.put_tokens(
        user_id="test_user_id",
        token="test_token",
        platform="test_platform",
        token_type="test_token_type",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/tokens"
    assert call_args.kwargs["json"] == {
        "token": "test_token",
        "platform": "test_platform",
        "token_type": "test_token_type",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_tokens(post_mock):
    test_api = PublicAPIV2()
    test_api.users.post_tokens(
        user_id="test_user_id",
        token="test_token",
        platform="test_platform",
        token_type="test_token_type",
        kwarg1="kwarg1",
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/tokens"
    assert call_args.kwargs["json"] == {
        "token": "test_token",
        "platform": "test_platform",
        "token_type": "test_token_type",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_tokens(delete_mock):
    test_api = PublicAPIV2()
    test_api.users.delete_tokens("test_user_id", "test_token", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/tokens/test_token"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_update_metadata(post_mock):
    test_api = PublicAPIV2()

    new_metadata = {
        "key1": "value1",
        "key2": "value2",
        "key3": 3,
    }

    test_api.users.post_update_metadata("test_user_id", new_metadata, kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/users/test_user_id/update_metadata"
    assert call_args.kwargs["json"] == {"metadata": new_metadata, "kwarg1": "kwarg1"}
