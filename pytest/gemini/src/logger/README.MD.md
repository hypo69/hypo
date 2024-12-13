```python
import pytest
import logging
from hypotez.src.logger import Logger, SingletonMeta, JsonFormatter
import os
from colorama import Fore, Back

# Fixture for Logger instance
@pytest.fixture
def logger_instance():
    """Provides an instance of the Logger class."""
    return Logger()

# Fixture for log file paths
@pytest.fixture
def log_paths(tmpdir):
    """Provides temporary log file paths."""
    return {
        'info_log_path': str(tmpdir.join('info.log')),
        'debug_log_path': str(tmpdir.join('debug.log')),
        'errors_log_path': str(tmpdir.join('errors.log')),
        'json_log_path': str(tmpdir.join('log.json'))
    }

# Test for SingletonMeta metaclass
def test_singleton_meta():
    """Verify that the SingletonMeta ensures only one instance of a class."""
    class TestClass(metaclass=SingletonMeta):
        pass

    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 is instance2, "SingletonMeta should return the same instance."

# Test for JsonFormatter
def test_json_formatter():
    """Verify that JsonFormatter produces valid JSON log messages."""
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name='test',
        level=logging.INFO,
        pathname='test.py',
        lineno=10,
        msg='Test Message',
        args=(),
        exc_info=None
    )
    formatted_message = formatter.format(record)
    assert isinstance(formatted_message, str), "JsonFormatter should return a string."
    assert '"message": "Test Message"' in formatted_message, "Formatted message should contain the log message."

# Test for _configure_logger
def test_configure_logger(logger_instance, log_paths):
    """Verify the _configure_logger function creates a logger with correct settings."""
    log_path = log_paths['info_log_path']
    logger = logger_instance._configure_logger('test_logger', log_path)
    assert isinstance(logger, logging.Logger), "Should return a logging.Logger instance"
    assert logger.level == logging.DEBUG, "Default logging level should be DEBUG"
    assert len(logger.handlers) == 1, "Logger should have one handler"
    assert isinstance(logger.handlers[0], logging.FileHandler), "Handler should be a FileHandler"
    assert logger.handlers[0].baseFilename == log_path, "FileHandler should point to the correct log path"


def test_configure_logger_custom_level(logger_instance, log_paths):
        """Verify the _configure_logger function creates a logger with custom level."""
        log_path = log_paths['info_log_path']
        logger = logger_instance._configure_logger('test_logger', log_path, level=logging.ERROR)
        assert logger.level == logging.ERROR, "Custom logging level should be ERROR"


def test_configure_logger_custom_formatter(logger_instance, log_paths):
    """Verify the _configure_logger function creates a logger with a custom formatter."""
    log_path = log_paths['info_log_path']
    custom_formatter = logging.Formatter('%(message)s')
    logger = logger_instance._configure_logger('test_logger', log_path, formatter=custom_formatter)
    assert logger.handlers[0].formatter == custom_formatter, "Custom formatter should be set"
    

def test_configure_logger_custom_mode(logger_instance, log_paths):
    """Verify the _configure_logger function creates a logger with a custom file mode."""
    log_path = log_paths['info_log_path']
    logger = logger_instance._configure_logger('test_logger', log_path, mode='w')
    assert logger.handlers[0].mode == 'w', "Custom mode should be set to 'w'"

# Test for initialize_loggers
def test_initialize_loggers(logger_instance, log_paths):
    """Verify that initialize_loggers sets up console, file, and json loggers correctly."""
    logger_instance.initialize_loggers(**log_paths)
    assert logger_instance.console_logger is not None, "Console logger should be initialized"
    assert logger_instance.info_logger is not None, "Info logger should be initialized"
    assert logger_instance.debug_logger is not None, "Debug logger should be initialized"
    assert logger_instance.errors_logger is not None, "Errors logger should be initialized"
    assert logger_instance.json_logger is not None, "JSON logger should be initialized"

# Test for log
def test_log_info(logger_instance, log_paths):
    """Verify that log method correctly logs messages at different levels."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(logging.INFO, "Info message")
    with open(log_paths['info_log_path'], 'r') as f:
        content = f.read()
        assert "INFO - Info message" in content, "Info message should be logged to the correct file."


def test_log_debug(logger_instance, log_paths):
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(logging.DEBUG, "Debug message")
    with open(log_paths['debug_log_path'], 'r') as f:
       content = f.read()
       assert "DEBUG - Debug message" in content, "Debug message should be logged to the correct file."


def test_log_error(logger_instance, log_paths):
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(logging.ERROR, "Error message")
    with open(log_paths['errors_log_path'], 'r') as f:
        content = f.read()
        assert "ERROR - Error message" in content, "Error message should be logged to the correct file."


def test_log_json(logger_instance, log_paths):
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(logging.INFO, "JSON message", formatter=JsonFormatter())
    with open(log_paths['json_log_path'], 'r') as f:
        content = f.read()
        assert '"message": "JSON message"' in content, "JSON message should be logged to the correct file."


def test_log_exception(logger_instance, log_paths):
        """Verify that log method correctly handles exception logging."""
        logger_instance.initialize_loggers(**log_paths)
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            logger_instance.log(logging.ERROR, "Error with exception", ex=e, exc_info=True)

        with open(log_paths['errors_log_path'], 'r') as f:
            content = f.read()
            assert "Error with exception" in content, "Exception message should be logged."
            assert "ValueError: Test exception" in content, "Exception info should be logged."


def test_log_with_color(logger_instance, log_paths, capsys):
    """Verify that the log method handles color output."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(logging.INFO, "Colored message", color=(Fore.RED, Back.WHITE))
    captured = capsys.readouterr()
    assert f"{Fore.RED}{Back.WHITE}Colored message{Fore.RESET}{Back.RESET}" in captured.out, "Color should be applied"


# Test for info, success, warning, debug, error, critical
def test_info(logger_instance, log_paths):
    """Verify that info method correctly logs an info message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.info("Info test")
    with open(log_paths['info_log_path'], 'r') as f:
        content = f.read()
        assert "INFO - Info test" in content

def test_success(logger_instance, log_paths):
    """Verify that success method correctly logs a success message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.success("Success test")
    with open(log_paths['info_log_path'], 'r') as f:
        content = f.read()
        assert "INFO - Success test" in content

def test_warning(logger_instance, log_paths):
    """Verify that warning method correctly logs a warning message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.warning("Warning test")
    with open(log_paths['errors_log_path'], 'r') as f:
        content = f.read()
        assert "WARNING - Warning test" in content

def test_debug(logger_instance, log_paths):
    """Verify that debug method correctly logs a debug message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.debug("Debug test")
    with open(log_paths['debug_log_path'], 'r') as f:
        content = f.read()
        assert "DEBUG - Debug test" in content
       
def test_error(logger_instance, log_paths):
    """Verify that error method correctly logs an error message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.error("Error test")
    with open(log_paths['errors_log_path'], 'r') as f:
        content = f.read()
        assert "ERROR - Error test" in content
    
def test_critical(logger_instance, log_paths):
    """Verify that critical method correctly logs a critical message."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.critical("Critical test")
    with open(log_paths['errors_log_path'], 'r') as f:
        content = f.read()
        assert "CRITICAL - Critical test" in content


def test_info_with_colors(logger_instance, log_paths, capsys):
    """Verify that info method can log with color."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.info("Colored Info", colors=(Fore.GREEN, Back.BLACK))
    captured = capsys.readouterr()
    assert f"{Fore.GREEN}{Back.BLACK}Colored Info{Fore.RESET}{Back.RESET}" in captured.out, "Color should be applied"

def test_error_with_colors(logger_instance, log_paths, capsys):
    """Verify that error method can log with color."""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.error("Colored Error", colors=(Fore.RED, Back.WHITE))
    captured = capsys.readouterr()
    assert f"{Fore.RED}{Back.WHITE}Colored Error{Fore.RESET}{Back.RESET}" in captured.out, "Color should be applied"

def test_exception_logging(logger_instance, log_paths):
        """Verify the methods correctly handles exception logging."""
        logger_instance.initialize_loggers(**log_paths)
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            logger_instance.error("Error with exception", ex=e, exc_info=True)
        with open(log_paths['errors_log_path'], 'r') as f:
            content = f.read()
            assert "Error with exception" in content, "Exception message should be logged."
            assert "ValueError: Test exception" in content, "Exception info should be logged."


def test_log_no_file_paths(logger_instance):
    """Test when file paths are not specified during initialization"""
    logger_instance.initialize_loggers()
    logger_instance.info("Test no file paths")
    # check that no errors are raised, that console logger exists and message sent
    assert logger_instance.console_logger is not None


def test_log_no_level(logger_instance, log_paths):
    """Test that all levels are captured if logging level is not passed"""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(level=logging.DEBUG, message="debug test", exc_info=True)
    logger_instance.log(level=logging.INFO, message="info test", exc_info=True)
    logger_instance.log(level=logging.WARNING, message="warning test", exc_info=True)
    logger_instance.log(level=logging.ERROR, message="error test", exc_info=True)
    logger_instance.log(level=logging.CRITICAL, message="critical test", exc_info=True)
    
    with open(log_paths["debug_log_path"], "r") as f:
        assert "debug test" in f.read()
    with open(log_paths["info_log_path"], "r") as f:
         assert "info test" in f.read()
    with open(log_paths["errors_log_path"], "r") as f:
        content = f.read()
        assert "warning test" in content
        assert "error test" in content
        assert "critical test" in content


def test_log_with_custom_formatter(logger_instance, log_paths):
    """Test logging with custom formatter."""
    logger_instance.initialize_loggers(**log_paths)
    formatter = logging.Formatter('%(message)s')
    logger_instance.log(level=logging.INFO, message="Custom format test", formatter=formatter)
    with open(log_paths['info_log_path'], 'r') as f:
        content = f.read()
        assert "Custom format test" in content, "Custom formatter should be used."


def test_log_empty_message(logger_instance, log_paths):
    """Test with empty log message"""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(level=logging.INFO, message="")
    with open(log_paths['info_log_path'], 'r') as f:
        content = f.read()
        assert "INFO - " in content

def test_log_none_message(logger_instance, log_paths):
    """Test with none log message"""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(level=logging.INFO, message=None)
    with open(log_paths['info_log_path'], 'r') as f:
       content = f.read()
       assert "INFO - None" in content

def test_log_with_default_formatter(logger_instance, log_paths):
    """Test logging with default formatter"""
    logger_instance.initialize_loggers(**log_paths)
    logger_instance.log(level=logging.INFO, message="Default format test")
    with open(log_paths['info_log_path'], 'r') as f:
       content = f.read()
       assert "INFO - Default format test" in content, "Default formatter should be used"
```