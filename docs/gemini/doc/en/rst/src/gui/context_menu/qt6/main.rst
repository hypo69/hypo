hypotez/src/gui/context_menu/qt6/main.py
==========================================

.. module:: hypotez.src.gui.context_menu.qt6.main
   :platform: Windows, Unix
   :synopsis: Module to manage a custom context menu item for the desktop and folder background using PyQt6.

This module provides functions to add or remove a custom context menu item called 'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.  It utilizes the Windows Registry, targeting the right-click menu on empty spaces.


Functions
---------

.. autofunction:: hypotez.src.gui.context_menu.qt6.main.add_context_menu_item
.. autofunction:: hypotez.src.gui.context_menu.qt6.main.remove_context_menu_item

Classes
-------

.. autoclass:: hypotez.src.gui.context_menu.qt6.main.ContextMenuManager
   :members:
   :undoc-members:
   :show-inheritance: