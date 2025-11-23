import os

import keyring

from sxapi.integrationV2 import IntegrationAPIV2
from sxapi.publicV2 import PublicAPIV2


class CliUser:
    """
    CliUser class used for initializing, storing, retrieving and deleting
    credentials and creating/holding Instances of supported API
    Client.

    This class should only be used in the cli package.
    """

    def __init__(self):
        """
        Basic User Credentials Constructor

        calls self._init_creds() to set available credentials on startup.
        """
        self.organisation_id = None
        self.api_access_token = None
        self.public_v2_api = None
        self.integration_v2_api = None

    @staticmethod
    def get_token_environment():
        """
        Gets token named 'SMAXTEC_API_ACCESS_TOKEN' from the systems' environment.
        """

        return os.environ.get("SMAXTEC_API_ACCESS_TOKEN", None)

    def set_token_keyring(self, token):
        """
        Store the given token in keyring.
        """
        keyring.set_password("sxapi", "SMAXTEC_API_ACCESS_TOKEN", token)
        self.api_access_token = token

    @staticmethod
    def get_token_keyring():
        """
        Gets the token stored in the keyring.
        """
        return keyring.get_password("sxapi", "SMAXTEC_API_ACCESS_TOKEN")

    @staticmethod
    def clear_token_keyring():
        """
        Deletes the token from the keyring.
        """
        keyring.delete_password("sxapi", "SMAXTEC_API_ACCESS_TOKEN")

    # general functions
    def check_credentials_set(self):
        """
        Checks if token is already set.
        """
        if self.api_access_token is not None:
            return True
        return False

    def init_user(self, config, args_token, args_keyring, args_orga_id):
        """
        This function retrieves the token from the specified resource
        (keyring, environment or args) and initializes clients
        of the supported APIs (PublicV2, IntegrationV2).

        If no token can be found the token is retrieved via
        the username and password.

        If username and password are also missing, no credentials get
        stored and not API clients are created.
        """
        if args_orga_id:
            self.organisation_id = args_orga_id
        elif config.orga:
            self.organisation_id = config.orga

        if args_token:
            self.api_access_token = args_token
        elif args_keyring:
            self.api_access_token = self.get_token_keyring()
            if self.api_access_token is None:
                print("No token found in keyring. Use values from config file.\n")
        else:
            self.api_access_token = self.get_token_environment()

        if self.api_access_token is None and config.user and config.password:
            self.public_v2_api = PublicAPIV2(
                base_url=config.api_public_v2_path,
                email=config.user,
                password=config.password,
            )
            self.integration_v2_api = IntegrationAPIV2(
                base_url=config.api_integration_v2_path,
                email=config.user,
                password=config.password,
            )

            self.api_access_token = self.public_v2_api.get_token()

        elif self.api_access_token:
            self.public_v2_api = PublicAPIV2(
                base_url=config.api_public_v2_path,
                api_token=self.api_access_token,
            )

            self.integration_v2_api = IntegrationAPIV2(
                base_url=config.api_integration_v2_path,
                api_token=self.api_access_token,
            )


cli_user = CliUser()
