rst
How to use the CategoryEditor class
========================================================================================

Description
-------------------------
This Python code defines a `CategoryEditor` class, a PyQt6-based graphical user interface (GUI) for managing and preparing advertising campaigns from JSON data. It allows users to select a JSON file, display campaign details, and prepare either all categories or a specific category.  The preparation process is asynchronous, using `qasync` for improved responsiveness. Error handling is included to provide informative messages to the user.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports PyQt6 modules for GUI elements, `qasync` for asynchronous operations, `pathlib` for file path handling, `types.SimpleNamespace` for structured data, and custom modules (`header`, `sys`, `asyncio`, `jjson`, `AliCampaignEditor`).

2. **Define the `CategoryEditor` class:** This class represents the main window of the application.
    - **Initialization (`__init__`)**: Initializes the UI, sets window title and size, creates buttons for file opening, preparing all/specific categories, and a label to display the file name.  Crucially, it stores the `main_app` instance as an attribute.
    - **`setup_ui()`**: Sets up the visual components of the application window by creating the necessary widgets (buttons, labels) and arranging them in a layout.
    - **`setup_connections()`**: Establishes connections between UI elements and their actions (e.g., button clicks).
    - **`open_file()`**: Opens a file dialog to choose a JSON file. It extracts the file path and then calls the `load_file()` method with the selected file.
    - **`load_file()`**: Loads the JSON file into `self.data` using `j_loads_ns` and displays the file's name. Creates an `AliCampaignEditor` object to handle campaign actions.  It also correctly extracts the language and sets up the `editor` object.
    - **`create_widgets()`**: Creates widgets representing campaign and category data extracted from the loaded JSON file.  Crucially, this method removes previously created category widgets to prevent duplication.
    - **`prepare_all_categories_async()`**: Asynchronously prepares all categories using the `AliCampaignEditor` instance. Handles potential errors and displays success or error messages accordingly.
    - **`prepare_category_async()`**: Asynchronously prepares a specific category using the `AliCampaignEditor` instance. Handles potential errors and displays success or error messages accordingly.

3. **Error handling**: The code includes `try...except` blocks to catch potential errors during JSON loading and campaign preparation, providing informative error messages to the user.

Usage example
-------------------------
.. code-block:: python

    import sys
    from PyQt6.QtWidgets import QApplication
    from hypotez.src.suppliers.aliexpress.gui.category import CategoryEditor

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main_app = QApplication(sys.argv) # Create a main app instance (Crucial!)
        editor_window = CategoryEditor(main_app=main_app)  # Pass main_app as an argument
        editor_window.show()
        sys.exit(app.exec())