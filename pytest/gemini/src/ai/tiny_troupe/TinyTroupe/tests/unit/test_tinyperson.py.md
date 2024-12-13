```python
import pytest
import logging
import sys
import os

# Ensure that the package is imported from the parent directory
sys.path.insert(0, '../../tinytroupe/')
sys.path.insert(0, '../../')
sys.path.insert(0, '..')

from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tiny_person import TinyPerson
from testing_utils import *


logger = logging.getLogger("tinytroupe")


@pytest.fixture
def setup():
    """Provides a setup fixture for the tests."""
    # Setup code, if any, can go here. This one does not need setup.
    pass

def test_act(setup):
    """
    Tests the act method of TinyPerson.
    Verifies that the agent produces at least one action, a TALK action, and terminates with a DONE action.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        actions = agent.listen_and_act("Tell me a bit about your life.", return_actions=True)
        logger.info(agent.pp_current_interactions())
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform (even if it is just DONE)."
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we asked him to do so."
        assert terminates_with_action_type(actions, "DONE"), f"{agent.name} should always terminate with a DONE action."


def test_listen(setup):
    """
    Tests the listen method of TinyPerson.
    Verifies that the agent updates its current messages and episodic memory correctly after listening to a speech stimulus.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.listen("Hello, how are you?")

        assert len(agent.current_messages) > 0, f"{agent.name} should have at least one message in its current messages."
        assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user', f"{agent.name} should have the last message as 'user'."
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION', f"{agent.name} should have the last message as a 'CONVERSATION' stimulus."
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?', f"{agent.name} should have the last message with the correct content."


def test_define(setup):
    """
    Tests the define method of TinyPerson.
    Verifies that the agent updates its configuration and prompt correctly after defining a new value.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        original_prompt = agent.current_messages[0]['content']

        agent.define('age', 25)

        assert agent._configuration['age'] == 25, f"{agent.name} should have the age set to 25."
        assert agent.current_messages[0]['content'] != original_prompt, f"{agent.name} should have a different prompt after defining a new value."
        assert '25' in agent.current_messages[0]['content'], f"{agent.name} should have the age in the prompt."


def test_define_several(setup):
    """
    Tests the define_several method of TinyPerson.
    Verifies that the agent correctly adds several values to a specified group in its configuration.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.define_several(group="skills", records=["Python", "Machine learning", "GPT-3"])
        assert "Python" in agent._configuration["skills"], f"{agent.name} should have Python as a skill."
        assert "Machine learning" in agent._configuration["skills"], f"{agent.name} should have Machine learning as a skill."
        assert "GPT-3" in agent._configuration["skills"], f"{agent.name} should have GPT-3 as a skill."

def test_socialize(setup):
    """
    Tests the socialize method of TinyPerson.
    Verifies that the agent correctly interacts with another agent, including adding the friend to the list and referencing it in the conversation.
    """
    an_oscar = create_oscar_the_architect()
    a_lisa = create_lisa_the_data_scientist()
    for agent in [an_oscar, a_lisa]:
        other = a_lisa if agent.name == "Oscar" else an_oscar
        agent.make_agent_accessible(other, relation_description="My friend")
        agent.listen(f"Hi {agent.name}, I am {other.name}.")
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we started a conversation."
        assert contains_action_content(actions, other.name), f"{agent.name} should mention {other.name} in the TALK action, since they are friends."


def test_see(setup):
    """
    Tests the see method of TinyPerson.
    Verifies that the agent correctly processes a visual stimulus and generates a THINK action related to the content.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.see("A beautiful sunset over the ocean.")
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        assert contains_action_type(actions, "THINK"), f"{agent.name} should have at least one THINK action to perform, since they saw something interesting."
        assert contains_action_content(actions, "sunset"), f"{agent.name} should mention the sunset in the THINK action, since they saw it."


def test_think(setup):
    """
    Tests the think method of TinyPerson.
    Verifies that the agent correctly processes a thought and generates a TALK action related to that thought.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.think("I will tell everyone right now how awesome life is!")
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since they are eager to talk."
        assert contains_action_content(actions, "life"), f"{agent.name} should mention life in the TALK action, since they thought about it."

def test_internalize_goal(setup):
    """
    Tests the internalize_goal method of TinyPerson.
    Verifies that the agent correctly internalizes a goal and generates a SEARCH action related to that goal.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.internalize_goal("I want to learn more about GPT-3.")
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        assert contains_action_type(actions, "SEARCH"), f"{agent.name} should have at least one SEARCH action to perform, since they have a learning goal."
        assert contains_action_content(actions, "GPT-3"), f"{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it."

def test_move_to(setup):
    """
    Tests the move_to method of TinyPerson.
    Verifies that the agent correctly updates its current location and context.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.move_to("New York", context=["city", "busy", "diverse"])
        assert agent._configuration["current_location"] == "New York", f"{agent.name} should have New York as the current location."
        assert "city" in agent._configuration["current_context"], f"{agent.name} should have city as part of the current context."
        assert "busy" in agent._configuration["current_context"], f"{agent.name} should have busy as part of the current context."
        assert "diverse" in agent._configuration["current_context"], f"{agent.name} should have diverse as part of the current context."

def test_change_context(setup):
    """
    Tests the change_context method of TinyPerson.
    Verifies that the agent correctly updates its current context.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.change_context(["home", "relaxed", "comfortable"])
        assert "home" in agent._configuration["current_context"], f"{agent.name} should have home as part of the current context."
        assert "relaxed" in agent._configuration["current_context"], f"{agent.name} should have relaxed as part of the current context."
        assert "comfortable" in agent._configuration["current_context"], f"{agent.name} should have comfortable as part of the current context."

def test_save_spec(setup):
    """
    Tests the save_spec and load_spec methods of TinyPerson.
    Verifies that the agent's specification can be correctly saved to a file and loaded back, maintaining the original configuration (except for the name).
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # save to a file
        file_path = get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json")
        agent.save_spec(file_path, include_memory=True)

        # check that the file exists
        assert os.path.exists(file_path), f"{agent.name} should have saved the file."

        # load the file to see if the agent is the same. The agent name should be different because it TinyTroupe does not allow two agents with the same name.
        loaded_name = f"{agent.name}_loaded"
        loaded_agent = TinyPerson.load_spec(file_path, new_agent_name=loaded_name)

        # check that the loaded agent is the same as the original
        assert loaded_agent.name == loaded_name, f"{agent.name} should have the same name as the loaded agent."
        
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True), f"{agent.name} should have the same configuration as the loaded agent, except for the name."
```