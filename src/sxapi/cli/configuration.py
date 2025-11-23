import configparser
import os
from os.path import (
    abspath,
    expanduser,
)

from sxapi.errors import (
    SxapiConfigurationFileError,
    SxapiFileNotFoundError,
)


class Config:

    _config_file_paths = ["/etc/sxapi.conf", "~/.config/sxapi.conf"]

    def __init__(self, configfile=None):

        self.user = None
        self.password = None
        self.orga = None
        self.api_public_v2_path = None
        self.api_integration_v2_path = None

        self._read_config_from_file(configfile)
        self._update_config_with_env()

    def to_dict(self):
        return {
            "user": self.user,
            "password": self.password,
            "orga": self.orga,
            "api_public_v2_path": self.api_public_v2_path,
            "api_integration_v2_path": self.api_integration_v2_path,
        }

    def _update_config_with_env(self):
        self.user = os.getenv("SXAPI_USER", self.user)
        self.password = os.getenv("SXAPI_PASSWORD", self.password)
        self.orga = os.getenv("SXAPI_ORGA", self.orga)
        self.api_public_v2_path = os.getenv(
            "SXAPI_API_PUBLIC_V2_PATH", self.api_public_v2_path
        )
        self.api_integration_v2_path = os.getenv(
            "SXAPI_API_INTEGRATION_V2_PATH", self.api_integration_v2_path
        )

    def _read_config_from_file(self, config_file_path):
        if config_file_path:
            if not os.path.isfile(config_file_path):
                raise SxapiFileNotFoundError(
                    f"Config file {config_file_path} does not exist."
                )
            self._config_file_paths.append(config_file_path)

        parsable_files = []
        for config_file in self._config_file_paths:
            config_file = expanduser(config_file)
            config_file = abspath(config_file)
            parsable_files.append(config_file)

        config = configparser.ConfigParser(interpolation=None)

        # if no configfile was read return empty config_dict
        if len(config.read(parsable_files)) == 0:
            return self

        try:
            self.user = config.get("SXAPI", "USER")
            self.password = config.get("SXAPI", "PASSWORD")
            self.orga = config.get("SXAPI", "ORGA")
            self.api_public_v2_path = config.get("SXAPI", "API_PUBLIC_V2_PATH")
            self.api_integration_v2_path = config.get(
                "SXAPI", "API_INTEGRATION_V2_PATH"
            )
        except configparser.Error as e:
            raise SxapiConfigurationFileError(e)

        return self
