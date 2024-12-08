rst
How to Use the Code Assistant
========================================================================================

Description
-------------------------
The `Code Assistant` is a tool for interacting with Gemini and OpenAI models to process source code. It performs tasks such as generating documentation, code checking, and generating tests based on code from specified directories.  It reads Python files (`.py`) and README files (`.md`), processes them using chosen models (Gemini and/or OpenAI), and saves the results in designated directories.

Execution steps
-------------------------
1. **Prepare Configuration:** Create a JSON configuration file (e.g., `settings.json`) to define parameters such as the desired `role` (e.g., `doc_writer`), `language` (`en` or `ru`), `models` to use (`gemini`, `openai`, or both), and a list of `start_dirs` (directories containing the code to process).


2. **Specify Parameters (Optional):**
   - If you have a settings file, run the script with `--settings settings.json`.
   - If you want to specify parameters individually, use command-line arguments like `--role doc_writer`, `--lang en`, `--models gemini openai`, and `--start_dirs /path/to/dir1 /path/to/dir2`.  These arguments allow fine-grained control over the process.  Note that `--start_dirs` specifies the directories to read code from.


3. **Execute the Script:** Run the script `assistant.py` with the appropriate parameters.

4. **Process Files:** The script reads Python files (`.py`) and README files (`.md`) within the specified directories.

5. **Load Prompts:**  It loads prompts specific to the chosen `role` and `language` from files in the `src/ai/prompts/developer/` directory.

6. **Send Requests to Models:** The script sends formatted requests to the chosen language models (Gemini and/or OpenAI) incorporating the loaded code and prompts.

7. **Save Responses:** The results from the models are saved in directories organized by `role`, `model`, and `language` for later use or review.


Usage example
-------------------------
.. code-block:: bash

    python assistant.py --settings settings.json

.. code-block:: bash

    python assistant.py --role doc_writer --lang en --models gemini openai --start_dirs /path/to/project1 /path/to/project2

This example uses the `settings.json` file.  A more detailed example using command-line parameters is shown above.  Be sure to replace `/path/to/project1` and `/path/to/project2` with the actual paths to your project directories.