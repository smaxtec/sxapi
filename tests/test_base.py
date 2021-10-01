from sxapi.base import BaseAPI
import mock


@mock.patch('requests.Session.post')
def test_base(mock_post):
    api = BaseAPI("https://api.smaxtec.com/api/v2", "test_user", "test_password")
    assert api.api_base_url == "https://api.smaxtec.com/api/v2"
    assert api.email == "test_user"
    assert api.password == "test_password"
    api.post("/users/test_user/test_push")
    assert mock_post.call_count == 2
