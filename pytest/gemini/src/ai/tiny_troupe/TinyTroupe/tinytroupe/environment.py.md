```python
import pytest
import datetime
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.agent import TinyPerson

# Fixture for creating a basic TinyWorld
@pytest.fixture
def basic_world():
    """Provides a basic TinyWorld for testing."""
    return TinyWorld(name="TestWorld")

# Fixture for creating a TinyPerson
@pytest.fixture
def basic_agent():
    """Provides a basic TinyPerson for testing."""
    return TinyPerson(name="TestAgent")

@pytest.fixture
def basic_agent2():
    """Provides a basic TinyPerson for testing."""
    return TinyPerson(name="TestAgent2")


# Fixture for creating a social network
@pytest.fixture
def basic_social_network():
    """Provides a basic TinySocialNetwork for testing."""
    return TinySocialNetwork(name="TestSocialNetwork")


# Tests for TinyWorld class
def test_tinyworld_creation():
    """Checks if a TinyWorld instance can be created successfully."""
    world = TinyWorld(name="MyWorld")
    assert world.name == "MyWorld"
    assert world.agents == []
    assert isinstance(world.current_datetime, datetime.datetime)
    assert world.broadcast_if_no_target == True
    assert world.simulation_id is None
    assert world._displayed_communications_buffer == []
    assert world.name in TinyWorld.all_environments

def test_tinyworld_creation_with_agents(basic_agent):
    """Checks if a TinyWorld instance can be created with agents successfully."""
    world = TinyWorld(name="MyWorld", agents=[basic_agent])
    assert world.name == "MyWorld"
    assert len(world.agents) == 1
    assert world.agents[0].name == "TestAgent"
    assert world.name_to_agent["TestAgent"] == basic_agent
    assert world.name in TinyWorld.all_environments
    assert basic_agent.environment == world


def test_tinyworld_creation_with_initial_datetime():
    """Checks if a TinyWorld instance can be created with initial datetime."""
    initial_datetime = datetime.datetime(2024, 1, 1, 12, 0, 0)
    world = TinyWorld(name="MyWorld", initial_datetime=initial_datetime)
    assert world.current_datetime == initial_datetime


def test_tinyworld_add_agent(basic_world, basic_agent):
    """Checks if an agent can be added to the environment."""
    basic_world.add_agent(basic_agent)
    assert basic_agent in basic_world.agents
    assert basic_world.name_to_agent["TestAgent"] == basic_agent
    assert basic_agent.environment == basic_world

def test_tinyworld_add_agents(basic_world, basic_agent, basic_agent2):
    """Checks if a list of agents can be added to the environment."""
    basic_world.add_agents([basic_agent, basic_agent2])
    assert basic_agent in basic_world.agents
    assert basic_agent2 in basic_world.agents
    assert basic_world.name_to_agent["TestAgent"] == basic_agent
    assert basic_world.name_to_agent["TestAgent2"] == basic_agent2
    assert basic_agent.environment == basic_world
    assert basic_agent2.environment == basic_world

def test_tinyworld_add_existing_agent(basic_world, basic_agent):
    """Checks if adding an existing agent to the environment does not add the agent twice."""
    basic_world.add_agent(basic_agent)
    basic_world.add_agent(basic_agent) # add again, should not add twice
    assert len(basic_world.agents) == 1
    assert basic_world.name_to_agent["TestAgent"] == basic_agent

def test_tinyworld_add_agent_duplicate_name(basic_world, basic_agent):
    """Checks if adding an agent with a duplicate name raises an error."""
    basic_world.add_agent(basic_agent)
    agent_duplicate = TinyPerson(name="TestAgent")
    with pytest.raises(ValueError, match="Agent names must be unique, but 'TestAgent' is already in the environment."):
        basic_world.add_agent(agent_duplicate)

def test_tinyworld_remove_agent(basic_world, basic_agent):
    """Checks if an agent can be removed from the environment."""
    basic_world.add_agent(basic_agent)
    basic_world.remove_agent(basic_agent)
    assert basic_agent not in basic_world.agents
    assert "TestAgent" not in basic_world.name_to_agent

def test_tinyworld_remove_all_agents(basic_world, basic_agent, basic_agent2):
    """Checks if all agents can be removed from the environment."""
    basic_world.add_agents([basic_agent, basic_agent2])
    basic_world.remove_all_agents()
    assert basic_world.agents == []
    assert basic_world.name_to_agent == {}

def test_tinyworld_get_agent_by_name(basic_world, basic_agent):
    """Checks if an agent can be retrieved by its name."""
    basic_world.add_agent(basic_agent)
    retrieved_agent = basic_world.get_agent_by_name("TestAgent")
    assert retrieved_agent == basic_agent

def test_tinyworld_get_agent_by_name_not_found(basic_world):
    """Checks if None is returned when an agent is not found."""
    retrieved_agent = basic_world.get_agent_by_name("NonExistentAgent")
    assert retrieved_agent is None

def test_tinyworld_step_no_timedelta(basic_world, basic_agent):
    """Checks if a step is correctly executed when no timedelta is provided."""
    basic_world.add_agent(basic_agent)
    initial_datetime = basic_world.current_datetime
    
    basic_world._step()
    
    assert basic_world.current_datetime == initial_datetime
    # Verify that the agent's act method was called, for example:
    # assert basic_agent.last_action_type == "DEFAULT"

def test_tinyworld_step_with_timedelta(basic_world, basic_agent):
    """Checks if a step is correctly executed when a timedelta is provided."""
    basic_world.add_agent(basic_agent)
    initial_datetime = basic_world.current_datetime
    delta = datetime.timedelta(minutes=10)
    
    basic_world._step(timedelta_per_step=delta)
    
    assert basic_world.current_datetime == initial_datetime + delta
    # Verify that the agent's act method was called, for example:
    # assert basic_agent.last_action_type == "DEFAULT"

def test_tinyworld_advance_datetime(basic_world):
    """Checks if the datetime is advanced correctly."""
    initial_datetime = basic_world.current_datetime
    delta = datetime.timedelta(days=1)
    basic_world._advance_datetime(delta)
    assert basic_world.current_datetime == initial_datetime + delta

def test_tinyworld_advance_datetime_no_delta(basic_world):
    """Checks if the datetime is not advanced when no delta is provided."""
    initial_datetime = basic_world.current_datetime
    basic_world._advance_datetime(None)
    assert basic_world.current_datetime == initial_datetime

def test_tinyworld_run(basic_world, basic_agent):
    """Checks if the environment runs for the specified number of steps."""
    basic_world.add_agent(basic_agent)
    initial_datetime = basic_world.current_datetime
    steps = 3
    delta = datetime.timedelta(minutes=1)

    basic_world.run(steps=steps, timedelta_per_step=delta)

    assert basic_world.current_datetime == initial_datetime + (steps * delta)
    
def test_tinyworld_run_return_actions(basic_world, basic_agent):
    """Checks if the environment runs for the specified number of steps and returns the actions."""
    basic_world.add_agent(basic_agent)
    steps = 2
    delta = datetime.timedelta(minutes=1)

    actions_over_time = basic_world.run(steps=steps, timedelta_per_step=delta, return_actions=True)
    
    assert len(actions_over_time) == steps
    # assert actions_over_time == [{"TestAgent": ["DEFAULT_ACTION"]}, {"TestAgent": ["DEFAULT_ACTION"]}]
    # Verify structure of returned actions

def test_tinyworld_skip(basic_world):
    """Checks if the environment skips the specified number of steps without acting."""
    initial_datetime = basic_world.current_datetime
    steps = 2
    delta = datetime.timedelta(days=1)
    basic_world.skip(steps=steps, timedelta_per_step=delta)
    assert basic_world.current_datetime == initial_datetime + (steps * delta)

def test_tinyworld_run_minutes(basic_world):
    """Checks if the environment runs for the specified number of minutes."""
    initial_datetime = basic_world.current_datetime
    minutes = 60
    basic_world.run_minutes(minutes=minutes)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(minutes=minutes)

def test_tinyworld_skip_minutes(basic_world):
    """Checks if the environment skips for the specified number of minutes."""
    initial_datetime = basic_world.current_datetime
    minutes = 60
    basic_world.skip_minutes(minutes=minutes)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(minutes=minutes)

def test_tinyworld_run_hours(basic_world):
    """Checks if the environment runs for the specified number of hours."""
    initial_datetime = basic_world.current_datetime
    hours = 2
    basic_world.run_hours(hours=hours)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(hours=hours)

def test_tinyworld_skip_hours(basic_world):
    """Checks if the environment skips for the specified number of hours."""
    initial_datetime = basic_world.current_datetime
    hours = 2
    basic_world.skip_hours(hours=hours)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(hours=hours)

def test_tinyworld_run_days(basic_world):
    """Checks if the environment runs for the specified number of days."""
    initial_datetime = basic_world.current_datetime
    days = 7
    basic_world.run_days(days=days)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(days=days)

def test_tinyworld_skip_days(basic_world):
    """Checks if the environment skips for the specified number of days."""
    initial_datetime = basic_world.current_datetime
    days = 7
    basic_world.skip_days(days=days)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(days=days)

def test_tinyworld_run_weeks(basic_world):
    """Checks if the environment runs for the specified number of weeks."""
    initial_datetime = basic_world.current_datetime
    weeks = 4
    basic_world.run_weeks(weeks=weeks)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(weeks=weeks)

def test_tinyworld_skip_weeks(basic_world):
    """Checks if the environment skips for the specified number of weeks."""
    initial_datetime = basic_world.current_datetime
    weeks = 4
    basic_world.skip_weeks(weeks=weeks)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(weeks=weeks)

def test_tinyworld_run_months(basic_world):
    """Checks if the environment runs for the specified number of months."""
    initial_datetime = basic_world.current_datetime
    months = 6
    basic_world.run_months(months=months)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(weeks=months*4)

def test_tinyworld_skip_months(basic_world):
    """Checks if the environment skips for the specified number of months."""
    initial_datetime = basic_world.current_datetime
    months = 6
    basic_world.skip_months(months=months)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(weeks=months*4)

def test_tinyworld_run_years(basic_world):
    """Checks if the environment runs for the specified number of years."""
    initial_datetime = basic_world.current_datetime
    years = 1
    basic_world.run_years(years=years)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(days=years*365)

def test_tinyworld_skip_years(basic_world):
    """Checks if the environment skips for the specified number of years."""
    initial_datetime = basic_world.current_datetime
    years = 1
    basic_world.skip_years(years=years)
    assert basic_world.current_datetime == initial_datetime + datetime.timedelta(days=years*365)

def test_tinyworld_broadcast(basic_world, basic_agent):
    """Checks if a message is broadcasted to all agents."""
    basic_world.add_agent(basic_agent)
    message = "Hello everyone!"
    basic_world.broadcast(message, source=basic_agent)

    # Verify that the agent's listen method was called with correct message, for example:
    # assert basic_agent.last_speech == message

def test_tinyworld_broadcast_thought(basic_world, basic_agent):
    """Checks if a thought is broadcasted to all agents."""
    basic_world.add_agent(basic_agent)
    thought = "I am thinking..."
    basic_world.broadcast_thought(thought)

     # Verify that the agent's think method was called with correct thought, for example:
    # assert basic_agent.last_thought == thought
    
def test_tinyworld_broadcast_internal_goal(basic_world, basic_agent):
    """Checks if an internal goal is broadcasted to all agents."""
    basic_world.add_agent(basic_agent)
    goal = "My goal is to do something"
    basic_world.broadcast_internal_goal(goal)

    # Verify that the agent's internalize_goal method was called with correct internal goal, for example:
    # assert basic_agent.last_internal_goal == goal

def test_tinyworld_broadcast_context_change(basic_world, basic_agent):
    """Checks if a context change is broadcasted to all agents."""
    basic_world.add_agent(basic_agent)
    context = ["new_context1", "new_context2"]
    basic_world.broadcast_context_change(context)
    
     # Verify that the agent's change_context method was called with correct context, for example:
    # assert basic_agent.last_context == context

def test_tinyworld_make_everyone_accessible(basic_world, basic_agent, basic_agent2):
    """Checks if all agents are made accessible to each other."""
    basic_world.add_agents([basic_agent, basic_agent2])
    basic_world.make_everyone_accessible()
    
    assert basic_agent2 in basic_agent.accessible_agents
    assert basic_agent in basic_agent2.accessible_agents

def test_tinyworld_display_communication(basic_world):
    """Checks if display communication is correctly added to the buffer."""
    basic_world._display_communication(cur_step=1, total_steps=10, kind="step", timedelta_per_step=datetime.timedelta(minutes=1))
    assert len(basic_world._displayed_communications_buffer) == 1
    
    communication = basic_world._displayed_communications_buffer[0]
    assert communication["kind"] == "step"
    assert "step 1 of 10" in communication["content"]

def test_tinyworld_push_and_display_latest_communication(basic_world):
    """Checks if push and display is working correctly."""
    rendering = {"content": "test", "kind": "test_kind"}
    basic_world._push_and_display_latest_communication(rendering)
    assert len(basic_world._displayed_communications_buffer) == 1
    assert basic_world._displayed_communications_buffer[0] == rendering

def test_tinyworld_pop_and_display_latest_communications(basic_world):
    """Checks if pop and display of communication is working correctly."""
    rendering1 = {"content": "test1", "kind": "test_kind1"}
    rendering2 = {"content": "test2", "kind": "test_kind2"}
    basic_world._push_and_display_latest_communication(rendering1)
    basic_world._push_and_display_latest_communication(rendering2)
    
    communications = basic_world.pop_and_display_latest_communications()
    
    assert len(basic_world._displayed_communications_buffer) == 0
    assert communications == [rendering1, rendering2]

def test_tinyworld_clear_communications_buffer(basic_world):
    """Checks if the communications buffer is cleared correctly."""
    rendering = {"content": "test", "kind": "test_kind"}
    basic_world._push_and_display_latest_communication(rendering)
    basic_world.clear_communications_buffer()
    assert len(basic_world._displayed_communications_buffer) == 0

def test_tinyworld_pretty_step(basic_world):
    """Checks if the pretty step formatting works correctly"""
    rendering = basic_world._pretty_step(cur_step=5, total_steps=10, timedelta_per_step=datetime.timedelta(minutes=1))
    assert "TestWorld step 5 of 10" in rendering
    assert "(" in rendering
    
def test_tinyworld_pretty_step_no_timedelta(basic_world):
    """Checks if the pretty step formatting works correctly when there is no time delta."""
    rendering = basic_world._pretty_step(cur_step=5, total_steps=10, timedelta_per_step=None)
    assert "TestWorld step 5 of 10" in rendering
    assert "(" not in rendering

def test_tinyworld_repr(basic_world):
    """Checks the __repr__ method of TinyWorld."""
    assert repr(basic_world) == "TinyWorld(name='TestWorld')"

def test_tinyworld_pp_current_interactions(basic_world, basic_agent):
   """Checks if the pretty print interactions method works correctly."""
   basic_world.add_agent(basic_agent)

   # this test can only verify that the method executes without problems, since the output
   # depends on other classes.
   try:
       basic_world.pp_current_interactions()
   except Exception as e:
        assert False, f"pp_current_interactions raised an exception: {e}"
    
def test_tinyworld_pretty_current_interactions(basic_world, basic_agent):
    """Checks if the pretty current interactions method works correctly."""
    basic_world.add_agent(basic_agent)
    
    # this test can only verify that the method executes without problems, since the output
    # depends on other classes.
    try:
        basic_world.pretty_current_interactions()
    except Exception as e:
            assert False, f"pretty_current_interactions raised an exception: {e}"

def test_tinyworld_handle_actions_reach_out(basic_world, basic_agent, basic_agent2):
   """Tests the _handle_actions method with REACH_OUT action."""
   basic_world.add_agents([basic_agent, basic_agent2])
   action = {"type": "REACH_OUT", "content": "reaching out", "target": "TestAgent2"}
   
   basic_world._handle_actions(basic_agent, [action])
   
   assert basic_agent2 in basic_agent.accessible_agents
   assert basic_agent in basic_agent2.accessible_agents
   # assert "was successfully reached out" in basic_agent.last_speech
   # assert "reached out to you" in basic_agent2.last_speech


def test_tinyworld_handle_actions_talk(basic_world, basic_agent, basic_agent2):
    """Tests the _handle_actions method with TALK action."""
    basic_world.add_agents([basic_agent, basic_agent2])
    action = {"type": "TALK", "content": "hello", "target": "TestAgent2"}
    
    basic_world._handle_actions(basic_agent, [action])

     # Verify that the agent's listen method was called with the message, for example:
    # assert basic_agent2.last_speech == "hello"

def test_tinyworld_handle_actions_talk_broadcast(basic_world, basic_agent, basic_agent2):
    """Tests the _handle_actions method with TALK action where the target is not found, hence broadcast."""
    basic_world.add_agents([basic_agent])
    action = {"type": "TALK", "content": "hello", "target": "NonExistentAgent"}
    
    basic_world._handle_actions(basic_agent, [action])
    
    # Verify that the agent's listen method was called with the message, for example:
    # assert basic_agent.last_speech == "hello"

def test_tinyworld_handle_actions_unknown_type(basic_world, basic_agent):
   """Tests the _handle_actions method with an unknown action type."""
   action = {"type": "UNKNOWN_ACTION", "content": "some content"}
   
   basic_world._handle_actions(basic_agent, [action])
   # Test that no error is raised, and the unknown action is ignored.

def test_tinyworld_encode_decode_state(basic_world, basic_agent, basic_agent2):
    """Checks if the complete state can be encoded and decoded correctly."""
    basic_world.add_agents([basic_agent, basic_agent2])
    
    # set a timedelta
    delta = datetime.timedelta(minutes=10)
    basic_world._advance_datetime(delta)

    # do one step and set the actions of the agents
    basic_world._step()
    
    encoded_state = basic_world.encode_complete_state()
    decoded_world = TinyWorld().decode_complete_state(encoded_state)
    
    assert decoded_world.name == "TestWorld"
    assert decoded_world.current_datetime == basic_world.current_datetime
    assert len(decoded_world.agents) == 2
    assert decoded_world.agents[0].name == "TestAgent"
    assert decoded_world.agents[1].name == "TestAgent2"
    #assert decoded_world.agents[0].last_action_type == "DEFAULT"
    #assert decoded_world.agents[1].last_action_type == "DEFAULT"

def test_tinyworld_encode_decode_state_no_agents(basic_world):
    """Checks if the complete state can be encoded and decoded correctly when no agents are present."""
    encoded_state = basic_world.encode_complete_state()
    decoded_world = TinyWorld().decode_complete_state(encoded_state)
    
    assert decoded_world.name == "TestWorld"
    assert decoded_world.agents == []

def test_tinyworld_add_environment():
    """Checks if an environment can be added to the global dictionary."""
    world = TinyWorld(name="TestEnv")
    
    assert "TestEnv" in TinyWorld.all_environments
    assert TinyWorld.all_environments["TestEnv"] == world

def test_tinyworld_add_environment_duplicate_name():
   """Checks if adding an environment with duplicate name raises an exception."""
   world1 = TinyWorld(name="TestEnv")
   with pytest.raises(ValueError, match="Environment names must be unique, but \'TestEnv\' is already defined."):
        world2 = TinyWorld(name="TestEnv")

def test_tinyworld_set_simulation_for_free_environments(basic_world):
    """Checks if the simulation is set only when free environments are detected."""
    class MockSimulation:
        def __init__(self):
            self.environments = []
        
        def add_environment(self, environment):
            self.environments.append(environment)

    simulation = MockSimulation()
    basic_world.simulation_id = 123 # if a simulation id is provided, it should not add to the "free environments".

    TinyWorld.set_simulation_for_free_environments(simulation)
    assert len(simulation.environments) == 0
    
    basic_world.simulation_id = None
    TinyWorld.set_simulation_for_free_environments(simulation)
    assert len(simulation.environments) == 1
    assert simulation.environments[0] == basic_world

def test_tinyworld_get_environment_by_name():
    """Checks if an environment can be retrieved by its name."""
    world = TinyWorld(name="TestEnv")
    retrieved_env = TinyWorld.get_environment_by_name("TestEnv")
    assert retrieved_env == world

def test_tinyworld_get_environment_by_name_not_found():
    """Checks if None is returned if an environment is not found."""
    retrieved_env = TinyWorld.get_environment_by_name("NonExistentEnv")
    assert retrieved_env is None

def test_tinyworld_clear_environments():
    """Checks if the environment dictionary is cleared correctly."""
    world = TinyWorld(name="TestEnv")
    TinyWorld.clear_environments()
    assert TinyWorld.all_environments == {}
    
def test_tinysocialnetwork_creation():
    """Checks if a TinySocialNetwork instance can be created successfully."""
    network = TinySocialNetwork(name="MySocialNetwork")
    assert network.name == "MySocialNetwork"
    assert network.agents == []
    assert isinstance(network.current_datetime, datetime.datetime)
    assert network.broadcast_if_no_target == True
    assert network.simulation_id is None
    assert network._displayed_communications_buffer == []
    assert network.name in TinyWorld.all_environments
    assert network.relations == {}

def test_tinysocialnetwork_add_relation(basic_social_network, basic_agent, basic_agent2):
    """Checks if a relation can be added to the social network."""
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    assert "friendship" in basic_social_network.relations
    assert (basic_agent, basic_agent2) in basic_social_network.relations["friendship"]
    assert basic_agent in basic_social_network.agents
    assert basic_agent2 in basic_social_network.agents

def test_tinysocialnetwork_add_relation_agents_already_in_network(basic_social_network, basic_agent, basic_agent2):
    """Checks if adding an relation with agents already in the network does not add them again."""
    basic_social_network.add_agent(basic_agent)
    basic_social_network.add_agent(basic_agent2)
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    
    assert len(basic_social_network.agents) == 2

def test_tinysocialnetwork_update_agents_contexts(basic_social_network, basic_agent, basic_agent2):
    """Checks if agents' contexts are updated based on relations."""
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    basic_social_network._update_agents_contexts()
    assert basic_agent2 in basic_agent.accessible_agents
    assert basic_agent in basic_agent2.accessible_agents

def test_tinysocialnetwork_step(basic_social_network, basic_agent, basic_agent2):
    """Checks if a step correctly updates agents' contexts and runs the base step."""
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    initial_datetime = basic_social_network.current_datetime
    basic_social_network._step()
    
    assert basic_social_network.current_datetime == initial_datetime
    assert basic_agent2 in basic_agent.accessible_agents
    assert basic_agent in basic_agent2.accessible_agents

def test_tinysocialnetwork_handle_reach_out_success(basic_social_network, basic_agent, basic_agent2):
    """Checks if a successful reach out is handled."""
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    action = {"type": "REACH_OUT", "content": "reaching out", "target": "TestAgent2"}
    
    basic_social_network._handle_actions(basic_agent, [action])
    
    assert basic_agent2 in basic_agent.accessible_agents
    assert basic_agent in basic_agent2.accessible_agents
    # assert "was successfully reached out" in basic_agent.last_speech
    # assert "reached out to you" in basic_agent2.last_speech

def test_tinysocialnetwork_handle_reach_out_failure(basic_social_network, basic_agent, basic_agent2):
    """Checks if a reach out fails if agents are not related."""
    basic_social_network.add_agent(basic_agent)
    basic_social_network.add_agent(basic_agent2)
    action = {"type": "REACH_OUT", "content": "reaching out", "target": "TestAgent2"}
    
    basic_social_network._handle_actions(basic_agent, [action])

    assert basic_agent2 not in basic_agent.accessible_agents
    assert basic_agent not in basic_agent2.accessible_agents
    # assert "is not in the same relation as you" in basic_agent.last_speech

def test_tinysocialnetwork_is_in_relation_with(basic_social_network, basic_agent, basic_agent2):
    """Checks if two agents are in a relation."""
    basic_social_network.add_relation(basic_agent, basic_agent2, "friendship")
    assert basic_social_network.is_in_relation_with(basic_agent, basic_agent2, "friendship") == True
    assert basic_social_network.is_in_relation_with(basic_agent2, basic_agent, "friendship") == True
    assert basic_social_network.is_in_relation_with(basic_agent, basic_agent2) == True
    assert basic_social_network.is_in_relation_with(basic_agent, TinyPerson(name="TestAgent3"), "friendship") == False
    assert basic_social_network.is_in_relation_with(basic_agent, TinyPerson(name="TestAgent3")) == False
    assert basic_social_network.is_in_relation_with(basic_agent, basic_agent2, "otherrelation") == False

```