# hypotez/src/gui/context_menu/tkinter/main.py

## Overview

This module provides a Tkinter-based graphical user interface (GUI) for managing a custom context menu item, "hypo AI assistant," within Windows Explorer.  It allows users to add or remove this item from the context menu that appears when right-clicking on empty areas of the desktop or folders.  The module utilizes the Windows Registry to achieve this.

## Table of Contents

* [Functions](#functions)
    * [`add_context_menu_item`](#add_context_menu_item)
    * [`remove_context_menu_item`](#remove_context_menu_item)
    * [`create_gui`](#create_gui)

## Functions

### `add_context_menu_item`

**Description**: Adds the "hypo AI assistant" context menu item to the background of folders and the desktop.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `FileNotFoundError`: Raised if the specified Python script file (`command_path`) does not exist.
- `Exception`: Raised for other errors during registry operations. Displays an error message to the user.


### `remove_context_menu_item`

**Description**: Removes the "hypo AI assistant" context menu item.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `FileNotFoundError`: Raised if the registry key for the context menu item is not found. Displays a warning to the user.
- `Exception`: Raised for other errors during registry operations. Displays an error message to the user.


### `create_gui`

**Description**: Creates a Tkinter GUI for managing the context menu item.

**Parameters**:
None

**Returns**:
None

**Raises**:
- None