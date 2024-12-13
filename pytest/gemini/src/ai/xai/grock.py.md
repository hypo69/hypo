```python
import pytest
import requests
import json
from unittest.mock import patch, MagicMock
from hypotez.src.ai.xai.grock import XAI  # Assuming the file is located as specified

@pytest.fixture
def mock_xai():
    """Provides a mock XAI instance with a dummy API key."""
    return XAI("dummy_api_key")

@pytest.fixture
def mock_response():
    """Provides a mock requests response object."""
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {"test": "response"}
    return mock

@pytest.fixture
def mock_stream_response():
    """Provides a mock streaming requests response object."""
    mock = MagicMock()
    mock.status_code = 200
    mock.iter_lines.return_value = [
        '{"data": "line1"}',
        '{"data": "line2"}'
    ]
    return mock

def test_xai_init(mock_xai):
    """Checks if XAI class initializes correctly."""
    assert mock_xai.api_key == "dummy_api_key"
    assert mock_xai.base_url == "https://api.x.ai/v1"
    assert mock_xai.headers == {
        "Authorization": "Bearer dummy_api_key",
        "Content-Type": "application/json"
    }


def test_send_request_success(mock_xai, mock_response):
    """Checks if _send_request sends a request and returns the json response for successful requests."""
    with patch('requests.request', return_value=mock_response) as mock_request:
        response = mock_xai._send_request("POST", "test_endpoint", {"data": "test"})
        mock_request.assert_called_once_with(
            "POST", 
            "https://api.x.ai/v1/test_endpoint", 
            headers=mock_xai.headers, 
            json={"data": "test"}
        )
        assert response == {"test": "response"}


def test_send_request_failure(mock_xai):
    """Checks if _send_request raises an exception for failed requests."""
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Bad Request")
    with patch('requests.request', return_value=mock_response) as mock_request:
        with pytest.raises(requests.exceptions.HTTPError, match="Bad Request"):
            mock_xai._send_request("POST", "test_endpoint", {"data": "test"})
        mock_request.assert_called_once()


def test_chat_completion_valid_input(mock_xai, mock_response):
    """Checks if chat_completion sends a request and returns a valid response."""
    messages = [{"role": "user", "content": "hello"}]
    with patch('requests.request', return_value=mock_response) as mock_request:
        response = mock_xai.chat_completion(messages)
        mock_request.assert_called_once()
        assert response == {"test": "response"}


def test_chat_completion_with_custom_params(mock_xai, mock_response):
    """Checks if chat_completion can handle custom model, stream and temperature."""
    messages = [{"role": "user", "content": "hello"}]
    with patch('requests.request', return_value=mock_response) as mock_request:
      response = mock_xai.chat_completion(messages, model="test-model", stream=True, temperature=0.5)
      mock_request.assert_called_once()
      assert response == {"test": "response"}
      
def test_chat_completion_invalid_input(mock_xai):
    """Check if chat_completion handles error for invalid message input"""
    with pytest.raises(TypeError):
        mock_xai.chat_completion("not a list")


def test_stream_chat_completion_success(mock_xai, mock_stream_response):
    """Checks if stream_chat_completion sends a request and returns a response stream."""
    messages = [{"role": "user", "content": "hello"}]
    with patch('requests.post', return_value=mock_stream_response) as mock_post:
        response_stream = mock_xai.stream_chat_completion(messages)
        mock_post.assert_called_once()
        
        lines = list(response_stream)
        assert lines == ['{"data": "line1"}', '{"data": "line2"}']
        

def test_stream_chat_completion_failure(mock_xai):
    """Checks if stream_chat_completion handles errors."""
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Bad Request")
    with patch('requests.post', return_value=mock_response) as mock_post:
        with pytest.raises(requests.exceptions.HTTPError, match="Bad Request"):
            mock_xai.stream_chat_completion([{"role": "user", "content": "hello"}])
        mock_post.assert_called_once()


def test_stream_chat_completion_with_custom_params(mock_xai, mock_stream_response):
    """Checks if stream_chat_completion can handle custom model, stream and temperature."""
    messages = [{"role": "user", "content": "hello"}]
    with patch('requests.post', return_value=mock_stream_response) as mock_post:
      response = mock_xai.stream_chat_completion(messages, model="test-model", temperature=0.5)
      mock_post.assert_called_once()
      lines = list(response)
      assert lines == ['{"data": "line1"}', '{"data": "line2"}']

def test_stream_chat_completion_invalid_input(mock_xai):
    """Check if stream_chat_completion handles error for invalid message input"""
    with pytest.raises(TypeError):
        mock_xai.stream_chat_completion("not a list")
```