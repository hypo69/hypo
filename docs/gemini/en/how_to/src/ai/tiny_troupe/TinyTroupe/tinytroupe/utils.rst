rst
How to use the tinytroupe.utils module
========================================================================================

Description
-------------------------
This module provides general utilities and convenience functions for the TinyTroupe project.  It includes functions for composing LLM messages, extracting JSON and code blocks from strings, handling errors with retries, validating dictionary fields, sanitizing strings and dictionaries, managing prompt templates, injecting styles into HTML, breaking text at a length, formatting dates, dedenting strings, reading and managing configurations, starting a logger, and providing a mixin class for JSON serialization and deserialization.

Execution steps
-------------------------
1. **Import the module:** Import the `tinytroupe.utils` module into your script.

2. **Compose LLM messages:** Use `compose_initial_LLM_messages_with_templates` to create initial messages for an LLM call.  This function takes a system template name (path relative to the prompts directory), an optional user template name, and rendering configurations (dictionary).

3. **Extract JSON:** Use `extract_json` to extract a JSON object from a string.  This function handles various edge cases, including text before the JSON, markdown code blocks, and invalid escape sequences.

4. **Extract code block:** Use `extract_code_block` to extract a code block from a string, handling cases with leading/trailing backticks.

5. **Handle errors with retries:** Use the `repeat_on_error` decorator to wrap functions that might throw exceptions. This decorator allows you to repeat the function call a specified number of times if a particular exception is encountered.

6. **Validate dictionary fields:** Use `check_valid_fields` to validate that a dictionary contains only expected keys.

7. **Sanitize strings:** Use `sanitize_raw_string` to sanitize strings, removing invalid characters and ensuring they don't exceed the maximum Python string length.

8. **Sanitize dictionaries:** Use `sanitize_dict` to sanitize dictionaries, ensuring that they are valid JSON and not excessively nested.

9. **Manage prompt templates:** Use various functions to work with prompt templates, like adding RAI disclaimers using `add_rai_template_variables_if_enabled`.

10. **Inject styles into HTML:** Use `inject_html_css_style_prefix` to add a CSS style prefix to all style attributes in an HTML string.

11. **Break text at length:** Use `break_text_at_length` to break text (or JSON) at a specified length with an appropriate suffix.

12. **Format dates:** Use `pretty_datetime` to format a `datetime` object into a readable string.

13. **Dedent strings:** Use `dedent` to remove leading whitespace and indentation from a string.

14. **Read and manage configurations:** Use `read_config_file` to read configuration files (config.ini) in the current project directory and default module directory, providing fallback mechanisms. Use `pretty_print_config` to print the loaded configuration.  Use `start_logger` to set up a logger based on the configuration.

15. **JSON Serializable Mixin:** Utilize the `JsonSerializableRegistry` class as a mixin to easily serialize and deserialize objects to/from JSON. This class supports recursive serialization of nested objects and collections.


Usage example
-------------------------
.. code-block:: python

    import tinytroupe.utils as utils
    import json
    from datetime import datetime

    # Example usage of compose_initial_LLM_messages_with_templates
    rendering_configs = {"name": "Alice"}
    messages = utils.compose_initial_LLM_messages_with_templates(
        system_template_name="system_prompt", user_template_name="user_prompt", rendering_configs=rendering_configs
    )
    print(json.dumps(messages, indent=2))


    # Example usage of extract_json
    input_string = """```json
    {
        "name": "Bob",
        "age": 30
    }
    ```"""
    extracted_json = utils.extract_json(input_string)
    print(extracted_json)


    # Example usage of pretty_datetime
    dt = datetime(2024, 1, 1, 10, 30)
    pretty_date_string = utils.pretty_datetime(dt)
    print(pretty_date_string)

    # Example of reading the config file
    config = utils.read_config_file(verbose=True)
    utils.pretty_print_config(config)

    # Example of using JsonSerializableRegistry
    class MyObject(utils.JsonSerializableRegistry):
        serializable_attributes = ['name', 'value']
        def __init__(self, name, value):
            self.name = name
            self.value = value
        def _post_init(self):
            print("Post initialization call")

    obj = MyObject("myobject", 123)
    json_representation = obj.to_json()
    print(json.dumps(json_representation, indent=4))

    loaded_object = utils.JsonSerializableRegistry.from_json(json_representation)
    print(loaded_object.name) # Access the deserialized data