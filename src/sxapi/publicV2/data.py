class Data:
    """
    This Class represents the /data endpoint fo the PublicAPIV2
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/data"

    def get_data_animals(self, animal_id, metrics, from_date, to_date, **kwargs):
        """Query sensordata for an animal.

        https://api.smaxtec.com/api/v2/data/animals/{animal_id}.json

        Args:
            animal_id (str): ID of the animal
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {"metrics": metrics, "from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/animals/{animal_id}.json"
        return self.api.get(url_suffix, json=params)

    def get_metrics_animals(self, animal_id, **kwargs):
        """List available metrics for an animal.

        https://api.smaxtec.com/api/v2/data/animals/{animal_id}/metrics

        Args:
            animal_id (str): ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response from the API.  List of available metrics on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/animals/{animal_id}/metrics"
        self.api.get(url_suffix, json=params)

    def get_data_devices(self, device_id, metrics, from_date, to_date, **kwargs):
        """Query sensordata for a device.

        https://api.smaxtec.com/api/v2/data/devices/{device_id}.json

        Args:
            device_id (str): ID of the device
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {"metrics": metrics, "from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/devices/{device_id}.json"
        return self.api.get(url_suffix, json=params)

    def get_metrics_devices(self, device_id, **kwargs):
        """List available metrics for a device.

        https://api.smaxtec.com/api/v2/data/devices/{device_id}/metrics

        Args:
            device_id (str): ID of the device
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response from the API.  List of available metrics on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/devices/{device_id}/metrics"
        return self.api.get(url_suffix, json=params)

    def get_download_animal_data(
        self, animal_ids, metrics, from_date, to_date, **kwargs
    ):
        """Download sensordata for animals.

        https://api.smaxtec.com/api/v2/data/download_animal_data

        Args:
            animal_ids (list(str)): List of animal IDs
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {
            "animal_ids": animal_ids,
            "metrics": metrics,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/download_animal_data"
        return self.api.get(url_suffix, json=params)

    def get_download_device_data(
        self, device_ids, metrics, from_date, to_date, **kwargs
    ):
        """Download sensordata for devices.

        https://api.smaxtec.com/api/v2/data/download_device_data

        Args:
            device_ids (list(str)): List of device IDs
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {
            "device_ids": device_ids,
            "metrics": metrics,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/download_device_data"
        return self.api.get(url_suffix, json=params)

    def get_download_group_data(self, group_ids, metrics, from_date, to_date, **kwargs):
        """Download sensordata for groups.

        https://api.smaxtec.com/api/v2/data/download_group_data

        Args:
            group_ids (list(str)): List of group IDs
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {
            "group_ids": group_ids,
            "metrics": metrics,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/download_group_data"
        return self.api.get(url_suffix, json=params)

    def post_downloads_excel_report(self, from_date, to_date, **kwargs):
        """Generates an Excel report and sends an email
        containing a download link for the Excel report to the user.

        https://api.smaxtec.com/api/v2/data/downloads/generate_excel_report

        Args:
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Empty dict on success, error message else.

        """
        params = {"from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/downloads/generate_excel_report"
        return self.api.post(url_suffix, json=params)

    def post_downloads_messages_excel_report(self, from_date, to_date, **kwargs):
        """Generates an Excel report and sends an email
        containing a download link for the Excel report to the user.

        https://api.smaxtec.com/api/v2/data/downloads/generate_messages_excel_report

        Args:
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Empty dict on success, error message else.

        """
        params = {"from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/downloads/generate_messages_excel_report"
        return self.api.post(url_suffix, json=params)

    def post_downloads_organisation_messages_excel_report(
        self, organisation_id, from_date, to_date, **kwargs
    ):
        """Generates an Excel report and sends an email
        containing a download link for the Excel report to the user.

        https://api.smaxtec.com/api/v2/data/downloads/generate_organisation_messages_excel_report

        Args:
            organisation_id (str): ID of organisation the report should be created for
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Empty dict on success, error message else.

        """
        params = {
            "organisation_id": organisation_id,
            "from_date": from_date,
            "to_date": to_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + "/downloads/generate_organisation_messages_excel_report"
        )
        return self.api.post(url_suffix, json=params)

    def get_downloads(self, download_id, **kwargs):
        """Download a generated Excel report.

        https://api.smaxtec.com/api/v2/data/downloads/{download_id}

        Args:
            download_id (str): ID of the download
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/downloads/{download_id}"
        return self.api.get(url_suffix, json=params)

    def get_data_feedrations(
        self, feedration_id, metrics, from_date, to_date, **kwargs
    ):
        """Query feedration data.

        https://api.smaxtec.com/api/v2/data/feedrations/{feedration_id}.json

        Args:
            feedration_id (str): ID of the feedration group
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.

        """
        params = {"metrics": metrics, "from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/feedrations/{feedration_id}.json"
        return self.api.get(url_suffix, json=params)

    def get_data_groups(self, group_id, metrics, from_date, to_date, **kwargs):
        """Query group data.

        https://api.smaxtec.com/api/v2/data/groups/{group_id}.json

        Args:
            group_id (str): ID of the group
            metrics (list(str)): List of metrics to query
            from_date (str): Query from date
            to_date (str): Query end date
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/
        Returns:
            dict: Response from the API. Requested Metric values on success,
                error message else.
        """
        params = {"metrics": metrics, "from_date": from_date, "to_date": to_date}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/groups/{group_id}.json"
        return self.api.get(url_suffix, json=params)

    def get_metrics_groups(self, group_id, **kwargs):
        """List available metrics for a group.

        https://api.smaxtec.com/api/v2/data/groups/{group_id}/metrics

        Args:
            group_id (str): ID of the group
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/
        Returns:
            list[dict]: Response from the API.  List of available metrics on success,
                error message else.
        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/groups/{group_id}/metrics"
        return self.api.get(url_suffix, json=params)
