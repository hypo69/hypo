# tinytroupe.environment

## Overview

This module defines the `TinyWorld` class, which serves as the base class for environments.  It provides methods for managing agents within the environment, handling agent actions, and simulating interactions over time.  The `TinySocialNetwork` class extends `TinyWorld` to incorporate social relationships between agents.


## Classes

### `TinyWorld`

**Description**: The base class for defining environments in the Tiny Troupe framework.  It manages agents, their actions, and the passage of time.  It supports running simulations for a specified number of steps or time intervals (minutes, hours, days, weeks, months, or years).


**Methods**

- `__init__(self, name: str="A TinyWorld", agents=[], initial_datetime=datetime.datetime.now(), broadcast_if_no_target=True)`: Initializes a `TinyWorld` instance.
    * **Parameters**:
        * `name` (str): The name of the environment.
        * `agents` (list): A list of `TinyPerson` agents to add to the environment.
        * `initial_datetime` (datetime): The initial datetime of the environment. Defaults to the current datetime.
        * `broadcast_if_no_target` (bool): If True, broadcasts actions if the target of an action is not found.
    * **Raises**:
        * `ValueError`: If an agent with the same name already exists in the environment.
- `_step(self, timedelta_per_step=None)`: Performs a single step in the environment.
    * **Parameters**:
        * `timedelta_per_step` (timedelta, optional): The time interval between steps.
    * **Returns**:
        * dict: A dictionary containing actions taken by each agent in the current step.
- `_advance_datetime(self, timedelta)`: Advances the current datetime of the environment.
    * **Parameters**:
        * `timedelta` (timedelta): The timedelta to advance by.
- `run(self, steps: int, timedelta_per_step=None, return_actions=False)`: Runs the environment for a given number of steps.
    * **Parameters**:
        * `steps` (int): The number of steps to run the environment for.
        * `timedelta_per_step` (timedelta, optional): The time interval between steps.
        * `return_actions` (bool, optional): If True, returns the actions taken by the agents over time.
    * **Returns**:
        * list: A list of actions taken by the agents if `return_actions` is True.
- `skip(self, steps: int, timedelta_per_step=None)`: Skips a given number of steps in the environment.
    * **Parameters**:
        * `steps` (int): The number of steps to skip.
        * `timedelta_per_step` (timedelta, optional): The time interval between steps.
- `run_minutes(self, minutes: int)`: Runs the environment for a given number of minutes.
    * **Parameters**:
        * `minutes` (int): The number of minutes to run the environment for.
- `skip_minutes(self, minutes: int)`: Skips a given number of minutes in the environment.
    * **Parameters**:
        * `minutes` (int): The number of minutes to skip.
- `run_hours(self, hours: int)` and similar (`skip_hours`, `run_days`, `skip_days`, `run_weeks`, `skip_weeks`, `run_months`, `skip_months`, `run_years`, `skip_years`):  Methods for running or skipping the environment for various time intervals.


- `add_agents(self, agents: list)`: Adds a list of agents to the environment.
    * **Parameters**:
        * `agents` (list): A list of agents to add.
- `add_agent(self, agent: TinyPerson)`: Adds a single agent to the environment.
    * **Parameters**:
        * `agent` (`TinyPerson`): The agent to add.
    * **Raises**:
        * `ValueError`: If the agent name already exists in the environment.
- `remove_agent(self, agent: TinyPerson)`: Removes an agent from the environment.
    * **Parameters**:
        * `agent` (`TinyPerson`): The agent to remove.
- `remove_all_agents(self)`: Removes all agents from the environment.
- `get_agent_by_name(self, name: str) -> TinyPerson`: Returns an agent by its name.
- `_handle_actions(self, source: TinyPerson, actions: list)`: Handles the actions issued by agents.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Handles the REACH_OUT action.
- `_handle_talk(self, source_agent: TinyPerson, content: str, target: str)`: Handles the TALK action.
- `broadcast(self, speech: str, source: AgentOrWorld=None)`: Delivers a speech to all agents in the environment.
- `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`: Delivers a thought to all agents.
- `broadcast_internal_goal(self, internal_goal: str)`: Broadcasts an internal goal.
- `broadcast_context_change(self, context: list)`: Broadcasts a context change.
- `make_everyone_accessible(self)`: Makes all agents accessible to each other.
- `_display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)`: Displays environment communication and stores it in a buffer.
- `_push_and_display_latest_communication(self, rendering)`: Pushes the latest communication to the agent's buffer and displays it.
- `pop_and_display_latest_communications(self)`: Pops and displays latest communications. Clears the buffer.
- `clear_communications_buffer(self)`: Clears the communications buffer.
- `__repr__(self)`: Returns a string representation of the `TinyWorld` object.
- `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`: Returns a formatted string representation of the step.
- `pp_current_interactions(self, simplified=True, skip_system=True)`: Pretty prints current agent interactions.
- `pretty_current_interactions(self, simplified=True, skip_system=True, ...)`: Returns a formatted string of current agent interactions.
- `encode_complete_state(self) -> dict`: Encodes the complete state of the environment.
- `decode_complete_state(self, state:dict) -> Self`: Decodes the complete environment state from a dictionary.

### `TinySocialNetwork`

**Description**: A specialized environment for simulating social interactions. It extends `TinyWorld` by incorporating relationships between agents.


**Methods**

- `__init__(self, name, broadcast_if_no_target=True)`: Initializes a `TinySocialNetwork` environment.
- `add_relation(self, agent_1, agent_2, name="default")`: Adds a relation between two agents.
- `_update_agents_contexts(self)`: Updates agents' contexts based on relations.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Implements REACH_OUT action for social network.
- `is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool`: Checks if two agents are in a relation.


## Functions

### `TinyWorld.add_environment(environment)`

**Description**: Adds an environment to the global list of environments.
* **Parameters**:
    * `environment`: The `TinyWorld` environment to add.
* **Raises**:
    * `ValueError`: If an environment with the same name already exists.

### `TinyWorld.set_simulation_for_free_environments(simulation)`

**Description**: Sets the simulation for any free environments (environments without a simulation ID).
* **Parameters**:
    * `simulation`: The simulation to associate with environments.

### `TinyWorld.get_environment_by_name(name: str)`

**Description**: Returns an environment by its name.
* **Parameters**:
    * `name` (str): The name of the environment.
* **Returns**:
    * `TinyWorld`: The environment with the specified name, or `None` if not found.

### `TinyWorld.clear_environments()`

**Description**: Clears the global list of environments.


## Attributes

- `TinyWorld.all_environments`: A dictionary mapping environment names to `TinyWorld` instances.
- `TinyWorld.communication_display`: A boolean indicating whether environment communications should be displayed.