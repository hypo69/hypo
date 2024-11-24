Module CodeAssistant
=====================

This module contains the :class:`CodeAssistant` class, used for working with various AI models,
such as Google Gemini and OpenAI, to perform code processing tasks.

Usage Examples
----------------

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()


Platforms and Synopsis
----------------------

Platforms:  Python 3.x
Synopsis:  Provides a framework for interacting with AI models for code analysis and generation.


.. automodule:: hypotez.src.ai.prompts.developer.code_assistant
    :members:
    :undoc-members:
    :show-inheritance: