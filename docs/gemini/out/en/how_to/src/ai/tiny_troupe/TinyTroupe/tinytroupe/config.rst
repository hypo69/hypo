rst
How to use the configuration file
========================================================================================

Description
-------------------------
This configuration file (`config.ini`) defines parameters for interacting with an OpenAI or Azure OpenAI service.  It sets default API type, model parameters, timeout settings, caching options, and logging levels for the TinyTroupe application.  It also handles potential harmful content and copyright issues.

Execution steps
-------------------------
1. **API Type Selection**: The `API_TYPE` parameter sets the API to use.  Default is `openai`.  This can be changed to `azure` for Azure OpenAI integration.  This choice directly affects the subsequent parameters.

2. **Azure API Version (if applicable):** If `API_TYPE` is `azure`, the `AZURE_API_VERSION` parameter sets the Azure OpenAI API version.

3. **Model Selection**: The `MODEL` parameter selects the specific OpenAI model.  For example, `gpt-4o` is a suitable option.

4. **Parameterization**: Parameters like `MAX_TOKENS`, `TEMPERATURE`, `FREQ_PENALTY`, and `PRESENCE_PENALTY` control model behavior and output.  These parameters influence aspects of the model responses.

5. **Timeout and Attempt Limits**: `TIMEOUT`, `MAX_ATTEMPTS`, and `WAITING_TIME` control timeouts and retry mechanisms for API calls.

6. **Embedding Model Selection**:  `EMBEDDING_MODEL` parameter defines the model to be used for embeddings.

7. **Caching**: `CACHE_API_CALLS` enables/disables caching of API calls for performance gains.  `CACHE_FILE_NAME` specifies the cache file path.

8. **Output Length**: `MAX_CONTENT_DISPLAY_LENGTH` sets the maximum length of displayed content from responses.

9. **Harmful Content Prevention**: `RAI_HARMFUL_CONTENT_PREVENTION` and `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` enable content moderation checks.

10. **Logging**:  The `LOGLEVEL` parameter controls the verbosity of logging output, with choices such as `ERROR`, `WARNING`, `INFO`, and `DEBUG`.


Usage example
-------------------------
.. code-block:: python

    # Load the configuration file
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Access a specific value
    api_type = config['OpenAI']['API_TYPE']
    model = config['OpenAI']['MODEL']
    max_tokens = int(config['OpenAI']['MAX_TOKENS'])

    print(f"Using API type: {api_type}, Model: {model}, Max Tokens: {max_tokens}")