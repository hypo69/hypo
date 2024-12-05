rst
How to use this code block
=========================================================================================

Description
-------------------------
This code defines a Python function `add_numbers` that takes two numbers as input and returns their sum.  It utilizes a function `calculate_sum` (presumably from a utility module) to perform the addition.

Execution steps
-------------------------
1. The code imports the `calculate_sum` function from the `src.utils.calculator` module.
2. It defines a function `add_numbers` that accepts two arguments, `a` and `b`.
3. Inside `add_numbers`, it calls `calculate_sum` with `a` and `b` as arguments.
4. The result of `calculate_sum` is stored in the `result` variable.
5. The function returns the calculated `result`.

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