# hypotez/src/utils/date_time.py

## Overview

This module provides functions for checking if the current time falls within a specified interval, with optional timeout handling.  It's useful for scheduling tasks that should only run during particular hours, like late-night maintenance.  The module also includes a method for getting user input with a timeout.


## Classes

### `TimeoutCheck`

**Description**: This class encapsulates functions for checking time intervals and handling potential timeouts.

**Methods**

#### `interval`

**Description**: Checks if the current time falls within a specified time interval.

**Parameters**

- `start` (time): The start time of the interval (default is 23:00).
- `end` (time): The end time of the interval (default is 06:00).

**Returns**

- `bool`: `True` if the current time is within the interval, `False` otherwise.


#### `interval_with_timeout`

**Description**: Checks if the current time falls within a specified time interval, waiting for a response with a timeout.

**Parameters**

- `timeout` (int): The maximum time in seconds to wait for the interval check. Defaults to 5.
- `start` (time): The start time of the interval (default is 23:00).
- `end` (time): The end time of the interval (default is 06:00).

**Returns**

- `bool`: `True` if the current time is within the interval and the response is received within the timeout. Returns `False` if the timeout occurs.

#### `get_input`

**Description**: Prompts the user for input.

**Returns**
None

#### `input_with_timeout`

**Description**: Waits for user input with a specified timeout.

**Parameters**

- `timeout` (int): The maximum time in seconds to wait for user input. Defaults to 5.

**Returns**

- `str | None`: The user's input if provided within the timeout, otherwise `None`.



## Functions

There are no functions in this module other than those within the `TimeoutCheck` class.