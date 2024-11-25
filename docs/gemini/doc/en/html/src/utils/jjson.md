html
<h1>Module: hypotez/src/utils/jjson</h1>

<h2>Overview</h2>
<p>This module provides functions for handling JSON and CSV files, including loading, dumping, merging data, and converting to/from SimpleNamespace objects.  It supports various file formats and modes, including reading from directories and merging multiple JSON files.  The module also incorporates error handling and logging for robustness.</p>

<h2>Functions</h2>

<h3><code>j_dumps</code></h3>

<p><strong>Description</strong>: Dumps JSON data to a file or returns it as a dictionary. Supports SimpleNamespace and list of dictionaries/SimpleNamespaces.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.</li>
  <li><code>file_path</code> (Optional[Path], optional): Path to the output file. If None, returns JSON as a dictionary. Defaults to None.</li>
  <li><code>ensure_ascii</code> (bool, optional): If True, escapes non-ASCII characters in output. Defaults to True.</li>
  <li><code>mode</code> (str, optional): File open mode ("w", "a+", "+a"). Defaults to "w".</li>
  <li><code>exc_info</code> (bool, optional): If True, logs exceptions with traceback. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Optional[Dict]</code>: JSON data as a dictionary if successful, or nothing if an error occurs. If <code>file_path</code> is specified, the function returns <code>None</code> on failure.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>ValueError</code>: If the file mode is unsupported.</li>
</ul>


<h3><code>j_loads</code></h3>

<p><strong>Description</strong>: Loads JSON or CSV data from a file, directory, or string.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>jjson</code> (Path | dict | str): Path to a file, directory, JSON data as a string, or JSON object. Supports JSON files and CSV files.</li>
  <li><code>ordered</code> (bool, optional): If True, returns OrderedDict to preserve element order. Defaults to False.</li>
  <li><code>exc_info</code> (bool, optional): If True, logs exceptions with traceback. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Any</code>: A dictionary or list of dictionaries if successful, or nothing if an error occurs.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>FileNotFoundError</code>: If the specified file is not found.</li>
  <li><code>json.JSONDecodeError</code>: If JSON data could not be parsed.</li>
</ul>


<h3><code>j_loads_ns</code></h3>

<p><strong>Description</strong>: Loads JSON or CSV data and converts it to SimpleNamespace objects.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>jjson</code> (Path | SimpleNamespace | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.</li>
  <li><code>ordered</code> (bool, optional): If True, returns OrderedDict instead of a regular dict to preserve element order. Defaults to False.</li>
  <li><code>exc_info</code> (bool, optional): If True, logs exceptions with traceback. Defaults to True.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Optional[SimpleNamespace | List[SimpleNamespace]]</code>: Returns SimpleNamespace or a list of SimpleNamespace objects if successful. Returns <code>None</code> if <code>jjson</code> is not found or cannot be read.</li>
</ul>


<h3><code>replace_key_in_json</code></h3>

<p><strong>Description</strong>: Recursively replaces a key in a nested dictionary or list.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (dict | list): The dictionary or list where key replacement occurs.</li>
  <li><code>old_key</code> (str): The key to be replaced.</li>
  <li><code>new_key</code> (str): The new key.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: The updated dictionary with replaced keys.</li>
</ul>


<h3><code>process_json_file</code></h3>
<p><strong>Description</strong>: Processes a JSON file, replacing the 'name' key with 'category_name'.</p>
<p><strong>Parameters</strong>:</p>
<ul><li><code>json_file</code> (Path): Path to the JSON file.</li> </ul>
<p><strong>Returns</strong>: None. Writes updated JSON to the file.</p>
<p><strong>Raises</strong>: Exception if there is an error during processing</p>


<h3><code>recursive_process_json_files</code></h3>
<p><strong>Description</strong>: Recursively processes JSON files in a directory and its subdirectories.</p>
<p><strong>Parameters</strong>:</p>
<ul><li><code>directory</code> (Path): Path to the directory containing JSON files.</li></ul>
<p><strong>Returns</strong>: None. Modifies the files in-place.</p>


<h3><code>extract_json_from_string</code></h3>
<p><strong>Description</strong>: Extracts JSON content from a Markdown string.</p>
<p><strong>Parameters</strong>:</p>
<ul><li><code>md_string</code> (str): The Markdown string containing JSON.</li></ul>
<p><strong>Returns</strong>: JSON content as a string, or an empty string if no JSON is found.  Logs warnings or errors as appropriate.</p>