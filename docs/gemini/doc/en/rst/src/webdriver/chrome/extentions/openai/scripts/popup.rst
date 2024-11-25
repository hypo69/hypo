Popup JavaScript Script
=========================

This file contains the JavaScript code for the OpenAI popup extension.  It handles user interactions, fetching assistants, and sending messages to the backend API for processing.

.. automodule:: popup
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: loadAssistants
    :noindex:
    :show-inheritance:

    Loads a list of available assistants from the backend API.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: An error occurred during the API call.


.. autofunction:: sendMessage
    :noindex:
    :show-inheritance:

    Sends a message to the OpenAI backend API for processing.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: An error occurred during the API call.