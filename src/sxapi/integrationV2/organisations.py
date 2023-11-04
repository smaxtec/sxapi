class Organisations:
    """
    This Class represents the /organisations endpoint for the IntegrationAPIV2
    https://api.smaxtec.com/integration/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/organisations"

    def post(self, name, timezone, **kwargs):
        """Create an organisation.

        Args:
            name (str): Name of the organisation
            timezone (str): Timezone of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Created organisation on success,
                error message else.

        """
        params = {"name": name, "timezone": timezone}

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get(self, **kwargs):
        """Get all organisation the user has access to.

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            list of dicts: Response of API call. List of
                (organisation_Id, organisation_name, user role) on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        return self.api.get(self.path_suffix, json=params)

    def get_odoo_organisations(self, **kwargs):
        """Get all odoo organisations the user has access to.

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of
                (organisation_Id, organisation_name, user role) on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/odoo_organisations"
        return self.api.get(url_suffix, json=params)

    def get_animal_ids(self, organisation_id, **kwargs):
        """Get all animal official_ids of an organisation.

        Args:
            organisation_id (str): Organisation ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of animal ids on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animal_ids"
        return self.api.get(url_suffix, json=params)

    def put_animals(self, organisation_id, body, **kwargs):
        """Create/Update animals of an organisation.

        Args:
            organisation_id (str): Organisation ID of the organisation
            body (:obj:`list` of :obj:`dict`): List of animals to create/update
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of animal ids on success,
                error message else.

        """
        params = {"body": body}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animals"
        return self.api.put(url_suffix, json=params)

    def get_animals(self, organisation_id, **kwargs):
        """Get all animals of an organisation.

        Args:
            organisation_id (str): Organisation ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of animals on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animals"
        return self.api.get(url_suffix, json=params)

    def put_animals_by_official_id(self, organisation_id, official_id, **kwargs):
        """Create/Update an animal of an organisation by official_id.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Nothing on Success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animals/{official_id}"
        return self.api.put(url_suffix, json=params)

    def get_animals_by_official_id(self, organisation_id, official_id, **kwargs):
        """Get an animal of an organisation by official_id.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animals/{official_id}"
        return self.api.get(url_suffix, json=params)

    def get_animals_data_by_official_id(
        self, organisation_id, official_id, metrics, from_date, to_date, **kwargs
    ):
        """Get sensordata of an animal by official_id.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            metrics (str): Metrics of the animal
            from_date (str): From date of the animal
            to_date (str): To date of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Sensor data on success,
                error message else.

        """
        params = {
            "metrics": metrics,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/animals/{official_id}/data.json"
        )
        return self.api.get(url_suffix, json=params)

    def put_animals_events_by_official_id(
        self, organisation_id, official_id, events, **kwargs
    ):
        """Create/Update events of an animal by official_id.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            events (:obj:`list` of :obj:`dict`): List of events to create/update
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Nothing on Success, error message else.

        """
        params = {"events": events}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/animals/{official_id}/events"
        )
        return self.api.put(url_suffix, json=params)

    def get_animals_events_by_official_id(self, organisation_id, official_id, **kwargs):
        """Get events of an animal by official_id.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of animal events on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/animals/{official_id}/events"
        )
        return self.api.get(url_suffix, json=params)

    def get_animals_metrics_by_official_id(
        self, organisation_id, official_id, **kwargs
    ):
        """Get a list of metrics available for animal.

        Args:
            organisation_id (str): Organisation ID of the organisation
            official_id (str): Official ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: List of metrics on Success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/animals/{official_id}/metrics"
        )
        return self.api.get(url_suffix, json=params)

    def put_animals_events(self, organisation_id, events, **kwargs):
        """Create/Update events of an organisation.

        Args:
            organisation_id (str): Organisation ID of the organisation
            events (:obj:`list` of :obj:`dict`): List of events to create/update
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: List of animal events on success, error message else.

        """
        params = {"events": events}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/animals_events"
        return self.api.put(url_suffix, json=params)

    def get_devices(self, organisation_id, **kwargs):
        """Get all devices of an organisation.

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
             dict: Response of API call. List of devices on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/devices"
        return self.api.get(url_suffix, json=params)

    def get_devices_data(
        self, organisation_id, device_id, metrics, from_date, to_date, **kwargs
    ):
        """Get sensordata of a device.

        Args:
            organisation_id (str): ID of the organisation
            device_id (str): ID of the device
            metrics (:obj:`list` of :obj:`str`): Metrics of the device
            from_date (str): From date of the device
            to_date (str): To date of the device
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. Sensor data on success, error message else.

        """
        params = {
            "metrics": metrics,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/devices/{device_id}/data.json"
        )
        return self.api.get(url_suffix, json=params)

    def get_devices_readouts_latest(self, organisation_id, device_id, **kwargs):
        """Get latest readout of a device.

        Args:
            organisation_id (str): ID of the organisation
            device_id (str): ID of the device
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
             dict: Response of API call. Latest readout on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{organisation_id}/devices/{device_id}/readouts/latest"
        )
        return self.api.get(url_suffix, json=params)

    def get_events(self, organisation_id, **kwargs):
        """Get all events of an organisation.

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
             dict: Response of API call. List of events on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/events"
        return self.api.get(url_suffix, json=params)

    def get_simple_animals(self, organisation_id, **kwargs):
        """Get all animals of an organisation.

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
             dict: Response of API call. List of animals on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{organisation_id}/simple_animals"
        return self.api.get(url_suffix, json=params)
