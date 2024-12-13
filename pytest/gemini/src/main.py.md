```python
import pytest
from unittest.mock import patch
from io import StringIO
import argparse
from src.main import script1, script2, show_help, interactive_menu, main
from src.logger.logger import logger

# Fixture definitions, if needed
@pytest.fixture
def mock_input(monkeypatch):
    """Mocks the input function to simulate user input."""
    def mock_input_func(inputs):
        input_generator = (i for i in inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_generator))
    return mock_input_func

@pytest.fixture
def mock_logger(monkeypatch):
    """Mocks the logger to capture log messages."""
    captured_logs = []
    def mock_logger_func(level, message):
        captured_logs.append((level, message))
    monkeypatch.setattr(logger, 'error', lambda message: mock_logger_func('error', message))
    return captured_logs

# Tests for script1 function
def test_script1_valid_execution(capsys):
    """Checks if script1 executes correctly and prints the expected message."""
    script1()
    captured = capsys.readouterr()
    assert "Script 1 started" in captured.out

# Tests for script2 function
def test_script2_valid_execution(capsys):
    """Checks if script2 executes correctly and prints the expected message."""
    script2()
    captured = capsys.readouterr()
    assert "Script 2 started" in captured.out


# Tests for show_help function
def test_show_help_displays_commands(capsys):
    """Checks if show_help prints the help commands correctly."""
    show_help()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "1. Run script 1" in captured.out
    assert "2. Run script 2" in captured.out
    assert "3. --help" in captured.out
    assert "4. exit" in captured.out

# Tests for interactive_menu function
def test_interactive_menu_script1(capsys, mock_input):
    """Checks if selecting '1' runs script1 and exits."""
    mock_input(['1', 'exit'])
    interactive_menu()
    captured = capsys.readouterr()
    assert "Script 1 started" in captured.out
    assert "Exiting the program." in captured.out

def test_interactive_menu_script2(capsys, mock_input):
    """Checks if selecting '2' runs script2 and exits."""
    mock_input(['2', 'exit'])
    interactive_menu()
    captured = capsys.readouterr()
    assert "Script 2 started" in captured.out
    assert "Exiting the program." in captured.out

def test_interactive_menu_show_help(capsys, mock_input):
    """Checks if selecting '3' or '--help' shows help and then exits."""
    mock_input(['3', 'exit'])
    interactive_menu()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    mock_input(['--help', 'exit'])
    interactive_menu()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "Exiting the program." in captured.out

def test_interactive_menu_invalid_input(capsys, mock_input, mock_logger):
     """Checks if invalid input is handled correctly and logged."""
     mock_input(['invalid', 'exit'])
     interactive_menu()
     assert "Invalid input. Please choose a valid command." in mock_logger[0][1]
     captured = capsys.readouterr()
     assert "Exiting the program." in captured.out

def test_interactive_menu_exit(capsys, mock_input):
    """Checks if 'exit' command correctly exits the menu."""
    mock_input(['exit'])
    interactive_menu()
    captured = capsys.readouterr()
    assert "Exiting the program." in captured.out

# Tests for main function
def test_main_with_help_argument(capsys):
    """Checks if --help argument calls show_help."""
    with patch('sys.argv', ['main.py', '--help']):
         main()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out

def test_main_without_arguments(capsys, mock_input):
    """Checks if main runs interactive menu without arguments."""
    with patch('sys.argv', ['main.py']):
        mock_input(['exit'])
        main()
    captured = capsys.readouterr()
    assert "Welcome! Choose one of the commands:\\n" in captured.out
    assert "Exiting the program." in captured.out
```