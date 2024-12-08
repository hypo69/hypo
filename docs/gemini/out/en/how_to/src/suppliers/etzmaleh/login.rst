rst
How to use the login function
========================================================================================

Description
-------------------------
This Python code defines a function `login` which simulates a login process. The function takes a `Supplier` object (`s`) as input and returns `True` if the login is successful, and `False` otherwise.  It also logs a message indicating that a login attempt has been made.

Execution steps
-------------------------
1. The function `login` takes a `Supplier` object (`s`) as input.
2. It logs a message "Залогинился ..." to the logger.
3. It returns `True`.

Usage example
-------------------------
.. code-block:: python

    from src.logger import logger  # Import the logger
    # ... (Assume you have a Supplier object called 'supplier')
    # Example Supplier object (replace with your actual object)
    class Supplier:
        def __init__(self, name):
            self.name = name

    supplier = Supplier("MySupplier")
    
    def my_login_process():
        # ... (Your other code logic)
        result = login(supplier)
        if result:
            logger.info(f"Login successful for {supplier.name}")
        else:
            logger.error(f"Login failed for {supplier.name}")

    my_login_process()