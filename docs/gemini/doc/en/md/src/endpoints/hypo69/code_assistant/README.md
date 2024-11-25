# Code Assistant: Training Project Code Model

## Overview

`Code Assistant` is a tool for interacting with **Gemini** and **OpenAI** models to process source code. It performs tasks such as generating documentation, code validation, and generating tests based on the code from specified files.

## Table of Contents

* [Overview](#overview)
* [Key Features](#key-features)
* [Project Structure](#project-structure)
* [Usage Examples](#usage-examples)
    * [Running with settings from JSON](#running-with-settings-from-json)
    * [Running with explicit parameters](#running-with-explicit-parameters)
    * [Example for `code_checker` role](#example-for-code_checker-role)
    * [Example for `openai` model](#example-for-openai-model)
* [Command-Line Parameters](#command-line-parameters)
* [Workflow](#workflow)
* [Exceptions](#exceptions)
* [Logging](#logging)
* [Dependencies](#dependencies)


## Key Features

- **Source File Reading**: Reads code from files with `.py` and `README.MD` extensions from specified directories.
- **Model Processing**: Sends code to models for tasks like documentation generation or error checking.
- **Result Generation**: Model responses are saved to specified directories for each role.


## Project Structure

- **Models**: Uses **Gemini** and **OpenAI** models for processing requests.
- **Prompts**: The program reads prompts from files in the `src/ai/prompts/developer/` directory (e.g., `doc_writer_en.md`).
- **Files**: Processes `.py` and `README.MD` files in specified starting directories.


## Usage Examples

### Running with settings from JSON

```bash
python assistant.py --settings settings.json
```

### Running with explicit parameters

```bash
python assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Example for `code_checker` role

```bash
python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Example for `openai` model

```bash
python assistant.py --role doc_writer --lang en --models openai
```


## Command-Line Parameters

- `--settings`: Path to a JSON file with settings. Loads parameters from the file.
- `--role`: Model role for the task (e.g., `doc_writer`, `code_checker`).
- `--lang`: Language for the task (e.g., `ru` or `en`).
- `--models`: List of models to initialize (e.g., `gemini`, `openai`).
- `--start_dirs`: List of directories for processing (e.g., `/path/to/dir1`).


## Workflow

1. **File Reading**: Finds `.py` and `README.MD` files in the specified starting directories.
2. **Prompt Loading**: Loads prompt files for each role and language from the `src/ai/prompts/developer/` directory.
3. **Request Processing**: Forms requests based on loaded files and sends them to models.
4. **Response Saving**: Saves responses from models to a directory corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).


## Exceptions

Configuration for file and directory exclusions using parameters:
- `exclude_file_patterns`: List of regular expressions to exclude files.
- `exclude_dirs`: List of directories to exclude.
- `exclude_files`: List of files to exclude.


## Logging

Logs are saved using the `logger` library and contain information about the file processing process and the received responses.


## Dependencies

- **Gemini API**: Requires an API key for working with the Gemini model.
- **OpenAI API**: Requires an API key for working with the OpenAI model.