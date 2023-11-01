class ObservationGroups:
    """
    This Class represents the /observation_groups endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/observation_groups"

    def post(self, name, group_type, start_date, organisation_id, **kwargs):
        """Create a new observation group.

        Args:
            name (str): Name of the observation group.
            group_type (str): Type of the observation group.
            start_date (str): Start date of the observation group.
            organisation_id (str):  ID of the organisation the observation group
                should be created for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Observation group on success,
                error message else.

        """
        params = {
            "name": name,
            "group_type": group_type,
            "start_date": start_date,
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get_dim_series_line(self, reference_type, reference_id, **kwargs):
        """Get aggregated DIM line chart data for an organisation.

        Args:
            reference_type (str): Observation group reference type.
            reference_id (str): ID of Observation group.
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Aggregated DIM Series on success,
                error message else.

        """
        params = {
            "reference_type": reference_type,
            "reference_id": reference_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/dim_series_line.json"
        return self.api.get(url_suffix, json=params)

    def put(self, group_id, **kwargs):
        """Update an observation group.

        Args:
            group_id (str): ID of the observation group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Observation group on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}"
        return self.api.put(url_suffix, json=params)

    def get(self, group_id, **kwargs):
        """Get one observation group by ID.

        Args:
            group_id (str): ID of the observation group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Observation group on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}"
        return self.api.get(url_suffix, json=params)

    def delete(self, group_id, **kwargs):
        """Delete an observation group.

        Args:
            group_id (str): ID of the observation group
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

    def put_add_animals(self, group_id, animal_ids, **kwargs):
        """Add animals to an observation group.

        Args:
            group_id (str): ID of the observation group
            animal_ids (:obj:`list` of :obj:`str`): List of animal IDs
                to add to the group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Observation group on success,
                error message else.

        """
        params = {"animal_ids": animal_ids}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}/add_animals"
        return self.api.put(url_suffix, json=params)

    def put_remove_animals(self, group_id, animal_ids, **kwargs):
        """Remove animals from an observation group.

        Args:
            group_id (str): ID of the observation group
            animal_ids (:obj:`list` of :obj:`str`): List of animal IDs
                to remove from the group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Observation group on success,
                error message else.

        """
        params = {"animal_ids": animal_ids}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{group_id}/remove_animals"
        return self.api.put(url_suffix, json=params)

    def get_observ_dim_series_bar(self, observation_group_id, **kwargs):
        """Get aggregated DIM bar char data for an observation group.

        Args:
            observation_group_id (str): ID of the observation group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Aggregated DIM Series on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{observation_group_id}/observ_dim_series_bar.json"
        )
        return self.api.get(url_suffix, json=params)

    def get_orga_dim_series_bar(self, organisation_id, **kwargs):
        """Get aggregated DIM bar char data for an organisation.

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Aggregated DIM Series on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/orga_dim_series_bar.json"
        return self.api.get(url_suffix, json=params)
