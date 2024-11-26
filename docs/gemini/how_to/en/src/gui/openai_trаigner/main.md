```python
# Usage Guide for hypotez/src/gui/openai_trаigner/main.py

This Python script creates a graphical user interface (GUI) application using PyQt6 for browsing the web.  It integrates a system tray and allows users to launch various web services and select different AI models.

**How to Use:**

1. **Dependencies:**  Ensure you have PyQt6 installed.  If not, use pip:
   ```bash
   pip install PyQt6
   ```
   Also, ensure that your Python interpreter is properly set up (e.g., using a virtual environment).  The shebang lines at the top of the file specify the expected interpreter.


2. **Running the Application:**
   ```bash
   python main.py
   ```

3. **GUI Elements:**

   * **Window:** A main window, resizable, with a title bar.

   * **Title Bar:**
      * **URL Input:**  Enter a URL and press Enter to load it.  Can also be loaded via the "Load" button.
      * **Load Button:**  Loads the URL entered in the input field.
      * **Minimize Button:** Hides the main window to the system tray.
      * **Fullscreen Button:** Makes the window fullscreen.
      * **Close Button:**  Hides the window to the system tray. It's crucial to understand that clicking the close button won't shut down the app; it hides it in the system tray.
      * **Services Google Button (with Menu):**  Opens a menu to quickly access common Google services (Google Login, Gmail, Docs, Sheets, Drive, Photos).
      * **Model Selection Button (with Menu):** Opens a menu to select AI models for potential integration (ChatGPT, Gemini, and Claude).  Note that the Gemini and Claude URLs are placeholders; you must replace them with actual links if you want to integrate them.

   * **Browser:** Displays the loaded web page.

   * **System Tray:** When the window is minimized, the system tray icon appears.  Clicking it reveals a context menu to restore the window or quit the application.


4. **Browser Selection:** When the application starts, it will ask for the default browser (Chrome, Firefox, or Edge).  Choose one.  An error message will show if the selected browser is not supported.  This uses the browser's user profile for the web engine to avoid problems with permissions.

5. **URL Loading:** The script attempts to ensure that you enter a valid URL. If you don't include `http://` or `https://` in your input, it automatically prefixes the input with `http://`.

6. **Minimizing and Closing:**
    * The `hide_to_tray()` function minimizes the main window to the system tray and sets up a context menu.
    * When you use the close button, the application doesn't fully exit. The window hides to the tray, and the system tray icon is shown.  You close the application through the context menu on the tray icon (using `quit_app()`).
    * The `app.setQuitOnLastWindowClosed(False)` line in `if __name__ == "__main__":` is crucial.  It prevents the application from terminating immediately when the last window is closed.

**Important Considerations:**

* **Error Handling:** The code includes a basic error message if the user selects an unsupported browser. Improve this by adding more robust error checking and handling.
* **Model Integration:** The Gemini and Claude URLs are placeholders. Update these with the correct URLs for those models to enable functionality.
* **Security:** Be very cautious when allowing user input to directly load web pages.  This code has no input validation or security measures in place for user-entered URLs.  Sanitize input to prevent malicious code or unexpected behavior.
* **Customization:** Modify the available Google services and models within the respective menus.  Add functionality to handle more services or customize the look and feel of the UI.


This guide provides a basic understanding of how to use the code.  Further exploration of the `main.py` file will allow you to customize and extend the functionality according to your needs. Remember to replace placeholder URLs and handle potential errors more thoroughly for a production-ready application.
```