# Module for Working with Code Assistants

## Overview

This module provides a way to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.  It allows for the handling of code files and offers flexible configuration options for the assistant.

## Example Usage

```python
from code_assistant import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
try:
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={'max_tokens': 500})
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
```

## Classes

### `CodeAssistant`

**Description**: This class provides methods for interacting with code assistant AI models. It handles setting up the assistant, processing files, and managing potential errors.

**Attributes**:

- `role` (str): The role of the assistant, for example, 'code_checker'.
- `lang` (str): The language the assistant should use, for example, 'en'.
- `model` (list): A list of AI models to use, for example, ['gemini'].

**Methods**:

- `process_files(files: list, options: dict = {}) -> list | None`: Processes a list of files.

    **Description**: This method takes a list of files and a dictionary of options. It processes the files using the specified AI models.  If the assistant encounters an error, it raises an exception.

    **Parameters**:
    - `files` (list): A list of file paths to process.
    - `options` (dict, optional): A dictionary of options.  Defaults to an empty dictionary.

    **Returns**:
    - list | None: A list of processed data or `None` if an error occurred during processing.

    **Raises**:
    - `FileNotFoundError`: If one or more files do not exist.
    - `Exception`: If any other exception occurs during the file processing or interaction with the AI models.


## Functions

(No functions defined in the provided code snippet.)

```