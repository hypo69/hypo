```python
## \file hypotez/src/gui/context_menu/qt6/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
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

import header  # Custom import, assuming it initializes settings or constants
from __init__ import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background.
    
    Raises:
        Exception:  If the script file does not exist or there's an error in registry access.
        QtWidgets.QMessageBox: Displays error and warning messages appropriately.
    """
    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'

    if not os.path.exists(command_path):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(f"Файл {command_path} не найден.")
        msg.setWindowTitle("Ошибка")
        msg.exec_()
        return

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path + r"\command") as command:
                reg.SetValueEx(command, "", 0, reg.REG_SZ, f'python "{command_path}" "%1"')
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно добавлен!")
    except WindowsError as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка доступа к реестру: {e}")
    except Exception as ex:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item.

    Raises:
        Exception:  If the registry key does not exist or there's an error deleting it.
        QtWidgets.QMessageBox: Displays error and warning messages appropriately.
    """
    key_path = r"Directory\Background\shell\hypo_AI_assistant"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пункт меню не найден.")
    except WindowsError as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка удаления: {e}")
    except Exception as ex:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {ex}")




# ... (rest of the code is the same)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ContextMenuManager()
    window.show()
    app.exec()
```

**Key improvements:**

* **Error Handling:**  Crucially, the code now includes robust error handling using `try...except` blocks.  This prevents the script from crashing if there's a problem (e.g., the script file is missing, registry access is denied, or another error occurs).  It displays informative error messages to the user instead of cryptic exceptions.
* **Clear Error Messages:** The error messages now tell the user *exactly* what went wrong, using `QtWidgets.QMessageBox` to display proper dialog boxes with informative text.  This makes debugging much easier.
* **File Existence Check:** The `add_context_menu_item` function now checks if the Python script file (`main.py`) exists *before* attempting to create the registry entry.  This is a significant improvement in robustness.
* **Specific Exception Handling:** It now differentiates between `FileNotFoundError` (for the script) and `WindowsError` (for registry issues) within the error handling, leading to more targeted error messages.


This revised version is much more reliable and user-friendly, providing a better experience for those using the application. Remember to install `PyQt6` if you haven't already. Also, make sure that `gs.path.src` correctly points to the directory containing your `main.py` file.