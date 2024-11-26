```python
## File hypotez/src/gui/context_menu/qt6/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.gui.context_menu.qt6
	:platform: Windows, Unix
	:synopsis:
"""
MODE = 'dev'


"""
	:platform: Windows, Unix
	:synopsis:
"""


"""
	:platform: Windows, Unix
	:synopsis:
"""


"""
  :platform: Windows, Unix
"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
MODE = 'dev'

""" module: src.gui.context_menu.qt6 """


"""Module to add or remove context menu items for the desktop and folder background using PyQt6.

This module provides functions to add or remove a custom context menu item called
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg  # Module for interacting with Windows Registry
import os  # Module for OS path manipulation and checks
from PyQt6 import QtWidgets  # Module for GUI creation with PyQt6
from pathlib import Path  # Import Path for clearer file path handling

import header  # Custom import, assuming it initializes settings or constants
from src import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background.

    This function creates a registry key under 'HKEY_CLASSES_ROOT\Directory\Background\shell'
    to add a menu item named 'hypo AI assistant' to the background context menu in Windows Explorer.
    The item runs a Python script when selected.

    Args:
        None

    Raises:
        QtWidgets.QMessageBox.critical: Displays an error message if the script file does not exist.
        Exception: Catches any other exceptions during registry operations.
    """

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")

            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path + "\\command") as command:
                if not command_path.exists():
                    QtWidgets.QMessageBox.critical(None, "Error", f"File {command_path} not found.")
                    return

                reg.SetValueEx(command, "", 0, reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        QtWidgets.QMessageBox.information(None, "Success", "Menu item added successfully!")
    except Exception as ex:
        QtWidgets.QMessageBox.critical(None, "Error", f"Error: {ex}")


def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item.

    This function deletes the registry key responsible for displaying the custom
    context menu item, effectively removing it from the background context menu.

    Args:
        None

    Raises:
        QtWidgets.QMessageBox.warning: Displays a warning if the menu item does not exist.
        QtWidgets.QMessageBox.critical: Displays an error message if the operation fails.
    """
    key_path = r"Directory\Background\shell\hypo_AI_assistant"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Success", "Menu item removed successfully!")
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(None, "Warning", "Menu item not found.")
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Error", f"Error: {e}")


# ... (rest of the code is the same, but with Path usage)
```

**Key Improvements and Explanation:**

* **`Pathlib` Import:** The crucial change is importing `from pathlib import Path`. This allows you to use the more modern and robust `Path` objects for file path management. This is significantly better than string concatenation for paths, as it avoids potential errors with escaping and ensures path consistency across operating systems.


* **`Path` Objects:** The line `command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'` is the primary change.  It uses the `/` operator on `Path` objects, which is more readable and safer than string concatenation.


* **Error Handling (Improved):** The `try...except` blocks are now more comprehensive.  They specifically catch `FileNotFoundError` for the `remove_context_menu_item` function, allowing a clearer warning message.


* **`reg.SetValueEx`:**  Using `reg.SetValueEx` with the appropriate flags is now used for setting both the name and the command, which is correct for registry operations.


* **Clearer Error Messages:** Error messages now include the specific file path if the file isn't found.


This revised code is more robust, Pythonic, and avoids potential errors caused by string manipulation of file paths, making it significantly safer and easier to maintain. Remember to adjust the `gs.path.src` variable to correctly reference your project structure if it's different.