html
<h1>Module: hypotez/src/gui/context_menu/header.py</h1>

<h2>Overview</h2>
<p>This module defines constants and paths related to the project, including GTK, FFmpeg, and Graphviz bin directories.  It also modifies the system path to include these directories, and sets a variable for WeasyPrint.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string variable, likely representing the development mode ('dev').</p>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: A <code>pathlib.Path</code> object representing the absolute path to the project root directory, retrieved from a 'settings.json' file.  Ensures consistency across different project setups by taking project name into account.</p>


<h3><code>gtk_bin_path</code></h3>

<p><strong>Description</strong>: A <code>pathlib.Path</code> object containing the path to the GTK bin directory. Resolves to the project root / bin / gtk / gtk-nsis-pack / bin.</p>

<h3><code>ffmpeg_bin_path</code></h3>

<p><strong>Description</strong>: A <code>pathlib.Path</code> object containing the path to the FFmpeg bin directory. Resolves to the project root / bin / ffmpeg / bin.</p>

<h3><code>graphviz_bin_path</code></h3>

<p><strong>Description</strong>: A <code>pathlib.Path</code> object containing the path to the Graphviz bin directory. Resolves to the project root / bin / graphviz / bin.</p>


<h2>Functions</h2>

<h3><code><span style="color:gray;">(none)</span></code></h3>


<h2>Notes</h2>

<p>The module dynamically updates the <code>sys.path</code> to include the necessary directories, preventing errors when modules or libraries from these directories are called.</p>

<p>It suppresses GTK warnings by using <code>warnings.filterwarnings()</code>.  This is a common practice to prevent the console from being cluttered with warnings that don't impact the functionality.</p>

<h2>Import Statements</h2>

<p>The module imports <code>json</code>, <code>sys</code>, <code>pathlib</code>, and likely other relevant packages.</p>