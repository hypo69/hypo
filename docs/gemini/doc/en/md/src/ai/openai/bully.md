# bully.py

## Overview

This module provides a function to interact with the OpenAI API to generate examples of bullying behavior from a bully's perspective. It utilizes a system prompt to guide the AI model to produce a structured JSON response containing the example.

## Functions

### `bully`

**Description**: This function interacts with the OpenAI API to generate examples of bullying behavior.

**Parameters**:
- `user_message` (str): The initial message or statement to provide to the AI model. Defaults to "Hello!".
- `messages` (list, optional): A list of messages to be used in the conversation with the model.  Defaults to a list containing the system prompt.

**Returns**:
- `messages` (list): A list of messages exchanged in the conversation, including the generated bully response.

**Raises**:
- `Exception`: An exception might be raised if the OpenAI API call fails or returns an unexpected response.