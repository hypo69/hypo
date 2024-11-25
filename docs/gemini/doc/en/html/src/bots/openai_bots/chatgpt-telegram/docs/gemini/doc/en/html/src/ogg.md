html
<h1>Ogg Converter Module</h1>

<h2>Overview</h2>
<p>This module provides functionality for converting OGG audio files to MP3 and downloading OGG audio files from URLs.</p>

<h2>Classes</h2>

<h3><code>OggConverter</code></h3>

<p><strong>Description</strong>: This class encapsulates the logic for converting OGG files to MP3 and downloading OGG files from URLs.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>toMp3(input, output)</code>: Converts an OGG file to MP3.</li>
  <li><code>create(url, filename)</code>: Downloads an OGG file from a given URL and saves it.</li>
</ul>


<h2>Functions</h2>

<!-- No functions defined in this module -->


<h2>Methods</h2>

<h3><code>toMp3(input, output)</code></h3>

<p><strong>Description</strong>: Converts an OGG file to MP3 format, optionally limiting the conversion duration to 30 seconds.  Handles errors during conversion and cleans up the original input file on successful conversion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>input</code> (str): Path to the input OGG file.</li>
  <li><code>output</code> (str): Desired output filename (without extension). Output file will be in the same directory as the input file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise&lt;string&gt;</code>: Resolves to the path of the converted MP3 file on success. Rejects with an error message on failure.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>:  Any errors encountered during the FFmpeg conversion process (e.g., invalid input file, FFmpeg errors).</li>
</ul>


<h3><code>create(url, filename)</code></h3>

<p><strong>Description</strong>: Downloads an OGG audio file from a given URL and saves it to a specified location.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>url</code> (str): The URL of the OGG audio file.</li>
  <li><code>filename</code> (str): The name to be used for the downloaded file (without extension).  The extension '.ogg' will be appended.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Promise&lt;string&gt;</code>: Resolves to the path of the downloaded OGG file on success. Rejects with an error message on failure.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: Any errors encountered during the download process (e.g., network issues, invalid URL).</li>
</ul>