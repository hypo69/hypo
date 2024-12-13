```python
import pytest
from unittest.mock import MagicMock, patch
import json
from xai import XAI  # Assuming xai.py is in the same directory


@pytest.fixture
def mock_xai():
    """Provides a mock XAI client for testing."""
    with patch('xai.requests') as mock_requests:
        mock_session = MagicMock()
        mock_requests.Session.return_value = mock_session
        mock_session.post.return_value = MagicMock(status_code=200, text='{"choices": [{"message": {"content": "Test Response"}}]}')
        mock_session.get.return_value = MagicMock(status_code=200, iter_lines=lambda **kwargs: iter([b'{"choices": [{"message": {"content": "Test Line 1"}}]}\n', b'{"choices": [{"message": {"content": "Test Line 2"}}]}\n']))
        yield mock_requests



def test_xai_initialization():
    """Checks that XAI class can be initialized with a valid API key."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    assert xai_client.api_key == api_key
    assert xai_client.headers == {"Authorization": f"Bearer {api_key}"}
    

def test_chat_completion_valid_input(mock_xai):
    """Checks correct behavior of chat_completion with valid input."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    messages = [{"role": "user", "content": "Hello"}]
    response = xai_client.chat_completion(messages)
    assert isinstance(response, dict)
    assert response == {"choices": [{"message": {"content": "Test Response"}}]}
    mock_xai.Session.return_value.post.assert_called_once()
    
    
def test_chat_completion_invalid_input_messages_type(mock_xai):
    """Checks that chat_completion raises an exception with invalid messages type."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    with pytest.raises(AttributeError):
        xai_client.chat_completion("invalid_messages")
    mock_xai.Session.return_value.post.assert_not_called()
    
def test_chat_completion_invalid_input_empty_messages(mock_xai):
     """Checks that chat_completion handles empty message lists correctly."""
     api_key = "test_api_key"
     xai_client = XAI(api_key)
     messages = []  # Empty message list
     response = xai_client.chat_completion(messages)
     assert response == {"choices": [{"message": {"content": "Test Response"}}]}
     mock_xai.Session.return_value.post.assert_called_once()


def test_stream_chat_completion_valid_input(mock_xai):
    """Checks correct behavior of stream_chat_completion with valid input."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    messages = [{"role": "user", "content": "Hello"}]
    response_stream = xai_client.stream_chat_completion(messages)
    
    response_list = [json.loads(line) for line in response_stream if line.strip()]
    assert len(response_list) == 2
    assert response_list[0] == {"choices": [{"message": {"content": "Test Line 1"}}]}
    assert response_list[1] == {"choices": [{"message": {"content": "Test Line 2"}}]}
    mock_xai.Session.return_value.get.assert_called_once()


def test_stream_chat_completion_invalid_input_messages_type(mock_xai):
    """Checks that stream_chat_completion raises exception with invalid messages type."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    with pytest.raises(AttributeError):
        for line in xai_client.stream_chat_completion("invalid_messages"):
            pass # Exhaust iterator to trigger request
    mock_xai.Session.return_value.get.assert_not_called()


def test_stream_chat_completion_invalid_input_empty_messages(mock_xai):
    """Checks that stream_chat_completion handles empty message lists correctly."""
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    messages = []  # Empty message list
    response_stream = xai_client.stream_chat_completion(messages)
    response_list = [json.loads(line) for line in response_stream if line.strip()]
    assert len(response_list) == 2
    assert response_list[0] == {"choices": [{"message": {"content": "Test Line 1"}}]}
    assert response_list[1] == {"choices": [{"message": {"content": "Test Line 2"}}]}
    mock_xai.Session.return_value.get.assert_called_once()


def test_chat_completion_api_error(mock_xai):
    """Checks how chat_completion handles API errors."""
    mock_xai.Session.return_value.post.return_value.status_code = 500
    mock_xai.Session.return_value.post.return_value.text = "Internal Server Error"
    api_key = "test_api_key"
    xai_client = XAI(api_key)
    messages = [{"role": "user", "content": "Hello"}]
    with pytest.raises(Exception, match=r'API request failed with status code 500: Internal Server Error'):
        xai_client.chat_completion(messages)
    mock_xai.Session.return_value.post.assert_called_once()

def test_stream_chat_completion_api_error(mock_xai):
    """Checks how stream_chat_completion handles API errors."""
    mock_xai.Session.return_value.get.return_value.status_code = 401
    mock_xai.Session.return_value.get.return_value.text = "Unauthorized"

    api_key = "test_api_key"
    xai_client = XAI(api_key)
    messages = [{"role": "user", "content": "Hello"}]
    with pytest.raises(Exception, match=r'API request failed with status code 401: Unauthorized'):
         for line in xai_client.stream_chat_completion(messages):
              pass
    mock_xai.Session.return_value.get.assert_called_once()
```