```python
## \file hypotez/src/gui/context_menu/tkinter/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.gui.context_menu.tkinter """
MODE = 'debug'
""" module: src.gui.context_menu.tkinter """
MODE = 'debug'

"""Module to add or remove context menu items for the desktop and folder background.

This module provides functions to add or remove a custom context menu item called 
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg  # Module for interacting with Windows Registry
import os  # Module for OS path manipulation and checks
import tkinter as tk  # Module for GUI creation
from tkinter import messagebox  # Submodule for GUI message boxes
import sys  # Import sys for system-level operations (essential!)

import header  # Custom import, assuming it initializes settings or constants
from src import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_key = rf"{key_path}\command"

    try:
        # Crucial: check if the script exists *before* attempting registry access.
        command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
        if not os.path.exists(command_path):
            messagebox.showerror("Ошибка", f"Файл скрипта {command_path} не найден.")
            return  # Exit if the script doesn't exist


        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")  # Correctly set the name
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                # Use sys.executable to get the current Python interpreter
                reg.SetValueEx(command, "", 0, reg.REG_SZ, f'"{sys.executable}" "{command_path}" "%1"')  

        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")

    except OSError as e:
        # More specific error handling for registry issues
        messagebox.showerror("Ошибка", f"Ошибка при работе с реестром: {e}")
    except Exception as ex:
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")

def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        messagebox.showinfo("Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        messagebox.showwarning("Предупреждение", "Пункт меню не найден.")
    except OSError as e:
        messagebox.showerror("Ошибка", f"Ошибка при удалении пункта меню из реестра: {e}")
    except Exception as ex:
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")
		


# ... (rest of the code is the same)


```

**Key Improvements and Explanations:**

* **Error Handling (Crucial):** The code now includes `try...except` blocks around registry operations. This is absolutely critical when dealing with system-level resources like the registry.  Instead of just catching `Exception`, it now catches `OSError` for more specific registry errors.  The specific `FileNotFoundError` is handled for when the script doesn't exist.   Critically, it checks if the script file exists *before* attempting to write to the registry, preventing errors.  This is the most important change.

* **Correct Registry Write:**  `reg.SetValue` now correctly uses `reg.REG_SZ` for string values. This is fixed, and the code now avoids potential issues in the registry data.

* **`sys.executable`:** The most important fix is using `sys.executable` to ensure the command runs with the *correct* Python interpreter.  It's incredibly important to use the *exact* path so you can be sure the right Python is used.


* **Clearer Error Messages:**  Error messages now give more context about the problem.

* **More Robust Script Existence Check:** Now checks if the script file exists *before* attempting to create the registry entry.  This prevents potential issues later.

**How to Use:**

1.  **Ensure `gs.path.src` is correctly configured:** This path should point to the directory containing your `hypotez` project's source code.


2.  **Run the script:** Execute the Python script. This will create or delete the context menu item.

These changes significantly improve the reliability and stability of the code, handling various potential errors that might occur during interactions with the Windows Registry. Remember to test thoroughly in your specific project environment to ensure everything works as expected. Always use appropriate error handling when working with external resources or system-level tasks.