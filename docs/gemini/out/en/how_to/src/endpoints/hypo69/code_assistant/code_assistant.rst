rst
How to use the CodeAssistant class
=========================================================================================

Description
-------------------------
This Python code defines a `CodeAssistant` class for processing code files using an AI model (currently Gemini).  It reads code files, formats requests for the AI model, processes the responses, and saves the results to a specified directory. The class is designed to be robust, handling errors and offering flexibility in file selection and model utilization. It also handles command-line arguments for configuration.  It includes functions for creating requests, processing files, saving responses, and removing unwanted characters from the AI's output. The class uses logging to record errors and inform the user about the progress.

Execution steps
-------------------------
1. **Initialization:** The `CodeAssistant` class is initialized with parameters like the desired role (e.g., `code_checker`), language, and a list of AI models to use.  It loads configurations from a JSON file (`code_assistant.json`) and initializes the chosen AI models (e.g., Gemini).

2. **Request Creation:** The `_create_request` method constructs a structured request for the AI model.  It includes the code content, desired output language, and role information.  The request is formatted to provide the AI with sufficient context for accurate processing.

3. **File Handling:** The `_yield_files_content` method iterates through files in specified directories, excluding those based on configured patterns and specified in a configuration file. It efficiently handles large directories. It handles potential errors reading the files, logging issues as they occur.

4. **File Sending and Processing:** The `process_files` method iterates through the files.
    - It checks if the file should be skipped based on a configurable start file number.
    - For each valid file, it sends the code to the AI model for processing via the `gemini_model.ask` method.
    - It handles the model response, removing unwanted characters or additional formatting via `_remove_outer_quotes` if needed.
    - It saves the response to the appropriate file in a designated output directory, creating the necessary directories if they do not exist.   Specific file extensions are determined based on the role.
    - It logs any errors that occur during file processing or response handling.

5. **Argument Parsing:** The `parse_args` method defines command-line arguments for the user to configure the role, language, models, and directories to process.

6. **Main Function Loop:** The `main` function orcheStartes the overall process. It loads configurations from a file, and initializes and executes the `CodeAssistant` for each configuration combination of language and roles. It also includes error handling and a signal handler to gracefully exit on interrupts.

Usage example
-------------------------
.. code-block:: python

    # Example usage (run from the command line)
    python code_assistant.py --role doc_writer_rst --lang en --model gemini --start-dirs src