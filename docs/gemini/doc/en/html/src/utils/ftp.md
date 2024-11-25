html
<h1>FTP Utilities Module Documentation</h1>

<h2>Overview</h2>
<p>This module provides an interface for interacting with FTP servers, allowing for file transfer and deletion operations.</p>

<h2>Functions</h2>

<h3><code>write</code></h3>

<p><strong>Description</strong>: Sends a file to an FTP server.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>source_file_path</code> (str): The path of the file to be sent.</li>
  <li><code>dest_dir</code> (str): The destination directory on the FTP server.</li>
  <li><code>dest_file_name</code> (str): The name of the file on the FTP server.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the file is successfully sent, False otherwise.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: An exception is raised if there is an error connecting to the FTP server, transferring the file, or closing the session.</li>
</ul>


<h3><code>read</code></h3>

<p><strong>Description</strong>: Retrieves a file from an FTP server.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>source_file_path</code> (str): The path where the file will be saved locally.</li>
  <li><code>dest_dir</code> (str): The directory on the FTP server where the file is located.</li>
  <li><code>dest_file_name</code> (str): The name of the file on the FTP server.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Union[str, bytes, None]</code>: The file content if successfully retrieved, None otherwise.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(content)
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: An exception is raised if there is an error connecting to the FTP server, retrieving the file, or closing the session.</li>
</ul>



<h3><code>delete</code></h3>

<p><strong>Description</strong>: Deletes a file from an FTP server.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>source_file_path</code> (str): The path where the file is located locally (not used).</li>
  <li><code>dest_dir</code> (str): The directory on the FTP server where the file is located.</li>
  <li><code>dest_file_name</code> (str): The name of the file on the FTP server.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the file is successfully deleted, False otherwise.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: An exception is raised if there is an error connecting to the FTP server, deleting the file, or closing the session.</li>
</ul>