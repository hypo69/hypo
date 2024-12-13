```python
import pytest
import os
import json
from datetime import datetime
from unittest.mock import patch, mock_open

from tinytroupe.agent import TinyPerson, TinyMentalFaculty, RecallFaculty, FilesAndWebGroundingFaculty, TinyToolUse
from tinytroupe.agent import EpisodicMemory, SemanticMemory
from tinytroupe import utils
from tinytroupe.control import current_simulation

# Mock the openai_utils.client() and its send_message method
@pytest.fixture
def mock_openai_client():
    with patch("tinytroupe.agent.openai_utils.client") as mock_client:
        mock_client.return_value.send_message.return_value = {"role": "assistant", "content": json.dumps({"action": {"type": "DONE", "content": "some content"}, "cognitive_state": {"goals": [], "attention": None, "emotions": "calm"}})}
        yield mock_client

# Mock the chevron.render method, so that we don't need the prompts directory
@pytest.fixture
def mock_chevron_render():
    with patch("tinytroupe.agent.chevron.render") as mock_render:
        mock_render.return_value = "This is a mock prompt"
        yield mock_render


@pytest.fixture
def example_agent():
    """Provides a basic TinyPerson agent for tests."""
    agent = TinyPerson(name="TestAgent")
    return agent


@pytest.fixture
def example_memory():
    """Provides a basic episodic memory for tests."""
    memory = EpisodicMemory()
    return memory


@pytest.fixture
def example_semantic_memory():
    """Provides a basic semantic memory for tests."""
    memory = SemanticMemory()
    return memory


@pytest.fixture
def example_mental_faculty():
    """Provides a basic mental faculty for tests."""
    faculty = TinyMentalFaculty(name="TestFaculty")
    return faculty


def test_tinyperson_creation(example_agent):
    """Checks if a TinyPerson is created correctly."""
    assert example_agent.name == "TestAgent"
    assert example_agent.episodic_memory is not None
    assert example_agent.semantic_memory is not None
    assert example_agent._mental_faculties == []
    assert TinyPerson.has_agent("TestAgent")
    assert example_agent.simulation_id is None

def test_tinyperson_creation_with_mental_faculties():
    """Checks if a TinyPerson is created correctly with mental faculties."""
    faculty = TinyMentalFaculty(name="TestFaculty")
    agent = TinyPerson(name="TestAgent", mental_faculties=[faculty])
    assert agent._mental_faculties == [faculty]
    assert TinyPerson.has_agent("TestAgent")

def test_tinyperson_creation_with_memory():
    """Checks if a TinyPerson is created correctly with custom memory."""
    memory = EpisodicMemory()
    memory2 = SemanticMemory()
    agent = TinyPerson(name="TestAgent", episodic_memory=memory, semantic_memory=memory2)
    assert agent.episodic_memory == memory
    assert agent.semantic_memory == memory2
    assert TinyPerson.has_agent("TestAgent")

def test_tinyperson_creation_fails_if_no_name():
    """Checks if a TinyPerson fails to create if name is not given."""
    with pytest.raises(AssertionError, match="A TinyPerson must have a name."):
         TinyPerson()

def test_tinyperson_post_init_default_values(example_agent):
    """Checks if default values are initialized correctly in _post_init."""
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]
    assert example_agent.environment is None
    assert example_agent._actions_buffer == []
    assert example_agent._accessible_agents == []
    assert example_agent._displayed_communications_buffer == []
    assert example_agent._configuration["name"] == "TestAgent"

def test_tinyperson_post_init_auto_rename(mock_chevron_render):
    """Checks if auto-rename mechanism works"""
    agent = TinyPerson(name="TestAgent", auto_rename=True)
    assert agent.name.startswith("TestAgent_")
    assert TinyPerson.has_agent(agent.name)

def test_tinyperson_post_init_rename_agent(mock_chevron_render):
    """Checks if rename mechanism works"""
    agent = TinyPerson(name="TestAgent", new_agent_name="NewAgentName")
    assert agent.name == "NewAgentName"
    assert agent._configuration["name"] == "NewAgentName"
    assert TinyPerson.has_agent("NewAgentName")

def test_tinyperson_post_init_simulation_id(mock_chevron_render):
    """Checks if the simulation_id is correctly initialized."""
    with patch("tinytroupe.agent.current_simulation") as mock_current_simulation:
        mock_current_simulation.return_value = type('MockSimulation', (object,), {"add_agent": lambda x,y: None})()
        agent = TinyPerson(name="TestAgent")
        assert agent.simulation_id is not None

def test_tinyperson_get(example_agent):
    """Checks if the get method retrieves configuration values."""
    example_agent._configuration["test_key"] = "test_value"
    assert example_agent.get("test_key") == "test_value"
    assert example_agent.get("non_existent_key") is None

def test_tinyperson_define(example_agent, mock_chevron_render):
    """Checks if the define method sets configuration values."""
    example_agent.define("test_key", "test_value")
    assert example_agent._configuration["test_key"] == "test_value"
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]

def test_tinyperson_define_with_group(example_agent, mock_chevron_render):
    """Checks if the define method sets configuration values with a group."""
    example_agent.define("key1", "value1", "group1")
    assert example_agent._configuration["group1"] == [{"key1": "value1"}]
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]

    example_agent.define(None, "value2", "group1")
    assert example_agent._configuration["group1"] == [{"key1": "value1"}, "value2"]

def test_tinyperson_define_dedent(example_agent, mock_chevron_render):
    """Checks if the define method dedents values."""
    indented_value = "    test_value"
    example_agent.define("test_key", indented_value)
    assert example_agent._configuration["test_key"] == "test_value"

def test_tinyperson_define_several(example_agent, mock_chevron_render):
    """Checks if the define several method adds records to a group."""
    records = ["record1", "record2", "record3"]
    example_agent.define_several("group1", records)
    assert example_agent._configuration["group1"] == records
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]

def test_tinyperson_define_relationships(example_agent, mock_chevron_render):
    """Checks if the define_relationships method adds or replaces relationships."""
    relationships = [{"Name": "Agent1", "Description": "Friend"}, {"Name": "Agent2", "Description": "Colleague"}]
    example_agent.define_relationships(relationships)
    assert example_agent._configuration["relationships"] == relationships

    new_relationships = [{"Name": "Agent3", "Description": "Acquaintance"}]
    example_agent.define_relationships(new_relationships, replace=False)
    assert example_agent._configuration["relationships"] == relationships + new_relationships

def test_tinyperson_define_relationships_fails_with_dict(example_agent, mock_chevron_render):
    """Checks if the define_relationships method fails if dict does not have the expected keys."""
    with pytest.raises(Exception, match="Only one key-value pair is allowed in the relationships dict."):
        example_agent.define_relationships({"Name": "Agent1", "Description": "Friend", "Extra": "Extra"}, replace=False)

def test_tinyperson_define_relationships_fails_with_invalid_arguments(example_agent, mock_chevron_render):
    """Checks if the define_relationships method fails with invalid arguments."""
    with pytest.raises(Exception, match="Invalid arguments for define_relationships."):
        example_agent.define_relationships("invalid")
    
    with pytest.raises(Exception, match="Invalid arguments for define_relationships."):
        example_agent.define_relationships({"Name": "Agent1", "Description": "Friend"}, replace=True)

def test_tinyperson_clear_relationships(example_agent, mock_chevron_render):
    """Checks if the clear_relationships method clears relationships."""
    example_agent._configuration["relationships"] = [{"Name": "Agent1", "Description": "Friend"}]
    example_agent.clear_relationships()
    assert example_agent._configuration["relationships"] == []

def test_tinyperson_related_to(example_agent, mock_chevron_render):
    """Checks if the related_to method adds relationships between agents."""
    agent2 = TinyPerson(name="Agent2")
    example_agent.related_to(agent2, "Friend")
    assert example_agent._configuration["relationships"] == [{"Name": "Agent2", "Description": "Friend"}]
    assert agent2._configuration["relationships"] == [] # no symmetric relation was defined.

    example_agent.related_to(agent2, "Good friend", "Good friend too")
    assert example_agent._configuration["relationships"] == [{"Name": "Agent2", "Description": "Friend"}, {"Name": "Agent2", "Description": "Good friend"}]
    assert agent2._configuration["relationships"] == [{"Name": "TestAgent", "Description": "Good friend too"}]

def test_tinyperson_add_mental_faculty(example_agent, mock_chevron_render):
    """Checks if the add_mental_faculty method adds mental faculties."""
    faculty1 = TinyMentalFaculty(name="Faculty1")
    example_agent.add_mental_faculty(faculty1)
    assert faculty1 in example_agent._mental_faculties

    # test for adding existing faculty
    with pytest.raises(Exception, match="The mental faculty TestFaculty is already present in the agent."):
      example_agent.add_mental_faculty(faculty1)

def test_tinyperson_add_mental_faculties(example_agent, mock_chevron_render):
    """Checks if the add_mental_faculties method adds multiple mental faculties."""
    faculty1 = TinyMentalFaculty(name="Faculty1")
    faculty2 = TinyMentalFaculty(name="Faculty2")
    example_agent.add_mental_faculties([faculty1, faculty2])
    assert faculty1 in example_agent._mental_faculties
    assert faculty2 in example_agent._mental_faculties

def test_tinyperson_act_with_n_actions(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the act method performs a specified number of actions."""
    actions = example_agent.act(n=3, return_actions=True)
    assert len(actions) == 3
    assert len(example_agent._actions_buffer) == 3

def test_tinyperson_act_until_done(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the act method performs actions until done."""
    actions = example_agent.act(until_done=True, return_actions=True)
    assert len(actions) > 0
    assert len(example_agent._actions_buffer) > 0
    assert actions[-1]["action"]["type"] == "DONE"


def test_tinyperson_act_fails_if_both_until_done_and_n_are_given(example_agent):
    """Checks if act raises an error if both until_done and n are specified."""
    with pytest.raises(AssertionError):
        example_agent.act(until_done=True, n=1)

def test_tinyperson_act_fails_if_n_is_too_large(example_agent):
    """Checks if act raises an error if n is too large."""
    with pytest.raises(AssertionError):
        example_agent.act(n=16)


def test_tinyperson_listen(example_agent, mock_chevron_render):
    """Checks if the listen method processes speech stimuli."""
    example_agent.listen("Hello, world!")
    assert len(example_agent.episodic_memory.memory) > 0

    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "CONVERSATION"
    assert stimulus["content"] == "Hello, world!"
    assert stimulus["source"] == ""

def test_tinyperson_listen_with_source(example_agent, mock_chevron_render):
    """Checks if the listen method processes speech stimuli with a source."""
    agent2 = TinyPerson(name="Agent2")
    example_agent.listen("Hello, world!", source=agent2)
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["source"] == "Agent2"

def test_tinyperson_socialize(example_agent, mock_chevron_render):
    """Checks if the socialize method processes social stimuli."""
    example_agent.socialize("A social event")
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "SOCIAL"
    assert stimulus["content"] == "A social event"
    assert stimulus["source"] == ""

def test_tinyperson_see(example_agent, mock_chevron_render):
    """Checks if the see method processes visual stimuli."""
    example_agent.see("A visual scene")
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "VISUAL"
    assert stimulus["content"] == "A visual scene"
    assert stimulus["source"] == ""

def test_tinyperson_think(example_agent, mock_chevron_render):
    """Checks if the think method processes thoughts."""
    example_agent.think("A thought")
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "THOUGHT"
    assert stimulus["content"] == "A thought"
    assert stimulus["source"] == "TestAgent"


def test_tinyperson_internalize_goal(example_agent, mock_chevron_render):
    """Checks if the internalize_goal method processes goals."""
    example_agent.internalize_goal("A goal")
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "INTERNAL_GOAL_FORMULATION"
    assert stimulus["content"] == "A goal"
    assert stimulus["source"] == "TestAgent"

def test_tinyperson_observe(example_agent, mock_chevron_render):
    """Checks if the _observe method processes stimuli."""
    example_agent._observe({"type": "TEST", "content": "test content"})
    assert len(example_agent.episodic_memory.memory) > 0
    stimulus = example_agent.episodic_memory.memory[-1]["content"]["stimuli"][0]
    assert stimulus["type"] == "TEST"
    assert stimulus["content"] == "test content"
    assert stimulus["source"] == ""

def test_tinyperson_listen_and_act(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the listen_and_act method combines listen and act."""
    actions = example_agent.listen_and_act("Some speech", return_actions=True)
    assert len(actions) > 0
    assert len(example_agent._actions_buffer) > 0

def test_tinyperson_see_and_act(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the see_and_act method combines see and act."""
    actions = example_agent.see_and_act("Some visual", return_actions=True)
    assert len(actions) > 0
    assert len(example_agent._actions_buffer) > 0

def test_tinyperson_think_and_act(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the think_and_act method combines think and act."""
    actions = example_agent.think_and_act("Some thought", return_actions=True)
    assert len(actions) > 0
    assert len(example_agent._actions_buffer) > 0

def test_tinyperson_read_documents_from_folder(example_agent, example_semantic_memory, mock_chevron_render):
    """Checks if documents are loaded from a folder."""
    with patch("tinytroupe.agent.SimpleDirectoryReader") as mock_reader:
        mock_reader.return_value.load_data.return_value = [{"metadata": {"file_name":"test.txt"}, "text":"text from a file"}]
        example_agent.semantic_memory = example_semantic_memory
        example_agent.read_documents_from_folder("test_folder")
        assert len(example_agent.semantic_memory.documents) == 1
        assert len(example_agent.semantic_memory.filename_to_document) == 1
        assert "test.txt" in example_agent.semantic_memory.filename_to_document
        assert len(example_agent.semantic_memory.documents_paths) == 1
        assert "test_folder" in example_agent.semantic_memory.documents_paths

def test_tinyperson_read_documents_from_web(example_agent, example_semantic_memory, mock_chevron_render):
    """Checks if documents are loaded from the web."""
    with patch("tinytroupe.agent.SimpleWebPageReader") as mock_reader:
        mock_reader.return_value.load_data.return_value = [{"id_":"web_url", "text":"text from a web page"}]
        example_agent.semantic_memory = example_semantic_memory
        example_agent.read_documents_from_web(["test_url"])
        assert len(example_agent.semantic_memory.documents) == 1
        assert len(example_agent.semantic_memory.filename_to_document) == 1
        assert "web_url" in example_agent.semantic_memory.filename_to_document
        assert len(example_agent.semantic_memory.documents_web_urls) == 1
        assert "test_url" in example_agent.semantic_memory.documents_web_urls

def test_tinyperson_move_to(example_agent, mock_chevron_render):
    """Checks if the move_to method updates the agent's location."""
    example_agent.move_to("New Location", ["context1", "context2"])
    assert example_agent._configuration["current_location"] == "New Location"
    assert example_agent._configuration["current_context"] == {
            "description": item for item in ["context1", "context2"]
        }
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]


def test_tinyperson_change_context(example_agent, mock_chevron_render):
    """Checks if the change_context method updates the agent's context."""
    example_agent.change_context(["context1", "context2"])
    assert example_agent._configuration["current_context"] == {
            "description": item for item in ["context1", "context2"]
        }
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]

def test_tinyperson_make_agent_accessible(example_agent, mock_chevron_render):
    """Checks if the make_agent_accessible method adds agents to the accessible list."""
    agent2 = TinyPerson(name="Agent2")
    example_agent.make_agent_accessible(agent2)
    assert agent2 in example_agent._accessible_agents
    assert {"name": "Agent2", "relation_description": "An agent I can currently interact with."} in example_agent._configuration["currently_accessible_agents"]

    # test for adding accessible agents again, just to verify that no error is raised
    example_agent.make_agent_accessible(agent2)
    assert agent2 in example_agent._accessible_agents
    assert len(example_agent._accessible_agents) == 1
    assert len(example_agent._configuration["currently_accessible_agents"]) == 1

def test_tinyperson_make_agent_inaccessible(example_agent, mock_chevron_render):
    """Checks if the make_agent_inaccessible method removes agents from the accessible list."""
    agent2 = TinyPerson(name="Agent2")
    example_agent._accessible_agents.append(agent2)
    example_agent._configuration["currently_accessible_agents"] = [{"name": "Agent2", "relation_description": "An agent I can currently interact with."}]
    example_agent.make_agent_inaccessible(agent2)
    assert agent2 not in example_agent._accessible_agents
    assert example_agent._configuration["currently_accessible_agents"] == []

    # test for removing inaccessible agents, just to verify no error is raised
    example_agent.make_agent_inaccessible(agent2)
    assert len(example_agent._accessible_agents) == 0
    assert len(example_agent._configuration["currently_accessible_agents"]) == 0

def test_tinyperson_make_all_agents_inaccessible(example_agent, mock_chevron_render):
    """Checks if the make_all_agents_inaccessible method clears the accessible list."""
    agent2 = TinyPerson(name="Agent2")
    example_agent._accessible_agents = [agent2]
    example_agent._configuration["currently_accessible_agents"] = [{"name": "Agent2", "relation_description": "An agent I can currently interact with."}]
    example_agent.make_all_agents_inaccessible()
    assert example_agent._accessible_agents == []
    assert example_agent._configuration["currently_accessible_agents"] == []

def test_tinyperson_produce_message(example_agent, mock_openai_client, mock_chevron_render):
    """Checks if the _produce_message method sends messages to OpenAI API."""
    role, content = example_agent._produce_message()
    mock_openai_client.return_value.send_message.assert_called()
    assert role == "assistant"
    assert content == {"action": {"type": "DONE", "content": "some content"}, "cognitive_state": {"goals": [], "attention": None, "emotions": "calm"}}


def test_tinyperson_update_cognitive_state(example_agent, mock_chevron_render):
    """Checks if the _update_cognitive_state method updates the agent's cognitive state."""
    example_agent._update_cognitive_state(goals=["goal1"], context=["context1"], attention="focused", emotions="happy")
    assert example_agent._configuration["current_goals"] == ["goal1"]
    assert example_agent._configuration["current_context"] == ["context1"]
    assert example_agent._configuration["current_attention"] == "focused"
    assert example_agent._configuration["current_emotions"] == "happy"
    assert example_agent.current_messages == [{"role": "system", "content": "This is a mock prompt"}]

def test_tinyperson_update_cognitive_state_datetime_from_environment(example_agent, mock_chevron_render):
    """Checks if the _update_cognitive_state method updates the agent's current_datetime if an environment is defined."""
    with patch("tinytroupe.agent.utils.pretty_datetime") as mock_pretty_datetime:
      mock_pretty_datetime.return_value = "2024-01-01T12:00:00"

      class MockEnvironment():
        def __init__(self) -> None:
            self.current_datetime = datetime.fromisoformat("2024-01-01T12:00:00")

      env = MockEnvironment()
      example_agent.environment = env
      example_agent._update_cognitive_state()
      assert example_agent._configuration["current_datetime"] == "2024-01-01T12:00:00"

def test_tinyperson_display_communication_stimuli(example_agent, mock_chevron_render, capsys):
    """Checks if stimuli communications are correctly displayed."""
    example_agent._display_communication(role="user", content={"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, kind="stimuli", simplified=True, max_content_length=100)
    captured = capsys.readouterr()
    assert "test_source --> TestAgent" in captured.out
    assert "test content" in captured.out

def test_tinyperson_display_communication_action(example_agent, mock_chevron_render, capsys):
    """Checks if actions communications are correctly displayed."""
    example_agent._display_communication(role="assistant", content={"action": {"type": "TALK", "content": "test action content"}}, kind="action", simplified=True, max_content_length=100)
    captured = capsys.readouterr()
    assert "TestAgent acts" in captured.out
    assert "test action content" in captured.out


def test_tinyperson_display_communication_invalid_kind(example_agent):
    """Checks if _display_communication raises an error with invalid kind."""
    with pytest.raises(ValueError, match="Unknown communication kind: invalid"):
      example_agent._display_communication(role="user", content={}, kind="invalid")

def test_tinyperson_push_and_display_latest_communication(example_agent, capsys):
    """Checks if push_and_display_latest_communication correctly displays and buffers communications."""
    example_agent._push_and_display_latest_communication("test communication")
    captured = capsys.readouterr()
    assert "test communication" in captured.out
    assert len(example_agent._displayed_communications_buffer) == 1
    assert example_agent._displayed_communications_buffer[0] == "test communication"

def test_tinyperson_pop_and_display_latest_communications(example_agent, capsys):
    """Checks if pop_and_display_latest_communications correctly pops and displays communications."""
    example_agent._displayed_communications_buffer = ["comm1", "comm2"]
    communications = example_agent.pop_and_display_latest_communications()
    captured = capsys.readouterr()
    assert "comm1" in captured.out
    assert "comm2" in captured.out
    assert communications == ["comm1", "comm2"]
    assert len(example_agent._displayed_communications_buffer) == 0


def test_tinyperson_clear_communications_buffer(example_agent):
    """Checks if clear_communications_buffer correctly clears the communications buffer."""
    example_agent._displayed_communications_buffer = ["comm1", "comm2"]
    example_agent.clear_communications_buffer()
    assert example_agent._displayed_communications_buffer == []


def test_tinyperson_pop_latest_actions(example_agent):
    """Checks if pop_latest_actions correctly pops actions."""
    example_agent._actions_buffer = ["action1", "action2"]
    actions = example_agent.pop_latest_actions()
    assert actions == ["action1", "action2"]
    assert example_agent._actions_buffer == []

def test_tinyperson_pop_actions_and_get_contents_for(example_agent):
    """Checks if pop_actions_and_get_contents_for correctly retrieves action contents."""
    example_agent._actions_buffer = [
        {"type": "TALK", "content": "content1"},
        {"type": "THINK", "content": "content2"},
        {"type": "TALK", "content": "content3"},
    ]
    content = example_agent.pop_actions_and_get_contents_for("TALK", only_last_action=True)
    assert content == "content3"

    content = example_agent.pop_actions_and_get_contents_for("TALK", only_last_action=False)
    assert content == "content1\\ncontent3"

    content = example_agent.pop_actions_and_get_contents_for("NON_EXISTENT_ACTION", only_last_action=True)
    assert content == ""


def test_tinyperson_repr(example_agent):
    """Checks if the __repr__ method returns the correct string."""
    assert repr(example_agent) == "TinyPerson(name='TestAgent')"

def test_tinyperson_minibio(example_agent, mock_chevron_render):
    """Checks if the minibio method returns the correct string."""
    example_agent._configuration["age"] = 30
    example_agent._configuration["occupation"] = "Engineer"
    example_agent._configuration["nationality"] = "Brazilian"
    example_agent._configuration["country_of_residence"] = "Brazil"
    assert example_agent.minibio() == "TestAgent is a 30 year old Engineer, Brazilian, currently living in Brazil."

def test_tinyperson_pp_current_interactions(example_agent, mock_chevron_render, capsys):
    """Checks if the pp_current_interactions method prints current interactions."""
    example_agent.episodic_memory.memory = [{"role": "user", "content": {"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, 'simulation_timestamp': '2024-01-01T12:00:00'}]
    example_agent.pp_current_interactions()
    captured = capsys.readouterr()
    assert "test_source --> TestAgent" in captured.out
    assert "test content" in captured.out
    assert "Date and time of events" in captured.out


def test_tinyperson_pretty_current_interactions(example_agent, mock_chevron_render):
  """Checks if pretty_current_interactions returns formatted interactions as strings."""
  example_agent.episodic_memory.memory = [{"role": "user", "content": {"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, 'simulation_timestamp': '2024-01-01T12:00:00'}]
  interactions = example_agent.pretty_current_interactions()
  assert "test_source --> TestAgent" in interactions
  assert "test content" in interactions
  assert "Date and time of events" in interactions

  interactions = example_agent.pretty_current_interactions(first_n=1, include_omission_info=False)
  assert "test_source --> TestAgent" in interactions
  assert "test content" in interactions
  assert "Date and time of events" in interactions
  assert "Info: there were other messages here, but they were omitted for brevity." not in interactions
  
  
  example_agent.episodic_memory.memory = [{"role": "system", "content": "test system message", 'simulation_timestamp': '2024-01-01T12:00:00'},
                                            {"role": "user", "content": {"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, 'simulation_timestamp': '2024-01-01T12:00:00'}]
  interactions = example_agent.pretty_current_interactions(skip_system=True)
  assert "test system message" not in interactions
  assert "test_source --> TestAgent" in interactions
  assert "test content" in interactions
  assert "Date and time of events" in interactions

  
  example_agent.episodic_memory.memory = [{"role": "system", "content": "test system message", 'simulation_timestamp': '2024-01-01T12:00:00'},
                                            {"role": "user", "content": {"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, 'simulation_timestamp': '2024-01-01T12:00:00'}]
  interactions = example_agent.pretty_current_interactions(skip_system=False)
  assert "test system message" in interactions
  assert "test_source --> TestAgent" in interactions
  assert "test content" in interactions
  assert "Date and time of events" in interactions

  example_agent.episodic_memory.memory = [{"role": "system", "content": "test system message", 'simulation_timestamp': '2024-01-01T12:00:00'},
                                            {"role": "user", "content": {"stimuli":[{"type": "CONVERSATION", "content": "test content", "source": "test_source"}]}, 'simulation_timestamp': '2024-01-01T12:00:00'},
                                            {"role": "assistant", "content": {"action": {"type": "TALK", "content": "test action content"}}, 'simulation_timestamp': '2024-01-01T12:00:00'}]
  interactions = example