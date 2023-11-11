class Feedrations:
    """
    This Class represents the /feedrations endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/feedrations"

    def post(self, name, organisation_id, **kwargs):
        """Creates a new feedration.

         https://api.smaxtec.com/api/v2/feedrations

        Args:
            name (str): Name of the feedration to be created
            organisation_id (str): ID of the organisation the feedration
                should be created for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Created feedration on success,
                error message else.

        """
        params = {
            "name": name,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        self.api.post(self.path_suffix, json=params)

    def put(self, feedration_id, name, organisation_id, **kwargs):
        """Updates an existing feedration.

        https://api.smaxtec.com/api/v2/feedrations/{feedration_id}

        Args:
            feedration_id (str): ID of the feedration which should be updated.
            name (str): Name of the feedration to be updated
            organisation_id (str): ID of the organisation the feedration
                should be updated for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated feedration on success,
                error message else.

        """
        params = {
            "name": name,
            "organisation_id": organisation_id,
        }
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{feedration_id}"
        return self.api.put(url_suffix, json=params)

    def get(self, feedration_id, **kwargs):
        """Get one feedration.

        https://api.smaxtec.com/api/v2/feedrations/{feedration_id}

        Args:
            feedration_id (str): ID of the desired feedration
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Feedration on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{feedration_id}"
        return self.api.get(url_suffix, json=params)

    def delete(self, feedration_id, **kwargs):
        """Deletes a feedration.

        https://api.smaxtec.com/api/v2/feedrations/{feedration_id}

        Args:
            feedration_id (str): ID of the feedration which should be deleted.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Result on success, error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{feedration_id}"
        return self.api.delete(url_suffix, json=params)
