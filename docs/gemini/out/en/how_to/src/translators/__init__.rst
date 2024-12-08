rst
How to use this code block
=========================================================================================\n\nDescription
-------------------------
This code block defines a module-level variable named `MODE` and sets its value to the string 'dev'. This variable likely controls the operational mode of the application, potentially used for different configurations (e.g., development, testing, production).

Execution steps
-------------------------
1. The code sets the value of the `MODE` variable to 'dev'.
2. The code defines the variable globally within the scope of the `src.translators` module. This means it's accessible from any other part of the module and any files that import `src.translators`.

Usage example
-------------------------
.. code-block:: python

    import hypotez.src.translators

    current_mode = hypotez.src.translators.MODE
    print(f"The current mode is: {current_mode}")