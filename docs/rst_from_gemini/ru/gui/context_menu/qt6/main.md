```python
## \file hypotez/src/gui/context_menu/qt6/main.py
# -*- coding: utf-8 -*-

""" module: src.gui.context_menu.qt6 """
MODE = 'debug'
""" module: src.gui.context_menu.qt6 """
MODE = 'debug'

"""Module to add or remove context menu items for the desktop and folder background using PyQt6.

This module provides functions to add or remove a custom context menu item called 
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg
import os
from PyQt6 import QtWidgets
import sys  # Import sys for handling exceptions gracefully
import header  # Custom import, assuming it initializes settings or constants
from __init__ import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_key = rf"{key_path}\command"

    try:
        # Create the necessary registry keys, handling potential errors.
        with reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path, 0, reg.KEY_ALL_ACCESS, 0) as key:
          reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")
        
        with reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, command_key, 0, reg.KEY_ALL_ACCESS, 0) as command:
          command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
          if not os.path.exists(command_path):
              raise FileNotFoundError(f"Файл {command_path} не найден.")
          
          reg.SetValueEx(command, "", 0, reg.REG_SZ, f"python \"{command_path}\" \"%1\"")

        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно добавлен!")
    except FileNotFoundError as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", str(e))  # Display a more descriptive error
        print(f"Error: {e}", file=sys.stderr)  # Print error to console
        return
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {e}")
        print(f"Error: {e}", file=sys.stderr)
        return
  
def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {e}")
        print(f"Error: {e}", file=sys.stderr)  # Print error to console


# ... (Rest of the code remains the same)
```

**Key improvements:**

* **Error Handling:** The code now includes robust error handling using `try...except` blocks.  This is crucial for dealing with potential issues like the file not being found, registry access problems, and other exceptions.  It catches `FileNotFoundError` explicitly and displays more informative error messages.  Error messages are also printed to the console using `print(f"Error: {e}", file=sys.stderr)`. This is vital for debugging and seeing the *exact* error message, especially if the error is inside a Windows Registry operation that might not produce a clear user-facing message.  Crucially, `return` is used after each `except` block to prevent further execution if an error occurs.
* **`CreateKeyEx`:**  `reg.CreateKeyEx` is now used to create the registry keys. This gives more control over how the keys are created and potentially prevents some errors.
* **`SetValueEx`:**  Uses `reg.SetValueEx` which is preferred for its flexibility and better error handling compared to the older `reg.SetValue`.
* **Clearer Error Messages:**  The error messages are more informative.  Instead of just saying "Ошибка", it now tells the user what the problem *was*.
* **Console Output:**  Crucially, errors are logged to the console. This helps diagnose problems when running the script in the terminal. Using `sys.stderr` ensures that error messages are printed even if the GUI is interacting with the user.

**Additional Recommendations:**

* **Logging:**  Instead of using `print` directly for errors, consider a more robust logging mechanism (e.g., `logging` module) for better organization and control of output.
* **More specific exception handling:** Consider catching specific exceptions like `WindowsError` or other registry-related errors, and providing more detailed error messages for those cases.  This will allow for more tailored handling of different error scenarios.
* **Input Validation:**  In a production environment, validate the input parameters to the functions (`add_context_menu_item` and `remove_context_menu_item`) to prevent unexpected behavior.


By implementing these improvements, your code becomes significantly more robust and reliable, especially in a production environment. Remember to install the PyQt6 library if you haven't already. `pip install pyqt6`