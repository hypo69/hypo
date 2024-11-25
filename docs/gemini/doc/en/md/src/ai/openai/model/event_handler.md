# hypotez/src/ai/openai/model/event_handler.py

## Overview

This module defines an `EventHandler` class that handles events generated during a conversation with an OpenAI Assistant.  It provides a custom way to process text and tool call events, printing them to the console for visualization and potential further processing.

## Classes

### `EventHandler`

**Description**: This class extends `AssistantEventHandler` to customize how events are handled during a conversation with an OpenAI Assistant.  It specifically provides a way to print text deltas and tool calls, and for code interpreter tool calls, it prints the tool call input and any resulting logs.

**Methods**

#### `on_text_created(self, text: Text) -> None`

**Description**: Called when a new text message is created by the assistant.

**Parameters**:
- `text` (Text): The new text message.

**Returns**:
- `None`:  No return value.


#### `on_text_delta(self, delta: TextDelta, snapshot: Text)`

**Description**: Called when an update to an existing text message occurs.

**Parameters**:
- `delta` (TextDelta): The update to the text message.
- `snapshot` (Text): The current state of the text message.


**Returns**:
- `None`:  No return value.

#### `on_tool_call_created(self, tool_call: ToolCall)`

**Description**: Called when a new tool call is created by the assistant.

**Parameters**:
- `tool_call` (ToolCall): The newly created tool call.

**Returns**:
- `None`:  No return value.

#### `on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)`

**Description**: Called when an update to an existing tool call occurs.

**Parameters**:
- `delta` (ToolCallDelta): The update to the tool call.
- `snapshot` (ToolCall): The current state of the tool call.


**Returns**:
- `None`: No return value.


## Constants

### `MODE`

**Description**: A string representing the current mode (e.g., 'dev').


```