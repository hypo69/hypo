# TinyTroupe Story Module

This module provides helper functions for creating stories in the TinyTroupe simulation framework.  It allows users to generate stories based on the interactions within an environment or an agent.

## Table of Contents

- [TinyStory](#tinystory)
    - [__init__](#init)
    - [start_story](#startstory)
    - [continue_story](#continuestory)
    - [_current_story](#_currentstory)

## Classes

### `TinyStory`

**Description**: This class manages the generation of stories related to simulations, based on provided environments or agents.  It handles the initial story setup, continuation, and incorporating simulation interactions.


#### `__init__`

**Description**: Initializes a `TinyStory` object.  It requires either an environment or an agent, but not both. The purpose of the story, the current context, and other parameters are also set.


**Parameters**:

- `environment` (TinyWorld, optional): The environment in which the story takes place. Defaults to None.
- `agent` (TinyPerson, optional): The agent in the story. Defaults to None.
- `purpose` (str, optional): The purpose of the story. Defaults to "Be a realistic simulation.".
- `context` (str, optional): The current story context. Defaults to "". The actual story will be appended to this context.
- `first_n` (int, optional): The number of first interactions to include in the story. Defaults to 10.
- `last_n` (int, optional): The number of last interactions to include in the story. Defaults to 20.
- `include_omission_info` (bool, optional): Whether to include information about omitted interactions. Defaults to True.

**Raises**:

- `Exception`: If neither `environment` nor `agent` is provided, or if both are provided.


#### `start_story`

**Description**: Starts a new story based on provided requirements.  It composes prompts and sends them to an LLM (Large Language Model) to generate the initial story content.


**Parameters**:

- `requirements` (str, optional): Specific instructions for the story's beginning. Defaults to "Start some interesting story about the agents.".
- `number_of_words` (int, optional): The desired length of the generated story in words. Defaults to 100.
- `include_plot_twist` (bool, optional): Whether to include a plot twist in the story. Defaults to False.


**Returns**:

- `str`: The generated initial story content.


#### `continue_story`

**Description**: Continues the existing story by generating additional text.  It leverages an LLM to create the continuation.


**Parameters**:

- `requirements` (str, optional): Instructions for continuing the story. Defaults to "Continue the story in an interesting way.".
- `number_of_words` (int, optional): The desired length of the generated continuation in words. Defaults to 100.
- `include_plot_twist` (bool, optional): Whether to include a plot twist in the continuation. Defaults to False.


**Returns**:

- `str`: The generated story continuation.


#### `_current_story`

**Description**: Constructs and returns the current story, including information about the simulation interactions (from the environment or agent, if provided).


**Parameters**:

- None

**Returns**:

- `str`: The current story text.