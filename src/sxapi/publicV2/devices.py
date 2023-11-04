class Devices:
    """
    This Class represents the /todos endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/devices"

    def get_check_activatable(self, device_id, activation_code, **kwargs):
        """
        Check if a device can be activated with the given activation code.

        Args:
            device_id (str): ID of the device check if activation is possible
            activation_code (str): Devices activation code
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Result on success, error message else.

        """
        params = {"activation_code": activation_code}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{device_id}/check_activatable"
        return self.api.get(url_suffix, json=params)

    def put_move(
        self, device_id, organisation_id, target_organisation_id, archive, **kwargs
    ):
        """
        Move a device to another organisation.

        Args:
            device_id (str): ID of the device to be moved
            organisation_id (str): ID of the organisation the device is currently in
            target_organisation_id (str): ID of the organisation the device
                should be moved to
            archive (bool): If True, the source animal will be archived after moving
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Device on success, error message else.

        """
        params = {
            "organisation_id": organisation_id,
            "target_organisation_id": target_organisation_id,
            "archive": archive,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{device_id}/move"
        return self.api.put(url_suffix, json=params)

    def put_update_name(self, device_id, name, **kwargs):
        """
        Update the name of a device.

        Args:
            device_id (str): ID of the device to be moved
            name (str): New name of the device
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Device on success, error message else.

        """
        params = {"name": name}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{device_id}/update_name"
        return self.api.put(url_suffix, json=params)
