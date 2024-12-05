# Code Assistant: Training Project Code Model

## Overview

`Code Assistant` is a tool for interacting with **Gemini** and **OpenAI** models to process source code. It performs tasks such as generating documentation, checking code, and generating tests based on the code from specified files.

## Table of Contents

* [Overview](#overview)
* [Key Features](#key-features)
* [Project Structure](#project-structure)
* [Usage Examples](#usage-examples)
* [Command Line Parameters](#command-line-parameters)
* [Workflow](#workflow)
* [Exceptions](#exceptions)
* [Logging](#logging)
* [Dependencies](#dependencies)
* [Adding a New AI Model Role](#adding-a-new-ai-model-role)


## Key Features

* **Reading Source Files**: Reads code from `.py` and `README.MD` files from specified directories.
* **Processing with Models**: Sends code to models to perform tasks such as generating documentation or checking errors.
* **Generating Results**: Saves model responses to specified directories for each role.

## Project Structure

* **Models**: Uses **Gemini** and **OpenAI** models for processing requests.
* **Prompts**: Reads prompts from files in the `src/ai/prompts/developer/` directory (e.g., `doc_writer_en.md`).
* **Files**: Processes `.py` and `README.MD` files in the specified starting directories.

## Usage Examples

### Running with Settings from JSON:

```bash
python assistant.py --settings settings.json
```

### Running with Explicit Parameters:

```bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Example for `code_checker` Role:

```bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Example for `openai` Model:

```bash
python assistant.py --role doc_writer --lang en --models openai
```

## Command Line Parameters

* `--settings`: Path to a JSON file containing settings. Loads parameters from the file.
* `--role`: Model role to perform the task (e.g., `doc_writer`, `code_checker`).
* `--lang`: Language for task execution (e.g., `ru` or `en`).
* `--models`: List of models to initialize (e.g., `gemini`, `openai`).
* `--start_dirs`: List of directories to process (e.g., `/path/to/dir1`).


## Workflow

1. **Reading Files**: Finds `.py` and `README.MD` files in the specified starting directories.
2. **Loading Prompts**: Loads prompt files for each role and language from the `src/ai/prompts/developer/` directory.
3. **Processing Requests**: Forms requests based on loaded files and sends them to the models.
4. **Saving Responses**: Saves responses from the models to directories corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).

## Exceptions

Configuration of exceptions for files and directories using parameters:
* `exclude_file_patterns`: List of regular expressions for excluding files.
* `exclude_dirs`: List of directories to exclude.
* `exclude_files`: List of files to exclude.

## Logging

Logs are saved using the `logger` library and contain information about the file processing process and received responses.

## Dependencies

* **Gemini API**: Requires an API key for working with the Gemini model.
* **OpenAI API**: Requires an API key for working with the OpenAI model.


## Adding a New AI Model Role

To add a new role for the AI model (`gemini`, `openai`, etc.):

1. **`code_assistant.json`**:
   Add the new role to the list of roles in the `"roles"` array or to the `"exclude-roles"` array to make it inactive.  
2. **`translations/translations.json`**: Add the role to the translation file.
3. **`src/ai/prompts/developer/`**: Create a system prompt file for the new role.
4. **`instructions/`**: Create a command instruction file for the new role.