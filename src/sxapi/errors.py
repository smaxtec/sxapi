class SxapiAuthorizationError(Exception):
    """Raised when authorization fails 401."""

    AUTHORIZATION_ERROR_MSG = """
    Requested object could not be accessed.
    Maybe the organisation_id or the _id of the requested object is wrong."""

    def __init__(self, message=AUTHORIZATION_ERROR_MSG):
        self.message = message

    def __str__(self):
        return self.message


class SxapiUnprocessableContentError(Exception):
    """Raised when content is unprocessable 422."""

    UNPROCESSABLE_CONTENT_ERROR_MSG = """
    The request was well-formed but was unable to be followed due to semantic errors."""

    def __init__(self, message=UNPROCESSABLE_CONTENT_ERROR_MSG):
        self.message = message

    def __str__(self):
        return self.message


class SxapiConfigurationFileError(Exception):
    """Raised when configuration file is not found."""

    CONFIGURATION_FILE_ERROR_MSG = """
    Configuration file not found.
    Please create a configuration file in one of the following paths:
    /etc/sxapi.conf
    ~/.config/sxapi.conf
    """

    def __init__(self, message, info=CONFIGURATION_FILE_ERROR_MSG):
        self.message = message
        self.info = info

    def __str__(self):
        return self.message + self.info
