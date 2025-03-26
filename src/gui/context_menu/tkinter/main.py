## \file /src/gui/context_menu/tkinter/main.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.gui.context_menu.tkinter 
	:platform: Windows, Unix
	:synopsis:  Module to add or remove context menu items for the desktop and folder background.


This module provides functions to add or remove a custom context menu item called 
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg  # Module for interacting with Windows Registry
import os  # Module for OS path manipulation and checks
import tkinter as tk  # Module for GUI creation
from tkinter import messagebox  # Submodule for GUI message boxes

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
    key_path = r"Directory\Background\shell\hypo_AI_assistant"

    try:
        # Create a new key for the menu item under the specified registry path
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")  # Display name of the context menu item
            
            # Sub-key to define the command to run when the menu item is selected
            command_key = rf"{key_path}\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                
                # Define the path to the Python script that will be executed
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'  # Path to the script
                if not os.path.exists(command_path):
                    # Show an error if the script is not found at the specified location
                    messagebox.showerror("Ошибка", f"Файл {command_path} не найден.")
                    return
                
                # Set the command to execute the script with Python when the context menu item is clicked
                reg.SetValue(command, "", reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        
        # Confirmation message for successful addition
        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
        # Display any error that occurs during the registry modification
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")

def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item.

    This function deletes the registry key responsible for displaying the custom
    context menu item, effectively removing it from the background context menu.

    Registry Path Details:
        - `key_path`: Directory\Background\shell\hypo_AI_assistant
            This path targets the custom context menu item and deletes it from the 
            background context menu of the desktop and folders.
    
    Raises:
        Displays a warning if the menu item does not exist, and an error if the operation fails.
    """

    # Registry path for the custom menu item
    key_path = r"Directory\Background\shell\hypo_AI_assistant"

    try:
        # Attempt to delete the registry key associated with the context menu item
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        # Confirmation message for successful removal
        messagebox.showinfo("Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        # Warn if the context menu item was not found
        messagebox.showwarning("Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        # Display any other errors encountered during the key deletion
        messagebox.showerror("Ошибка", f"Ошибка: {e}")

def create_gui():
    """Creates a simple GUI for managing the custom context menu item.

    This function initializes a tkinter-based GUI with buttons to add, remove,
    or exit the menu manager. It provides user-friendly interaction for registry
    modifications.
    """
    
    root = tk.Tk()  # Main window
    root.title("Управление контекстным меню")  # Window title

    # Button to add the custom context menu item
    add_button = tk.Button(root, text="Добавить пункт меню", command=add_context_menu_item)
    add_button.pack(pady=10)

    # Button to remove the custom context menu item
    remove_button = tk.Button(root, text="Удалить пункт меню", command=remove_context_menu_item)
    remove_button.pack(pady=10)

    # Button to exit the program
    exit_button = tk.Button(root, text="Выход", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()  # Run the GUI event loop

if __name__ == "__main__":
    create_gui()  # Launch the GUI application
