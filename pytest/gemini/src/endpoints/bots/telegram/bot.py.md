```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path
import asyncio
from telegram import Update, Message, Voice, Document, File
from telegram.ext import CallbackContext

from src.endpoints.bots.telegram.bot import TelegramBot

# Mock the logger
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.endpoints.bots.telegram.bot.logger') as mock:
        yield mock

# Mock gs.path
@pytest.fixture
def mock_gs_path():
    with patch('src.endpoints.bots.telegram.bot.gs.path') as mock:
        mock.temp = Path('./temp')
        yield mock

# Mock gs.credentials
@pytest.fixture
def mock_gs_credentials():
    with patch('src.endpoints.bots.telegram.bot.gs.credentials.telegram.bot') as mock:
         mock.kazarinov = "test_token"
         yield mock


# Fixture for creating a TelegramBot instance
@pytest.fixture
def bot(mock_gs_credentials):
    return TelegramBot(token=mock_gs_credentials.kazarinov)

# Fixture for creating a mock Update object
@pytest.fixture
def mock_update():
    update_mock = AsyncMock(spec=Update)
    update_mock.message = AsyncMock(spec=Message)
    return update_mock

# Fixture for creating a mock CallbackContext object
@pytest.fixture
def mock_context():
    context_mock = AsyncMock(spec=CallbackContext)
    context_mock.bot = AsyncMock()
    return context_mock


# Test for TelegramBot initialization
def test_telegrambot_initialization(mock_gs_credentials):
    """Test that TelegramBot is initialized with a token."""
    token = mock_gs_credentials.kazarinov
    bot = TelegramBot(token)
    assert bot.application is not None
    assert bot.application._bot.token == token


def test_register_handlers(bot):
    """Test that command and message handlers are registered."""
    assert len(bot.application.handlers[0]) > 0


# Test cases for /start command
@pytest.mark.asyncio
async def test_start_command(bot, mock_update, mock_context):
    """Test that /start command sends a greeting message."""
    await bot.start(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with(
        'Hello! I am your simple bot. Type /help to see available commands.'
    )


# Test cases for /help command
@pytest.mark.asyncio
async def test_help_command(bot, mock_update, mock_context):
    """Test that /help command sends a help message."""
    await bot.help_command(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with(
        'Available commands:\n'
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/sendpdf - Send a PDF file'
    )


# Test cases for /sendpdf command
@pytest.mark.asyncio
async def test_send_pdf_valid_file(bot, mock_update, mock_context, tmp_path):
    """Test that /sendpdf command sends a PDF file."""
    # Create a dummy PDF file
    pdf_file_path = tmp_path / "test.pdf"
    with open(pdf_file_path, "wb") as f:
        f.write(b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Kids[]/Count 0>>endobj")

    bot.update = mock_update
    bot.context = mock_context
    await bot.send_pdf(pdf_file_path)
    mock_update.message.reply_document.assert_called()

@pytest.mark.asyncio
async def test_send_pdf_invalid_file(bot, mock_update, mock_context, mock_logger):
    """Test /sendpdf command with an invalid file."""
    bot.update = mock_update
    bot.context = mock_context
    invalid_file_path = "invalid.pdf"  # A file that doesn't exist
    await bot.send_pdf(invalid_file_path)
    mock_update.message.reply_text.assert_called_with('Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')
    mock_logger.error.assert_called()


# Test cases for handle_voice command
@pytest.mark.asyncio
async def test_handle_voice_valid_voice(bot, mock_update, mock_context, mock_gs_path):
    """Test handling of valid voice message."""
    # Mock voice and file
    mock_voice = AsyncMock(spec=Voice)
    mock_voice.file_id = "test_file_id"
    mock_update.message.voice = mock_voice

    mock_file = AsyncMock(spec=File)
    mock_file.download_to_drive = AsyncMock()
    mock_context.bot.get_file = AsyncMock(return_value=mock_file)

    bot.update = mock_update
    bot.context = mock_context

    await bot.handle_voice(mock_update, mock_context)
    mock_context.bot.get_file.assert_called_with(mock_voice.file_id)
    mock_file.download_to_drive.assert_called_with(mock_gs_path.temp / f'{mock_voice.file_id}.ogg')
    mock_update.message.reply_text.assert_called_with('Распознанный текст: Распознавание голоса ещё не реализовано.')

@pytest.mark.asyncio
async def test_handle_voice_exception(bot, mock_update, mock_context, mock_logger):
    """Test exception handling for voice messages."""
    # Mock exception during processing
    mock_update.message.voice = AsyncMock()
    mock_context.bot.get_file = AsyncMock(side_effect=Exception("Test Exception"))
    bot.update = mock_update
    bot.context = mock_context
    await bot.handle_voice(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with('Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')
    mock_logger.error.assert_called()


# Test cases for handle_document command
@pytest.mark.asyncio
async def test_handle_document_valid_document(bot, mock_update, mock_context, tmp_path):
    """Test handling of a valid document."""
    # Mock document and file
    mock_document = AsyncMock(spec=Document)
    mock_file = AsyncMock(spec=File)
    mock_file.download_to_drive = AsyncMock(return_value=tmp_path / 'test.txt')
    mock_document.get_file = AsyncMock(return_value=mock_file)
    mock_update.message.document = mock_document

    # create a dummy text file for read_text_file mock
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
      f.write("Test text content.")

    bot.update = mock_update
    bot.context = mock_context
    with patch('src.endpoints.bots.telegram.bot.read_text_file', return_value="Test text content.") as mock_read_text_file:
       result = await bot.handle_document(mock_update, mock_context)
       assert result == "Test text content."
       mock_read_text_file.assert_called_once()

@pytest.mark.asyncio
async def test_handle_document_exception(bot, mock_update, mock_context):
    """Test document handling with an exception."""
    mock_update.message.document = AsyncMock()
    mock_update.message.document.get_file = AsyncMock(side_effect=Exception("Test Exception"))

    bot.update = mock_update
    bot.context = mock_context

    with pytest.raises(Exception, match="Test Exception"):
        await bot.handle_document(mock_update, mock_context)


# Test cases for handle_message command
@pytest.mark.asyncio
async def test_handle_message_valid_text(bot, mock_update, mock_context):
    """Test handling of a valid text message."""
    mock_update.message.text = "Test message"
    bot.update = mock_update
    bot.context = mock_context
    result = await bot.handle_message(mock_update, mock_context)
    assert result == "Test message"


# Test cases for handle_log command
@pytest.mark.asyncio
async def test_handle_log_valid_log(bot, mock_update, mock_context, mock_logger):
    """Test handling of a log message."""
    mock_update.message.text = "Test log message"
    bot.update = mock_update
    bot.context = mock_context
    await bot.handle_log(mock_update, mock_context)
    mock_logger.info.assert_called_with('Received log message: Test log message')
    mock_update.message.reply_text.assert_called_with("Log received and processed.")


@pytest.mark.asyncio
async def test_main_function(mock_gs_credentials):
    """Test that main function initializes and runs the bot."""
    with patch('src.endpoints.bots.telegram.bot.TelegramBot') as MockTelegramBot:
         mock_bot = MagicMock()
         MockTelegramBot.return_value = mock_bot
         mock_bot.application = MagicMock()
         mock_bot.application.run_polling = MagicMock()
         from src.endpoints.bots.telegram.bot import main
         main()

         MockTelegramBot.assert_called_once_with(mock_gs_credentials.kazarinov)
         mock_bot.application.run_polling.assert_called_once()
```