<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> \ 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/README.MD'>endpoints</A> \ 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/README.MD'>hypo69</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/code_assistant/readme.ru.md'>Русский</A>
</TD>
</TR>
</TABLE>

Вот обновленный текст файла `README.md` для модуля `code_assistant`, который описывает все скрипты (`code_assistant.py`, `make_summary.py`, `onela_bot.py`, `bot_handlers.py`):

---

```rst
.. module:: src.endpoints.hypo69.code_assistant
```

<TABLE>
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> \ 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/README.MD'>endpoints</A> \
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/README.MD'>hypo69</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/code_assistant/README.MD'>English</A>
</TD>
</TR>
</TABLE>

# Code Assistant Module

## Overview

The `Code Assistant` module is a set of tools designed to interact with **Gemini** and **OpenAI** models for processing project source code. It performs tasks such as generating documentation, code review, and test generation based on specified files. Additionally, it includes scripts for creating a `SUMMARY.md` file for documentation compilation and a Telegram bot for handling code-related tasks.

## Key Features

### `code_assistant.py`
- **File Reading**: Reads code from `.py` and `README.MD` files in specified directories.
- **Model Interaction**: Sends code to models for tasks like documentation generation or error checking.
- **Result Generation**: Saves model responses in designated directories for each role.

### `make_summary.py`
- **SUMMARY.md Generation**: Recursively traverses a directory to create a `SUMMARY.md` file for documentation compilation.
- **Language Filtering**: Supports filtering files by language (`ru` or `en`).

### `onela_bot.py` and `bot_handlers.py`
- **Telegram Bot**: A bot for handling code-related tasks, such as sending code snippets for review or generating documentation.
- **Bot Handlers**: Contains handlers for processing bot commands and messages.

## Project Structure

- **Models**: Uses **Gemini** and **OpenAI** models for processing requests.
- **Prompts**: Reads prompts from files in `src/ai/prompts/developer/` (e.g., `doc_writer_en.md`).
- **Files**: Processes `.py` and `README.MD` files in specified directories.

## Usage Examples

### Running with JSON Settings:
```bash
python code_assistant.py --settings settings.json
```

### Running with Explicit Parameters:
```bash
python code_assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Example for Role `code_checker`:
```bash
python code_assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Example for Model `openai`:
```bash
python code_assistant.py --role doc_writer --lang en --models openai
```

## Command-Line Parameters

- `--settings`: Path to a JSON file with settings. Loads parameters from the file.
- `--role`: The role of the model for the task (e.g., `doc_writer`, `code_checker`).
- `--lang`: The language for the task (e.g., `ru` or `en`).
- `--models`: List of models to initialize (e.g., `gemini`, `openai`).
- `--start_dirs`: List of directories to process (e.g., `/path/to/dir1`).

## Workflow

1. **File Reading**: Searches for `.py` and `README.MD` files in specified directories.
2. **Prompt Loading**: Loads role-specific prompts from `src/ai/prompts/developer/`.
3. **Request Processing**: Forms requests based on loaded files and sends them to models.
4. **Response Saving**: Saves model responses in directories corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).

## Exceptions

Configure exceptions for files and directories using parameters:
- `exclude_file_patterns`: List of regex patterns to exclude files.
- `exclude_dirs`: List of directories to exclude.
- `exclude_files`: List of files to exclude.

## Logging

Logs are saved using the `logger` library and contain information about the file processing and model responses.

## Dependencies

- **Gemini API**: Requires an API key for the Gemini model.
- **OpenAI API**: Requires an API key for the OpenAI model.

## Creating a New Role for AI Models

1. **Update `code_assistant.json`**:
   - Add the new role to the list of roles:
     ```json
     "roles": [
       "code_checker",
       ...
     ]
     ```
   - Alternatively, exclude it in `"exclude-roles"`.

2. **Add Role to Translations**:
   - Update the `translations/translations.json` file with the new role.

3. **Create a System Prompt**:
   - Add a new system prompt in `ai/prompts/developer/`.

4. **Create a Command Instruction**:
   - Add a new command instruction in `instructions/`.

---

This `README.md` provides a comprehensive overview of the `code_assistant` module, its scripts, and how to use them effectively.