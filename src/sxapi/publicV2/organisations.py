class Organisations:
    """
    This Class represents the /todos endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/organisations"

    def post(self, name, timezone, account_id, **kwargs):
        """Create a new organisation.

        https://api.smaxtec.com/api/v2/organisations

        Args:
            name (str): Name of the new organisation
            timezone (str): Timezone of the new organisation
            account_id (str): Account ID of the new organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Organisation on success, error message else.

        """
        params = {"name": name, "timezone": timezone, "account_id": account_id}

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get_settings_hints(self, **kwargs):
        """Get hints for changing the organisation settings.

        https://api.smaxtec.com/api/v2/organisations/settings/hints

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings hints on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + "/settings/hints"
        return self.api.get(url_prefix, json=kwargs)

    def put(self, organisation_id, **kwargs):
        """Update an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}

        Args:
            organisation_id (str): ID of the organisation to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Organisation on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}"
        return self.api.put(url_prefix, json=params)

    def get(self, organisation_id, **kwargs):
        """Get an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}

        Args:
            organisation_id (str): ID of the organisation to be retrieved
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Organisation on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}"
        return self.api.get(url_prefix, json=params)

    def put_add_device(self, organisation_id, device_id, activation_code, **kwargs):
        """Add a device to an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/add_device

        Args:
            organisation_id (str): ID of the organisation the device should be added to
            device_id (str): ID of the device to be added
            activation_code (str): Activation code of the device to be added
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Organisation on success, error message else.

        """
        params = {"device_id": device_id, "activation_code": activation_code}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/add_device"
        return self.api.put(url_prefix, json=params)

    def get_animal_ids(self, organisation_id, **kwargs):
        """Get all animal IDs of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/animal_ids

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of animal IDs on success,
             error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/animal_ids"
        return self.api.get(url_prefix, json=params)

    def get_animals(self, organisation_id, **kwargs):
        """Get all animals of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/animals

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of animals on success,
             error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/animals"
        return self.api.get(url_prefix, json=params)

    def post_import(self, organisation_id, file, **kwargs):
        """Import animals to an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/import

        Args:
            organisation_id (str): ID of the organisation
            file (str): base64 encoded import file
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Nothing on success, error message else.

        """
        params = {"file": file}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/import"
        return self.api.post(url_prefix, json=params)

    def get_import(self, organisation_id, celery_task_id, **kwargs):
        """Get the result of an import.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/import/{celery_task_id}

        Args:
            organisation_id (str): ID of the organisation
            celery_task_id (str): ID of the import task
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Imported animals on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/import/{celery_task_id}"
        return self.api.get(url_prefix, json=params)

    def get_integrations(self, organisation_id, **kwargs):
        """Get information about current and possible
            integrations for the organisations

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. List of integrations on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/integrations"
        return self.api.get(url_prefix, json=params)

    def delete_integrations_icbf(self, organisation_id, **kwargs):
        """Delete all data related to the ICBF integration

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations/icbf

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. List of integrations on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/integrations/icbf"
        return self.api.delete(url_prefix, json=params)

    def delete_integrations_lic(self, organisation_id, **kwargs):
        """Delete all data related to the LIC integration

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations/lic

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. List of integrations on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/integrations/lic"
        return self.api.delete(url_prefix, json=params)

    def delete_integrations_seges(self, organisation_id, **kwargs):
        """Delete all data related to the SEGES integration

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations/seges

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. List of integrations on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/integrations/seges"
        return self.api.delete(url_prefix, json=params)

    def put_integrations(
        self, organisation_id, integration_id, integration_name, **kwargs
    ):
        """Update an integration

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations/{integration_id}

        Args:
            organisation_id (str): ID of the organisation
            integration_id (str): ID of the integration
            integration_name (str): Name of the integration
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Nothing on success,
                error message else.

        """
        params = {"integration_id": integration_id}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = (
            self.path_suffix + f"/{organisation_id}/integrations/{integration_name}"
        )
        return self.api.put(url_prefix, json=params)

    def delete_integrations(
        self, organisation_id, integration_id, integration_name, **kwargs
    ):
        """Delete an integration

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/integrations/{integration_id}

        Args:
            organisation_id (str): ID of the organisation
            integration_id (str): ID of the integration
            integration_name (str): Name of the integration
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Nothing on success,
                error message else.

        """
        params = {"integration_id": integration_id}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = (
            self.path_suffix + f"/{organisation_id}/integrations/{integration_name}"
        )
        return self.api.delete(url_prefix, json=params)

    def get_lists(self, organisation_id, **kwargs):
        """Get all animals lists of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/lists

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             list[dict]: Response of API call. List of animal lists on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/lists"
        return self.api.get(url_prefix, json=params)

    def get_list_by_name(self, organisation_id, list_name, **kwargs):
        """Get an animal list by name of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/lists/{list_name}

        Args:
            organisation_id (str): ID of the organisation
            list_name (str): Name of the list to be retrieved
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Animal list on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/lists/{list_name}"
        return self.api.get(url_prefix, json=params)

    def get_settings(self, organisation_id, **kwargs):
        """Get the settings of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/settings

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/settings"
        return self.api.get(url_prefix, json=params)

    def put_settings(self, organisation_id, setting, **kwargs):
        """Update the settings of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/settings

        Args:
            organisation_id (str): ID of the organisation
            setting (dict): Settings to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings on success,
                error message else.

        """
        params = {"setting": setting}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/settings"
        return self.api.put(url_prefix, json=params)

    def post_settings(self, organisation_id, setting, **kwargs):
        """Override the whole settings of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/settings

        Args:
            organisation_id (str): ID of the organisation
            setting (dict): Settings to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings on success,
                error message else.

        """
        params = {"setting": setting}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/settings"
        return self.api.post(url_prefix, json=params)

    def put_settings_key(self, organisation_id, key, **kwargs):
        """Update the organisation setting at a given key, or
            add if it does not exist yet.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/settings/{key}

        Args:
            organisation_id (str): ID of the organisation
            key (str): Key of the setting to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/settings/{key}"
        return self.api.put(url_prefix, json=params)

    def delete_settings_key(self, organisation_id, key, **kwargs):
        """Delete the given key and its value from the organisation settings.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/settings/{key}

        Args:
            organisation_id (str): ID of the organisation
            key (str): Key of the setting to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Settings on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/settings/{key}"
        return self.api.delete(url_prefix, json=params)

    def get_shares(self, organisation_id, **kwargs):
        """Get all shares of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/shares

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of all shares on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/shares"
        return self.api.get(url_prefix, json=params)

    def get_todos(self, organisation_id, **kwargs):
        """Get all todos of an organisation.

        https://api.smaxtec.com/api/v2/organisations/{organisation_id}/todos

        Args:
            organisation_id (str): ID of the organisation
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/
        Returns:
            list[dict]: Response of API call. List of all todos on success,
                error message else.
        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_prefix = self.path_suffix + f"/{organisation_id}/todos"
        return self.api.get(url_prefix, json=params)
