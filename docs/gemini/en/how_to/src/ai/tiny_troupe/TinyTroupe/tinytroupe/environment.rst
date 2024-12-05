rst
How to use the TinyWorld class
========================================================================================

Description
-------------------------
The `TinyWorld` class, part of the `tinytroupe` library, provides a framework for defining and managing environments in an agent-based simulation.  It handles the interaction between agents and external entities, like search engines,  and facilitates the execution of steps within a simulated timeframe.  Crucially, it offers methods for running simulations for various durations (minutes, hours, days, etc.) and for skipping time without triggering agent actions.  It also manages the addition and removal of agents, and provides methods to retrieve agents by name.

Execution steps
-------------------------
1. **Initialization**: Create a `TinyWorld` object.  This involves providing a name for the environment, a list of agents to be included, an optional initial datetime, and whether actions should be broadcast if a target agent isn't found.

2. **Agent Management**: Add agents to the environment using `add_agents()` or `add_agent()`.  Ensure agent names are unique within the environment.  Remove agents using `remove_agent()`.  Manage agents using their unique names, retrieved using `get_agent_by_name()`.

3. **Time Advancement (Optional):** If a `timedelta_per_step` is specified when running or skipping steps, the `current_datetime` is updated.

4. **Simulation Execution**:  Run simulations using the `run()` method.  Specify the number of steps and an optional `timedelta_per_step`. The run() method also optionally returns a list of actions for each step if asked for. Skipping time without executing actions is done via `skip()` method, also accepting `timedelta_per_step` for control of the elapsed time.

5. **Action Handling**: The `_handle_actions()` method processes actions performed by agents. This method is called internally by `run()` and `skip()`, and different specific actions, like "REACH_OUT" and "TALK", are processed by methods specialized for those actions.

6. **Broadcast Handling**: Use `broadcast()`, `broadcast_thought()`, `broadcast_internal_goal()`, and `broadcast_context_change()` to communicate information across all agents in the environment. These are called by `_handle_talk()`.

7. **Encoding and Decoding**: The `encode_complete_state()` and `decode_complete_state()` methods allow you to serialize and deserialize the environment state for persistence or sharing.

8. **Communication Display**: The `_display_communication()` method manages the display and storage of the simulation communications.

9. **Convenience Methods**: The class offers several convenience methods (`run_minutes`, `skip_hours`, `run_days`, etc.) for simulating time intervals in minutes, hours, days, etc.

Usage example
-------------------------
.. code-block:: python

    from tinytroupe.environment import TinyWorld
    from tinytroupe.agent import TinyPerson
    from datetime import datetime, timedelta

    # Create agents
    agent1 = TinyPerson(name="Agent1")
    agent2 = TinyPerson(name="Agent2")

    # Create the environment
    env = TinyWorld(name="MyEnvironment", agents=[agent1, agent2], initial_datetime=datetime(2024, 1, 1))

    # Run the environment for 2 steps with a timedelta of 1 hour
    env.run(steps=2, timedelta_per_step=timedelta(hours=1))