```python
import pytest
from PyQt6 import QtWidgets
from hypotez.src.suppliers.aliexpress.gui.styles import set_fixed_size

# Fixtures (if needed, none in this case)


# Tests for set_fixed_size function
def test_set_fixed_size_valid_input():
    """Checks correct behavior with valid input."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == width
    assert widget.height() == height

def test_set_fixed_size_positive_integers():
    """Tests with positive integer inputs."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == 100
    assert widget.height() == 200


def test_set_fixed_size_zero_width():
    """Tests with zero width."""
    widget = QtWidgets.QWidget()
    width = 0
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == 0
    assert widget.height() == 200


def test_set_fixed_size_zero_height():
    """Tests with zero height."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 0
    set_fixed_size(widget, width, height)
    assert widget.width() == 100
    assert widget.height() == 0



def test_set_fixed_size_negative_width():
    """Tests with negative width (should not raise error)."""
    widget = QtWidgets.QWidget()
    width = -10
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == -10
    assert widget.height() == 200

def test_set_fixed_size_negative_height():
    """Tests with negative height (should not raise error)."""
    widget = QtWidgets.QWidget()
    width = 100
    height = -200
    set_fixed_size(widget, width, height)
    assert widget.width() == 100
    assert widget.height() == -200



def test_set_fixed_size_non_integer_width():
    """Tests with non-integer width (should not raise error)."""
    widget = QtWidgets.QWidget()
    width = 100.5
    height = 200
    set_fixed_size(widget, width, height)
    assert widget.width() == 100
    assert widget.height() == 200  # PyQt6 might have a rounding behavior


def test_set_fixed_size_non_integer_height():
    """Tests with non-integer height (should not raise error)."""
    widget = QtWidgets.QWidget()
    width = 100
    height = 200.5
    set_fixed_size(widget, width, height)
    assert widget.width() == 100
    assert widget.height() == 200


def test_set_fixed_size_widget_is_none():
    """Tests with None widget input (should raise TypeError)."""
    with pytest.raises(TypeError):
        set_fixed_size(None, 100, 200)


def test_set_fixed_size_width_is_not_int():
    """Tests with width that is not an integer."""
    widget = QtWidgets.QWidget()
    with pytest.raises(TypeError):
        set_fixed_size(widget, "abc", 200)


def test_set_fixed_size_height_is_not_int():
    """Tests with height that is not an integer."""
    widget = QtWidgets.QWidget()
    with pytest.raises(TypeError):
        set_fixed_size(widget, 100, "def")
```