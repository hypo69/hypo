```python
import pytest
from PyQt6 import QtWidgets
from hypotez.src.suppliers.aliexpress.gui.styles import set_fixed_size

# Fixture definitions (if needed, but not in this case)
# @pytest.fixture
# def example_widget():
#     return QtWidgets.QWidget()


def test_set_fixed_size_valid_input():
    """Checks correct behavior with valid input."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_zero_width():
    """Checks behavior with zero width."""
    widget = QtWidgets.QWidget()
    width = 0
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_zero_height():
    """Checks behavior with zero height."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 0
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_negative_width():
    """Checks behavior with negative width (should still set)."""
    widget = QtWidgets.QWidget()
    width = -100
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height


def test_set_fixed_size_negative_height():
    """Checks behavior with negative height (should still set)."""
    widget = QtWidgets.QWidget()
    width = 100
    height = -200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height



def test_set_fixed_size_non_integer_width():
    """Checks behavior with non-integer width (should still set)."""
    widget = QtWidgets.QWidget()
    width = 100.5
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == int(width)  # Important: Check the integer value
    assert widget.height() == height



def test_set_fixed_size_non_integer_height():
    """Checks behavior with non-integer height (should still set)."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 200.5
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == int(height) # Important: Check the integer value


def test_set_fixed_size_with_none_widget():
    """Checks behavior with None widget (should not crash)."""
    with pytest.raises(AttributeError):
        set_fixed_size(None, 100, 200)



def test_set_fixed_size_with_invalid_widget_type():
  """Check with invalid widget type (e.g., str)."""
  with pytest.raises(AttributeError):
      set_fixed_size("not_a_widget", 100, 200)


```