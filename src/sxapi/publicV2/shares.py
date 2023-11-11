class Shares:
    """
    Class for interacting with the notes endpoint of the public V2 API
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/shares"

    def post(self, email, organisation_id, **kwargs):
        """Create a new share.

         https://api.smaxtec.com/api/v2/shares

        Args:
            email (str): Email of the user to share
            organisation_id (str): ID of the organisation to share
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Share on success,
                error message else.

        """
        params = {
            "email": email,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get(self, share_id, **kwargs):
        """Get one share.

        https://api.smaxtec.com/api/v2/shares/{share_id}

        Args:
            share_id (str): ID of the desired share
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Share on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{share_id}"
        return self.api.get(url_suffix, json=params)

    def put(self, share_id, role, **kwargs):
        """Update one share.

        https://api.smaxtec.com/api/v2/shares/{share_id}

        Args:
            share_id (str): ID of the desired share
            role (str): Role of the share
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Share on success,
                error message else.

        """
        params = {
            "role": role,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{share_id}"
        return self.api.put(url_suffix, json=params)

    def delete(self, share_id, **kwargs):
        """Delete one share.

        https://api.smaxtec.com/api/v2/shares/{share_id}

        Args:
            share_id (str): ID of the desired share
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Result on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{share_id}"
        return self.api.delete(url_suffix, json=params)
