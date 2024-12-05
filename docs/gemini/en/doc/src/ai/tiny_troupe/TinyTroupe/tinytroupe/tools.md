# tinytroupe.tools

## Overview

This module defines tools for agents to perform specialized tasks. It includes classes for creating and managing tools with various functionalities, including exporting and enriching results.

## Classes

### `TinyTool`

**Description**: The base class for all tools. It handles common tool attributes and methods, including name, description, owner, and whether it has real-world side effects.

**Attributes**:
- `name` (str): The name of the tool.
- `description` (str): A brief description of the tool.
- `owner` (str): The agent that owns the tool. `None` if the tool can be used by anyone.
- `real_world_side_effects` (bool): Whether the tool has real-world side effects.
- `exporter` (ArtifactExporter): An exporter for the tool's results.
- `enricher` (Enricher): An enricher for the tool's results.

**Methods**:
- `__init__(name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None)`: Initializes a new tool.
    - **Args**:
        - `name` (str): The name of the tool.
        - `description` (str): A brief description of the tool.
        - `owner` (str, optional): The agent that owns the tool. Defaults to `None`.
        - `real_world_side_effects` (bool, optional): Whether the tool has real-world side effects. Defaults to `False`.
        - `exporter` (ArtifactExporter, optional): An exporter that can be used to export the results of the tool's actions. Defaults to `None`.
        - `enricher` (Enricher, optional): An enricher that can be used to enrich the results of the tool's actions. Defaults to `None`.
    - **Returns**: None

- `_process_action(agent, action: dict) -> bool`: Processes a given action.  Subclasses must implement this method.
    - **Args**:
        - `agent`: The agent performing the action.
        - `action` (dict): The action to process.
    - **Returns**: `bool`: True if the action was processed successfully.
    - **Raises**: `NotImplementedError`: If not implemented in the subclass.

- `_protect_real_world()`: Logs a warning if the tool has real-world side effects.
- `_enforce_ownership(agent)`: Raises `ValueError` if the agent doesn't own the tool.
- `set_owner(owner)`: Sets the owner of the tool.
- `actions_definitions_prompt() -> str`: Generates a prompt defining possible actions.  Subclasses must implement this method.
    - **Returns**: str: The prompt string.
    - **Raises**: `NotImplementedError`: If not implemented in the subclass.
- `actions_constraints_prompt() -> str`: Generates a prompt with constraints on actions. Subclasses must implement this method.
    - **Returns**: str: The prompt string.
    - **Raises**: `NotImplementedError`: If not implemented in the subclass.
- `process_action(agent, action: dict) -> bool`: Processes an action after checking for real-world side effects and ownership.
   - **Args**:
     - `agent`: The agent taking the action.
     - `action` (dict): The action to perform.
   - **Returns**: `bool`: True if the action was successfully processed.

### `TinyCalendar`

**Description**: A tool for managing appointments and meetings.

**Attributes**:
- `calendar` (dict): A dictionary mapping dates to lists of events.


**Methods**:
- `__init__(owner=None)`: Initializes a calendar tool.
- `add_event(date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None)`: Adds an event to the calendar.
- `find_events(year, month, day, hour=None, minute=None)`: Finds events on a given date and time (Not implemented).
- `_process_action(agent, action) -> bool`: Processes actions for creating events.
- `actions_definitions_prompt() -> str`: Returns a prompt for creating events.
- `actions_constraints_prompt() -> str`: Returns a prompt for action constraints (currently empty).


### `TinyWordProcessor`

**Description**: A tool for writing documents.

**Attributes**:

**Methods**:
- `__init__(owner=None, exporter=None, enricher=None)`: Initializes a word processor tool.
- `write_document(title, content, author=None)`: Writes a document, optionally enriching and exporting it.
- `_process_action(agent, action) -> bool`: Processes actions for writing documents.
- `actions_definitions_prompt() -> str`: Returns a prompt for writing documents.
- `actions_constraints_prompt() -> str`: Returns a prompt with constraints on writing documents.

## Functions


```
```