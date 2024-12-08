rst
How to use the affiliate_links_shortener_scenario script
========================================================================================

Description
-------------------------
This Python script defines a function `get_short_affiliate_link` that automates the process of shortening affiliate links using a web browser. It utilizes a `Driver` object (presumably from a separate WebDriver library) to interact with a website's UI, inputting the original URL, clicking a button, extracting the shortened link, and verifying its validity.  The script handles potential errors by logging them and, optionally, raising exceptions.

Execution steps
-------------------------
1. **Load Locators:** The script loads locators for UI elements (input field, button, shortened link display) from a JSON file (`affiliate_links_shortener.json`).  This JSON file defines the selectors needed to identify these elements on the website.  This file must exist in the expected path relative to the script's location.

2. **Input URL:** The `get_short_affiliate_link` function takes a `Driver` object (`d`) and the original URL (`url`) as input. It uses the `execute_locator` method to insert the `url` into the designated input field on the website.

3. **Trigger Shortening:** It then uses `execute_locator` to click the button that triggers the shortening process.

4. **Wait for Update:** The script waits for 1 second (`d.wait(1)`) to allow the webpage to update and generate the shortened link.

5. **Retrieve Shortened Link:** The script extracts the shortened link using `execute_locator` and stores it in the `short_url` variable.

6. **Error Handling (Critical):** The script checks if the `short_url` is empty. If it's empty, it logs an error (using `logger.error`) indicating that the shortening process failed for the given URL.  Importantly, it avoids stopping the entire process by not raising an exception here, but logs the error for further investigation.

7. **Open New Tab:** A new tab is opened in the browser containing the shortened link using `execute_script`.

8. **Switch to New Tab:** The script switches the focus to the newly opened tab (`d.switch_to.window(d.window_handles[-1])`).

9. **Verify Shortened Link:** The `startswith()` method is used to verify if the `current_url` in the new tab starts with the expected "https://..." prefix.

10. **Error Handling (Link Validation):** If the shortened link is invalid (e.g., pointing to an error page), an error is logged (`logger.error`) and the invalid tab is closed and the script switches back to the original tab.  Again, stopping the script for an invalid URL is avoided by logging the error, potentially allowing the program to continue processing other URLs.

11. **Close New Tab & Return:** The script closes the new tab and returns to the original tab. The shortened URL (`short_url`) is returned.


Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver  # Assuming this import is available
    from hypotez.src.suppliers.aliexpress.scenarios.affiliate_links_shortener_scenario import get_short_affiliate_link


    # Example usage:
    driver = Driver()  # Create a WebDriver instance
    url_to_shorten = "https://example.com/long-affiliate-link"

    try:
        shortened_url = get_short_affiliate_link(driver, url_to_shorten)
        print(f"Shortened URL: {shortened_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()  # Close the browser