#! /usr/bin/python
﻿## \file src/webdriver/_examples/_example_executor.py
## \file /src/webdriver/_examples/_example_executor.py
# -*- coding: utf-8 -*-
""" Extend the Driver Class
<pre>
src.webdriver.excecutor
│
├── Imports
│   ├── selenium.webdriver (webdriver.Chrome)
│   ├── src.webdriver.executor (ExecuteLocator)
│   ├── src.settings (gs)
│   └── src.logger.exceptions (ExecuteLocatorException)
│
├── main() Function
│   ├── Create WebDriver Instance
│   │   └── Calls: webdriver.Chrome
│   ├── Create ExecuteLocator Instance
│   │   └── Calls: ExecuteLocator
│   ├── Simple Locator Example
│   │   └── Calls: locator.execute_locator
│   ├── Complex Locator Example
│   │   └── Calls: locator.execute_locator
│   ├── Error Handling Example
│   │   └── Calls: locator.execute_locator
│   ├── send_message Example
│   │   └── Calls: locator.send_message
│   ├── Multi Locator Example
│   │   └── Calls: locator.execute_locator
│   ├── evaluate_locator Example
│   │   └── Calls: locator.evaluate_locator
│   ├── Exception Handling Example
│   │   └── Calls: locator.execute_locator
│   └── Full Test Example
│       └── Calls: locator.execute_locator
│
└── Driver Cleanup
    └── Calls: driver.quit
</pre>
@dotfile webdriver//executor.dot
"""

from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
from src.logger.exceptions import ExecuteLocatorException

def main():
    # Create WebDriver instance (e.g., Chrome)
    driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
    driver.get("https://example.com")  # Navigate to the website

    # Create an instance of ExecuteLocator
    locator = ExecuteLocator(driver)

    # Simple example of creating an instance and using methods
    print("Simple example of creating an instance and using methods")

    # Simple locator to get an element by XPath
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page title"
    }

    # Execute the locator
    result = locator.execute_locator(simple_locator)
    print(f"Result of executing simple locator: {result}")

    # Example of using different events and attributes
    print("\nExample of using different events and attributes")

    # Locator for sending a message and getting an attribute
    complex_locator = {
        "product_links": {
            "attribute": "href",
            "by": "XPATH",
            "selector": "//a[contains(@class, 'product')]",
            "event": None,
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Getting the product link"
        },
        "pagination": {
            "ul": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//ul[@class='pagination']",
                "event": "click()",
                "if_list":"first","use_mouse": False,
                "mandatory": True,
                "locator_description": "Click on pagination"
            },
            "->": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
                "event": "click()",
                "if_list":"first","use_mouse": False,
                "mandatory": True,
                "locator_description": "Click on the next page"
            }
        }
    }

    # Execute locator with different events
    result = locator.execute_locator(complex_locator)
    print(f"Result of executing complex locator: {result}")

    # Example of error handling and continuing on errors
    print("\nExample of error handling and continuing on errors")

    try:
        locator.execute_locator(complex_locator, continue_on_error=True)
    except ExecuteLocatorException as ex:
        print(f"An error occurred: {ex}")

    # Example of using `send_message`
    print("\nExample of using `send_message`")

    # Locator for sending a message to a text field
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name='search']",
        "attribute": None,
        "event": "%SEARCH%",
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Sending a search query"
    }

    # Send a message using the send_message method
    message = "Buy a new phone"
    result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
    print(f"Result of sending message: {result}")

    # Example of using a list of locators
    print("\nExample of using a list of locators")

    # Locator for multiple elements
    multi_locator = {
        "by": ["XPATH", "XPATH"],
        "selector": ["//button[@id='submit']", "//input[@id='username']"],
        "attribute": ["textContent", "value"],
        "event": ["click()", "send_keys('user')"],
        "if_list":"first","use_mouse": [True, False],
        "mandatory": [True, True],
        "locator_description": ["Click the submit button", "Enter username"]
    }

    # Execute locator with multiple elements
    results = locator.execute_locator(multi_locator)
    print(f"Results of executing multiple locators: {results}")

    # Example of `evaluate_locator`
    print("\nExample of using `evaluate_locator`")

    # Locator for evaluating an attribute
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name='description']",
        "attribute": "content",
        "event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page meta-description"
    }

    # Evaluate the locator and get the attribute
    attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
    print(f"Attribute value: {attribute_value}")

    # Example of exception handling
    print("\nExample of exception handling")

    # Example of handling exceptions when executing a locator
    try:
        locator.execute_locator(simple_locator)
    except ExecuteLocatorException as ex:
        print(f"An error occurred during locator execution: {ex}")

    # Full test example
    print("\nFull test example")

    # Test locator example
    test_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page title"
    }

    # Execute the test locator
    result = locator.execute_locator(test_locator)
    print(f"Result of executing test locator: {result}")

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()

