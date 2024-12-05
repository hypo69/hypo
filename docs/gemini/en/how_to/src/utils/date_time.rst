rst
How to use the date_time module
========================================================================================

Description
-------------------------
This module provides functions for checking if the current time falls within a specified interval, optionally with a timeout.  The `interval` function determines if the current time is within the given interval. The `interval_with_timeout` function extends this by adding a timeout to the interval check, ensuring that the function doesn't block indefinitely. The module also includes a `input_with_timeout` function for getting user input with a timeout.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `datetime`, `time`, `threading` to work with dates, times, and threads.


2. **`TimeoutCheck` class definition:** This class encapsulates the time-checking logic.


3. **`interval` method:** This method checks if the current time is within a specified time interval.
   - It takes `start` and `end` time objects as input to define the interval.
   - It calculates the current time.
   - It handles intervals that cross midnight.
   - It returns `True` if the current time is within the interval, `False` otherwise.


4. **`interval_with_timeout` method:** This method extends `interval` to include a timeout.
   - It creates a separate thread to run the `interval` function.
   - It waits for the thread's result for up to the specified `timeout` (in seconds).
   - If the thread is still active after the timeout, it prints a timeout message and returns `False`.
   - Otherwise, it returns the result of the `interval` function.


5. **`get_input` method:** This method prompts the user for input.


6. **`input_with_timeout` method:** This method gets user input using a thread and a timeout.
    - It creates a separate thread to read user input.
    - It waits for the thread to complete or the timeout occurs.
    - If a timeout occurs, it returns None; otherwise, returns the input.


7. **Main execution block (`if __name__ == '__main__':`)**
   - It creates a `TimeoutCheck` object.
   - It demonstrates how to use `interval_with_timeout` and prints the result.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.utils.date_time import TimeoutCheck
    import time

    timeout_check = TimeoutCheck()

    # Example using interval_with_timeout (checking if it's after 23:00):
    if timeout_check.interval_with_timeout(timeout=5, start=time(23, 0), end=time(6, 0)):
        print("Current time is within the interval (23:00-06:00).")
    else:
        print("Current time is outside the interval (23:00-06:00) or timeout occurred.")


    # Example of input with timeout (try entering input before 5s)
    user_input = timeout_check.input_with_timeout(timeout=5)
    if user_input:
        print(f"User input: {user_input}")
    else:
        print("Timeout occurred while waiting for user input.")

    # Add a delay to see timeout in action in your test
    time.sleep(6) # sleep for 6 seconds
    if timeout_check.interval_with_timeout(timeout=5, start=time(23, 0), end=time(6, 0)):
        print("Current time is within the interval (23:00-06:00).")
    else:
        print("Current time is outside the interval (23:00-06:00) or timeout occurred.")