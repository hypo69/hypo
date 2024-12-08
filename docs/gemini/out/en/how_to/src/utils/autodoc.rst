rst
How to use the autodoc decorator
========================================================================================

Description
-------------------------
This Python code defines a decorator `autodoc` that dynamically updates the docstring of a function with the timestamp of its last call.  This decorator automatically adds the time information to the function's docstring each time the function is invoked.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `functools` and `time` modules. `functools.wraps` is used to preserve metadata of the original function. `time` is used to obtain the current time.

2. **Define the `autodoc` decorator:** The `autodoc` decorator takes a function (`func`) as input. It uses `functools.wraps` to preserve the original function's metadata.  A wrapper function (`wrapper`) is created that updates the docstring before calling the original function.

3. **Update the docstring:** Inside the `wrapper`, the `update_docstring` function is called with the original function (`func`) as an argument.  This function retrieves the current timestamp using `time.strftime`.

4. **Add timestamp to docstring:**  The `update_docstring` function checks if a docstring already exists for the function. If one does, it appends the timestamp to the existing docstring. Otherwise, it sets the docstring to the timestamp.

5. **Call the original function:** The `wrapper` function then calls the original function (`func`) with its arguments.

6. **Return the result:** The decorated function returns the result of the original function's execution.

Usage example
-------------------------
.. code-block:: python

    import time
    from hypotez.src.utils.autodoc import autodoc

    @autodoc
    def example_function(param1: int, param2: str) -> None:
        """Example function.

        Args:
            param1 (int): First value.
            param2 (str): Second value.
        """
        print(f"Processing {param1} and {param2}")

    example_function(1, "test")
    print(example_function.__doc__)  # Output the updated docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Output the updated docstring