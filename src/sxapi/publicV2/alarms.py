class Alarms:
    """
    This class represents the /alarms API endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/alarms"

    def post(self, organisation_id, title, **kwargs):
        """Creates a new alarm.

        Args:
            organisation_id (str): ID of organisation the alarm should be created for
            title (str): Title of the alarm
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Created alarm on success, error message else.

        """
        params = {
            "organisation_id": organisation_id,
            "title": title,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get_categories(self, **kwargs):
        """Get all alarms categories for a user or organisation.
        If no user or organisation is given, this
        function return a BadRequestError

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. List of alarms on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/categories"
        return self.api.get(url_suffix, json=params)

    def put(self, alarm_id, organisation_id, **kwargs):
        """Updates an existing alarm.

        Args:
            alarm_id (str): ID of the alarm which should be updated.
            organisation_id (str): ID of organisation the alarm should be updated for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Updated alarm on success, error message else.

        """
        params = {
            "organisation_id": organisation_id,
        }
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{alarm_id}"
        return self.api.put(url_suffix, json=params)

    def get(self, alarm_id, **kwargs):
        """Get one alarm.

        Args:
            alarm_id (str): ID of the desired alarm
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Queried alarm on success, error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{alarm_id}"
        return self.api.get(url_suffix, json=params)

    def delete(self, alarm_id, **kwargs):
        """Delete one alarm.

        Args:
            alarm_id (str): ID of the alarm to delete
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Deleted alarm on success, error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{alarm_id}"
        return self.api.delete(url_suffix, json=params)
