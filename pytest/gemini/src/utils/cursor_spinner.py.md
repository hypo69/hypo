```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner


def test_spinning_cursor_cycle():
    """Test that the spinning_cursor generator cycles correctly through the symbols."""
    cursor = spinning_cursor()
    assert next(cursor) == '|'
    assert next(cursor) == '/'
    assert next(cursor) == '-'
    assert next(cursor) == '\\'
    assert next(cursor) == '|'  # Check if it loops back


def test_show_spinner_valid_duration():
    """Test that show_spinner runs for approximately the specified duration."""
    duration = 0.3
    start_time = time.time()
    show_spinner(duration=duration, delay=0.05)
    end_time = time.time()
    elapsed_time = end_time - start_time
    # We use an approximate check because time.sleep() isn't exact, and some time is used for overhead
    assert duration - 0.1 <= elapsed_time <= duration + 0.1


def test_show_spinner_short_duration():
     """Test that show_spinner functions correctly with short duration."""
     duration = 0.01  # very short duration
     start_time = time.time()
     show_spinner(duration=duration, delay=0.001)
     end_time = time.time()
     elapsed_time = end_time - start_time
     assert duration - 0.01 <= elapsed_time <= duration + 0.01


def test_show_spinner_zero_duration():
     """Test that show_spinner functions correctly when given zero duration."""
     duration = 0.0
     start_time = time.time()
     show_spinner(duration=duration, delay=0.001)
     end_time = time.time()
     elapsed_time = end_time - start_time
     assert elapsed_time <= 0.01 # Expect it to be almost instant


def test_show_spinner_default_values():
     """Test show_spinner with default arguments. This test will be hard to check exactly."""
     start_time = time.time()
     show_spinner() # default duration is 5 seconds and delay is 0.1
     end_time = time.time()
     elapsed_time = end_time - start_time
     assert 4.9 <= elapsed_time <= 5.1 # Check if it runs approximately for 5 seconds


def test_show_spinner_negative_duration():
     """Test show_spinner with a negative duration. Should not raise an exception and exit quickly."""
     duration = -1
     start_time = time.time()
     show_spinner(duration=duration, delay=0.1)
     end_time = time.time()
     elapsed_time = end_time - start_time
     assert elapsed_time < 0.1 # Expect it to exit quickly.


def test_show_spinner_small_delay():
    """Test show_spinner with very short delay."""
    duration = 0.1
    start_time = time.time()
    show_spinner(duration=duration, delay=0.001)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert duration - 0.05 <= elapsed_time <= duration + 0.05
```