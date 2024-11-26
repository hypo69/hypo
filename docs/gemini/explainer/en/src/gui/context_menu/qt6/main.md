```python
## \file hypotez/src/gui/context_menu/qt6/main.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.gui.context_menu.qt6 
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
"""MODE = 'dev'
  
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
from src import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background.

    This function creates a registry key under 'HKEY_CLASSES_ROOT\Directory\Background\shell' 
    to add a menu item named 'hypo AI assistant' to the background context menu in Windows Explorer.
    The item runs a Python script when selected.

    Registry Path Details:
        - `key_path`: Directory\Background\shell\hypo_AI_assistant
            This path adds the context menu item to the background of folders and 
            the desktop, allowing users to trigger it when right-clicking on empty space.
        
        - `command_key`: Directory\Background\shell\hypo_AI_assistant\command
            This subkey specifies the action for the context menu item and links it to a script 
            or command (in this case, a Python script).
    
    Raises:
        Displays an error message if the script file does not exist.
    """
    
    # Registry path for adding a menu item to the background of folders and the desktop
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")  # Display name
            
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not os.path.exists(command_path):
                    QtWidgets.QMessageBox.critical(None, "Ошибка", f"Файл {command_path} не найден.")
                    return
                reg.SetValue(command, "", reg.REG_SZ, f"python \\\"{command_path}\\\" \\\"%1\\\"\" )
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item."""
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {e}")


class ContextMenuManager(QtWidgets.QWidget):
    """Main application window for managing the custom context menu item."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Управление контекстным меню")
        layout = QtWidgets.QVBoxLayout()

        add_button = QtWidgets.QPushButton("Добавить пункт меню")
        add_button.clicked.connect(add_context_menu_item)
        layout.addWidget(add_button)

        remove_button = QtWidgets.QPushButton("Удалить пункт меню")
        remove_button.clicked.connect(remove_context_menu_item)
        layout.addWidget(remove_button)

        exit_button = QtWidgets.QPushButton("Выход")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ContextMenuManager()
    window.show()
    app.exec()
```

```
<algorithm>
1. **Initialization:**
   - Imports necessary modules: `winreg` for registry access, `os` for file system operations, `PyQt6` for GUI, custom modules `header` and `src.gs`.
   - Sets a global variable `MODE` to 'dev'.


2. **`add_context_menu_item()`:**
   - Takes no arguments.
   - Constructs the registry path for the context menu item.
   - **Example:**
     - `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant`

   - Tries to create the registry key.
   - **Example:**
     - Sets the display name using `reg.SetValue`.
     - Constructs the command key path.
     - **Example:**
       - `command_key`: `Directory\\Background\\shell\\hypo_AI_assistant\\command`
     - Checks if the script file exists using `os.path.exists`.
     - **Example:** If the file `gs.path.src / 'gui' / 'context_menu' / 'main.py'` doesn't exist, it displays an error.
     - Sets the command to execute the Python script using `reg.SetValue`.
     - **Example:** `python "path/to/script.py" "%1"`
   - Displays success or error message.


3. **`remove_context_menu_item()`:**
   - Takes no arguments.
   - Constructs the registry path for the context menu item.
   - **Example:**
     - `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant`
   - Tries to delete the registry key.
   - **Example:** `reg.DeleteKey`
   - Displays success or error message.


4. **`ContextMenuManager` class:**
   - Initializes the main application window.
   - Creates a GUI with buttons for adding, removing, and exiting.
   - **Example:**
     - Adds a button to add context menu item. This button is linked to the `add_context_menu_item` function.
     - Adds a button to remove context menu item. This button is linked to the `remove_context_menu_item` function.
   - Sets up the layout.
   - Shows the window.


5. **Main execution block (`if __name__ == "__main__":`)**
   - Initializes the `PyQt6` application.
   - Creates an instance of `ContextMenuManager`.
   - Shows the main window.
   - Enters the application's event loop.

```

```
<explanation>

- **Imports:**
    - `winreg`: Used for interacting with the Windows Registry, crucial for modifying the context menu.  Relationship: This module is fundamental for the core functionality of the script, directly impacting the way context menu items are added and removed.
    - `os`: Used for operating system-related tasks, especially file system checks.  Relationship: essential for file existence validation, enabling the script to ensure the target file exists before attempting operations on it.
    - `QtWidgets`: From PyQt6, used for creating the graphical user interface (GUI). Relationship: Provides the necessary tools to build the application's window and buttons for user interaction.
    - `header`: A custom module, likely containing configuration settings or constants. Relationship: This is crucial for how the code interacts with the project's global state, especially for paths.
    - `src.gs`: A custom module from the `src` package, presumed to handle paths and project structure. Relationship: This import suggests a well-structured project with a dedicated module to manage paths, which improves the maintainability of the codebase, reducing hardcoded path reliance and simplifying future updates to file locations.


- **Classes:**
    - `ContextMenuManager`: This class is the core GUI component.
        - `__init__`: Initializes the window.
        - `initUI`: Creates the UI layout with buttons for adding and removing the context menu item. This function sets up the user interaction elements, making the code well-organized.


- **Functions:**
    - `add_context_menu_item`: Creates a new context menu item in the Windows Registry.
        - Takes no arguments.
        - Uses `winreg` to create and modify registry keys for adding a menu item to the context menu. It validates the existence of the target script file before proceeding, improving error handling.
        - `gs.path.src`:  Crucial part, it's assumed that `gs.path` provides a structured path to the project's source directory and `src` represents the project root path.
        - Raises an error if the script file is missing.
    - `remove_context_menu_item`: Removes the context menu item from the Windows Registry.
        - Takes no arguments.
        - Uses `winreg` to delete the registry key.
        - Includes error handling for cases where the item doesn't exist.


- **Variables:**
    - `MODE`: A global variable likely for selecting development or production modes.
    - `key_path`, `command_key`: These variables store the registry paths for adding and modifying context menu items.


- **Potential Errors/Improvements:**
    - Error handling is present but could be improved.  Adding more specific exception handling (e.g., `WindowsError` for registry-specific issues) could make debugging easier.
    - The code assumes a specific structure (e.g., `gs.path.src`) for accessing the script file.  It would be better to explicitly define the absolute or relative path to the script file.
    - Consider adding more descriptive error messages to improve user experience.
    - The script doesn't handle cases where the registry key already exists for the context menu item, potentially causing issues, or needs to check and avoid redundancies if the script was already added.


- **Relationships:**
    - The code depends on the `src.gs` module for path management. This highlights the importance of proper modularization, with modules responsible for managing their specific areas of functionality.


```