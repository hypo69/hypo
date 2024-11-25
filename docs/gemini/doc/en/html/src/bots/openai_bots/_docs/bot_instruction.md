html
<h1>Module Documentation</h1>

<h2>Overview</h2>
<p>This module defines various commands for interacting with a system, including greetings, training, testing, archiving, selecting datasets, and displaying instructions.</p>

<h2>Commands</h2>

<h3><code>!hi</code></h3>

<p><strong>Description</strong>: Greets the user.</p>


<h3><code>!train</code></h3>

<p><strong>Description</strong>: Trains the model with the provided data.  Use <code>data</code> for a file, <code>data_dir</code> for a directory, or <code>attachment</code> for a file attachment.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (str, optional): Path to a data file.  Optional if <code>data_dir</code> or <code>attachment</code> are used.</li>
  <li><code>data_dir</code> (str, optional): Path to a directory containing data. Optional if <code>data</code> or <code>attachment</code> are used.</li>
  <li><code>positive</code> (str, optional):  A positive value to pass during training.</li>
  <li><code>attachment</code> (str, optional): Base64 encoded data of the attachment to be used for training.</li>
</ul>

<h3><code>!test</code></h3>

<p><strong>Description</strong>: Tests the model with provided JSON test data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>test_data</code> (str): Path to a JSON file containing test data.</li>
</ul>

<h3><code>!archive</code></h3>

<p><strong>Description</strong>: Archives files in the specified directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>directory</code> (str): Path to the directory to archive.</li>
</ul>

<h3><code>!select_dataset</code></h3>

<p><strong>Description</strong>: Selects a dataset for training from the specified directory.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>path_to_dir_positive</code> (str): Path to the directory containing positive data.</li>
  <li><code>positive</code> (str, optional): Identifier for the specific dataset to select.</li>
</ul>

<h3><code>!instruction</code></h3>

<p><strong>Description</strong>: Displays this instruction message.</p>