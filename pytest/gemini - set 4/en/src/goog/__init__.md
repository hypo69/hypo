```python
import pytest
from hypotez.src.goog import SpreadSheet

# No test data or fixtures are needed for this code snippet
# as it only contains module imports and a constant definition

def test_mode_exists():
    """Checks that the MODE constant exists and is a string."""
    assert hasattr(SpreadSheet, 'MODE')
    assert isinstance(SpreadSheet.MODE, str)

def test_mode_value():
    """Checks the value of the MODE constant."""
    assert SpreadSheet.MODE == 'dev'


def test_spreadsheet_class_exists():
    """Check if the SpreadSheet class is defined."""
    assert hasattr(SpreadSheet, '__name__')
    assert SpreadSheet.__name__ == 'Spreadsheet'
```