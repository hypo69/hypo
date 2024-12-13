```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from openai import OpenAI
import os

# Mocking the config module
@pytest.fixture
def mock_config():
    with patch('config.get') as mock:
        mock.return_value = 'test_api_key'
        yield mock

# Mocking createReadStream 
@pytest.fixture
def mock_createReadStream():
  with patch('openai.createReadStream',return_value='test_file_stream') as mock:
    yield mock

# Mocking the OpenAI API
@pytest.fixture
def mock_openai_api():
    with patch('openai.OpenAIApi') as mock:
        yield mock

# Mocking the OpenAI Configuration
@pytest.fixture
def mock_openai_configuration():
     with patch('openai.Configuration') as mock:
        yield mock

# Fixture for creating an instance of OpenAI
@pytest.fixture
def openai_instance(mock_config,mock_openai_configuration,mock_openai_api):
    return OpenAI('test_api_key')


def test_openai_initialization(mock_config,mock_openai_configuration,mock_openai_api):
    """
    Test that the OpenAI class is initialized correctly.
    """
    openai_instance = OpenAI('test_api_key')

    mock_openai_configuration.assert_called_once_with({'apiKey': 'test_api_key'})
    mock_openai_api.assert_called_once()

    assert openai_instance.roles == {
      'ASSISTANT': 'assistant',
      'USER': 'user',
      'SYSTEM': 'system',
    }

def test_openai_chat_valid_input(openai_instance, mock_openai_api):
    """
    Test the chat function with valid input.
    """
    mock_response = AsyncMock()
    mock_response.data = {"choices": [{"message": "test_message"}]}
    mock_openai_api.return_value.createChatCompletion = AsyncMock(return_value=mock_response)

    messages = [{"role": "user", "content": "Hello"}]
    
    result = await openai_instance.chat(messages)

    mock_openai_api.return_value.createChatCompletion.assert_called_once_with(model='gpt-3.5-turbo', messages=messages)
    assert result == "test_message"


def test_openai_chat_api_error(openai_instance, mock_openai_api):
    """
    Test the chat function when the API returns an error.
    """
    mock_openai_api.return_value.createChatCompletion = AsyncMock(side_effect=Exception("API Error"))
    
    messages = [{"role": "user", "content": "Hello"}]
    result = await openai_instance.chat(messages)
    
    assert result is None


def test_openai_transcription_valid_input(openai_instance, mock_openai_api,mock_createReadStream):
    """
    Test the transcription function with a valid file path.
    """
    mock_response = AsyncMock()
    mock_response.data = {"text": "test_transcription"}
    mock_openai_api.return_value.createTranscription = AsyncMock(return_value=mock_response)

    filepath = "test_audio.mp3"
    result = await openai_instance.transcription(filepath)
    
    mock_createReadStream.assert_called_once_with(filepath)
    mock_openai_api.return_value.createTranscription.assert_called_once_with('test_file_stream', 'whisper-1')
    assert result == "test_transcription"


def test_openai_transcription_api_error(openai_instance, mock_openai_api,mock_createReadStream):
    """
    Test the transcription function when the API returns an error.
    """
    mock_openai_api.return_value.createTranscription = AsyncMock(side_effect=Exception("API Error"))
    
    filepath = "test_audio.mp3"
    result = await openai_instance.transcription(filepath)
    
    mock_createReadStream.assert_called_once_with(filepath)
    assert result is None

def test_openai_transcription_filenotfound_error(openai_instance,mock_createReadStream):
  """
    Test the transcription function when the file does not exist.
  """
  filepath = "non_existent_file.mp3"
  mock_createReadStream.side_effect=FileNotFoundError("File not found")

  result = await openai_instance.transcription(filepath)

  assert mock_createReadStream.call_count == 1
  assert result is None
```