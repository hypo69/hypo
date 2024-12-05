How to use this code block
=========================================================================================

Description
-------------------------
This code defines locators for elements on an HTML page using a JSON format.  Each key in the JSON represents a locator for a specific field, with details on how to find and interact with the corresponding web element using Selenium or similar WebDriver tools.  These locators specify the element's attributes, the method used to locate it (e.g., XPath), and optional actions to take (e.g., clicking, capturing a screenshot).

Execution steps
-------------------------
1. **Identify the desired element:**  Choose the JSON key that represents the field you want to interact with on the web page.  For example, `close_banner` represents the element that closes a banner.

2. **Analyze the locator:** Carefully examine the details within the chosen JSON key, particularly:
    * **`attribute`**: Determine the attribute to retrieve from the web element (e.g., `innerText`, `src`, `href`). If `null` or `false`, the entire web element is returned.
    * **`by`**:  Understand the method used to locate the element (e.g., `XPATH`, `CSS_SELECTOR`).
    * **`selector`**: Inspect the XPath or CSS selector string to ensure it precisely identifies the intended element.
    * **`if_list`**:  Determine how to handle multiple matching elements. `first` selects the first, `all` selects all, `last` selects the last, and specific numbers or ranges (`1,2`, `[1,3,5]`) are also possible.  Ensure the selector appropriately targets only the desired item.
    * **`use_mouse`**: If `true`, mouse actions (like clicks) will be performed; otherwise, no mouse interaction will be executed.
    * **`event`**: Specifies actions to take on the element *before* retrieving the `attribute`. For example, `click()`, `screenshot()`.  Be aware the action is performed *before* accessing the `attribute`.
    * **`mandatory`**: Indicates whether this locator is required.  If `true`, errors will result if the element isn't found; otherwise, the process will proceed to the next item.

3. **Handle Lists (if applicable):** If the `attribute`, `by`, `selector`, `event`, `if_list`, etc. are lists, those items within the list are considered sequentially. In cases with `event` and `attribute` lists, actions are performed according to the order in the list, and the corresponding `attribute` is retrieved afterward.

4. **Implement with WebDriver:** Construct your WebDriver code to use the provided locator data.  Use the `by` value to create a `By` object and use the `selector` to perform the element selection. Access the specified `attribute` if applicable, and perform any specified `event` action (like clicks) using the retrieved web element.

5. **Error Handling (if `mandatory` is `true`):**  Implement error handling to catch cases where the element can't be located due to a missing element or an invalid selector.


Usage example
-------------------------
.. code-block:: python

    import json
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Load the locator data
    with open('locators.json', 'r') as f:
        locators = json.load(f)


    # Example usage for the "id_supplier" locator
    driver = webdriver.Chrome()
    driver.get("your_website_url")
    locator_data = locators['id_supplier']

    try:
        element = driver.find_element(By.XPATH, locator_data['selector'])
        id_supplier_value = element.get_attribute(locator_data['attribute'])
        print(f"ID Supplier value: {id_supplier_value}")
    except Exception as e:
        print(f"Error retrieving id_supplier: {e}")

    driver.quit()