rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `set_fixed_size` that sets the fixed size of a PyQt6 widget.  The function takes a widget object, width, and height as input and returns no value.

Execution steps
-------------------------
1. The code imports the necessary `QtWidgets` module from the `PyQt6` library.
2. It defines a function `set_fixed_size` which accepts three arguments:
    - `widget`: A `QtWidgets.QWidget` object representing the UI element to resize.
    - `width`: An integer representing the desired width of the widget.
    - `height`: An integer representing the desired height of the widget.
3. Inside the function, the `setFixedSize()` method of the input `widget` is called with the provided `width` and `height` values. This method directly modifies the widget's size, making it non-resizable.

Usage example
-------------------------
.. code-block:: python

    import sys
    from PyQt6 import QtWidgets
    from hypotez.src.suppliers.aliexpress.gui.styles import set_fixed_size

    # Example usage (requires a main window setup):
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    mainWindow.setWindowTitle("Fixed Size Example")

    # Create a button
    button = QtWidgets.QPushButton("Click Me")

    # Set the fixed size of the button
    set_fixed_size(button, 150, 50)

    # Add the button to the main window layout
    mainWindow.layout = QtWidgets.QVBoxLayout()
    mainWindow.layout.addWidget(button)
    mainWindow.setLayout(mainWindow.layout)

    mainWindow.show()
    sys.exit(app.exec())