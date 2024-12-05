rst
How to use this code block
=========================================================================================

Description
-------------------------
This code defines a function `add_numbers` that takes two numerical arguments, `a` and `b`, and returns their sum.  It leverages a function `calculate_sum` from a module named `src.utils.calculator` to perform the actual addition.

Execution steps
-------------------------
1. The code imports the `calculate_sum` function from the `src.utils.calculator` module.
2. It defines a function called `add_numbers` that accepts two arguments: `a` and `b`.
3. Inside the `add_numbers` function, it calls the `calculate_sum` function with `a` and `b` as arguments.
4. The result returned by `calculate_sum` is assigned to the variable `result`.
5. The function returns the value of `result`.

Usage example
-------------------------
.. code-block:: python

    from src.utils.calculator import calculate_sum

    def add_numbers(a, b):
        result = calculate_sum(a, b)
        return result

    # Example usage
    sum_result = add_numbers(5, 3)
    print(sum_result)  # Output: 8