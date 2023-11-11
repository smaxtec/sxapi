class Events:
    """
    This Class represents the /events endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/events"

    def get(self, organisation_id, **kwargs):
        """Get all events of an organisation.

        https://api.smaxtec.com/api/v2/events

        Args:
            organisation_id (str): ID of the organisation the events
                should be retrieved for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. List of events on success,
                error message else.

        """
        params = {
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.get(self.path_suffix, json=params)

    def get_by_id(self, event_id, **kwargs):
        """Get one event by ID.

        https://api.smaxtec.com/api/v2/events/by_id

        Args:
            event_id (str): ID of the desired event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Event on success, error message else.

        """
        params = {
            "event_id": event_id,
        }
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/by_id"
        return self.api.get(url_suffix, json=params)

    def get_categories(self, **kwargs):
        """Get all event categories.
            If no user id or organisation id in the parameter
            a Bad Request Error will be returned!

         https://api.smaxtec.com/api/v2/events/categories

        Args:
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. List of event categories on success,
                error message else.

        """
        params = {}
        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/categories"
        return self.api.get(url_suffix, json=params)
