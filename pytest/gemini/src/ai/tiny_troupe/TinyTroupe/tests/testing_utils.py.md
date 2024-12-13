```python
"""
Testing utilities.
"""
import os
import sys
from time import sleep
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib

# force caching, in order to save on API usage
openai_utils.force_api_cache(True, "tests_cache.pickle")

def contains_action_type(actions, action_type):
    """
    Checks if the given list of actions contains an action of the given type.
    """
    
    for action in actions:
        if action["action"]["type"] == action_type:
            return True
    
    return False

def contains_action_content(actions:list, action_content: str):
    """
    Checks if the given list of actions contains an action with the given content.
    """
    
    for action in actions:
        # checks whether the desired content is contained in the action content
        if action_content.lower() in action["action"]["content"].lower():
            return True
    
    return False

def contains_stimulus_type(stimuli, stimulus_type):
    """
    Checks if the given list of stimuli contains a stimulus of the given type.
    """
    
    for stimulus in stimuli:
        if stimulus["type"] == stimulus_type:
            return True
    
    return False

def contains_stimulus_content(stimuli, stimulus_content):
    """
    Checks if the given list of stimuli contains a stimulus with the given content.
    """
    
    for stimulus in stimuli:
        # checks whether the desired content is contained in the stimulus content
        if stimulus_content.lower() in stimulus["content"].lower():
            return True
    
    return False

def terminates_with_action_type(actions, action_type):
    """
    Checks if the given list of actions terminates with an action of the given type.
    """
    
    if len(actions) == 0:
        return False
    
    return actions[-1]["action"]["type"] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Checks if the given proposition is true according to an LLM call.
    This can be used to check for text properties that are hard to
    verify mechanically, such as "the text contains some ideas for a product".
    """

    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don't write anything else!
    """

    user_prompt = f"""
    Proposition: {proposition}
    """

    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]
    
    # call the LLM
    next_message = openai_utils.client().send_message(messages)

    # check the result
    cleaned_message = only_alphanumeric(next_message["content"])
    if cleaned_message.lower().startswith("true"):
        return True
    elif cleaned_message.lower().startswith("false"):
        return False
    else:
        raise Exception(f"LLM returned unexpected result: {cleaned_message}")

def only_alphanumeric(string: str):
    """
    Returns a string containing only alphanumeric characters.
    """
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt, system_prompt="You are a helpful AI assistant."):
    """
    Creates a list containing one system message and one user message. 
    """
    
    messages = [{"role": "system", "content": system_prompt}]
    
    if user_prompt is not None:
        messages.append({"role": "user", "content": user_prompt})
    
    return messages

def agents_configs_are_equal(agent1, agent2, ignore_name=False):
    """
    Checks if the configurations of two agents are equal.
    """

    ignore_keys = []
    if ignore_name:
        ignore_keys.append("name")
    
    for key in agent1._configuration.keys():
        if key in ignore_keys:
            continue
        
        if agent1._configuration[key] != agent2._configuration[key]:
            return False
    
    return True
############################################################################################################
# I/O utilities
############################################################################################################

def remove_file_if_exists(file_path):
    """
    Removes the file at the given path if it exists.
    """
    
    if os.path.exists(file_path):
        os.remove(file_path)

def get_relative_to_test_path(path_suffix):
    """
    Returns the path to the test file with the given suffix.
    """
    
    return os.path.join(os.path.dirname(__file__), path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope="function")
def focus_group_world():
    import tinytroupe.examples as examples   
    
    world = TinyWorld("Focus group", [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope="function")
def setup():
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()

    yield
```
```python
import pytest
from tinytroupe.tests.testing_utils import (
    contains_action_type,
    contains_action_content,
    contains_stimulus_type,
    contains_stimulus_content,
    terminates_with_action_type,
    proposition_holds,
    only_alphanumeric,
    create_test_system_user_message,
    agents_configs_are_equal,
    remove_file_if_exists,
    get_relative_to_test_path
)
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import os

# Fixture definitions, if needed
@pytest.fixture
def example_actions():
    """Provides a sample list of actions for testing."""
    return [
        {"action": {"type": "move", "content": "go to the kitchen"}},
        {"action": {"type": "speak", "content": "Hello there!"}},
        {"action": {"type": "think", "content": "I need to find the key"}},
         {"action": {"type": "move", "content": "Go to the living room"}},
    ]

@pytest.fixture
def example_stimuli():
    """Provides a sample list of stimuli for testing."""
    return [
        {"type": "sight", "content": "a red door"},
        {"type": "sound", "content": "a loud bang"},
        {"type": "smell", "content": "fresh bread"},
        {"type": "touch", "content": "a soft pillow"}
    ]

@pytest.fixture
def example_agent():
    """Provides a sample TinyPerson agent for testing."""
    config = {
            "name": "Test Agent",
            "persona": "A test agent.",
            "goal": "To test functionalities.",
            "initial_plan": "Start testing.",
            "working_memory": {"key": "value"},
            "reflection_strategy": "reflecting",
            "action_strategy": "acting",
             "llm_strategy": "gpt-4-1106-preview",
        }

    return TinyPerson(config=config)


@pytest.fixture
def example_agent2():
    """Provides a sample TinyPerson agent for testing."""
    config = {
            "name": "Test Agent 2",
            "persona": "A test agent.",
            "goal": "To test functionalities.",
            "initial_plan": "Start testing.",
            "working_memory": {"key": "value"},
            "reflection_strategy": "reflecting",
            "action_strategy": "acting",
             "llm_strategy": "gpt-4-1106-preview",
        }

    return TinyPerson(config=config)

@pytest.fixture
def example_agent_diff_config():
    """Provides a sample TinyPerson agent with a different config for testing."""
    config = {
            "name": "Test Agent",
            "persona": "A test agent.",
            "goal": "To test different functionalities.",
            "initial_plan": "Start testing differently.",
            "working_memory": {"key": "different_value"},
            "reflection_strategy": "reflecting",
            "action_strategy": "acting",
             "llm_strategy": "gpt-4-1106-preview",
        }

    return TinyPerson(config=config)

# Tests for contains_action_type
def test_contains_action_type_valid(example_actions):
    """Checks if an action type is correctly identified."""
    assert contains_action_type(example_actions, "speak") is True

def test_contains_action_type_invalid(example_actions):
    """Checks if the function returns False for a non-existent action type."""
    assert contains_action_type(example_actions, "jump") is False

def test_contains_action_type_empty_list():
    """Checks if the function works with an empty list."""
    assert contains_action_type([], "speak") is False

# Tests for contains_action_content
def test_contains_action_content_valid(example_actions):
    """Checks if an action content is correctly identified."""
    assert contains_action_content(example_actions, "hello") is True

def test_contains_action_content_case_insensitive(example_actions):
    """Checks if content check is case-insensitive."""
    assert contains_action_content(example_actions, "hELLo") is True

def test_contains_action_content_invalid(example_actions):
    """Checks if the function returns False for non-existent action content."""
    assert contains_action_content(example_actions, "goodbye") is False

def test_contains_action_content_empty_list():
    """Checks if the function works with an empty list."""
    assert contains_action_content([], "hello") is False

# Tests for contains_stimulus_type
def test_contains_stimulus_type_valid(example_stimuli):
    """Checks if a stimulus type is correctly identified."""
    assert contains_stimulus_type(example_stimuli, "sound") is True

def test_contains_stimulus_type_invalid(example_stimuli):
    """Checks if the function returns False for a non-existent stimulus type."""
    assert contains_stimulus_type(example_stimuli, "taste") is False

def test_contains_stimulus_type_empty_list():
    """Checks if the function works with an empty list."""
    assert contains_stimulus_type([], "sound") is False


# Tests for contains_stimulus_content
def test_contains_stimulus_content_valid(example_stimuli):
    """Checks if a stimulus content is correctly identified."""
    assert contains_stimulus_content(example_stimuli, "red") is True

def test_contains_stimulus_content_case_insensitive(example_stimuli):
     """Checks if content check is case-insensitive."""
     assert contains_stimulus_content(example_stimuli, "rEd") is True

def test_contains_stimulus_content_invalid(example_stimuli):
    """Checks if the function returns False for non-existent stimulus content."""
    assert contains_stimulus_content(example_stimuli, "blue") is False

def test_contains_stimulus_content_empty_list():
    """Checks if the function works with an empty list."""
    assert contains_stimulus_content([], "red") is False


# Tests for terminates_with_action_type
def test_terminates_with_action_type_valid(example_actions):
    """Checks if an action type at the end of the list is correctly identified."""
    assert terminates_with_action_type(example_actions, "move") is True

def test_terminates_with_action_type_invalid(example_actions):
    """Checks if the function returns False when the last action type doesn't match."""
    assert terminates_with_action_type(example_actions, "speak") is False

def test_terminates_with_action_type_empty_list():
    """Checks if the function returns False for an empty list."""
    assert terminates_with_action_type([], "move") is False


# Tests for proposition_holds (Note: This requires LLM interaction, so can be slow or unreliable)
@pytest.mark.slow
def test_proposition_holds_true():
    """Checks if a true proposition is correctly evaluated."""
    assert proposition_holds("The sky is blue.") is True

@pytest.mark.slow
def test_proposition_holds_false():
    """Checks if a false proposition is correctly evaluated."""
    assert proposition_holds("The earth is flat.") is False

@pytest.mark.slow
def test_proposition_holds_invalid_response():
    """Checks if an exception is raised for an unexpected LLM response."""
    with pytest.raises(Exception, match="LLM returned unexpected result"):
        proposition_holds("Some random text")

# Tests for only_alphanumeric
def test_only_alphanumeric_valid():
    """Checks if the function correctly extracts alphanumeric characters."""
    assert only_alphanumeric("a1b2c3!") == "a1b2c3"

def test_only_alphanumeric_no_change():
    """Checks if the function handles strings without special characters."""
    assert only_alphanumeric("abc123def") == "abc123def"

def test_only_alphanumeric_empty_string():
    """Checks if the function handles an empty string."""
    assert only_alphanumeric("") == ""


# Tests for create_test_system_user_message
def test_create_test_system_user_message_with_user_prompt():
    """Checks if both system and user messages are created correctly."""
    messages = create_test_system_user_message("Hello, world!", "System prompt")
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == "System prompt"
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "Hello, world!"

def test_create_test_system_user_message_no_user_prompt():
    """Checks if only the system message is created when no user prompt is given."""
    messages = create_test_system_user_message(None)
    assert len(messages) == 1
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == "You are a helpful AI assistant."

# Tests for agents_configs_are_equal
def test_agents_configs_are_equal_valid(example_agent, example_agent2):
    """Checks if the function correctly identifies when configurations are equal (except name)."""
    assert agents_configs_are_equal(example_agent, example_agent2, ignore_name=True) is True

def test_agents_configs_are_equal_diff_config(example_agent, example_agent_diff_config):
    """Checks if the function correctly identifies when configurations are different."""
    assert agents_configs_are_equal(example_agent, example_agent_diff_config, ignore_name=True) is False

def test_agents_configs_are_equal_diff_name(example_agent, example_agent2):
     """Checks if the function correctly identifies when configurations are equal (including name)."""
     assert agents_configs_are_equal(example_agent, example_agent2) is False

# Tests for remove_file_if_exists
def test_remove_file_if_exists_existing_file():
    """Checks if an existing file is removed."""
    test_file = "test_file.txt"
    with open(test_file, "w") as f:
        f.write("This is a test file.")
    remove_file_if_exists(test_file)
    assert not os.path.exists(test_file)

def test_remove_file_if_exists_nonexistent_file():
    """Checks if no error is raised when trying to remove a non-existent file."""
    test_file = "nonexistent_file.txt"
    remove_file_if_exists(test_file)
    assert not os.path.exists(test_file) # no error raised


# Tests for get_relative_to_test_path
def test_get_relative_to_test_path_valid():
    """Checks if the function returns a valid path relative to the test file."""
    path = get_relative_to_test_path("test_file.txt")
    assert path.endswith("tinytroupe/src/ai/tiny_troupe/TinyTroupe/tests/test_file.txt")
    assert os.path.isabs(path)

def test_get_relative_to_test_path_empty_suffix():
    """Checks if the function returns the path of the current test file directory."""
    path = get_relative_to_test_path("")
    assert path.endswith("tinytroupe/src/ai/tiny_troupe/TinyTroupe/tests")
    assert os.path.isabs(path)
```