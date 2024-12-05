rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines several variables within a module. These variables likely store metadata about the module, including its version number, name, documentation, details, type annotations, and author information.  The variables are important for maintaining a consistent record of the module's identity.

Execution steps
-------------------------
1. The code sets the `__version__` variable to "3.12.0.0.0.4", indicating the version of the module or package.
2. The `__doc__`, `__details__`, `__name__`, and `__annotations__` variables are defined. These store descriptive information about the module.
3. The `__author__` variable is set to 'hypotez '.


Usage example
-------------------------
.. code-block:: python

    import hypotez.src.suppliers.aliexpress.api.version as version

    print(version.__version__)
    print(version.__doc__)
    print(version.__details__)
    print(version.__author__)