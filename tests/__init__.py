from requests import Response

from sxapi.base import check_response
from sxapi.cli import CliUser
from sxapi.cli.cli import Cli
from sxapi.cli.configuration import Config
from sxapi.cli.parser.main_parser import SxApiMainParser
from sxapi.integrationV2 import IntegrationAPIV2
from sxapi.publicV2 import PublicAPIV2


class SxMainTestParser(SxApiMainParser):
    def __init__(self, subparsers=True):
        self.config = Config(configfile="./tests/cli_tests/test-config.conf")

        super().__init__(subparsers=subparsers)


class CliTest(Cli):
    sx_main_parser = SxMainTestParser(subparsers=True)


class ResponseMock(Response):
    """
    Object to mock a response object from the requests library.
    """

    def __init__(self, value, status_code, exception=None, iterator=False):
        """
        Initialize a new response object.

        Args:
            value (Any): Desired return value of the response object.
            status_code (int): Desired status code of the response object.
            exception (Exception): Desired exception to be raised by the response object.
            iterator (bool): If value is an iterator and mocked call is performed several types
                set this to True in order to get the next value of the iterator on each call.
        """

        super().__init__()

        self.value = value
        self.status_code = status_code
        self.exception = exception
        self.iterator = iterator

    def json(self, **kwargs):
        """
        Mock the json method of the response object.
        """
        return self.value


class _APIMock:
    """
    Base Mock object for the API classes.
    """

    def __init__(self):
        super().__init__()

        self.get_iterator = None
        self.post_iterator = None
        self.put_iterator = None
        self.delete_iterator = None

        self.get_return_value = None
        self.post_return_value = None
        self.put_return_value = None
        self.delete_return_value = None

        self.get_called_with = []
        self.post_called_with = []
        self.put_called_with = []
        self.delete_called_with = []

    def mock_get_return_value(self, return_value):
        """
        Set the return value of the mock object.
        Args:
            return_value:

        Returns:

        """
        if not isinstance(return_value, ResponseMock):
            raise ValueError("return_value is not of type ResponseMock")

        self.get_return_value = return_value

        if return_value.iterator:
            self.get_iterator = iter(self.get_return_value.value)

    def mock_post_return_value(self, return_value):
        """
        Set the return value of the mock object.
        Args:
            return_value:

        Returns:

        """
        if not isinstance(return_value, ResponseMock):
            raise ValueError("return_value is not of type ResponseMock")

        self.post_return_value = return_value

        if return_value.iterator:
            self.post_iterator = iter(self.post_return_value.value)

    def mock_put_return_value(self, return_value):
        """
        Set the return value of the mock object.
        Args:
            return_value:

        Returns:

        """
        if not isinstance(return_value, ResponseMock):
            raise ValueError("return_value is not of type ResponseMock")

        self.put_return_value = return_value

        if return_value.iterator:
            self.put_iterator = iter(self.put_return_value.value)

    def mock_delete_return_value(self, return_value):
        """
        Set the return value of the mock object.
        Args:
            return_value:

        Returns:

        """
        if not isinstance(return_value, ResponseMock):
            raise ValueError("return_value is not of type ResponseMock")

        self.delete_return_value = return_value

        if return_value.iterator:
            self.delete_iterator = iter(self.delete_return_value.value)

    def reset_mock(self, get=False, post=False, put=False, delete=False):

        # if nothing is set reset all
        if not get and not post and not put and not delete:
            get = post = put = delete = True

        if get:
            self.get_return_value = []
            self.get_called_with = []
        if post:
            self.post_return_value = []
            self.post_called_with = []
        if put:
            self.put_return_value = []
            self.put_called_with = []
        if delete:
            self.delete_return_value = []
            self.delete_called_with = []

    @check_response
    def get(self, path, *args, **kwargs):
        self.get_called_with.append({"path": path, "kwargs": kwargs})

        if self.get_return_value.exception:
            raise self.get_return_value.exception

        if self.get_iterator:
            self.get_return_value.value = next(self.get_iterator)

        return self.get_return_value

    @check_response
    def post(self, path, *args, **kwargs):
        self.post_called_with.append({"path": path, "kwargs": kwargs})

        if self.post_return_value.exception:
            raise self.post_return_value.exception

        if self.post_iterator:
            self.post_return_value.value = next(self.post_iterator)

        return self.post_return_value

    @check_response
    def put(self, path, *args, **kwargs):
        self.put_called_with.append({"path": path, "kwargs": kwargs})

        if self.put_return_value.exception:
            raise self.put_return_value.exception

        if self.put_iterator:
            self.put_return_value.value = next(self.put_iterator)

        return self.put_return_value

    @check_response
    def delete(self, path, *args, **kwargs):
        self.delete_called_with.append({"path": path, "kwargs": kwargs})

        if self.delete_return_value.exception:
            raise self.delete_return_value.exception

        if self.delete_iterator:
            self.delete_return_value.value = next(self.delete_iterator)

        return self.delete_return_value


class PublicAPIV2Test(_APIMock, PublicAPIV2):
    def __init__(self):
        super().__init__()


class IntegrationAPIV2Test(_APIMock, IntegrationAPIV2):
    def __init__(self):
        super().__init__()


class CliUserTest(CliUser):
    def __init__(self):
        super().__init__()

        self.organisation_id = "test_organisation_id"
        self.api_access_token = "test_api_token"
        self.public_v2_api = PublicAPIV2Test()
        self.integration_v2_api = IntegrationAPIV2Test()

    def check_credentials_set(self):
        return True

    def init_user(self, config, args_token, args_keyring, args_orga_id):
        pass
