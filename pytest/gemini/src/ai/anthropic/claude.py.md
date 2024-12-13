```python
import pytest
from unittest.mock import MagicMock
from hypotez.src.ai.anthropic.claude import ClaudeClient
import anthropic

# Fixture definitions
@pytest.fixture
def mock_anthropic_client():
    """Mocks the anthropic.Client for testing."""
    mock_client = MagicMock(spec=anthropic.Client)
    return mock_client

@pytest.fixture
def claude_client(mock_anthropic_client):
    """Provides a ClaudeClient instance with a mocked anthropic client."""
    return ClaudeClient(api_key="test-api-key")

# Tests for ClaudeClient class
def test_claude_client_initialization(mock_anthropic_client):
    """Checks if ClaudeClient initializes the client with the given API key."""
    api_key = "test-api-key"
    client = ClaudeClient(api_key=api_key)
    assert client.client is not None
    mock_anthropic_client.assert_not_called()


def test_generate_text_valid_input(claude_client, mock_anthropic_client):
    """Checks correct behavior of generate_text with valid input."""
    prompt = "Write a short poem"
    mock_anthropic_client.completion.return_value = {"completion": "Roses are red..."}
    
    result = claude_client.generate_text(prompt)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=prompt,
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "Roses are red..."

def test_generate_text_custom_max_tokens(claude_client, mock_anthropic_client):
    """Checks if generate_text handles a custom max_tokens_to_sample correctly."""
    prompt = "Write a short poem"
    max_tokens = 50
    mock_anthropic_client.completion.return_value = {"completion": "Test response"}
    
    result = claude_client.generate_text(prompt, max_tokens_to_sample=max_tokens)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=prompt,
            model="claude-v1",
            max_tokens_to_sample=max_tokens,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "Test response"

def test_generate_text_empty_prompt(claude_client, mock_anthropic_client):
    """Checks behavior of generate_text with an empty prompt."""
    prompt = ""
    mock_anthropic_client.completion.return_value = {"completion": "No response"}
    
    result = claude_client.generate_text(prompt)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=prompt,
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "No response"

def test_analyze_sentiment_valid_text(claude_client, mock_anthropic_client):
    """Checks correct behavior of analyze_sentiment with valid text."""
    text = "This is great news!"
    mock_anthropic_client.completion.return_value = {"completion": "Positive"}
    
    result = claude_client.analyze_sentiment(text)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=f"Analyze the sentiment of the following text: {text}",
            model="claude-v1",
            max_tokens_to_sample=50,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "Positive"

def test_analyze_sentiment_empty_text(claude_client, mock_anthropic_client):
    """Checks behavior of analyze_sentiment with empty text."""
    text = ""
    mock_anthropic_client.completion.return_value = {"completion": "Neutral"}
    
    result = claude_client.analyze_sentiment(text)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=f"Analyze the sentiment of the following text: {text}",
            model="claude-v1",
            max_tokens_to_sample=50,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "Neutral"

def test_translate_text_valid_input(claude_client, mock_anthropic_client):
    """Checks correct behavior of translate_text with valid input."""
    text = "Hello"
    source_language = "en"
    target_language = "es"
    mock_anthropic_client.completion.return_value = {"completion": "Hola"}
    
    result = claude_client.translate_text(text, source_language, target_language)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == "Hola"

def test_translate_text_empty_text(claude_client, mock_anthropic_client):
    """Checks behavior of translate_text with empty text."""
    text = ""
    source_language = "en"
    target_language = "fr"
    mock_anthropic_client.completion.return_value = {"completion": ""}
    
    result = claude_client.translate_text(text, source_language, target_language)
    
    mock_anthropic_client.completion.assert_called_once_with(
            prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
        )
    assert result == ""

def test_translate_text_invalid_lang_codes(claude_client, mock_anthropic_client):
     """Checks the behavior of translate_text with invalid language codes"""
     text = "Good morning"
     source_language = "invalid_code"
     target_language = "invalid_target"
     mock_anthropic_client.completion.return_value = {"completion": "Translation Failed"}

     result = claude_client.translate_text(text,source_language,target_language)

     mock_anthropic_client.completion.assert_called_once_with(
            prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
         )
     assert result == "Translation Failed"
```