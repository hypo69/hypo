# hypotez/src/gui/context_menu/qt6/main.py

## Overview

This module provides a PyQt6-based application for managing a custom context menu item (named 'hypo AI assistant') in Windows Explorer.  It allows users to add or remove this item from the context menu displayed when right-clicking empty spaces on the desktop or within folders. The module interacts with the Windows Registry to achieve this functionality.


## Classes

### `ContextMenuManager`

**Description**: The main application window for managing the context menu. It provides buttons to add, remove, or exit the application.

**Methods**

- `__init__`(): Initializes the `ContextMenuManager` window with the UI elements.
- `initUI`(): Sets up the user interface by creating buttons for adding/removing the context menu item and exiting the application.  The buttons are connected to the corresponding functions (`add_context_menu_item`, `remove_context_menu_item`, and `close`).


## Functions

### `add_context_menu_item`

**Description**: Adds the 'hypo AI assistant' context menu item to the background context menu of folders and the desktop in Windows Explorer. This is achieved by creating the necessary registry keys.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `Exception`: Any error encountered during the registry interaction.  Displays an error message using `QtWidgets.QMessageBox.critical` if the script file (`command_path`) specified in the registry isn't found.


### `remove_context_menu_item`

**Description**: Removes the 'hypo AI assistant' context menu item from the background context menu of folders and the desktop in Windows Explorer.

**Parameters**:
None

**Returns**:
None

**Raises**:
- `FileNotFoundError`: If the context menu item doesn't exist. Displays a warning message.
- `Exception`: Any other error during registry interaction. Displays an error message.


## Variables

### `MODE`

**Description**: A string variable, likely indicating the current application mode (e.g., 'dev', 'prod').

### `key_path`
**Description**: The path to the registry key in the Windows registry for storing the context menu item settings.


## Module Level Documentation

**Description**: The module implements the logic for adding or removing a context menu item to the Windows Explorer background context menu for folders and the desktop.

**Imports:**

- `winreg as reg`: Used for interacting with the Windows Registry.
- `os`: Used for OS path manipulation and checks.
- `PyQt6`: Used for GUI creation.
- `header`: Custom import, assumed to contain settings or constants.
- `src.gs`: Custom import, likely for project paths or settings.


## Usage Example

```python
# Example of how to use the module
from hypotez.src.gui.context_menu.qt6.main import add_context_menu_item, remove_context_menu_item, ContextMenuManager

# Add the context menu item
add_context_menu_item()

# Or remove it
remove_context_menu_item()

# Alternatively, to run the GUI application
if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # Initialize the Qt application
    window = ContextMenuManager()    # Create the main window
    window.show()  # Make the window visible
    app.exec()  # Enter the Qt application event loop
```

**Note**:  This documentation assumes the existence of `gs` and `header` modules within the `src` directory and that they provide necessary functions or constants.  The exact paths and interactions will vary based on your project's structure.