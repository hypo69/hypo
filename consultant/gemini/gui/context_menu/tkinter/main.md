```python
## \file hypotez/src/gui/context_menu/tkinter/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.gui.context_menu.tkinter """

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
import sys

import header  # Custom import, assuming it initializes settings or constants
# Crucial fix: Import gs from the correct location
from .. import gs  # Corrected import path

def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_key = rf"{key_path}\command"
    
    try:
        command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'

        if not os.path.exists(command_path):
            messagebox.showerror("Ошибка", f"Файл {command_path} не найден.")
            return

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                reg.SetValueEx(command, "", 0, reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл {command_path} не найден.\n{e}")
    except OSError as e:
        messagebox.showerror("Ошибка", f"Ошибка доступа к реестру: {e}")
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
        messagebox.showerror("Ошибка", f"Ошибка доступа к реестру: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")



def create_gui():
    root = tk.Tk()
    root.title("Управление контекстным меню")

    add_button = tk.Button(root, text="Добавить пункт меню", command=add_context_menu_item)
    add_button.pack(pady=10)

    remove_button = tk.Button(root, text="Удалить пункт меню", command=remove_context_menu_item)
    remove_button.pack(pady=10)

    exit_button = tk.Button(root, text="Выход", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
```

**Key Improvements and Explanations:**

* **Correct `gs` import:** The crucial fix is importing `gs` from the correct relative path (`from .. import gs`).  This is *essential* for finding the `gs` object that's presumably in a parent module/package.  The previous import was incorrect.
* **Robust Error Handling:** The code now catches `FileNotFoundError` *specifically* for the script file, providing a more informative error message. It also includes a more general `except OSError` and handles other potential exceptions.  This dramatically improves the program's resilience.
* **Clearer Error Messages:** Error messages are now more user-friendly, explaining what went wrong.
* **`reg.SetValueEx`:**  Instead of `reg.SetValue`, use `reg.SetValueEx` which is the correct way to add data into the registry. This ensures that the types are handled properly.
* **`"%1"` in the command:** The command now correctly uses `"%1"` to pass the selected file/folder as an argument to the Python script.


**How to Use:**

1.  **Ensure `gs` is defined:**  Make sure your `header.py` or similar initialization file defines `gs.path.src` correctly.  This should be the location of your Python script, such as `C:\Users\user\Documents\repos\hypotez\src`.


2.  **Run the script:** Run the Python script from the correct directory.


**Crucial Considerations:**

* **Permissions:** Running this script requires administrative privileges (or elevated rights). If the script fails, check your Windows user rights and try running the program again with administrative privileges.
* **Error Logging (Optional but Recommended):** For production code, consider logging errors to a file for more detailed analysis of problems. This can be done using the Python `logging` module.

This revised solution should address most of the previous issues and make the context menu functionality much more robust and reliable. Remember to always handle potential errors carefully when interacting with the Windows Registry. Remember to replace `"C:\Users\user\Documents\repos\hypotez\src"` with the actual path to your `src` directory.