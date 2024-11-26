Module for a Code Assistant
============================

This module provides the :class:`CodeAssistant` class for interacting with various AI models, like Google Gemini and OpenAI, to perform code processing tasks.

Examples
--------

.. code-block:: python
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()


Platforms and Synopsis
----------------------

Platforms:  Python 3.x
Synopsis:  Handles code analysis and processing using specified AI models.


Class CodeAssistant
===================

The :class:`CodeAssistant` class interacts with AI models to analyze and generate documentation for code.

Attributes
----------

- `role`: The role of the assistant (e.g., 'code_checker').
- `lang`: The language of the assistant (e.g., 'ru').
- `model`: A list of AI models to use (e.g., ['gemini']).


Methods
-------

- `process_files`: Processes files containing code.


Method process_files
--------------------

This method analyzes and processes files.

Parameters
----------

- `files`: A list of file paths to process.
- `options`: Additional options for customizing the processing.


Return Value
------------

- Returns a list of processed data.


Examples
--------

.. code-block:: python
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={})


Exceptions
----------

- :exc:`FileNotFoundError`: Raised if a file specified in the `files` list does not exist.