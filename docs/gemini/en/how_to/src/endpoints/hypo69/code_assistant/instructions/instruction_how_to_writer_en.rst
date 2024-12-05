How to use this code block
=========================================================================================

Description
-------------------------
This code block defines a function to calculate the factorial of a non-negative integer.  It uses recursion to achieve this.

Execution steps
-------------------------
1. The function `factorial` is defined, taking an integer `n` as input.
2. It checks if `n` is equal to 0. If it is, it returns 1 (the factorial of 0 is 1).
3. If `n` is greater than 0, it recursively calls `factorial` with `n-1` and multiplies the result by `n`.

Usage example
-------------------------
.. code-block:: python

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    # Example usage
    result = factorial(5)
    print(result)  # Output: 120