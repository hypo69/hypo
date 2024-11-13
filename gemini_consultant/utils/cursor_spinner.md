```python
# \file hypotez/src/utils/cursor_spinner.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.utils """
"""
This module provides a utility to show a spinning cursor in the console 
to simulate a loading or waiting process.
"""

import time
import sys

def spinning_cursor():
    """ Generator for a spinning cursor that cycles through |, /, -, \\ symbols.
    
    Yields:
        str: The next symbol in the cursor sequence.
    
    Example:
        >>> cursor = spinning_cursor()
        >>> next(cursor)  # '|'
        >>> next(cursor)  # '/'
        >>> next(cursor)  # '-'
        >>> next(cursor)  # '\\'
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(duration: float = 5.0, delay: float = 0.1):
    """ Shows a spinning cursor in the console for a specified duration.
    
    Args:
        duration (float): How long the spinner should run (in seconds). Defaults to 5.0.
        delay (float): Delay between each spin (in seconds). Defaults to 0.1.
    
    Raises:
        TypeError: if duration or delay are not float.
        ValueError: if duration or delay are not positive.
    
    Example:
        >>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
    """
    if not isinstance(duration, float) or not isinstance(delay, float):
        raise TypeError("Duration and delay must be floats.")
    if duration <= 0 or delay <= 0:
        raise ValueError("Duration and delay must be positive values.")

    spinner = spinning_cursor()
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write('\b')
    except KeyboardInterrupt:
        print("\nSpinner interrupted.")
        
if __name__ == "__main__":
    try:
        print("Spinner for 5 seconds:")
        show_spinner(duration=5.0, delay=0.1)
        print("\nDone!")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

```

**Improvements:**

* **Error Handling:** Added `TypeError` and `ValueError` checks to ensure `duration` and `delay` are valid float values and positive.  This is crucial for robustness.  The `try...except` block in the `if __name__ == "__main__":` section now catches these exceptions and prints a user-friendly error message. This prevents the script from crashing if the user provides incorrect input.


* **Keyboard Interrupt Handling:** Added a `try...except KeyboardInterrupt` block.  This is important because if the user presses Ctrl+C while the spinner is running, the script will now gracefully handle the interruption and print a message ("Spinner interrupted"). Without this, the script would likely crash.


This revised code is more robust and user-friendly.  It's ready to be used in a production environment where you might not have perfect control over user input. Importantly, the error handling and interrupt handling will help prevent unexpected behavior.


**How to run it:**

1.  Save the code as `cursor_spinner.py`.
2.  Make sure you have a Python virtual environment (`venv`) activated (as indicated in the `#!` shebang line).
3.  Run from your terminal:

```bash
python cursor_spinner.py
```

This will start the spinner, and you can press Ctrl+C to stop it. If you run it with `python3` rather than `python` you'll need to ensure the `venv` is set up appropriately.