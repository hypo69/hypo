```python
import pytest
import logging
import json
from pathlib import Path
from unittest.mock import patch, mock_open
from datetime import datetime
from types import SimpleNamespace

from src.logger.logger import Logger, JsonFormatter, SingletonMeta, TEXT_COLORS, BG_COLORS
from src.header import __root__
import colorama


# Fixture for creating a mock config file
@pytest.fixture
def mock_config_file(tmp_path):
    """Creates a mock config.json file for testing."""
    config_data = {
        "path": {
            "log": str(tmp_path / "logs")
        }
    }
    config_path = tmp_path / "config.json"
    with open(config_path, "w") as f:
        json.dump(config_data, f)
    return config_path


@pytest.fixture
def logger_instance(mock_config_file):
    """Provides a Logger instance for tests with a mock config file."""
    with patch("src.logger.logger.Path", side_effect=lambda path: Path(str(path).replace(str(__root__ / 'src' / 'config.json'), str(mock_config_file)))):
        return Logger()


@pytest.fixture
def mock_datetime():
    """Mocks datetime for consistent timestamps in tests."""
    with patch('src.logger.logger.datetime') as mock_dt:
        mock_dt.datetime.now.return_value = datetime(2024, 1, 1, 10, 30)
        yield mock_dt


def test_singleton_meta_creates_single_instance():
    """Checks if SingletonMeta creates only one instance of a class."""
    class TestClass(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value

    instance1 = TestClass(10)
    instance2 = TestClass(20)
    assert instance1 is instance2
    assert instance1.value == 10


def test_json_formatter_format():
    """Checks if JsonFormatter correctly formats a log record."""
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname="test.py",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None,
    )
    formatted_log = json.loads(formatter.format(record))
    assert "asctime" in formatted_log
    assert formatted_log["levelname"] == "INFO"
    assert formatted_log["message"] == "Test message"
    assert formatted_log["exc_info"] is None


def test_json_formatter_format_with_exception():
    """Checks if JsonFormatter correctly formats a log record with exception info."""
    formatter = JsonFormatter()
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        record = logging.LogRecord(
            name="test_logger",
            level=logging.ERROR,
            pathname="test.py",
            lineno=10,
            msg="Test message",
            args=(),
            exc_info=logging.makeLogRecord({}).exc_info
        )
        formatted_log = json.loads(formatter.format(record))
        assert "exc_info" in formatted_log
        assert formatted_log["exc_info"] is not None


def test_logger_initialization(mock_config_file, mock_datetime):
    """Tests if Logger initializes correctly with default paths."""
    config = SimpleNamespace(**json.loads(Path(mock_config_file).read_text(encoding='UTF-8')))
    timestamp = datetime(2024, 1, 1, 10, 30).strftime("%d%m%y%H%M")
    base_path = Path(config.path['log'])
    log_files_path = base_path / timestamp

    with patch("src.logger.logger.Path", side_effect=lambda path: Path(str(path).replace(str(__root__ / 'src' / 'config.json'), str(mock_config_file)))):
        logger = Logger()
        assert logger.log_files_path == log_files_path
        assert logger.info_log_path == log_files_path / 'info.log'
        assert logger.debug_log_path == log_files_path / 'debug.log'
        assert logger.errors_log_path == log_files_path / 'errors.log'
        assert logger.json_log_path ==  base_path / f'{timestamp}.json'
        assert isinstance(logger.logger_console, logging.Logger)
        assert isinstance(logger.logger_file_info, logging.Logger)
        assert isinstance(logger.logger_file_debug, logging.Logger)
        assert isinstance(logger.logger_file_errors, logging.Logger)
        assert isinstance(logger.logger_file_json, logging.Logger)


def test_logger_custom_paths(mock_config_file, mock_datetime):
    """Tests if Logger initializes correctly with custom paths."""
    config = SimpleNamespace(**json.loads(Path(mock_config_file).read_text(encoding='UTF-8')))
    timestamp = datetime(2024, 1, 1, 10, 30).strftime("%d%m%y%H%M")
    base_path = Path(config.path['log'])
    log_files_path = base_path / timestamp
    with patch("src.logger.logger.Path", side_effect=lambda path: Path(str(path).replace(str(__root__ / 'src' / 'config.json'), str(mock_config_file)))):
        logger = Logger(
            info_log_path="custom_info.log",
            debug_log_path="custom_debug.log",
            errors_log_path="custom_errors.log",
            json_log_path="custom_log.json",
        )

        assert logger.log_files_path == log_files_path
        assert logger.info_log_path == log_files_path / "custom_info.log"
        assert logger.debug_log_path == log_files_path / "custom_debug.log"
        assert logger.errors_log_path == log_files_path / "custom_errors.log"
        assert logger.json_log_path == base_path / "custom_log.json"



def test_logger_creates_log_directories_and_files(mock_config_file, mock_datetime, tmp_path):
    """Tests if Logger creates log directories and files."""
    with patch("src.logger.logger.Path", side_effect=lambda path: Path(str(path).replace(str(__root__ / 'src' / 'config.json'), str(mock_config_file)))):
        logger = Logger()
        
        assert logger.log_files_path.exists()
        assert logger.info_log_path.exists()
        assert logger.debug_log_path.exists()
        assert logger.errors_log_path.exists()
        assert logger.json_log_path.exists()

def test_format_message_no_color(logger_instance):
    """Checks if _format_message formats message correctly without colors."""
    message = "Test message"
    formatted_message = logger_instance._format_message(message)
    assert formatted_message == "Test message "

def test_format_message_with_color(logger_instance):
    """Checks if _format_message formats message with colors correctly."""
    message = "Test message"
    color = ("red", "yellow")
    expected_message = f"{TEXT_COLORS.get('red', colorama.Fore.RESET)}{BG_COLORS.get('yellow', colorama.Back.RESET)}{message} {colorama.Style.RESET_ALL}"
    formatted_message = logger_instance._format_message(message, color=color)
    assert formatted_message == expected_message

def test_format_message_with_invalid_color(logger_instance):
    """Checks if _format_message handles invalid colors."""
    message = "Test message"
    color = ("invalid_text_color", "invalid_bg_color")
    expected_message = f"{colorama.Fore.RESET}{colorama.Back.RESET}{message} {colorama.Style.RESET_ALL}"
    formatted_message = logger_instance._format_message(message, color=color)
    assert formatted_message == expected_message

def test_ex_full_info(logger_instance):
    """Checks if _ex_full_info returns correct exception info."""
    try:
        raise ValueError("Test exception")
    except ValueError as e:
         info = logger_instance._ex_full_info(e)
         assert "File:" in info
         assert "Function:" in info
         assert "Line:" in info
         assert "Test exception" in info

def test_ex_full_info_no_exception(logger_instance):
     """Checks if _ex_full_info handles no exception case"""
     info = logger_instance._ex_full_info(None)
     assert "\\nFile:" in info
     assert "\\n  -Function:" in info
     assert "\\n   |\\n    --Line:" in info
     assert "" in info

def test_log_message(logger_instance, caplog):
    """Checks if log method logs a message with correct level."""
    logger_instance.log(logging.INFO, "Test log message")
    assert "Test log message" in caplog.text

def test_log_message_with_color(logger_instance, caplog):
    """Checks if log method logs a message with correct color."""
    color = ("red", "white")
    logger_instance.log(logging.INFO, "Test log message", color=color)
    expected_message = f"{TEXT_COLORS.get('red', colorama.Fore.RESET)}{BG_COLORS.get('white', colorama.Back.RESET)}Test log message {colorama.Style.RESET_ALL}"
    assert expected_message in caplog.text

def test_log_message_with_exception_info(logger_instance, caplog):
    """Checks if log method logs a message with exception info."""
    try:
        raise ValueError("Test Exception")
    except ValueError as e:
        logger_instance.log(logging.ERROR, "Test log message", ex=e, exc_info=True)
        assert "Test log message" in caplog.text
        assert "Test Exception" in caplog.text
        assert "File:" in caplog.text
        assert "Function:" in caplog.text
        assert "Line:" in caplog.text

def test_log_message_without_exception_info(logger_instance, caplog):
    """Checks if log method logs a message without exception info."""
    logger_instance.log(logging.INFO, "Test log message", exc_info=False)
    assert "Test log message" in caplog.text
    assert "File:" not in caplog.text


def test_info_log(logger_instance, caplog):
    """Checks if info method logs a message with info level."""
    logger_instance.info("Test info message")
    assert "Test info message" in caplog.text
    assert logging.INFO == caplog.records[0].levelno

def test_success_log(logger_instance, caplog):
    """Checks if success method logs a message with info level."""
    logger_instance.success("Test success message")
    assert "Test success message" in caplog.text
    assert logging.INFO == caplog.records[0].levelno


def test_warning_log(logger_instance, caplog):
    """Checks if warning method logs a message with warning level."""
    logger_instance.warning("Test warning message")
    assert "Test warning message" in caplog.text
    assert logging.WARNING == caplog.records[0].levelno

def test_debug_log(logger_instance, caplog):
    """Checks if debug method logs a message with debug level."""
    logger_instance.debug("Test debug message")
    assert "Test debug message" in caplog.text
    assert logging.DEBUG == caplog.records[0].levelno

def test_error_log(logger_instance, caplog):
    """Checks if error method logs a message with error level."""
    logger_instance.error("Test error message")
    assert "Test error message" in caplog.text
    assert logging.ERROR == caplog.records[0].levelno

def test_critical_log(logger_instance, caplog):
    """Checks if critical method logs a message with critical level."""
    logger_instance.critical("Test critical message")
    assert "Test critical message" in caplog.text
    assert logging.CRITICAL == caplog.records[0].levelno
```