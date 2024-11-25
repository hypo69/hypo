# Module: src.suppliers.chat_gpt.chat_gpt

## Overview

This module provides functionalities related to interacting with the ChatGPT API.  It currently focuses on retrieving conversation HTML files from a specified directory.


## Classes

### `ChatGpt`

**Description**: This class encapsulates methods for handling ChatGPT conversations.

**Methods**

#### `yeld_conversations_htmls`

**Description**: Generates HTML content of ChatGPT conversations from a specified directory.

**Returns**:
- `str`: Returns the HTML content of the retrieved conversation files.

**Raises**:
- `FileNotFoundError`: If the specified directory or conversation HTML files do not exist.
- `Exception`: If any other unforeseen error occurs.


## Functions (None)


## Variables

### `MODE`

**Description**: A string variable representing the current mode (e.g., 'dev', 'prod').

**Value**:  'dev'