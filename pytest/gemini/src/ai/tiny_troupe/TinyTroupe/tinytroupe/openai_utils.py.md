```python
import pytest
import os
from unittest.mock import patch, MagicMock
import time
import pickle
from tinytroupe import utils
from tinytroupe.openai_utils import (
    LLMCall,
    OpenAIClient,
    AzureClient,
    InvalidRequestError,
    NonTerminalError,
    register_client,
    client,
    force_api_type,
    force_api_cache,
    force_default_value,
    default,
    _api_type_to_client,
    _api_type_override,
)
import openai
from openai import OpenAI, AzureOpenAI

# Mock the logging to avoid cluttering test output.
import logging
logger = logging.getLogger("tinytroupe")
logger.disabled = True

# Fixture for the config
@pytest.fixture
def mock_config():
    config = {
        "OpenAI": {
            "MODEL": "gpt-4",
            "MAX_TOKENS": "1024",
            "TEMPERATURE": "0.3",
            "TOP_P": "0",
            "FREQ_PENALTY": "0.0",
            "PRESENCE_PENALTY": "0.0",
            "TIMEOUT": "30.0",
            "MAX_ATTEMPTS": "3.0",
            "WAITING_TIME": "0.5",
            "EXPONENTIAL_BACKOFF_FACTOR": "5",
            "EMBEDDING_MODEL": "text-embedding-3-small",
            "CACHE_API_CALLS": "True",
            "CACHE_FILE_NAME": "test_cache.pickle",
            "API_TYPE": "openai",
            "AZURE_API_VERSION": "2023-05-15",
        }
    }
    with patch("tinytroupe.openai_utils.utils.read_config_file", return_value=config):
        yield config

# Fixture for a mock OpenAI client
@pytest.fixture
def mock_openai_client():
     with patch('tinytroupe.openai_utils.OpenAI') as MockOpenAI:
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(to_dict=MagicMock(return_value={'content':'test response'})))])
        MockOpenAI.return_value = mock_client
        yield MockOpenAI

# Fixture for a mock Azure client
@pytest.fixture
def mock_azure_client():
    with patch('tinytroupe.openai_utils.AzureOpenAI') as MockAzureOpenAI:
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(to_dict=MagicMock(return_value={'content':'test response'})))])
        MockAzureOpenAI.return_value = mock_client
        yield MockAzureOpenAI

# Fixture for a mock tiktoken encoder
@pytest.fixture
def mock_tiktoken():
    with patch('tinytroupe.openai_utils.tiktoken') as mock_tiktoken:
        mock_encoding = MagicMock()
        mock_encoding.encode.return_value = [1, 2, 3]
        mock_tiktoken.encoding_for_model.return_value = mock_encoding
        mock_tiktoken.get_encoding.return_value = mock_encoding
        yield mock_tiktoken

# Fixture for mock embedding calls
@pytest.fixture
def mock_embedding():
    with patch('tinytroupe.openai_utils.OpenAI') as MockOpenAI:
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = MagicMock(data=[MagicMock(embedding=[0.1, 0.2, 0.3])])
        MockOpenAI.return_value = mock_client
        yield MockOpenAI

@pytest.fixture
def mock_azure_embedding():
    with patch('tinytroupe.openai_utils.AzureOpenAI') as MockAzureOpenAI:
        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = MagicMock(data=[MagicMock(embedding=[0.1, 0.2, 0.3])])
        MockAzureOpenAI.return_value = mock_client
        yield MockAzureOpenAI


@pytest.fixture(autouse=True)
def reset_api_overrides():
    global _api_type_override
    _api_type_override = None
    _api_type_to_client.clear()
    register_client("openai", OpenAIClient())
    register_client("azure", AzureClient())

@pytest.fixture
def mock_utils_compose():
    with patch('tinytroupe.openai_utils.utils.compose_initial_LLM_messages_with_templates', return_value=[{"role": "user", "content": "test message"}]) as mock:
         yield mock
###########################################################################
# LLMCall tests
###########################################################################
def test_llmcall_initialization():
    """Test that LLMCall initializes correctly with a system template."""
    llm_call = LLMCall(system_template_name="test_system_template")
    assert llm_call.system_template_name == "test_system_template"
    assert llm_call.user_template_name is None
    assert llm_call.model_params == {}


def test_llmcall_call_with_content(mock_openai_client, mock_utils_compose):
    """Test that LLMCall correctly calls the LLM and extracts content."""
    llm_call = LLMCall(system_template_name="test_system_template")
    
    response = llm_call.call()

    assert response == 'test response'
    assert mock_utils_compose.call_count == 1
    assert mock_openai_client.return_value.send_message.call_count == 1


def test_llmcall_call_without_content(mock_openai_client, mock_utils_compose):
    """Test LLMCall handling of a response without content."""
    mock_openai_client.return_value.send_message.return_value = {'error': 'no content'}
    llm_call = LLMCall(system_template_name="test_system_template")
    
    response = llm_call.call()
    
    assert response is None
    assert mock_utils_compose.call_count == 1
    assert mock_openai_client.return_value.send_message.call_count == 1


def test_llmcall_repr():
    """Test the __repr__ method of LLMCall."""
    llm_call = LLMCall(system_template_name="test_system", user_template_name="test_user", model_params={"model": "gpt-4"})
    llm_call.messages = [{"role":"system", "content":"test system"}]
    llm_call.model_output = {'content': 'test response'}
    
    expected_repr = "LLMCall(messages=[{'role': 'system', 'content': 'test system'}], model_config={}, model_output={'content': 'test response'})"
    assert repr(llm_call) == expected_repr

###########################################################################
# OpenAIClient tests
###########################################################################
def test_openai_client_initialization(mock_config):
    """Test that OpenAIClient initializes correctly."""
    client = OpenAIClient()
    assert client.cache_api_calls is True
    assert client.cache_file_name == "test_cache.pickle"
    assert hasattr(client, "api_cache")

def test_openai_client_set_api_cache(mock_config):
    """Test that OpenAIClient set_api_cache method updates the cache parameters correctly."""
    client = OpenAIClient()
    client.set_api_cache(False, "new_cache.pickle")
    assert client.cache_api_calls is False
    assert client.cache_file_name == "new_cache.pickle"
    assert not hasattr(client, "api_cache")

    client.set_api_cache(True)
    assert client.cache_api_calls is True
    assert client.cache_file_name == "test_cache.pickle"
    assert hasattr(client, "api_cache")

def test_openai_client_setup_from_config(mock_config, mock_openai_client):
     """Test that OpenAIClient sets up the OpenAI API client correctly."""
     client = OpenAIClient()
     client._setup_from_config()
     mock_openai_client.assert_called_once()

def test_openai_client_send_message_valid(mock_config, mock_openai_client, mock_tiktoken):
    """Test send_message with valid parameters."""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    response = client.send_message(messages)
    assert response == {'content':'test response'}
    mock_openai_client.return_value.chat.completions.create.assert_called_once()
    assert mock_tiktoken.encoding_for_model.call_count == 1

def test_openai_client_send_message_with_cache(mock_config, mock_openai_client, mock_tiktoken):
    """Test that cached responses are returned if present in the cache"""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    cache_key = str(("gpt-4", {'messages': messages, 'temperature': 0.3, 'max_tokens': 1024, 'top_p': 0, 'frequency_penalty': 0.0, 'presence_penalty': 0.0, 'stop': [], 'timeout': 30.0, 'stream': False, 'n': 1}))
    client.api_cache[cache_key] = {'content': 'cached response'}
    response = client.send_message(messages)

    assert response == {'content':'cached response'}
    mock_openai_client.return_value.chat.completions.create.assert_not_called()
    assert mock_tiktoken.encoding_for_model.call_count == 1

def test_openai_client_send_message_invalid_request_error(mock_config, mock_openai_client, mock_tiktoken):
    """Test send_message handling of InvalidRequestError."""
    mock_openai_client.return_value.chat.completions.create.side_effect = openai.BadRequestError("Invalid request", "invalid_request")
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    response = client.send_message(messages)
    assert response is None
    mock_openai_client.return_value.chat.completions.create.assert_called_once()
    assert mock_tiktoken.encoding_for_model.call_count == 1


def test_openai_client_send_message_rate_limit_error(mock_config, mock_openai_client, mock_tiktoken):
     """Test send_message handling of RateLimitError."""
     mock_openai_client.return_value.chat.completions.create.side_effect = openai.RateLimitError("rate limit error", "rate_limit")
     client = OpenAIClient()
     messages = [{"role": "user", "content": "test message"}]
     response = client.send_message(messages, max_attempts=2)
     assert response is None
     assert mock_openai_client.return_value.chat.completions.create.call_count == 2
     assert mock_tiktoken.encoding_for_model.call_count == 2

def test_openai_client_send_message_non_terminal_error(mock_config, mock_openai_client, mock_tiktoken):
    """Test send_message handling of NonTerminalError."""
    mock_openai_client.return_value.chat.completions.create.side_effect = NonTerminalError("non-terminal error")
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    response = client.send_message(messages, max_attempts=2)
    assert response is None
    assert mock_openai_client.return_value.chat.completions.create.call_count == 2
    assert mock_tiktoken.encoding_for_model.call_count == 2


def test_openai_client_send_message_generic_error(mock_config, mock_openai_client, mock_tiktoken):
    """Test send_message handling of generic exceptions."""
    mock_openai_client.return_value.chat.completions.create.side_effect = Exception("generic error")
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    response = client.send_message(messages, max_attempts=2)
    assert response is None
    assert mock_openai_client.return_value.chat.completions.create.call_count == 2
    assert mock_tiktoken.encoding_for_model.call_count == 2

def test_openai_client_raw_model_call(mock_config, mock_openai_client):
    """Test that _raw_model_call calls the API with the correct parameters."""
    client = OpenAIClient()
    chat_api_params = {
         "messages": [{"role": "user", "content": "test message"}],
            "temperature": 0.3,
            "max_tokens": 1024,
            "top_p": 0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "stop": [],
            "timeout": 30.0,
            "stream": False,
            "n": 1,
    }
    client._raw_model_call("gpt-4", chat_api_params)
    mock_openai_client.return_value.chat.completions.create.assert_called_once_with(
         model="gpt-4",
         messages=[{'role': 'user', 'content': 'test message'}],
         temperature=0.3,
         max_tokens=1024,
         top_p=0,
         frequency_penalty=0.0,
         presence_penalty=0.0,
         stop=[],
         timeout=30.0,
         stream=False,
         n=1,
    )

def test_openai_client_raw_model_response_extractor(mock_config):
    """Test that _raw_model_response_extractor extracts the response correctly."""
    client = OpenAIClient()
    response = MagicMock(choices=[MagicMock(message=MagicMock(to_dict=MagicMock(return_value={'content': 'test response'})))])
    extracted_response = client._raw_model_response_extractor(response)
    assert extracted_response == {'content': 'test response'}

def test_openai_client_count_tokens_valid(mock_config, mock_tiktoken):
    """Test _count_tokens with a valid model and messages."""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    tokens = client._count_tokens(messages, "gpt-4-0613")
    assert tokens == 9
    assert mock_tiktoken.encoding_for_model.call_count == 1
    assert mock_tiktoken.get_encoding.call_count == 0

def test_openai_client_count_tokens_not_implemented(mock_config, mock_tiktoken):
    """Test _count_tokens with a model that is not implemented."""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    with pytest.raises(NotImplementedError, match=r"num_tokens_from_messages\(\) is not implemented for model test_model"):
        client._count_tokens(messages, "test_model")
    assert mock_tiktoken.encoding_for_model.call_count == 1
    assert mock_tiktoken.get_encoding.call_count == 0


def test_openai_client_count_tokens_key_error(mock_config, mock_tiktoken):
    """Test _count_tokens with a model that is not found."""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    mock_tiktoken.encoding_for_model.side_effect = KeyError("model not found")
    tokens = client._count_tokens(messages, "test_model")
    assert tokens == 9
    assert mock_tiktoken.encoding_for_model.call_count == 1
    assert mock_tiktoken.get_encoding.call_count == 1


def test_openai_client_count_tokens_exception(mock_config, mock_tiktoken):
    """Test _count_tokens with a generic error during token counting."""
    client = OpenAIClient()
    messages = [{"role": "user", "content": "test message"}]
    mock_tiktoken.encoding_for_model.side_effect = Exception("test error")
    tokens = client._count_tokens(messages, "gpt-4")
    assert tokens is None
    assert mock_tiktoken.encoding_for_model.call_count == 1


def test_openai_client_save_cache(mock_config, tmp_path):
    """Test that _save_cache saves the API cache to disk."""
    client = OpenAIClient()
    client.cache_file_name = str(tmp_path / "test_cache.pickle")
    client.api_cache = {"test_key": "test_value"}
    client._save_cache()
    assert os.path.exists(client.cache_file_name)
    with open(client.cache_file_name, "rb") as f:
        loaded_cache = pickle.load(f)
    assert loaded_cache == {"test_key": "test_value"}

def test_openai_client_load_cache_existing(mock_config, tmp_path):
    """Test that _load_cache loads the API cache from disk."""
    client = OpenAIClient()
    client.cache_file_name = str(tmp_path / "test_cache.pickle")
    with open(client.cache_file_name, "wb") as f:
        pickle.dump({"test_key": "test_value"}, f)
    loaded_cache = client._load_cache()
    assert loaded_cache == {"test_key": "test_value"}

def test_openai_client_load_cache_not_existing(mock_config, tmp_path):
    """Test that _load_cache returns an empty dictionary if the cache file does not exist."""
    client = OpenAIClient()
    client.cache_file_name = str(tmp_path / "test_cache.pickle")
    loaded_cache = client._load_cache()
    assert loaded_cache == {}

def test_openai_client_get_embedding(mock_config, mock_embedding):
    """Test that get_embedding calls the API and returns the embedding."""
    client = OpenAIClient()
    embedding = client.get_embedding("test text")
    assert embedding == [0.1, 0.2, 0.3]
    mock_embedding.return_value.embeddings.create.assert_called_once_with(input=["test text"], model="text-embedding-3-small")

def test_openai_client_raw_embedding_model_call(mock_config, mock_embedding):
    """Test that _raw_embedding_model_call calls the API with the correct parameters."""
    client = OpenAIClient()
    client._raw_embedding_model_call("test text", "test_model")
    mock_embedding.return_value.embeddings.create.assert_called_once_with(input=["test text"], model="test_model")

def test_openai_client_raw_embedding_model_response_extractor(mock_config):
    """Test that _raw_embedding_model_response_extractor extracts the embedding correctly."""
    client = OpenAIClient()
    response = MagicMock(data=[MagicMock(embedding=[0.1, 0.2, 0.3])])
    extracted_embedding = client._raw_embedding_model_response_extractor(response)
    assert extracted_embedding == [0.1, 0.2, 0.3]


###########################################################################
# AzureClient tests
###########################################################################
def test_azure_client_initialization(mock_config):
    """Test that AzureClient initializes correctly."""
    client = AzureClient()
    assert client.cache_api_calls is True
    assert client.cache_file_name == "test_cache.pickle"
    assert hasattr(client, "api_cache")

def test_azure_client_setup_from_config(mock_config, mock_azure_client):
    """Test that AzureClient sets up the Azure OpenAI client correctly."""
    with patch.dict(os.environ, {"AZURE_OPENAI_ENDPOINT": "https://test.azure.com", "AZURE_OPENAI_KEY":"test_key"}):
         client = AzureClient()
         client._setup_from_config()
    mock_azure_client.assert_called_once()

def test_azure_client_raw_model_call(mock_config, mock_azure_client):
    """Test that _raw_model_call calls the Azure API with the correct parameters."""
    client = AzureClient()
    chat_api_params = {
         "messages": [{"role": "user", "content": "test message"}],
            "temperature": 0.3,
            "max_tokens": 1024,
            "top_p": 0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "stop": [],
            "timeout": 30.0,
            "stream": False,
            "n": 1,
    }
    client._raw_model_call("gpt-4", chat_api_params)
    mock_azure_client.return_value.chat.completions.create.assert_called_once_with(
         model="gpt-4",
         messages=[{'role': 'user', 'content': 'test message'}],
         temperature=0.3,
         max_tokens=1024,
         top_p=0,
         frequency_penalty=0.0,
         presence_penalty=0.0,
         stop=[],
         timeout=30.0,
         stream=False,
         n=1,
    )

def test_azure_client_get_embedding(mock_config, mock_azure_embedding):
    """Test that get_embedding calls the API and returns the embedding."""
    client = AzureClient()
    with patch.dict(os.environ, {"AZURE_OPENAI_ENDPOINT": "https://test.azure.com", "AZURE_OPENAI_KEY":"test_key"}):
        embedding = client.get_embedding("test text")
    assert embedding == [0.1, 0.2, 0.3]
    mock_azure_embedding.return_value.embeddings.create.assert_called_once_with(input=["test text"], model="text-embedding-3-small")

def test_azure_client_raw_embedding_model_call(mock_config, mock_azure_embedding):
    """Test that _raw_embedding_model_call calls the API with the correct parameters."""
    client = AzureClient()
    with patch.dict(os.environ, {"AZURE_OPENAI_ENDPOINT": "https://test.azure.com", "AZURE_OPENAI_KEY":"test_key"}):
         client._raw_embedding_model_call("test text", "test_model")
    mock_azure_embedding.return_value.embeddings.create.assert_called_once_with(input=["test text"], model="test_model")


###########################################################################
# Client Registry Tests
###########################################################################

def test_register_client():
    """Test that register_client registers a client correctly."""
    class MockClient:
        pass
    register_client("test_api", MockClient)
    assert "test_api" in _api_type_to_client
    assert _api_type_to_client["test_api"] == MockClient

def test_get_client_for_api_type():
    """Test that _get_client_for_api_type returns the correct client."""
    class MockClient:
        pass
    register_client("test_api", MockClient)
    client = _api_type_to_client["test_api"]
    retrieved_client = _api_type_to_client["test_api"]
    assert client == retrieved_client

def test_get_client_for_api_type_not_found():
    """Test that _get_client_for_api_type raises a ValueError if the API type is not found."""
    with pytest.raises(ValueError, match=r"API type test_api is not supported. Please check the 'config.ini' file."):
        _get_client_for_api_type("test_api")

def test_client_default(mock_config, mock_openai_client):
    """Test that client() returns the default client based on the configuration."""
    retrieved_client = client()
    assert isinstance(retrieved_client, OpenAIClient)


def test_client_override(mock_config, mock_azure_client):
    """Test that client() returns the overridden client if force_api_type is used."""
    force_api_type("azure")
    retrieved_client = client()
    assert isinstance(retrieved_client, AzureClient)

def test_force_api_type():
    """Test that force_api_type correctly overrides the API type."""
    force_api_type("test_api")
    assert _api_type_override == "test_api"


def test_force_api_cache(mock_config):
     """Test that force_api_cache correctly overrides the cache settings."""
     force_api_cache(False, "new_cache.pickle")
     for client in _api_type_to_client.values():
         assert client.cache_api_calls is False
         assert client.cache_file_name == "new_cache.pickle"

     force_api_cache(True)
     for client in _api_type_to_client.values():
         assert client.cache_api_calls is True
         assert client.cache_file_name == "test_cache.pickle"

def test_force_default_value():
    """Test that force_default_value correctly overrides the default configuration values."""
    force_default_value("model", "test_model")
    assert default["model"] == "test_model"

    force_default_value("max_tokens", 2048)
    assert default["max_tokens"] == 2048

    with pytest.raises(ValueError, match=r"Key invalid_key is not a valid configuration key."):
        force_default_value("invalid_key", "test_value")
```