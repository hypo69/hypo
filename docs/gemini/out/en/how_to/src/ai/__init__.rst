rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python file, `src/ai/__init__.py`, is an initialization module for AI models. It imports classes representing different AI models, making them available for use in other parts of the project.  Specifically, it imports classes for Google's Gemini and OpenAI models.  It also defines a global variable `MODE` to likely store the current operating mode (e.g., 'dev', 'prod').


Execution steps
-------------------------
1. The file sets the global variable `MODE` to the string 'dev'.  This is likely a configuration for the operation mode of the AI modules (development, testing, or production).
2. The file imports classes from submodules `gemini.py` and `openai.py`, which are likely to contain specific implementations for interacting with Google's Gemini and OpenAI's AI models.  This import statement makes the functionality of those models available in this module for other parts of the project.

Usage example
-------------------------
.. code-block:: python

    from src.ai import GoogleGenerativeAI

    # Create an instance of the GoogleGenerativeAI model.
    model = GoogleGenerativeAI()
    # Access the model properties, and call model methods if applicable.
    response = model.generate_text("This is a test prompt.")
    print(response)