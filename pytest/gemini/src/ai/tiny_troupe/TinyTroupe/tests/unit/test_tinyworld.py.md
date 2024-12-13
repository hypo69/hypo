```python
import pytest
import logging
logger = logging.getLogger("tinytroupe")

import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
from tinytroupe.environment import TinyWorld
from testing_utils import *

# Fixture to provide a pre-configured TinyWorld with agents
@pytest.fixture
def focus_group_world():
    """Provides a TinyWorld instance with three agents for testing."""
    agents = [create_lisa_the_data_scientist(), create_oscar_the_architect(), create_marcos_the_physician()]
    world = TinyWorld("Focus Group", agents)
    return world


def test_run_empty_world():
    """Tests the run method with an empty world."""
    # Create an empty world
    world_1 = TinyWorld("Empty land", [])
    # Run the world for 2 steps
    world_1.run(2)
    # No assertions needed here, just checking that it runs without errors
    # and doesn't break the program.


def test_run_with_agents(focus_group_world):
    """Tests the run method with a world containing agents."""
    # Use the focus_group_world fixture
    world_2 = focus_group_world
    # Broadcast a message to all agents
    world_2.broadcast("Discuss ideas for a new AI product you'd love to have.")
    # Run the world for 2 steps
    world_2.run(2)

    # Check integrity of conversation
    for agent in world_2.agents:
        for msg in agent.episodic_memory.retrieve_all():
            # Check that no agent sends messages to itself
            if 'action' in msg['content'] and 'target' in msg['content']['action']:
                assert msg['content']['action']['target'] != agent.name, f"{agent.name} should not have any messages with itself as the target."
            # TODO stimulus integrity check?


def test_broadcast_message_received(focus_group_world):
    """Tests that broadcast messages are received by all agents."""
    world = focus_group_world
    # Broadcast a message
    world.broadcast("""
                Folks, we need to brainstorm ideas for a new baby product. Something moms have been asking for centuries and never got.

                Please start the discussion now.
                """)

    # Check if each agent received the message
    for agent in world.agents:
        first_message = agent.episodic_memory.retrieve_first(1)[0]
        # Assert that the message content is what's expected
        assert "Folks, we need to brainstorm" in first_message['content']['stimuli'][0]['content'], f"{agent.name} should have received the message."


def test_encode_complete_state_valid(focus_group_world):
    """Tests the encoding of a complete world state."""
    world = focus_group_world

    # Encode the state
    state = world.encode_complete_state()

    # Assert the state is not None
    assert state is not None, "The state should not be None."
    # Assert the state contains the world name
    assert state['name'] == world.name, "The state should have the world name."
    # Assert the state contains agents
    assert state['agents'] is not None, "The state should have the agents."


def test_decode_complete_state_valid(focus_group_world):
    """Tests the decoding of a complete world state."""
    world = focus_group_world

    # Store initial world state
    name_1 = world.name
    n_agents_1 = len(world.agents)

    # Encode the state
    state = world.encode_complete_state()

    # Mess up the world
    world.name = "New name"
    world.agents = []

    # Decode the state back into the world
    world_2 = world.decode_complete_state(state)

    # Check if the decoded world is valid
    assert world_2 is not None, "The world should not be None."
    # Check if the name has been restored
    assert world_2.name == name_1, "The world should have the same name."
    # Check if the agents have been restored
    assert len(world_2.agents) == n_agents_1, "The world should have the same number of agents."
```