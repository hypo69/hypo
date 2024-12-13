```python
import pytest
import os
import json
from unittest.mock import patch, MagicMock
from tinytroupe.factory import TinyFactory, TinyPersonFactory
from tinytroupe.agent import TinyPerson
from tinytroupe import utils
from tinytroupe.control import transactional
import logging

logger = logging.getLogger("tinytroupe")

# Fixture for a basic TinyFactory instance
@pytest.fixture
def tiny_factory():
    return TinyFactory()

# Fixture for a TinyPersonFactory instance
@pytest.fixture
def tiny_person_factory():
    return TinyPersonFactory(context_text="Test context")

# Fixture for a TinyPersonFactory instance with a simulation ID
@pytest.fixture
def tiny_person_factory_with_simulation_id():
    return TinyPersonFactory(context_text="Test context", simulation_id="sim123")

# Fixture for a TinyPerson instance
@pytest.fixture
def tiny_person():
    return TinyPerson("Test Person")

class MockOpenAIClient:
    def __init__(self, responses):
        self.responses = responses
        self.call_count = 0

    def send_message(self, messages, temperature=None):
        if self.call_count < len(self.responses):
             response = self.responses[self.call_count]
             self.call_count += 1
             return response
        else:
            return None
        
# Mock the openai_utils.client() to avoid actual API calls
@pytest.fixture(autouse=True)
def mock_openai_client():
    with patch("tinytroupe.factory.openai_utils.client") as mock_client:
        yield mock_client

# Mock the logger to avoid actual logging
@pytest.fixture(autouse=True)
def mock_logger():
    with patch("tinytroupe.factory.logger") as mock_logger:
        yield mock_logger


################################################################################
# Tests for TinyFactory
################################################################################
def test_tinyfactory_initialization(tiny_factory):
    """Tests if a TinyFactory is initialized with a unique name and optional simulation ID."""
    assert tiny_factory.name.startswith("Factory ")
    assert tiny_factory.simulation_id is None

def test_tinyfactory_initialization_with_simulation_id():
    """Tests if a TinyFactory is initialized with a unique name and a simulation ID."""
    factory = TinyFactory(simulation_id="sim123")
    assert factory.simulation_id == "sim123"

def test_tinyfactory_repr(tiny_factory):
    """Tests the string representation of a TinyFactory instance."""
    assert repr(tiny_factory) == f"TinyFactory(name='{tiny_factory.name}')"

def test_tinyfactory_add_factory(tiny_factory):
    """Tests if a factory is added to the list of all factories and an exception if not unique"""
    
    assert tiny_factory.name in TinyFactory.all_factories
    
    with pytest.raises(ValueError, match=f"Factory names must be unique, but '{tiny_factory.name}' is already defined."):
        TinyFactory.add_factory(tiny_factory) # attempt to add the same factory again.

def test_tinyfactory_clear_factories():
    """Tests if the list of all factories is cleared."""
    TinyFactory.clear_factories()
    assert not TinyFactory.all_factories

def test_tinyfactory_set_simulation_for_free_factories():
    """Tests if free factories are captured by a specific simulation scope."""
    simulation_mock = MagicMock()
    factory1 = TinyFactory()
    factory2 = TinyFactory(simulation_id="sim123") # already has simulation id
    TinyFactory.set_simulation_for_free_factories(simulation_mock)

    simulation_mock.add_factory.assert_called_once_with(factory1)


def test_tinyfactory_encode_decode_complete_state(tiny_factory):
    """Tests if the complete state of the factory can be encoded and decoded."""
    state = tiny_factory.encode_complete_state()
    new_factory = TinyFactory()
    new_factory.decode_complete_state(state)

    assert new_factory.name == tiny_factory.name
    assert new_factory.simulation_id == tiny_factory.simulation_id

################################################################################
# Tests for TinyPersonFactory
################################################################################
def test_tinypersonfactory_initialization(tiny_person_factory):
    """Tests if a TinyPersonFactory is initialized with the correct attributes."""
    assert tiny_person_factory.context_text == "Test context"
    assert tiny_person_factory.person_prompt_template_path.endswith('prompts/generate_person.mustache')
    assert tiny_person_factory.generated_minibios == []
    assert tiny_person_factory.generated_names == []
    assert tiny_person_factory.simulation_id is None

def test_tinypersonfactory_initialization_with_simulation_id(tiny_person_factory_with_simulation_id):
    """Tests if a TinyPersonFactory is initialized with the correct attributes and a simulation id."""
    assert tiny_person_factory_with_simulation_id.simulation_id == "sim123"
    

def test_tinypersonfactory_generate_person_factories(mock_openai_client):
    """Tests if generate_person_factories method correctly uses the LLM and generates instances."""
    mock_openai_client.return_value.send_message.return_value = {"content": json.dumps([
        {"name":"test1"},
        {"name":"test2"},
        {"name":"test3"}
        ])}
    
    number_of_factories = 3
    generic_context_text = "Some generic context"
    factories = TinyPersonFactory.generate_person_factories(number_of_factories, generic_context_text)

    assert len(factories) == number_of_factories
    for factory in factories:
        assert isinstance(factory, TinyPersonFactory)
    
    # check if the prompt was generated as expected
    mock_openai_client.assert_called_once()
    args, kwargs = mock_openai_client.mock_calls[0]
    messages = args[0]
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert 'Please, create 3 person descriptions based on the following broad context: Some generic context' in messages[1]["content"]
    
def test_tinypersonfactory_generate_person_factories_no_response(mock_openai_client):
    """Tests if generate_person_factories method returns None if the API gives no response."""
    mock_openai_client.return_value.send_message.return_value = None
    factories = TinyPersonFactory.generate_person_factories(2, "context")
    assert factories is None
    
def test_tinypersonfactory_generate_person(tiny_person_factory, mock_openai_client):
    """Tests if generate_person method correctly uses the LLM and generates a TinyPerson instance."""
    mock_openai_client.return_value.send_message.return_value = {"content": json.dumps({
        "name": "Test Person",
        "_configuration": {
            "key1": "value1",
            "key2": ["value2a", "value2b"]
            }})}

    person = tiny_person_factory.generate_person()

    assert isinstance(person, TinyPerson)
    assert person.get("name") == "Test Person"
    assert person.get("key1") == "value1"
    assert person.get("key2") == ["value2a", "value2b"]
    assert len(tiny_person_factory.generated_minibios) == 1
    assert len(tiny_person_factory.generated_names) == 1
    
    # check if the prompt was generated as expected
    mock_openai_client.assert_called_once()
    args, kwargs = mock_openai_client.mock_calls[0]
    messages = args[0]
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert 'Test context' in messages[1]["content"]


def test_tinypersonfactory_generate_person_with_agent_particularities(tiny_person_factory, mock_openai_client):
    """Tests if generate_person method includes agent particularities."""
    mock_openai_client.return_value.send_message.return_value = {"content": json.dumps({
        "name": "Test Person",
        "_configuration": {
            "key1": "value1",
            "key2": ["value2a", "value2b"]
            }})}

    person = tiny_person_factory.generate_person(agent_particularities="particularities")
    
    # check if the prompt was generated as expected
    mock_openai_client.assert_called_once()
    args, kwargs = mock_openai_client.mock_calls[0]
    messages = args[0]
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert 'particularities' in messages[1]["content"]

def test_tinypersonfactory_generate_person_no_response(tiny_person_factory, mock_openai_client):
    """Tests if generate_person method returns None when the API does not give a response."""
    mock_openai_client.return_value.send_message.return_value = None
    person = tiny_person_factory.generate_person()
    assert person is None

def test_tinypersonfactory_generate_person_max_attempts(tiny_person_factory, mock_openai_client):
    """Tests if generate_person method gives up after maximum attempts"""
    mock_openai_client.return_value.send_message.side_effect = [None,None,None,None,None]
    person = tiny_person_factory.generate_person(attepmpts=5)
    assert person is None

    # assert it tried 5 times to contact the model
    assert mock_openai_client.return_value.send_message.call_count == 5

def test_tinypersonfactory_generate_person_repeated_name(tiny_person_factory, mock_openai_client):
    """Tests if generate_person method avoids name repetitions, and re-tries"""

    mock_responses = [
            {"content": json.dumps({ "name": "Test Person", "_configuration": {"key1": "value1" } })},
            {"content": json.dumps({ "name": "Test Person", "_configuration": {"key1": "value1" } })},
            {"content": json.dumps({ "name": "Test Person2", "_configuration": {"key1": "value1" } })},
            ]
    
    mock_openai_client.return_value = MockOpenAIClient(mock_responses)
    
    person = tiny_person_factory.generate_person(attepmpts=3) # set to 3 attempts so we can force this
    
    assert isinstance(person, TinyPerson)
    assert person.get("name") == "Test Person2"
    
    # assert it tried 3 times to contact the model
    assert mock_openai_client.return_value.call_count == 3
    assert len(tiny_person_factory.generated_names) == 1
    assert tiny_person_factory.generated_names[0] == "test person2"

def test_tinypersonfactory_setup_agent(tiny_person_factory, tiny_person):
    """Tests if the _setup_agent method correctly sets up the agent with the configuration."""
    config = {
        "key1": "value1",
        "key2": ["value2a", "value2b"]
    }
    
    tiny_person_factory._setup_agent(tiny_person, config)
    
    assert tiny_person.get("key1") == "value1"
    assert tiny_person.get("key2") == ["value2a", "value2b"]

def test_tinypersonfactory_aux_model_call_transactional(tiny_person_factory, mock_openai_client):
    """Tests if the _aux_model_call method correctly interacts with the client and cache."""
    mock_openai_client.return_value.send_message.return_value = {"content": "some content"}
    
    messages = [{"role": "system", "content": "test"}, {"role": "user", "content": "test"}]
    
    # Call the method twice to ensure it caches the call
    result1 = tiny_person_factory._aux_model_call(messages=messages, temperature=1.5)
    result2 = tiny_person_factory._aux_model_call(messages=messages, temperature=1.5)
    
    assert result1 == {"content": "some content"}
    assert result2 == {"content": "some content"}
    
    # assert it called only once, to ensure that it was cached the second time
    assert mock_openai_client.return_value.send_message.call_count == 1
```