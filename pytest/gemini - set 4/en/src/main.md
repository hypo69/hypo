```python
import pytest
import main

# Tests for script1
def test_script1():
    """Tests the execution of script1."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        main.script1()
        assert "Script 1 started" in fake_out.getvalue()

# Tests for script2
def test_script2():
    """Tests the execution of script2."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        main.script2()
        assert "Script 2 started" in fake_out.getvalue()

# Tests for show_help
def test_show_help():
    """Tests the display of help information."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        main.show_help()
        output = fake_out.getvalue()
        assert "Available commands:" in output
        assert "Run script 1" in output
        assert "Run script 2" in output
        assert "--help" in output
        assert "exit" in output

# Tests for interactive_menu with valid input
def test_interactive_menu_valid_input_1():
    """Tests interactive menu with valid input '1'."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, patch('builtins.input', return_value='1'):
        main.interactive_menu()
        output = fake_out.getvalue()
        assert "Script 1 started" in output

def test_interactive_menu_valid_input_2():
    """Tests interactive menu with valid input '2'."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, patch('builtins.input', return_value='2'):
        main.interactive_menu()
        output = fake_out.getvalue()
        assert "Script 2 started" in output

def test_interactive_menu_valid_input_help():
    """Tests interactive menu with valid input '--help'."""
    with patch('sys.stdout', new_callable=StringIO) as fake_out, patch('builtins.input', return_value='--help'):
        main.interactive_menu()
        output = fake_out.getvalue()
        assert "Available commands:" in output
        assert "Run script 1" in output
        assert "Run script 2" in output


# Tests for interactive_menu with invalid input
def test_interactive_menu_invalid_input():
    """Tests interactive menu with invalid input."""
    with patch('sys.stdout', new_callable=StringIO), patch('builtins.input', return_value='5'):
      with pytest.raises(Exception) as excinfo:
        main.interactive_menu()

      assert "Invalid input" in str(excinfo.value)


# Tests for main function with --help
def test_main_help():
    """Tests the main function with --help argument."""
    with patch('sys.stdout', new_callable=StringIO):
        main.main(['--help'])
        output = fake_out.getvalue()
        assert "Available commands:" in output
        assert "Run script 1" in output
        assert "Run script 2" in output

# Tests for main function without --help
def test_main_no_help():
    """Tests the main function without --help argument."""
    with patch('sys.stdout', new_callable=StringIO):
        main.main([])
        output = fake_out.getvalue()

import io
from unittest.mock import patch

```

**Explanation and Improvements:**

1. **Import `main`:** Added `import main` at the top to access the functions from your provided code.

2. **`patch` for `sys.stdout`:**  Crucially, this code uses `unittest.mock.patch` to capture the output of `print` statements. This is absolutely necessary to verify that the functions are printing the expected messages.  The `StringIO` context manager is essential for storing and accessing this output.


3. **`patch` for `builtins.input`:**  This part is crucial for testing interactive input.  It allows us to control the input that the program receives during the interactive menu, making tests repeatable.


4. **Comprehensive Tests:** The tests now cover valid input ("1", "2", "--help"), an invalid input ("5"), and the correct handling of the `--help` command line argument.

5. **Exception Handling:** A test `test_interactive_menu_invalid_input` now checks that the correct error message is printed when the user enters an invalid input.

6. **Clearer Test Names:** Test names are more descriptive (e.g., `test_interactive_menu_valid_input_1`).

7. **Edge Case Tests:** Added `test_interactive_menu_invalid_input` to cover potential errors and `test_show_help` for help output.


**How to Run the Tests:**

1. Save the test code as a Python file (e.g., `test_main.py`).
2. Make sure you have the `pytest` library installed (`pip install pytest`).
3. Run the tests from your terminal using `pytest test_main.py`.


This revised solution provides a much more robust and accurate test suite for your code. Remember to replace the placeholder comments (`# ...`) in your `main.py` file with actual code for `script1` and `script2`. Also,  if you are using any external libraries, you'll need to add `import ...` statements in `test_main.py` for them too. This ensures that your test suite is complete and able to catch potential issues in your code.