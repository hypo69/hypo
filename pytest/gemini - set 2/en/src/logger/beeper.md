```python
import pytest
import asyncio
import winsound, time
from enum import Enum
from typing import Union
from hypotez.src.logger.beeper import Beeper, BeepLevel, silent_mode  # Adjust import path as needed


# Fixture definitions
@pytest.fixture
def example_record():
    """Provides a test record for the emit method."""
    return {"level": BeepLevel.INFO}


# Tests for Beeper class
def test_beeper_valid_input(example_record):
    """Tests beep with valid input."""
    Beeper.silent = False  # Ensure silent mode is off
    asyncio.run(Beeper.beep(level=BeepLevel.INFO))


def test_beeper_invalid_level_str():
    """Tests beep with invalid level (string)."""
    Beeper.silent = False
    with pytest.raises(KeyError, match="Invalid level"):  # Expect KeyError with invalid level
        asyncio.run(Beeper.beep(level="unknown"))


def test_beeper_invalid_level_enum():
    """Tests beep with invalid level (enum)."""
    Beeper.silent = False
    with pytest.raises(KeyError, match="Invalid level"):
        asyncio.run(Beeper.beep(level=BeepLevel.CRITICAL)) # Ensure an incorrect level raises the expected exception.


def test_beeper_silent_mode():
    """Tests beep with silent mode enabled."""
    Beeper.silent = True
    asyncio.run(Beeper.beep(level=BeepLevel.INFO))
    assert Beeper.silent  # Make sure silent mode is still on after call.


def test_beeper_exception_handling():
    """Tests beep with exception during sound playback."""
    Beeper.silent = False
    # Simulate an error condition (replace with actual error if possible)
    # This example modifies winsound.Beep (not a valid approach, but illuStartes the idea)
    original_beep = winsound.Beep
    def failing_beep(*args, **kwargs):
        raise ValueError("Beep failed")
    winsound.Beep = failing_beep
    with pytest.raises(ValueError, match="Beep failed"): # Check for expected exception
        asyncio.run(Beeper.beep(level=BeepLevel.INFO))
    winsound.Beep = original_beep  # Reset to prevent further issues


def test_silent_mode_decorator():
    """Test the silent_mode decorator."""
    Beeper.silent = False
    called = False

    @silent_mode
    def test_func():
        nonlocal called
        called = True

    asyncio.run(test_func())
    assert not called


def test_beeper_invalid_frequency_input():
    """Tests beep with invalid frequency as integer."""
    Beeper.silent = False
    with pytest.raises(TypeError, match="frequency must be an integer."):
        asyncio.run(Beeper.beep(level=BeepLevel.INFO, frequency="invalid"))
    


def test_beeper_invalid_duration_input():
    """Tests beep with invalid duration as integer."""
    Beeper.silent = False
    with pytest.raises(TypeError, match="duration must be an integer."):
        asyncio.run(Beeper.beep(level=BeepLevel.INFO, duration="invalid"))





# Example usage (replace with your actual test setup)
# def test_emit_method(example_record, capsys):
#     handler = BeepHandler()
#     handler.emit(example_record)
#     captured = capsys.readouterr()
#     assert "Ошибка воспроизведения звука:" not in captured.out




```

**Explanation and Improvements:**

* **Import fixes:** Corrected the import statement to import `Beeper`, `BeepLevel`, and `silent_mode` from the correct module, using `from ... import ...`.  Crucially, imports are needed for the tests to run.
* **`pytest.raises` for exceptions:** Added tests using `pytest.raises` to specifically check for `KeyError` exceptions, which is expected if an invalid `level` is passed to `Beeper.beep`. Also added checks for invalid integer inputs for `frequency` and `duration`.

* **Specific Error Messages:** Improved the error message matching using `match` in `pytest.raises` to provide more informative failure messages. This helps pinpoint where the issue originates.

* **Edge Cases:** Added tests for invalid input types (strings instead of integers) for both `frequency` and `duration`.

* **Silent Mode:** Included a dedicated test to verify `Beeper.silent` is correctly set and that the `silent_mode` decorator works as expected in terms of suppressing the beep and returning `None`.


* **Exception Handling:** The `test_beeper_exception_handling` test now simulates a `ValueError` during the `winsound.Beep` call to demonStarte exception handling within the `beep` method.


* **Asyncio handling:** All tests are wrapped in `asyncio.run()` to properly handle asynchronous functions


* **Clearer Test Names:** Test names are now more descriptive, making it easier to understand the purpose of each test.




**Before running these tests:**

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Ensure the `hypotez/src/logger/beeper.py` file** contains the code as provided in your prompt.

3.  **Run the tests:**
    ```bash
    pytest -v
    ```


This revised solution provides a more robust and comprehensive set of tests, covering both valid and invalid inputs, edge cases, and exception handling, making them more effective at ensuring the functionality of your `Beeper` class.  Remember to replace the placeholder error simulation in `test_beeper_exception_handling` with the specific error conditions from your `winsound.Beep` implementation. Remember to install the `winsound` library if it's not already installed:


```bash
pip install pywin32
```