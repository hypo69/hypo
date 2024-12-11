# Code Explanation: tinytroupe/utils.py

## <input code>

```python
"""
General utilities and convenience functions.
"""
import re
import json
import os
import sys
import hashlib
import textwrap
import logging
import chevron
import copy
from typing import Collection
from datetime import datetime
from pathlib import Path
import configparser
from typing import Any, TypeVar, Union
AgentOrWorld = Union["TinyPerson", "TinyWorld"]

# logger
logger = logging.getLogger("tinytroupe")


################################################################################
# Model input utilities
################################################################################


def compose_initial_LLM_messages_with_templates(system_template_name:str, user_template_name:str=None, rendering_configs:dict={}) -> list:
    """
    Composes the initial messages for the LLM model call, under the assumption that it always involves 
    a system (overall task description) and an optional user message (specific task description). 
    These messages are composed using the specified templates and rendering configurations.
    """

    # ... (rest of the function)
```

## <algorithm>

**Function: `compose_initial_LLM_messages_with_templates`**

1. **Input:** `system_template_name`, `user_template_name` (optional), `rendering_configs`
2. **Construct paths:** Construct paths for system and user prompt templates using `os.path.join`.
3. **Initialize list:** Create an empty list `messages`.
4. **Render system message:** Read the system prompt template, render it using `chevron`, and append it as a dictionary to the `messages` list.
5. **Render user message (optional):** If `user_template_name` is provided, read the user prompt template, render it using `chevron`, and append it to `messages`.
6. **Return messages:** Return the `messages` list.

**Example:**

```
system_template_name = "task_description.txt"
rendering_configs = {"task": "summarize the article"}

messages = compose_initial_LLM_messages_with_templates(system_template_name, rendering_configs=rendering_configs)
```


## <mermaid>

```mermaid
graph LR
    A[utils.py] --> B{compose_initial_LLM_messages_with_templates};
    B --> C[os.path.join];
    C --> D(system_prompt_template_path);
    D --> E(open(system_prompt_template_path));
    E --> F(chevron.render);
    F --> G[{"role": "system", "content": ...}];
    G --> H[messages.append];
    H --> I[messages];
    subgraph User Prompt (optional)
        B --> J(user_prompt_template_path);
        J --> K(open(user_prompt_template_path));
        K --> F;
        F --> L[{"role": "user", "content": ...}];
        L --> H;
    end
    H --> M[Return messages];
```

**Dependencies:**

- `re`, `json`, `os`, `sys`, `hashlib`, `textwrap`, `logging`, `chevron`, `copy`, `typing`, `datetime`, `pathlib`, `configparser`: Standard Python libraries used for various functionalities like regular expressions, JSON handling, file I/O, logging, template rendering, copying objects, type hinting, date handling, and path operations, and config files.
- `Union`, `Any`, `TypeVar`: Typing tools for type hinting, used for enhancing code readability and maintainability.
- `AgentOrWorld`: Custom type alias, defining a union of `TinyPerson` and `TinyWorld` types (likely custom types not shown in the code snippet but from the same package, suggesting these types are defined elsewhere in the `tinytroupe` package).


## <explanation>

**Imports:** The code imports various standard Python libraries, including those for regular expressions (`re`), JSON handling (`json`), operating system interactions (`os`), system-related functions (`sys`), hashing (`hashlib`), text manipulation (`textwrap`), logging (`logging`), templating (`chevron`), copying data (`copy`), type hinting (`typing`), date and time operations (`datetime`), path operations (`pathlib`), configuration parsing (`configparser`), and more.  The usage of these imports is straightforward and aligned with their conventional roles in Python programming.


**Classes:** The code defines a single class `JsonSerializableRegistry` with methods for serialization (`to_json`) and deserialization (`from_json`) and a class method `__init_subclass__`. This class is designed to be a mixin that provides functionality for serializing and deserializing objects to and from JSON format. It supports handling various data types like dictionaries, lists, and other instances of `JsonSerializableRegistry`. A `post_init` decorator enforces a call to a class's `_post_init` method, if it exists.

**Functions:**

- **`compose_initial_LLM_messages_with_templates`**: Creates LLM messages using templates. It takes template names, optional user template, and rendering configurations. It renders the templates using the `chevron` library and returns the rendered messages.
- **`extract_json`**: Extracts a JSON object from a string, handling various edge cases such as different delimiters and escaping problems.
- **`extract_code_block`**: Extracts a code block from a string, using regex to remove surrounding text.
- **`repeat_on_error`**: A decorator that allows a function to be retried a specified number of times if an exception from a specified list of exceptions is raised.  Critically important for handling potential network or API timeouts, data retrieval issues, etc.
- **`check_valid_fields`**: Validates a dictionary's keys against a predefined list.
- **`sanitize_raw_string`**: Sanitizes a string by removing invalid characters and ensuring it doesn't exceed the maximum Python string length. Important for security.
- **`sanitize_dict`**: Sanitizes a dictionary, similar to `sanitize_raw_string` but using `json.dumps` and `json.loads` to handle potential problems with embedded dictionaries and nested data structures.
- **`add_rai_template_variables_if_enabled`**: Loads RAI (Responsible AI) template variables based on configuration settings.
- **`inject_html_css_style_prefix`**: Injects a CSS style prefix to HTML style attributes.
- **`break_text_at_length`**: Breaks a string (or JSON) if it exceeds a maximum length.
- **`pretty_datetime`**: Returns a formatted string representation of a datetime object.
- **`dedent`**: Removes leading whitespace from a multiline string.
- **`read_config_file`**: Reads a configuration file (`config.ini`). It prioritizes config.ini in the same directory as the script and if it is not present, tries current directory.
- **`pretty_print_config`**: Prints a nicely formatted representation of the config.
- **`start_logger`**: Initializes the logger, setting the level according to the configuration.

**Variables:**
- `logger`: A logger instance for logging messages.
- `_config`: A cached instance of the configuration parser. This caches the config for performance and prevents re-reading the config every time.
- `AgentOrWorld`: A type alias to clarify expected types (TinyPerson, TinyWorld).


**Potential Errors/Improvements:**

- **Circular imports:** The `add_rai_template_variables_if_enabled` function imports `config` from `tinytroupe`.  A more robust solution would be to inject the `config` object instead of importing the entire module. This would avoid issues in case of cyclical dependencies.
- **Error handling in `extract_json` and `extract_code_block`:**  While the functions handle exceptions, consider adding more descriptive error messages to help with debugging.
- **`read_config_file`:** Error handling and logging are present but could be strengthened.  Consider raising a more specific exception type (e.g., `ConfigFileNotFoundError`).
- **`JsonSerializableRegistry` subclass regiStartion:**  The `__init_subclass__` method is a good way to register subclasses. However, consider validating the inputs to `serializable_attributes` to ensure they're lists or similar.


**Relationships:** This module likely interacts with other modules in the `tinytroupe` package, especially those that use LLM model calls, input/output utilities, and those where configuration is used in some fashion.  For example, `compose_initial_LLM_messages_with_templates` is likely used by other parts of the project that handle model interactions.  The `JsonSerializableRegistry` is used for serialization and deserialization of objects, likely objects within the `tinytroupe` package.


```