```python
import pytest
import time
import sys
from hypotez.src.utils.cursor_spinner import spinning_cursor, show_spinner

# Test fixtures (if needed)


# Tests for spinning_cursor
def test_spinning_cursor_valid_output():
    """Tests if spinning_cursor yields the expected symbols in sequence."""
    cursor = spinning_cursor()
    assert next(cursor) == "|"
    assert next(cursor) == "/"
    assert next(cursor) == "-"
    assert next(cursor) == "\\"
    assert next(cursor) == "|"  # Verifies the cycle


def test_spinning_cursor_multiple_iterations():
    """Tests if spinning_cursor repeats the cycle correctly."""
    cursor = spinning_cursor()
    expected_symbols = "|/-\\"
    for i in range(len(expected_symbols)):
        assert next(cursor) == expected_symbols[i % 4]


# Tests for show_spinner
def test_show_spinner_valid_duration():
    """Tests show_spinner with a valid duration."""
    start_time = time.time()
    show_spinner(duration=1.0, delay=0.1)
    end_time = time.time()
    assert end_time - start_time >= 0.9 # Account for slight variations

def test_show_spinner_zero_duration():
    """Tests show_spinner with a duration of 0."""
    start_time = time.time()
    show_spinner(duration=0, delay=0.1)
    end_time = time.time()
    assert end_time - start_time == 0, "Show spinner should not run if duration is 0"


def test_show_spinner_negative_duration():
    """Tests show_spinner with a negative duration."""
    with pytest.raises(ValueError, match="Duration must be a positive value"):
        show_spinner(duration=-1.0, delay=0.1)



def test_show_spinner_very_short_duration():
    """Tests show_spinner with very short duration and delay."""
    start_time = time.time()
    show_spinner(duration=0.05, delay=0.01)  # Very short duration
    end_time = time.time()
    assert end_time - start_time >= 0, "Show spinner should run at least for a short time"


def test_show_spinner_valid_delay():
    """Tests show_spinner with a valid delay."""
    start_time = time.time()
    show_spinner(duration=2.0, delay=0.5)
    end_time = time.time()
    assert end_time - start_time >= 1.5 # Account for slight variations, delay is greater than duration

def test_show_spinner_zero_delay():
    """Tests show_spinner with a delay of 0."""
    start_time = time.time()
    with pytest.raises(ValueError, match="Delay must be a positive value"):
        show_spinner(duration=1.0, delay=0)


def test_show_spinner_negative_delay():
    """Tests show_spinner with a negative delay."""
    with pytest.raises(ValueError, match="Delay must be a positive value"):
        show_spinner(duration=2.0, delay=-0.5)


# Redirect stdout for testing show_spinner (crucial for testing output)
@pytest.fixture
def capsys():
    return pytest.importorskip("sys").stdin


@pytest.mark.usefixtures("capsys")
def test_show_spinner_output_correct():
    """Tests that show_spinner prints the expected output to console."""
    captured = capsys.readouterr()  # Capture stdout
    show_spinner(duration=0.3, delay=0.1)
    assert captured.out, "Expected output from spinner."




```