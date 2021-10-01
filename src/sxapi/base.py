#!/usr/bin/python
# coding: utf8

import requests

PUBLIC_API_V2 = "https://api.smaxtec.com/api/v2"
INTEGRATION_API_V2 = "https://api.smaxtec.com/integration/v2"


class BaseAPI(object):
    def __init__(self, base_url, email=None, password=None, api_key=None):
        """Initialize a new base low level API client instance.
        """
        self.api_base_url = base_url.rstrip("/")
        self.email = email
        self.password = password
        self.api_key = api_key
        self._session_key = None
        self._session = None

    @property
    def session(self):
        """
            Geneate a new HTTP session on the fly and login.
        """
        if not self._session:
            self._session = requests.Session()
        # check login
        if not self._login():
            raise ValueError("invalid login information")
        return self._session

    def to_url(self, path):
        return f"{self.api_base_url}{path}"

    def _login(self):
        """
            Login to the api with api key or the given credentials.
        """
        if self.api_key:
            self._session_key = self.api_key
            self._session.headers.update(
                {"Authorization": "Bearer {}".format(self._session_key)})
            return True
        # login with credentials
        if self.email is None or self.password is None:
            raise ValueError("user and password are needed for API access")
        params = {"user": self.email, "password": self.password}

        response = self._session.post(self.to_url("/users/credentials"), params=params)
        self._session_key = response.json()["api_token"]
        self._session.headers.update(
            {"Authorization": "Bearer {}".format(self._session_key)})
        return True

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
