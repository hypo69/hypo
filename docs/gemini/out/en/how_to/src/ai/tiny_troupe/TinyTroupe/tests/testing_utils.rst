rst
How to use the testing utilities
========================================================================================

Description
-------------------------
This code defines utility functions for testing the TinyTroupe codebase.  These functions provide ways to check for specific actions, stimuli, and action types within lists of actions and stimuli, as well as whether an action type concludes a list of actions. It also includes a function to check a proposition using an LLM call and other functions for file management and creating test scenarios.

Execution steps
-------------------------
1. **Import necessary modules**: The code imports modules like `os`, `sys`, `time`, `pytest`, and custom modules from the `tinytroupe` package, setting paths for the import process.

2. **Enable API caching**: A function call (`openai_utils.force_api_cache`) is used to enable API caching for the OpenAI API for testing, which saves time.


3. **Define utility functions for checking actions and stimuli**: Functions like `contains_action_type`, `contains_action_content`, `contains_stimulus_type`, and `contains_stimulus_content` are defined to check if a list of actions or stimuli contains a specific type or content.

4. **Define functions for checking actions termination**: The function `terminates_with_action_type` checks if a list of actions ends with a specific action type.

5. **Implement proposition checking function**: `proposition_holds` checks whether a given proposition is true or false by calling an LLM (Large Language Model) using OpenAI API. It formats a system prompt, a user prompt, and sends the messages to the LLM. Then, it cleans the returned result and checks if the cleaned result starts with "true" or "false", returning the corresponding boolean value.

6. **Define function for alphanumeric filtering**: `only_alphanumeric` removes non-alphanumeric characters from a string.

7. **Define function for creating messages for LLM**: `create_test_system_user_message` creates a list containing a system message and an optional user message, useful for constructing inputs for LLM calls.

8. **Define function for checking agent configurations**: `agents_configs_are_equal` checks if the configurations of two agents are the same, optionally ignoring the agent name.

9. **Define I/O utility functions**: `remove_file_if_exists` removes a file if it exists, and `get_relative_to_test_path` constructs a path relative to the test file directory.

10. **Define pytest fixtures**: Fixtures like `focus_group_world` and `setup` are defined to set up the testing environment for pytest tests.


Usage example
-------------------------
.. code-block:: python

    import pytest
    from tinytroupe.tests.testing_utils import contains_action_type, proposition_holds

    # Example usage for contains_action_type
    actions = [
        {"action": {"type": "greet"}},
        {"action": {"type": "ask_question"}},
    ]
    result = contains_action_type(actions, "ask_question")
    print(result)  # Output: True

    # Example usage for proposition_holds
    proposition = "The text contains some ideas for a product."
    result = proposition_holds(proposition)
    print(result)  # Output: True/False (depending on the LLM's response)

    # Example usage inside a pytest test
    def test_proposition_positive(focus_group_world):
       assert proposition_holds("The world object exists.") is True