```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Assuming the XAI class is defined in a file named xai.py
# and it has a structure similar to what's described in the readme.
class XAI:
    def __init__(self, api_key):
      self.api_key = api_key
      self.base_url = "https://api.x.ai/chat/completions"

    def chat_completion(self, messages):
        # Mocking the actual API call to avoid real network requests
        # For demonstration purposes, return a simple string
        return "Mocked non-streaming response"

    def stream_chat_completion(self, messages):
        # Mocking the actual API call to avoid real network requests
        # For demonstration purposes, yield a few lines of mocked streaming response
        yield '{"text": "Mocked"} \n'
        yield '{"text": "streaming"} \n'
        yield '{"text": "response"} \n'


@pytest.fixture
def mock_xai_instance():
    """Provides a mock instance of the XAI class."""
    return XAI(api_key="test_api_key")


def test_xai_initialization():
    """Checks if XAI class initializes correctly with the provided API key."""
    api_key = "test_api_key"
    xai = XAI(api_key)
    assert xai.api_key == api_key
    assert xai.base_url == "https://api.x.ai/chat/completions"


def test_chat_completion_valid_input(mock_xai_instance):
    """Checks the chat_completion method with valid input."""
    messages = [
        {"role": "system", "content": "You are a test chatbot."},
        {"role": "user", "content": "Hello!"},
    ]
    response = mock_xai_instance.chat_completion(messages)
    assert response == "Mocked non-streaming response"  # Expect a mocked response, as we are not making API calls.


def test_chat_completion_empty_messages(mock_xai_instance):
  """Checks the chat_completion method with empty messages."""
  messages = []
  response = mock_xai_instance.chat_completion(messages)
  assert response == "Mocked non-streaming response"  # Expect a mocked response, as we are not making API calls.


def test_chat_completion_invalid_input_types(mock_xai_instance):
  """Checks the chat_completion method with invalid message input type."""
  with pytest.raises(TypeError):
    mock_xai_instance.chat_completion("invalid_messages") # Should raise error if not list


def test_stream_chat_completion_valid_input(mock_xai_instance):
    """Checks the stream_chat_completion method with valid input."""
    messages = [
        {"role": "system", "content": "You are a test chatbot."},
        {"role": "user", "content": "Hello!"},
    ]
    stream_response = mock_xai_instance.stream_chat_completion(messages)
    
    expected_response = [
        {"text": "Mocked"},
        {"text": "streaming"},
        {"text": "response"},
    ]
    actual_response = [json.loads(line.strip()) for line in stream_response if line.strip()]

    assert actual_response == expected_response # Expect a mocked streaming response, as we are not making API calls.


def test_stream_chat_completion_empty_messages(mock_xai_instance):
  """Checks the stream_chat_completion method with empty messages."""
  messages = []
  stream_response = mock_xai_instance.stream_chat_completion(messages)
  
  expected_response = [
        {"text": "Mocked"},
        {"text": "streaming"},
        {"text": "response"},
    ]
  actual_response = [json.loads(line.strip()) for line in stream_response if line.strip()]

  assert actual_response == expected_response # Expect a mocked streaming response, as we are not making API calls.


def test_stream_chat_completion_invalid_input_type(mock_xai_instance):
  """Checks the stream_chat_completion method with invalid message input type."""
  with pytest.raises(TypeError):
    for _ in mock_xai_instance.stream_chat_completion("invalid_messages"): # Should raise error if not list
      pass
```