import mock

from tests import (
    CliUserTest,
    ResponseMock,
    SxMainTestParser,
)

test_paser = SxMainTestParser(True)
args_parser = test_paser.parse_args
test_cli_user = CliUserTest()


@mock.patch("builtins.print")
@mock.patch("sxapi.cli.parser.main_parser.cli_user", test_cli_user)
@mock.patch("sxapi.cli.parser.subparser.animals.get.cli_user", test_cli_user)
def test_cli_animals_get(print_mock):

    # test output for all animals and organisation_id
    test_cli_user.integration_v2_api.mock_get_return_value(
        ResponseMock([{"all": "animals"}], 200)
    )

    # check for correct argument parsing
    namespace = args_parser(["animals", "get", "--organisation_id", "parent_orga_id"])
    assert namespace.animals_sub_commands == "get"
    assert namespace.ids is None
    assert namespace.official_ids is False
    assert namespace.organisation_id == "parent_orga_id"
    assert namespace.limit == 0
    assert namespace.archived is False

    # check if output was correctly printed to stdout
    assert print_mock.call_args[0][0] == '[{"all": "animals"}]'
    assert test_cli_user.integration_v2_api.get_called_with[0] == {
        "kwargs": {"json": {"include_archived": False}},
        "path": "/organisations/parent_orga_id/animals",
    }

    test_cli_user.integration_v2_api.reset_mock()

    # test output for multiple animals with id
    test_cli_user.public_v2_api.mock_get_return_value(
        ResponseMock(
            [
                {"animal_id": "1", "archived": True},
                {"animal_id": "2", "archived": False},
                {"animal_id": "3", "archived": True},
                {"animal_id": "4", "archived": True},
            ],
            200,
        )
    )

    # check for correct argument parsing
    namespace = args_parser(
        ["animals", "get", "--ids", "1", "2", "3", "4", "--limit", "2", "--archived"]
    )
    assert namespace.animals_sub_commands == "get"
    assert namespace.ids == ["1", "2", "3", "4"]
    assert namespace.official_ids is False
    assert namespace.organisation_id is None
    assert namespace.limit == 2
    assert namespace.archived is True

    # check if output was correctly printed to stdout
    assert (
        print_mock.call_args[0][0]
        == '[{"animal_id": "1", "archived": true}, {"animal_id": "3", "archived": true}]'
    )
    assert test_cli_user.public_v2_api.get_called_with[0] == {
        "kwargs": {"json": {"animal_ids": ["1", "2", "3", "4"]}},
        "path": "/animals/by_ids",
    }
    test_cli_user.public_v2_api.reset_mock()

    # test output for multiple animals with official id and archived
    animals_list = [
        {"animal_id": "1", "archived": True},
        {"animal_id": "2", "archived": False},
        {"animal_id": "3", "archived": True},
        {"animal_id": "4", "archived": True},
    ]
    test_cli_user.public_v2_api.mock_get_return_value(
        ResponseMock(animals_list, 200, iterator=True)
    )

    # check for correct argument parsing
    namespace = args_parser(
        ["animals", "get", "--ids", "1", "2", "3", "4", "--official-ids"]
    )
    assert namespace.animals_sub_commands == "get"
    assert namespace.ids == ["1", "2", "3", "4"]
    assert namespace.official_ids is True
    assert namespace.organisation_id is None
    assert namespace.limit == 0
    assert namespace.archived is False

    assert len(test_cli_user.public_v2_api.get_called_with) == 4
    for idx, a in enumerate(animals_list):
        assert test_cli_user.public_v2_api.get_called_with[idx] == {
            "kwargs": {"json": {}},
            "path": f"/animals/by_official_id/{test_cli_user.organisation_id}/{a['animal_id']}",
        }

    # check if output was correctly printed to stdout
    assert print_mock.call_args[0][0] == '[{"animal_id": "2", "archived": false}]'
