import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(mock_post):
    test_api = PublicAPIV2()
    test_api.observation_groups.post(
        "test_name",
        "test_group_type",
        "test_start_date",
        "test_organisation_id",
        kwarg1="kwarg1",
    )

    call_args = mock_post.call_args_list[0]

    assert mock_post.call_count == 1
    assert call_args.args[0] == "/observation_groups"
    assert call_args.kwargs["json"] == {
        "name": "test_name",
        "group_type": "test_group_type",
        "start_date": "test_start_date",
        "organisation_id": "test_organisation_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_dim_series_line(get_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.get_dim_series_line(
        "test_reference_type",
        "test_reference_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/dim_series_line.json"
    assert call_args.kwargs["json"] == {
        "reference_type": "test_reference_type",
        "reference_id": "test_reference_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.put(
        "test_group_id",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/test_group_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.get(
        "test_group_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/test_group_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete(delete_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.delete(
        "test_group_id",
        kwarg1="kwarg1",
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/test_group_id"
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_add_animals(put_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.put_add_animals(
        "test_group_id",
        ["test_animal_id1", "tet_animal_id2"],
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/test_group_id/add_animals"
    assert call_args.kwargs["json"] == {
        "animal_ids": ["test_animal_id1", "tet_animal_id2"],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_remove_animals(put_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.put_remove_animals(
        "test_group_id",
        ["test_animal_id1", "tet_animal_id2"],
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/observation_groups/test_group_id/remove_animals"
    assert call_args.kwargs["json"] == {
        "animal_ids": ["test_animal_id1", "tet_animal_id2"],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_observ_dim_series_bar(get_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.get_observ_dim_series_bar(
        "test_group_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/observation_groups/test_group_id/observ_dim_series_bar.json"
    )
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_orga_dim_series_bar(get_mock):
    test_api = PublicAPIV2()
    test_api.observation_groups.get_orga_dim_series_bar(
        "test_orga_id",
        kwarg1="kwarg1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert (
        call_args.args[0] == "/observation_groups/test_orga_id/orga_dim_series_bar.json"
    )
    assert call_args.kwargs["json"] == {"kwarg1": "kwarg1"}
