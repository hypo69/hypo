rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code creates a graphical user interface (GUI) application using PyQt6 and QtWebEngineWidgets. The application acts as a web browser, allowing the user to input URLs, load websites, and minimize to the system tray.  It also provides a way to select a default browser and load predefined Google services or select various AI models.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports essential libraries like PyQt6 modules for GUI elements and QtWebEngineWidgets for web browser integration.

2. **Define the `AssistantMainWindow` class:** This class handles the main window functionality.

3. **Set window properties:** It sets the window flags to allow resizing and calculates appropriate window size based on the primary screen resolution.

4. **Get default browser choice:** The application prompts the user to select the default browser (Chrome, Firefox, or Edge).

5. **Create a web browser profile:**  It constructs a web engine profile based on the chosen browser and uses the corresponding profile path (e.g., Chrome's User Data folder).

6. **Create a QWebEngineView object:** A web browser control is created and associated with the application.

7. **Create title bar widgets:**  A title bar is created with an input field for URL, load button, minimize button, fullscreen button, and close button.

8. **Set up layouts:** Horizontal and vertical layouts are used to organize and position the various UI elements.

9. **Create and initialize system tray icon:** A system tray icon is created with an icon and context menu for actions like restore and exit.

10. **Create menus for Google services and models:** Menus are designed for quick access to common Google services (Gmail, Docs, etc.) and for selecting AI models (ChatGPT, Gemini, Claude).

11. **Connect signals and slots:** The code connects button clicks and input events to their corresponding actions (e.g., loading URLs, minimizing, closing the application).  Methods like `load_url`, `hide_to_tray`, and `quit_app` are defined to handle these actions.

12. **Display the main window:** The application displays the main window and system tray icon.

13. **Handle browser selection:** An error message and application exit are handled if the chosen browser is unsupported.

14. **Handle window closing:** Overrides the `closeEvent` to prevent window closure and instead minimize to system tray when closing the window.  It also sets the `setQuitOnLastWindowClosed` flag to `False` to keep the application running when the last window is closed.

15. **Initialize and run the application:** The `QApplication` is initialized with command-line arguments, and the main window is displayed using `window.show()`.  The `app.exec()` call starts the application event loop.



Usage example
-------------------------
.. code-block:: python

    import sys
    from PyQt6.QtWidgets import QApplication
    from hypotez.src.gui.openai_trаigner.main import AssistantMainWindow

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = AssistantMainWindow()
        window.show()
        sys.exit(app.exec())

This example demonstrates how to run the application.  Replace `hypotez.src.gui.openai_trаigner.main` with the correct path if your file is in a different location.  The application will launch and allow you to enter URLs or use the Google services and AI model menus.