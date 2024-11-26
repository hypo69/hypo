How to use the `src.scenario` module

This module automates interaction with suppliers using JSON-based scenarios.  It adapts the process of extracting and processing product data from supplier websites and synchronizing it with your database (e.g., PrestaShop).

**1. Understanding the Scenario Files**

Scenario files are JSON documents defining how to interact with a supplier's website to gather product data.  Each file likely contains multiple scenarios.  A scenario describes a specific product category, including:

* **`url`**: The URL of the product category page on the supplier's website.
* **`name`**: A descriptive name for the product category.  Crucially, this is often used as a key to identify the scenario within the JSON file.
* **`presta_categories`**:  A crucial part. This dictionary specifies the PrestaShop categories where products from this scenario should be stored.
    * `default_category`: The primary PrestaShop category.
    * `additional_categories`: An optional list of secondary PrestaShop categories where products might also be placed.

**Example Scenario (JSON):**

```json
{
    "scenarios": {
        "Mineral+MoisturizersForFaceMineralsAndPlantExtracts": {
            "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
            "name": "Mineral+MoisturizersForFaceMineralsAndPlantExtracts",
            "presta_categories": {
                "default_category": 11245,
                "additional_categories": [11288]
            }
        }
    }
}
```

**2. Running the Module**

The module provides functions to load, process, and store the results:

* **`run_scenario_files(scenario_files_list)`**: This function takes a list of file paths to JSON scenario files and executes them sequentially.  It's the entry point for running multiple categories at once.

* **`run_scenario_file(scenario_file)`**: This function loads the JSON data from a single scenario file and then calls `run_scenario` for each scenario in that file.

* **`run_scenario(scenario)`**:  This function is the core logic for a single scenario:
    1. It extracts the `url` from the `scenario`.
    2. It fetches the product data from the corresponding URL on the supplier's website.
    3. It uses the `presta_categories` information to correctly categorize the products in your PrestaShop database.  This is crucial for proper organization.

* **`dump_journal(journal)`**: This function logs the execution details (success, errors, warnings) into a file.  This is essential for debugging and tracking progress.  The `journal` parameter contains details of the entire process.

* **`main()`**: The main function where you'll initiate the process.  It calls `run_scenario_files` and handles potential errors.

**3.  Key Steps in using the `src.scenario` module**

1. **Prepare Scenario Files:** Create JSON files following the structure demonstrated in the example.
2. **List File Paths:** Create a list of paths to these JSON files (`scenario_files_list`).
3. **Run the Script:** Call the `main()` function of the module, passing the file list as an argument.
```python
# Example usage in your main script (e.g., your app.py or similar)
from your_module import main  # Replace your_module with the actual module name
scenario_files = ["path/to/scenario1.json", "path/to/scenario2.json"]
main(scenario_files)
```
4. **Review the Journal:** Examine the log file created by the module (`dump_journal`) to review the execution progress, identify any failures, and pinpoint errors in the scenarios.

**Important Considerations:**

* **Error Handling:** The `run_scenario` function should include robust error handling (e.g., `try...except` blocks) to catch issues like network problems, invalid JSON data, or problems with the supplier's website.
* **Data Extraction:** The code needs mechanisms for extracting product data from the supplier's website (e.g., using libraries like `BeautifulSoup` or `requests`).
* **PrestaShop Integration:** The module should provide clear methods for inserting or updating product data in your PrestaShop database (e.g., using the PrestaShop API if available).
* **Data Validation:** Implement validation steps for the product data to prevent issues when importing it into your database.


This revised guide provides a more structured and actionable understanding of how to use the `src.scenario` module. Remember to replace placeholders like `"path/to/scenario1.json"` with actual file paths.