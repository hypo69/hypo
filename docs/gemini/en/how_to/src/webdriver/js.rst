rst
How to use the JavaScript utility functions
===========================================================================================

Description
-------------------------
This Python code provides a class (`JavaScript`) for interacting with a web page using JavaScript within a Selenium WebDriver context.  It offers functions to manipulate DOM elements, retrieve page metadata, and manage browser focus.  Specifically, it allows making hidden elements visible, obtaining document loading status, getting the referrer URL, and the page language, as well as bringing the browser window to the foreground.

Execution steps
-------------------------
1. **Import the necessary modules:** Import the `WebDriver`, `WebElement`, and other required modules, ensuring the `JavaScript` class is accessible.

2. **Create a `JavaScript` object:** Instantiate the `JavaScript` class, passing the Selenium WebDriver instance as an argument to the constructor.

3. **Use the desired method:** Choose the appropriate method based on the desired action. For example:
    * **`unhide_DOM_element(element)`:**  This method modifies the CSS styles of a given WebElement to make it visible.
    * **`ready_state`:** Retrieves the document loading state ('loading' or 'complete').
    * **`window_focus()`:** Brings the browser window to the foreground.
    * **`get_referrer()`:** Obtains the referrer URL.
    * **`get_page_lang()`:** Extracts the language code of the current page.

4. **Handle potential errors:** The `try...except` blocks within each method catch exceptions during JavaScript execution.  Appropriate logging (using the `logger` module) is included to record any errors.

5. **Process the result:** The returned value (e.g., `True` or `False` for `unhide_DOM_element`, the ready state, or a URL) needs to be processed according to the context of the program.  The method returns an appropriate value (often a boolean, string, or None).



Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver import js  # Assuming correct import path

    # ... (your WebDriver setup) ...
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Find the element (replace with your actual element finding)
    element = driver.find_element("xpath", "//your/element/xpath")

    # Create a JavaScript object
    js_utils = js.JavaScript(driver)

    # Make the element visible
    if js_utils.unhide_DOM_element(element):
        print("Element successfully made visible.")
    else:
        print("Failed to make element visible.")

    # Get the document ready state
    readyState = js_utils.ready_state
    print(f"Document ready state: {readyState}")


    # Get the page language
    page_language = js_utils.get_page_lang()
    print(f"Page language: {page_language}")

    #Bring the browser window to the foreground
    js_utils.window_focus()

    # Close the browser
    driver.quit()