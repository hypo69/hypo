html
<h1>hypotez/src/credentials.py</h1>

<h2>Overview</h2>
<p>This module defines global project settings, including paths, passwords, logins, and API settings. It utilizes the <code>PyKeePass</code> library for securely storing credentials.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the project mode (e.g., 'dev').</p>


<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files (e.g., 'pyproject.toml', 'requirements.txt', '.git').</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>singleton</code></h3>

<p><strong>Description</strong>: Decorator for implementing the Singleton pattern.</p>


<h2>Classes</h2>

<h3><code>ProgramSettings</code></h3>

<p><strong>Description</strong>: A class representing program settings. It's a singleton holding essential project parameters and configurations. It loads credentials from a KeePass database and config file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>base_dir</code> (Path): Path to the project root directory.  Defaults to the directory containing the current file.</li>
  <li><code>config</code> (SimpleNamespace): A namespace object to store configuration data (loaded from 'src/config.json').</li>
  <li><code>credentials</code> (SimpleNamespace): A namespace object to store credentials from the KeePass database, organized into different categories (e.g., 'aliexpress', 'openai').</li>
  <li><code>MODE</code> (str): Project mode (default 'development').</li>
  <li><code>path</code> (SimpleNamespace): A namespace for paths to various project directories (root, src, bin, log, etc.)</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the <code>ProgramSettings</code> instance, loads configuration from a JSON file, and initializes paths.  It also checks for a new release and sets the environment variables needed for the project.</li>
  <li><code>_load_credentials</code>: Loads credentials from the KeePass database, handling potential errors during the database access.</li>
  <li><code>_open_kp</code>: Attempts to open the KeePass database a specified number of times, handling potential exceptions.  Includes a password from a plaintext file which is included for security purposes.</li>
  <li><code>_load_*_credentials</code> (e.g., <code>_load_aliexpress_credentials</code>): Loads specific credential types from the KeePass database. These methods handle credential extraction for various services, such as Aliexpress, OpenAI, Gemini, Discord, Telegram, PrestaShop, SMTP, Facebook, and Google API (GAPI).</li>
 <li><code>now</code>: Returns the current timestamp in a specific format.</li>

</ul>
<p><strong>Raises</strong>:</p>
<ul>
  <li><code>BinaryError</code>, <code>CredentialsError</code>, <code>DefaultSettingsException</code>, <code>HeaderChecksumError</code>, <code>KeePassException</code>, <code>PayloadChecksumError</code>, <code>UnableToSendToRecycleBin</code>: Exceptions related to loading configurations and credentials.</li>


</ul>

<h2>Global Instance</h2>

<h3><code>gs</code></h3>

<p><strong>Description</strong>: A global instance of the <code>ProgramSettings</code> class, providing access to the program settings.</p>