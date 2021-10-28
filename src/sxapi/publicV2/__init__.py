import os

from sxapi.base import PublicAPIV2

token = os.environ.get("SMAXTEC_TOKEN")
user_email = os.environ.get("SMAXTEC_USER")
user_password = os.environ.get("SMAXTEC_PASSWORD")

public_api = PublicAPIV2(email=user_email, password=user_password, api_token=token)
