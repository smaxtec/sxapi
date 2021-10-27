import os

from sxapi.base import PublicAPIV2

token = os.environ.get("SMAXTEC_TOKEN")
user_email = "marco.moser@smaxtec.com"
user_password = "L3d3nitz3n%13"

public_api = PublicAPIV2(email=user_email, password=user_password, api_token=token)
