import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(post_mock):
    test_api = PublicAPIV2()
    test_api.organisations.post(
        "test_orga", "Europe/Malta", "test_account_id", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/organisations"
    assert call_args.kwargs["json"] == {
        "name": "test_orga",
        "timezone": "Europe/Malta",
        "account_id": "test_account_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_settings_hints(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_settings_hints(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/settings/hints"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.organisations.put("test_orga_id", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_add_device(put_mock):
    test_api = PublicAPIV2()
    test_api.organisations.put_add_device(
        "test_orga_id", "test_device_id", "test_activation_code", kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/add_device"
    assert call_args.kwargs["json"] == {
        "device_id": "test_device_id",
        "activation_code": "test_activation_code",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_animal_ids(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_animal_ids("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/animal_ids"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_animals(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_animals("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/animals"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_import(post_mock):
    test_api = PublicAPIV2()
    test_api.organisations.post_import("test_orga_id", "test_file", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/import"
    assert call_args.kwargs["json"] == {"file": "test_file", "kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_import(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_import("test_orga_id", "test_task_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/import/test_task_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_integrations(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_integrations("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/integrations"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_integrations_icbf(delete_mock):
    test_api = PublicAPIV2()
    test_api.organisations.delete_integrations_icbf("test_orga_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/integrations/icbf"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_integrations_lic(delete_mock):
    test_api = PublicAPIV2()
    test_api.organisations.delete_integrations_lic("test_orga_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/integrations/lic"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_integrations_seges(delete_mock):
    test_api = PublicAPIV2()
    test_api.organisations.delete_integrations_seges("test_orga_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/integrations/seges"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_integrations(delete_mock):
    test_api = PublicAPIV2()
    test_api.organisations.delete_integrations(
        "test_orga_id", "test_integration_id", "test_integration_name", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_orga_id/integrations/test_integration_name"
    )
    assert call_args.kwargs["json"] == {
        "integration_id": "test_integration_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_integrations(put_mock):
    test_api = PublicAPIV2()
    test_api.organisations.put_integrations(
        "test_orga_id", "test_integration_id", "test_integration_name", kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/organisations/test_orga_id/integrations/test_integration_name"
    )
    assert call_args.kwargs["json"] == {
        "integration_id": "test_integration_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_lists(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_lists("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/lists"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_list_by_name(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_list_by_name(
        "test_orga_id", "test_list_name", kwarg1="kwarg1"
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/lists/test_list_name"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_settings(put_mock):
    test_api = PublicAPIV2()
    test_api.organisations.put_settings(
        "test_orga_id", {"test": "settings"}, kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/settings"
    assert call_args.kwargs["json"] == {
        "setting": {"test": "settings"},
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_settings(post_mock):
    test_api = PublicAPIV2()
    test_api.organisations.post_settings(
        "test_orga_id", {"test": "settings"}, kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/settings"
    assert call_args.kwargs["json"] == {
        "setting": {"test": "settings"},
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_settings(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_settings("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/settings"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_settings_key(delete_mock):
    test_api = PublicAPIV2()
    test_api.organisations.delete_settings_key(
        "test_orga_id", "test_key", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/settings/test_key"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_settings_key(put_mock):
    test_api = PublicAPIV2()
    test_api.organisations.put_settings_key("test_orga_id", "test_key", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/settings/test_key"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_shares(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_shares("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/shares"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_todos(get_mock):
    test_api = PublicAPIV2()
    test_api.organisations.get_todos("test_orga_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/organisations/test_orga_id/todos"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}
