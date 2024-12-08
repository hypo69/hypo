rst
How to use the Logger module
=========================================================================================

Description
-------------------------
This module provides a singleton logger that handles logging to the console, files, and JSON.  It supports various log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL) and custom formatting, including colorization for console output. The `Logger` class is implemented as a singleton to ensure a single instance is used throughout the application.  It allows for flexible configuration of log file destinations and formats.


Execution steps
-------------------------
1. **Import the module:**
   Import the `Logger` class from the `logger` module.

2. **Create a Logger instance:**
   Instantiate the `Logger` class.  This creates (or retrieves) the single logger instance.


3. **Initialize loggers:**
   Call the `initialize_loggers` method on the logger instance. This method is crucial for setting up the different log destinations (console, info file, debug file, error file, JSON file). Pass the paths to the desired log files.

   Example:

   ```python
   logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')
   ```


4. **Log messages:**
   Use the various logging methods (e.g., `logger.info()`, `logger.debug()`, `logger.error()`, `logger.success()`, etc.) to log messages at different severity levels.  Pass the message text as the first argument.  Optional arguments allow for exception information (`exc_info`) and colorization.

   Example:

   ```python
   logger.info('This is an info message.')
   logger.warning('This is a warning message', exc_info=True)
   logger.error('This is an error message', ex=Exception('Some Error'))
   ```

5. **Configure the logging format (optional):**
    The module provides a `JsonFormatter` for creating JSON log entries. You can specify this formatter when initializing loggers in step 3.  This formatter is used for the JSON log file.


Usage example
-------------------------
.. code-block:: python

    import logging
    import colorama
    from hypotez.src.logger.logger import Logger

    # Create a Logger instance
    logger = Logger()

    # Initialize loggers with file paths
    logger.initialize_loggers(
        info_log_path='info.log',
        debug_log_path='debug.log',
        errors_log_path='errors.log',
        json_log_path='log.json'
    )

    try:
        # Example of logging an error message
        raise Exception("Example error occurred")
    except Exception as ex:
        logger.error("An error occurred", ex, exc_info=True)


    #Example of logging with colored output in the console
    logger.info("This is an info message with color", colors=colorama.Fore.GREEN)
    logger.debug("This is a debug message", colors=(colorama.Fore.MAGENTA, colorama.Back.YELLOW))


    #Additional example showing how to specify specific color
    logger.warning("This is a warning", colors=colorama.Fore.RED)