rst
How to use the src.scenario module
========================================================================================

Description
-------------------------
The `src.scenario` module automates interactions with suppliers to extract and process product data. It reads scenarios from JSON files, interacts with supplier websites to fetch product details, processes the data, logs execution steps, and synchronizes the information with a database (like PrestaShop).  The module handles errors and provides a structured workflow for processing multiple scenarios.

Execution steps
-------------------------
1. **Prepare Scenario Files**:  Create JSON files containing supplier product data, URLs, and target database information.  Each file should represent a distinct set of operations to perform.  See the `Example Scenario` section for a sample format.

2. **Create a Settings Object**: Instantiate a `Settings` object.  This object should hold configurations, such as the database connection details. This object is passed as `s` to all functions within the `src.scenario` module.  It may be beneficial to parameterize the instantiation based on the environment (e.g., testing, development, production).

3. **Specify a List of Scenario Files**: Create a list of file paths to the prepared JSON files.

4. **Initiate Data Extraction**: Call `run_scenario_files(s, scenario_files_list)`. This function iterates through the list and processes each file sequentially. This function will call `run_scenario_file` to load and process each file.

5. **Handle Errors**: Implement appropriate error handling (e.g., `try...except` blocks) within `run_scenario_files`, `run_scenario_file`, and `run_scenario` to manage issues like invalid JSON, file not found, or website connectivity problems.  The functions raise specific exceptions for different error types.

6. **Review Execution Logs**: After the module finishes running, analyze the generated logs to track the success or failure of each scenario. The execution logs, stored in a file, provide details for every processed scenario and pinpoint issues.


7. **Analyze Results:** Examine the data in the target database (PrestaShop) to confirm the successful synchronization of the extracted product information. This is crucial for validation of the overall extraction and processing workflow.


Usage example
-------------------------
.. code-block:: python

    import json
    from src.scenario import run_scenario_files, Settings

    # Create a Settings object (replace with your actual settings)
    settings = Settings(db_host='your_db_host', db_user='your_db_user', db_password='your_db_password', db_name='your_db_name')


    # Create a list of scenario files.
    scenario_files = ['path/to/scenario1.json', 'path/to/scenario2.json']


    # Run the scenarios
    run_scenario_files(settings, scenario_files)


    #Example error handling (within the main code block that calls run_scenario_files):
    try:
        run_scenario_files(settings, scenario_files)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except JSONDecodeError as e:
        print(f"Error: Invalid JSON in scenario file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")