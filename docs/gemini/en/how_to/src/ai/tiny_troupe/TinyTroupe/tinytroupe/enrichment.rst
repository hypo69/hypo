rst
How to use the TinyEnricher class
========================================================================================

Description
-------------------------
This code defines a `TinyEnricher` class for enriching content using a language model (likely OpenAI).  It takes requirements, content, and optional context as input and returns enriched content (often code) from the language model's response.  The class utilizes the `chevron` library for templating, handles logging, and leverages TinyTroupe's existing utilities for message composition, OpenAI interaction, and code block extraction.  It also allows for caching context for improved responses.


Execution steps
-------------------------
1. **Initialization:** The `__init__` method initializes the `TinyEnricher` object, taking an optional `use_past_results_in_context` flag and an empty `context_cache`.  This flag determines if previously generated results should be included in the context for subsequent requests.  The `context_cache` will hold such past results for future use.

2. **Enrichment Process (`enrich_content`):**
    * **Input Handling:** Accepts `requirements`, `content`, `content_type`, `context_info`, and an optional `context_cache` and a `verbose` flag.
    * **Message Composition:**  Constructs a message to the language model using `chevron` templates.  The `rendering_configs` dictionary provides the input data to the templates.  These templates ("enricher.system.mustache" and "enricher.user.mustache") are presumably designed for specific formatting of the LLM instructions.
    * **OpenAI Interaction:** Sends the structured messages to the OpenAI API using `openai_utils.client().send_message()`. This is where the actual enrichment happens. The function waits for the LLM's response.
    * **Error Handling and Logging:** Checks if the response (`next_message`) is valid. If not, sets `result` to `None`. Otherwise, it extracts the code block from the response using `utils.extract_code_block()`.  Logs debug information about the response and the potential code block extracted.
    * **Return Value:** Returns the extracted code block (`result`) or `None` if the API call fails.


Usage example
-------------------------
.. code-block:: python

    import logging
    from tinytroupe.enrichment import TinyEnricher
    from tinytroupe import openai_utils # This will likely need to be adapted to your actual setup

    # Configure logging (Crucial for debugging)
    logging.basicConfig(level=logging.DEBUG)

    # Example Usage
    enricher = TinyEnricher(use_past_results_in_context=True)

    requirements = "Write a Python function to calculate the factorial of a number."
    content = "Input number: 5"
    context_cache = [] # Example usage of context caching.  Likely populated in a larger context.

    result = enricher.enrich_content(requirements, content, context_cache=context_cache, verbose=True)

    if result:
        print("Enriched code:\n", result)
    else:
        print("No code block found in the response.")