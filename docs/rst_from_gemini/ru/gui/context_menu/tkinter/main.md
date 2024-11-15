```python
## \file hypotez/src/gui/context_menu/tkinter/main.py
# -*- coding: utf-8 -*-
 # <- venv win
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

# Crucial: Avoid hardcoding paths.  Use absolute paths if possible.
# This is especially important for deployment.
import pathlib

# Import gs from __init__.py (assuming it's present).  Better way.
try:
    from . import gs  # adjust if necessary
except ImportError:
    print("Error: gs module not found.  Please make sure your __init__.py correctly imports gs.")
    sys.exit(1)


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background."""

    key_path = r"Directory\Background\shell\hypo_AI_assistant"
    command_key = rf"{key_path}\command"
    
    script_path = pathlib.Path(__file__).resolve().parent / "run_script.py"

    if not script_path.exists():
        messagebox.showerror("Ошибка", f"Файл {script_path} не найден.")
        return


    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValueEx(key, "", 0, reg.REG_SZ, "hypo AI assistant")

            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                reg.SetValueEx(command, "", 0, reg.REG_SZ, f"python \"{script_path}\" \"%1\"")

        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")
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
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")


def create_gui():
    """Creates a simple GUI for managing the custom context menu item."""
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

**Explanation of Improvements:**

* **`pathlib` for paths:**  Instead of string manipulation, use `pathlib.Path` for constructing paths. This makes your code more robust and easier to maintain, especially when dealing with file systems across different operating systems.  Crucially, it allows you to use relative paths that are resolved *relative to the current file's location.*
* **Error Handling for `gs`:** The code now checks if the `gs` module can be imported, printing a clear error message and exiting if it can't. This prevents cryptic errors later on.
* **`run_script.py`:**  Creates a separate file `run_script.py` which *actually* handles the tasks that you want to perform from the context menu, to help avoid accidentally running the main GUI from the context menu.
* **Absolute paths are a strong recommendation.**  It's usually the safest strategy, and this example now shows how to construct them.

**`run_script.py` (Example):**

```python
import sys

def process_argument(argument):
  print(f"Argument Received: {argument}")
  # Perform tasks with argument, if any, otherwise, do default tasks.
  return  # Or return result.


if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_argument(sys.argv[1])
    else:
        print("No argument provided.")
```

**How to Use:**

1.  **Create `run_script.py`:**  Place the `run_script.py` code in the same directory as `main.py`.
2.  **Run the GUI:** Execute `main.py` from your terminal. This will create the GUI.
3.  **Add the Context Menu Item:** Click the "Add" button in the GUI. This should add the item to the context menu.
4.  **Right-Click Test:** Right-click on an empty area on your desktop or in a folder. You should see the "hypo AI assistant" item. When you click it, `run_script.py` will execute.  Pass arguments if you need to.

**Important Considerations for Deployment:**

*   **Deployment of `gs`:** Ensure `gs` is handled correctly when your project is deployed.  In a production environment, you will likely want absolute paths for all files in your main script.
*   **Permissions:** Make sure that your Python script has the necessary permissions to access the registry.


This revised answer significantly improves the robustness, maintainability, and safety of the code. Remember to adapt `run_script.py` to perform your desired actions based on arguments if applicable.