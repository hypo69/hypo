rst
How to use the ProductEditor class
========================================================================================

Description
-------------------------
This code defines a PyQt6-based `ProductEditor` widget for loading and processing product data from a JSON file. It allows users to select a JSON file, load its contents, display basic product information, and then prepare the product asynchronously.  Error handling is included to manage potential issues during file loading and product preparation.

Execution steps
-------------------------
1. **Initialization:** The `ProductEditor` class is instantiated, taking a parent widget and the main application instance as arguments. This setup is crucial for proper integration with the broader application.

2. **UI Setup:** The `setup_ui()` method creates a window with a title, adjustable size, a button to select the JSON file (`open_button`), a label to display the file name (`file_name_label`), and another button to prepare the product (`prepare_button`).  A vertical layout is used to arrange these components in the window.

3. **File Selection:** When the "Open JSON File" button is clicked, the `open_file()` method triggers a file dialog to allow the user to select a JSON file. The selected file path is validated and used to load the data.

4. **File Loading:** The `load_file()` method attempts to load the JSON file using the `j_loads_ns()` function from the `src.utils.jjson` module.  If successful, it extracts and displays the file path in the `file_name_label`. It also creates an instance of the `AliCampaignEditor` class to handle product preparation, using the loaded file path. Finally, it displays product details in the UI. Error handling catches and reports potential issues, using a critical message box.

5. **Product Details Display:** The `create_widgets()` method displays a title and details for the loaded product from the JSON.  Crucially, it clears any pre-existing widgets from the layout, preventing duplication, except the open button, the file name label, and the prepare button, improving user experience.

6. **Product Preparation (Async):** The `prepare_product_async()` method asynchronously initiates the preparation of the product using the `AliCampaignEditor` instance. This method handles potential errors during the asynchronous preparation process, displaying error messages to the user if necessary. It uses a success message box for successful preparation.

Usage example
-------------------------
.. code-block:: python

    import sys
    from PyQt6.QtWidgets import QApplication
    from hypotez.src.suppliers.aliexpress.gui.product import ProductEditor

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        # Assuming 'main_app' is an instance of your main application class.
        editor = ProductEditor(main_app=main_app)
        editor.show()
        sys.exit(app.exec())