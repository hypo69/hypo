# hypotez/src/logger/beeper.py

## Overview

This module provides a system for generating auditory signals (beeps) based on different log levels. It allows for customization of beep frequencies and durations, and includes a silent mode for disabling beeps.

## Table of Contents

* [Overview](#overview)
* [BeepLevel Enum](#beeplevel-enum)
* [BeepHandler Class](#beephandler-class)
* [Beeper Class](#beeper-class)
* [silent_mode Function](#silent-mode-function)


## BeepLevel Enum

### `BeepLevel`

**Description**: An enumeration defining different levels of auditory signals, each corresponding to a specific melody.

**Values**:

- `SUCCESS`: A short melody for successful events.
- `INFO`: A short beep for informational events.
- `INFO_LONG`: A longer beep for informational events.
- `ATTENTION`: A longer beep for attention-requiring events.
- `WARNING`: A short melody for warnings.
- `DEBUG`: A combination of beeps for debug messages.
- `ERROR`: A long beep for error events.
- `LONG_ERROR`: A very long beep for critical errors.
- `CRITICAL`: A combined beep for critical events.
- `BELL`: A short, repeating melody for bell-like events.


## BeepHandler Class

### `BeepHandler`

**Description**: A class responsible for handling the selection and emission of beeps based on log levels.


**Methods**:

#### `emit`

**Description**: Selects and emits the appropriate beep based on the provided log `record`.

**Parameters**:

- `record` (dict): A dictionary containing log level information.

**Raises**:

- `Exception`: If an error occurs during beep emission.


#### `play_sound`

**Description**: Plays a beep with a specific frequency and duration.

**Parameters**:
- `frequency` (int): The frequency of the beep in Hz.
- `duration` (int): The duration of the beep in milliseconds.

**Raises**:

- `Exception`: If an error occurs during beep generation.


#### `play_default_sound`

**Description**: Plays a default beep if no specific beep is defined.

**Returns**:

- None



## Beeper Class

### `Beeper`

**Description**: A class responsible for managing beeps, including silent mode.

**Attributes**:

- `silent` (bool): A flag indicating whether silent mode is enabled. Defaults to `False`.


**Methods**:

#### `beep`

**Description**: Emits an auditory signal based on the specified level.

**Parameters**:

- `level` (BeepLevel | str, optional): The level of the event. Defaults to `BeepLevel.INFO`.
- `frequency` (int, optional): The frequency of the beep. Defaults to `400`.
- `duration` (int, optional): The duration of the beep. Defaults to `1000`.

**Returns**:

- `None`

**Raises**:


- `Exception`: If an error occurs during beep emission.


## silent_mode Function

### `silent_mode`

**Description**: A decorator that allows the silencing of beeps.

**Parameters**:

- `func`: The function to decorate.

**Returns**:

- A wrapped function that checks for silent mode before calling the original function.

**Raises**:

- None


**Note**: This documentation reflects the code provided, including comments and docstrings.  The `...` in the original code signifies omitted sections; these parts would need to be included to complete the documentation.  Additionally, there are multiple uses of comments like `@todo` and `@details` not standard Python comments,  which would be better handled as Markdown format within the documentation.  Finally, the `note_freq` dictionary (and associated functions) were not documented.  Complete documentation of those would require more information from the source code.