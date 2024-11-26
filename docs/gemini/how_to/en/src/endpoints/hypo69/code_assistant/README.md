# Code Assistant Usage Guide

This guide explains how to use the `Code Assistant` tool to process code files and generate documentation, perform code checks, or generate tests using Gemini and OpenAI models.

## Prerequisites

- Python 3.x
- Necessary Python libraries (installed via `requirements.txt`)
- API keys for Gemini and/or OpenAI (if applicable)


## Running the Code Assistant

The `Code Assistant` is invoked from the command line using `assistant.py`.  Several options are available, allowing you to customize the execution parameters.

### Using a Configuration File

The recommended method is to use a configuration file (e.g., `settings.json`). This file should contain the necessary parameters.

```bash
python assistant.py --settings settings.json
```

Example `settings.json`:

```json
{
  "role": "doc_writer",
  "lang": "en",
  "models": ["gemini", "openai"],
  "start_dirs": ["/path/to/dir1", "/path/to/dir2"],
  "exclude_file_patterns": ["test_*.py"],
  "exclude_dirs": ["temp_dir"],
  "exclude_files": ["README.md"]
}
```

### Running with Explicit Parameters

You can also specify parameters directly on the command line.

```bash
python assistant.py --role doc_writer --lang ru --models gemini --start_dirs /path/to/project_dir
```


**Important Parameters:**

* **`--settings`**: Path to a JSON configuration file.  **Highly recommended** for managing parameters.
* **`--role`**: The desired role for the model (e.g., `doc_writer`, `code_checker`).  Crucial for choosing the appropriate prompts.
* **`--lang`**: The language for processing (e.g., `ru`, `en`).  Used for prompts.
* **`--models`**: List of models to use (`gemini`, `openai`, or both).
* **`--start_dirs`**:  List of directories containing code files to process.
* **`--exclude_file_patterns`**:  List of file patterns to exclude (using regular expressions).
* **`--exclude_dirs`**: List of directories to exclude.
* **`--exclude_files`**:  List of specific files to exclude.


### File Handling

The assistant looks for `.py` and `README.md` files within the specified `start_dirs`.  Files matching the `exclude_*` patterns will be skipped.


## Prompt Files

The script reads prompts from files in the `src/ai/prompts/developer/` directory.  The file names should indicate the role and language (e.g., `doc_writer_en.md`).  Make sure these files are properly formatted for the corresponding model.


## Output Files

The results from the models are saved in directories matching the role and model, for example, `docs/raw_rst_from_<model>/<lang>/`.


## Error Handling and Logging

The script uses a logging library (`logger`) for debugging information.  Error conditions are handled with exceptions, and log messages help diagnose issues with files, directories, or model responses.  Refer to the logging documentation for more detail.

## Example Scenarios

- **Generate documentation:** Specify `doc_writer` as the role, the target language, and the directory containing the code.
- **Run code checks:** Specify `code_checker` as the role and the directory to analyze.
- **Generate tests:** (Add details on how to achieve this if applicable)


Remember to install the required libraries and set up API keys if needed.  Consult the `README` file for any further specific instructions.


```