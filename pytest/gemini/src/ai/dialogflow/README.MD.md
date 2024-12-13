```python
import pytest
from unittest.mock import MagicMock
from google.cloud import dialogflow_v2 as dialogflow

# Mock the Dialogflow client for testing
@pytest.fixture
def mock_dialogflow_client():
    mock_client = MagicMock()
    mock_session_client = MagicMock()
    mock_intent_client = MagicMock()
    mock_client.SessionsClient.return_value = mock_session_client
    mock_client.IntentsClient.return_value = mock_intent_client
    return mock_client, mock_session_client, mock_intent_client

# Mock the detect_intent response
@pytest.fixture
def mock_detect_intent_response():
    mock_response = MagicMock()
    mock_response.query_result.intent.display_name = "TestIntent"
    mock_response.query_result.fulfillment_text = "Hello, user!"
    return mock_response

# Mock the list_intents response
@pytest.fixture
def mock_list_intents_response():
    mock_response = MagicMock()
    mock_response.intents = [
        MagicMock(display_name="Intent1"),
        MagicMock(display_name="Intent2")
    ]
    return mock_response


# Mock the create_intent response
@pytest.fixture
def mock_create_intent_response():
    mock_response = MagicMock()
    mock_response.display_name = "NewIntent"
    mock_response.training_phrases = [
        MagicMock(parts=[MagicMock(text="new phrase")]),
        MagicMock(parts=[MagicMock(text="another phrase")])
    ]
    mock_response.messages = [
        MagicMock(text=MagicMock(text=["This is a new intent"]))
    ]
    return mock_response


# Mock the delete_intent response
@pytest.fixture
def mock_delete_intent_response():
    mock_response = MagicMock()
    return mock_response


# Test for Dialogflow class instantiation
def test_dialogflow_init(mock_dialogflow_client):
    """Tests the initialization of the Dialogflow class."""
    mock_client, _, _ = mock_dialogflow_client
    project_id = "test-project"
    session_id = "test-session"
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow(project_id, session_id, client=mock_client)
    assert dialogflow_instance.project_id == project_id
    assert dialogflow_instance.session_id == session_id
    assert dialogflow_instance.session_path.startswith(f"projects/{project_id}/agent/sessions/{session_id}")

# Tests for detect_intent method
def test_detect_intent_valid_input(mock_dialogflow_client, mock_detect_intent_response):
    """Tests detect_intent with valid text input."""
    mock_client, mock_session_client, _ = mock_dialogflow_client
    mock_session_client.detect_intent.return_value = mock_detect_intent_response
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    response = dialogflow_instance.detect_intent("Hello")
    assert response.query_result.intent.display_name == "TestIntent"
    assert response.query_result.fulfillment_text == "Hello, user!"


def test_detect_intent_empty_input(mock_dialogflow_client, mock_detect_intent_response):
    """Tests detect_intent with empty input string."""
    mock_client, mock_session_client, _ = mock_dialogflow_client
    mock_session_client.detect_intent.return_value = mock_detect_intent_response
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    response = dialogflow_instance.detect_intent("")
    assert response.query_result.intent.display_name == "TestIntent"
    assert response.query_result.fulfillment_text == "Hello, user!"

def test_detect_intent_invalid_input_type(mock_dialogflow_client):
    """Tests detect_intent with invalid input type."""
    mock_client, _, _ = mock_dialogflow_client
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    with pytest.raises(AttributeError):
        dialogflow_instance.detect_intent(123)  # Invalid input type


# Tests for list_intents method
def test_list_intents_valid(mock_dialogflow_client, mock_list_intents_response):
    """Tests list_intents with valid response."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.list_intents.return_value = mock_list_intents_response
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    intents = dialogflow_instance.list_intents()
    assert len(intents) == 2
    assert intents[0].display_name == "Intent1"
    assert intents[1].display_name == "Intent2"

def test_list_intents_no_intents(mock_dialogflow_client):
    """Tests list_intents when no intents are found."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.list_intents.return_value = MagicMock(intents=[])
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    intents = dialogflow_instance.list_intents()
    assert intents == []

def test_list_intents_exception(mock_dialogflow_client):
    """Tests list_intents handling of exceptions."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.list_intents.side_effect = Exception("API Error")
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    with pytest.raises(Exception, match="API Error"):
      dialogflow_instance.list_intents()

# Tests for create_intent method
def test_create_intent_valid_input(mock_dialogflow_client, mock_create_intent_response):
    """Tests create_intent with valid inputs."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.create_intent.return_value = mock_create_intent_response
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    new_intent = dialogflow_instance.create_intent(
        display_name="NewIntent",
        training_phrases_parts=["new phrase", "another phrase"],
        message_texts=["This is a new intent"]
    )
    assert new_intent.display_name == "NewIntent"
    assert len(new_intent.training_phrases) == 2
    assert len(new_intent.messages) == 1
    
def test_create_intent_empty_input(mock_dialogflow_client):
    """Tests create_intent with empty training phrases."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    with pytest.raises(TypeError): # should raise exception
      dialogflow_instance.create_intent(display_name="NewIntent")

def test_create_intent_exception(mock_dialogflow_client):
     """Tests create_intent handling of exceptions."""
     mock_client, _, mock_intent_client = mock_dialogflow_client
     mock_intent_client.create_intent.side_effect = Exception("API Error")
     from src.ai.dialogflow import Dialogflow
     dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
     with pytest.raises(Exception, match="API Error"):
       dialogflow_instance.create_intent(
          display_name="NewIntent",
          training_phrases_parts=["new phrase", "another phrase"],
          message_texts=["This is a new intent"]
      )


# Tests for delete_intent method
def test_delete_intent_valid(mock_dialogflow_client, mock_delete_intent_response):
    """Tests delete_intent with valid intent ID."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.delete_intent.return_value = mock_delete_intent_response
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    response = dialogflow_instance.delete_intent("test-intent-id")
    assert response == mock_delete_intent_response

def test_delete_intent_invalid_id(mock_dialogflow_client):
    """Tests delete_intent with an empty intent ID."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    with pytest.raises(Exception):
        dialogflow_instance.delete_intent("")

def test_delete_intent_exception(mock_dialogflow_client):
    """Tests delete_intent handling of exceptions."""
    mock_client, _, mock_intent_client = mock_dialogflow_client
    mock_intent_client.delete_intent.side_effect = Exception("API Error")
    from src.ai.dialogflow import Dialogflow
    dialogflow_instance = Dialogflow("test-project", "test-session", client=mock_client)
    with pytest.raises(Exception, match="API Error"):
        dialogflow_instance.delete_intent("test-intent-id")
```