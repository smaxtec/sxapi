class Todos:
    """
    This Class represents the /todos endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/todos"

    def post(self, todo_type, organisation_id, **kwargs):
        """Creates a new todo.

        Args:
            todo_type (str): Type of the todo to be created
            organisation_id (str): Id of organisation the todo should be created for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Created todo on success, error message else.

        """
        params = {
            "todo_type": todo_type,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        self.api.post(self.path_suffix, json=params)

    def put(self, todo_id, **kwargs):
        """Updates an existing todo.

        Args:
            todo_id (str): Id of the todo which should be updated.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated todo on success, error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{todo_id}"
        return self.api.put(url_suffix, json=params)

    def get(self, todo_id):
        """Get one todo.

        Args:
            todo_id (str): Id of the desired todo

        Returns:
            dict: Response of API call. Queried todo on success, error message else.

        """
        return self.api.get(self.path_suffix + f"/{todo_id}")

    def post_comment(self, todo_id, content):
        """Create a comment for a todo.

        Args:
            todo_id (str): Id of the todo a comment is to be created.
            content (str): Content of the comment

        Returns:
            dict: Response of API call. Updated todo on success, error message else.
        """
        params = {
            "content": content,
        }

        url_suffix = self.path_suffix + f"/{todo_id}/comments"
        return self.api.post(url_suffix, json=params)

    def delete_comment(self, todo_id, comment_id):
        """Delete a comment from a todo.

        Args:
            todo_id (str): Id of the todo a comment is to be deleted.
            comment_id (str): Id of the comment to delete.

        Returns:
            dict: Response of API call. Updated todo on success, error message else.
        """

        url_suffix = self.path_suffix + f"/{todo_id}/comments/{comment_id}"
        return self.api.delete(url_suffix)

    def put_comment(self, todo_id, comment_id, content):
        """Update a comment from a todo.

        Args:
            todo_id (str): Id of the todo a comment is to be updated.
            comment_id (str): Id of the comment to be updated.
            content (str): Updated content of the Id.

        Returns:
            dict: Response of API call. Updated todo on success, error message else.
        """
        params = {
            "content": content,
        }

        url_suffix = self.path_suffix + f"/{todo_id}/comments/{comment_id}"
        return self.api.put(url_suffix, json=params)
