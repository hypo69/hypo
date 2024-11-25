html
<h1>Module: hypotez/src/suppliers/aliexpress/gui/main</h1>

<h2>Overview</h2>
<p>This module defines the <code>MainApp</code> class, which is the main window interface for managing advertising campaigns. It utilizes PyQt6 for GUI elements and features tabs for different editors (JSON, Campaign, Product).</p>

<h2>Classes</h2>

<h3><code>MainApp</code></h3>

<p><strong>Description</strong>: The main application window, handling tabs for different editors. It also includes a menu bar for file operations and edit commands.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initializes the main application window, sets the title, size, and creates the tab widget. It also creates instances of the JSON Editor, Campaign Editor, and Product Editor tabs.</p>
  <ul>
    </ul>
  </li>
  <li><code>create_menubar</code>:
      <p><strong>Description</strong>: Creates the menu bar with "File" and "Edit" menus.  Adds actions for file operations (open, save, exit) and edit operations (copy, paste). Includes handling for opening product files.</p>
  </li>
  <li><code>open_file</code>:
    <p><strong>Description</strong>: Opens a file dialog to select a JSON file. Loads the file depending on the current tab. Loads the JSON file and updates the appropriate editor.</p>
  <ul>
  <li><strong>Parameters</strong>: None.</li>
  <li><strong>Returns</strong>: None.</li>
  <li><strong>Raises</strong>: None.</li>
</ul>
</li>
  <li><code>save_file</code>:
    <p><strong>Description</strong>: Saves the changes from the currently active tab.</p>
<ul>
    <li><strong>Parameters</strong>: None.</li>
    <li><strong>Returns</strong>: None.</li>
    <li><strong>Raises</strong>: None. (Relies on underlying editors to handle errors.)</li>
</ul>
  </li>
  <li><code>exit_application</code>:
    <p><strong>Description</strong>: Closes the application.</p>
<ul>
    <li><strong>Parameters</strong>: None.</li>
    <li><strong>Returns</strong>: None.</li>
    <li><strong>Raises</strong>: None.</li>
</ul>
  </li>
  <li><code>copy</code>:
    <p><strong>Description</strong>: Copies selected text to the clipboard from a focused text widget.</p>
    <ul>
    <li><strong>Parameters</strong>: None.</li>
    <li><strong>Returns</strong>: None.</li>
    <li><strong>Raises</strong>: None. (Displays a warning if no text widget is focused.)</li>
    </ul>
  </li>
  <li><code>paste</code>:
      <p><strong>Description</strong>: Pastes text from the clipboard into a focused text widget.</p>
    <ul>
    <li><strong>Parameters</strong>: None.</li>
    <li><strong>Returns</strong>: None.</li>
    <li><strong>Raises</strong>: None. (Displays a warning if no text widget is focused.)</li>
    </ul>
  </li>

 <li><code>load_file</code>:
    <p><strong>Description</strong>: Loads a JSON file into the JSON editor.</p>
    <ul>
    <li><strong>Parameters</strong>:
        <ul>
            <li><code>campaign_file</code> (str): The path to the JSON file.</li>
        </ul>
    </li>
    <li><strong>Returns</strong>: None.</li>
    <li><strong>Raises</strong>:
        <ul><li><code>Exception</code>: If there's an error loading the JSON file.</li></ul>
    </li>
    </ul>
  </li>


</ul>

<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>: Initializes the application and creates an instance of the <code>MainApp</code> class, displays the window and starts the application event loop.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li>None</li>
</ul>