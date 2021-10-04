#!/usr/bin/python
# coding: utf8

import requests

PUBLIC_API_V2 = "https://api.smaxtec.com/api/v2"
INTEGRATION_API_V2 = "https://api.smaxtec.com/integration/v2"


class BaseAPI(object):
    def __init__(self, base_url, email=None, password=None, api_token=None):
        """Initialize a new base low level API client instance.
        """
        self.api_base_url = base_url.rstrip("/")
        self.email = email
        self.password = password
        self.api_token = api_token
        self._session = None

    @property
    def session(self):
        """
            Geneates a new HTTP session on the fly and logs in if no session exists.
        """
        if self._session is None:
            self._session = requests.Session()
        self._login()
        return self._session

    def to_url(self, path):
        return f"{self.api_base_url}{path}"

    def _login(self):
        """
            Login to the api with api key or the given credentials.
        """
        if self.api_token is not None:
            self._session.headers.update(
                {"Authorization": f"Bearer {self.api_token}"})
        else:
            params = {"user": self.email, "password": self.password}
            response = self._session.post(self.to_url("/users/credentials"), params=params)
            self.api_token = response.json()['api_token']
            self._session.headers.update(
                {"Authorization": f"Bearer {self.api_token}"})

    def get(self, path, *args, **kwargs):
        url = self.to_url(path)
        r = self.session.get(url, *args, **kwargs)
        return r.json()

    def post(self, path, *args, **kwargs):
        url = self.to_url(path)
        r = self.session.post(url, *args, allow_redirects=False, **kwargs)
        return r.json()

    def put(self, path, *args, **kwargs):
        url = self.to_url(path)
        r = self.session.put(url, *args, allow_redirects=False, **kwargs)
        return r.json()

    def delete(self, path, *args, **kwargs):
        url = self.to_url(path)
        r = self.session.delete(url, *args, **kwargs)
        return r.json()


class PublicAPIV2(BaseAPI):
    def __init__(self, base_url=None, email=None, password=None, api_token=None):
        """Initialize a new public api client instance.
        """
        base_url = base_url or PUBLIC_API_V2
        super(PublicAPIV2, self).__init__(base_url, email=email,
                                                password=password, api_token=api_token)


class IngtegrationAPIV2(BaseAPI):
    def __init__(self, base_url=None, email=None, password=None, api_token=None):
        """Initialize a new integration client instance.
        """
        base_url = base_url or INTEGRATION_API_V2
        super(PublicAPIV2, self).__init__(base_url, email=email,
                                                password=password, api_token=api_token)
