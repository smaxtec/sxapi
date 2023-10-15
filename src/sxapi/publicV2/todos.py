class Todos:
    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/todos"

    def post_todos(self, todo_id, organisation_id, **kwargs):
        params = {"organisation_id": organisation_id, "todo_id": todo_id}

        for k, v in kwargs.items():
            params[k] = v

        self.api.post(self.path_suffix, json=params)

    def put_todos(self, todo_id, **kwargs):
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{todo_id}"
        return self.api.put(url_suffix, json=params)

    def get_todos(self, todo_id):
        return self.api.get(self.path_suffix + f"/{todo_id}")

    def post_todos_comment(self, todo_id, content):
        params = {
            "content": content,
        }

        url_suffix = self.path_suffix + f"/{todo_id}/comments"
        return self.api.post(url_suffix, json=params)

    def delete_todos_comment(self, todo_id, comment_id):

        url_suffix = self.path_suffix + f"/{todo_id}/comments/{comment_id}"
        return self.api.delete(url_suffix)

    def put_todos_comment(self, todo_id, comment_id, content):
        params = {
            "content": content,
        }

        url_suffix = self.path_suffix + f"/{todo_id}/comments/{comment_id}"
        return self.api.put(url_suffix, json=params)
