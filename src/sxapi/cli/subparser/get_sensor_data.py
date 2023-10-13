import json

from sxapi.cli import cli_user
from sxapi.publicV2.sensordata import get_sensor_data_from_animal


def create_gsd_parser(subparsers):
    """
    get_sensor_data subparser for cli_tests.
    Responsible for performing api-call to get the sensor data for a given animal.

    The 'animals_id' is mandatory argument 'animal_id'.
    It represents the animal you want to get data from.

    The following flag are only optional.
    The --metrics/-m Flag defines the metrics you want to get from the animal sensor.
    It expects at most two arguments 'temp', 'act' or both together. Where 'temp' means
    getting the temperature metric and 'act' means the activity metric.


    The --from_date Flag defines the start-date of window you want to get data from.
    It expects exactly one argument, a datetime in the format 'YYYY-MM-DD'
    (e.g. 2022.01.12).

    The --to_date Flag defines the end-date of window you want to get data from.
    It expects exactly one argument, a datetime in the format 'YYYY-MM-DD'
    (e.g. 2022.01.12).
    """
    gsd_parser = subparsers.add_parser(
        "get_sensor_data",
        aliases=["gsd"],
        help="Get sensor data from animal(by its ID)",
    )
    gsd_parser.add_argument(
        "animal_id",
        help="Animal you want get data from",
    )
    gsd_parser.add_argument(
        "--metrics",
        "-m",
        nargs="*",
        default=None,
        help="metrics for sensordata",
    )
    gsd_parser.add_argument(
        "--from_date",
        default=None,
        nargs=1,
        help="from_date format: YYYY-MM-DD",
    )
    gsd_parser.add_argument(
        "--to_date",
        default=None,
        nargs=1,
        help="to_date format: YYYY-MM-DD",
    )

    gsd_parser.set_defaults(func=gsd_sub_function)


def gsd_sub_function(args):
    """
    The get_sensor_data subparser default function.
    This function gets called if you get_sensor_data subparser is used.

    Pares the given arguments and calls a function which
    performs the desired api call.
    """
    if not cli_user.check_credentials_set():
        print("No credentials set. Use --help for more information.")
        return

    api = cli_user.public_v2_api

    id = args.animal_id
    metrics = args.metrics
    from_date = args.from_date
    to_date = args.to_date
    resp = get_sensor_data_from_animal(
        api=api, animal_id=id, metrics=metrics, from_date=from_date, to_date=to_date
    )
    if resp is not None:
        print(json.dumps(resp, indent=0))
