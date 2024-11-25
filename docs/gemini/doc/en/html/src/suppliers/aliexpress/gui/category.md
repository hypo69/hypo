html
<h1>Module: hypotez/src/suppliers/aliexpress/gui/category.py</h1>

<h2>Overview</h2>
<p>This module provides a graphical user interface (GUI) for preparing advertising campaigns on AliExpress. It allows users to load JSON files containing campaign data, prepare all or specific categories within a campaign, and displays the loaded data in a user-friendly way.  This GUI utilizes PyQt6 for the UI and asynchronous operations using qasync.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operating mode of the application. Currently set to 'dev'.</p>


<h2>Classes</h2>

<h3><code>CategoryEditor</code></h3>

<p><strong>Description</strong>: A class representing the main window for editing AliExpress campaign categories.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>campaign_name</code> (str): The name of the campaign being edited.  </li>
  <li><code>data</code> (SimpleNamespace): Holds the loaded campaign data from the JSON file.  </li>
  <li><code>language</code> (str): The language of the campaign. Defaults to 'EN'.  </li>
  <li><code>currency</code> (str): The currency used for the campaign. Defaults to 'USD'.</li>
  <li><code>file_path</code> (str): The path to the loaded JSON file.  </li>
  <li><code>editor</code> (AliCampaignEditor): An instance of the campaign editor class used to prepare categories.</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, parent=None, main_app=None)</code></li>
</ul>

<p><strong>Description</strong>: Initializes the CategoryEditor window. Takes an optional parent widget and MainApp instance as arguments.</p>

<ul>
<li><code>setup_ui(self)</code></li>
</ul>
<p><strong>Description</strong>: Sets up the user interface elements of the window, including buttons for loading JSON files, preparing all or specific categories, and displaying the loaded data.  Adds buttons, labels, and a layout to the window.</p>

<ul>
<li><code>setup_connections(self)</code></li>
</ul>
<p><strong>Description</strong>: Establishes signal-slot connections between UI elements and the corresponding actions. </p>


<ul>
<li><code>open_file(self)</code></li>
</ul>
<p><strong>Description</strong>: Opens a file dialog to select and load a JSON file containing campaign data. The loaded file should follow the expected structure to avoid errors.  Prompts the user to choose a JSON file.  Sets the file name label to display the file path.</p>

<ul>
<li><code>load_file(self, campaign_file)</code></li>
</ul>
<p><strong>Description</strong>: Loads the JSON file contents into the data attribute.  Creates a new instance of the `AliCampaignEditor` to process and prepare the categories.  Displays a success message or an error message based on loading success.</p>

<ul>
  <li><code>create_widgets(self, data)</code></li>
</ul>
<p><strong>Description</strong>: Creates UI widgets based on the campaign data loaded from the JSON file. Updates the window layout with newly created widgets.</p>

<ul>
<li><code>prepare_all_categories_async(self)</code></li>
</ul>
<p><strong>Description</strong>: Asynchronously prepares all categories within the loaded campaign.  Uses the campaign editor to prepare and displays confirmation or error messages based on the preparation status.</p>

<ul>
  <li><code>prepare_category_async(self)</code></li>
</ul>
<p><strong>Description</strong>: Asynchronously prepares a specific category within the loaded campaign.  Uses the campaign editor to perform the preparation and displays confirmation or error messages based on the preparation status.</p>



<h2>Functions</h2>


<!-- Add function documentation here as needed -->