import mock

from sxapi.publicV2 import PublicAPIV2


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_data_animals(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_data_animals(
        "test_animal_id",
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/animals/test_animal_id.json"
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_metrics_animals(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_metrics_animals("test_animal_id", kwargs1="1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/animals/test_animal_id/metrics"
    assert call_args.kwargs["json"] == {"kwargs1": "1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_data_devices(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_data_devices(
        "test_device_id",
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/devices/test_device_id.json"
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_metrics_devices(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_metrics_devices("test_device_id", kwargs1="1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/devices/test_device_id/metrics"
    assert call_args.kwargs["json"] == {"kwargs1": "1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_download_animal_data(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_download_animal_data(
        ["animal1", "animal2"],
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/download_animal_data"
    assert call_args.kwargs["json"] == {
        "animal_ids": ["animal1", "animal2"],
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_download_device_data(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_download_device_data(
        ["device1", "device2"],
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/download_device_data"
    assert call_args.kwargs["json"] == {
        "device_ids": ["device1", "device2"],
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_download_group_data(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_download_group_data(
        ["group1", "group2"],
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/download_group_data"
    assert call_args.kwargs["json"] == {
        "group_ids": ["group1", "group2"],
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_downloads_excel_report(post_mock):
    test_api = PublicAPIV2()
    test_api.data.post_downloads_excel_report("2019-01-01", "2019-01-02", kwargs1="1")

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/data/downloads/generate_excel_report"
    assert call_args.kwargs["json"] == {
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_downloads_messages_excel_report(post_mock):
    test_api = PublicAPIV2()
    test_api.data.post_downloads_messages_excel_report(
        "2019-01-01", "2019-01-02", kwargs1="1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert call_args.args[0] == "/data/downloads/generate_messages_excel_report"
    assert call_args.kwargs["json"] == {
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.post")
def test_post_downloads_organisation_messages_excel_report(post_mock):
    test_api = PublicAPIV2()
    test_api.data.post_downloads_organisation_messages_excel_report(
        "test_organisation_id", "2019-01-01", "2019-01-02", kwargs1="1"
    )

    call_args = post_mock.call_args_list[0]

    assert post_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/data/downloads/generate_organisation_messages_excel_report"
    )
    assert call_args.kwargs["json"] == {
        "organisation_id": "test_organisation_id",
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_downloads(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_downloads("test_download_id", kwargs1="1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/downloads/test_download_id"
    assert call_args.kwargs["json"] == {"kwargs1": "1"}


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_data_feedrations(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_data_feedrations(
        "test_feedration_id",
        ["metric1", "metric2"],
        "2019-01-01",
        "2019-01-02",
        kwargs1="1",
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/feedrations/test_feedration_id.json"
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_data_groups(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_data_groups(
        "test_group_id", ["metric1", "metric2"], "2019-01-01", "2019-01-02", kwargs1="1"
    )

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/groups/test_group_id.json"
    assert call_args.kwargs["json"] == {
        "metrics": ["metric1", "metric2"],
        "from_date": "2019-01-01",
        "to_date": "2019-01-02",
        "kwargs1": "1",
    }


@mock.patch("sxapi.publicV2.PublicAPIV2.get")
def test_get_metrics_groups(get_mock):
    test_api = PublicAPIV2()
    test_api.data.get_metrics_groups("test_group_id", kwargs1="1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/data/groups/test_group_id/metrics"
    assert call_args.kwargs["json"] == {"kwargs1": "1"}
