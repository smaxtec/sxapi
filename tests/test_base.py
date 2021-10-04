from sxapi.base import BaseAPI, PublicAPIV2, IntegrationAPIV2
import mock

@mock.patch('requests.Session.delete')
@mock.patch('requests.Session.put')
@mock.patch('requests.Session.get')
@mock.patch('requests.Session.post')
def test_base(mock_post, mock_get, mock_put, mock_delete):
    api = BaseAPI("https://api.smaxtec.com/api/v2", "test_user", "test_password")
    assert api.api_base_url == "https://api.smaxtec.com/api/v2"
    assert api.email == "test_user"
    assert api.password == "test_password"
    api.post("/users/test_user/test_push")
    assert mock_post.call_count == 2
    api.api_token = "testtoken123lalala"
    api.post("/users/test_user/test_push")
    assert mock_post.call_count == 3

    publicAPI = PublicAPIV2(email="test_user", password="test_password")
    assert publicAPI.api_base_url == "https://api.smaxtec.com/api/v2"
    assert publicAPI.email == "test_user"
    assert publicAPI.password == "test_password"
    publicAPI.post("/users/test_user/test_push")
    assert mock_post.call_count == 5

    integrationAPI = IntegrationAPIV2(email="test_user", password="test_password")
    assert integrationAPI.api_base_url == "https://api.smaxtec.com/integration/v2"
    assert integrationAPI.email == "test_user"
    assert integrationAPI.password == "test_password"
    integrationAPI.get("/service/status")
    assert mock_post.call_count == 6
    assert mock_get.call_count == 1
    integrationAPI = IntegrationAPIV2(email="test_user", password="test_password")
    assert integrationAPI.api_base_url == "https://api.smaxtec.com/integration/v2"
    assert integrationAPI.email == "test_user"
    assert integrationAPI.password == "test_password"
    integrationAPI.put("/test")
    assert mock_post.call_count == 7
    assert mock_get.call_count == 1
    assert mock_put.call_count == 1
    integrationAPI = IntegrationAPIV2(email="test_user", password="test_password")
    assert integrationAPI.api_base_url == "https://api.smaxtec.com/integration/v2"
    assert integrationAPI.email == "test_user"
    assert integrationAPI.password == "test_password"
    integrationAPI.delete("/test")
    assert mock_post.call_count == 8
    assert mock_get.call_count == 1
    assert mock_put.call_count == 1
    assert mock_delete.call_count == 1
