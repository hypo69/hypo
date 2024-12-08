# tinytroupe.experimentation

## Overview

This module provides classes for experimental randomization and intervention management.  It includes tools for randomizing choices and for implementing interventions on agents and environments.


## Classes

### `ABRandomizer`

**Description**: A utility class for randomizing and de-randomizing choices between two options.  It maintains a mapping of item indices to their randomization states.

**Methods**

#### `__init__`

**Description**: Initializes an `ABRandomizer` instance.

**Parameters**:

- `real_name_1` (str): The name of the first option (e.g., "control").
- `real_name_2` (str): The name of the second option (e.g., "treatment").
- `blind_name_a` (str): The name of the first option as presented to the user.
- `blind_name_b` (str): The name of the second option as presented to the user.
- `passtrough_name` (list): A list of names that are not randomized.
- `random_seed` (int): The random seed used for randomization.


#### `randomize`

**Description**: Randomizes the order of choices for a given item index.

**Parameters**:

- `i` (int): The index of the item to randomize.
- `a` (str): The first choice option.
- `b` (str): The second choice option.

**Returns**:

- `tuple`: A tuple containing the randomized order of choices (a, b).


#### `derandomize`

**Description**: De-randomizes the choices for a given item index to their original order.

**Parameters**:

- `i` (int): The index of the item to de-randomize.
- `a` (str): The first choice option.
- `b` (str): The second choice option.

**Returns**:

- `tuple`: A tuple containing the original order of choices (a, b).

**Raises**:
- `Exception`: If no randomization is found for the specified item.


#### `derandomize_name`

**Description**: Decodes the randomized choice based on user input.

**Parameters**:

- `i` (int): The index of the item.
- `blind_name` (str): The choice made by the user.


**Returns**:

- `str`: The corresponding real name of the chosen option.


**Raises**:
- `Exception`: If the user's choice is not recognized.

### `Intervention`

**Description**: A base class for implementing interventions on agents or environments.

**Methods**

#### `__init__`

**Description**: Initializes the intervention object.

**Parameters**:

- `agent` (TinyPerson, optional): The agent to intervene on.  Either `agent` or `agents` must be provided, but not both.
- `agents` (list, optional): A list of agents to intervene on.  Either `agent` or `agents` must be provided, but not both.
- `environment` (TinyWorld, optional): The environment to intervene on.
- `environments` (list, optional): A list of environments to intervene on. Either `environment` or `environments` must be provided, but not both.


**Raises**:

- `Exception`: If both `agent` and `agents` or both `environment` and `environments` are provided.
- `Exception`: If no agent or environment is specified.


#### `check_precondition`

**Description**: Checks if the precondition for the intervention is met.


**Raises**:
- `NotImplementedError`: This method is not yet implemented.

#### `apply`

**Description**: Applies the intervention.


**Raises**:
- `NotImplementedError`: This method is not yet implemented.

#### `set_textual_precondition`

**Description**: Sets the precondition for the intervention as a textual description.

**Parameters**:

- `text` (str): The precondition description.

#### `set_functional_precondition`

**Description**: Sets the precondition for the intervention as a function.

**Parameters**:

- `func` (function): The precondition function that takes `agent`, `agents`, `environment`, `environments` as arguments.

#### `set_effect`

**Description**: Sets the effect function for the intervention.

**Parameters**:

- `effect_func` (function): The effect function.


## Functions

(No functions are defined in this module.)