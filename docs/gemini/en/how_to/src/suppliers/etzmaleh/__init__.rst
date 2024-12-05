rst
How to use the etzmaleh module
========================================================================================

Description
-------------------------
This module initializes the `etzmaleh` supplier, specifically setting a development mode. It also imports the `Graber` class from the `graber` submodule.

Execution steps
-------------------------
1. Sets the `MODE` variable to 'dev'. This likely controls how the supplier interacts with the system (e.g., data sources, logging levels).
2. Imports the `Graber` class from the `graber` submodule. This makes the functionality of the `Graber` class available for use in other parts of the application.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.etzmaleh import Graber

    # Example usage (assuming Graber needs additional initialization):
    graber_instance = Graber()
    # ... Perform operations using graber_instance ...

    # Example using the MODE variable (if needed elsewhere):
    supplier_mode = __import__("hypotez.src.suppliers.etzmaleh").MODE
    print(f"Current supplier mode: {supplier_mode}")