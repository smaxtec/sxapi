#!/usr/bin/python
# coding: utf8

from enum import Enum

import requests


class ApiTypes(Enum):
    PUBLIC = 1
    INTEGRATION = 2


class BaseAPI(object):
    def __init__(
        self,
        base_url,
        email=None,
        password=None,
        api_token=None,
        api_type=None,
    ):
        """Initialize a new base low level API client instance."""
        self.api_base_url = base_url.rstrip("/")
        self.email = email
        self.password = password
        self.api_token = api_token
        self.api_type = api_type
        self._session = None

    def get_token(self):
        if self.api_token is None:
            self.session
        return self.api_token

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
            self._session.headers.update({"Authorization": f"Bearer {self.api_token}"})
        else:
            params = {"user": self.email, "password": self.password}
            response = requests.Response
            if self.api_type == ApiTypes.PUBLIC:
                response = self._session.post(
                    self.to_url("/users/credentials"), params=params
                )
                self.api_token = response.json().get("api_token", None)
            elif self.api_type == ApiTypes.INTEGRATION:
                response = self._session.post(
                    self.to_url("/users/session_token"), params=params
                )
                self.api_token = response.json().get("token", None)
            if self.api_token is None:
                raise requests.HTTPError(response.status_code, response.reason)
            self._session.headers.update({"Authorization": f"Bearer {self.api_token}"})

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
