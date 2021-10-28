import json

from sxapi.publicV2.sensordata import get_sensor_data_for_animal


def create_gsd_parser(subparsers):
    gsd_parser = subparsers.add_parser(
        "get_sensor_data",
        aliases=["gsd"],
        help="get sensor data from animal(by its ID)",
    )
    gsd_parser.add_argument("animal_id", help="animal you want get data from")
    gsd_parser.add_argument(
        "--metrics",
        "-m",
        nargs="*",
        default=None,
        help="metrics for sensordata",
    )
    gsd_parser.add_argument(
        "--from_date",
        "-fd",
        default=None,
        nargs=1,
        help="from_date format: YYYY-MM-DD",
    )
    gsd_parser.add_argument(
        "--to_date", "-td", default=None, nargs=1, help="to_date format: YYYY-MM-DD"
    )

    gsd_parser.set_defaults(func=gsd_sub_function)


def gsd_sub_function(args):
    """
    function which gets call if the arguments were parsed
    with get_sensor_data sub-parser
    """
    id = args.animal_id
    metrics = args.metrics
    from_date = args.from_date
    to_date = args.to_date
    resp = get_sensor_data_for_animal(
        id, metrics=metrics, from_date=from_date, to_date=to_date
    )
    if resp is not None:
        print(json.dumps(resp, indent=0))
