# hypotez/src/suppliers/aliexpress/gui/styles.py

## Overview

This module contains styling functions for UI elements in the AliExpress supplier GUI.

## Table of Contents

* [set_fixed_size](#set_fixed_size)

## Functions

### `set_fixed_size`

**Description**: Sets a fixed size for a given widget.

**Parameters**:
- `widget` (QtWidgets.QWidget): The widget to set the size for.
- `width` (int): The desired width of the widget.
- `height` (int): The desired height of the widget.

**Returns**:
- None

**Raises**:
- `TypeError`: If `widget` is not a `QtWidgets.QWidget`, `width` or `height` are not integers.


```python
def set_fixed_size(widget: QtWidgets.QWidget, width: int, height: int):
    """ Set a fixed size for a given widget """
    widget.setFixedSize(width, height)