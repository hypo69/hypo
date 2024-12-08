# tinytroupe.utils

## Overview

This module provides general utilities, convenience functions, and tools for input/output, prompt engineering, validation, and other tasks related to the TinyTroupe system.  It includes functions for composing LLM messages, extracting JSON and code blocks from text, handling errors with retries, validating data, sanitizing strings and dictionaries, adding RAI templates, rendering HTML, breaking text at length, formatting datetimes, and generating unique IDs.  Importantly, it introduces the `JsonSerializableRegistry` class, a mixin that facilitates JSON serialization and deserialization of objects and their subclasses, managing included/excluded attributes and potential post-deserialization actions.


## Classes

### `JsonSerializableRegistry`

**Description**: A mixin class that provides JSON serialization, deserialization, and subclass registration for custom classes. This class allows for more controlled serialization of complex objects containing potentially nested data and other custom classes.


**Methods**

- `to_json(include: list = None, suppress: list = None, file_path: str = None) -> dict`:
    **Description**: Returns a JSON representation of the object.
    **Parameters**:
        - `include` (list, optional): Attributes to include in the serialization.
        - `suppress` (list, optional): Attributes to suppress from the serialization.
        - `file_path` (str, optional): Path to a file where the JSON will be written.
    **Returns**:
        - `dict`: A dictionary representation of the object in JSON format.


- `from_json(json_dict_or_path, suppress: list = None, post_init_params: dict = None)`:
    **Description**: Loads a JSON representation of the object and creates an instance of the class.
    **Parameters**:
        - `json_dict_or_path` (dict or str): The JSON dictionary representing the object or a file path to load the JSON from.
        - `suppress` (list, optional): Attributes to suppress from being loaded.
        - `post_init_params` (dict, optional): Parameters to pass to the `_post_deserialization_init` method.
    **Returns**:
        - An instance of the class populated with the data from json_dict_or_path.


## Functions

### `compose_initial_LLM_messages_with_templates`

**Description**: Composes the initial messages for the LLM model call, using templates for system and user messages.

**Parameters**:
    - `system_template_name` (str): Name of the template file for the system message.
    - `user_template_name` (str, optional): Name of the template file for the user message. Defaults to `None`.
    - `rendering_configs` (dict, optional): Configuration variables for rendering the templates. Defaults to an empty dictionary.


**Returns**:
    - list: A list of dictionaries representing the initial messages for the LLM. Each dictionary has a "role" (system or user) and "content" (rendered template).


### `extract_json`

**Description**: Extracts a JSON object from a string, handling various cases including regex to remove leading/trailing text.

**Parameters**:
    - `text` (str): The input string containing the JSON object.


**Returns**:
    - dict: The extracted JSON object as a Python dictionary. Returns an empty dictionary if extraction fails.


### `extract_code_block`

**Description**: Extracts a code block from a string, using regex to handle potential extra characters and ensure it returns a valid code block.

**Parameters**:
    - `text` (str): The input string containing the code block.


**Returns**:
    - str: The extracted code block. Returns an empty string if extraction fails.



### `repeat_on_error`

**Description**: A decorator that repeats a function call a certain number of times if specific exceptions occur.

**Parameters**:
    - `retries` (int): The number of times to retry the function.
    - `exceptions` (list): A list of exception types to catch.


**Returns**:
    - A decorator function that can be applied to other functions.

**Example Usage**:

```python
@repeat_on_error(retries=3, exceptions=[SomeException])
def my_function():
  # ... function body ...
```

### `check_valid_fields`

**Description**: Validates that a dictionary contains only expected keys.

**Parameters**:
    - `obj` (dict): The dictionary to validate.
    - `valid_fields` (list): A list of valid keys.

**Raises**:
    - `ValueError`: If an invalid key is found in the dictionary.


### `sanitize_raw_string`

**Description**: Sanitizes a string by removing invalid characters and ensuring it does not exceed the maximum Python string length.

**Parameters**:
    - `value` (str): The string to sanitize.


**Returns**:
    - str: The sanitized string.


### `sanitize_dict`

**Description**: Sanitizes a dictionary by removing invalid characters and ensuring it does not exceed the maximum allowed depth.

**Parameters**:
    - `value` (dict): The dictionary to sanitize.


**Returns**:
    - dict: The sanitized dictionary.

### `add_rai_template_variables_if_enabled`

**Description**: Adds RAI template variables to a dictionary based on configuration settings.

**Parameters**:
    - `template_variables` (dict): The dictionary to add variables to.

**Returns**:
    - dict: The updated dictionary.

### `inject_html_css_style_prefix`

**Description**: Injects a style prefix into all style attributes in an HTML string.

**Parameters**:
    - `html` (str): The HTML string to modify.
    - `style_prefix_attributes` (str): The style prefix to inject.


**Returns**:
    - str: The modified HTML string.


### `break_text_at_length`

**Description**: Breaks a string or JSON object at a specified maximum length.

**Parameters**:
    - `text` (Union[str, dict]): The text or JSON object to break.
    - `max_length` (int, optional): The maximum length for the text. Defaults to `None`.

**Returns**:
    - str: The text or JSON object, potentially broken at the maximum length with a "(...)".


### `pretty_datetime`

**Description**: Formats a `datetime` object into a user-friendly string.

**Parameters**:
    - `dt` (datetime): The `datetime` object to format.

**Returns**:
    - str: A formatted string representation of the datetime.

### `dedent`

**Description**: Removes leading whitespace and indentation from a string.


**Parameters**:
    - `text` (str): The string to dedent.


**Returns**:
    - str: The dedented string.



### `read_config_file`

**Description**: Reads the TinyTroupe configuration file (config.ini), handling both default and custom configuration files in multiple locations.

**Parameters**:
    - `use_cache` (bool): Use a cached config. Defaults to True.
    - `verbose` (bool): Print verbose messages. Defaults to True.

**Returns**:
    - configparser.ConfigParser: The parsed configuration object.


### `pretty_print_config`

**Description**: Prints the TinyTroupe configuration in a formatted manner.

**Parameters**:
    - `config` (configparser.ConfigParser): The configuration to print.

**Returns**:
    - None

### `start_logger`

**Description**: Starts and configures the logger with specific log level based on the config.

**Parameters**:
    - `config` (configparser.ConfigParser): The configuration to determine the log level.

**Returns**:
    - None

### `name_or_empty`

**Description**: Returns the name of an agent or environment, or an empty string if it's None.

**Parameters**:
    - `named_entity` (AgentOrWorld): The agent or environment to get the name from.

**Returns**:
    - str: The name of the entity, or an empty string.

### `custom_hash`

**Description**: Returns a deterministic hash of an object.

**Parameters**:
    - `obj`: The object to hash.

**Returns**:
    - str: The hexadecimal representation of the SHA256 hash.


### `fresh_id`

**Description**: Generates a unique incrementing ID.

**Returns**:
    - int: The next available unique ID.