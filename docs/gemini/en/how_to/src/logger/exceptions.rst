rst
How to use custom exceptions in the application
=============================================================================================

Description
-------------------------
This Python module defines custom exception classes for handling various error scenarios within the application.  It centralizes exception handling for better error logging and management, extending standard Python exceptions.  This improves the robustness and maintainability of the application. The custom exceptions are specialized for different error types, providing more context than general `Exception` classes.  This enables tailored error handling and logging specific to each exception type (file not found, product field issues, etc.).

Execution steps
-------------------------
1. **Define custom exceptions:** The module defines custom exception classes (`CustomException`, `FileNotFoundError`, `ProductFieldException`, `KeePassException`, etc.) inheriting from base exceptions (e.g., `Exception`, `IOError`).  These classes extend the standard exception handling mechanisms.

2. **Handle original exceptions:** The `CustomException` class is a base class for custom exceptions. It takes an optional `original_exception` parameter, allowing it to capture the original Python exception that triggered the custom one. This enables the application to preserve context and debug information more easily. The `handle_exception` method logs the custom exception with details, including the original exception (if available).  This provides a detailed error traceback for debugging.

3. **Specialized exception classes:** Each custom exception (e.g., `FileNotFoundError`, `KeePassException`) is tailored to specific error types within the application.  These specialized classes enable specific error handling for different parts of the application (files, product fields, database connections, etc.).

4. **PrestaShop specific exceptions:**  The module includes specific classes for PrestaShop WebService errors (`PrestaShopException`, `PrestaShopAuthenticationError`). These classes allow for more informative error handling for PrestaShop interactions. The class `PrestaShopException` captures detailed error messages from PrestaShop (`ps_error_msg`), error codes (`ps_error_code`), and related information (`error_code`), providing more context about the cause of the error.  This is crucial for debugging issues related to PrestaShop WebService interactions.

5. **Error logging:**  The code leverages the `logger` from the `src.logger` module to record both the custom exceptions and any original exceptions that occurred. The log messages include the custom exception information (e.g., message, original exception), making it easier to track down the cause and location of issues.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.logger.exceptions import FileNotFoundError, PrestaShopException

    try:
        # ... some code that might raise an exception ...
        with open("nonexistent_file.txt", "r") as f:
            # ... read from the file ...
            pass
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        # ... handle the file not found error ...
    except PrestaShopException as e:
        print(f"PrestaShop error: {e.msg}, PrestaShop error code: {e.ps_error_code}")
        # ... handle the PrestaShop error ...


    try:
        # ... code that might raise a PrestaShop Authentication error
        # ...
    except PrestaShopAuthenticationError as e:
        # Handle the specific authentication error
        print(f"PrestaShop authentication failed: {e}")