hypotez/src/gui/context_menu/tkinter/main.py
=============================================

.. module:: hypotez.src.gui.context_menu.tkinter.main
    :platform: Windows, Unix
    :synopsis: Module for adding or removing a context menu item in Windows Explorer.

Module to add or remove context menu items for the desktop and folder background.

This module provides functions to add or remove a custom context menu item called
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).


Functions
---------

.. autofunction:: add_context_menu_item
.. autofunction:: remove_context_menu_item
.. autofunction:: create_gui