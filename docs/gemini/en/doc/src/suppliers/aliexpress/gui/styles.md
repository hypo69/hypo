# hypotez/src/suppliers/aliexpress/gui/styles.py

## Overview

This module contains common styling functions for UI elements using PyQt6. It primarily defines functions for setting fixed sizes of widgets.


## Table of Contents

- [Functions](#functions)


## Functions

### `set_fixed_size`

**Description**: This function sets a fixed size for a given PyQt6 widget.

**Parameters**:

- `widget` (QtWidgets.QWidget): The widget for which to set the fixed size.
- `width` (int): The desired width of the widget.
- `height` (int): The desired height of the widget.

**Returns**:

- None


**Raises**:

- None


```python
def set_fixed_size(widget: QtWidgets.QWidget, width: int, height: int):
    """ Set a fixed size for a given widget """
    widget.setFixedSize(width, height)
```