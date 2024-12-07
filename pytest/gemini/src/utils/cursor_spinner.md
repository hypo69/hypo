```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner


# Test cases for spinning_cursor
def test_spinning_cursor_basic():
    """Checks basic functionality of spinning_cursor."""
    cursor = spinning_cursor()
    assert next(cursor) == '|'
    assert next(cursor) == '/'
    assert next(cursor) == '-'
    assert next(cursor) == '\\'


def test_spinning_cursor_cycle():
    """Checks if the spinning_cursor cycles through the characters."""
    cursor = spinning_cursor()
    expected_cycle = ['|', '/', '-', '\\']
    for i in range(len(expected_cycle)):
        assert next(cursor) == expected_cycle[i % 4]


def test_spinning_cursor_exhaustion():
    """Checks that spinning_cursor generates an infinite sequence."""
    cursor = spinning_cursor()
    for _ in range(10):
        next(cursor)
    # Verify that it continues to generate new characters
    assert next(cursor) == '|'



# Test cases for show_spinner
def test_show_spinner_valid_duration():
    """Tests show_spinner with valid duration and delay."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.1)
    end_time = time.time()
    assert end_time - start_time >= 0.9  #Allow for some margin


def test_show_spinner_short_duration():
    """Tests show_spinner with a short duration."""
    start_time = time.time()
    show_spinner(duration=0.2, delay=0.05)
    end_time = time.time()
    assert end_time - start_time >= 0.15  # Ensure spinner runs for at least 0.2 seconds


def test_show_spinner_long_duration():
    """Tests show_spinner with a long duration."""
    start_time = time.time()
    show_spinner(duration=10.0, delay=0.2)
    end_time = time.time()
    assert end_time - start_time >= 9.8  # Ensure spinner runs for at least 10 seconds


def test_show_spinner_zero_delay():
    """Tests show_spinner with zero delay to avoid potential issues"""
    with pytest.raises(ValueError) as excinfo:
        show_spinner(delay=0)
    assert "Delay must be greater than 0" in str(excinfo.value)


def test_show_spinner_negative_duration():
    """Tests show_spinner with negative duration."""
    with pytest.raises(ValueError) as excinfo:
        show_spinner(duration=-1)
    assert "Duration must be a positive value" in str(excinfo.value)

def test_show_spinner_negative_delay():
    """Tests show_spinner with negative delay."""
    with pytest.raises(ValueError) as excinfo:
        show_spinner(delay=-0.1)
    assert "Delay must be a positive value" in str(excinfo.value)


# Capture stdout for testing the printing and backspacing correctly
@pytest.fixture
def captured_output():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    yield mystdout
    sys.stdout = old_stdout


from io import StringIO
def test_show_spinner_output(captured_output):
    show_spinner(duration=0.3, delay=0.1)
    output = captured_output.getvalue()
    assert len(output) > 0

```