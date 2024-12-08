rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block contains a test function (`test_default_llmm_api`) designed to verify the security and expected behavior of the default Large Language Model (LLM) API integrated with the TinyTroupe library. It checks for crucial aspects like the response not being null, containing required keys ("content", "role"), having non-empty values, adhering to character length limits, and encoding compatibility.  It uses the `openai_utils` module to interact with the LLM.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports `pytest`, `textwrap`, `logging`, `sys`, and specific modules from the TinyTroupe library, like `openai_utils`. It also sets up logging and adds necessary paths to the system path for module discovery.


2. **Define the test function (`test_default_llmm_api`):**  This function focuses on testing the default LLM API.


3. **Create test messages:** It creates a sample message using `create_test_system_user_message` to send to the LLM API.


4. **Send message to the LLM API:** It sends the test message to the LLM using `openai_utils.client().send_message(messages)`, storing the response in `next_message`.


5. **Validate the LLM response:** The code performs several crucial checks on the received response:
   - Checks if the response is not `None`.
   - Checks if the response dictionary contains the `content` key.
   - Checks if the `content` value is not empty.
   - Checks if the response dictionary contains the `role` key.
   - Checks if the `role` value is not empty.
   - Checks if the response string length is within the acceptable range (1 to 2,000,000 characters).
   - Checks that the response string can be encoded in UTF-8 without raising exceptions.


6. **Print response:**  The code prints the response as both a dictionary and a string for easier debugging.

7. **Assertions:** The function uses `assert` statements to confirm that the response meets the expected criteria.


Usage example
-------------------------
.. code-block:: python

    import pytest
    import textwrap
    import logging
    import sys
    from tinytroupe import openai_utils
    from testing_utils import create_test_system_user_message


    def test_default_llmm_api():
        messages = create_test_system_user_message("If you ask a cat what is the secret to a happy life, what would the cat say?")
        next_message = openai_utils.client().send_message(messages)
        print(f"Next message as dict: {next_message}")
        assert next_message is not None
        assert "content" in next_message
        assert len(next_message["content"]) >= 1
        assert "role" in next_message
        assert len(next_message["role"]) >= 1
        next_message_str = str(next_message)
        print(f"Next message as string: {next_message_str}")
        assert len(next_message_str) >= 1
        assert len(next_message_str) <= 2000000
        assert next_message_str.encode('utf-8')

    # ... (rest of the test code)