class AnimalGroups:
    """
    This Class represents the /animalgroups endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/animalgroups"

    def post(self, name, location, organisation_id, **kwargs):
        """Create a new animal group.

        Args:
            name (str): Name of the animal group
            location (str): Location of the animal group
            organisation_id (str): ID of the organisation the animal group
                should be created for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal group on success,
                error message else.

        """
        params = {
            "name": name,
            "location": location,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def put(self, group_id, name, location, organisation_id, **kwargs):
        """Update an animal group.

        Args:
            group_id (str): ID of the animal group
            name (str): Name of the animal group
            location (str): Location of the animal group
            organisation_id (str): ID of the organisation the animal group
                should be updated for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal group on success,
                error message else.

        """
        params = {
            "name": name,
            "location": location,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}"
        return self.api.put(url_suffix, json=params)

    def get(self, group_id, **kwargs):
        """Get one animal group by ID.

        Args:
            group_id (str): ID of the desired animal group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal group on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}"
        return self.api.get(url_suffix, json=params)

    def delete(self, group_id, **kwargs):
        """Delete an animal group.

        Args:
            group_id (str): ID of the animal group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Result on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}"
        return self.api.delete(url_suffix, json=params)
