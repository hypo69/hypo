rst
How to use the scenario_executor
========================================================================================

Description
-------------------------
This code block, represented by a graph, outlines the execution flow of a scenario executor. It describes how the system handles a list of scenario files, loads and runs each scenario, and interacts with a PrestaShop system to create products.  The process includes error handling for invalid scenario file lists and failures during scenario execution.

Execution steps
-------------------------
1. **Supplier Instance** provides a list of scenario files.

2. **Scenario Files List Validation**: The system validates if the provided list of scenario files is valid.

3. **Valid List**: If the list is valid, the executor proceeds to run the scenario files.

4. **Invalid List**: If the list is invalid, the executor enters error handling and returns an appropriate error message.

5. **Iterate Through Each Scenario File**:  The executor iterates through each scenario file in the valid list.

6. **Run Scenario File**: Each scenario file is processed.

7. **Load Scenarios**: The system loads the scenarios defined within the current file.

8. **Iterate Through Each Scenario**: The executor iterates through each scenario loaded from the file.

9. **Run Scenario**: Each individual scenario is executed.

10. **Navigate to URL**:  The scenario execution involves navigating to a specific URL.

11. **Get List of Products**:  The system retrieves a list of products from the specified URL.

12. **Iterate Through Products**: The executor iterates through each product in the retrieved list.

13. **Navigate to Product Page**: The system navigates to the product page of each product.

14. **Grab Product Fields**: Relevant product information (fields) are extracted from the product page.

15. **Create Product Object**: A product object is constructed based on the extracted data.

16. **Insert Product into PrestaShop**: The product object is inserted into the PrestaShop database.

17. **Success**: If the product insertion into PrestaShop is successful, a success signal is indicated.

18. **Failure**: If the product insertion fails, the system enters error handling.

19. **Error Handling**:  The executor handles errors encountered during any step in the process. This includes invalid file lists, loading scenarios, running scenarios, or database insertion errors.

20. **Update Journal**: On success, the system updates the execution journal.

21. **Return True/False**: The executor returns a boolean value indicating the overall success or failure of executing all scenarios in the file.


Usage example
-------------------------
.. code-block:: python

    # Example assuming a 'scenario_executor' module
    from hypotez.src.scenario.scenario_executor import ScenarioExecutor

    # Replace with actual scenario file list
    scenario_files = ["scenario1.json", "scenario2.json"]

    executor = ScenarioExecutor()
    success = executor.execute(scenario_files)

    if success:
        print("All scenarios executed successfully.")
    else:
        print("Errors encountered during scenario execution.")