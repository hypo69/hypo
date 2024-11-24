Module for a Code Assistant
==========================

This module contains the :class:`CodeAssistant` class for working with various AI models,
such as Google Gemini and OpenAI, to perform code processing tasks.

Examples
--------

Example usage of the `CodeAssistant` class:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()


Platforms and synopsis
----------------------

Platform:  Python

Synopsis: This module provides tools to interact with AI models for code analysis and documentation generation.


.. automodule:: hypotez.src.ai.prompts.developer.code_assistant
    :members:
    :undoc-members:
    :show-inheritance: