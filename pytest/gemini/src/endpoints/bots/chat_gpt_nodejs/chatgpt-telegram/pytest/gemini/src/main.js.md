```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from main import bot # Assuming main.py is the name of the file

# Mocking necessary external dependencies and objects
@pytest.fixture
def mock_telegraf():
    """Mocks the Telegraf bot object and its methods."""
    mock_bot = MagicMock()
    mock_bot.command = MagicMock(return_value=None)
    mock_bot.on = MagicMock(return_value=None)
    mock_bot.launch = MagicMock(return_value=None)
    mock_bot.stop = MagicMock(return_value=None)
    return mock_bot

@pytest.fixture
def mock_ctx():
    """Mocks the context object with relevant properties."""
    mock_ctx = MagicMock()
    mock_ctx.reply = AsyncMock()
    mock_ctx.telegram = MagicMock()
    mock_ctx.telegram.getFileLink = AsyncMock(return_value=MagicMock(href='test_link'))
    mock_ctx.message = MagicMock()
    mock_ctx.message.voice = MagicMock(file_id='test_file_id')
    mock_ctx.message.from = MagicMock(id=12345)
    mock_ctx.message.text = 'test message'
    mock_ctx.session = None 
    return mock_ctx

@pytest.fixture
def mock_ogg():
    """Mocks the ogg module."""
    mock_ogg = MagicMock()
    mock_ogg.create = AsyncMock(return_value='test_ogg_path')
    mock_ogg.toMp3 = AsyncMock(return_value='test_mp3_path')
    return mock_ogg

@pytest.fixture
def mock_openai():
    """Mocks the openai module."""
    mock_openai = MagicMock()
    mock_openai.transcription = AsyncMock(return_value='transcribed text')
    mock_openai.chat = AsyncMock(return_value=MagicMock(content='response content'))
    mock_openai.roles = MagicMock(USER='user')
    return mock_openai

@pytest.fixture
def mock_removeFile():
    """Mocks the removeFile function"""
    mock_removeFile = MagicMock()
    return mock_removeFile


# Tests for the /start command handler
def test_start_command_handler(mock_telegraf, mock_ctx):
    """Test the /start command handler to check if it replies with ctx.message."""
    bot.command('start', mock_telegraf.command)
    mock_telegraf.command.side_effect[0](mock_ctx)
    mock_ctx.reply.assert_called_once()

# Tests for voice message handler
@pytest.mark.asyncio
async def test_voice_message_handler_success(mock_telegraf, mock_ctx, mock_ogg, mock_openai, mock_removeFile):
    """Test the voice message handler with successful processing."""
    with patch('main.ogg', mock_ogg), patch('main.openai', mock_openai), patch('main.removeFile', mock_removeFile):
        bot.on('voice', mock_telegraf.on)
        await mock_telegraf.on.side_effect[0](mock_ctx)
        mock_ctx.reply.assert_called()
        assert mock_ctx.reply.call_count == 3
        mock_ogg.create.assert_called_once()
        mock_ogg.toMp3.assert_called_once()
        mock_removeFile.assert_called_once()
        mock_openai.transcription.assert_called_once()
        mock_openai.chat.assert_called_once()

@pytest.mark.asyncio
async def test_voice_message_handler_error(mock_telegraf, mock_ctx, mock_ogg, mock_openai, mock_removeFile):
    """Test the voice message handler when an error occurs during processing."""
    with patch('main.ogg', mock_ogg), patch('main.openai', mock_openai), patch('main.removeFile', mock_removeFile):
       mock_ogg.create.side_effect = Exception("Test Error")
       bot.on('voice', mock_telegraf.on)
       await mock_telegraf.on.side_effect[0](mock_ctx)
       mock_ctx.reply.assert_called_once() #Check if it called only one time the initial message before the error

# Tests for text message handler
@pytest.mark.asyncio
async def test_text_message_handler_success(mock_telegraf, mock_ctx):
    """Test the text message handler with valid input and session initialization."""
    with patch('main.processTextToChat', new_callable=AsyncMock) as mock_processTextToChat:
        bot.on('text', mock_telegraf.on)
        await mock_telegraf.on.side_effect[0](mock_ctx)
        mock_ctx.reply.assert_called_once()
        mock_processTextToChat.assert_called_once_with(mock_ctx, 'test message')
        assert mock_ctx.session is not None #Check if session is initialize

@pytest.mark.asyncio
async def test_text_message_handler_error(mock_telegraf, mock_ctx):
    """Test the text message handler when an error occurs."""
    with patch('main.processTextToChat', new_callable=AsyncMock) as mock_processTextToChat:
        mock_processTextToChat.side_effect = Exception('Test Error')
        bot.on('text', mock_telegraf.on)
        await mock_telegraf.on.side_effect[0](mock_ctx)
        mock_ctx.reply.assert_called_once()


def test_bot_launch(mock_telegraf):
     """Test bot launch"""
     bot.launch = mock_telegraf.launch
     bot.launch()
     mock_telegraf.launch.assert_called_once()

def test_bot_stop_sigint(mock_telegraf):
    """Test bot stop with SIGINT"""
    bot.stop = mock_telegraf.stop
    with patch('main.process') as mock_process:
        mock_process.once.side_effect[0]()
    mock_telegraf.stop.assert_called_once_with('SIGINT')

def test_bot_stop_sigterm(mock_telegraf):
    """Test bot stop with SIGTERM"""
    bot.stop = mock_telegraf.stop
    with patch('main.process') as mock_process:
      mock_process.once.side_effect[1]()
    mock_telegraf.stop.assert_called_once_with('SIGTERM')
```