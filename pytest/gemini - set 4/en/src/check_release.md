```python
import pytest
import requests
from requests.exceptions import RequestException

from hypotez.src.check_release import check_latest_release


# Mock the requests library to simulate API calls
def mock_requests_get(url, status_code=200, json_data={'tag_name': 'v1.0.0'}):
    """Mocks the requests.get function for testing."""
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json = lambda: json_data
        
    return MockResponse(status_code, json_data)
    

@pytest.fixture
def mocked_requests(monkeypatch):
    """Provides a mocked requests library for tests."""
    mock_get = lambda url: mock_requests_get(url)
    monkeypatch.setattr(requests, 'get', mock_get)
    return mock_get

def test_check_latest_release_valid_input(mocked_requests):
    """Checks the function with valid inputs."""
    owner = "ownername"
    repo = "reponame"
    latest_release = check_latest_release(owner, repo)
    assert latest_release == "v1.0.0"  # Assumes a specific tag for valid input



def test_check_latest_release_invalid_status_code(mocked_requests):
    """Tests handling of invalid status codes (e.g., 404)."""
    owner = "ownername"
    repo = "reponame"
    # Mock a 404 response
    mock_requests_get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', status_code=404)
    latest_release = check_latest_release(owner, repo)
    assert latest_release is None


def test_check_latest_release_invalid_json_structure(mocked_requests):
    """Tests handling if the response is not a valid JSON."""
    owner = "ownername"
    repo = "reponame"
    # Mock a response with an invalid JSON format
    mock_requests_get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', status_code=200, json_data="invalid json")
    latest_release = check_latest_release(owner, repo)
    assert latest_release is None


def test_check_latest_release_request_exception(monkeypatch):
  """Tests handling of a RequestException during the API call."""
  class MockRequestException(RequestException):
    pass
  
  monkeypatch.setattr(requests, 'get', lambda url: raise MockRequestException())
  owner = "ownername"
  repo = "reponame"
  latest_release = check_latest_release(owner, repo)
  assert latest_release is None


def test_check_latest_release_empty_tag_name(mocked_requests):
  """Tests that the function returns None if tag_name is missing or empty."""
  owner = "ownername"
  repo = "reponame"
  #Mock the response with an empty tag_name
  mock_requests_get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', status_code=200, json_data={'tag_name': ''})
  latest_release = check_latest_release(owner, repo)
  assert latest_release is None
```