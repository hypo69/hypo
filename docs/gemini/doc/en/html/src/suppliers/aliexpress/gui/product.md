html
<h1>Module: src.suppliers.aliexpress.gui.product</h1>

<h2>Overview</h2>
<p>This module defines the <code>ProductEditor</code> class, a PyQt6-based widget for editing product information from JSON files, specifically those related to campaigns from AliExpress.</p>

<h2>Classes</h2>

<h3><code>ProductEditor</code></h3>

<p><strong>Description</strong>: A PyQt6 widget for editing product details from a JSON file.  It allows users to open a JSON file, load product data, and prepare product information using an internal <code>AliCampaignEditor</code> instance. </p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>data</code> (<code>SimpleNamespace</code>): The loaded product data from the JSON file.  Defaults to <code>None</code>.</li>
  <li><code>language</code> (<code>str</code>): Product language. Defaults to 'EN'.</li>
  <li><code>currency</code> (<code>str</code>): Product currency. Defaults to 'USD'.</li>
  <li><code>file_path</code> (<code>str</code>): Path to the loaded JSON file. Defaults to <code>None</code>.</li>
  <li><code>editor</code> (<code>AliCampaignEditor</code>): An instance used to prepare the product data. </li>
  <li><code>main_app</code> (<code>MainApp</code>, optional): A reference to the main application. </li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, parent=None, main_app=None)</code>:
    <p><strong>Description</strong>: Initializes the <code>ProductEditor</code> widget. Stores a reference to the MainApp instance, sets up the UI, and establishes connections.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>parent</code> (<code>QWidget</code>, optional): The parent widget. Defaults to <code>None</code>.</li>
      <li><code>main_app</code> (<code>MainApp</code>, optional): The main application instance. Defaults to <code>None</code>. </li>
    </ul>
    <p><strong>Raises</strong>: None</p>
  </li>
  <li><code>setup_ui(self)</code>:
    <p><strong>Description</strong>: Sets up the user interface with a file opening button, a file name label, a "Prepare Product" button and appropriate layout.</p>
    <p><strong>Parameters</strong>: None</p>
    <p><strong>Raises</strong>: None</p>
  </li>
  <li><code>setup_connections(self)</code>:
    <p><strong>Description</strong>: Establishes signal-slot connections for UI elements. </p>
    <p><strong>Parameters</strong>: None</p>
    <p><strong>Raises</strong>: None</p>
  </li>
   <li><code>open_file(self)</code>:
    <p><strong>Description</strong>: Opens a file dialog to select a JSON file. Loads the selected file using <code>load_file</code>.</p>
    <p><strong>Parameters</strong>: None</p>
    <p><strong>Raises</strong>: None</p>
  </li>
  <li><code>load_file(self, file_path)</code>:
    <p><strong>Description</strong>: Loads the JSON file at the specified path.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>file_path (str)</code>: The path to the JSON file.</li>
    </ul>
    <p><strong>Returns</strong>: None</p>
    <p><strong>Raises</strong>:
    <ul>
      <li><code>Exception</code>: If there is an error loading or parsing the JSON file. An error message box is displayed to the user.</li>
    </ul>
    </p>
  </li>
   <li><code>create_widgets(self, data)</code>:
    <p><strong>Description</strong>: Creates UI elements based on the loaded product data.  Clears previous widgets to prevent duplication.  Adds labels for product title and details.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>data (SimpleNamespace)</code>: The product data from the loaded JSON.</li>
    </ul>
    <p><strong>Returns</strong>: None</p>
    <p><strong>Raises</strong>: None</p>
  </li>
   <li><code>prepare_product_async(self)</code>:
    <p><strong>Description</strong>: Asynchronously prepares the product data using the <code>AliCampaignEditor</code> instance. Displays success or error messages.</p>
    <p><strong>Parameters</strong>: None</p>
    <p><strong>Returns</strong>: None</p>
    <p><strong>Raises</strong>:
    <ul>
      <li><code>Exception</code>: If any error occurs during preparation. An error message box is displayed.</li>
    </ul>
  </li>
</ul>
<h2>Functions</h2>
<p>(None)</p>