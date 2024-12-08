rst
How to use the scenario_pricelist code block
========================================================================================

Description
-------------------------
This Python code defines a `Mexiron` class for extracting, parsing, and processing product data from various suppliers. It handles data preparation, AI processing (using the Gemini API), and integration with Facebook for product posting.  The code fetches product data from specified URLs, processes it using a generative AI model (Google Gemini), and saves the results, along with reports in HTML and PDF formats.  Crucially, it supports different suppliers through a `Graber` class implementation for each supplier.

Execution steps
-------------------------
1. **Initialization:**
   - The `Mexiron` class is initialized with a Selenium WebDriver instance (`driver`) and an optional `mexiron_name`.
   - Configuration data (`kazarinov.json`) is loaded, determining the storage location.  Error handling is implemented to catch issues during configuration loading.
   - The `export_path` is constructed based on the configuration.
   - An instance of the appropriate `Graber` class for the specified supplier is created based on the URL.
   -  The `GoogleGenerativeAI` model is initialized with an API key, system instructions, and generation configuration. Error handling is included for loading these components.

2. **Product Data Extraction and Parsing:**
   - The `run_scenario` method is called with a list of URLs.
   - For each URL, a relevant `Graber` object is retrieved.
   - The `driver` navigates to the product page URL.
   - The `Graber` object extracts the product fields and returns the product data as a dictionary of fields.
   - The extracted `ProductFields` is converted to a dictionary.
   -  The product data is saved to a JSON file.  Error handling is in place to catch issues during saving.

3. **AI Processing and Translation:**
   - The `process_ai` method takes the list of product dictionaries, sends this data to a generative AI model (Gemini), and processes the response from the model.  Retrial attempts are built-in in case of model errors.
   - The AI output is checked for validity and language specific data.  Error handling is built-in in case of model errors.
   - The processed data (in 'he' and 'ru' languages) is stored as JSON files.  Error handling is provided for issues during saving.

4. **Report Generation and Facebook Posting:**
   - HTML and PDF reports are generated from the processed data using the `ReportGenerator` class.  Error handling is present for report creation.
   - Messages containing the translated product data are posted to Facebook using functions (`post_message_title`, `upload_post_media`, `message_publish`). Error handling is included in the Facebook posting steps.


Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.endpoints.kazarinov.scenarios.scenario_pricelist import Mexiron
    from pathlib import Path

    # Replace with your actual WebDriver setup
    driver = webdriver.Chrome()
    urls_to_process = ["https://morlevi.co.il/someproduct", "https://ksp.co.il/anotherproduct"]

    mexiron_instance = Mexiron(driver)
    
    try:
        success = asyncio.run(mexiron_instance.run_scenario(urls=urls_to_process))
        if success:
            print("Scenario executed successfully.")
        else:
            print("Scenario execution failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()