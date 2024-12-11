rst
How to use the TinyTroupe control module
========================================================================================

Description
-------------------------
This code demonStartes how to interact with the TinyTroupe simulation control module. It shows how to initialize, run, checkpoint, and end a TinyTroupe simulation. The code includes tests for different simulation scenarios, including using agents, a world, and a factory.  Crucially, it showcases the use of `Simulation.STATUS_STARTED` and `Simulation.STATUS_STOPPED` to verify the simulation's state during different phases.  It also handles file management (removing and creating the cache file) before and after each simulation run.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports essential TinyTroupe modules and functions, including simulation control classes, agent creation functions, and utility functions.


2. **Initialize simulation control:** The `control.reset()` function resets the simulation control.


3. **Begin simulation:** The `control.begin(filename)` function initializes a new simulation and creates a cache file (`filename`).  This method is used before starting the simulation.


4. **Create agents or a world:** This section sets up the entities for the simulation. This can involve creating agents (e.g., `create_oscar_the_architect()`) or a `TinyWorld` object.


5. **Add faculties (optional):**  If agents are involved,  `add_mental_faculties` can be used to give them capabilities like processing text using tools like `TinyWordProcessor`.


6. **Define agent attributes:** The code demonStartes setting agent properties like `age` and `nationality` using `agent.define()`.


7. **Run simulation (using agents or world):** For running with agents, actions like `agent.listen_and_act()` are used to drive the simulation's logic.  For running with a world, `world.run()` is used with a configurable time period.


8. **Checkpoint:** The `control.checkpoint()` function saves the simulation state to the cache file, making it possible to restore the state later.


9. **End simulation:** The `control.end()` function concludes the simulation.


10. **Assertions for simulation status:**  Crucially, the code verifies the simulation status (`Simulation.STATUS_STARTED`, `Simulation.STATUS_STOPPED`) using assertions at key points to validate that the simulation is in the expected state throughout.


11. **File existence checks:** The code uses `remove_file_if_exists()` to handle potential issues with already existing cache files, ensuring file operations run cleanly.


Usage example
-------------------------
.. code-block:: python

    import pytest
    import os
    import sys
    # ... (Import statements from the provided code)

    def test_begin_checkpoint_end_with_agent_only(setup):
        # ... (rest of the function as in the provided code)