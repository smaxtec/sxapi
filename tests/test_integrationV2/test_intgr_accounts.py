import mock

from sxapi.integrationV2 import IntegrationAPIV2


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.get")
def test_get_usages(get_mock):
    test_api = IntegrationAPIV2()
    test_api.accounts.get_usages(kwarg1="kwarg1")

    call_args = get_mock.call_args_list[0]

    assert get_mock.call_count == 1
    assert call_args.args[0] == "/accounts/usages"
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put(put_mock):
    test_api = IntegrationAPIV2()
    test_api.accounts.put(
        "test_account_nr",
        "test_account_name",
        "test_partner_id",
        "test_address_name",
        "test_street",
        "test_county_code",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert call_args.args[0] == "/accounts/test_account_nr"
    assert call_args.kwargs["json"] == {
        "account_name": "test_account_name",
        "partner_id": "test_partner_id",
        "address_name": "test_address_name",
        "street": "test_street",
        "county_code": "test_county_code",
        "kwarg1": "kwarg1",
    }


@mock.patch("sxapi.integrationV2.IntegrationAPIV2.put")
def test_put_organisation(put_mock):
    test_api = IntegrationAPIV2()
    test_api.accounts.put_organisation(
        "test_account_nr",
        "test_organisation_id",
        kwarg1="kwarg1",
    )

    call_args = put_mock.call_args_list[0]

    assert put_mock.call_count == 1
    assert (
        call_args.args[0]
        == "/accounts/test_account_nr/organisation/test_organisation_id"
    )
    assert call_args.kwargs["json"] == {
        "kwarg1": "kwarg1",
    }
