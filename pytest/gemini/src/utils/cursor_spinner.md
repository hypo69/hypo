```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner


# Test cases for spinning_cursor
def test_spinning_cursor_basics():
    """Tests the spinning_cursor generator for basic functionality."""
    cursor = spinning_cursor()
    assert next(cursor) == '|'
    assert next(cursor) == '/'
    assert next(cursor) == '-'
    assert next(cursor) == '\\'
    assert next(cursor) == '|'


def test_spinning_cursor_cycle():
    """Tests the spinning_cursor generator to ensure it cycles correctly."""
    cursor = spinning_cursor()
    expected_symbols = ['|', '/', '-', '\\']
    for i in range(len(expected_symbols)):
        assert next(cursor) == expected_symbols[i % len(expected_symbols)]


# Test cases for show_spinner
def test_show_spinner_valid_input():
    """Tests show_spinner with valid input and duration."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.1)
    end_time = time.time()
    assert end_time - start_time > 0.9  # Check if function took at least the specified time


def test_show_spinner_short_duration():
    """Tests show_spinner with a very short duration (less than delay)."""
    start_time = time.time()
    show_spinner(duration=0.05, delay=0.1)  # Duration is less than delay
    end_time = time.time()
    assert end_time - start_time < 0.15   # Duration should be nearly zero


def test_show_spinner_zero_duration():
    """Tests show_spinner with zero duration."""
    start_time = time.time()
    show_spinner(duration=0, delay=0.1)  # Duration is zero
    end_time = time.time()
    assert end_time - start_time < 0.005  # Time should be negligibly small


def test_show_spinner_negative_duration():
    """Tests show_spinner with negative duration (edge case)."""
    with pytest.raises(AssertionError):  # Expecting an AssertionError since duration is invalid
        show_spinner(duration=-1, delay=0.1)


def test_show_spinner_zero_delay():
    """Tests show_spinner with zero delay (edge case)."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.0)
    end_time = time.time()
    assert end_time - start_time > 0.9


def test_show_spinner_large_delay():
    """Tests show_spinner with a very large delay."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=2.0)
    end_time = time.time()
    assert end_time - start_time > 0.9



# Redirect stdout for testing
@pytest.fixture
def captured_output(monkeypatch):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buffer)
    yield buffer
    sys.stdout = old_stdout



import io  # Needed for captured_output fixture


def test_show_spinner_output_length(captured_output):
    show_spinner(duration=1.0, delay=0.1)
    assert len(captured_output.getvalue()) > 0  # Check if any output was produced

```

**Explanation and Improvements:**

* **`captured_output` fixture:** This crucial addition redirects standard output (`sys.stdout`) to a buffer using `monkeypatch`. This allows us to verify the output of `show_spinner` without interfering with the console.
* **Comprehensive tests for `show_spinner`:**  The tests now cover:
    * Valid duration values
    * Short duration (less than delay)
    * Zero duration
    * Negative duration (testing for expected exception)
    * Zero delay (edge case where spinner should complete quickly)
    * Large delay
* **Clearer Assertions:** The assertions are more specific and meaningful, particularly in cases like `test_show_spinner_short_duration`, ensuring that the duration is appropriately handled.
* **Import `io`:** This line is essential for the `captured_output` fixture to work correctly.
* **Output Length Check:** The test `test_show_spinner_output_length` verifies that the spinner produces some output. This is important to check for edge cases where nothing is printed.
* **`pytest.raises` for exception:** Now includes a test (`test_show_spinner_negative_duration`) that uses `pytest.raises` to check the expected exception behavior.

This revised solution provides a more robust and comprehensive set of tests for both functions, addressing potential issues and edge cases. Remember to place this test file in a suitable directory structure, likely in the same directory as `cursor_spinner.py` or a dedicated test folder.  Run it using `pytest`. Remember to install the `pytest` library if you haven't already: `pip install pytest`.