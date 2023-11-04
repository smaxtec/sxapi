class Accounts:
    """
    This Class represents the /accounts endpoint fo the IntegrationAPIV2
    https://api.smaxtec.com/integration/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/accounts"

    def get_usages(self, **kwargs):
        """Get usages of provided account numbers.

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of usages on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/usages"
        return self.api.get(url_suffix, json=params)

    def put(
        self,
        account_nr,
        account_name,
        partner_id,
        address_name,
        street,
        county_code,
        **kwargs,
    ):
        """Update an account.

        Args:
            account_nr (str): Account number of the account
            account_name (str): Name of the account
            partner_id (str): Partner ID of the account
            address_name (str): Name of the address of the account
            street (str): Street of the address of the account
            county_code (str): Country code of the address of the account
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Updated account on success,
                error message else.

        """
        params = {
            "account_name": account_name,
            "partner_id": partner_id,
            "address_name": address_name,
            "street": street,
            "county_code": county_code,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{account_nr}"
        return self.api.put(url_suffix, json=params)

    def put_organisation(self, account_nr, organisation_id, **kwargs):
        """Add an account to an organisation.

        Args:
            account_nr (str): Account number of the account
            organisation_id (str): Organisation ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Result on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{account_nr}/organisation/{organisation_id}"
        return self.api.put(url_suffix, json=params)
