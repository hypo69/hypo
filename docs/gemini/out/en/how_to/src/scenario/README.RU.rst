rst
How to use the `src.scenario` module
=========================================================================================

Description
-------------------------
The `src.scenario` module automates interactions with suppliers using scenarios defined in JSON files. It extracts and processes product data from supplier websites and synchronizes this information with a database (e.g., PrestaShop).  The module handles reading scenarios, interacting with websites, processing data, logging execution, and orcheStarting the entire process.

Execution steps
-------------------------
1. **Prepare the scenario files:** Create JSON files that describe the supplier's products and their URLs.  These files will be the input for the automation process.  A crucial example is provided in the documentation.

2. **Define the configuration:** Create a configuration object (`s`) containing necessary settings, such as database connection details. This object is passed as an argument to the various functions within the module.

3. **Run the scenario files:** Use the `run_scenario_files` function to process the list of scenario files. This function iterates through the files, loading each, and calling `run_scenario_file` for each.

4. **Execute each scenario file:** The `run_scenario_file` function loads scenarios from each file and iterates through them, calling the `run_scenario` function for each.

5. **Process each scenario:** The `run_scenario` function processes a single scenario. This includes:
    a. Navigating to the specified product URL.
    b. Retrieving a list of product details from the webpage.
    c.  Extracting the required product information.
    d. Creating a product object.
    e. Inserting the product details into the PrestaShop database.
    f. Logging the success or failure of each step in a journal.

6. **Handle errors:**  The module includes error handling for various situations, such as:
    - `FileNotFoundError` if a scenario file or a URL is not found.
    - `JSONDecodeError` if the scenario file format is invalid.
    - `requests.exceptions.RequestException` for issues communicating with web servers.
    - Generic exceptions for any other problems encountered.


7. **Update the execution journal:** The `dump_journal` function records all the steps and results, both successes and failures, into a journal file.


8. **Run the main function:**  The `main` function provides an entry point for running the scenario process. It orcheStartes the loading of the configuration and the scenario files.


Usage example
-------------------------
.. code-block:: python

    import json
    from src.scenario import run_scenario_files

    # Replace with your actual scenario file paths
    scenario_files = ["supplier_data_1.json", "supplier_data_2.json"]

    # Create a configuration object (example).  Crucially, replace with your connection parameters
    config = {
        "db_host": "localhost",
        "db_user": "your_user",
        "db_password": "your_password",
        "db_name": "prestashop_db",
        "supplier_url": "https://example.com" #Example supplier URL
    }
    
    #Run the scenario files.
    run_scenario_files(config, scenario_files)