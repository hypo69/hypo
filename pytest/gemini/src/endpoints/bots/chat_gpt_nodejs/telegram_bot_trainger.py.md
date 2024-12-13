```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from telegram import Update, Message, Document, Voice, File
from telegram.ext import CallbackContext
from src.bots.openai_bots.telegram_bot_trainger import start, help_command, handle_document, handle_message, handle_voice, model
import tempfile
from src.utils.convertors.tts import recognizer, text_to_speech


@pytest.fixture
def mock_update():
    """Provides a mock Update object."""
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    return update

@pytest.fixture
def mock_context():
    """Provides a mock CallbackContext object."""
    return MagicMock(spec=CallbackContext)


@pytest.mark.asyncio
async def test_start_command(mock_update, mock_context):
    """Checks if the /start command sends a welcome message."""
    await start(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_once_with(
        'Hello! I am your simple bot. Type /help to see available commands.'
    )


@pytest.mark.asyncio
async def test_help_command(mock_update, mock_context):
    """Checks if the /help command sends the help message."""
    await help_command(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_once_with(
        'Available commands:\n/start - Start the bot\n/help - Show this help message'
    )


@pytest.mark.asyncio
async def test_handle_document_valid(mock_update, mock_context):
    """Checks if the document handler correctly reads and processes a valid document."""
    mock_file = MagicMock(spec=File)
    mock_file.download_to_drive = AsyncMock(return_value=f"{tempfile.gettempdir()}/test_file.txt")
    mock_update.message.document = MagicMock(spec=Document)
    mock_update.message.document.get_file = AsyncMock(return_value=mock_file)

    with open(f"{tempfile.gettempdir()}/test_file.txt", 'w') as f:
        f.write('test content')

    mock_model_send = MagicMock(return_value="Model response")
    model.send_message = mock_model_send

    await handle_document(mock_update, mock_context)
    mock_model_send.assert_called_once()
    mock_update.message.reply_text.assert_called_once_with('Model response')


@pytest.mark.asyncio
async def test_handle_message_valid(mock_update, mock_context):
    """Checks if the message handler correctly processes a text message."""
    mock_update.message.text = "Test message"
    mock_model_send = MagicMock(return_value="Model response")
    model.send_message = mock_model_send
    await handle_message(mock_update, mock_context)
    mock_model_send.assert_called_once_with("Test message")
    mock_update.message.reply_text.assert_called_once_with("Model response")

@pytest.mark.asyncio
async def test_handle_voice_valid(mock_update, mock_context):
    """Checks if the voice message handler correctly processes a voice message."""
    mock_file = MagicMock(spec=File)
    mock_file.file_path = 'test_voice_path'
    mock_update.message.voice = MagicMock(spec=Voice)
    mock_update.message.voice.get_file = AsyncMock(return_value=mock_file)

    mock_recognizer = MagicMock(return_value="Recognized text")
    mock_tts = AsyncMock(return_value='test_tts_path')

    with patch('src.bots.openai_bots.telegram_bot_trainger.recognizer', mock_recognizer), \
            patch('src.bots.openai_bots.telegram_bot_trainger.text_to_speech', mock_tts), \
            patch('builtins.open', MagicMock()) as mock_open:
        mock_model_send = MagicMock(return_value="Model response")
        model.send_message = mock_model_send

        await handle_voice(mock_update, mock_context)
        mock_recognizer.assert_called_once_with(audio_url='test_voice_path')
        mock_model_send.assert_called_once_with("Recognized text")
        mock_update.message.reply_text.assert_called_once_with("Model response")
        mock_tts.assert_called_once_with("Model response")
        mock_update.message.reply_audio.assert_called_once()
        
```