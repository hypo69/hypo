# test_security.py

## Overview

This module contains non-functional security tests for the TinyTroupe library.  It focuses on verifying the behavior of the default LLM API.

## Table of Contents

* [test_default_llmm_api](#test_default_llmm_api)

## Functions

### `test_default_llmm_api`

**Description**: Tests the default LLM API configured for TinyTroupe, ensuring it returns valid and expected responses.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `AssertionError`: Raised if any of the assertions fail, indicating a problem with the LLM API response.

**Detailed Explanation**:

This function verifies that the default LLM API call returns a non-empty dictionary containing `content` and `role` keys with a minimum length.  It also checks that the response is less than 2 million characters and is properly encoded in UTF-8, ensuring the API's functionality and data integrity. The response is also checked to make sure the message isn't None to ensure that the request is correctly routed.



```
```python
import pytest
import textwrap
import logging
import sys

import logging
logger = logging.getLogger("tinytroupe")

import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

from tinytroupe import openai_utils

from testing_utils import *

def test_default_llmm_api():
    """
    Tests some desireable properties of the default LLM API configured for TinyTroupe.
    """

    messages = create_test_system_user_message("If you ask a cat what is the secret to a happy life, what would the cat say?")

    next_message = openai_utils.client().send_message(messages)

    print(f"Next message as dict: {next_message}")

    # checks that the response meets minimum requirements
    assert next_message is not None, "The response from the LLM API should not be None."
    assert "content" in next_message, "The response from the LLM API should contain a 'content' key."
    assert len(next_message["content"]) >= 1, "The response from the LLM API should contain a non-empty 'content' key."
    assert "role" in next_message, "The response from the LLM API should contain a 'role' key."
    assert len(next_message["role"]) >= 1, "The response from the LLM API should contain a non-empty 'role' key."

    # convert to the dict to string
    next_message_str = str(next_message)
    print(f"Next message as string: {next_message_str}")

    # checks max and min characters
    assert len(next_message_str) >= 1, "The response from the LLM API should contain at least one character."
    assert len(next_message_str) <= 2000000, "The response from the LLM API should contain at most 2000000 characters."

    # checks encoding is UTF-8
    assert next_message_str.encode('utf-8'), "The response from the LLM API should be encodable in UTF-8 without exceptions."