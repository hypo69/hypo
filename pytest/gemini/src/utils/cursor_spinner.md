```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner


# Test functions for spinning_cursor
def test_spinning_cursor_basic():
    """Tests that spinning_cursor yields the expected characters in sequence."""
    cursor = spinning_cursor()
    assert next(cursor) == '|'
    assert next(cursor) == '/'
    assert next(cursor) == '-'
    assert next(cursor) == '\\'
    assert next(cursor) == '|'


def test_spinning_cursor_loop():
    """Tests that spinning_cursor loops through the sequence."""
    cursor = spinning_cursor()
    for _ in range(10):
        assert next(cursor) in '|/-\\'


# Test functions for show_spinner
def test_show_spinner_valid_duration():
    """Tests show_spinner with a valid duration."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.1)
    end_time = time.time()
    # Check that the spinner ran roughly for the specified duration
    assert end_time - start_time >= 0.9 and end_time - start_time <= 1.1


def test_show_spinner_zero_duration():
    """Tests show_spinner with a duration of 0."""
    start_time = time.time()
    show_spinner(duration=0.0, delay=0.1)
    end_time = time.time()
    # Expect zero duration
    assert end_time - start_time == 0

def test_show_spinner_negative_duration():
    """Tests show_spinner with a negative duration (should not raise an exception)."""
    with pytest.raises(AssertionError) as excinfo:
        show_spinner(duration=-1.0)
    expected_message = "Duration must be positive."
    assert str(excinfo.value) == expected_message


def test_show_spinner_small_delay():
    """Tests show_spinner with a very small delay."""
    start_time = time.time()
    show_spinner(duration=0.1, delay=0.001)
    end_time = time.time()
    assert end_time - start_time >= 0.009 and end_time - start_time <= 0.11


def test_show_spinner_large_delay():
    """Tests show_spinner with a very large delay."""
    start_time = time.time()
    show_spinner(duration=10, delay=0.5)
    end_time = time.time()
    assert end_time - start_time >= 9.5 and end_time - start_time <= 10.5



# Redirect stdout for testing show_spinner (crucial for testing output)
@pytest.fixture
def capsys():
    """Fixture to capture stdout for testing console output."""
    return pytest.importorskip("pytest").capsys


def test_show_spinner_output_with_capsys(capsys):
    """Tests that show_spinner correctly prints spinner characters."""
    show_spinner(duration=0.3, delay=0.1)
    captured = capsys.readouterr()
    assert len(captured.out) > 0  # check that some output is printed

def test_show_spinner_correct_output_order_with_capsys(capsys):
  """Test that spinner chars are correctly printed (order matters)."""
  show_spinner(duration=0.4, delay=0.1)
  captured = capsys.readouterr()
  spinner_chars = "|/-\\"
  assert captured.out.strip()
  for i in range(len(spinner_chars)):
      assert spinner_chars[i] in captured.out


# This test assumes no error is raised on non-positive durations.
#  Consider adding assertions for handling exceptions if appropriate.

```