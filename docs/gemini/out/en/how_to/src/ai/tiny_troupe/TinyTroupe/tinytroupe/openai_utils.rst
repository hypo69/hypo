rst
How to use the `openai_utils` module
========================================================================================

Description
-------------------------
This module provides functions and classes for interacting with the OpenAI API, including setting up configurations, handling API calls, caching responses, and managing different API clients.  It handles configurations from a `config.ini` file,  allowing for caching of API calls and the use of various OpenAI models. It supports both OpenAI and Azure OpenAI service API, offering flexibility for different integration needs. The module also includes error handling and retry mechanisms for robust API interaction.

Execution steps
-------------------------
1. **Import the necessary modules:**
   The code imports modules like `os`, `openai`, `time`, `json`, `pickle`, `logging`, `configparser`, `tiktoken`, and custom `utils` from the `tinytroupe` package.  It also imports necessary classes from the `openai` library (e.g., `OpenAI`, `AzureOpenAI`).  It defines a `logger` instance using `logging.getLogger()` to capture and log relevant information during the execution.

2. **Read configuration:**
   The `utils.read_config_file()` function is called to read configuration settings from `config.ini`. These settings include API keys, model parameters (e.g., `MODEL`, `MAX_TOKENS`), and caching preferences.

3. **Define default parameter values:**
   A `default` dictionary is created to hold default parameter values for API calls.  These are typically retrieved from the configuration. Values like `model`, `max_tokens`, `temperature`, and timeout are set.

4. **Define `LLMCall` class:**
   This class encapsulates an LLM model call, holding input messages, model configuration, and output.  The `__init__` method initializes the class with system and user templates for context. The `call` method composes messages, calls the actual OpenAI API (via the `client()` function), and extracts and returns the content from the API response.

5. **Define `OpenAIClient` and `AzureClient` classes:**
   These classes provide methods for interacting with the OpenAI API (either standard or Azure). `OpenAIClient` and `AzureClient` handle API initialization using the configured settings. The `send_message` method in both classes makes the API call and returns the response after error handling (including rate limit errors).

6. **Implement API calls:**
   The `_raw_model_call` method in `OpenAIClient` and `AzureClient` is a crucial function point.  It calls the respective OpenAI API, and `_raw_model_response_extractor` processes the raw response to return a useful Python dictionary.

7. **Client registration and retrieval:**
   The `register_client` function adds clients (OpenAI and Azure) to a registry. The `client()` function retrieves the appropriate client instance based on the `config.ini` setting.  This allows flexibility for using different API providers.

8. **Caching Mechanism:**
   The `_save_cache` and `_load_cache` methods handle persisting and retrieving API responses to the cache for reuse.

9. **Embedding Functionality:**
   The module provides methods to get text embeddings via the `get_embedding` function.

10. **Error Handling:**
   The module includes `InvalidRequestError` and `NonTerminalError` to manage various errors during API calls, facilitating better error management and retry logic.

11. **Forced configuration overrides:** Functions like `force_api_type`, `force_api_cache`, and `force_default_value` allow overriding specific configuration parameters for testing or specialized scenarios.


Usage example
-------------------------
.. code-block:: python

    import os
    from tinytroupe.openai_utils import client

    # Set environment variable for API key (crucial for production).
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    # Example usage
    messages = [
        {"role": "user", "content": "What is the capital of France?"},
    ]
    response = client().send_message(messages)

    if response:
        print(response)

    #Example for Azure OpenAI
    # os.environ["AZURE_OPENAI_ENDPOINT"] = "YOUR_AZURE_OPENAI_ENDPOINT"
    # os.environ["AZURE_OPENAI_KEY"] = "YOUR_AZURE_OPENAI_KEY"
    # ... use the client object with the same pattern.