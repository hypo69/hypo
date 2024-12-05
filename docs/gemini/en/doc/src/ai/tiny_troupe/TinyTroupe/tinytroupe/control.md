# tinytroupe.control

## Overview

This module provides the core control mechanisms for simulations, including initialization, management of simulation entities (agents, environments, and factories), checkpointing, and transactional execution of operations. It leverages caching to optimize repeated operations and maintain consistency across simulation steps.


## Classes

### `Simulation`

**Description**: The `Simulation` class encapsulates the entire simulation control logic. It manages the lifecycle of agents, environments, factories, and simulation state.

**Attributes**:

- `id`: A unique identifier for the simulation. Defaults to "default".
- `agents`: A list of agents within the simulation.
- `name_to_agent`: A dictionary mapping agent names to their corresponding agent objects.
- `environments`: A list of environments within the simulation.
- `factories`: A list of factories within the simulation.
- `name_to_factory`: A dictionary mapping factory names to their corresponding factory objects.
- `name_to_environment`: A dictionary mapping environment names to their corresponding environment objects.
- `status`: Current status of the simulation ("stopped" or "started").
- `cache_path`: The path to the cache file. Defaults to `./tinytroupe-cache-{id}.json`.
- `auto_checkpoint`: A boolean indicating whether to automatically checkpoint at the end of each transaction. Defaults to False.
- `has_unsaved_cache_changes`: A boolean indicating if there are changes to the cache that haven't been saved.
- `_under_transaction`: A boolean indicating if the simulation is currently under a transaction.
- `cached_trace`: A list storing simulation states, each represented as a tuple (previous_node_hash, event_hash, event_output, state).
- `execution_trace`: A list storing the current execution trace (similar to `cached_trace`, but for the current execution).

**Methods**:

#### `__init__(self, id="default", cached_trace:list=None)`

**Description**: Initializes a `Simulation` object.

**Parameters**:
- `id` (str, optional): A unique identifier for the simulation. Defaults to "default".
- `cached_trace` (list, optional): A list of simulation states to initialize with. Defaults to `None` (creating an empty trace).

#### `begin(self, cache_path:str=None, auto_checkpoint:bool=False)`

**Description**: Starts the simulation.

**Parameters**:
- `cache_path` (str, optional): The path to the cache file. Defaults to the default cache path.
- `auto_checkpoint` (bool, optional): Whether to automatically checkpoint at the end of each transaction. Defaults to False.

**Raises**:
- `ValueError`: If the simulation is already started.


#### `end(self)`

**Description**: Ends the simulation.

**Raises**:
- `ValueError`: If the simulation is already stopped.


#### `checkpoint(self)`

**Description**: Saves the current simulation trace to a file.


#### `add_agent(self, agent)`

**Description**: Adds an agent to the simulation.

**Parameters**:
- `agent`: The agent object to add.

**Raises**:
- `ValueError`: If an agent with the same name already exists.


#### `add_environment(self, environment)`

**Description**: Adds an environment to the simulation.

**Parameters**:
- `environment`: The environment object to add.

**Raises**:
- `ValueError`: If an environment with the same name already exists.


#### `add_factory(self, factory)`

**Description**: Adds a factory to the simulation.

**Parameters**:
- `factory`: The factory object to add.

**Raises**:
- `ValueError`: If a factory with the same name already exists.


#### `_execution_trace_position(self) -> int`

**Description**: Returns the current position in the execution trace, or -1 if the execution trace is empty.


#### `_function_call_hash(self, function_name, *args, **kwargs) -> int`

**Description**: Computes the hash of the given function call.


#### `_skip_execution_with_cache(self)`

**Description**: Skips the current execution, assuming a cached state exists.

**Raises**:
- `AssertionError`: If there's no cached state at the current execution position.



#### `_is_transaction_event_cached(self, event_hash) -> bool`

**Description**: Checks if the given event hash matches a cached one.


#### `_drop_cached_trace_suffix(self)`

**Description**: Drops the cached trace suffix starting at the current execution trace position.


#### `_add_to_execution_trace(self, state: dict, event_hash: int, event_output)`

**Description**: Adds a state to the execution trace.


#### `_add_to_cache_trace(self, state: dict, event_hash: int, event_output)`

**Description**: Adds a state to the cached trace.


#### `_load_cache_file(self, cache_path:str)`

**Description**: Loads the cache file from the given path.


#### `_save_cache_file(self, cache_path:str)`

**Description**: Saves the cache file to the given path.


#### `begin_transaction(self)`

**Description**: Starts a transaction.


#### `end_transaction(self)`

**Description**: Ends a transaction.


#### `is_under_transaction(self)`

**Description**: Checks if the simulation is under a transaction.


#### `_clear_communications_buffers(self)`

**Description**: Clears the communications buffers of all agents and environments.


#### `_encode_simulation_state(self) -> dict`

**Description**: Encodes the current simulation state.


#### `_decode_simulation_state(self, state: dict)`

**Description**: Decodes the given simulation state.

### `Transaction`

**Description**:  Manages transactional execution of functions within a simulation.

### `transactional(func)`

**Description**: A decorator that makes a function transactional within a simulation context.


### `SkipTransaction`, `CacheOutOfSync`, `ExecutionCached`

**Description**: Custom exception classes for handling specific scenarios.


## Functions

### `reset()`

**Description**: Resets the entire simulation control state.  Initializes the `_current_simulations` global.


### `_simulation(id="default")`

**Description**: Returns a `Simulation` instance for the given ID. Creates a new simulation if one doesn't exist.


### `begin(cache_path=None, id="default", auto_checkpoint=False)`

**Description**: Starts a simulation.

**Parameters**:
- `cache_path` (str, optional): Path to the cache file.
- `id` (str, optional): Simulation identifier. Defaults to "default".
- `auto_checkpoint` (bool, optional): Whether to automatically checkpoint. Defaults to False.

**Raises**:
- `ValueError`: If a simulation is already running.


### `end(id="default")`

**Description**: Ends the current simulation.


### `checkpoint(id="default")`

**Description**: Saves the current simulation state.


### `current_simulation()`

**Description**: Returns the currently active simulation, or `None` if no simulation is running.