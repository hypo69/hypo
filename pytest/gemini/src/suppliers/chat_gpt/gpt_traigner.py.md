```python
import pytest
import pandas as pd
from pathlib import Path
from unittest.mock import MagicMock, patch
from hypotez.src.suppliers.chat_gpt.gpt_traigner import GPT_Traigner
from src.utils.jjson import j_dumps
from src import gs


@pytest.fixture
def mock_gpt_gs(mocker):
    mock = mocker.patch('hypotez.src.suppliers.chat_gpt.gpt_traigner.GptGs')
    return mock.return_value

@pytest.fixture
def mock_driver(mocker):
    mock = mocker.patch('hypotez.src.suppliers.chat_gpt.gpt_traigner.Driver')
    driver_instance = mock.return_value
    driver_instance.execute_locator = MagicMock(return_value=[MagicMock(text='Test User'), MagicMock(text='Test Assistant')])
    return driver_instance

@pytest.fixture
def gpt_trainer_instance(mock_gpt_gs, mock_driver):
    return GPT_Traigner()

@pytest.fixture
def conversation_pair():
    return {"user": "Hello", "assistant": "Hi there"}


def test_determine_sentiment_positive(gpt_trainer_instance, conversation_pair):
    """Test determine_sentiment with a sentiment provided."""
    assert gpt_trainer_instance.determine_sentiment(conversation_pair, "positive") == "positive"

def test_determine_sentiment_negative(gpt_trainer_instance, conversation_pair):
    """Test determine_sentiment with an empty sentiment."""
    assert gpt_trainer_instance.determine_sentiment(conversation_pair, "") == "positive"


def test_determine_sentiment_no_sentiment(gpt_trainer_instance, conversation_pair):
    """Test determine_sentiment with no sentiment parameter. should return positive for default value"""
    assert gpt_trainer_instance.determine_sentiment(conversation_pair) == "positive"

def test_save_conversations_to_jsonl(gpt_trainer_instance, tmp_path):
    """Test save_conversations_to_jsonl with valid data."""
    data = [{"user": "Hello", "assistant": "Hi there"}, {"user": "How are you?", "assistant": "I'm fine"}]
    output_file = str(tmp_path / "test.jsonl")
    gpt_trainer_instance.save_conversations_to_jsonl(data, output_file)
    
    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert j_dumps(data[0]) + "\n" == lines[0]
        assert j_dumps(data[1]) + "\n" == lines[1]


def test_save_conversations_to_jsonl_empty_data(gpt_trainer_instance, tmp_path):
     """Test save_conversations_to_jsonl with empty data list."""
     data = []
     output_file = str(tmp_path / "test.jsonl")
     gpt_trainer_instance.save_conversations_to_jsonl(data, output_file)
     
     with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 0

def test_dump_downloaded_conversations(gpt_trainer_instance, mock_driver, mocker, tmp_path):
    """Test dump_downloaded_conversations with mocked file and driver."""
    # Setup mock file system and driver
    mock_glob = mocker.patch("pathlib.Path.glob", return_value=[tmp_path / "test.html"])
    mock_driver.execute_locator.side_effect = [
        [MagicMock(text='User 1'), MagicMock(text='User 2')],
        [MagicMock(text='Assistant 1'), MagicMock(text='Assistant 2')],
    ]

    # Set up the folder for mock files
    (tmp_path / 'chat_gpt' / 'conversation').mkdir(parents=True, exist_ok=True)
    gs.path.google_drive = tmp_path

    # Execute the method
    gpt_trainer_instance.dump_downloaded_conversations()

    # Assertions
    mock_glob.assert_called_once()
    mock_driver.get_url.assert_called_once()
    mock_driver.execute_locator.assert_called_with(gpt_trainer_instance.gs.locators.assistant)
    
    # Verify CSV output
    csv_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
    assert csv_file.exists()
    csv_data = pd.read_csv(csv_file)
    assert len(csv_data) == 2
    assert list(csv_data["content"]) == ['User 1', 'Assistant 1']
    assert list(csv_data["role"]) == ['user', 'assistant']
    
    # Verify JSONL output
    jsonl_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
    assert jsonl_file.exists()
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        jsonl_lines = f.readlines()
        assert len(jsonl_lines) == 2
        assert '"content":["User 1","Assistant 1"]' in jsonl_lines[0]
    
    # Verify TXT output
    txt_file = tmp_path / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
    assert txt_file.exists()
    with open(txt_file, 'r', encoding='utf-8') as f:
        txt_content = f.read()
        assert txt_content == "User 1 Assistant 1"

def test_dump_downloaded_conversations_no_data(gpt_trainer_instance, mock_driver, mocker, tmp_path):
    """Test dump_downloaded_conversations when no conversation data is found."""
    # Setup mock file system and driver
    mock_glob = mocker.patch("pathlib.Path.glob", return_value=[tmp_path / "test.html"])
    mock_driver.execute_locator.side_effect = [
        [],
        [],
    ]

    # Set up the folder for mock files
    (tmp_path / 'chat_gpt' / 'conversation').mkdir(parents=True, exist_ok=True)
    gs.path.google_drive = tmp_path
    # Execute the method
    gpt_trainer_instance.dump_downloaded_conversations()

    # Assertions
    mock_glob.assert_called_once()
    mock_driver.get_url.assert_called_once()
    mock_driver.execute_locator.assert_called_with(gpt_trainer_instance.gs.locators.assistant)
   
     # Verify no CSV output
    csv_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
    assert not csv_file.exists()

    # Verify no JSONL output
    jsonl_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
    assert not jsonl_file.exists()

    # Verify no TXT output
    txt_file = tmp_path / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
    assert not txt_file.exists()
    
def test_dump_downloaded_conversations_one_element(gpt_trainer_instance, mock_driver, mocker, tmp_path):
    """Test dump_downloaded_conversations when one of user or assistant elements is missed."""
    # Setup mock file system and driver
    mock_glob = mocker.patch("pathlib.Path.glob", return_value=[tmp_path / "test.html"])
    mock_driver.execute_locator.side_effect = [
        [MagicMock(text='User 1')],
        [MagicMock(text='Assistant 1')],
    ]

    # Set up the folder for mock files
    (tmp_path / 'chat_gpt' / 'conversation').mkdir(parents=True, exist_ok=True)
    gs.path.google_drive = tmp_path
    # Execute the method
    gpt_trainer_instance.dump_downloaded_conversations()

    # Assertions
    mock_glob.assert_called_once()
    mock_driver.get_url.assert_called_once()
    mock_driver.execute_locator.assert_called_with(gpt_trainer_instance.gs.locators.assistant)

    # Verify CSV output
    csv_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
    assert csv_file.exists()
    csv_data = pd.read_csv(csv_file)
    assert len(csv_data) == 1
    assert list(csv_data["content"]) == ['User 1', 'Assistant 1']
    assert list(csv_data["role"]) == ['user', 'assistant']
    
    # Verify JSONL output
    jsonl_file = tmp_path / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
    assert jsonl_file.exists()
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        jsonl_lines = f.readlines()
        assert len(jsonl_lines) == 1
        assert '"content":["User 1","Assistant 1"]' in jsonl_lines[0]
    
    # Verify TXT output
    txt_file = tmp_path / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
    assert txt_file.exists()
    with open(txt_file, 'r', encoding='utf-8') as f:
        txt_content = f.read()
        assert txt_content == "User 1 Assistant 1"
```