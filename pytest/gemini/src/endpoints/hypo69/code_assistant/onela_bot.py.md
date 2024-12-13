```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from telegram import Update, Message, Document, User
from telegram.ext import CallbackContext
from pathlib import Path

from src.endpoints.hypo69.code_assistant.onela_bot import OnelaBot
from src import gs  # Assuming gs is a module or object defined somewhere


# Fixtures
@pytest.fixture
def mock_update():
    """Provides a mock Update object for testing."""
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 12345
    return update


@pytest.fixture
def mock_context():
    """Provides a mock CallbackContext object for testing."""
    return MagicMock(spec=CallbackContext)


@pytest.fixture
def mock_file():
    """Provides a mock File object for testing."""
    file = MagicMock()
    file.download_to_drive = AsyncMock(return_value=Path("test_file.txt"))
    return file


@pytest.fixture
def mock_document(mock_file):
    """Provides a mock Document object for testing."""
    document = MagicMock(spec=Document)
    document.get_file = AsyncMock(return_value=mock_file)
    return document


@pytest.fixture
def onela_bot():
    """Provides an instance of OnelaBot."""
    return OnelaBot()


# Tests for OnelaBot.handle_message
@pytest.mark.asyncio
async def test_handle_message_valid_input(onela_bot, mock_update, mock_context):
    """Checks correct behavior with valid text input."""
    mock_update.message.text = "Hello, bot!"
    mock_update.message.reply_text = AsyncMock()
    mock_update.effective_user.id = 123
    
    with patch.object(onela_bot.model, 'chat', new_callable=AsyncMock) as mock_chat:
        mock_chat.return_value = "Hello, user!"
        await onela_bot.handle_message(mock_update, mock_context)
        mock_chat.assert_called_once_with("Hello, bot!")
        mock_update.message.reply_text.assert_called_once_with("Hello, user!")


@pytest.mark.asyncio
async def test_handle_message_exception(onela_bot, mock_update, mock_context):
    """Checks correct handling of exception during model call."""
    mock_update.message.text = "Error please"
    mock_update.message.reply_text = AsyncMock()
    with patch.object(onela_bot.model, 'chat', new_callable=AsyncMock) as mock_chat:
        mock_chat.side_effect = Exception("Test exception")
        with patch("src.endpoints.hypo69.code_assistant.onela_bot.logger.error") as mock_logger_error:
             await onela_bot.handle_message(mock_update, mock_context)
             mock_logger_error.assert_called_once()
        mock_update.message.reply_text.assert_not_called()


# Tests for OnelaBot.handle_document
@pytest.mark.asyncio
async def test_handle_document_valid_input(onela_bot, mock_update, mock_context, mock_document):
    """Checks correct behavior with a valid document input."""
    mock_update.message.document = mock_document
    mock_update.message.reply_text = AsyncMock()
    
    await onela_bot.handle_document(mock_update, mock_context)
    mock_document.get_file.assert_called_once()
    mock_update.message.reply_text.assert_called()
    #check call count since it is called twice
    assert mock_update.message.reply_text.call_count == 2


@pytest.mark.asyncio
async def test_handle_document_exception(onela_bot, mock_update, mock_context, mock_document):
    """Checks correct handling of exception during document processing."""
    mock_update.message.document = mock_document
    mock_update.message.reply_text = AsyncMock()
    with patch.object(mock_document, 'get_file', new_callable=AsyncMock) as mock_get_file:
        mock_get_file.side_effect = Exception("File processing error")
        with patch("src.endpoints.hypo69.code_assistant.onela_bot.logger.error") as mock_logger_error:
             await onela_bot.handle_document(mock_update, mock_context)
             mock_logger_error.assert_called_once()
        mock_update.message.reply_text.assert_not_called()


@pytest.mark.asyncio
async def test_bot_run_polling():
    """Checks if the bot can start polling without issues."""
    bot = OnelaBot()
    with patch.object(bot.application, "run_polling", new_callable=AsyncMock) as mock_run_polling:
        await bot.application.run_polling()
        mock_run_polling.assert_called_once()
```