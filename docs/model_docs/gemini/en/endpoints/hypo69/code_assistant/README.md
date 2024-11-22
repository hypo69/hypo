```rst
Code Assistant
=============

.. automodule:: assistant
    :members:
    :undoc-members:
    :show-inheritance:

Description
-----------

`Code Assistant` is a tool for interacting with Gemini and OpenAI models to process source code.
It performs tasks such as generating documentation, code validation, and test generation based on specified files.

Main Features
------------

- Reading source files: Reads code from files with `.py` and `README.MD` extensions from specified directories.
- Processing with models: Sends code to models to perform tasks like generating documentation or checking errors.
- Generating results: Model responses are saved to specified directories for each role.

Project Structure
----------------

- Models: Uses Gemini and OpenAI models for processing requests.
- Prompts: The program reads prompts from files in the `src/ai/prompts/developer/` directory (e.g., `doc_writer_en.md`).
- Files: Processes `.py` and `README.MD` files in specified starting directories.

Usage Examples
-------------

Running with settings from JSON:

.. code-block:: bash

    python assistant.py --settings settings.json

Running with explicit parameters:

.. code-block:: bash

    python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2

Example for `code_checker` role:

.. code-block:: bash

    python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir

Example for `openai` model:

.. code-block:: bash

    python assistant.py --role doc_writer --lang en --models openai


Command Line Parameters
-----------------------

- `--settings`: Path to the JSON settings file. Loads parameters from the file.
- `--role`: Model role for task execution (e.g., `doc_writer`, `code_checker`).
- `--lang`: Execution language (e.g., `ru` or `en`).
- `--models`: List of models to initialize (e.g., `gemini`, `openai`).
- `--start_dirs`: List of directories for processing (e.g., `/path/to/dir1`).


Working Logic
-------------

1. File reading: Searches for `.py` and `README.MD` files in the specified starting directories.
2. Prompt loading: Loads prompt files for each role and language from the `src/ai/prompts/developer/` directory.
3. Request processing: Forms requests based on loaded files and sends them to models.
4. Saving responses: Model responses are saved to the directory corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).

Exceptions
----------

Configuring exceptions for files and directories using parameters:
- `exclude_file_patterns`: List of regular expressions to exclude files.
- `exclude_dirs`: List of directories to exclude.
- `exclude_files`: List of files to exclude.

Logging
-------

Logs are saved using the `logger` library and contain information about the file processing progress and received responses.

Dependencies
------------

- Gemini API: Requires an API key to work with the Gemini model.
- OpenAI API: Requires an API key to work with the OpenAI model.
```