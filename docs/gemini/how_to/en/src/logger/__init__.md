How to use the `hypotez/src/logger` module

This module provides logging functionality and defines various exceptions for `hypotez`.

**Contents:**

* **`logger`:** A logging object for use throughout the application.
* **`ExecuteLocatorException`:** Exception raised when issues occur during the execution locator process.
* **`DefaultSettingsException`:** Exception raised when there are problems with default settings.
* **`CredentialsError`:** Exception for issues with authentication credentials.
* **`PrestaShopException`:** Exception raised for errors encountered while interacting with the PrestaShop API.
* **`PayloadChecksumError`:** Exception raised if a payload's checksum does not match expectations.


**Example Usage:**

```python
import logging
from hypotez.src.logger import logger, ExecuteLocatorException

def my_function():
    try:
        # ... some code that might raise an exception ...
        result = perform_operation() 
        return result
    except ExecuteLocatorException as e:
        logger.error("Failed to locate execution: %s", e)
        # Add more specific logging or error handling here
        raise  # Re-raise the exception for further processing if needed
    except Exception as e:  # Handle other potential exceptions
        logger.exception("An unexpected error occurred: %s", e)
        # Add your specific error handling logic
        raise


# Example usage
if __name__ == "__main__":
    try:
       my_function()
    except Exception as e:
       print(f"Program terminated due to error: {e}")

```

**Explanation:**

1. **Import necessary classes:** The example imports `logger` and `ExecuteLocatorException`.

2. **`try...except` block:** The code is enclosed in a `try...except` block to gracefully handle potential exceptions.

3. **Logging specific exceptions:** The `except ExecuteLocatorException` block logs a more specific error message using the `logger.error` method.   Crucially, it includes the exception details in the log.

4. **Logging unexpected errors:** The `except Exception` block catches all other exceptions, logs a general error message using `logger.exception`, and includes the full traceback for detailed debugging.

5. **Re-raising exceptions:**  The `raise` statement in the `ExecuteLocatorException` block (and potentially the other `except` blocks) re-raises the exception. This is important in a production environment.  Error handling at that level is crucial for maintaining the program's response to a problem.

**Important Considerations:**

* **Logging Levels:** The `logger` object uses standard Python logging levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). Adjust the logging level as needed.
* **Configuration:** The way the `logger` is configured (e.g., log file, console output) depends on the rest of your application's setup.  Refer to the Python `logging` module documentation for details.
* **Error Handling:**  The specific error handling and logging within `my_function` should be tailored to the code's logic and expected errors.
* **Custom Exceptions:** The provided custom exceptions (`ExecuteLocatorException`, etc.) help categorize errors.  You should leverage these to ensure logging is relevant to the error type and for better debugging.

This example demonstrates best practices for using the logger and handling exceptions within the application. Remember to adapt the specific error handling and log messages based on the context of your code.