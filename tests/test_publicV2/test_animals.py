import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post("test_organisatin_id", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals"
    assert call_args.kwargs["json"] == {
        "organisation_id": "test_organisatin_id",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_by_ids(get_mock):
    test_api = PublicAPIV2()
    test_api.animals.get_by_ids(["test_id1", "test_id2"], kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/animals/by_ids"
    assert call_args.kwargs["json"] == {
        "animal_ids": ["test_id1", "test_id2"],
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_by_official_id(get_mock):
    test_api = PublicAPIV2()
    test_api.animals.get_by_official_id(
        "test_orga_id", "test_official_id", kwarg1="kwarg1"
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/animals/by_official_id/test_orga_id/test_official_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.animals.get("test_animal_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put("test_animal_id", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_aborts(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_aborts(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/aborts"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_aborts(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_aborts(
        "test_animal_id", "2022-01-01T10:10+00:00", "test_abort_id", kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/aborts/test_abort_id"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_aborts(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_aborts("test_animal_id", "test_abort_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/aborts/test_abort_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_calving_confirmations(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_calving_confirmations(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/calving_confirmations"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_calving_confirmations(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_calving_confirmations(
        "test_animal_id",
        "test_calving_confirmation_id",
        "2022-01-01T10:10+00:00",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/calving_confirmations/test_calving_confirmation_id"
    )
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_calving_confirmations(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_calving_confirmations(
        "test_animal_id", "test_calving_confirmation_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/calving_confirmations/test_calving_confirmation_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_diagnosis(get_mock):
    test_api = PublicAPIV2()
    test_api.animals.get_diagnosis("test_animal_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/diagnosis"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_diagnosis(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_diagnosis(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/diagnosis"
    assert call_args.kwargs["json"] == {
        "diagnosis_date": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_diagnosis(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_diagnosis(
        "test_animal_id",
        "test_diagnosis_id",
        "2022-01-01T10:10+00:00",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/diagnosis/test_diagnosis_id"
    assert call_args.kwargs["json"] == {
        "diagnosis_date": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_diagnosis(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_diagnosis(
        "test_animal_id", "test_diagnosis_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/diagnosis/test_diagnosis_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_dry_offs(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_dry_offs(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/dry_offs"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_dry_offs(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_dry_offs("test_animal_id", "test_dry_off_id", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/dry_offs/test_dry_off_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_dry_offs(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_dry_offs(
        "test_animal_id", "test_dry_off_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/dry_offs/test_dry_off_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_events_false_positive(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_events_false_positive(
        "test_animal_id", "test_event_id", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/events/test_event_id/false_positive"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_heats(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_heats(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/heats"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_heats(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_heats("test_animal_id", "test_heat_id", kwarg1="kwarg1")

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/heats/test_heat_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_heats(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_heats("test_animal_id", "test_heat_id", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/heats/test_heat_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_inseminations(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_inseminations(
        "test_animal_id", "2022-01-01T10:10+00:00", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/inseminations"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_inseminations(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_inseminations(
        "test_animal_id", "test_insemination_id", kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/inseminations/test_insemination_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_inseminations(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_inseminations(
        "test_animal_id", "test_insemination_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/inseminations/test_insemination_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_no_inseminations(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_no_inseminations(
        "test_animal_id", "2022-01-01T10:10+00:00", "test_reason", kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/no_inseminations"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "reason": "test_reason",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_no_inseminations(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_no_inseminations(
        "test_animal_id", "test_no_insemination_id", kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/no_inseminations/test_no_insemination_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_no_inseminations(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_no_inseminations(
        "test_animal_id", "test_no_insemination_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/no_inseminations/test_no_insemination_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_pregnancy_results(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_pregnancy_results(
        "test_animal_id", "2022-01-01T10:10+00:00", True, kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/pregnancy_results"
    assert call_args.kwargs["json"] == {
        "event_ts": "2022-01-01T10:10+00:00",
        "pregnant": True,
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put_pregnancy_results(put_mock):
    test_api = PublicAPIV2()
    test_api.animals.put_pregnancy_results(
        "test_animal_id", "test_pregnancy_result_id", False, kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/pregnancy_results/test_pregnancy_result_id"
    )
    assert call_args.kwargs["json"] == {
        "pregnant": False,
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_pregnancy_results(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_pregnancy_results(
        "test_animal_id", "test_pregnancy_result_id", kwarg1="kwarg1"
    )

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/animals/test_animal_id/pregnancy_results/test_pregnancy_result_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_tags(get_mock):
    test_api = PublicAPIV2()
    test_api.animals.get_tags("test_animal_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/tags"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_tags(post_mock):
    test_api = PublicAPIV2()
    test_api.animals.post_tags("test_animal_id", "test_tag", kwarg1="kwarg1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/tags"
    assert call_args.kwargs["json"] == {
        "tag": "test_tag",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.delete")
def test_delete_tags(delete_mock):
    test_api = PublicAPIV2()
    test_api.animals.delete_tags("test_animal_id", "test_tag", kwarg1="kwarg1")

    call_args = delete_mock.call_args_list[0]

    assert delete_mock.call_count == 1
    assert call_args.args[0] == "/animals/test_animal_id/tags"
    assert call_args.kwargs["json"] == {
        "tag": "test_tag",
        "kwarg1": "kwarg1",
    }
