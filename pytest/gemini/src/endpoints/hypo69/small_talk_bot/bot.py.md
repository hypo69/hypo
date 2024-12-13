```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from telegram import Update, Message, User, Document, Voice
from telegram.ext import CallbackContext

from src.endpoints.hypo69.small_talk_bot.bot import PsychologistTelgrambot
from src.utils.file import read_text_file, recursively_read_text_files
from src.ai.gemini import GoogleGenerativeAI

@pytest.fixture
def mock_gs(mocker):
    """Mocks the global settings object."""
    mock_gs = MagicMock()
    mock_gs.credentials.telegram.hypo69_psychologist_bot = "test_token"
    mock_gs.credentials.gemini.hypo69_psychologist_bot = "test_gemini_key"
    mock_gs.path.google_drive = MagicMock()
    mock_gs.path.google_drive.__truediv__.return_value = "mock_path"
    mock_gs.now = "mock_timestamp"
    mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.gs", mock_gs)
    return mock_gs

@pytest.fixture
def mock_read_text_file(mocker):
    """Mocks the read_text_file function."""
    mock_read = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.read_text_file")
    mock_read.return_value = "test system instruction"
    return mock_read

@pytest.fixture
def mock_recursively_read_text_files(mocker):
    """Mocks the recursively_read_text_files function."""
    mock_read = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.recursively_read_text_files")
    mock_read.return_value = ["question1", "question2"]
    return mock_read

@pytest.fixture
def mock_google_generative_ai(mocker):
    """Mocks the GoogleGenerativeAI class."""
    mock_ai = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.GoogleGenerativeAI")
    mock_ai_instance = MagicMock()
    mock_ai.return_value = mock_ai_instance
    mock_ai_instance.ask = MagicMock(return_value="test answer")
    return mock_ai_instance

@pytest.fixture
def mock_telegram_bot(mocker):
     """Mocks the TelegramBot class."""
     mock_bot = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.TelegramBot", autospec=True)
     mock_bot_instance = MagicMock()
     mock_bot.return_value = mock_bot_instance
     mock_bot_instance.start = AsyncMock()
     mock_bot_instance.handle_document = AsyncMock(return_value="test_content")
     return mock_bot_instance

@pytest.fixture
def mock_save_text_file(mocker):
    """Mocks the save_text_file function."""
    mock_save = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.save_text_file")
    return mock_save

@pytest.fixture
def mock_driver(mocker):
    """Mocks the Driver class."""
    mock_driver = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.Driver")
    mock_driver_instance = MagicMock()
    mock_driver.return_value = mock_driver_instance
    return mock_driver_instance

@pytest.fixture
def bot_instance(mock_gs, mock_read_text_file, mock_recursively_read_text_files, mock_google_generative_ai, mock_telegram_bot, mock_driver):
    """Creates an instance of the PsychologistTelgrambot with mocked dependencies."""
    return PsychologistTelgrambot()

@pytest.fixture
def mock_update():
    """Mocks the Telegram Update object."""
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 12345
    return update

@pytest.fixture
def mock_context():
    """Mocks the Telegram CallbackContext object."""
    return MagicMock(spec=CallbackContext)

@pytest.mark.asyncio
async def test_psychologist_telegrambot_init(bot_instance, mock_gs, mock_read_text_file, mock_recursively_read_text_files, mock_google_generative_ai, mock_driver, mock_telegram_bot):
    """Tests the initialization of the PsychologistTelgrambot."""
    assert bot_instance.token == "test_token"
    assert bot_instance.system_instruction == "test system instruction"
    assert bot_instance.questions_list == ["question1", "question2"]
    assert mock_gs.path.google_drive.__truediv__.call_count == 3
    mock_read_text_file.assert_called_once()
    mock_recursively_read_text_files.assert_called_once()
    mock_google_generative_ai.assert_called_once()
    mock_telegram_bot.assert_called_once()

@pytest.mark.asyncio
async def test_start_command(bot_instance, mock_update, mock_context, mock_telegram_bot):
    """Tests the /start command handler."""
    await bot_instance.start(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with('Hi! I am a smart assistant psychologist.')
    mock_telegram_bot.start.assert_called_once_with(mock_update, mock_context)


@pytest.mark.asyncio
async def test_handle_message(bot_instance, mock_update, mock_context, mock_google_generative_ai, mock_save_text_file):
    """Tests the handle_message function with a text message."""
    mock_update.message.text = "Hello bot"
    await bot_instance.handle_message(mock_update, mock_context)
    mock_google_generative_ai.ask.assert_called_once_with(q="Hello bot", history_file="12345.txt")
    mock_update.message.reply_text.assert_called_with("test answer")
    mock_save_text_file.assert_called_once()


@pytest.mark.asyncio
async def test_handle_message_with_url(bot_instance, mock_update, mock_context, mock_google_generative_ai):
    """Tests the handle_message function with a message containing URL (should not trigger URL-specific handlers)."""
    mock_update.message.text = "https://www.google.com"
    await bot_instance.handle_message(mock_update, mock_context)
    mock_google_generative_ai.ask.assert_called_once()

@pytest.mark.asyncio
async def test_get_handler_for_url_suppliers(bot_instance):
    """Tests get_handler_for_url with a suppliers URL."""
    url = "https://morlevi.co.il/some_path"
    handler = bot_instance.get_handler_for_url(url)
    assert handler == bot_instance.handle_suppliers_response

@pytest.mark.asyncio
async def test_get_handler_for_url_onetab(bot_instance):
    """Tests get_handler_for_url with a onetab URL."""
    url = "https://www.one-tab.com/some_path"
    handler = bot_instance.get_handler_for_url(url)
    assert handler == bot_instance.handle_onetab_response

@pytest.mark.asyncio
async def test_get_handler_for_url_no_match(bot_instance):
    """Tests get_handler_for_url with no matching URL."""
    url = "https://www.example.com"
    handler = bot_instance.get_handler_for_url(url)
    assert handler is None

@pytest.mark.asyncio
async def test_handle_suppliers_response_success(bot_instance, mock_update, mock_telegram_bot):
    """Tests handle_suppliers_response when mexiron.run_scenario succeeds."""
    mock_telegram_bot.mexiron.run_scenario = AsyncMock(return_value=True)
    await bot_instance.handle_suppliers_response(mock_update, "https://morlevi.co.il/test")
    mock_update.message.reply_text.assert_called_with('Готово!')

@pytest.mark.asyncio
async def test_handle_suppliers_response_failure(bot_instance, mock_update, mock_telegram_bot):
    """Tests handle_suppliers_response when mexiron.run_scenario fails."""
    mock_telegram_bot.mexiron.run_scenario = AsyncMock(return_value=False)
    await bot_instance.handle_suppliers_response(mock_update, "https://morlevi.co.il/test")
    mock_update.message.reply_text.assert_called_with('Хуёвенько. Попробуй еще раз')

@pytest.mark.asyncio
async def test_handle_onetab_response_success(bot_instance, mock_update, mock_telegram_bot):
    """Tests handle_onetab_response when mexiron.run_scenario succeeds."""
    mock_telegram_bot.mexiron.run_scenario = AsyncMock(return_value=True)
    await bot_instance.handle_onetab_response(mock_update, "https://www.one-tab.com/test")
    mock_update.message.reply_text.assert_called_with('Готово!\nСсылку я вышлю на WhatsApp')

@pytest.mark.asyncio
async def test_handle_onetab_response_failure(bot_instance, mock_update, mock_telegram_bot):
    """Tests handle_onetab_response when mexiron.run_scenario fails."""
    mock_telegram_bot.mexiron.run_scenario = AsyncMock(return_value=False)
    await bot_instance.handle_onetab_response(mock_update, "https://www.one-tab.com/test")
    mock_update.message.reply_text.assert_called_with('Хуёвенько. Попробуй ещё раз')

@pytest.mark.asyncio
async def test_handle_next_command_success(bot_instance, mock_update, mock_google_generative_ai):
    """Tests handle_next_command with successful question selection and response."""
    mock_google_generative_ai.ask.return_value = "answer"
    await bot_instance.handle_next_command(mock_update)
    mock_update.message.reply_text.assert_any_call("question1")
    mock_update.message.reply_text.assert_any_call("answer")
    mock_google_generative_ai.ask.assert_called_once()

@pytest.mark.asyncio
async def test_handle_next_command_exception(bot_instance, mock_update, mock_google_generative_ai, mocker):
    """Tests handle_next_command when an exception occurs."""
    mock_google_generative_ai.ask.side_effect = Exception("Test Exception")
    mock_logger = mocker.patch("src.endpoints.hypo69.small_talk_bot.bot.logger")

    await bot_instance.handle_next_command(mock_update)
    mock_logger.debug.assert_called_with("Ошибка чтения вопросов")
    mock_update.message.reply_text.assert_called_with('Произошла ошибка при чтении вопросов.')

@pytest.mark.asyncio
async def test_handle_document(bot_instance, mock_update, mock_context, mock_telegram_bot):
    """Tests handle_document method."""
    await bot_instance.handle_document(mock_update, mock_context)
    mock_telegram_bot.handle_document.assert_called_once_with(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with('Received your document. Content: test_content')
```