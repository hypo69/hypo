# hypotez/src/ai/openai/model/training.py

## Overview

This module defines the `OpenAIModel` class for interacting with the OpenAI API, handling model communication, training, and image description. It includes methods for retrieving and listing available models and assistants, sending messages, performing sentiment analysis, dynamic training, and training the model with provided data.


## Table of Contents

* [OpenAIModel](#openai-model-class)
    * [__init__](#init)
    * [list_models](#list-models)
    * [list_assistants](#list-assistants)
    * [set_assistant](#set-assistant)
    * [_save_dialogue](#save-dialogue)
    * [determine_sentiment](#determine-sentiment)
    * [ask](#ask)
    * [describe_image](#describe-image)
    * [describe_image_by_requests](#describe-image-by-requests)
    * [dynamic_train](#dynamic-train)
    * [train](#train)
    * [save_job_id](#save-job-id)
* [main](#main-function)


## OpenAIModel Class

### `OpenAIModel`

**Description**: This class provides methods for interacting with the OpenAI API, handling model communication, training, and image description.

#### `__init__`

**Description**: Initializes the `OpenAIModel` object with API key, assistant ID, and optional system instructions.

**Parameters**:
- `system_instruction` (str, optional): An optional system instruction for the model. Defaults to `None`.
- `model_name` (str, optional): The name of the model to use. Defaults to 'gpt-4o-mini'.
- `assistant_id` (str, optional): An optional assistant ID. Defaults to the assistant ID from `gs.credentials.openai.assistant_id.code_assistant`.

**Returns**:
- None

#### `list_models`

**Description**: Dynamically fetches and returns available models from the OpenAI API.

**Returns**:
- List[str]: A list of model IDs available via the OpenAI API, or an empty list if an error occurs.

#### `list_assistants`

**Description**: Dynamically loads available assistants from a JSON file.

**Returns**:
- List[str]: A list of assistant names, or an empty list if an error occurs.


#### `set_assistant`

**Description**: Sets the assistant using the provided assistant ID.

**Parameters**:
- `assistant_id` (str): The ID of the assistant to set.


**Returns**:
- None

#### `_save_dialogue`

**Description**: Saves the entire dialogue to the JSON file specified by `dialogue_log_path`.

**Returns**:
- None


#### `determine_sentiment`

**Description**: Determines the sentiment of a message (positive, negative, or neutral).

**Parameters**:
- `message` (str): The message to analyze.

**Returns**:
- str: The sentiment ('positive', 'negative', or 'neutral').


#### `ask`

**Description**: Sends a message to the model and returns the response, along with sentiment analysis.

**Parameters**:
- `message` (str): The message to send to the model.
- `system_instruction` (str, optional): Optional system instruction. Defaults to the current `system_instruction`.
- `attempts` (int, optional): Number of retry attempts. Defaults to 3.

**Returns**:
- str: The response from the model, or None if the maximum number of attempts is reached.

#### `describe_image`

**Description**: Sends an image to the OpenAI API and receives a description.

**Parameters**:
- `image_path` (str | Path): Path to the image file.
- `prompt` (Optional[str], optional): Optional prompt to guide the description. Defaults to None.
- `system_instruction` (Optional[str], optional): Optional system instruction. Defaults to None.


**Returns**:
- str: The JSON formatted description from the model, or None if an error occurs.

#### `describe_image_by_requests`

**Description**: Sends an image to the OpenAI API using the `requests` library and receives a description.

**Parameters**:
- `image_path` (str | Path): Path to the image file.
- `prompt` (str, optional): Optional prompt to guide the description. Defaults to None.

**Returns**:
- str: The description from the model, or None if an error occurs.

#### `dynamic_train`

**Description**: Dynamically loads previous dialogue and fine-tunes the model based on it.

**Returns**:
- None


#### `train`

**Description**: Trains the model on the specified data or directory.

**Parameters**:
- `data` (str, optional): Path to a CSV file or CSV-formatted string with data.
- `data_dir` (Path | str, optional): Directory containing CSV files for training.
- `data_file` (Path | str, optional): Path to a single CSV file with training data.
- `positive` (bool, optional): Whether the data is positive or negative. Defaults to True.

**Returns**:
- str | None: The job ID of the training job or None if an error occurred.

#### `save_job_id`

**Description**: Saves the job ID with description to a file.

**Parameters**:
- `job_id` (str): The job ID to save.
- `description` (str): Description of the job.
- `filename` (str, optional): The file to save job IDs. Defaults to "job_ids.json".

**Returns**:
- None


## main Function

**Description**: Main function to initialize the `OpenAIModel` and demonstrate usage.


**Returns**:
- None