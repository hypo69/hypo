# tinytroupe/config.ini

## Overview

This configuration file (`config.ini`) defines parameters for the TinyTroupe AI system, specifically for interacting with the OpenAI or Azure OpenAI services.  It outlines API types, model parameters, caching settings, logging levels, and simulation flags.

## Sections

### `[DEFAULT]`

**Description**: This section contains general configuration settings, like the default API type.

**Parameters**:

- `API_TYPE` (str): Specifies whether the system should use the OpenAI or Azure OpenAI service.  Defaults to `openai`.


### `[OpenAI]`

**Description**: This section defines parameters for interacting with the OpenAI API.

**Parameters**:

- `API_TYPE` (str): Specifies whether the system should use the OpenAI API.  Defaults to `openai`.


### `[Azure]`

**Description**: This section defines parameters for interacting with the Azure OpenAI API.

**Parameters**:

- `AZURE_API_VERSION` (str):  Specifies the Azure OpenAI API version.  Defaults to `2023-05-15`.  Refer to Microsoft's documentation for current versions: [https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python)


### `[Model]`

**Description**: This section contains parameters related to the AI model used.

**Parameters**:

- `MODEL` (str): Specifies the AI model to be used.  Defaults to `gpt-4o`.
- `MAX_TOKENS` (int): Maximum number of tokens allowed in a response.  Defaults to `4000`.
- `TEMPERATURE` (float): Controls the randomness of the model's output. Defaults to `0.3`.
- `FREQ_PENALTY` (float): Penalty for repeated tokens. Defaults to `0.0`.
- `PRESENCE_PENALTY` (float): Penalty for repeated tokens in different parts of the response. Defaults to `0.0`.
- `TIMEOUT` (int): Timeout for API calls in seconds. Defaults to `60`.
- `MAX_ATTEMPTS` (int): Maximum number of retries for failed API calls. Defaults to `5`.
- `WAITING_TIME` (int): Time between retries in seconds. Defaults to `1`.
- `EXPONENTIAL_BACKOFF_FACTOR` (int): Factor for increasing waiting time exponentially between retries. Defaults to `5`.
- `EMBEDDING_MODEL` (str): Model used for embeddings. Defaults to `text-embedding-3-small`.

### `[Caching]`

**Description**: Settings related to caching API calls.

**Parameters**:

- `CACHE_API_CALLS` (bool): Whether to cache API calls. Defaults to `False`.
- `CACHE_FILE_NAME` (str): Name of the cache file. Defaults to `openai_api_cache.pickle`.

### `[Display]`

**Description**: Settings related to the displayed content length.

**Parameters**:

- `MAX_CONTENT_DISPLAY_LENGTH` (int): Maximum length of displayed content. Defaults to `1024`.

### `[Simulation]`

**Description**: Parameters related to simulation mode and harmful content prevention.

**Parameters**:

- `RAI_HARMFUL_CONTENT_PREVENTION` (bool): Flag to enable harmful content prevention. Defaults to `True`.
- `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` (bool): Flag to enable copyright infringement prevention. Defaults to `True`.

### `[Logging]`

**Description**: Configuration for logging output.

**Parameters**:

- `LOGLEVEL` (str): Sets the logging level.  Options include: `ERROR`, `WARNING`, `INFO`, `DEBUG`. Defaults to `ERROR`.