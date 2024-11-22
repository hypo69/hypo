```rst
utils Module
============

.. module:: hypotez.src.utils.autodoc
    :platform: Windows, Unix
    :synopsis: Demonstration of using a decorator for automatic docstring update of a function.

Description:
    This module contains the `autodoc` decorator, which updates the function's docstring by adding the time of the last function call.
    The decorator is used to automatically update the function's docstring when it is called.

    The decorator wraps the function, updating its docstring before the call, adding a line with the current time.
    The `time` library is used to get the current time.

Example Usage:
    Example of the `example_function`, which uses the `autodoc` decorator. Each time it is called, its docstring is updated, and information about the time of the last function call is added.
    
    Example code:
    ```python
    @autodoc
    def example_function(param1: int, param2: str) -> None:
        "\""Example function.
    
        Args:
            param1 (int): First value.
            param2 (str): Second value.
        "\""
        print(f"Processing {param1} and {param2}")
    
    example_function(1, "test")
    print(example_function.__doc__)  # Output of the updated docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Output of the updated docstring
    ```


Functions
---------

.. autofunction:: hypotez.src.utils.autodoc.autodoc
   :noindex:

.. autofunction:: hypotez.src.utils.autodoc.update_docstring
   :noindex:

.. autofunction:: hypotez.src.utils.autodoc.example_function
   :noindex:


```