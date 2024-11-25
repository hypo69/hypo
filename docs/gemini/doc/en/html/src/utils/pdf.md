html
<h1>Module: hypotez/src/utils/pdf.py</h1>

<h2>Overview</h2>
<p>This module provides functionalities for converting HTML content or files to PDF format using the `pdfkit` library.  It also includes an alternative method using the `FPDF` library for saving text to PDF.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string constant representing the current mode (e.g., 'dev').</p>

<h2>Functions</h2>

<h3><code>set_project_root</code></h3>

<p><strong>Description</strong>: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the specified marker files.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>marker_files</code> (tuple): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Path</code>: Path to the root directory if found, otherwise the directory where the script is located.</li>
</ul>


<h3><code>PDFUtils.save_pdf</code></h3>

<p><strong>Description</strong>: Saves HTML content or a file to a PDF file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (str | Path): HTML content or a path to an HTML file.</li>
  <li><code>pdf_file</code> (str | Path): Path to the output PDF file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the PDF was successfully saved, otherwise <code>False</code>.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>pdfkit.PDFKitError</code>: Error during PDF generation using `pdfkit`.</li>
  <li><code>OSError</code>: Error accessing the file.</li>
</ul>

<h3><code>PDFUtils.save_pdf_v2</code></h3>

<p><strong>Description</strong>: An alternative method for saving text to PDF using the `FPDF` library.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (str): Text to be saved in the PDF.</li>
  <li><code>pdf_file</code> (str | Path): Path to the output PDF file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the PDF was successfully saved, otherwise <code>False</code>.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: General exception during PDF generation.</li>
</ul>


<h2>Variables</h2>

<h3><code>__root__</code></h3>

<p><strong>Description</strong>: Path to the root directory of the project.  Initialized by the `set_project_root` function.</p>

<h3><code>wkhtmltopdf_exe</code></h3>
<p><strong>Description</strong>: Path to wkhtmltopdf.exe.  Initialized using the project root.</p>


<h3><code>configuration</code></h3>

<p><strong>Description</strong>: PDFKit configuration object.  Uses `wkhtmltopdf` from the project's `bin` folder.</p>
<h3><code>options</code></h3>

<p><strong>Description</strong>: Options passed to `pdfkit` for PDF generation.  Includes `enable-local-file-access` to allow local file access (likely for static HTML templates).</p>