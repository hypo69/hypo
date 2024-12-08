rst
How to use the Aliexpress module
========================================================================================

Description
-------------------------
This module provides access to AliExpress data using HTTPS (webdriver) and API protocols.  It enables various interactions, including retrieving product information, navigating categories, and generating affiliate links.  Internal modules handle different aspects of the interaction, from data formatting and error handling to GUI elements and complex interaction scenarios.

Execution steps
-------------------------
1. **Import necessary modules:**  Import the required modules from the `aliexpress` package, such as `utils`, `api`, `campaign`, `gui`, `locators`, and `scenarios`.

2. **Initialize connection (webdriver):** If using the webdriver method, initialize a web driver instance, configuring necessary parameters such as browser type, URL, and potentially credentials.

3. **Interact with API:**  If using the API method, use the `api` module functions for making requests, handling responses, and managing authentication.  This could involve sending specific requests (e.g., for product information, affiliate links) and handling potential errors or invalid responses.

4. **Implement scenarios:** Utilize the `scenarios` module to define and execute complex interactions. This might involve combining API calls, GUI interactions, and data processing steps in more intricate operations (e.g., synchronizing products, managing orders, running campaigns).

5. **Utilize utility functions (utils):** The `utils` module provides general utility functions like data formatting, error handling, and logging.  Employ these functions to support any specific data transformation, error management, or logging requirements throughout the interaction flow.

6. **Define GUI elements (gui):** If your interaction requires interacting with GUI elements, the `gui` module provides the necessary tools for manipulating those elements (e.g., handling forms, dialogues, or other visual components).

7. **Locate web elements (locators):** Using the `locators` module, specify precise locations (selectors) for web elements on AliExpress pages.  These locators are essential for automating interactions with the web page using the webdriver.

8. **Execute actions:** Based on the chosen interaction method (webdriver or API), execute actions, such as navigating to product pages, collecting data, or running campaigns.  Ensure appropriate error handling for potential exceptions.

9. **Process responses:** The responses from API calls, or data collected via webdriver, should be parsed and processed to extract relevant information. This may include data formatting, transformation, and validation.

10. **Log results (optional but recommended):** Log the interactions, results, and any encountered issues for debugging and monitoring purposes.


Usage example
-------------------------
.. code-block:: python

    # Example using the API module to fetch product details.
    from aliexpress.api import AliExpressAPI

    api = AliExpressAPI("your_api_key", "your_api_secret")

    try:
        product_data = api.getProductDetails("product_id")
        print(product_data)
    except Exception as e:
        print(f"Error fetching product data: {e}")

    # Example using the webdriver for navigating pages
    from selenium import webdriver
    from aliexpress.locators import product_page_locator

    driver = webdriver.Chrome()
    driver.get("https://www.aliexpress.com")

    try:
        element = driver.find_element(*product_page_locator)
        element.click()  # Simulates clicking on a product
    except Exception as e:
        print(f"Error navigating to product page: {e}")
    finally:
        driver.quit()