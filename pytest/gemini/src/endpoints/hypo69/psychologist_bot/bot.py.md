```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path
from src.endpoints.hypo69.psychologist_bot.bot import PsychologistTelgrambot
from src.bots.telegram import TelegramBot
from src.ai.gemini import GoogleGenerativeAI
from telegram import Update, User, Message, Document
from telegram.ext import CallbackContext
from src import gs
import asyncio


@pytest.fixture
def mock_gs():
    """Mocks the gs module."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.gs") as mock:
        mock.now = "test_time"
        mock.credentials.telegram.hypo69_psychologist_bot = "test_token"
        mock.credentials.gemini.hypo69_psychologist_bot = "test_gemini_key"
        mock.path.google_drive = Path("/mocked/google/drive")
        yield mock

@pytest.fixture
def mock_read_text_file():
    """Mocks the read_text_file function."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.read_text_file") as mock:
        mock.return_value = "test_system_instruction"
        yield mock

@pytest.fixture
def mock_recursively_read_text_files():
    """Mocks the recursively_read_text_files function."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.recursively_read_text_files") as mock:
        mock.return_value = ["test_question_1", "test_question_2"]
        yield mock

@pytest.fixture
def mock_google_generative_ai():
    """Mocks the GoogleGenerativeAI class."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.GoogleGenerativeAI") as mock:
        mock_instance = MagicMock()
        mock_instance.ask.return_value = "test_answer"
        mock.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def mock_save_text_file():
    """Mocks the save_text_file function."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.save_text_file") as mock:
        yield mock
    
@pytest.fixture
def mock_driver():
    """Mocks the Driver class."""
    with patch("src.endpoints.hypo69.psychologist_bot.bot.Driver") as mock_driver:
        mock_instance = MagicMock()
        mock_driver.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def mock_telegram_bot():
     with patch("src.endpoints.hypo69.psychologist_bot.bot.TelegramBot", autospec=True) as mock_telegram_bot:
        mock_instance = MagicMock()
        mock_instance.start = AsyncMock()
        mock_instance.handle_document = AsyncMock(return_value='mocked_file_content')
        mock_telegram_bot.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def bot(mock_gs, mock_read_text_file, mock_recursively_read_text_files, 
        mock_google_generative_ai, mock_driver, mock_telegram_bot):
    """Creates an instance of PsychologistTelgrambot with mocked dependencies."""
    return PsychologistTelgrambot()

@pytest.fixture
def mock_update():
    """Creates a mock Update object."""
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 12345
    return update

@pytest.fixture
def mock_context():
    """Creates a mock CallbackContext object."""
    return MagicMock(spec=CallbackContext)


def test_psychologist_bot_init(bot, mock_gs, mock_read_text_file, mock_recursively_read_text_files, 
                            mock_google_generative_ai, mock_driver, mock_telegram_bot):
    """Tests the initialization of the PsychologistTelgrambot."""
    assert bot.token == "test_token"
    assert bot.system_instruction == "test_system_instruction"
    assert bot.questions_list == ["test_question_1", "test_question_2"]
    assert isinstance(bot.model, MagicMock)
    assert isinstance(bot.d, MagicMock)
    
    mock_read_text_file.assert_called_once_with(
        Path("/mocked/google/drive/hypo69_psychologist_bot/prompts/chat_system_instruction.txt")
    )
    mock_recursively_read_text_files.assert_called_once_with(
        Path("/mocked/google/drive/hypo69_psychologist_bot/prompts/train_data/q"), ["*.*"], as_list=True
    )
    mock_google_generative_ai.assert_called_once_with(
         api_key="test_gemini_key",
        system_instruction="test_system_instruction",
        generation_config={"response_mime_type": "text/plain"}
    )
    mock_telegram_bot.assert_called_once_with("test_token")
    mock_driver.assert_called_once()

def test_register_handlers(bot):
    """Tests if handlers are registered correctly."""
    assert bot.application.add_handler.call_count == 5

def test_start_command(bot, mock_update, mock_context):
    """Tests the /start command."""
    asyncio.run(bot.start(mock_update, mock_context))
    mock_update.message.reply_text.assert_called_once_with('Hi! I am a smart assistant psychologist.')
    bot.application.bot.start.assert_called_once()

def test_handle_message_valid_input(bot, mock_update, mock_save_text_file, mock_google_generative_ai):
    """Tests handle_message with valid input."""
    mock_update.message.text = "test_message"
    asyncio.run(bot.handle_message(mock_update, None))
    mock_save_text_file.assert_called_once()
    mock_google_generative_ai.ask.assert_called_once_with(q="test_message", history_file='12345.txt')
    mock_update.message.reply_text.assert_called_with("test_answer")

def test_get_handler_for_url_suppliers(bot):
    """Tests get_handler_for_url with a supplier URL."""
    url = "https://morlevi.co.il/test"
    handler = bot.get_handler_for_url(url)
    assert handler == bot.handle_suppliers_response

def test_get_handler_for_url_onetab(bot):
     """Tests get_handler_for_url with a onetab URL."""
     url = "https://www.one-tab.com/test"
     handler = bot.get_handler_for_url(url)
     assert handler == bot.handle_onetab_response

def test_get_handler_for_url_no_match(bot):
    """Tests get_handler_for_url with no matching URL."""
    url = "https://example.com/test"
    handler = bot.get_handler_for_url(url)
    assert handler is None

@patch("src.endpoints.hypo69.psychologist_bot.bot.PsychologistTelgrambot.mexiron", new_callable=MagicMock)
def test_handle_suppliers_response_success(mock_mexiron, bot, mock_update):
    """Tests handle_suppliers_response with successful mexiron run."""
    mock_mexiron.run_scenario = AsyncMock(return_value=True)
    asyncio.run(bot.handle_suppliers_response(mock_update, "https://morlevi.co.il/test"))
    mock_update.message.reply_text.assert_called_with("Готово!")

@patch("src.endpoints.hypo69.psychologist_bot.bot.PsychologistTelgrambot.mexiron", new_callable=MagicMock)
def test_handle_suppliers_response_failure(mock_mexiron, bot, mock_update):
    """Tests handle_suppliers_response with failed mexiron run."""
    mock_mexiron.run_scenario = AsyncMock(return_value=False)
    asyncio.run(bot.handle_suppliers_response(mock_update, "https://morlevi.co.il/test"))
    mock_update.message.reply_text.assert_called_with("Хуёвенько. Попробуй еще раз")

@patch("src.endpoints.hypo69.psychologist_bot.bot.PsychologistTelgrambot.mexiron", new_callable=MagicMock)
def test_handle_onetab_response_success(mock_mexiron, bot, mock_update):
    """Tests handle_onetab_response with successful mexiron run."""
    mock_mexiron.run_scenario = AsyncMock(return_value=True)
    asyncio.run(bot.handle_onetab_response(mock_update, "https://www.one-tab.com/test"))
    mock_update.message.reply_text.assert_called_with("Готово!\nСсылку я вышлю на WhatsApp")

@patch("src.endpoints.hypo69.psychologist_bot.bot.PsychologistTelgrambot.mexiron", new_callable=MagicMock)
def test_handle_onetab_response_failure(mock_mexiron, bot, mock_update):
    """Tests handle_onetab_response with failed mexiron run."""
    mock_mexiron.run_scenario = AsyncMock(return_value=False)
    asyncio.run(bot.handle_onetab_response(mock_update, "https://www.one-tab.com/test"))
    mock_update.message.reply_text.assert_called_with("Хуёвенько. Попробуй ещё раз")

def test_handle_next_command_success(bot, mock_update, mock_google_generative_ai):
    """Tests handle_next_command with successful question retrieval."""
    asyncio.run(bot.handle_next_command(mock_update))
    mock_google_generative_ai.ask.assert_called()
    assert mock_update.message.reply_text.call_count == 2

def test_handle_next_command_exception(bot, mock_update, mock_google_generative_ai):
    """Tests handle_next_command with an exception during question retrieval."""
    mock_google_generative_ai.ask.side_effect = Exception("Test Exception")
    asyncio.run(bot.handle_next_command(mock_update))
    mock_update.message.reply_text.assert_called_with('Произошла ошибка при чтении вопросов.')

def test_handle_document(bot, mock_update, mock_context, mock_telegram_bot):
    """Tests handling of document uploads."""
    mock_update.message.document = MagicMock(spec=Document)
    asyncio.run(bot.handle_document(mock_update, mock_context))
    mock_telegram_bot.handle_document.assert_called_once_with(mock_update,mock_context)
    mock_update.message.reply_text.assert_called_with('Received your document. Content: mocked_file_content')
```