class SxapiCliArgumentError(Exception):
    """Raised when arguments are valid for argparse
    but make no sense semantically."""

    ARGUMENT_ERROR_MSG = """
    Invalid arguments provided. Please check the help for the correct usage."""

    def __init__(self, message=ARGUMENT_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"


class SxapiAuthorizationError(Exception):
    """Raised when authorization fails 401, 403."""

    AUTHORIZATION_ERROR_MSG = """
    Authorization failed: Access to the requested resource is denied.
    Please check your if your credentials are set and ensure you have the necessary permissions."""

    def __init__(self, message=AUTHORIZATION_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"


class SxapiMissingOrgaIDError(Exception):
    """Raised when no organisation_id can be found"""

    ORGANISATION_ID_ERROR_MSG = """
        No organisation_id was set.
        Provide you organisation_id as env var, as cli parameter or inside the config File"""

    def __init__(self, message=ORGANISATION_ID_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"


class SxapiUnprocessableContentError(Exception):
    """Raised when content is unprocessable 422."""

    UNPROCESSABLE_CONTENT_ERROR_MSG = """
    The request was well-formed but was unable to be followed due to semantic errors."""

    def __init__(self, message=UNPROCESSABLE_CONTENT_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"


class SxapiConfigurationFileError(Exception):
    """Raised when configuration file is not valid."""

    CONFIGURATION_FILE_ERROR_MSG = "Configuration File Error"

    def __init__(self, parent, info=CONFIGURATION_FILE_ERROR_MSG):
        self.parent_name = parent.__class__.__name__
        self.message = parent.message
        self.info = info

    def __str__(self):
        return f"{self.info} -> {self.parent_name} -> {self.message}"


class SxapiInvalidJsonError(Exception):
    """Raised when JSON object is not valid."""

    AUTHORIZATION_ERROR_MSG = """
    Object is not a valid JSON object."""

    def __init__(self, message=AUTHORIZATION_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"


class SxapiFileNotFoundError(Exception):
    """Raised when the path is not valid or the file does not exist."""

    AUTHORIZATION_ERROR_MSG = """
    Given Path is not correct or file does not exist."""

    def __init__(self, message=AUTHORIZATION_ERROR_MSG):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:  {self.message}"
