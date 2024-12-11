rst
How to use the `post_event` function
========================================================================================

Description
-------------------------
This Python code defines functions for posting event details on a Facebook page, likely within a marketing automation or social media management system. It uses Selenium to interact with the Facebook web interface.  The `post_event` function orcheStartes the posting process by calling other functions to input the event title, date, time, description, and potentially other details.  The code utilizes a `Driver` object from a separate library (`src.webdriver.driver`) for browser interaction and loads locators from a JSON file. Error handling and logging are implemented to manage issues during the posting process.

Execution steps
-------------------------
1. **Initialization**: The code loads locators from a JSON file (`post_event.json`) into a `SimpleNamespace` object called `locator`. This JSON file likely contains the unique identifiers (e.g., CSS selectors, XPath expressions) for the input fields on the Facebook page.

2. **`post_title`, `post_date`, `post_time`, `post_description` functions**: These functions take the `Driver` object and the event details (title, date, time, description) as input.  Each function uses `d.execute_locator` to interact with the specific input field on the Facebook page and populate it with the given data.  `post_title`, `post_date`, and `post_time` each return `True` if successful and `None` otherwise, indicating failure. This allows for error handling within the `post_event` function, to check if the steps succeeded.

3. **`post_event` function**: This function takes a `Driver` object and a `SimpleNamespace` called `event` as input.
    * It calls `post_title`, `post_date`, `post_time`, and `post_description` sequentially to send the event details.
    * Importantly, it checks if each function returns `True` before continuing, ensuring a functional workflow.
    * If any of these steps fail, it immediately returns `None`, preventing further execution and providing informative logging through `logger.error`.
    * A crucial step for posting is `d.execute_locator(locator = locator.event_send)`, which triggers the posting action after completing all the details.
    * `time.sleep(30)` introduces a delay to allow Facebook's server time to process the request, which is good practice for avoiding rate-limiting issues.

4. **Error Handling**: The code uses `logger.error` to log any errors encountered during the execution of functions.

Usage example
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from pathlib import Path
    from types import SimpleNamespace

    # Assuming you have a Driver instance initialized
    driver = Driver()

    # Example event details
    event = SimpleNamespace(
        title="Campaign Launch Event",
        start="2024-10-26 10:00",  # format is critical
        description="Details about the event",
        promotional_link="https://example.com/campaign"
    )
    
    if post_event(driver, event):
        print("Event posted successfully!")
    else:
        print("Failed to post event.")

    driver.quit()  # Important: Close the browser after use