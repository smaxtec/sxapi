class Notes:
    """
    Class for interacting with the notes endpoint of the public V2 API
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/notes"

    def post(self, source, reference_type, reference_id, category, note_event, **kwargs):
        """Create a new note.

        Args:
            source (str): Source of the note
            reference_type (str): Type of the reference
            reference_id (str): ID of the reference
            category (str): Category of the note
            note_event (str): Event of the note
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Note on success,
                error message else.

        """
        params = {
            "source": source,
            "reference_type": reference_type,
            "reference_id": reference_id,
            "category": category,
            "note_event": note_event,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get(self, note_id, **kwargs):
        """Get one note.

        Args:
            note_id (str): ID of the desired note
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Note on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{note_id}"
        return self.api.get(url_suffix, json=kwargs)

    def put(self, note_id, source, reference_type, reference_id, category, note_event, **kwargs):
        """Update an existing note.

        Args:
            note_id (str): ID of the note to be updated
            source (str): Source of the note
            reference_type (str): Type of the reference
            reference_id (str): ID of the reference
            category (str): Category of the note
            note_event (str): Event of the note
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Note on success,
                error message else.

        """
        params = {
            "source": source,
            "reference_type": reference_type,
            "reference_id": reference_id,
            "category": category,
            "note_event": note_event,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{note_id}"
        return self.api.put(url_suffix, json=params)