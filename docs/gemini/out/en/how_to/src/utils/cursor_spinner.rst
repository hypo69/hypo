rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines functions for creating and displaying a spinning cursor in a console.  The `spinning_cursor` function generates a sequence of symbols ('|', '/', '-', '\\') that can be used to visually indicate a process that is taking some time. The `show_spinner` function displays the spinning cursor for a specified duration, pausing between each symbol to create the animation effect.

Execution steps
-------------------------
1. The `spinning_cursor()` function is a generator that continuously yields the next symbol in the sequence ('|', '/', '-', '\\'). This function is essential for generating the symbols.
2. The `show_spinner()` function takes the `duration` (in seconds) and `delay` (in seconds) as input.
3. It initializes a `spinner` generator from the `spinning_cursor()` function.
4. It calculates the `end_time` based on the provided `duration`.
5. It enters a `while` loop that continues as long as the current time is less than the `end_time`.
6. Inside the loop, it prints the next symbol from the `spinner` generator to the console.
7. It uses `sys.stdout.flush()` to immediately print the symbol to the console rather than buffering.
8. It pauses for the specified `delay` using `time.sleep()`.
9. It prints a backspace ('\b') character to overwrite the previous symbol with the next, creating the animation effect.

Usage example
-------------------------
.. code-block:: python

    import time
    from hypotez.src.utils.cursor_spinner import show_spinner

    print("Spinner for 3 seconds:")
    show_spinner(duration=3.0, delay=0.2)
    print("\nDone!")