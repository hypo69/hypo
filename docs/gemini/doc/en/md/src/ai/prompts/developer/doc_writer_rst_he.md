# Code Assistant Module

## Overview

This module provides a class for interacting with various AI models, such as Google Gemini and OpenAI, for code processing tasks.  It facilitates code analysis and documentation generation.  Example usage is provided below.

## Platforms and Synopsis

This module is designed for use with platforms capable of running Python code, primarily focusing on interacting with AI models for tasks related to code analysis.

## Classes

### `CodeAssistant`

**Description**: This class encapsulates the functionality for interacting with AI models for code-related tasks. It handles the interaction with the chosen AI model, defining the role, language, and models used.

**Attributes**:

- `role` (str): Specifies the role of the assistant (e.g., "code_checker").
- `lang` (str): Defines the language for the assistant (e.g., "ru").
- `model` (list): A list of AI models (e.g., ["gemini"]).

**Methods**:

#### `process_files`

**Description**: Processes a list of files using the configured AI models.

**Parameters**:

- `files` (list): A list of file paths to be processed.
- `options` (dict, optional): Additional options for file processing. Defaults to an empty dictionary.


**Returns**:

- `list`: A list of processed data.  Returns an empty list if no files are provided.


**Raises**:

- `FileNotFoundError`: Raised if a file specified in the `files` list does not exist.
- `Exception`: A general exception handler for unexpected errors during file processing.




## Usage Examples

```python
# Example usage of the CodeAssistant class
from code_assistant import CodeAssistant  # Assuming code_assistant is the module name.

assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
files_to_process = ['file1.py', 'file2.py']
try:
    result = assistant.process_files(files=files_to_process, options={'verbose': True})
    print(result)  # Print the processed data
except FileNotFoundError as ex:
    print(f"Error: {ex}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
```


```