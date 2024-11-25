html
<h1>Module: hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py</h1>

<h2>Overview</h2>
<p>This module contains Jupyter widgets for managing AliExpress campaigns. It provides a user interface for selecting campaigns, categories, languages, initializing editors, saving campaigns, and displaying products within a Jupyter Notebook environment.</p>

<h2>Classes</h2>

<h3><code>JupyterCampaignEditorWidgets</code></h3>

<p><strong>Description</strong>: This class provides widgets for interacting with and managing AliExpress campaigns. It allows users to select campaigns, categories, and languages, and perform actions such as initializing editors, saving campaigns, and showing products.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self)</code>:
    <p><strong>Description</strong>: Initializes the widgets and sets up the campaign editor.</p>
    <p><strong>Initialization</strong>:
        <ul><li>Sets up the widgets for selecting campaigns, categories, and languages.</li>
        <li>Sets up default values and callbacks for the widgets.</li>
        <li>Initializes the campaign editor with default values.</li></ul>
    </p>
  </li>
  <li><code>initialize_campaign_editor(self, _)</code>:
    <p><strong>Description</strong>: Initializes the campaign editor.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>_</code> (Unused): Unused argument, required for button callback.</li>
    </ul>
    <p><strong>Description</strong>: Sets up the campaign editor based on the selected campaign and category. It updates the editor object and loads category data (if available).</p>
    <p><strong>Error Handling</strong>:
        <ul><li>Raises a <code>FileNotFoundError</code> if the campaigns directory doesn't exist.</li>
    </ul>
    </p>
  </li>
  <li><code>update_category_dropdown(self, campaign_name: str)</code>:
    <p><strong>Description</strong>: Updates the category dropdown based on the selected campaign.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>campaign_name (str)</code>: The name of the campaign.</li>
    </ul>
  </li>
  <li><code>on_campaign_name_change(self, change: dict[str, str])</code>:
    <p><strong>Description</strong>: Handles changes in the campaign name dropdown.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>change (dict[str, str])</code>: The change dictionary containing the new value.</li>
    </ul>
  </li>
  <li><code>on_category_change(self, change: dict[str, str])</code>:
    <p><strong>Description</strong>: Handles changes in the category dropdown.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>change (dict[str, str])</code>: The change dictionary containing the new value.</li>
    </ul>
  </li>
  <li><code>on_language_change(self, change: dict[str, str])</code>:
    <p><strong>Description</strong>: Handles changes in the language dropdown.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>change (dict[str, str])</code>: The change dictionary containing the new value.</li>
    </ul>
  </li>
    <li><code>save_campaign(self, _)</code>:
    <p><strong>Description</strong>: Saves the campaign and its categories.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>_</code> (Unused): Unused argument, required for button callback.</li>
    </ul>
    <p><strong>Error Handling</strong>:
        <ul><li>Catches and logs exceptions during save operation.</li>
    </ul>
    </p>
  </li>
  <li><code>show_products(self, _)</code>:
    <p><strong>Description</strong>: Displays the products in the selected category.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>_</code> (Unused): Unused argument, required for button callback.</li>
    </ul>
    <p><strong>Error Handling</strong>:
        <ul><li>Catches and logs exceptions during product display operation.</li>
    </ul>
    </p>
  </li>
  <li><code>open_spreadsheet(self, _)</code>:
    <p><strong>Description</strong>: Opens the Google Spreadsheet in a browser.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>_</code> (Unused): Unused argument, required for button callback.</li>
    </ul>
  </li>
    <li><code>setup_callbacks(self)</code>:
    <p><strong>Description</strong>: Sets up callbacks for the widgets.</p>
  </li>
  <li><code>display_widgets(self)</code>:
    <p><strong>Description</strong>: Displays the widgets for interaction in the Jupyter notebook.</p>
    <p><strong>Functionality</strong>: Initializes the campaign editor automatically with the first campaign selected.</p>
  </li>
</ul>

<h2>Functions</h2>


```
```

```html
<!-- Note:  The following functions are present in the file, but not documented in the original code and therefore excluded from the documentation. -->
```