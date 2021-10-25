from datetime import (
    datetime,
    timedelta,
)
from urllib.parse import urlencode

import sxapi.publicV2 as publicV2


def get_sensor_data_for_animal(animal_id, *args, **kwargs):
    """
    Performs a get call to PUBLIC_API_V2, to get the sensordata from the given animal_id
    """

    metrics = kwargs.get("metrics")
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
            print("from_date has not in the right format YYYY-MM-DD!")
            return None

    param = {
        "metrics": metrics,
        "to_date": to_date,
        "from_date": from_date,
    }
    url_path = f"/data/animals/{animal_id}.json?{urlencode(param, True)}"
    resp = publicV2.public_api.get(url_path, params=param)

    return resp
