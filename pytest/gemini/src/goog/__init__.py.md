```python
import pytest

from hypotez.src.goog import SpreadSheet, MODE


def test_mode_is_dev():
    """Verify that the global variable MODE is set to 'dev'."""
    assert MODE == 'dev'


def test_spreadsheet_class_exists():
    """Verify that the SpreadSheet class is available."""
    assert SpreadSheet is not None


def test_spreadsheet_class_is_callable():
    """Verify that the SpreadSheet class can be instantiated without arguments."""
    try:
        SpreadSheet()
    except Exception as e:
        pytest.fail(f"SpreadSheet class instantiation failed: {e}")


def test_spreadsheet_instantiation_with_no_args():
    """Verify that Spreadsheet can be instantiated without arguments."""
    spreadsheet = SpreadSheet()
    assert isinstance(spreadsheet, SpreadSheet)
```