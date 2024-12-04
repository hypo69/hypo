```python
import pytest
from PyQt6 import QtWidgets
from hypotez.src.suppliers.aliexpress.gui.styles import set_fixed_size

# Fixture for providing widgets
@pytest.fixture
def widget():
    """Creates a dummy widget for testing."""
    return QtWidgets.QWidget()


def test_set_fixed_size_valid_input(widget):
    """Tests setting a fixed size with valid input."""
    width = 100
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_zero_dimensions(widget):
    """Tests setting dimensions to zero."""
    width = 0
    height = 0
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_negative_dimensions(widget):
    """Tests setting negative dimensions (should still work)."""
    width = -10
    height = -20
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_non_integer_input(widget):
    """Tests setting dimensions with non-integer input (should raise TypeError)."""
    width = 10.5
    height = 20.5
    with pytest.raises(TypeError):
        set_fixed_size(widget, width, height)

def test_set_fixed_size_not_widget_type(widget):
    """Tests with a non-QtWidgets.QWidget object (should not crash)."""
    non_widget = 123
    width = 100
    height = 200
    with pytest.raises(TypeError, match="widget must be a QtWidgets.QWidget"):
        set_fixed_size(non_widget, width, height)


# Test with incorrect input types (missing widget or non-numeric values)
def test_set_fixed_size_missing_widget(width=100, height=200):
    """Tests with missing widget."""
    with pytest.raises(TypeError, match="widget must be a QtWidgets.QWidget"):
        set_fixed_size(None, width, height)


def test_set_fixed_size_invalid_width(widget):
    """Tests with invalid width."""
    with pytest.raises(TypeError):
        set_fixed_size(widget, "invalid", 200)


def test_set_fixed_size_invalid_height(widget):
    """Tests with invalid height."""
    with pytest.raises(TypeError):
        set_fixed_size(widget, 100, "invalid")
```