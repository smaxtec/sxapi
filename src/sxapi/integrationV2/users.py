class Users:
    """
    This Class represents the /users endpoint fo the IntegrationAPIV2
    https://api.smaxtec.com/integration/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/users"

    def get(self, **kwargs):
        """Grant access to demo farm

        https://api.smaxtec.com/integration/v2/users

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Demo farm User on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        return self.api.get(self.path_suffix, json=params)

    def post_session_token(self, user, password, **kwargs):
        """Creates a new session token.

        https://api.smaxtec.com/integration/v2/users/session_token

        Args:
            user (str): Email of the user to be logged in
            password (str): Password of the user to be logged in
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Created session token on success,
                error message else.

        """
        params = {"user": user, "password": password}

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix + "/session_token", json=params)
