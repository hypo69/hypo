html
<h1>Module: hypotez/src/endpoints/kazarinov/react/pricelist_generator.py</h1>

<h2>Overview</h2>
<p>This module provides a class for generating HTML and PDF reports based on data from a JSON file.  It utilizes Jinja2 for HTML templating and wkhtmltopdf for PDF conversion.</p>

<h2>Classes</h2>

<h3><code>ReportGenerator</code></h3>

<p><strong>Description</strong>: A class responsible for generating HTML and PDF reports from JSON data.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>template_path</code> (str): Path to the Jinja2 template file. Defaults to <code>gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'</code>.</li>
  <li><code>env</code> (Environment): Jinja2 environment object for loading and rendering templates. Initialized using FileSystemLoader.</li>
</ul>

<p><strong>Methods</strong>:</p>

<h4><code>generate_html(self, data: dict) -> str</code></h4>

<p><strong>Description</strong>: Generates HTML content based on the provided template and data.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (dict): The data to be used to render the template.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The generated HTML content.</li>
</ul>

<h4><code>create_report(self, data: dict, html_file: str | Path, pdf_file: str | Path) -> None</code></h4>

<p><strong>Description</strong>: Executes the full report generation process, including HTML generation, saving, and PDF conversion.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>data</code> (dict): The data to be used for generating the report.</li>
  <li><code>html_file</code> (str | Path): The path to save the generated HTML file.</li>
  <li><code>pdf_file</code> (str | Path): The path to save the generated PDF file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>:  The method does not return a value.</li>
</ul>


<h2>Global Variables</h2>
<ul>
  <li><code>MODE</code> (str):  The current operation mode, likely 'dev'.</li>
</ul>

<h2>Imports</h2>
<p>The module imports various libraries, including dataclasses, JSON handling, path manipulation, Jinja2 templating, PDFKit, custom utility functions, and logging.</p>
<ul>
<li><code>header</code></li>
<li><code>dataclasses</code></li>
<li><code>src.gs</code></li>
<li><code>json</code></li>
<li><code>pathlib</code></li>
<li><code>jinja2</code></li>
<li><code>pdfkit</code></li>
<li><code>src.utils.jjson</code></li>
<li><code>src.utils.file</code></li>
<li><code>src.utils.pdf</code></li>
<li><code>src.utils.convertors.html</code></li>
<li><code>src.utils.printer</code></li>
<li><code>src.logger</code></li>
</ul>