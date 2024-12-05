# Google Generative AI Integration

## Overview

This module provides an interface for interacting with Google's Generative AI models, specifically Gemini.  It handles sending requests, receiving responses, and managing dialogues, allowing for integration into larger applications.  The module includes functionality for saving dialogue history to text and JSON files, along with robust error handling for various potential issues.


## Table of Contents

* [GoogleGenerativeAI](#googlegenerativeai)
    * [__init__](#__init__)
    * [ask](#ask)
    * [chat](#chat)
    * [describe_image](#describe_image)
    * [upload_file](#upload_file)
    * [MODELS](#models)


## Classes

### `GoogleGenerativeAI`

**Description**:  A class for interacting with Google Generative AI models.  It encapsulates the logic for sending prompts, handling responses, and managing dialogue history.

**Attributes**:
- `MODELS` (List[str]): A list of available AI models.
- `api_key` (str): The API key for accessing the generative model.
- `model_name` (str): The name of the model to use (defaults to `gemini-1.5-flash-8b`).
- `generation_config` (Dict): Configuration for generation (defaults to `{"response_mime_type": "text/plain"}`).
- `system_instruction` (Optional[str]): System instructions for the model.
- `dialogue_log_path` (Optional[Path]): Path to save dialogue logs.
- `dialogue_txt_path` (Optional[Path]): Path to save dialogue logs in text format.
- `history_dir` (Path): Directory for storing conversation history.
- `history_txt_file` (Optional[Path]): Path to the history log file (text).
- `history_json_file` (Optional[Path]): Path to the history log file (JSON).
- `model` (Optional[genai.GenerativeModel]): The initialized Google Generative AI model object.
- `_chat`:  Internal chat object.


**Methods**:

#### `__init__`

**Description**: Initializes a `GoogleGenerativeAI` object.

**Parameters**:
- `api_key` (str): The API key for accessing the generative model.
- `model_name` (Optional[str], optional): The name of the model to use. Defaults to "gemini-1.5-flash-8b".
- `generation_config` (Optional[Dict], optional): Configuration for generation. Defaults to `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str], optional): System instructions for the model. Defaults to `None`.


#### `ask`

**Description**: Sends a text prompt to the model and returns the response.

**Parameters**:
- `q` (str): The prompt to send to the model.
- `attempts` (int, optional): The number of attempts to get a response. Defaults to 15.

**Returns**:
- `Optional[str]`: The response from the model, or `None` if no response is received.

**Raises**:
- `requests.exceptions.RequestException`: Network error.
- `GatewayTimeout`, `ServiceUnavailable`: Service unavailable errors.
- `ResourceExhausted`: Quota exceeded error.
- `DefaultCredentialsError`, `RefreshError`: Authentication errors.
- `ValueError`, `TypeError`: Invalid input errors.
- `InvalidArgument`, `RpcError`: API error.
- `Exception`:  Other unexpected errors.



#### `chat`

**Description**:  Handles a chat conversation with the model.

**Parameters**:
- `q` (str): The user prompt to send to the model.

**Returns**:
- str: The response from the model.
- None: If any error occurs.


#### `describe_image`

**Description**: Generates a description of an image.

**Parameters**:
- `image_path` (Path): The path to the image file.

**Returns**:
- Optional[str]: The description of the image, or `None` if an error occurred.


**Raises**:
- `Exception`:  General errors during image processing.


#### `upload_file`

**Description**: Uploads a file to a service.

**Parameters**:
- `file` (str | Path | IOBase): The file to upload.
- `file_name` (Optional[str], optional): The desired name for the uploaded file. Defaults to `None`


**Returns**:
- bool: Status indicating successful upload.


**Raises**:
- `Exception`: Error during file upload.


#### `_save_dialogue`

**Description**: Saves the dialogue to text and JSON files.

**Parameters**:
- `dialogue` (list): List of dialogue messages.


#### `config`

**Description**: Retrieves the configuration from a JSON file.

**Returns**:
- dict: Configuration data from the file.



### `MODELS`

**Description**: A predefined list of available AI models.

```