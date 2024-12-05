# TinyTroupe Configuration File

## Overview

This file defines the configuration parameters for the TinyTroupe application, specifically regarding the API interaction and model parameters.  It outlines the communication method (OpenAI or Azure OpenAI), API versioning, model selection, token limits, temperature, penalties, timeouts, retry attempts, waiting times, exponential backoff factors, embedding models, caching mechanisms, content display length, and safety settings for simulated interactions. It also controls the logging level.


## Configuration Sections

### `[OpenAI]`

**Description**: This section defines the OpenAI API parameters and configurations.

**Parameters**:

- `API_TYPE` (str): Specifies the API type.  Currently supports "openai" (default) or "azure" for Azure OpenAI.
- `AZURE_API_VERSION` (str, optional):  The API version to use for Azure OpenAI. Defaults to `2023-05-15`.


### `[Model]`

**Description**: This section defines parameters related to the language model used for interactions.

**Parameters**:

- `MODEL` (str): The specific model name to use. Currently set to `gpt-4o`.
- `MAX_TOKENS` (int): The maximum number of tokens allowed in a single API call.  Set to 4000.
- `TEMPERATURE` (float): A value controlling the randomness of the model's output.  Set to 0.3.
- `FREQ_PENALTY` (float): Penalty for repeated tokens.  Set to 0.0.
- `PRESENCE_PENALTY` (float): Penalty for frequent tokens. Set to 0.0.
- `TIMEOUT` (int): The timeout period for API calls in seconds. Set to 60.
- `MAX_ATTEMPTS` (int): The maximum number of times to retry a failed API call. Set to 5.
- `WAITING_TIME` (int):  Time to wait between API call attempts in seconds. Set to 1.
- `EXPONENTIAL_BACKOFF_FACTOR` (int): Factor for exponential backoff. Set to 5.
- `EMBEDDING_MODEL` (str): Specifies the model for embedding operations. Currently set to `text-embedding-3-small`.
- `CACHE_API_CALLS` (bool): A flag to enable caching of API responses. Set to `False`.
- `CACHE_FILE_NAME` (str): The name of the cache file. Set to `openai_api_cache.pickle`.
- `MAX_CONTENT_DISPLAY_LENGTH` (int): Maximum characters displayed for content.  Set to 1024.



### `[Simulation]`

**Description**: This section controls safety features for simulated interactions.

**Parameters**:

- `RAI_HARMFUL_CONTENT_PREVENTION` (bool): Set to `True` to enable harmfulness detection.
- `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` (bool): Set to `True` to enable copyright infringement checks.



### `[Logging]`

**Description**: This section defines the logging level for the application.

**Parameters**:

- `LOGLEVEL` (str): The logging level to use. Set to `ERROR`.  Other options include `WARNING`, `INFO`, and `DEBUG`.