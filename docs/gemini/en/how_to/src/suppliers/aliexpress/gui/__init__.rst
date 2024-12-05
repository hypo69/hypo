rst
How to use this code block
=========================================================================================\n\nDescription
-------------------------
This Python code block defines a variable named `MODE` and assigns the string 'dev' to it.  This variable likely represents a mode for the application, in this case, a development mode. This mode might be used for configuration purposes, selecting different behavior based on its value.


Execution steps
-------------------------
1. The code block initializes a string variable named `MODE`.
2. It assigns the literal string value 'dev' to the `MODE` variable.
3. The value of `MODE` will be available for later use in the application.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.gui import MODE

    if MODE == 'dev':
        print('Running in development mode.')
    elif MODE == 'prod':
        print('Running in production mode.')
    else:
        print('Unknown mode.')