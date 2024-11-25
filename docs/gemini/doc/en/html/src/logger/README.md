html
<h1>src.logger Module Documentation</h1>

<h2>Overview</h2>
<p>The <code>src.logger</code> module provides a flexible logging system supporting console, file, and JSON logging. It utilizes the Singleton design pattern for a single logger instance.  The logger supports various log levels (INFO, ERROR, DEBUG) and colorized output for console logs.  It allows for custom log output formats and logging to different files.</p>

<h2>Classes</h2>

<h3><code>SingletonMeta</code></h3>

<p><strong>Description</strong>: Metaclass implementing the Singleton design pattern for the logger.</p>


<h3><code>JsonFormatter</code></h3>

<p><strong>Description</strong>: A custom formatter for outputting logs in JSON format.</p>


<h3><code>Logger</code></h3>

<p><strong>Description</strong>: The main logger class supporting console, file, and JSON logging.</p>
<p><strong>Methods</strong>:</p>
<ul>
<li><code>__init__</code>: Initializes the Logger instance.</li>
<li><code>_configure_logger</code>: Configures and returns a logger instance.</li>
<li><code>initialize_loggers</code>: Initializes loggers for console and file logging (info, debug, error, and JSON).</li>
<li><code>log</code>: Logs a message at the specified level.</li>
<li><code>info</code>: Logs an info message.</li>
<li><code>success</code>: Logs a success message.</li>
<li><code>warning</code>: Logs a warning message.</li>
<li><code>debug</code>: Logs a debug message.</li>
<li><code>error</code>: Logs an error message.</li>
<li><code>critical</code>: Logs a critical message.</li>
</ul>


<h2>Functions</h2>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the Logger instance with placeholders for different logger types (console, file, and JSON).</p>


<h3><code>_configure_logger</code></h3>

<p><strong>Description</strong>: Configures and returns a logger instance.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>name</code> (str): Name of the logger.</li>
<li><code>log_path</code> (str): Path to the log file.</li>
<li><code>level</code> (Optional[int], optional): Logging level. Defaults to <code>logging.DEBUG</code>.</li>
<li><code>formatter</code> (Optional[logging.Formatter], optional): Custom formatter.</li>
<li><code>mode</code> (Optional[str], optional): File mode, defaults to 'a' (append).</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
<li><code>logging.Logger</code>: Configured logger instance.</li>
</ul>


<h3><code>initialize_loggers</code></h3>

<p><strong>Description</strong>: Initializes the loggers for console and file logging (info, debug, error, and JSON).</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>info_log_path</code> (Optional[str], optional): Path for info log file.</li>
<li><code>debug_log_path</code> (Optional[str], optional): Path for debug log file.</li>
<li><code>errors_log_path</code> (Optional[str], optional): Path for error log file.</li>
<li><code>json_log_path</code> (Optional[str], optional): Path for JSON log file.</li>
</ul>


<h3><code>log</code></h3>

<p><strong>Description</strong>: Logs a message at the specified level with optional exception and color formatting.</p>

<p><strong>Parameters</strong>:</p>
<ul>
<li><code>level</code>: Logging level (e.g., <code>logging.INFO</code>, <code>logging.DEBUG</code>).</li>
<li><code>message</code>: The log message.</li>
<li><code>ex</code> (Optional): Optional exception to log.</li>
<li><code>exc_info</code> (bool): Include exception information (defaults to False).</li>
<li><code>color</code> (Optional[tuple]): Tuple with text and background colors for console output.</li>
</ul>


<h3><code>info</code>, <code>success</code>, <code>warning</code>, <code>debug</code>, <code>error</code>, <code>critical</code></h3>

<p>(These share the same parameter structure as <code>log</code>)</p>


<h2>Parameters for the Logger</h2>

<p>The <code>Logger</code> class accepts several optional parameters for customizing logging behavior:</p>

<ul>
<li><strong>Level</strong>: Controls the severity of captured logs.</li>
<li><strong>Formatter</strong>: Defines log message format.</li>
<li><strong>Color</strong>: Tuple specifying text and background colors for console output.</li>
</ul>

<h2>File Logging Configuration (config)</h2>
<p>To log messages to a file, specify file paths in the <code>config</code> dictionary.</p>

<h2>Example Usage</h2>
<p>(Example code blocks are already present in the input.  These are correctly formatted for inclusion within the HTML)</p>

<h2>Conclusion</h2>
<p>This module provides a comprehensive and customizable logging system for Python applications.</p>