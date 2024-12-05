rst
How to use this code block
=========================================================================================

Description
-------------------------
This code defines a function `add_numbers` that calculates the sum of two numbers.  It utilizes a function `calculate_sum` from a module `src.utils.calculator` to perform the addition.

Execution steps
-------------------------
1. The code imports the `calculate_sum` function from the `src.utils.calculator` module.
2. It defines a function `add_numbers` that takes two arguments, `a` and `b`.
3. Inside `add_numbers`, it calls the `calculate_sum` function, passing `a` and `b` as arguments.
4. The result returned by `calculate_sum` is assigned to the variable `result`.
5. The function `add_numbers` returns the calculated `result`.

Usage example
-------------------------
.. code-block:: python

    from src.utils.calculator import calculate_sum

    def add_numbers(a, b):
        result = calculate_sum(a, b)
        return result

    # Example usage
    num1 = 5
    num2 = 10
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")