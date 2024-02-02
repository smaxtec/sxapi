class SxapiAuthorizationError(Exception):
    """Raised when authorization fails 401."""

    AUTHORIZATION_ERROR_MSG = """
    Requested object could not be accessed.
    Maybe the organisation_id or the _id of the requested object is wrong.
    """

    def __init__(self, message=AUTHORIZATION_ERROR_MSG, status_code=None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        text = self.message
        if self.status_code:
            text = text + "status code: " + str(self.status_code)

        return text


class SxapiUnprocessableContentError(Exception):
    """Raised when content is unprocessable 422."""

    UNPROCESSABLE_CONTENT_ERROR_MSG = """
    The request was well-formed but was unable to be followed due to semantic errors.
    """

    def __init__(self, message=UNPROCESSABLE_CONTENT_ERROR_MSG, status_code=None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        text = self.message
        if self.status_code:
            text = text + "status code: " + str(self.status_code)

        return text


class SxapiConfigurationFileError(Exception):
    """Raised when configuration file is not valid."""

    CONFIGURATION_FILE_ERROR_MSG = "Configuration File Error"

    def __init__(self, parent, info=CONFIGURATION_FILE_ERROR_MSG):
        self.parent_name = parent.__class__.__name__
        self.message = parent.message
        self.info = info

    def __str__(self):
        return self.info + " -> " + self.parent_name + " -> " + self.message
