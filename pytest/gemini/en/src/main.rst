```python
import pytest
import sys
from unittest.mock import patch
from hypotez.src.main import main, script1, script2, show_help, interactive_menu


def test_script1():
    """Tests the execution of script1."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        script1()
        assert "Script 1 started" in fake_out.getvalue()


def test_script2():
    """Tests the execution of script2."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        script2()
        assert "Script 2 started" in fake_out.getvalue()


def test_show_help():
    """Tests the display of help information."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        show_help()
        output = fake_out.getvalue()
        assert "Available commands:" in output
        assert "Run script 1" in output
        assert "Run script 2" in output
        assert "--help" in output
        assert "exit" in output


def test_interactive_menu_valid_input_script1():
    """Tests the interactive menu with valid input (script 1)."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, \
            patch('builtins.input', side_effect=['1', 'exit']):
        interactive_menu()
        output = fake_out.getvalue()
        assert "Script 1 started" in output
        assert "Exiting the program." in output


def test_interactive_menu_valid_input_script2():
    """Tests the interactive menu with valid input (script 2)."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, \
            patch('builtins.input', side_effect=['2', 'exit']):
        interactive_menu()
        output = fake_out.getvalue()
        assert "Script 2 started" in output
        assert "Exiting the program." in output

def test_interactive_menu_help():
    """Tests the interactive menu with --help input."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, \
            patch('builtins.input', side_effect=['3', 'exit']):
        interactive_menu()
        output = fake_out.getvalue()
        assert "Available commands:" in output
        assert "Exiting the program." in output

def test_interactive_menu_invalid_input():
    """Tests the interactive menu with invalid input."""
    with patch('sys.stdout', new_callable=StringIO), \
         patch('builtins.input', side_effect=['abc', 'exit']):
        interactive_menu()
        output = sys.stdout.getvalue()
        assert "Invalid input" in output

def test_main_help_flag():
    """Test the main function with --help flag."""
    with patch('sys.stdout', new_callable=StringIO):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(help=True)):
           main()
           output = sys.stdout.getvalue()
           assert "Available commands:" in output

def test_main_no_help_flag():
    """Test the main function without --help flag (should enter interactive menu)."""
    with patch('sys.stdout', new_callable=StringIO), patch('builtins.input', side_effect=['1', 'exit']):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(help=False)):
            main()
            output = sys.stdout.getvalue()
            assert "Script 1 started" in output



import io
import argparse

class StringIO(io.StringIO):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


```

**Explanation and Improvements:**

1. **Mocking `input` and `stdout`:**  Crucially, the tests now use `unittest.mock.patch` to mock the `input` function and `sys.stdout`.  This is vital for testing interactive programs.  The `side_effect` argument provides a sequence of inputs for the mocked `input`, and the output of the `print` statements is captured in `fake_out`.

2. **Testing Invalid Input:** Added `test_interactive_menu_invalid_input` to verify the program handles user input that is not a valid choice.

3. **Testing `main` function with `--help`:** Added `test_main_help_flag` and `test_main_no_help_flag`.

4. **Comprehensive `show_help` Test:** Now verifies that the `show_help` function properly outputs all the help information.

5. **Robust `interactive_menu` Tests:**  The `interactive_menu` tests now cover various valid input cases (script 1, script 2, help) as well as the handling of invalid user input.

6. **`StringIO` class:** This is a crucial addition; it allows us to capture the output from `print` statements without actually printing to the console, and avoids the `BrokenPipeError` that might occur if you run the test interactively and try to read input from the console.  The `StringIO` class is now included in the test file, making the code self-contained.

7. **Import necessary modules:** Made sure to import `argparse` for the test of the `main` function.

**How to Run the Tests:**

1.  Save the above test code in a file named `test_main.py` (or a similar name) in the same directory as your `main.py` file.
2.  Make sure you have `pytest` installed (`pip install pytest`).
3.  Run the tests from your terminal: `pytest test_main.py`

These changes make the tests much more reliable and robust, covering the interactive behavior and edge cases more effectively. Remember to adapt the test cases further if you add more logic and features to your code.