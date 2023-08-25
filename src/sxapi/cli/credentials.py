import os

import keyring


class UserCredentials:
    """
    Credentials class used for initializing, storing, retrieving and deleting
    credentials.

    This class should only be used in the cli_tests package.
    """

    def __init__(self):
        """
        Basic User Credentials Constructor

        calls self._init_creds() to set available credentials on startup.
        """

        self.token_env_names = "SMAXTEC_TOKEN"
        self.token = None

        self._init_creds()

    def get_token_environment(self):
        """
        Gets token named 'SMAXTEC_TOKEN' from the systems environment.
        """

        return os.environ.get("SMAXTEC_TOKEN", None)

    def set_token_keyring(self, token):
        """
        Store the given token in keyring.
        """
        keyring.set_password("sxapi", "SMAXTEC_TOKEN", token)
        self.token = token

    def get_token_keyring(self):
        """
        Gets the token stored in the keyring.
        """
        return keyring.get_password("sxapi", "SMAXTEC_TOKEN")

    def clear_token_keyring(self):
        """
        Deletes the token from the keyring.
        """
        keyring.delete_password("sxapi", "SMAXTEC_TOKEN")

    # general functions
    def check_credentials_set(self):
        """
        Checks if token is already set.
        """
        if self.token is not None:
            return True
        return False

    def _init_creds(self):
        """
        This function tries to get the token from the system environment and
        stores it in self.token, on failure (no token found) it does the same
        with the keyring.

        If both sources fail self.token remains None.
        """
        env_token = self.get_token_environment()
        if env_token is not None:
            self.token = env_token
            return

        keyring_token = self.get_token_keyring()
        if keyring_token is not None:
            self.token = keyring_token
            return
