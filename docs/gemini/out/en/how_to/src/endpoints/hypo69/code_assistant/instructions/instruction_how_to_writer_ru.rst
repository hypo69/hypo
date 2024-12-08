```MD
How to use this code block
=========================================================================================

Description
-------------------------
This code block calculates the factorial of a given non-negative integer. It handles potential errors and provides a clear output.

Execution steps
-------------------------
1. The function `calculate_factorial` takes an integer `number` as input.
2. It checks if the input `number` is non-negative.  If it is negative, it raises a `ValueError` with an appropriate message.
3. If the input is 0, it returns 1 (factorial of 0 is 1).
4. If the input is a positive integer, it initializes a variable `factorial` to 1.
5. It enters a loop that iterates from 1 up to the input `number`.
6. In each iteration, it multiplies the current value of `factorial` by the loop counter.
7. Finally, it returns the calculated `factorial`.

Usage example
-------------------------
.. code-block:: python

    def calculate_factorial(number):
        if number < 0:
            raise ValueError("Input must be a non-negative integer")
        elif number == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            return factorial

    try:
        result = calculate_factorial(5)
        print(f"The factorial of 5 is: {result}")  # Output: The factorial of 5 is: 120

        result = calculate_factorial(-2)
    except ValueError as e:
        print(f"Error: {e}")  # Output: Error: Input must be a non-negative integer