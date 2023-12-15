class Animals:
    """
    This Class represents the /animals endpoint of the PublicAPIV2.
    https://api.smaxtec.com/api/v2/
    """

    def __init__(self, api=None):
        self.api = api
        self.path_suffix = "/animals"

    def post(self, organisation_id, **kwargs):
        """Create a new animal.

        https://api.smaxtec.com/api/v2/animals

        Args:
            organisation_id (str): ID of the organisation the animal
                should be created for
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "organisation_id": organisation_id,
        }

        for k, v in kwargs.items():
            params[k] = v

        return self.api.post(self.path_suffix, json=params)

    def get_by_ids(self, animal_ids, **kwargs):
        """Get animals by IDs.

        https://api.smaxtec.com/api/v2/animals/by_ids

        Args:
            animal_ids (list): List of animal IDs
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            list[dict]: Response of API call. Animals on success,
                error message else.

        """
        params = {
            "animal_ids": animal_ids,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + "/by_ids"
        return self.api.get(url_suffix, json=params)

    def get_by_official_id(self, organisation_id, official_id, **kwargs):
        """Get animal by official ID.

        https://api.smaxtec.com/api/v2/animals/by_official_id/{organisation_id}/{official_id}

        Args:
            organisation_id (str): organisation ID of the animal
            official_id (str): Official ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/by_official_id/{organisation_id}/{official_id}"
        )
        return self.api.get(url_suffix, json=params)

    def get(self, animal_id, **kwargs):
        """Get animal by ID.

        https://api.smaxtec.com/api/v2/animals/{animal_id}

        Args:
            animal_id (str): ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}"
        return self.api.get(url_suffix, json=params)

    def put(self, animal_id, **kwargs):
        """Update an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}

        Args:
            animal_id (str): ID of the animal to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}"
        return self.api.put(url_suffix, json=params)

    def post_aborts(self, animal_id, event_ts, **kwargs):
        """Create an abortion event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/aborts

        Args:
            animal_id (str): ID of the animal to be aborted
            event_ts (str): Timestamp of the abortion event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/aborts"
        return self.api.post(url_suffix, json=params)

    def put_aborts(self, animal_id, event_ts, abort_id, **kwargs):
        """Update an abortion event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/aborts/{abort_id}

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the abortion event
            abort_id (str): ID of the abortion event to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/aborts/{abort_id}"
        return self.api.put(url_suffix, json=params)

    def delete_aborts(self, animal_id, abort_id, **kwargs):
        """Delete an abortion event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/aborts/{abort_id}

        Args:
            animal_id (str): ID of the animal
            abort_id (str): ID of the abortion event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/aborts/{abort_id}"
        return self.api.delete(url_suffix, json=params)

    def post_calving_confirmations(self, animal_id, event_ts, **kwargs):
        """Create a calving confirmation event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/calving_confirmation

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the calving confirmation event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/calving_confirmations"
        return self.api.post(url_suffix, json=params)

    def put_calving_confirmations(
        self, animal_id, calving_confirmation_id, event_ts, **kwargs
    ):
        """Update a calving confirmation event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/calving_confirmations/{calving_confirmation_id}

        Args:
            animal_id (str): ID of the animal
            calving_confirmation_id (str): ID of the calving confirmation
             event to be updated
            event_ts (str): Timestamp of the calving confirmation event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix
            + f"/{animal_id}/calving_confirmations/{calving_confirmation_id}"
        )
        return self.api.put(url_suffix, json=params)

    def delete_calving_confirmations(
        self, animal_id, calving_confirmation_id, **kwargs
    ):
        """Delete a calving confirmation event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/calving_confirmations/{calving_confirmation_id}

        Args:
            animal_id (str): ID of the animal
            calving_confirmation_id (str): ID of the calving confirmation event
             to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix
            + f"/{animal_id}/calving_confirmations/{calving_confirmation_id}"
        )
        return self.api.delete(url_suffix, json=params)

    def get_diagnosis(self, animal_id, **kwargs):
        """Get diagnosis of an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/diagnosis

        Args:
            animal_id (str): ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
             list[dict]: Response of API call. List of diagnosis on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/diagnosis"
        return self.api.get(url_suffix, json=params)

    def post_diagnosis(self, animal_id, diagnosis_date, **kwargs):
        """Create a diagnosis for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/diagnosis

        Args:
            animal_id (str): ID of the animal
            diagnosis_date (str): Date of the diagnosis
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Diagnosis on success,
                error message else.

        """
        params = {
            "diagnosis_date": diagnosis_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/diagnosis"
        return self.api.post(url_suffix, json=params)

    def put_diagnosis(self, animal_id, diagnosis_id, diagnosis_date, **kwargs):
        """Update a diagnosis for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/diagnosis/{diagnosis_id}

        Args:
            animal_id (str): ID of the animal
            diagnosis_id (str): ID of the diagnosis to be updated
            diagnosis_date (str): Date of the diagnosis
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Diagnosis on success,
                error message else.

        """
        params = {
            "diagnosis_date": diagnosis_date,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/diagnosis/{diagnosis_id}"
        return self.api.put(url_suffix, json=params)

    def delete_diagnosis(self, animal_id, diagnosis_id, **kwargs):
        """Delete a diagnosis for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/diagnosis/{diagnosis_id}

        Args:
            animal_id (str): ID of the animal
            diagnosis_id (str): ID of the diagnosis to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Deleted diagnosis on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/diagnosis/{diagnosis_id}"
        return self.api.delete(url_suffix, json=params)

    def post_dry_offs(self, animal_id, event_ts, **kwargs):
        """Create a dry off event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/dry_offs

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the dry off event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/dry_offs"
        return self.api.post(url_suffix, json=params)

    def put_dry_offs(self, animal_id, dry_off_id, **kwargs):
        """Update a dry off event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/dry_offs/{dry_off_id}

        Args:
            animal_id (str): ID of the animal
            dry_off_id (str): ID of the dry off event to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/dry_offs/{dry_off_id}"
        return self.api.put(url_suffix, json=params)

    def delete_dry_offs(self, animal_id, dry_off_id, **kwargs):
        """Delete a dry off event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/dry_offs/{dry_off_id}

        Args:
            animal_id (str): ID of the animal
            dry_off_id (str): ID of the dry off event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/dry_offs/{dry_off_id}"
        return self.api.delete(url_suffix, json=params)

    def post_events_false_positive(self, animal_id, event_id, **kwargs):
        """Mark an animal Event as false positive.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/events/{event_id}/false_positive

        Args:
            animal_id (str): ID of the animal
            event_id (str): ID of the event to be marked as false positive
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/events/{event_id}/false_positive"
        return self.api.post(url_suffix, json=params)

    def post_heats(self, animal_id, event_ts, **kwargs):
        """Create a heat event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/heats

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the heat event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/heats"
        return self.api.post(url_suffix, json=params)

    def put_heats(self, animal_id, heat_id, **kwargs):
        """Update a heat event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/heats/{heat_id}

        Args:
            animal_id (str): ID of the animal
            heat_id (str): ID of the heat event to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/heats/{heat_id}"
        return self.api.put(url_suffix, json=params)

    def delete_heats(self, animal_id, heat_id, **kwargs):
        """Delete a heat event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/heats/{heat_id}

        Args:
            animal_id (str): ID of the animal
            heat_id (str): ID of the heat event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/heats/{heat_id}"
        return self.api.delete(url_suffix, json=params)

    def post_inseminations(self, animal_id, event_ts, **kwargs):
        """Create an insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/insemination

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the insemination event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/inseminations"
        return self.api.post(url_suffix, json=params)

    def put_inseminations(self, animal_id, insemination_id, **kwargs):
        """Update an insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/insemination/{insemination_id}

        Args:
            animal_id (str): ID of the animal
            insemination_id (str): ID of the insemination event to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/inseminations/{insemination_id}"
        return self.api.put(url_suffix, json=params)

    def delete_inseminations(self, animal_id, insemination_id, **kwargs):
        """Delete an insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/insemination/{insemination_id}

        Args:
            animal_id (str): ID of the animal
            insemination_id (str): ID of the insemination event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/inseminations/{insemination_id}"
        return self.api.delete(url_suffix, json=params)

    def post_no_inseminations(self, animal_id, event_ts, reason, **kwargs):
        """Create a no_insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/no_insemination

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the no_insemination event
            reason (str): Reason of the no_insemination event
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
            "reason": reason,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/no_inseminations"
        return self.api.post(url_suffix, json=params)

    def put_no_inseminations(self, animal_id, no_insemination_id, **kwargs):
        """Update a no_insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/no_insemination/{no_insemination_id}

        Args:
            animal_id (str): ID of the animal
            no_insemination_id (str): ID of the no_insemination event to be updated
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{animal_id}/no_inseminations/{no_insemination_id}"
        )
        return self.api.put(url_suffix, json=params)

    def delete_no_inseminations(self, animal_id, no_insemination_id, **kwargs):
        """Delete a no_insemination event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/no_insemination/{no_insemination_id}

        Args:
            animal_id (str): ID of the animal
            no_insemination_id (str): ID of the no_insemination event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{animal_id}/no_inseminations/{no_insemination_id}"
        )
        return self.api.delete(url_suffix, json=params)

    def post_pregnancy_results(self, animal_id, event_ts, pregnant, **kwargs):
        """Create a pregnancy result event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/pregnancy_results

        Args:
            animal_id (str): ID of the animal
            event_ts (str): Timestamp of the pregnancy result event
            pregnant (bool): Pregnancy result of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "event_ts": event_ts,
            "pregnant": pregnant,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/pregnancy_results"
        return self.api.post(url_suffix, json=params)

    def put_pregnancy_results(self, animal_id, pregnancy_result_id, pregnant, **kwargs):
        """Update a pregnancy result event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/pregnancy_results/{pregnancy_result_id}

        Args:
            animal_id (str): ID of the animal
            pregnancy_result_id (str): ID of the pregnancy result event to be updated
            pregnant (bool): Pregnancy result of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "pregnant": pregnant,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{animal_id}/pregnancy_results/{pregnancy_result_id}"
        )
        return self.api.put(url_suffix, json=params)

    def delete_pregnancy_results(self, animal_id, pregnancy_result_id, **kwargs):
        """Delete a pregnancy result event for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/pregnancy_results/{pregnancy_result_id}

        Args:
            animal_id (str): ID of the animal
            pregnancy_result_id (str): ID of the pregnancy result event to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns:
            dict: Response of API call. Animal on success,
                error message else.:

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = (
            self.path_suffix + f"/{animal_id}/pregnancy_results/{pregnancy_result_id}"
        )
        return self.api.delete(url_suffix, json=params)

    def get_tags(self, animal_id, **kwargs):
        """Get tags of an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/tags

        Args:
            animal_id (str): ID of the animal
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns
            dict: Response of API call. List of tags on success,
                error message else.

        """
        params = {}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/tags"
        return self.api.get(url_suffix, json=params)

    def post_tags(self, animal_id, tag, **kwargs):
        """Add a tag to an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/tags

        Args:
            animal_id (str): ID of the animal
            tag (str): Tag to be added
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {
            "tag": tag,
        }

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/tags"
        return self.api.post(url_suffix, json=params)

    def delete_tags(self, animal_id, tag, **kwargs):
        """Delete a tag for an animal.

        https://api.smaxtec.com/api/v2/animals/{animal_id}/tags/{tag}

        Args:
            animal_id (str): ID of the animal
            tag (str): Tag to be deleted
            **kwargs: Optional parameters of the API call.
                Find supported parameters under
                https://api.smaxtec.com/api/v2/

        Returns
            dict: Response of API call. Animal on success,
                error message else.

        """
        params = {"tag": tag}

        for k, v in kwargs.items():
            params[k] = v

        url_suffix = self.path_suffix + f"/{animal_id}/tags"
        return self.api.delete(url_suffix, json=params)
