hypotez/src/utils/autodoc.py
===========================

.. module:: src.utils
   :platform: Windows, Unix
   :synopsis: Demonstrates the use of a decorator for automatically updating the docstring of a function.

Description:
    This module contains the `autodoc` decorator, which updates the function's documentation string by adding the time of the last function call.
    The decorator is used to automatically update the function's docstring when it is called.
    The decorator wraps the function, updating its docstring before calling it, adding a line with the current time.
    The `time` library is used to get the current time.

Example Usage:
    Example function `example_function`, which uses the `autodoc` decorator. Each time it is called, its docstring is updated, and information about the last time the function was called is added to it.

    Example code:
    ```python
    @autodoc
    def example_function(param1: int, param2: str) -> None:
        """Example function.

        Args:
            param1 (int): First value.
            param2 (str): Second value.
        """
        print(f"Processing {param1} and {param2}")

    example_function(1, "test")
    print(example_function.__doc__)  # Output of the updated docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Output of the updated docstring
    ```


.. automodule:: hypotez.src.utils.autodoc
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: autodoc
   :noindex:
   :show-inheritance:

.. autofunction:: update_docstring
   :noindex:
   :show-inheritance:

.. autofunction:: example_function
   :noindex:
   :show-inheritance: