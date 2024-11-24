Code Assistant
=============

This module provides a tool for interacting with Gemini and OpenAI models for processing source code.  It handles tasks such as generating documentation, code checking, and generating tests based on the provided files.

.. automodule:: hypotez.src.endpoints.hypo69.code_assistant
   :members:
   :undoc-members:
   :show-inheritance:

Description
----------

`Code Assistant` is a tool for interacting with Gemini and OpenAI models to process source code.  It performs tasks like generating documentation, checking code, and generating tests from specified files.

Main Features
------------

- **Reading Source Files**: Reads code from files with `.py` and `README.MD` extensions from specified directories.
- **Processing with Models**: Sends the code to models for tasks such as generating documentation or checking errors.
- **Generating Results**: Saves model responses to specified directories for each role.

Project Structure
----------------

- **Models**: Uses Gemini and OpenAI models for processing requests.
- **Prompts**: Reads prompts from files in the `src/ai/prompts/developer/` directory (e.g., `doc_writer_en.md`).
- **Files**: Processes files with `.py` and `README.MD` extensions in specified starting directories.

Usage Examples
-------------

Command-line Usage
~~~~~~~~~~~~~~~~~

### Running with settings from JSON:

```bash
python assistant.py --settings settings.json
```

### Running with explicit parameters:

```bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Example for `code_checker` role:

```bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Example for `openai` model:

```bash
python assistant.py --role doc_writer --lang en --models openai
```

Command-line Arguments
~~~~~~~~~~~~~~~~~~~~~~~

- `--settings`: Path to the JSON file with settings. Loads parameters from the file.
- `--role`: Model role for performing the task (e.g., `doc_writer`, `code_checker`).
- `--lang`: Language for task execution (e.g., `ru` or `en`).
- `--models`: List of models for initialization (e.g., `gemini`, `openai`).
- `--start_dirs`: List of directories for processing (e.g., `/path/to/dir1`).


Workflow
--------

1. **File Reading**: Finds files with `.py` and `README.MD` extensions in specified starting directories.
2. **Prompt Loading**: Loads prompt files for each role and language from the `src/ai/prompts/developer/` directory.
3. **Request Processing**: Forms requests based on loaded files and sends them to the models.
4. **Response Saving**: Saves responses from models to the directory corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).

Exceptions
----------

- `exclude_file_patterns`: List of regular expressions to exclude files.
- `exclude_dirs`: List of directories to exclude.
- `exclude_files`: List of files to exclude.

Logging
-------

Logs are saved using the `logger` library and contain information about the file processing process and the received responses.

Dependencies
-----------

- **Gemini API**: Requires an API key for Gemini model interaction.
- **OpenAI API**: Requires an API key for OpenAI model interaction.