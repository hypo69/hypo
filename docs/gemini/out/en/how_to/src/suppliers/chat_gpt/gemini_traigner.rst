rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block defines a constant variable named `MODE` and assigns the string value 'dev' to it.  It's likely part of a larger program, setting a mode that controls how the application behaves. This particular code snippet is a simple configuration step.

Execution steps
-------------------------
1. The code defines a constant variable named `MODE`.
2. The string value 'dev' is assigned to the `MODE` variable.

Usage example
-------------------------
.. code-block:: python

    # No direct usage is shown, as the code is only a configuration step.
    # To use, the program will need to access the value of MODE.
    # For example, if MODE is 'dev':
    #
    # if MODE == 'dev':
    #   print("Running in development mode.")
    #
    # Example code showing how to access the variable's value
    # in another part of the larger application
    import os

    # Assuming MODE is defined in a file called 'config.py'
    # import config

    MODE = os.getenv('MODE')

    if MODE == 'dev':
        print("Running in development mode.")

    elif MODE == 'prod':
        print("Running in production mode.")

    else:
        print("Unknown mode.")