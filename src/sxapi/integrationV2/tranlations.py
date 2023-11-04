class Translations:
    """
    This Class represents the /translations endpoint fo the IntegrationAPIV2
    https://api.smaxtec.com/integration/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/translations"

    def get_events(self, language, **kwargs):
        """Get translations for events.

        Args:
            language (str): Language of the events to be returned
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

        url_suffix = self.path_suffix + f"/{language}/events"
        return self.api.get(url_suffix, json=params)

    def get_event_types(self, language, event_type, **kwargs):
        """Get translations for event types.

        Args:
            language (str): Language of the event types to be returned
            event_type (str): Type of the event types to be returned
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/integration/v2/

        Returns:
            dict: Response of API call. List of event types on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{language}/events/{event_type}"
        return self.api.get(url_suffix, json=params)
