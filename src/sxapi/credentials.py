import keyring
import os

class UserCredentials():
    """Credentials class using the keyring lib to store retrive and delete credentials"""

    def __init__(self):
        self.attributes = ["username", "password", "token"]
        self.SMAXTEC_USER = os.getenv("SMAXTEC_USER")
        self.SMAXTEC_PWD = os.getenv("SMAXTEC_PWD")
        self.SMAXTEC_TOKEN = os.getenv("SMAXTEC_TOKEN")
        self.set(username=self.SMAXTEC_USER, password=self.SMAXTEC_PWD, token=self.SMAXTEC_TOKEN)

    def set(self, **kwargs):
        for key, value in kwargs.items():
            if value:
                keyring.set_password("sxapi", key, value)

    def get(self):
        res = {}
        for key in self.attributes:
            res[key] = keyring.get_password("sxapi", key)
        return res

    def clean(self):
        for key in self.attributes:
            try:
                keyring.delete_password("sxapi", key)
            except keyring.errors.PasswordDeleteError:
                continue
