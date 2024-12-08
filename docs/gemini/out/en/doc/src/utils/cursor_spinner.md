# hypotez/src/utils/cursor_spinner.py

## Overview

This module provides a utility for displaying a spinning cursor in the console to indicate a loading or waiting process. It uses a generator function to cycle through different characters, allowing for a visually engaging progress indicator.

## Functions

### `spinning_cursor`

**Description**: This function acts as a generator, producing a sequence of characters ('|', '/', '-', '\\') in a loop.  It's designed to be used with `show_spinner` for creating the animated spinner effect.

**Yields**:
- `str`: The next character in the spinner sequence.


### `show_spinner`

**Description**: This function displays a spinning cursor in the console for a given duration. It utilizes the `spinning_cursor` function to generate the characters for the animated spinner.

**Parameters**:
- `duration` (float): The desired duration of the spinner animation (in seconds). Defaults to 5.0.
- `delay` (float): The time interval (in seconds) between each spinner character update. Defaults to 0.1.


**Example Usage**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
```

**Implementation Details**:

1. Creates a generator object (`spinner`) from `spinning_cursor`.
2. Calculates the end time based on the `duration`.
3. Enters a loop that continues as long as the current time is less than the end time.
4. Prints the next character from the `spinner` generator to `sys.stdout`.
5. Uses `sys.stdout.flush()` to immediately display the character, ensuring a smooth animation.
6. Introduces a delay using `time.sleep(delay)`.
7. Clears the previous character using `sys.stdout.write('\b')` to prevent character stacking.

**Raises**:
-  No exceptions are explicitly raised.


## Example Usage (in `if __name__ == "__main__":`)

This section demonstrates how to use the `show_spinner` function within a script.  It displays a 5-second spinner and then prints a "Done!" message to the console.
```python
print("Spinner for 5 seconds:")
show_spinner(duration=5.0, delay=0.1)
print("\\nDone!")
```
```
```