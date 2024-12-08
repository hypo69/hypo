# testing_utils.py

## Overview

This module provides utility functions for testing the `TinyTroupe` library. It includes functions for checking actions and stimuli, proposition verification, message creation, agent configuration comparison, file manipulation, and fixtures for testing environments.

## Table of Contents

* [Functions](#functions)
* [I/O Utilities](#i-o-utilities)
* [Fixtures](#fixtures)

## Functions

### `contains_action_type`

**Description**: Checks if a list of actions contains an action of a specified type.

**Parameters**:
- `actions` (list): A list of actions.
- `action_type` (str): The type of action to search for.

**Returns**:
- `bool`: `True` if an action of the specified type is found, `False` otherwise.


### `contains_action_content`

**Description**: Checks if a list of actions contains an action with a specific content.

**Parameters**:
- `actions` (list): A list of actions.
- `action_content` (str): The content to search for.

**Returns**:
- `bool`: `True` if an action with the specified content is found, `False` otherwise.


### `contains_stimulus_type`

**Description**: Checks if a list of stimuli contains a stimulus of a specified type.

**Parameters**:
- `stimuli` (list): A list of stimuli.
- `stimulus_type` (str): The type of stimulus to search for.

**Returns**:
- `bool`: `True` if a stimulus of the specified type is found, `False` otherwise.


### `contains_stimulus_content`

**Description**: Checks if a list of stimuli contains a stimulus with a specific content.

**Parameters**:
- `stimuli` (list): A list of stimuli.
- `stimulus_content` (str): The content to search for.

**Returns**:
- `bool`: `True` if a stimulus with the specified content is found, `False` otherwise.


### `terminates_with_action_type`

**Description**: Checks if a list of actions terminates with an action of a specified type.

**Parameters**:
- `actions` (list): A list of actions.
- `action_type` (str): The type of action to check for.

**Returns**:
- `bool`: `True` if the last action is of the specified type, `False` otherwise, or `False` if the list is empty.


### `proposition_holds`

**Description**: Checks if a given proposition is true according to an LLM call.

**Parameters**:
- `proposition` (str): The proposition to check.

**Returns**:
- `bool`: `True` if the proposition is true, `False` otherwise.

**Raises**:
- `Exception`: If the LLM returns an unexpected result.


### `only_alphanumeric`

**Description**: Returns a string containing only alphanumeric characters.

**Parameters**:
- `string` (str): The input string.

**Returns**:
- `str`: The string containing only alphanumeric characters.


### `create_test_system_user_message`

**Description**: Creates a list containing a system message and a user message (or only a system message if user_prompt is None).

**Parameters**:
- `user_prompt` (str, optional): The user prompt. Defaults to `None`.
- `system_prompt` (str, optional): The system prompt. Defaults to `"You are a helpful AI assistant."`.

**Returns**:
- `list`: A list containing the system message and the user message.


### `agents_configs_are_equal`

**Description**: Checks if the configurations of two agents are equal, ignoring the name if specified.

**Parameters**:
- `agent1`: The first agent.
- `agent2`: The second agent.
- `ignore_name` (bool, optional): If True, the agent names are ignored during comparison. Defaults to `False`.

**Returns**:
- `bool`: `True` if the configurations are equal, `False` otherwise.


### `remove_file_if_exists`

**Description**: Removes a file if it exists.

**Parameters**:
- `file_path` (str): The path to the file.


### `get_relative_to_test_path`

**Description**: Returns the path to the test file with the given suffix.

**Parameters**:
- `path_suffix` (str): The suffix to append to the test file path.

**Returns**:
- `str`: The path to the test file.


## I/O Utilities

(These sections are already documented within the function descriptions above)


## Fixtures

### `focus_group_world`

**Description**: Creates a `TinyWorld` fixture with pre-defined agents.

**Returns**:
- `TinyWorld`: The created `TinyWorld` object.


### `setup`

**Description**: Clears agents and environments before each test function.

```