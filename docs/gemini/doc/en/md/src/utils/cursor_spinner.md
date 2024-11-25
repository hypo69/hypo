# hypotez/src/utils/cursor_spinner.py

## Overview

This module provides a utility for displaying a spinning cursor in the console, simulating a loading or waiting process. It defines two functions: `spinning_cursor` and `show_spinner`.


## Functions

### `spinning_cursor`

**Description**: A generator that yields characters ('|', '/', '-', '\\') in a cyclical pattern, simulating a spinning cursor.

**Returns**:
- `str`: The next symbol in the cursor sequence.


### `show_spinner`

**Description**: Displays a spinning cursor in the console for a specified duration.

**Parameters**:
- `duration` (float): The duration (in seconds) for which the spinner should run. Defaults to 5.0.
- `delay` (float): The delay (in seconds) between each spinner symbol update. Defaults to 0.1.


**Example Usage**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Shows a spinner for 3 seconds
```

**Raises**:
- No exceptions are explicitly raised.

## Module Attributes

### `MODE`

**Description**: A string variable, currently set to 'dev'.  Its purpose isn't clear from the provided code.  Its use should be documented in a later phase of documentation development.


```