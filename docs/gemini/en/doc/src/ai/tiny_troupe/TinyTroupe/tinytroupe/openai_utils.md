# tinytroupe.openai_utils

## Overview

This module provides utility functions and classes for interacting with the OpenAI API, including handling different API types (OpenAI and Azure) and optional caching of API calls. It also defines default parameter values and helpers for model calls, allowing for flexible configuration and robust interaction with the OpenAI API.


## Classes

### `LLMCall`

**Description**: This class represents a single call to a Large Language Model (LLM). It encapsulates the input messages, model configuration, and the output response from the LLM call.

**Methods**

- `__init__(self, system_template_name: str, user_template_name: str = None, **model_params)`: Initializes an `LLMCall` instance.
    **Description**: Initializes the instance with system and user templates and optional model parameters.
    **Parameters**:
        - `system_template_name` (str): The name of the system template.
        - `user_template_name` (Optional[str], optional): The name of the user template. Defaults to `None`.
        - `**model_params` (Optional[dict], optional): Additional model parameters for the LLM call. Defaults to `None`.
    
- `call(self, **rendering_configs)`: Executes the LLM call.
    **Description**: Calls the LLM model with the specified rendering configurations.
    **Parameters**:
        - `**rendering_configs`: Arbitrary keyword arguments for rendering configurations.
    **Returns**:
        - `str | None`: The generated text content from the LLM, or `None` if an error occurs.


### `OpenAIClient`

**Description**: This class provides a client for interacting with the OpenAI API, enabling configuration and caching of API calls.

**Methods**

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Initializes the `OpenAIClient`.
    **Description**: Initializes the client, optionally enabling caching of API calls.
    **Parameters**:
        - `cache_api_calls` (bool): Whether to cache API calls. Defaults to the `default` value.
        - `cache_file_name` (str): The name of the file to use for caching API calls. Defaults to the `default` value.

- `set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"])`: Configures the cache settings for API calls.
    **Description**: Enables or disables caching of API calls.
    **Parameters**:
        - `cache_api_calls` (bool): Whether to enable API call caching.
        - `cache_file_name` (str): The file name to use for storing the cache.
    
- `_setup_from_config(self)`: Sets up the client from configuration.


- `send_message(self, current_messages, ...)`: Sends a message to the OpenAI API and retrieves the response.
    **Description**: Sends a message to the OpenAI API, with various parameters for controlling the response, and returns the response dictionary.
    **Parameters**:
        - `current_messages`: A list of dictionaries representing the conversation history.
        - `model`, `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, `presence_penalty`, `stop`, `timeout`, `max_attempts`, `waiting_time`, `exponential_backoff_factor`, `n`, `echo`: API parameters.  Refer to the OpenAI API documentation for details.
    **Returns**:
        - `dict | None`: A dictionary representing the generated response from the OpenAI API, or `None` if an error occurs or maximum attempts are reached.
    **Raises**:
      - `InvalidRequestError`: Raised for invalid requests.
      - `RateLimitError`: Raised if the request hits the API rate limit.
      - `NonTerminalError`: Raised for other errors that allow retrying.
      - Various other exceptions from the openai library.

- `_raw_model_call(self, model, chat_api_params)`: Calls the OpenAI API directly.
- `_raw_model_response_extractor(self, response)`: Extracts the response from the API response.
- `_count_tokens(self, messages: list, model: str)`: Counts tokens in a list of messages using tiktoken.
- `_save_cache(self)`: Saves the API cache to disk.
- `_load_cache(self)`: Loads the API cache from disk.
- `get_embedding(self, text, model=default["embedding_model"])`: Gets the embedding of a text.
- `_raw_embedding_model_call(self, text, model)`: Calls the embedding model.
- `_raw_embedding_model_response_extractor(self, response)`: Extracts the embedding from the API response.


### `AzureClient`

**Description**: A subclass of `OpenAIClient` for interacting with the Azure OpenAI Service API.


### `InvalidRequestError`

**Description**: Exception raised for invalid requests to the OpenAI API.

### `NonTerminalError`

**Description**: Exception raised for non-terminal errors that allow retrying.


## Functions

### `register_client(api_type, client)`

**Description**: Registers a client for a given API type.

**Parameters**:
- `api_type` (str): The type of the API (e.g., "openai", "azure").
- `client`: The client object to register.

### `_get_client_for_api_type(api_type)`

**Description**: Returns the registered client for the given API type.


### `client()`

**Description**: Returns the client configured for the current API type.


### `force_api_type(api_type)`

**Description**: Forces the use of a specific API type.


### `force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"])`

**Description**: Forces the use of a specific API cache configuration.

### `force_default_value(key, value)`

**Description**: Forces a specific default value for a given configuration key.


##  Constants / Variables

- `default`: A dictionary containing default parameters for the OpenAI API calls.
- `logger`: A logger instance for logging messages.