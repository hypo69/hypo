rst
How to use the `main.py` code block
========================================================================================

Description
-------------------------
This Python code defines a main application window (`MainApp`) using PyQt6 for managing various editor tabs (JSON, Campaign, Product).  It includes functionalities for opening, saving, and handling files (JSON files) within the application and provides basic editing commands (copy, paste). The code is structured to handle different editor types (product, campaign) by using inheritance and modular design.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports PyQt6 modules for creating the GUI, the `qasync` library for asynchronous operations, modules for handling JSON files, and modules for product, campaign and category editors.

2. **Define the `MainApp` class:** This class represents the main application window.
    - **Initialization (`__init__`)**:  It initializes the window title, geometry, and creates a `QTabWidget` for tabs.
    - **Tab creation**: It creates individual tabs (JSON Editor, Campaign Editor, Product Editor) using `QtWidgets.QWidget`.  Each tab hosts a specific editor (e.g., `CampaignEditor`).

3. **Create the menu bar:**
    - A menu bar (`menubar`) is added to the window.
    - "File" menu options (Open, Save, Exit) are created and linked to functions for file handling and application exit.
    - "Edit" menu options (Copy, Paste) are created and linked to copy/paste functions.
    - An "Open Product File" action is linked to the specific product editor for file handling.

4. **Implement file handling functions:**
    - `open_file`: Displays a file dialog to select a JSON file and loads it.
    - `save_file`: Saves the currently selected tab's content.  Saves from either the main tab, or the product editor.
    - `exit_application`: Closes the application.
    - `load_file`: Handles loading JSON data from the specified file into the respective editor tab.

5. **Implement copy/paste functions:**
    - `copy`: Copies selected text from a focused text widget to the clipboard.
    - `paste`: Pastes text from the clipboard to a focused text widget.

6. **Initialize and run the application:**
    - The `main` function creates an application object (`app`) using `QtWidgets.QApplication`.
    - It initializes an event loop, creates the main application window (`main_app`) and displays it.
    - The event loop runs indefinitely to process GUI events.

Usage example
-------------------------
.. code-block:: python

    import sys
    from PyQt6 import QtWidgets
    from hypotez.src.suppliers.aliexpress.gui.main import main

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        main()
        sys.exit(app.exec())

This example shows how to run the application using `QtWidgets.QApplication` and handling the main event loop. Remember to replace `hypotez.src.suppliers.aliexpress.gui.main` with the correct path to your file if it's not in the same directory.