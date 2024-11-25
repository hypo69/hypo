html
<h1>hypotez/src/gui/context_menu/qt6/main.py</h1>

<h2>Overview</h2>
<p>This module provides functions to add or remove a custom context menu item ('hypo AI assistant') for the background of directories and the desktop in Windows Explorer. It utilizes the Windows Registry to achieve this, targeting the right-click menu on empty spaces.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string representing the current application mode (e.g., 'dev').</p>


<h2>Functions</h2>

<h3><code>add_context_menu_item</code></h3>

<p><strong>Description</strong>: Adds a context menu item to the desktop and folder background.</p>

<p><strong>Description</strong>: Creates a registry key to add a menu item named 'hypo AI assistant' to the background context menu in Windows Explorer. The item runs a Python script when selected.</p>

<p><strong>Registry Path Details:</strong></p>
<ul>
  <li><code>key_path</code>: <code>Directory\\Background\\shell\\hypo_AI_assistant</code> - Adds the context menu item to the background of folders and the desktop.</li>
  <li><code>command_key</code>: <code>Directory\\Background\\shell\\hypo_AI_assistant\\command</code> - Defines the action for the context menu item, linking it to a Python script.</li>
</ul>


<p><strong>Raises:</strong></p>
<ul>
  <li><code>QtWidgets.QMessageBox.critical</code>: Displays a critical error message if the script file specified by <code>command_path</code> does not exist.</li>
</ul>



<h3><code>remove_context_menu_item</code></h3>

<p><strong>Description</strong>: Removes the 'hypo AI assistant' context menu item.</p>

<p><strong>Description</strong>: Deletes the registry key responsible for the context menu item, removing it from the background context menu.</p>

<p><strong>Registry Path Details:</strong></p>
<ul>
  <li><code>key_path</code>: <code>Directory\\Background\\shell\\hypo_AI_assistant</code> - Specifies the registry key to remove.</li>
</ul>


<p><strong>Raises:</strong></p>
<ul>
  <li><code>QtWidgets.QMessageBox.warning</code>: Displays a warning if the menu item does not exist.</li>
  <li><code>QtWidgets.QMessageBox.critical</code>: Displays an error message if the registry operation fails.</li>
</ul>


<h2>Classes</h2>

<h3><code>ContextMenuManager</code></h3>

<p><strong>Description</strong>: Main application window for managing the custom context menu item.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the user interface with buttons to add, remove, or exit.</li>
  <li><code>initUI</code>: Initializes the UI layout with buttons to add/remove the context menu item and exit.</li>
</ul>


<h2>Imports</h2>

<ul>
  <li><code>winreg as reg</code></li>
  <li><code>os</code></li>
  <li><code>PyQt6.QtWidgets</code></li>
  <li><code>header</code> (custom)</li>
  <li><code>src.gs</code> (custom)</li>
</ul>

<h2>Usage Example (in `if __name__ == "__main__":`)</h2>
<p>The code initializes the PyQt application, creates an instance of <code>ContextMenuManager</code>, shows the window, and runs the application's event loop.</p>

```html

```

```
```
```html
<p><em>Note: The example usage section in the documentation was not easily extractable from the provided code.  This example is a placeholder; a more comprehensive example would require analyzing the `if __name__ == "__main__":` block and presenting the setup and usage of the classes in detail.</em></p>