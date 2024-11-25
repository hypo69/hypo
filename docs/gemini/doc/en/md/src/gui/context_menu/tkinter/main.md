# hypotez/src/gui/context_menu/tkinter/main.py

## Overview

This module provides a GUI application for managing a custom context menu item
in Windows Explorer.  It allows users to add or remove a menu item named
"hypo AI assistant" that, when triggered, executes a Python script.  The module
interacts with the Windows Registry to modify the context menu, and includes
error handling and informative messages for the user.


## Functions

### `add_context_menu_item`

**Description**: Adds the "hypo AI assistant" context menu item to the desktop and folder background context menus.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `Exception`:  Raised if an error occurs during registry operations, such as permission issues or invalid paths.
- `FileNotFoundError`: Raised if the specified Python script file is not found. Displays an error message to the user and prevents further processing.


### `remove_context_menu_item`

**Description**: Removes the "hypo AI assistant" context menu item.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `Exception`: Raised if an error occurs during registry operations (e.g., the key doesn't exist).
- `FileNotFoundError`: Raised if the context menu item is not found; displays a warning to the user.


### `create_gui`

**Description**: Creates the main GUI window for managing the context menu item.

**Parameters**:
None

**Returns**:
None

**Raises**:
None


## Module Constants

### `MODE`

**Description**:  Stores the current mode of the application.  It's set to 'dev' in this module.


## Module Imports

```
import winreg as reg
import os
import tkinter as tk
from tkinter import messagebox
import header
from src import gs
```

**Description**: Imports necessary modules for registry access, file system operations, GUI creation, error handling, and custom modules (likely for configuration, path handling, and core functions).


```