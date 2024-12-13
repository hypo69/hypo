```python
import pytest
import logging
from unittest.mock import patch, mock_open
from src.logger import Logger, SingletonMeta, JsonFormatter
import colorama
import os

# Fixtures
@pytest.fixture
def logger_instance():
    """Provides an instance of the Logger class."""
    return Logger()

@pytest.fixture
def mock_config():
    """Provides a mock configuration dictionary for the logger."""
    return {
        'info_log_path': 'test_logs/info.log',
        'debug_log_path': 'test_logs/debug.log',
        'errors_log_path': 'test_logs/errors.log',
        'json_log_path': 'test_logs/log.json'
    }

# Tests for SingletonMeta
def test_singleton_meta_instance_creation():
    """Verifies that SingletonMeta ensures only one instance is created."""
    class TestClass(metaclass=SingletonMeta):
        pass
    
    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 is instance2, "SingletonMeta should return the same instance."

def test_singleton_meta_different_classes():
      """Verifies that SingletonMeta works for different classes."""
      class TestClassA(metaclass=SingletonMeta):
            pass
      class TestClassB(metaclass=SingletonMeta):
            pass

      instance_a = TestClassA()
      instance_b = TestClassB()
      assert instance_a is not instance_b, "SingletonMeta should not share instances across different classes."

# Tests for JsonFormatter
def test_json_formatter_format_record():
    """Verifies that JsonFormatter formats log records correctly."""
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name='test',
        level=logging.INFO,
        pathname='test.py',
        lineno=10,
        msg='test message',
        args=(),
        exc_info=None,
        func='test_function',
        sinfo=None
    )
    
    formatted_record = formatter.format(record)
    assert isinstance(formatted_record, str), "The format method should return a string."
    assert '"message": "test message"' in formatted_record, "The formatted output should contain the message."
    assert '"level": "INFO"' in formatted_record, "The formatted output should contain the log level."
    assert '"name": "test"' in formatted_record, "The formatted output should contain the logger name."

# Tests for Logger.__init__
def test_logger_init(logger_instance):
    """Checks if Logger initializes with correct placeholders."""
    assert logger_instance.console_logger is None
    assert logger_instance.file_loggers == {}
    assert logger_instance.json_logger is None
    
# Tests for Logger._configure_logger
def test_configure_logger_with_default_values(logger_instance):
    """Checks logger configuration with default values."""
    logger = logger_instance._configure_logger(name='test_logger', log_path='test.log')
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.DEBUG
    
def test_configure_logger_with_custom_values(logger_instance):
    """Checks logger configuration with custom values."""
    formatter = logging.Formatter('%(message)s')
    logger = logger_instance._configure_logger(name='test_logger', log_path='test.log', level=logging.INFO, formatter=formatter, mode='w')
    assert logger.level == logging.INFO
    assert isinstance(logger.handlers[0].formatter, logging.Formatter)
    assert logger.handlers[0].mode == 'w'
    
def test_configure_logger_no_formatter(logger_instance):
    """Checks logger configuration without a custom formatter."""
    logger = logger_instance._configure_logger(name='test_logger', log_path='test.log', level=logging.INFO)
    assert logger.level == logging.INFO
    assert isinstance(logger.handlers[0].formatter, logging.Formatter) # Default formatter should be created
    
# Tests for Logger.initialize_loggers
def test_initialize_loggers_with_config(logger_instance, mock_config):
    """Tests that loggers are initialized correctly with config."""
    logger_instance.initialize_loggers(**mock_config)

    assert logger_instance.console_logger is not None
    assert isinstance(logger_instance.console_logger, logging.Logger)

    assert 'info' in logger_instance.file_loggers
    assert 'debug' in logger_instance.file_loggers
    assert 'errors' in logger_instance.file_loggers
    
    assert logger_instance.json_logger is not None
    assert isinstance(logger_instance.json_logger, logging.Logger)

    # Cleaning test files if present
    for path in mock_config.values():
        if os.path.exists(path):
            os.remove(path)
        
def test_initialize_loggers_empty_config(logger_instance):
    """Tests that loggers are not initialized if no config is provided."""
    logger_instance.initialize_loggers()

    assert logger_instance.console_logger is not None
    assert logger_instance.file_loggers == {}
    assert logger_instance.json_logger is None

# Tests for Logger.log
@patch('src.logger.Logger._configure_logger')
@patch('src.logger.logging.Logger.log')
def test_log_message_with_console_only(mock_logger_log, mock_configure_logger, logger_instance):
    """Tests the log method with console logger."""
    mock_configure_logger.return_value = logging.getLogger('console_test')
    logger_instance.console_logger = mock_configure_logger()
    
    logger_instance.log(level=logging.INFO, message="Test log message")
    mock_logger_log.assert_called_once_with(logging.INFO, "Test log message")

@patch('src.logger.Logger._configure_logger')
@patch('src.logger.logging.Logger.log')
def test_log_message_with_all_loggers(mock_logger_log, mock_configure_logger, logger_instance, mock_config):
    """Tests the log method with console, file and json loggers."""
    mock_configure_logger.side_effect = [logging.getLogger('console_test'), logging.getLogger('file_info_test'), logging.getLogger('file_debug_test'), logging.getLogger('file_error_test'), logging.getLogger('file_json_test')]

    logger_instance.initialize_loggers(**mock_config)
    
    logger_instance.log(level=logging.INFO, message="Test log message")
    assert mock_logger_log.call_count == 5, "Logger log function should have been called 5 times with all loggers."

    # Cleaning test files if present
    for path in mock_config.values():
        if os.path.exists(path):
            os.remove(path)
            
@patch('src.logger.Logger._configure_logger')
@patch('src.logger.logging.Logger.log')
def test_log_message_with_exception(mock_logger_log, mock_configure_logger, logger_instance, mock_config):
    """Tests logging a message with an exception."""
    mock_configure_logger.side_effect = [logging.getLogger('console_test'), logging.getLogger('file_info_test'), logging.getLogger('file_debug_test'), logging.getLogger('file_error_test'), logging.getLogger('file_json_test')]

    logger_instance.initialize_loggers(**mock_config)

    try:
        raise ValueError("Test exception")
    except ValueError as e:
        logger_instance.log(level=logging.ERROR, message="Error occurred", ex=e)

    # Check if the log method was called with the correct exception
    for call in mock_logger_log.mock_calls:
        if call.args[0] == logging.ERROR and "Error occurred" in call.args[1]:
            assert isinstance(call.kwargs.get('exc_info'), tuple), "Exception info is included"
    
    # Cleaning test files if present
    for path in mock_config.values():
        if os.path.exists(path):
            os.remove(path)

@patch('src.logger.Logger._configure_logger')
@patch('src.logger.logging.Logger.log')
def test_log_message_with_exc_info(mock_logger_log, mock_configure_logger, logger_instance, mock_config):
    """Tests logging a message with exc_info set to True."""
    mock_configure_logger.side_effect = [logging.getLogger('console_test'), logging.getLogger('file_info_test'), logging.getLogger('file_debug_test'), logging.getLogger('file_error_test'), logging.getLogger('file_json_test')]

    logger_instance.initialize_loggers(**mock_config)

    try:
        raise ValueError("Test exception")
    except ValueError:
        logger_instance.log(level=logging.ERROR, message="Error occurred", exc_info=True)
    
    for call in mock_logger_log.mock_calls:
         if call.args[0] == logging.ERROR and "Error occurred" in call.args[1]:
            assert isinstance(call.kwargs.get('exc_info'), tuple), "Exception info should be included"
    
    # Cleaning test files if present
    for path in mock_config.values():
        if os.path.exists(path):
            os.remove(path)

@patch('src.logger.Logger._configure_logger')
@patch('src.logger.logging.Logger.log')
def test_log_message_with_color(mock_logger_log, mock_configure_logger, logger_instance):
    """Tests that color is applied to console log message."""
    mock_configure_logger.return_value = logging.getLogger('console_test')
    logger_instance.console_logger = mock_configure_logger()
    
    color = (colorama.Fore.RED, colorama.Back.WHITE)
    logger_instance.log(level=logging.INFO, message="Colored log", color=color)
    
    mock_logger_log.assert_called_once()
    logged_message = mock_logger_log.call_args[0][1]
    
    assert color[0] in logged_message, "Text color should be in log message"
    assert color[1] in logged_message, "Background color should be in log message"
    assert colorama.Style.RESET_ALL in logged_message, "Reset color style should be in log message"

def test_log_with_invalid_level(logger_instance):
    """Tests the log method with an invalid logging level."""
    with pytest.raises(ValueError, match="Invalid log level provided"):
        logger_instance.log(level="INVALID_LEVEL", message="Invalid log level")

# Tests for shortcut methods
@patch('src.logger.Logger.log')
def test_info_shortcut(mock_log, logger_instance):
    """Tests the info shortcut method."""
    logger_instance.info("Info message")
    mock_log.assert_called_once_with(logging.INFO, "Info message", ex=None, exc_info=False, color=None)

@patch('src.logger.Logger.log')
def test_success_shortcut(mock_log, logger_instance):
    """Tests the success shortcut method."""
    logger_instance.success("Success message")
    mock_log.assert_called_once_with(logging.INFO, "Success message", ex=None, exc_info=False, color=(colorama.Fore.GREEN, colorama.Back.BLACK))

@patch('src.logger.Logger.log')
def test_warning_shortcut(mock_log, logger_instance):
    """Tests the warning shortcut method."""
    logger_instance.warning("Warning message")
    mock_log.assert_called_once_with(logging.WARNING, "Warning message", ex=None, exc_info=False, color=(colorama.Fore.YELLOW, colorama.Back.BLACK))

@patch('src.logger.Logger.log')
def test_debug_shortcut(mock_log, logger_instance):
    """Tests the debug shortcut method."""
    logger_instance.debug("Debug message")
    mock_log.assert_called_once_with(logging.DEBUG, "Debug message", ex=None, exc_info=False, color=(colorama.Fore.BLUE, colorama.Back.BLACK))

@patch('src.logger.Logger.log')
def test_error_shortcut(mock_log, logger_instance):
    """Tests the error shortcut method."""
    logger_instance.error("Error message")
    mock_log.assert_called_once_with(logging.ERROR, "Error message", ex=None, exc_info=False, color=(colorama.Fore.RED, colorama.Back.BLACK))

@patch('src.logger.Logger.log')
def test_critical_shortcut(mock_log, logger_instance):
    """Tests the critical shortcut method."""
    logger_instance.critical("Critical message")
    mock_log.assert_called_once_with(logging.CRITICAL, "Critical message", ex=None, exc_info=False, color=(colorama.Fore.RED, colorama.Back.WHITE))
```