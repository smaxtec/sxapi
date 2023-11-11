from datetime import (
    datetime,
    timedelta,
)

from sxapi.publicV2 import PublicAPIV2

# TODO: This function is located inside the CLI class.


def get_sensor_data_from_animal(api, animal_id, *args, **kwargs):
    """Performs a get call to PUBLIC_API_V2, to get the sensordata from the given animal_id

    Args:
        api (PublicAPIV2): Api object to perform the call
        animal_id (str): ID of the animal to get the sensordata from
        *args: Optional parameters of the API call.
        **kwargs: Optional parameters of the API call.

    Returns:
        dict: Response from the API. Requested Metric values on success,
                error message else.

    """
    if not isinstance(api, PublicAPIV2):
        print("This function is only available to PublicAPIV2!")
        return

    metrics = kwargs.get("metrics", None)
    if not metrics:
        metrics = ["temp", "act"]
    from_date_string = kwargs.get("from_date")
    to_date_string = kwargs.get("to_date")

    to_date = datetime.utcnow()
    from_date = to_date - timedelta(days=2)

    if to_date_string:
        try:
            to_date = datetime.strptime(*to_date_string, "%Y-%m-%d")
        except ValueError:
            print("to_date has not the right format YYYY-MM-DD!")
            return None

    if from_date_string:
        try:
            from_date = datetime.strptime(*from_date_string, "%Y-%m-%d")
        except ValueError:
            print("from_date has not the right format YYYY-MM-DD!")
            return None

    return api.data.get_data_animals(
        animal_id, metrics, from_date.isoformat(), to_date.isoformat()
    )
