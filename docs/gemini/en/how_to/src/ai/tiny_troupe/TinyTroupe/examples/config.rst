rst
How to use the config.ini file
========================================================================================

Description
-------------------------
This file configures parameters for interacting with the OpenAI or Azure OpenAI API. It defines various options, including API type, model parameters, timeout settings, caching behavior, and logging levels.  It also contains settings for handling potentially harmful or copyright-infringing content during simulation.

Execution steps
-------------------------
1. **Specify API Type:** The `API_TYPE` setting defaults to `openai`, but can be changed to `azure` if using the Azure OpenAI service.

2. **Set API Version (Azure):**  If `API_TYPE` is `azure`, set the `AZURE_API_VERSION` to the appropriate version from Azure's documentation.

3. **Configure Model Parameters:** Define parameters for the chosen model, such as `MODEL`, `MAX_TOKENS`, `TEMPERATURE`, `FREQ_PENALTY`, `PRESENCE_PENALTY`, and `TIMEOUT`.  These settings influence the AI model's output.

4. **Establish Timeout and Retries:** Configure the `TIMEOUT` and `MAX_ATTEMPTS` values to manage API call timeouts and retry attempts.

5. **Manage Caching:** The `CACHE_API_CALLS` setting enables caching of API calls.  `CACHE_FILE_NAME` specifies the cache file.

6. **Control Content Display Length:** `MAX_CONTENT_DISPLAY_LENGTH` limits the amount of displayed content.

7. **Enable Simulation Checks:** The `RAI_HARMFUL_CONTENT_PREVENTION` and `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` settings allow you to activate checks for inappropriate content during simulation.

8. **Configure Logging:** The `LOGLEVEL` setting controls the logging verbosity level (ERROR, WARNING, INFO, DEBUG).


Usage example
-------------------------
.. code-block:: ini

    [OpenAI]
    # OpenAI or Azure OpenAI Service
    # Default options: openai, azure
    API_TYPE=openai

    # Check Azure's documentation for updates here:
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python
    AZURE_API_VERSION=2023-05-15

    # Model parameters
    MODEL=gpt-4
    MAX_TOKENS=2000
    TEMPERATURE=0.7
    FREQ_PENALTY=0.8
    PRESENCE_PENALTY=0.6
    TIMEOUT=30
    MAX_ATTEMPTS=3
    WAITING_TIME=0.5
    EXPONENTIAL_BACKOFF_FACTOR=2

    EMBEDDING_MODEL=text-embedding-ada-002
    CACHE_API_CALLS=True
    CACHE_FILE_NAME=openai_cache.pickle

    MAX_CONTENT_DISPLAY_LENGTH=512

    [Simulation]
    RAI_HARMFUL_CONTENT_PREVENTION=True
    RAI_COPYRIGHT_INFRINGEMENT_PREVENTION=True

    [Logging]
    LOGLEVEL=INFO