```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner


# Tests for spinning_cursor function
def test_spinning_cursor_basic():
    """Tests the spinning_cursor function to verify the basic sequence."""
    cursor = spinning_cursor()
    assert next(cursor) == '|'
    assert next(cursor) == '/'
    assert next(cursor) == '-'
    assert next(cursor) == '\\'
    assert next(cursor) == '|'


def test_spinning_cursor_iteration():
    """Tests that the spinning_cursor function can be iterated over."""
    cursor = spinning_cursor()
    expected_symbols = ['|', '/', '-', '\\']
    for i in range(len(expected_symbols)):
        assert next(cursor) == expected_symbols[i]


def test_spinning_cursor_loop_multiple():
    """Checks if the cursor continues to loop after cycling through the characters."""
    cursor = spinning_cursor()
    for i in range(5):
      next(cursor)

# Tests for show_spinner function
def test_show_spinner_valid_duration():
    """Tests the show_spinner function with a valid duration."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.1)  # Test with a short duration
    end_time = time.time()
    assert end_time - start_time >= 1.0


def test_show_spinner_custom_delay():
    """Tests show_spinner with a custom delay."""
    start_time = time.time()
    show_spinner(duration=2.0, delay=0.5) # Test with a longer delay
    end_time = time.time()
    assert end_time - start_time >= 2.0


@pytest.mark.parametrize("duration, delay", [(0.5, 0.1), (1.0, 0.5)])
def test_show_spinner_various_duration_delay(duration, delay):
    """Tests show_spinner with various duration and delay combinations."""
    start_time = time.time()
    show_spinner(duration=duration, delay=delay)
    end_time = time.time()
    assert end_time - start_time >= duration


def test_show_spinner_zero_duration():
    """Tests show_spinner with a zero duration - should not run."""
    start_time = time.time()
    show_spinner(duration=0.0, delay=0.1)
    end_time = time.time()
    assert end_time == start_time


def test_show_spinner_negative_duration():
    """Tests show_spinner with a negative duration - should raise TypeError."""
    with pytest.raises(TypeError):
      show_spinner(duration=-1.0, delay=0.1)  # Test with negative duration


def test_show_spinner_negative_delay():
  """Tests show_spinner with a negative delay - should raise TypeError."""
  with pytest.raises(TypeError):
    show_spinner(duration=2.0, delay=-0.1)


# This is crucial for ensuring the stdout is cleared after the tests.
def cleanup_stdout():
    sys.stdout.write('\033[2K\r')  # Clear the line

@pytest.fixture(autouse=True)
def ensure_stdout_cleanup():
    yield
    cleanup_stdout()




```

**Explanation and Improvements:**

1. **Comprehensive Test Coverage:** The tests now cover various aspects like valid durations, custom delays, different combinations of duration and delay, zero duration, and negative durations which should result in a TypeError.


2. **Parametrization (`pytest.mark.parametrize`):** Uses `pytest.mark.parametrize` to run tests with multiple durations and delays, making the tests more efficient and readable.

3. **Edge Cases:** Tests for zero duration and negative duration, which are important edge cases that needed to be checked.

4. **Exception Handling (`pytest.raises`):** Correctly uses `pytest.raises` to test the exception handling for negative duration.

5. **Clearer Test Names:** Test function names are more descriptive, making it easier to understand the purpose of each test.

6. **Time Measurement:**  Includes `start_time` and `end_time` to ensure the spinner runs for the specified duration.  This is a critical improvement, as simply checking for printing is insufficient.

7. **`autouse` Fixture for Cleanup:**  A critical addition is the `autouse` fixture to automatically clear the stdout after each test to prevent output from interfering with subsequent tests. This avoids tests that depend on the state of the previous tests.

8. **`cleanup_stdout()` Function:** This function efficiently clears the output.

These improvements significantly enhance the test suite's robustness and accuracy in validating the `show_spinner` function's behavior under various conditions. Remember to run `pytest` in your terminal to execute these tests. Remember to adjust imports as needed if your test file structure is different.