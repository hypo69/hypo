html
<h1>hypotez/src/utils/file.py</h1>

<h2>Overview</h2>
<p>This module provides functions for file operations, including saving data to text files, reading file contents (including directory contents), getting filenames, and recursively reading files.</p>

<h2>Functions</h2>

<h3><code>save_text_file</code></h3>

<p><strong>Description</strong>: Saves data to a text file. Supports strings, lists of strings, and dictionaries. Handles different data types gracefully.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).  Description of the data being saved.</li>
  <li><code>file_path</code> (str | Path): Path where the file will be saved.  Full path to the destination file.</li>
  <li><code>mode</code> (str, optional): Write mode (`w` for write, `a` for append). Defaults to 'w'.  Specifies the mode for writing to the file. 'w' overwrites the file if it exists, 'a' appends to the file.</li>
  <li><code>exc_info</code> (bool, optional): If True, logs traceback on error. Defaults to True.  Controls whether to include traceback information in the error log.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: True if the file was successfully saved, False otherwise. Indicates the success or failure of the save operation.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Description of the situation in which the general exception is raised.  General error during file operations.</li>
</ul>


<h3><code>read_text_file</code></h3>

<p><strong>Description</strong>: Reads the contents of a file or directory. Supports reading files or directories.  If reading a directory, allows filtering by file extensions.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>file_path</code> (str | Path): Path to the file or directory.  Path to the file or directory.</li>
  <li><code>as_list</code> (bool, optional): If True, returns content as list of lines. Defaults to False.  Controls whether to return the content as a list of lines or as a single string.</li>
  <li><code>extensions</code> (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.  Allows filtering of file extensions when reading a directory. </li>
  <li><code>exc_info</code> (bool, optional): If True, logs traceback on error. Defaults to True.  Controls whether to include traceback information in the error log.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str | list[str] | None</code>: File content as a string or list of lines, or None if an error occurs.  The content of the file or directory, or None if an error occurred.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General error during file operations.</li>
</ul>


<h3><code>get_filenames</code></h3>

<p><strong>Description</strong>: Gets filenames in a directory optionally filtered by extension.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>directory</code> (str | Path): Directory to search. Path to the directory to search.</li>
  <li><code>extensions</code> (str | list[str], optional): Extensions to filter. Defaults to '*'. File extensions or pattern to filter by.</li>
  <li><code>exc_info</code> (bool, optional): If True, logs traceback on error. Defaults to True.  Controls whether to include traceback information in the error log.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>list[str]</code>: Filenames found in the directory. List of filenames.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General error during file operations.</li>
</ul>



<h3><code>recursively_yield_file_path</code></h3>

<p><strong>Description</strong>: Recursively yields file paths matching given patterns.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>root_dir</code> (str | Path): Root directory to search. Directory to start searching from.</li>
  <li><code>patterns</code> (str | list[str], optional): Patterns to filter files. Defaults to '*'.  Patterns to match against file names.</li>
  <li><code>exc_info</code> (bool, optional): If True, logs traceback on error. Defaults to True.  Controls whether to include traceback information in the error log.</li>
</ul>


<p><strong>Yields</strong>:</p>
<ul>
  <li><code>Path</code>: File paths matching the patterns. Paths to the matching files.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General error during file operations.</li>
</ul>

<!-- ... other functions ... -->