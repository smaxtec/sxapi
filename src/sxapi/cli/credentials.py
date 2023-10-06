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

    @staticmethod
    def get_token_environment():
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

    @staticmethod
    def get_token_keyring():
        """
        Gets the token stored in the keyring.
        """
        return keyring.get_password("sxapi", "SMAXTEC_TOKEN")

    @staticmethod
    def clear_token_keyring():
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
