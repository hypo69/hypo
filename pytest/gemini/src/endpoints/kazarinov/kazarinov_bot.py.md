```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path
from types import SimpleNamespace
from telegram import Update, User, Message
from telegram.ext import CallbackContext

from src.endpoints.kazarinov.kazarinov_bot import KazarinovTelegramBot
from src import gs
from src.ai.gemini import GoogleGenerativeAI


# Mock the necessary dependencies and settings
@pytest.fixture(autouse=True)
def mock_dependencies():
    gs.credentials = SimpleNamespace(
        telegram=SimpleNamespace(
            hypo69_test_bot="test_bot_token",
            hypo69_kazarinov_bot="prod_bot_token",
        ),
        gemini=SimpleNamespace(
            kazarinov="test_api_key",
        ),
    )
    gs.path = SimpleNamespace(
        endpoints = Path("./tests") ,
        
    )
    gs.path.endpoints.joinpath('kazarinov').mkdir(exist_ok=True)
    
    with open(gs.path.endpoints.joinpath('kazarinov','kazarinov.json'),'w') as f:
        f.write('{"mode":"test", "webdriver_name":"firefox"}')
        
    
    gs.host_name = "test_host"

    return 


@pytest.fixture
def mock_google_generative_ai():
    """Mocks the GoogleGenerativeAI class."""
    with patch("src.endpoints.kazarinov.kazarinov_bot.GoogleGenerativeAI") as MockGoogleGenerativeAI:
        mock_instance = MockGoogleGenerativeAI.return_value
        mock_instance.chat = AsyncMock(return_value="Mocked Gemini response")
        yield mock_instance



@pytest.fixture
def mock_update():
    """Provides a mock Update object."""
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 12345
    return update


@pytest.fixture
def mock_context():
    """Provides a mock CallbackContext object."""
    return MagicMock(spec=CallbackContext)


# Test for initialization with default mode
def test_kazarinov_bot_init_default(mock_dependencies):
    """Tests initialization with default mode."""
    kt = KazarinovTelegramBot()
    assert kt.token == "test_bot_token"
    assert kt.config.mode == "test"
    assert kt.config.webdriver_name == "firefox"


# Test for initialization with 'test' mode
def test_kazarinov_bot_init_test_mode(mock_dependencies):
    """Tests initialization with 'test' mode."""
    kt = KazarinovTelegramBot(mode="test")
    assert kt.token == "test_bot_token"
    assert kt.config.mode == "test"
    assert kt.config.webdriver_name == "firefox"


# Test for initialization with 'prod' mode
def test_kazarinov_bot_init_prod_mode(mock_dependencies):
    """Tests initialization with 'prod' mode."""
    kt = KazarinovTelegramBot(mode="prod")
    assert kt.token == "prod_bot_token"
    assert kt.config.mode == "test" # should be read from file


# Test for handle_message with '?' command
@pytest.mark.asyncio
async def test_handle_message_help_command(mock_update, mock_context, mock_dependencies):
    """Tests handling of the '?' command."""
    kt = KazarinovTelegramBot()
    mock_update.message.text = "?"
    mock_update.message.reply_photo = AsyncMock()
    await kt.handle_message(mock_update, mock_context)
    mock_update.message.reply_photo.assert_called_once()


# Test for handle_message with a URL
@pytest.mark.asyncio
async def test_handle_message_url(mock_update, mock_context, mock_dependencies, monkeypatch):
    """Tests handling of a URL message."""
    kt = KazarinovTelegramBot()
    mock_update.message.text = "https://example.com"
    mock_handle_url = AsyncMock()
    monkeypatch.setattr(kt, "handle_url", mock_handle_url)
    await kt.handle_message(mock_update, mock_context)
    mock_handle_url.assert_called_once_with(mock_update, mock_context)


# Test for handle_message with a next command
@pytest.mark.asyncio
async def test_handle_message_next_command(mock_update, mock_context, mock_dependencies, monkeypatch):
    """Tests handling of a next command."""
    kt = KazarinovTelegramBot()
    mock_update.message.text = "--next"
    mock_handle_next_command = AsyncMock()
    monkeypatch.setattr(kt, "handle_next_command", mock_handle_next_command)
    await kt.handle_message(mock_update, mock_context)
    mock_handle_next_command.assert_called_once_with(mock_update)


# Test for handle_message with regular text
@pytest.mark.asyncio
async def test_handle_message_regular_text(mock_update, mock_context, mock_dependencies, mock_google_generative_ai):
    """Tests handling of regular text message."""
    kt = KazarinovTelegramBot()
    mock_update.message.text = "Hello, how are you?"
    mock_update.message.reply_text = AsyncMock()
    await kt.handle_message(mock_update, mock_context)
    mock_google_generative_ai.chat.assert_called_once_with("Hello, how are you?")
    mock_update.message.reply_text.assert_called_once_with("Mocked Gemini response")


# Test for handle_message with empty text
@pytest.mark.asyncio
async def test_handle_message_empty_text(mock_update, mock_context, mock_dependencies, mock_google_generative_ai):
    """Tests handling of empty text message."""
    kt = KazarinovTelegramBot()
    mock_update.message.text = ""
    mock_update.message.reply_text = AsyncMock()
    await kt.handle_message(mock_update, mock_context)
    mock_google_generative_ai.chat.assert_called_once_with("")
    mock_update.message.reply_text.assert_called_once_with("Mocked Gemini response")
```