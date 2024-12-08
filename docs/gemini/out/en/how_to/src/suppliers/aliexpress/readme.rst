rst
How to use the Aliexpress Module
========================================================================================

Description
-------------------------
This module provides functionalities for interacting with the AliExpress supplier platform using both webdriver and API methods.  It encompasses several internal modules for various tasks, such as API interaction, campaign management, GUI interactions, element location, and complex scenario definition.

Execution steps
-------------------------
1. **Initialization:** Import the necessary modules from the `aliexpress` package.  This step varies depending on the specific module you need to use.

2. **API Interaction (if needed):**
   - If using the `api` module, authenticate with the AliExpress API using appropriate credentials.
   - Initiate API requests to fetch specific data (affiliate links, product descriptions, etc.) using the available API methods.

3. **Webdriver Interaction (if needed):**
   - Initialize a WebDriver instance, specifying the required driver (e.g., Chrome, Firefox).
   - Navigate to the relevant AliExpress web pages using WebDriver methods.
   - Locate elements on the web pages using locators defined in the `locators` module.
   - Perform actions like clicking buttons, filling forms, or extracting data using WebDriver commands.

4. **Data Handling (if needed):**
   - Process the data received from API requests or WebDriver interactions using functions in the `utils` module, which might include functions for data formatting, validation, and logging.

5. **Campaign Management (if needed):**
   - Utilize methods in the `campaign` module to create, update, track, and analyze AliExpress campaigns.

6. **GUI Interaction (if needed):**
   - Leverage the `gui` module to use graphical components for interaction with AliExpress functionalities.

7. **Scenario Execution (if needed):**
   - Call functions or execute scripts defined within the `scenarios` module for more complex, multi-step processes.


Usage example
-------------------------
.. code-block:: python

    # Example using API interaction
    from aliexpress.api import AliExpressAPI

    # Replace with actual API credentials
    api_client = AliExpressAPI("your_api_key", "your_api_secret")
    product_details = api_client.getProductDetails(product_id="12345")
    print(product_details)


    # Example using webdriver (requires Selenium setup)
    from selenium import webdriver
    from aliexpress.locators import ProductPageLocators

    driver = webdriver.Chrome()  # Or other webdriver
    driver.get("https://www.aliexpress.com/item/...")
    product_title = driver.find_element(ProductPageLocators.PRODUCT_TITLE).text
    print(product_title)
    driver.quit()