# OpenAI Model Training Module

## Overview

This module defines the `OpenAIModel` class for interacting with the OpenAI API, handling model communication, and training. It includes methods for interacting with the API, retrieving and listing models/assistants, sending messages, performing sentiment analysis, dynamic training, and traditional model training. The module also provides functionality for saving training job IDs.


## Table of Contents

* [OpenAIModel](#openai-model-class)
    * [\_\_init\_\_](#__init__)
    * [list\_models](#list_models)
    * [list\_assistants](#list_assistants)
    * [set\_assistant](#set_assistant)
    * [_save\_dialogue](#_save_dialogue)
    * [determine\_sentiment](#determine_sentiment)
    * [ask](#ask)
    * [describe\_image](#describe_image)
    * [describe_image_by_requests](#describe_image_by_requests)
    * [dynamic\_train](#dynamic_train)
    * [train](#train)
    * [save\_job\_id](#save_job_id)
* [main](#main-function)


## OpenAIModel Class

### `__init__`

**Description**: Initializes the `OpenAIModel` object with an optional system instruction and assistant ID. Fetches and loads available models and assistants.

**Parameters**:

* `system_instruction` (str, optional): An optional system instruction for the model. Defaults to None.
* `model_name` (str): The name of the model to use. Defaults to 'gpt-4o-mini'.
* `assistant_id` (str, optional): An optional assistant ID. Defaults to the value from `gs.credentials.openai.assistant_id.code_assistant`.


**Raises**:

* `Exception`: Any exception raised during API interaction or file loading.


### `list_models`

**Description**: Dynamically fetches and returns available models from the OpenAI API.

**Returns**:

* `List[str]`: A list of model IDs available via the OpenAI API. Returns an empty list if any error occurs.


**Raises**:

* `Exception`: Any exception raised while listing models.


### `list_assistants`

**Description**: Dynamically loads available assistants from a JSON file.

**Returns**:

* `List[str]`: A list of assistant names. Returns an empty list if any error occurs.


**Raises**:

* `Exception`: Any exception raised during assistant loading.


### `set_assistant`

**Description**: Sets the assistant using the provided assistant ID.

**Parameters**:

* `assistant_id` (str): The ID of the assistant to set.


**Raises**:

* `Exception`: Any exception raised during assistant retrieval.


### `_save_dialogue`

**Description**: Saves the entire dialogue to the JSON file specified in `dialogue_log_path`.

**Raises**:

* `Exception`: Any exception during file saving.


### `determine_sentiment`

**Description**: Determines the sentiment of a message (positive, negative, or neutral).

**Parameters**:

* `message` (str): The message to analyze.


**Returns**:

* `str`: The sentiment ('positive', 'negative', or 'neutral').


### `ask`

**Description**: Sends a message to the model and returns the response, along with sentiment analysis.

**Parameters**:

* `message` (str): The message to send to the model.
* `system_instruction` (str, optional): Optional system instruction for the model.
* `attempts` (int, optional): Number of retry attempts. Defaults to 3.


**Returns**:

* `str`: The response from the model.  Returns None if all attempts fail.


**Raises**:

* `Exception`: Any exception during API interaction.


### `describe_image`

**Description**: Sends an image to the OpenAI API and receives a description.

**Parameters**:

* `image_path` (str | Path): Path to the image file.
* `prompt` (Optional[str], optional): Optional prompt for the image description. Defaults to None.
* `system_instruction` (Optional[str], optional): Optional system instruction for the model. Defaults to None.

**Returns**:

* `str`: The response from the model as a JSON-like object. Returns None if any error occurs.



**Raises**:

* `Exception`: Any exception during API interaction.


### `describe_image_by_requests`

**Description**: Sends an image to the OpenAI API using `requests` and receives a description.

**Parameters**:

* `image_path` (str | Path): Path to the image file.
* `prompt` (str, optional): Optional prompt for the image description. Defaults to None.


**Returns**:

* `str`: The description of the image.


**Raises**:

* `Exception`: Any exception during API interaction.


### `dynamic_train`

**Description**: Dynamically loads previous dialogue and fine-tunes the model based on it.

**Raises**:

* `Exception`: Any exception during fine-tuning.


### `train`

**Description**: Trains the model on the specified data or directory.

**Parameters**:

* `data` (str, optional): Path to a CSV file or CSV-formatted string with data.
* `data_dir` (Path | str, optional): Directory containing CSV files for training.
* `data_file` (Path | str, optional): Path to a single CSV file with training data.
* `positive` (bool, optional): Whether the data is positive or negative. Defaults to True.


**Returns**:

* `str | None`: The job ID of the training job or None if an error occurred.


**Raises**:

* `Exception`: Any exception during training.


### `save_job_id`

**Description**: Saves the job ID with description to a file.

**Parameters**:

* `job_id` (str): The job ID to save.
* `description` (str): Description of the job.
* `filename` (str, optional): The file to save job IDs. Defaults to "job_ids.json".


## main Function

**Description**: Main function for initializing the `OpenAIModel` and demonstrating usage. Includes examples of listing models/assistants, asking questions, dynamic training, training the model, and saving the job ID.


```