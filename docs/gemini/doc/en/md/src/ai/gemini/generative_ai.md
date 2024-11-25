# hypotez/src/ai/gemini/generative_ai.py

## Overview

This module provides a Python class `GoogleGenerativeAI` for interacting with Google's Generative AI models, specifically Gemini. It handles sending requests, receiving responses, and managing dialogue logs.  The class includes features for saving dialogue history in text and JSON formats.  Error handling is comprehensive, with exponential backoff for network issues and authentication failures.

## Table of Contents

* [GoogleGenerativeAI](#googlegenerativeai)
    * [__init__](#__init__)
    * [__post_init__](#__post_init__)
    * [config](#config)
    * [_save_dialogue](#_save_dialogue)
    * [ask](#ask)
    * [describe_image](#describe_image)
* [chat](#chat)


## Classes

### `GoogleGenerativeAI`

**Description**: A class for interacting with Google Generative AI models, handling requests, responses, and dialogue logging.

**Attributes**:
- `MODELS` (List[str]): A list of available AI models.
- `api_key` (str): API key for accessing the generative model.
- `model_name` (str): Name of the model to use.
- `generation_config` (Dict): Configuration for generation.
- `mode` (str): Operating mode of the model (e.g., 'debug' or 'production').
- `dialogue_log_path` (Optional[Path]): Path for logging dialogues.
- `dialogue_txt_path` (Optional[Path]): Path for saving text files of dialogues.
- `history_dir` (Path): Directory for storing history.
- `history_txt_file` (Optional[Path]): Path to file for storing history in text format.
- `history_json_file` (Optional[Path]): Path to file for storing history in JSON format.
- `model` (Optional[genai.GenerativeModel]): The Google Generative AI model object.
- `system_instruction` (Optional[str]): Instruction for the system, setting model behavior parameters.

**Methods**:

- `__init__`: Initializes the `GoogleGenerativeAI` object.
- `__post_init__`: Initializes the model if the API key is present but the model wasn't initialized during construction.
- `config`: Retrieves configuration from a config file.
- `_save_dialogue`: Saves the dialogue to text and JSON files, handling file size.
- `ask`: Sends a text request to the model and returns the response.
- `describe_image`: Generates a description of an image.


## Functions

### `chat`

**Description**: Starts an interactive chat session with the AI model.

**Example Usage**:
```python
>>> chat() # Starts the interactive chat session.
```


```markdown
### `GoogleGenerativeAI.__init__`

**Description**: Initializes the GoogleGenerativeAI instance.

**Parameters**:
- `api_key` (str): API key for accessing the generative model.
- `model_name` (Optional[str], optional): Name of the model to use. Defaults to "gemini-1.5-flash-8b".
- `generation_config` (Optional[Dict], optional): Configuration for generation. Defaults to `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str], optional): Instruction for the system. Defaults to `None`.

**Raises**:
- `Exception`: Any error during initialization.


### `GoogleGenerativeAI.__post_init__`

**Description**: Initializes the AI model if the API key is present but the model wasn't initialized during construction.


### `GoogleGenerativeAI.config`

**Description**: Retrieves configuration from a config file.

**Returns**:
- `Dict`: The configuration dictionary.


### `GoogleGenerativeAI._save_dialogue`

**Description**: Saves the dialogue to text and JSON files.

**Parameters**:
- `dialogue` (list): List of messages representing the dialogue to save.

**Raises**:
- `Exception`: Any error during file saving.



### `GoogleGenerativeAI.ask`

**Description**: Sends a text request to the model and returns the response.

**Parameters**:
- `q` (str): The question to send to the model.
- `attempts` (int, optional): The number of attempts to get a response. Defaults to 15.

**Returns**:
- `Optional[str]`: The response from the model or `None` if no response was received after multiple attempts.


**Raises**:
- `requests.exceptions.RequestException`: Errors during network communication.
- `GatewayTimeout`, `ServiceUnavailable`, `ResourceExhausted`: Errors related to service availability or resource limits.
- `DefaultCredentialsError`, `RefreshError`: Errors related to authentication.
- `ValueError`, `TypeError`, `InvalidArgument`, `RpcError`, `Exception`: General errors during model interaction.


### `GoogleGenerativeAI.describe_image`

**Description**: Generates a description of an image.

**Parameters**:
- `image_path` (Path): Path to the image to describe.

**Returns**:
- `Optional[str]`: The image description or `None` if an error occurs.


**Raises**:
- `Exception`: Any error during image description process.



### `chat`

**Description**: Starts an interactive chat session.

```
```
```
```