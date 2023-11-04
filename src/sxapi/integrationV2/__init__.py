from sxapi.base import (
    ApiTypes,
    BaseAPI,
)
from sxapi.integrationV2.accounts import Accounts
from sxapi.integrationV2.organisations import Organisations
from sxapi.integrationV2.tranlations import Translations
from sxapi.integrationV2.users import Users

INTEGRATION_API_V2_BASE_URL = "https://api.smaxtec.com/integration/v2"


class IntegrationAPIV2(BaseAPI):
    def __init__(self, base_url=None, email=None, password=None, api_token=None):
        """Initialize a new integration api client instance."""
        base_url = base_url or INTEGRATION_API_V2_BASE_URL
        api_type = ApiTypes.INTEGRATION

        self.users = Users(api=self)
        self.translations = Translations(api=self)
        self.accounts = Accounts(api=self)
        self.organisations = Organisations(api=self)

        super().__init__(
            base_url,
            email=email,
            password=password,
            api_token=api_token,
            api_type=api_type,
        )
