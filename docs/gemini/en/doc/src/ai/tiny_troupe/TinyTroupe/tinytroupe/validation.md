# tinytroupe.validation

## Overview

This module provides a class for validating `TinyPerson` instances using OpenAI's LLM.  The `TinyPersonValidator` class facilitates a conversation-based validation process, prompting the LLM with questions to assess the person's responses and generate a confidence score.

## Classes

### `TinyPersonValidator`

**Description**: This class encapsulates the validation logic for `TinyPerson` instances. It leverages OpenAI's LLM to assess the person's responses and provide a confidence score.

**Methods**

#### `validate_person`

**Description**: Validates a `TinyPerson` instance based on provided expectations and parameters.

**Parameters**:
- `person` (TinyPerson): The `TinyPerson` instance to be validated.
- `expectations` (str, optional): The expectations to use during the validation process. Defaults to `None`.
- `include_agent_spec` (bool, optional): Whether to include the agent specification in the prompt. Defaults to `True`.
- `max_content_length` (int, optional): The maximum length of content displayed in the conversation. Defaults to `default_max_content_display_length`.

**Returns**:
- `float`: The confidence score of the validation process (0.0 to 1.0), or `None` if the validation fails.
- `str`: The justification for the validation score, or `None` if the validation fails.

**Raises**:
- `ValueError`: If the input parameters are invalid.
- `Exception`: For any other unexpected errors during the validation process.


## Functions

### `default_max_content_display_length`

**Description**: Defines the default maximum length of content displayed for the conversation.


## Modules Used

- `os`
- `json`
- `chevron`
- `logging`
- `openai_utils`
- `tinytroupe.agent`
- `tinytroupe.config`
- `tinytroupe.utils`