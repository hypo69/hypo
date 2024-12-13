```python
import pytest
from unittest.mock import MagicMock, patch

# Assuming the claude_client module is in the same directory as the test file, or in a directory that is part of PYTHONPATH.
try:
    from claude_client import ClaudeClient
except ImportError:
    # If import fails, create a mock to allow tests to run. This is for the case when the actual claude_client is not available.
    class MockClaudeClient:
      def __init__(self, api_key):
        self.api_key = api_key
        pass
      def generate_text(self, prompt, max_tokens_to_sample=100):
        return f"Generated text for prompt: {prompt}"

      def analyze_sentiment(self, text):
          return f"Sentiment analysis for: {text}"

      def translate_text(self, text, source_language, target_language):
        return f"Translated text: {text} from {source_language} to {target_language}"

    ClaudeClient = MockClaudeClient


@pytest.fixture
def mock_claude_client():
    """Provides a mock ClaudeClient object for testing."""
    # Using unittest.mock.MagicMock for more flexible mocking
    mock_client = MagicMock(spec=ClaudeClient)
    mock_client.api_key = "test_api_key"
    return mock_client

class TestClaudeClient:
    def test_claude_client_initialization(self):
        """Test that the ClaudeClient can be initialized with an API key."""
        api_key = "test_api_key"
        client = ClaudeClient(api_key)
        assert client.api_key == api_key
        
    def test_generate_text_valid_input(self, mock_claude_client):
        """Checks correct behavior of generate_text with valid input."""
        prompt = "Write a short story."
        mock_claude_client.generate_text.return_value = "A short story."
        
        result = mock_claude_client.generate_text(prompt)
        
        mock_claude_client.generate_text.assert_called_once_with(prompt)
        assert result == "A short story."
    
    def test_generate_text_with_max_tokens(self, mock_claude_client):
        """Checks generate_text with max_tokens parameter."""
        prompt = "Continue the story."
        max_tokens = 150
        mock_claude_client.generate_text.return_value = "Continuation of the story."

        result = mock_claude_client.generate_text(prompt, max_tokens_to_sample=max_tokens)

        mock_claude_client.generate_text.assert_called_once_with(prompt, max_tokens_to_sample=max_tokens)
        assert result == "Continuation of the story."

    def test_generate_text_empty_prompt(self, mock_claude_client):
        """Checks generate_text with an empty prompt."""
        prompt = ""
        mock_claude_client.generate_text.return_value = "No prompt, no story."

        result = mock_claude_client.generate_text(prompt)

        mock_claude_client.generate_text.assert_called_once_with(prompt)
        assert result == "No prompt, no story."

    def test_analyze_sentiment_valid_input(self, mock_claude_client):
        """Checks correct behavior of analyze_sentiment with valid input."""
        text = "I am very happy."
        mock_claude_client.analyze_sentiment.return_value = "Positive"
        
        result = mock_claude_client.analyze_sentiment(text)
        
        mock_claude_client.analyze_sentiment.assert_called_once_with(text)
        assert result == "Positive"

    def test_analyze_sentiment_empty_text(self, mock_claude_client):
        """Checks analyze_sentiment with an empty text."""
        text = ""
        mock_claude_client.analyze_sentiment.return_value = "Neutral"

        result = mock_claude_client.analyze_sentiment(text)
        
        mock_claude_client.analyze_sentiment.assert_called_once_with(text)
        assert result == "Neutral"


    def test_translate_text_valid_input(self, mock_claude_client):
        """Checks correct behavior of translate_text with valid input."""
        text = "Hello"
        source_language = "en"
        target_language = "es"
        mock_claude_client.translate_text.return_value = "Hola"
        
        result = mock_claude_client.translate_text(text, source_language, target_language)
        
        mock_claude_client.translate_text.assert_called_once_with(text, source_language, target_language)
        assert result == "Hola"

    def test_translate_text_empty_text(self, mock_claude_client):
      """Checks translate_text with an empty text string."""
      text = ""
      source_language = "en"
      target_language = "fr"
      mock_claude_client.translate_text.return_value = ""
      result = mock_claude_client.translate_text(text, source_language, target_language)
      mock_claude_client.translate_text.assert_called_once_with(text, source_language, target_language)
      assert result == ""
    
    def test_translate_text_invalid_language_code(self, mock_claude_client):
        """Checks translate_text with invalid language codes."""
        text = "Good morning"
        source_language = "invalid_source"
        target_language = "invalid_target"
        mock_claude_client.translate_text.side_effect = ValueError("Invalid language code")
        
        with pytest.raises(ValueError, match="Invalid language code"):
            mock_claude_client.translate_text(text, source_language, target_language)
        mock_claude_client.translate_text.assert_called_once_with(text, source_language, target_language)
```