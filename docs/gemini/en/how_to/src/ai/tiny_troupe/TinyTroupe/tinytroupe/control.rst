rst
How to use the simulation control code
========================================================================================

Description
-------------------------
This code defines a `Simulation` class and related functions for controlling simulations, including transaction management, caching, and checkpointing. It allows managing agents, environments, and factories within a simulation, and enables skipping executions based on a cached state.  The `Simulation` class tracks the simulation's status, agents, environments, factories, and a cache of simulation states. The `Transaction` class facilitates transactional execution of functions within the simulation, potentially caching results for efficiency and consistency.  The code utilizes JSON for persistent caching and provides functions for starting, ending, checkpointing, and retrieving the current simulation.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `json`, `os`, `tempfile`, `logging`, and custom modules (`tinytroupe` and `tinytroupe.utils`).

2. **Define the `Simulation` class:** This class handles the simulation control logic, including initialization, starting (`begin`), ending (`end`), checkpointing (`checkpoint`), and adding agents, environments, and factories.

3. **Define the `Transaction` class:** This class encapsulates a transactional execution of a function within the simulation.  Critically, it checks for a cached execution result, and if found, skips the function execution and returns the cached result. Otherwise, it executes the function, caches the result, and saves the state.

4. **Define helper functions:**  `reset`, `_simulation`, `begin`, `end`, `checkpoint`, `current_simulation` provide convenient access to initializing, starting/ending, and retrieving the current simulation, which avoids direct access to the global simulation object.

5. **Define the `transactional` decorator:** This decorator makes a function simulation-aware; it manages transactions, potentially caching execution outputs and restoring simulation states.

6. **Error Handling:** The code includes exception handling (`ValueError`) to catch cases where operations are attempted on a simulation that's not in the correct state. It also handles `FileNotFoundError` when loading cache files.

7. **Cache mechanism**: The simulation maintains a `cached_trace` of states, designed to store a history of simulation states. The `_is_transaction_event_cached` and `_skip_execution_with_cache` functions manage how to use this cache during execution.

8. **Transaction management**: The `begin_transaction` and `end_transaction` methods manage transactions for a simulation.


Usage example
-------------------------
.. code-block:: python

    import tinytroupe

    # Reset the simulation control state
    tinytroupe.reset()

    # Start a simulation with a custom cache path
    tinytroupe.begin(cache_path="./my_simulation_cache.json", id="my_simulation")

    # Add an agent
    # Assuming TinyPerson is defined in tinytroupe.agent
    agent = tinytroupe.TinyPerson("agent1")
    # ... (add agent to environment)
    tinytroupe.current_simulation().add_agent(agent)

    # Define a function to be executed transactionally
    def my_function(agent):
        # ... some actions ...
        return agent

    # Execute the function transactionally
    result = tinytroupe.transactional(my_function)(agent)
    print(f"Function result: {result}")

    # End the simulation
    tinytroupe.end(id="my_simulation")