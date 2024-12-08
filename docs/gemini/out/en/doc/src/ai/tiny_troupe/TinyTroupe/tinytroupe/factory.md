# tinytroupe.factory

## Overview

This module defines the `TinyFactory` base class and the `TinyPersonFactory` class, which are used to create and manage instances of artificial agents (e.g., TinyPerson).  It includes mechanisms for caching factories and generating agents using OpenAI's LLM, along with handling potential errors and managing the simulation context.


## Classes

### `TinyFactory`

**Description**: A base class for various types of factories. This design is crucial for extending the system and managing transactional caching.

**Attributes**:

- `all_factories`: A dictionary to store all created factory instances (name -> factory).
- `name`: A unique identifier for the factory.
- `simulation_id`: The ID of the simulation the factory belongs to.

**Methods**:

#### `__init__(self, simulation_id: str = None) -> None`

**Description**: Initializes a `TinyFactory` instance.

**Parameters**:
- `simulation_id` (str, optional): The ID of the simulation. Defaults to `None`.

**Raises**:
- `ValueError`: If a factory with the same name already exists.

#### `__repr__(self) -> str`

**Description**: Returns a string representation of the `TinyFactory` instance.

#### `set_simulation_for_free_factories(simulation)`

**Description**: Sets the simulation for free factories (those without an assigned `simulation_id`).

#### `add_factory(factory)`

**Description**: Adds a factory to the global list of factories.

**Parameters**:
- `factory`: The `TinyFactory` instance to add.

**Raises**:
- `ValueError`: If a factory with the same name already exists.

#### `clear_factories()`

**Description**: Clears the global list of all factory instances.

#### `encode_complete_state(self) -> dict`

**Description**: Encodes the complete state of the factory.

**Returns**:
- `dict`: The encoded state of the factory.  Subclasses should override to include any non-serializable attributes.


#### `decode_complete_state(self, state: dict) -> TinyFactory`

**Description**: Decodes the complete state of the factory.

**Parameters**:
- `state` (dict): The encoded state of the factory.

**Returns**:
- `TinyFactory`: The decoded factory instance. Subclasses should override to handle non-serializable attributes.


### `TinyPersonFactory`

**Description**: A factory specifically for creating `TinyPerson` instances. It uses a template and context to generate agent specifications.

**Attributes**:
- `person_prompt_template_path`: The path to the mustache template for generating agent prompts.
- `context_text`: The context text used for generating `TinyPerson` instances.
- `generated_minibios`: A list of `minibios` to avoid generating the same person twice.
- `generated_names`: A list to check for name uniqueness.

**Methods**:

#### `__init__(self, context_text, simulation_id: str = None) -> None`

**Description**: Initializes a `TinyPersonFactory` instance.

**Parameters**:
- `context_text` (str): The context text to use in generating TinyPerson agents.
- `simulation_id` (str, optional): The ID of the simulation. Defaults to `None`.

#### `generate_person_factories(number_of_factories, generic_context_text) -> list | None`

**Description**: Generates a list of `TinyPersonFactory` instances using OpenAI's LLM.

**Parameters**:
- `number_of_factories` (int): The number of factories to generate.
- `generic_context_text` (str): The context to use in generating agent prompts.

**Returns**:
- `list`: A list of `TinyPersonFactory` instances. Returns `None` if no suitable agents are generated.


#### `generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5) -> TinyPerson | None`

**Description**: Generates a `TinyPerson` instance using OpenAI's LLM.

**Parameters**:
- `agent_particularities` (str, optional): Particularities to include in the agent generation. Defaults to None.
- `temperature` (float, optional): The sampling temperature for the LLM. Defaults to 1.5.
- `attepmpts` (int, optional): The maximum number of attempts to generate the agent. Defaults to 5.

**Returns**:
- `TinyPerson`: The generated `TinyPerson` instance, or `None` if generation fails.

**Raises**:
- `Exception`: Any exception raised during the agent generation process.


#### `_aux_model_call(self, messages, temperature)`

**Description**: Auxiliary method for making model calls. This allows transactional decorators to function correctly.


#### `_setup_agent(self, agent, configuration)`

**Description**: Sets up the `agent` with elements from the `configuration`.  

## Functions


```