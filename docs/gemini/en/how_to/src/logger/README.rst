rst
How to use the src.logger module
=========================================================================================

Description
-------------------------
The `src.logger` module provides a flexible logging system for Python applications. It supports console, file, and JSON logging, utilizes the Singleton design pattern, and allows for customization of log levels, formats, and output destinations.  The module includes colorized output for console logs and facilitates logging exceptions.

Execution steps
-------------------------
1. **Import the necessary modules:** Import the `Logger` class from the `src.logger` module and any required modules for handling log colors (e.g., `colorama`).

2. **Create a configuration dictionary:** Define a dictionary (`config`) containing the paths to log files for different log levels (info, debug, errors, JSON).

3. **Initialize the logger:** Instantiate the `Logger` class and call the `initialize_loggers` method, passing the `config` dictionary.  This step configures the logger instances for the specified log destinations.

4. **Log messages:** Use the appropriate logging methods (`info`, `debug`, `error`, `warning`, `success`, `critical`) to log messages at different severity levels. These methods accept the message to log, an optional exception object (`ex`), and options to include exception details (`exc_info`) and to customize colors for console output.

5. **(Optional) Customize colors:** If you need colored output, provide a tuple containing the desired text and background colors. These colors are typically from a library like `colorama`.


Usage example
-------------------------
.. code-block:: python

    import logging
    import colorama
    from src.logger import Logger

    # Configure logger
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }

    # Initialize the logger
    logger: Logger = Logger()
    logger.initialize_loggers(**config)

    # Log messages at different levels
    logger.info('This is an informational message.')
    logger.debug('This is a debug message.')
    try:
        1/0  # Simulate an error
    except ZeroDivisionError as e:
        logger.error('Division by zero error occurred:', exc_info=True)
        logger.error("Exception:", ex=e)


    logger.warning('This is a warning message.')

    # Customize colors (using colorama)
    colorama.init(autoreset=True)
    logger.info('Colored Info Message', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('Colored Error Message', colors=(colorama.Fore.WHITE, colorama.Back.RED))