```python
"""
Usage Guide for hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py

This module provides functionality for extracting, parsing, and processing product data from various suppliers,
preparing data for AI processing, and integrating with Facebook for product posting.

Key Classes:

- Mexiron: The main class handling the entire process.

Functions:

- run_scenario: Executes the main scenario logic, including data extraction, AI processing, and Facebook posting.
- get_graber_by_supplier_url: Selects the appropriate graber based on the supplier URL.
- convert_product_fields: Converts product fields into a dictionary format suitable for AI input.
- save_product_data: Saves individual product data to a JSON file.
- process_ai: Passes product data to the AI model for processing and translation.
- post_facebook: Posts product data to Facebook.
- create_report: Generates reports (HTML and PDF).


How to use Mexiron:

1. **Initialization:** Create a Mexiron instance, passing a `Driver` object (Selenium WebDriver) and an optional custom name.

   ```python
   from src.webdriver import Driver
   from scenario_pricelist import Mexiron
   driver = Driver()
   mexiron = Mexiron(driver, "my_mexiron_instance") 
   ```
2. **Configuration:** The `Mexiron` constructor loads configuration from `kazarinov.json`.  Verify this file exists in the expected location (`gs.path.endpoints / 'kazarinov'`) and contains a valid configuration.  The `kazarinov.json` file (as shown in examples in the code) should be a properly formatted JSON structure with the `storage` field as expected.  Missing or incorrectly formatted configurations lead to errors and the program will exit.


3. **Running the Scenario:** Call the `run_scenario` method, providing URLs of product pages or a list of URLs.  You can optionally specify other parameters if needed.


   ```python
   urls = ["https://morlevi.co.il/product_page_1", "https://ksp.co.il/product_page_2"]
   await mexiron.run_scenario(urls=urls)  
   ```
4. **Error Handling:** The code includes robust error handling using `try...except` blocks and `logger` messages to catch issues with fetching pages, parsing data, or AI processing.  The logging is important for debugging and understanding where problems occur.  Critically, the code has `...` to indicate where additional error handling or logging is needed.  These placeholders should be filled to provide more context for errors.

**Crucial Considerations:**

- **Error Handling:**  The `run_scenario` function and related parts have important `logger` statements to capture failures.  Complete the `...` sections with proper error logging and potentially alternative actions (e.g., retries).
- **AI Model Output Validation:** The `process_ai` function has a critical loop to handle potential issues with the AI model returning invalid results. This is crucial, as AI models can sometimes produce faulty translations. The code attempts to re-prompt the model a few times before giving up. Robust validation of the AI model output is paramount.
- **Facebook Posting:** Ensure the necessary Facebook authentication is set up correctly and that your environment has the necessary packages (including those for Facebook interaction) installed to utilize the Facebook posting functionality.
- **Configuration File (`kazarinov.json`):** Verify the JSON file and the `gs` module are set up correctly for the environment you intend to use.


**Important Notes:**

- The code relies heavily on other modules (`src`, `gs`, etc.). Ensure those modules are correctly imported and configured in your environment.
- Be sure the graber classes for different suppliers (`MorleviGraber`, `KspGraber`, etc.) are correctly defined and functioning for the target sites.
- The code anticipates specific formatting from the product pages. The `convert_product_fields` function needs to be tailored precisely to the website layout to extract the required data.


This guide provides a high-level overview; you might need to consult the individual parts of the code, especially the graber classes, for finer details on each component's functionalities and parameters.
```