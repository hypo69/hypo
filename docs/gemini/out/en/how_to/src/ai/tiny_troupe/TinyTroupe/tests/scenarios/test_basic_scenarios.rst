How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a test function `test_scenario_1` that interacts with the `tinytroupe` library, managing a simulation.  It verifies the simulation's startup, state changes, and data collection.  The function creates an agent (`oscar_the_architect`), defines attributes for it, and runs actions within the simulation environment. Importantly, it uses the `control` module within `tinytroupe` to manage the simulation lifecycle.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports various modules including `pytest`, `logging`, the `tinytroupe` library, `TinyPerson`, `TinyWorld`, and related classes.  This imports all the necessary components for the simulation and testing process.

2. **Initialize and Reset:** It calls `control.reset()`, clearing any existing simulation data.  It verifies that no simulation is currently running.

3. **Start Simulation:** `control.begin()` initiates the simulation, setting its status to `Simulation.STATUS_STARTED`.  This step verifies that the simulation correctly begins.

4. **Create Agent:** `create_oscar_the_architect()` instantiates an agent representing an architect.

5. **Define Agent Attributes:** The code defines attributes for the `oscar_the_architect` agent, including age and nationality. This is a data initialization step for the agent within the simulation.

6. **Verify Simulation State:**  It checks that the simulation has a cached trace and an execution trace, confirming that data is being collected during the simulation.

7. **Checkpoint 1:** `control.checkpoint()` saves a snapshot of the simulation state. This is crucial for managing the simulation's progress and possibly enabling rollback.

8. **Agent Action 1:** `agent.listen_and_act("How are you doing?")` simulates the agent's response to a user's query.

9. **Define Agent Attribute:** `agent.define("occupation", "Engineer")` adds another attribute to the agent.

10. **Checkpoint 2:** Another checkpoint is created for further data saving and possible rollback.

11. **End Simulation:** `control.end()` concludes the simulation.

Usage example
-------------------------
.. code-block:: python

    import pytest
    # ... (import statements from the original code)

    def test_scenario_1():
        # ... (reset, begin, create agent code)
        control.checkpoint() # Add a checkpoint for data management
        agent.speak("Hello!")  # Example of an agent action.
        control.checkpoint() # Another checkpoint after an action
        control.end()

    # Example usage, outside the test function, which runs the simulation
    test_scenario_1()