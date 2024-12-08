rst
How to use the hypotez/src/suppliers/ivory/__init__.py file
========================================================================================

Description
-------------------------
This file, `hypotez/src/suppliers/ivory/__init__.py`, is an initialization module for the 'ivory' supplier within the 'hypotez' project. It primarily sets a configuration variable `MODE` to 'dev' and imports the `Graber` class from a submodule named `graber`.  This suggests that the `Graber` class will be used to perform some sort of data gathering or processing.

Execution steps
-------------------------
1. Sets the global variable `MODE` to the string value 'dev'. This likely defines a runtime mode, possibly for development or testing purposes.  The specific use of this mode is not explicitly shown here.
2. Imports the `Graber` class from the `graber` submodule within the `ivory` supplier. This step prepares the `Graber` class for use.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.ivory import Graber

    # Example usage (assuming Graber has necessary methods)
    graber_instance = Graber()
    # ... (Further code to initialize or use graber_instance) ...
    # Example:
    data = graber_instance.fetch_data()  # Example method call
    print(data)