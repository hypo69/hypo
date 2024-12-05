# hypotez/src/gui/context_menu/qt6/main.py

## Overview

This module provides functions for adding and removing a custom context menu item, "hypo AI assistant," within Windows Explorer. It utilizes the Windows Registry to modify the context menu for both the desktop and folder backgrounds. The module leverages PyQt6 for creating the GUI elements.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`add_context_menu_item`](#add_context_menu_item)
    * [`remove_context_menu_item`](#remove_context_menu_item)
* [Classes](#classes)
    * [`ContextMenuManager`](#contextmenumanager)
        * [`__init__`](#init)
        * [`initUI`](#initu)

## Functions

### `add_context_menu_item`

**Description**: Adds a custom context menu item named "hypo AI assistant" to the background of folders and the desktop in Windows Explorer.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `Exception`: If any error occurs during registry modification.  Displays a critical message box with details about the exception.

### `remove_context_menu_item`

**Description**: Removes the "hypo AI assistant" context menu item from the background context menu of folders and the desktop.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `FileNotFoundError`: If the context menu item does not exist.  Displays a warning message.
- `Exception`: If any other error occurs during registry modification. Displays a critical message box with details about the exception.


## Classes

### `ContextMenuManager`

**Description**: The main application window for managing the custom context menu item.

#### `__init__`

**Description**: Initializes the `ContextMenuManager` object. Calls the `initUI` method to set up the user interface.

**Parameters**:
None

**Returns**:
None

#### `initUI`

**Description**: Initializes the user interface with buttons to add, remove, or exit.

**Parameters**:
None

**Returns**:
None

**Implementation Details**:
- Creates a `QVBoxLayout` for vertical arrangement of UI elements.
- Adds buttons for adding the context menu item, removing it, and exiting the application.  Connects the buttons to the respective functions.
- Sets the window title.
- Sets the layout for the main window.



```
```