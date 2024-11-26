```python
## Usage Guide for hypotez/src/endpoints/hypo69/code_assistant/assistant.py

This guide explains how to use the `CodeAssistant` class to process code files, use AI models (currently Gemini), and save the results.

**1. Prerequisites:**

* **Python Environment:** Ensure you have a Python 3.12 environment (`venv/bin/python`) activated.
* **Dependencies:** Install the required packages.  The code uses `gs`, `jjson`, `gemini`, `openai` (if used), and others from `src` directory. Make sure these are properly installed in your environment.  Usually via a `requirements.txt` file managed by a package manager like `pip`.
* **Configuration:**  A configuration file `code_assistant.json` in the `hypotez/src/endpoints/hypo69/code_assistant` directory is crucial. This file likely defines parameters like excluded file patterns, included files, and output directories. It also needs API keys (like `gs.credentials.gemini.onela` and `gs.credentials.openai.assistant_id.code_assistant` for the AI models).
* **Data Files:** Ensure the input code files you want processed exist in the specified start directories.

**2. Running the Script:**

You can run the script either via the command line or by importing and calling the `run` method.

**Command-line execution:**

```bash
python hypotez/src/endpoints/hypo69/code_assistant/assistant.py --role code_checker --lang ru --model gemini --start-dirs .. --start-file-number 1
```
Replace `code_checker`, `ru`, `..` with your desired settings. `start-file-number` is useful for resuming processing after errors.

**Direct Method Call (for more control from another script):**

```python
from hypotez.src.endpoints.hypo69.code_assistant.assistant import CodeAssistant

assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'], start_dirs=['..'], start_file_number=1)
assistant.run()
```

**3. Code Explanation (Key Sections):**


* **`CodeAssistant` Class:**
    * `__init__(self, **kwargs)`: Initializes the assistant with role, language, models, start directories, and loads configuration.
    * `_initialize_models(self, **kwargs)`: Initializes the AI models (currently Gemini).
    * `parse_args()`: Parses command-line arguments.
    * `system_instruction`, `code_instruction`, `translations`: Load necessary instructions and translations. Crucial for proper prompting.
    * `process_files(self, start_file_number: Optional[int] = 1)`: This is the core method.
        * It iterates through files in the `start_dirs`.
        * It filters files based on `include_files`, `exclude_dirs`, `exclude_files`, and exclusion patterns in `config`.
        * It creates a request structure with role, language, file path, instruction, and code.
        * It sends the request to the `gemini_model` (or `openai_model` if configured).
        * It saves the response to the appropriate output directory based on `output_directory` in `config.json` and `role` and the `model_name`. The response's file type depends on your role, e.g., `.md` or `.rst`.
        * `_create_request()`: Builds the request for the AI model.
        * `_yield_files_content()`:  Iterates and filters files efficiently.
        * `_save_response(self, file_path: Path, response: str, model_name: str)`: Crucial for saving the results.  Crucially handles file paths, output directories, and file extensions correctly. It is robust by creating directories if necessary.
        * `_remove_outer_quotes()`: Cleans up the response from the AI, removing extra code blocks if present.


* **`main` Function:**
    * Demonstrates how to run the `CodeAssistant` in a loop with potentially changing configuration to adapt to new roles or languages as requested.

**4. Important Considerations:**

* **Error Handling:** The code includes significant error handling (e.g., using `try...except` blocks) for file reading and AI model interaction.
* **Rate Limiting:** Be aware of rate limits imposed by the AI models.  The `time.sleep(20)` is a placeholder, you might need more/less depending on the model's API and your usage patterns. Increase this if you encounter errors related to rate limiting.
* **Configuration:** The `code_assistant.json` file is critical. Ensure it's correctly formatted and contains all the necessary data.
* **Security:** Treat your API keys as sensitive information and protect them appropriately.


**5. Debugging Tips:**

* **Logging:** The `logger` module is already included, use it to track processing steps and errors.
* **Printing:** The `pprint` function is used for output; adjust the debug print statements in the `process_files` function as needed to monitor the response and requests.  Comment out the `pprint` and `response=True` lines when you are ready to run the code in production to speed things up.
* **File Output:** Inspect the output files in the `docs/gemini` folder to ensure they are in the expected format.  Examine the `export_path` and the output directory structure for correctness.


This comprehensive guide should help you understand and effectively use the `CodeAssistant` class for your coding assistance needs. Remember to adapt the settings based on your specific use case and AI model's constraints.
```