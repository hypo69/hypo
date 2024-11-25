html
<h1>Module src.scenario</h1>

<h2>Overview</h2>
<p>The `src.scenario` module is designed for automating interactions with suppliers using scenarios described in JSON files. The module's primary function is to adapt the data extraction and processing process for product information from supplier websites and synchronize this information with your system's database.</p>

<h2>Functions</h2>

<h3><code>run_scenario_files</code></h3>

<p><strong>Description</strong>: Takes a list of scenario files and executes them sequentially. Calls <code>run_scenario_file</code> to process each scenario file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): An object containing the necessary configuration and resources for the scenario execution.</li>
  <li><code>scenario_files_list</code> (list): A list of file paths to the scenario files.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value. The function performs operations on the provided scenario files.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception raised if any unexpected error occurs during file processing.</li>
</ul>


<h3><code>run_scenario_file</code></h3>

<p><strong>Description</strong>: Loads scenarios from the specified file and calls <code>run_scenario</code> for each scenario in the file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): An object containing the necessary configuration and resources for the scenario execution.</li>
  <li><code>scenario_file</code> (str): Path to the scenario file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception raised if any unexpected error occurs during file processing.</li>
</ul>


<h3><code>run_scenario</code></h3>

<p><strong>Description</strong>: Processes a single scenario. Navigates to the URL specified in the scenario, extracts product data, and saves the extracted data to the database.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): An object containing the necessary configuration and resources for the scenario execution.</li>
  <li><code>scenario</code> (dict): A dictionary containing the scenario data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value. The function performs operations on the provided scenario.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception raised if any unexpected error occurs during scenario processing (e.g., network issues, data format errors).</li>
</ul>


<h3><code>dump_journal</code></h3>

<p><strong>Description</strong>: Saves the execution journal to a file for subsequent analysis.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code> (object): An object containing the necessary configuration and resources for the scenario execution.</li>
  <li><code>journal</code> (dict): The journal data.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception raised if any unexpected error occurs during file writing.</li>
</ul>


<h3><code>main</code></h3>

<p><strong>Description</strong>: Main function for launching the module.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>None</code>: No parameters taken.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: No explicit return value.</li>
</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception raised if any unexpected error occurs during module execution.</li>
</ul>


<h2>Example Scenario (JSON)</h2>

<p>Example of a JSON scenario describing how to interact with specific product categories on a website. Includes URL, category name, and PrestaShop category IDs.</p>

<pre><code class="language-json">
{
    "scenarios": {
        "מינרל+לחויותלפניםמינרליםותמציותצמחים": {
            "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
            "name": "מינרל+לחויותלפניםמינרליםותמציותצמחים",
            "presta_categories": {
                "default_category": 11245,
                "additional_categories": [11288]
            }
        }
    }
}
</code></pre>


<h2>How it Works</h2>

<ol>
  <li>Loads scenarios from files.</li>
  <li>Extracts data from specified URLs.</li>
  <li>Saves extracted data to the database.</li>
  <li>Generates reports and logs execution details.</li>
</ol>
<p>This module automates data collection and processing, facilitating integration with various suppliers and e-commerce platforms.</p>