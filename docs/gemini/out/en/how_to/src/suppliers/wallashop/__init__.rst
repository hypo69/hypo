rst
How to use the wallaShop module
========================================================================================

Description
-------------------------
This module, `src.suppliers.wallashop`, initializes the WallaShop supplier. It primarily sets a mode (`MODE`) and imports the `Graber` class.

Execution steps
-------------------------
1. Defines a constant variable `MODE` with a value of 'dev'. This likely sets the operational mode of the supplier (e.g., development, production).
2. Imports the `Graber` class from the `graber` submodule within `wallashop`. This import is necessary for later use of the `Graber` functionality, such as fetching data or interacting with the WallaShop API.

Usage example
-------------------------
.. code-block:: python

    # Import the module
    import src.suppliers.wallashop as wallaShop

    # Access the mode
    current_mode = wallaShop.MODE
    print(f"Current mode: {current_mode}")

    # Example usage (if Graber functionality is needed)
    # ... (Assuming Graber has a necessary method like 'fetch_data')
    # from src.suppliers.wallashop.graber import Graber
    # graber_instance = Graber()
    # data = graber_instance.fetch_data() # Or other method calls

    # ... (rest of your code that uses the module)