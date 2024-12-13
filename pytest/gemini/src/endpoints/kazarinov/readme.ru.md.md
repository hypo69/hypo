```python
import pytest
from unittest.mock import MagicMock, patch
from src.endpoints.kazarinov import kazarinov_bot, scenarios

# --- Mocking external dependencies ---
@pytest.fixture
def mock_one_tab_data():
    """Provides mock data for OneTab."""
    return {
        "tabs": [
            {"url": "https://one-tab.co.il/some_url1"},
            {"url": "https://morlevi.co.il/some_url2"},
        ]
    }

@pytest.fixture
def mock_get_data_from_onetab(mock_one_tab_data):
    """Mocks the function to get data from OneTab."""
    with patch('src.endpoints.kazarinov.kazarinov_bot.get_data_from_onetab', return_value=mock_one_tab_data) as mock:
        yield mock

@pytest.fixture
def mock_run_scenario( ):
    """Mocks the function to run the Mexiron scenario."""
    with patch('src.endpoints.kazarinov.kazarinov_bot.scenarios.run_scenario', return_value = True) as mock:
        yield mock
    
@pytest.fixture
def mock_run_scenario_fail( ):
    """Mocks the function to run the Mexiron scenario with fail."""
    with patch('src.endpoints.kazarinov.kazarinov_bot.scenarios.run_scenario', return_value = False) as mock:
        yield mock

@pytest.fixture
def mock_send_message():
    """Mocks the function to send message via Telegram bot."""
    with patch('src.endpoints.kazarinov.kazarinov_bot.bot.send_message') as mock:
        yield mock

# --- Tests for `handle_message` function ---

def test_handle_message_valid_onetab_url(mock_get_data_from_onetab, mock_run_scenario, mock_send_message):
    """Tests handle_message with a valid OneTab URL, checks bot success message."""
    
    update_mock = MagicMock()
    update_mock.message.text = "https://one-tab.co.il/valid_url"
    kazarinov_bot.handle_message(update_mock, None)
    
    mock_get_data_from_onetab.assert_called_once()
    mock_run_scenario.assert_called_once()
    mock_send_message.assert_called_once_with(chat_id=update_mock.message.chat_id, text="Done! I will send the link to WhatsApp")

def test_handle_message_valid_onetab_url_scenario_fail(mock_get_data_from_onetab, mock_run_scenario_fail, mock_send_message):
    """Tests handle_message with a valid OneTab URL, but checks fail of scenario"""
    update_mock = MagicMock()
    update_mock.message.text = "https://one-tab.co.il/valid_url"
    kazarinov_bot.handle_message(update_mock, None)
    
    mock_get_data_from_onetab.assert_called_once()
    mock_run_scenario_fail.assert_called_once()
    mock_send_message.assert_called_once_with(chat_id=update_mock.message.chat_id, text="Error running scenario")
   
def test_handle_message_invalid_onetab_url(mock_send_message):
    """Tests handle_message with an invalid OneTab URL, bot sends error message."""
    
    update_mock = MagicMock()
    update_mock.message.text = "https://invalid.url"
    kazarinov_bot.handle_message(update_mock, None)
    
    mock_send_message.assert_called_once_with(chat_id=update_mock.message.chat_id, text="Try again")
  
def test_handle_message_empty_message(mock_send_message):
    """Tests handle_message with an empty message, checks the bot error message"""
    update_mock = MagicMock()
    update_mock.message.text = ""
    kazarinov_bot.handle_message(update_mock, None)

    mock_send_message.assert_called_once_with(chat_id=update_mock.message.chat_id, text="Try again")

def test_handle_message_none_message(mock_send_message):
    """Tests handle_message with a None message, checks the bot error message"""
    update_mock = MagicMock()
    update_mock.message.text = None
    kazarinov_bot.handle_message(update_mock, None)

    mock_send_message.assert_called_once_with(chat_id=update_mock.message.chat_id, text="Try again")
```