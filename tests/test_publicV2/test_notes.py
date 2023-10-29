import mock

from sxapi.publicV2 import PublicAPIV2

@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post(post_mock):
    test_api = PublicAPIV2()
    test_api.notes.post(
        "test_source",
        "test_reference_type",
        "test_reference_id",
        "test_category",
        "test_note_event",
        kwarg1="kwarg1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/notes"
    assert call_args.kwargs["json"] == {
        "source": "test_source",
        "reference_type": "test_reference_type",
        "reference_id": "test_reference_id",
        "category": "test_category",
        "note_event": "test_note_event",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get(get_mock):
    test_api = PublicAPIV2()
    test_api.notes.get("test_note_id", kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/notes/test_note_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.put")
def test_put(put_mock):
    test_api = PublicAPIV2()
    test_api.notes.put(
        "test_note_id",
        "test_source",
        "test_reference_type",
        "test_reference_id",
        "test_category",
        "test_note_event",
        kwarg1="kwarg1"
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/notes/test_note_id"
    assert call_args.kwargs["json"] == {
        "source": "test_source",
        "reference_type": "test_reference_type",
        "reference_id": "test_reference_id",
        "category": "test_category",
        "note_event": "test_note_event",
        "kwarg1": "kwarg1",
    }