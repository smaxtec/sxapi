import mock

from sxapi.base import PublicAPIV2


@mock.patch("sxapi.base.PublicAPIV2.post")
def test_post_todos(post_mock):
    test_api = PublicAPIV2()
    test_api.todos.post_todos(
        "test_todo_id", "test_orga_id", kwarg1="kwarg1", optional2="optional2"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/todos"
    assert call_args.kwargs["json"] == {
        "todo_id": "test_todo_id",
        "organisation_id": "test_orga_id",
        "kwarg1": "kwarg1",
        "optional2": "optional2",
    }


@mock.patch("sxapi.base.PublicAPIV2.post")
def test_post_todo_comment(post_mock):
    test_api = PublicAPIV2()
    test_api.todos.post_todos_comment("test_todo_id", content="comment_content")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/todos/test_todo_id/comments"
    assert call_args.kwargs["json"] == {
        "content": "comment_content",
    }


@mock.patch("sxapi.base.PublicAPIV2.put")
def test_put_todos(put_mock):
    test_api = PublicAPIV2()
    test_api.todos.put_todos("test_todo_id", kwarg1="1", kwarg2="2", kwarg3=3)

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/todos/test_todo_id"
    assert call_args.kwargs["json"] == {
        "kwarg1": "1",
        "kwarg2": "2",
        "kwarg3": 3,
    }


@mock.patch("sxapi.base.PublicAPIV2.put")
def test_put_todo_comments(get_mock):
    test_api = PublicAPIV2()
    test_api.todos.put_todos_comment(
        "test_todo_id", "test_comment_id", "updated_content"
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/todos/test_todo_id/comments/test_comment_id"
    assert call_args.kwargs["json"] == {"content": "updated_content"}


@mock.patch("sxapi.base.PublicAPIV2.get")
def test_get_todos(get_mock):
    test_api = PublicAPIV2()
    test_api.todos.get_todos("test_todo_id")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/todos/test_todo_id"
    assert call_args.kwargs == {}


@mock.patch("sxapi.base.PublicAPIV2.delete")
def test_delete_todo_comments(get_mock):
    test_api = PublicAPIV2()
    test_api.todos.delete_todos_comment("test_todo_id", "test_comment_id")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/todos/test_todo_id/comments/test_comment_id"
    assert call_args.kwargs == {}
