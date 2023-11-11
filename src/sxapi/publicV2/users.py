class Users:
    """
    This Class represents the /users endpoint fo the PublicAPIV2
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/users"

    def post_activate(self, user_secret, **kwargs):
        """Active a user with secret.

        https://api.smaxtec.com/api/v2/users/activate

        Args:
            user_secret (str): secrete received from registration email.

        Returns:
            dict: Response of API call. Activated User on success, error message else.
        """

        params = {"secret": user_secret}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/activate"
        return self.api.post(url_suffix, json=params)

    def post_credentials(self, user, password, **kwargs):
        """Create smaxtec api-access-token and an optional firestore-token.

        https://api.smaxtec.com/api/v2/users/credentials

        Args:
            user (str): Username/email
            password (str): User password
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Requested tokens and additional user
            information on success, error message else.
        """

        params = {
            "user": user,
            "password": password,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/credentials"
        return self.api.post(url_suffix, json=params)

    def get_credentials(self, **kwargs):
        """Retrieve smaxtec api-access-tokens with a JWT Token.

        https://api.smaxtec.com/api/v2/users/credentials

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Current tokens and additional user
            information on success, error message else.
        """

        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/credentials"
        return self.api.get(url_suffix, json=params)

    def post_reset_password(self, secret, new_password, **kwargs):
        """Reset password with secret.

        https://api.smaxtec.com/api/v2/users/reset_password

        Args:
            secret (str): secret received from email request.
            new_password (str): new password for the user.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated User on success, error message else.
        """

        params = {"secret": secret, "new_password": new_password}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/reset_password"
        return self.api.post(url_suffix, json=params)

    def get_reset_password_request(self, email, **kwargs):
        """Request a password reset email.

        https://api.smaxtec.com/api/v2/users/reset_password_request

        Args:
            email (str): email of the user.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Request result on success, error message else.
        """

        params = {"email": email}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/reset_password_request"
        return self.api.get(url_suffix, json=params)

    def get(self, user_id, **kwargs):
        """Get one user by id.

        https://api.smaxtec.com/api/v2/users/{user_id}

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. User object on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}"
        return self.api.get(url_suffix, json=params)

    def get_account(self, user_id, **kwargs):
        """Get a list of all Accounts of the given user

        https://api.smaxtec.com/api/v2/users/{user_id}/account

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of Account objects on success,
             error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/account"
        return self.api.get(url_suffix, json=params)

    def get_alarms(self, user_id, **kwargs):
        """Get a list of all Alarms of the given user

        https://api.smaxtec.com/api/v2/users/{user_id}/alarms

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of Alarm objects on success,
             error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/alarms"
        return self.api.get(url_suffix, json=params)

    def put_change_password(self, user_id, old_password, new_password, **kwargs):
        """Change password of a user with old password.

        https://api.smaxtec.com/api/v2/users/{user_id}/change_password

        Args:
            user_id (str): ID of the desired user
            old_password (str): old password of the user
            new_password (str): new password of the user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Request result on success, error message else.

        """
        params = {
            "old_password": old_password,
            "new_password": new_password,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/change_password"
        return self.api.put(url_suffix, json=params)

    def post_password_strength(self, user_id, email, password, **kwargs):
        """Check password strength.

        https://api.smaxtec.com/api/v2/users/{user_id}/password_strength

        Args:
            user_id (str): ID of the desired user
            email (str): email of the user
            password (str): password to check
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Request result and password strength on success,
             error message else.

        """
        params = {
            "password": password,
            "email": email,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/password_strength"
        return self.api.post(url_suffix, json=params)

    def get_shares(self, user_id, **kwargs):
        """Get a list of all Shares of the given user

        https://api.smaxtec.com/api/v2/users/{user_id}/shares

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of Share objects on success,
             error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/shares"
        return self.api.get(url_suffix, json=params)

    def post_test_email(self, user_id, **kwargs):
        """Send a test email to the user.

        https://api.smaxtec.com/api/v2/users/{user_id}/test_email

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Empty dict on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/test_email"
        return self.api.post(url_suffix, json=params)

    def post_test_push(self, user_id, **kwargs):
        """Send a test push notification to the user.

        https://api.smaxtec.com/api/v2/users/{user_id}/test_push

        Args:
            user_id (str): ID of the desired user
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Empty dict on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/test_push"
        return self.api.post(url_suffix, json=params)

    def put_tokens(self, user_id, token, platform, token_type, **kwargs):
        """Adds the token if it does not exist, else updates the token.

        Args:
            user_id (str): ID of the desired user
            token (str): some kind of token
            platform (str): platform of the token device
            token_type (str): type of the token (add push_ if push token)
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Request result on success, error message else.

        """
        params = {
            "token": token,
            "platform": platform,
            "token_type": token_type,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/tokens"
        return self.api.put(url_suffix, json=params)

    def post_tokens(self, user_id, token, platform, token_type, **kwargs):
        """Adds the token to the user.

        https://api.smaxtec.com/api/v2/users/{user_id}/tokens

        Args:
            user_id (str): ID of the desired user
            token (str): some kind of token
            platform (str): platform of the token device
            token_type (str): type of the token (add push_ if push token)
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Request result on success, error message else.

        """
        params = {
            "token": token,
            "platform": platform,
            "token_type": token_type,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/tokens"
        return self.api.post(url_suffix, json=params)

    def delete_tokens(self, user_id, token, **kwargs):
        """Deletes the token from the user.

        https://api.smaxtec.com/api/v2/users/{user_id}/tokens/{token}

        Args:
            user_id (str): ID of the desired user
            token (str): token to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Request result on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/tokens/{token}"
        return self.api.delete(url_suffix, json=params)

    def post_update_metadata(self, user_id, metadata, **kwargs):
        """Update metadata of a user.

        https://api.smaxtec.com/api/v2/users/{user_id}/update_metadata

        Args:
            user_id (str): ID of the desired user
            metadata (dict): updated metadata
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Updated user on success, error message else.

        """
        params = {
            "metadata": metadata,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{user_id}/update_metadata"
        return self.api.post(url_suffix, json=params)
