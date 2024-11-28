# WebDriver Executor (executor.py)

```markdown
The `executor.py` file in the `src.webdriver` module implements the `ExecuteLocator` class for interacting with web page elements using Selenium WebDriver.  It manages various actions like navigation, element interaction, attribute retrieval, and message sending based on locator dictionaries.
```

## General Structure and Purpose

The `ExecuteLocator` class is designed to automate actions on a web page based on predefined locator configurations.  These configurations are supplied as dictionaries, which define how to find and interact with elements on the page.

## Key Components and Functionality

1. **Imports:**
   - Imports necessary Selenium WebDriver components, like `webdriver`, `By`, `WebElement`, `WebDriverWait`, `ActionChains`, etc.
   - Imports utility modules (`src.utils`) for string formatting, JSON handling, and logging.
   - Imports custom exceptions for specific errors related to WebDriver operations.

2. **`ExecuteLocator` Class:**
   - **`driver` and `actions`:** Holds a reference to the WebDriver instance and an `ActionChains` object for complex interactions. These are crucial for browser control and element manipulation.
   - **`by_mapping`:** Maps locator strings (like "xpath") to Selenium's `By` constants.  This improves code readability and maintainability.
   - **`__init__`:** Initializes the WebDriver and `ActionChains` objects, preparing the class for use.
   - **`execute_locator`:**  The core method that takes a locator dictionary and performs the specified actions. It handles potentially problematic actions gracefully via optional `continue_on_error`.
   - **`get_webelement_by_locator`:** Locates and returns web elements based on the locator. It utilizes `WebDriverWait` for robust element presence checks and returns `False` if no matching element is found.  Crucially, it can return a *list* of elements if multiple elements are found, accommodating scenarios with multiple matches.
   - **`get_attribute_by_locator`:** Extracts attributes from the located element(s).  This allows for reading data from web elements, like text content or URLs.
   - **`_get_element_attribute`:** A helper method for retrieving a specific attribute from a `WebElement`.
   - **`send_message`:** Simulates user input by sending text to a text field, optionally controlling typing speed.
   - **`evaluate_locator` and `_evaluate`:** These methods handle the logic for evaluating locator attributes, including special handling of placeholders (`%EXTERNAL_MESSAGE%`).
   - **`get_locator_keys`:** A static method for obtaining a list of valid locator keys—useful for validation and understanding supported locator types.

3. **Locator Examples (JSON):**
   - Demonstrates how locator dictionaries are structured.  The dictionaries contain detailed information, including "attribute," "by" (locator type), "selector" (actual locator string), and potentially an "event" to execute (like "click()"). Importantly, the `if_list` option allows the script to either take the first item from a list of results or process all matched elements.


## Functionality Summary

The `ExecuteLocator` class is designed for:

- Locating web elements using various strategies (XPath, ID, CSS).
- Executing actions on those elements (e.g., clicks, sending keys).
- Retrieving attributes of elements (like text, href, etc.).
- Handling error conditions (like elements not found) in a controlled way.

This detailed structure and functionality enable robust and reliable automation of web interactions.


## Error Handling (Implicit)

While not explicitly shown in the code snippet, the presence of `try-except` blocks around crucial methods like `get_webelement_by_locator` and `send_message` suggests comprehensive error handling.  Catching exceptions like `NoSuchElementException` and `TimeoutException` prevents scripts from crashing due to unforeseen conditions.  The `continue_on_error` parameter further enables fault-tolerant execution.

## Dependencies

The `ExecuteLocator` class relies heavily on the Selenium WebDriver library for interacting with browsers and web elements.  It also uses internal utilities from the `src` directory for logging, file handling, and configuration management.


## Usage Example (Illustrative)

```python
# ... imports ...

driver = webdriver.Chrome()
executor = ExecuteLocator(driver)

locator_data = { ... (your locator dictionary) ... }

# Perform actions with 'execute_locator' using locator data
result = executor.execute_locator(locator_data, message="...")

# Process results as needed
```