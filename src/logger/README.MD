
## Overview

### logger.py

This file contains the core logging functionalities. It provides a flexible logging interface that allows developers to categorize log messages by severity. The supported log levels include:

- **SUCCESS**: Represents successful operations.
- **INFO**: General informational messages.
- **ATTENTION**: Important alerts that require user attention.
- **WARNING**: Indications of potential issues.
- **DEBUG**: Detailed debug information.
- **ERROR**: Errors encountered during execution.
- **LONG_ERROR**: Extended notifications for persistent errors.
- **CRITICAL**: Severe issues that may require immediate action.
- **BELL**: Standard notification sound.

### exceptions.py

This module defines custom exceptions to manage errors related to logging operations. It allows for clear and descriptive error handling, enabling developers to easily identify and rectify issues within the logging framework.

### beeper.py

The Beeper module handles sound notifications. It allows the application to emit different sounds based on the current logging level, providing auditory feedback that can be particularly useful in environments where visual monitoring is not practical.

## Usage

To utilize the Logger Module in your application, you can import the necessary components and configure the logger as needed.

### Example Usage

```python
from logger import Logger, BeepLevel

logger = Logger()

# Example logging messages
logger.log(BeepLevel.INFO, "This is an info message.")
logger.log(BeepLevel.ERROR, "An error occurred!")
```

### Sound Notifications

You can enable sound notifications for specific log levels:

```python
from beeper import Beeper, BeepLevel

async def notify_user():
    await Beeper.beep(level=BeepLevel.SUCCESS)  # Emits a success beep
    await Beeper.beep(level=BeepLevel.WARNING)  # Emits a warning beep

if __name__ == '__main__':
    import asyncio
    asyncio.run(notify_user())
```

## Features

- **Auditory Feedback**: Get immediate sound notifications for different logging levels, enhancing real-time monitoring.
- **Custom Exceptions**: Clear error handling using defined exceptions for robust logging operations.
- **Configurable Logging Levels**: Easily manage log messages and their severities.
- **Silent Mode**: Ability to toggle sound notifications on or off for a distraction-free experience.

## TODO

- Enhance asynchronous beep functionality to handle potential conflicts.
- Add more configurable options for sound frequency and duration.
- Improve logging functionality with additional features based on user feedback.

