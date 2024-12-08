# hypotez/src/logger/beeper.py

## Overview

This module provides a beeper functionality for generating audio signals (beeps) based on different log levels. It allows customizing the beep's frequency and duration, and supports different types of beeps for various log events.  The module includes a silent mode for disabling the beeping functionality,  and a flexible system for handling different types of log events.


## Classes

### `BeepLevel`

**Description**: An enumeration defining different beep levels, each associated with a specific melody.  Different events trigger different melodies (e.g., success, error, warning).

**Members**:

- `SUCCESS`: Plays a specific melody.
- `INFO`: Plays a specific melody.
- `ATTENTION`: Plays a specific melody.
- `WARNING`: Plays a specific melody.
- `DEBUG`: Plays a specific melody.
- `ERROR`: Plays a specific melody.
- `LONG_ERROR`: Plays a specific melody.
- `CRITICAL`: Plays a specific melody.
- `BELL`: Plays a specific melody.


### `BeepHandler`

**Description**: A class responsible for emitting beeps based on log records. It maps log levels to specific beep types and plays the appropriate sound.  It utilizes the `BeepLevel` enumeration.

**Methods**:

- `emit(self, record)`: Emits a beep based on the `level` attribute of the provided `record`. This method tries to handle different log levels by calling the appropriate functions, and a default sound for unrecognized levels.  Includes error handling using `ex`.


### `Beeper`

**Description**: A class managing the beeper's functionality. It provides static methods for emitting beeps based on log levels and includes a silent mode for disabling beeps.

**Methods**:

- `beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None`: Emits a beep with the specified `level`, `frequency`, and `duration`.  Supports both `BeepLevel` enums and strings for log level input.  Uses error handling and `silent` mode effectively.
- This method internally handles mapping string input to the `BeepLevel` for more flexibility.

**Attributes**:

- `silent`: A boolean flag that controls whether the beeper should be silent.


## Functions

### `silent_mode(func)`

**Description**: A decorator function that controls the "silent mode" for the decorated function.  When silent mode is enabled, beeping is skipped.

**Parameters**:

- `func`: The function to decorate.

**Returns**:
- The decorated function, which checks for the silent mode flag.  Includes appropriate error handling using `ex`.


## Variables

### `MODE`

**Description**: A string variable to control the beeper's behavior. Currently set to 'dev'.

### `note_freq`

**Description**: A dictionary that maps musical note names to their corresponding frequencies in Hz. Used for generating the beeps.


## Modules

### `asyncio`

**Description**: Used for asynchronous operations in the program.

### `winsound`

**Description**: Used to generate the beep sounds.

### `time`

**Description**: Used for pausing between beeps.

### `enum`

**Description**: Used for creating the `BeepLevel` enum.

### `typing`

**Description**: Used for type hinting.