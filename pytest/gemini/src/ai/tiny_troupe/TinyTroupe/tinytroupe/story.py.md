```python
import pytest
from unittest.mock import MagicMock, patch

from tinytroupe.story import TinyStory
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils


# Fixture for a mock TinyWorld
@pytest.fixture
def mock_tiny_world():
    world = MagicMock(spec=TinyWorld)
    world.pretty_current_interactions.return_value = "Mock environment interactions"
    return world

# Fixture for a mock TinyPerson
@pytest.fixture
def mock_tiny_person():
    person = MagicMock(spec=TinyPerson)
    person.pretty_current_interactions.return_value = "Mock agent interactions"
    return person


# Fixture for a mock openai client
@pytest.fixture
def mock_openai_client():
    client = MagicMock()
    client.send_message.return_value = {"content": "Mock story content"}
    return client

@pytest.fixture(autouse=True)
def mock_openai_utils(mock_openai_client):
  with patch.object(openai_utils, "client", return_value=mock_openai_client):
    yield


# Test cases for TinyStory class

def test_tinystory_init_with_environment(mock_tiny_world):
    """Checks initialization with environment only."""
    story = TinyStory(environment=mock_tiny_world, purpose="Test purpose", context="Initial context")
    assert story.environment == mock_tiny_world
    assert story.agent is None
    assert story.purpose == "Test purpose"
    assert story.current_story == "Initial context"
    assert story.first_n == 10
    assert story.last_n == 20
    assert story.include_omission_info == True

def test_tinystory_init_with_agent(mock_tiny_person):
    """Checks initialization with agent only."""
    story = TinyStory(agent=mock_tiny_person, purpose="Another test purpose", context="Another context", first_n=5, last_n=15, include_omission_info=False)
    assert story.agent == mock_tiny_person
    assert story.environment is None
    assert story.purpose == "Another test purpose"
    assert story.current_story == "Another context"
    assert story.first_n == 5
    assert story.last_n == 15
    assert story.include_omission_info == False


def test_tinystory_init_raises_exception_both_env_agent(mock_tiny_world, mock_tiny_person):
    """Checks that an exception is raised if both environment and agent are provided."""
    with pytest.raises(Exception, match="Either \'environment\' or \'agent\' should be provided, not both"):
      TinyStory(environment=mock_tiny_world, agent=mock_tiny_person)

def test_tinystory_init_raises_exception_neither_env_agent():
    """Checks that an exception is raised if neither environment nor agent are provided."""
    with pytest.raises(Exception, match="At least one of the parameters should be provided"):
      TinyStory()


def test_start_story(mock_tiny_world, mock_openai_client):
    """Checks that the story starts correctly."""
    story = TinyStory(environment=mock_tiny_world, purpose="Test purpose", context="Initial context")
    start_content = story.start_story(requirements="Start an amazing story")
    assert start_content == "Mock story content"
    assert "## The story begins" in story.current_story
    assert "Mock story content" in story.current_story
    mock_openai_client.send_message.assert_called_once()
    

def test_continue_story(mock_tiny_world, mock_openai_client):
    """Checks that the story continues correctly."""
    story = TinyStory(environment=mock_tiny_world, purpose="Test purpose", context="Initial context")
    continue_content = story.continue_story(requirements="Continue in a fun way")
    assert continue_content == "Mock story content"
    assert "## The story continues" in story.current_story
    assert "Mock story content" in story.current_story
    mock_openai_client.send_message.assert_called_once()

def test_current_story_with_agent(mock_tiny_person):
  """Checks that the current story is generated with agent."""
  story = TinyStory(agent=mock_tiny_person)
  current_story = story._current_story()
  assert "## New simulation interactions to consider" in current_story
  assert "Mock agent interactions" in current_story
  mock_tiny_person.pretty_current_interactions.assert_called_once()

def test_current_story_with_environment(mock_tiny_world):
  """Checks that the current story is generated with the environment."""
  story = TinyStory(environment=mock_tiny_world)
  current_story = story._current_story()
  assert "## New simulation interactions to consider" in current_story
  assert "Mock environment interactions" in current_story
  mock_tiny_world.pretty_current_interactions.assert_called_once()


def test_current_story_with_existing_story(mock_tiny_world):
    """Checks that the current story is generated correctly when there is an existing story."""
    story = TinyStory(environment=mock_tiny_world, context="Existing Story")
    story._current_story()
    assert "Existing Story" in story.current_story
    assert "## New simulation interactions to consider" in story.current_story
    assert "Mock environment interactions" in story.current_story

```