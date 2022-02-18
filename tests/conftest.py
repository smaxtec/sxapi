"""
    Dummy conftest.py for sxapi.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""
# import pytest
from keyring import backend


# this class prevents the "keyring.errors.NoKeyringError"
class TestKeyring(backend.KeyringBackend):
    """A test keyring which always outputs same password"""

    priority = 1

    def set_password(self, servicename, username, password):
        return "None"

    def get_password(self, servicename, username):
        return "None"

    def delete_password(self, servicename, username):
        return "None"
