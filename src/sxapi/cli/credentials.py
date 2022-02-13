import os

import keyring


class UserCredentials:
    """
    Credentials class used for initializing, storing, retrieving and deleting
    credentials. This class should only be used in the cli package.
    """

    def __init__(self):
        self.token_env_names = "SMAXTEC_TOKEN"
        self.token = None

        self._init_creds()

    def get_token_environment(self):
        """Get token from system environment"""
        return os.environ.get("SMAXTEC_TOKEN", None)

    def set_token_keyring(self, token):
        """Store token in keyring"""
        keyring.set_password("sxapi", "SMAXTEC_TOKEN", token)
        self.token = token

    def get_token_keyring(self):
        """Get token from keyring"""
        return keyring.get_password("sxapi", "SMAXTEC_TOKEN")

    def clear_token_keyring(self):
        """Clears keyring"""
        keyring.delete_password("sxapi", "SMAXTEC_TOKEN")

    # general functions
    def check_credentials_set(self):
        if self.token is not None:
            return True
        return False

    def _init_creds(self):
        """
        On startup try to load credentials from environment,
        if they aren't set, try to load them from keyring
        """
        env_token = self.get_token_environment()
        if env_token is not None:
            self.token = env_token
            return

        keyring_token = self.get_token_keyring()
        if keyring_token is not None:
            self.token = keyring_token
            return
