```python
import pytest
from unittest.mock import MagicMock
from google.cloud import dialogflow_v2 as dialogflow

# Mock the necessary Dialogflow classes and methods
@pytest.fixture
def mock_dialogflow_client():
    mock_client = MagicMock()
    mock_sessions_client = MagicMock()
    mock_intents_client = MagicMock()

    mock_client.SessionsClient.return_value = mock_sessions_client
    mock_client.IntentsClient.return_value = mock_intents_client

    mock_sessions_client.detect_intent.return_value = MagicMock(
        query_result=MagicMock(intent=MagicMock(display_name="Test Intent"))
    )

    mock_intents_client.list_intents.return_value = MagicMock(
        intents=[MagicMock(display_name="Intent1"), MagicMock(display_name="Intent2")]
    )

    mock_intents_client.create_intent.return_value = MagicMock(
        display_name="NewIntent",
        training_phrases=[MagicMock(parts=[MagicMock(text="new phrase"), MagicMock(text="another phrase")])],
        messages=[MagicMock(text=MagicMock(text=["This is a new intent"]))]
    )
    
    mock_intents_client.delete_intent.return_value = None

    return mock_client

# Mock the dialogflow module
@pytest.fixture
def mock_dialogflow(mocker, mock_dialogflow_client):
    mocker.patch('src.ai.dialogflow.dialogflow', new=mock_dialogflow_client)
    return mock_dialogflow_client


from src.ai.dialogflow import Dialogflow


def test_dialogflow_initialization(mock_dialogflow):
    """Test the Dialogflow client initialization."""
    project_id = "test-project-id"
    session_id = "test-session-id"
    dialogflow_client = Dialogflow(project_id, session_id)

    assert dialogflow_client.project_id == project_id
    assert dialogflow_client.session_id == session_id
    mock_dialogflow.SessionsClient.assert_called_once()


def test_detect_intent(mock_dialogflow):
    """Test the intent detection functionality."""
    project_id = "test-project-id"
    session_id = "test-session-id"
    dialogflow_client = Dialogflow(project_id, session_id)
    query = "Hello"
    response = dialogflow_client.detect_intent(query)

    mock_dialogflow.SessionsClient().detect_intent.assert_called_once()
    assert response.query_result.intent.display_name == "Test Intent"


def test_list_intents(mock_dialogflow):
    """Test the list intents functionality."""
    project_id = "test-project-id"
    session_id = "test-session-id"
    dialogflow_client = Dialogflow(project_id, session_id)
    intents = dialogflow_client.list_intents()

    mock_dialogflow.IntentsClient().list_intents.assert_called_once()
    assert len(intents) == 2
    assert intents[0].display_name == "Intent1"


def test_create_intent(mock_dialogflow):
    """Test the intent creation functionality."""
    project_id = "test-project-id"
    session_id = "test-session-id"
    dialogflow_client = Dialogflow(project_id, session_id)
    
    display_name="NewIntent"
    training_phrases_parts=["new phrase", "another phrase"]
    message_texts=["This is a new intent"]
    
    new_intent = dialogflow_client.create_intent(
        display_name=display_name,
        training_phrases_parts=training_phrases_parts,
        message_texts=message_texts
    )

    mock_dialogflow.IntentsClient().create_intent.assert_called_once()
    assert new_intent.display_name == display_name
    assert len(new_intent.training_phrases) == 1
    assert len(new_intent.training_phrases[0].parts) == 2
    assert new_intent.training_phrases[0].parts[0].text == training_phrases_parts[0]
    assert len(new_intent.messages) == 1
    assert new_intent.messages[0].text.text[0] == message_texts[0]


def test_delete_intent(mock_dialogflow):
    """Test the intent deletion functionality."""
    project_id = "test-project-id"
    session_id = "test-session-id"
    dialogflow_client = Dialogflow(project_id, session_id)
    intent_id = "test-intent-id"
    
    dialogflow_client.delete_intent(intent_id)

    mock_dialogflow.IntentsClient().delete_intent.assert_called_once()
```