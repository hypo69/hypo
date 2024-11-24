.. automodule:: hypotez.src.logger
   :members:
   :undoc-members:
   :show-inheritance:

Module Name
==========

The `hypotez.src.logger` module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application. The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

Classes
-------

.. autoclass:: hypotez.src.logger.SingletonMeta
   :members:

.. autoclass:: hypotez.src.logger.JsonFormatter
   :members:

.. autoclass:: hypotez.src.logger.Logger
   :members:

Functions
---------

.. autofunction:: hypotez.src.logger.__init__
   :noindex:

.. autofunction:: hypotez.src.logger._configure_logger
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.initialize_loggers
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.log
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.info
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.success
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.warning
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.debug
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.error
   :noindex:
   :show-inheritance:

.. autofunction:: hypotez.src.logger.critical
   :noindex:
   :show-inheritance:


Parameters for the Logger
-------------------------

The `Logger` class accepts several optional parameters for customizing the logging behavior.

- **Level**: Controls the severity of logs that are captured. Common levels include:
  - `logging.DEBUG`: Detailed information, useful for diagnosing issues.
  - `logging.INFO`: General information, such as successful operations.
  - `logging.WARNING`: Warnings that do not necessarily require immediate action.
  - `logging.ERROR`: Error messages.
  - `logging.CRITICAL`: Critical errors that require immediate attention.

- **Formatter**: Defines how the log messages are formatted. By default, messages are formatted as `'%(asctime)s - %(levelname)s - %(message)s'`. You can provide a custom formatter for different formats, such as JSON.

- **Color**: Colors for the log messages in the console. The colors are specified as a tuple with two elements:
  - **Text color**: Specifies the text color (e.g., `colorama.Fore.RED`).
  - **Background color**: Specifies the background color (e.g., `colorama.Back.WHITE`).

The color can be customized for different log levels (e.g., green for info, red for errors, etc.).


File Logging Configuration (`config`)
-------------------------------------

To log messages to a file, you can specify the file paths in the configuration.

.. code-block:: python
   :linenos:

   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }

The file paths provided in `config` are used to write logs to the respective files for each log level.


Example Usage
------------

.. code-block:: rst

   Example Usage for Logger
   ~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: python
       :linenos:

       # ... (Import necessary modules, including colorama if needed)
       # ... (Define your config dictionary)
       logger: Logger = Logger()
       config = {
           'info_log_path': 'logs/info.log',
           'debug_log_path': 'logs/debug.log',
           'errors_log_path': 'logs/errors.log',
           'json_log_path': 'logs/log.json'
       }
       logger.initialize_loggers(**config)
       logger.info('This is an info message')

       # ... (Other logging calls)