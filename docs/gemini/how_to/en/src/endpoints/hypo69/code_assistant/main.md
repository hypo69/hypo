How to use the `main.py` code assistant

This Python script, `main.py`, is a command-line interface (CLI) for a code assistant.  It allows you to process codebases using different roles (e.g., code checker, documentation writer), languages, and AI models.

**Basic Usage:**

The script can be run in two ways:

1.  **Using a settings file:** Specify the path to a JSON configuration file containing the assistant's settings.  This is the recommended approach for complex configurations.

    ```bash
    python main.py --settings settings.json
    ```

    Create a `settings.json` file (e.g.,):

    ```json
    {
      "role": "doc_writer",
      "lang": "ru",
      "models": ["gemini", "openai"],
      "start_dirs": ["/path/to/your/code/dir1", "/path/to/your/code/dir2"]
    }
    ```

2.  **Using command-line arguments:** Provide parameters directly on the command line.

    ```bash
    python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
    ```

**Detailed Parameter Explanation:**

*   `--settings <path_to_settings_file>`: Specifies a JSON file containing the assistant's configuration.  If this is provided, the other parameters (e.g., `--role`, `--lang`) can be omitted in the command line.

*   `--role <role_name>`: Defines the assistant's role.  Valid choices are `code_checker`, `code_analyzer`, `doc_writer`, and `tests_creator`. Defaults to `en`.

*   `--lang <language_code>`: Specifies the language for the assistant. Valid choices are `ru` (Russian) and `en` (English).  Defaults to `en`.

*   `--models <model_name>`:  Specifies the list of AI models to use.  Valid choices are `gemini` and `openai`. Use multiple models with space-separated values: `--models gemini openai`.

*   `--start_dirs <directory_path>`: Specifies one or more directories to process.  Multiple directories can be provided using multiple `--start_dirs` parameters.


**Important Considerations:**

*   **Error Handling:** The script checks if the settings file exists. If not, it prints an error message and exits.
*   **`settings.json`:**  The `settings.json` file structure must match the expected input of the `CodeAssistant` class.  Refer to the `CodeAssistant` class definition (not shown in this snippet) for the required keys.
*   **`start_dirs`:** Make sure to provide correct directory paths to the codebases you want to process.
*   **`CodeAssistant` Class:**  The `CodeAssistant` class, which is likely in a file called `assistant.py`, is essential for the functionality.  This code snippet shows how to call it, but it doesn't reveal the internal logic of the `CodeAssistant` class.


**Example Usage Scenarios (command line):**

* **Generating documentation for Russian code:**
```bash
python main.py --role doc_writer --lang ru --models gemini --start_dirs /path/to/my/project
```

* **Checking English code using both models:**
```bash
python main.py --role code_checker --lang en --models gemini openai --start_dirs /path/to/other/project
```

**Next Steps:**

To fully understand how to use this code, you need to:

1.  **Inspect the `CodeAssistant` class:** This class contains the core logic for processing files and interacting with the specified AI models.
2.  **Modify the `settings.json` file:**  Ensure the data structure and values match the expected input for the `CodeAssistant` constructor.
3.  **Install any necessary libraries:**  `argparse`, `json`, and any other libraries used by the `CodeAssistant` class.


This comprehensive guide should help you use the `main.py` script effectively. Remember to replace placeholders like `/path/to/your/code/dir1` with the actual paths to your code directories. Remember to adapt the examples to fit your specific requirements and code structure.