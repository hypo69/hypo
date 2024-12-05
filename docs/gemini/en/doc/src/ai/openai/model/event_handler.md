# hypotez/src/ai/openai/model/event_handler.py

## Overview

This module defines a custom `EventHandler` class for handling events from an OpenAI Assistant API stream.  It extends the `AssistantEventHandler` class and provides custom logic for printing assistant text, tool calls, and tool call deltas, including code interpreter output.

## Classes

### `EventHandler`

**Description**: A custom event handler class to manage and print events from OpenAI Assistant API responses.

**Methods**

#### `on_text_created(text: Text) -> None`

**Description**: Handles the creation of new text in the assistant response.

**Parameters**:

- `text` (Text): The newly created text object from OpenAI Assistant API.

**Returns**:

- `None`:  This method does not return any value. It prints the assistant's response.


#### `on_text_delta(delta: TextDelta, snapshot: Text)`

**Description**: Handles updates to existing text in the assistant response.

**Parameters**:

- `delta` (TextDelta): The update to the text.
- `snapshot` (Text): The current text snapshot.

**Returns**:

- `None`: This method does not return any value. It prints the updated response text.


#### `on_tool_call_created(tool_call: ToolCall)`

**Description**: Handles the creation of tool calls in the assistant response.

**Parameters**:

- `tool_call` (ToolCall): The tool call object from OpenAI Assistant API.

**Returns**:

- `None`: This method does not return any value. It prints the tool call type.


#### `on_tool_call_delta(delta: ToolCallDelta, snapshot: ToolCall)`

**Description**: Handles updates to tool calls in the assistant response.

**Parameters**:

- `delta` (ToolCallDelta): The update to the tool call.
- `snapshot` (ToolCall): The current tool call snapshot.

**Returns**:

- `None`: This method does not return any value. It prints the input and outputs of code interpreter tool calls.


## Global Variables

### `MODE`

**Description**: A string defining the current operating mode (e.g., 'dev', 'prod').