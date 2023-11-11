class Groups:
    """
    This Class represents the /groups endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/groups"

    def put_actions(self, group_id, **kwargs):
        """Add an action to a group.

        https://api.smaxtec.com/api/v2/groups/{group_id}/actions

        Args:
            group_id (str): ID of the group which should be updated.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated group on success, error message else.
        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}/actions"
        self.api.put(url_suffix, json=params)

    def get_actions(self, group_id, **kwargs):
        """Get all actions of a group.

         https://api.smaxtec.com/api/v2/groups/{group_id}/actions

        Args:
            group_id (str): ID of the group which should be updated.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated group on success, error message else.
        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}/actions"
        return self.api.get(url_suffix, json=params)

    def delete_actions(self, group_id, action_id, **kwargs):
        """Delete an action from a group.

         https://api.smaxtec.com/api/v2/groups/{group_id}/actions/{action_id}

        Args:
            group_id (str): ID of the group which should be updated.
            action_id (str): ID of the action which should be deleted.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Result on success, error message else.
        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}/actions/{action_id}"
        return self.api.delete(url_suffix, json=params)
