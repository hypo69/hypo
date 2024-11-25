html
<h1>src.logger Module</h1>

<h2>Overview</h2>
<p>This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.</p>

<h2>Classes</h2>

<h3><code>SingletonMeta</code></h3>

<p><strong>Description</strong>: Metaclass for Singleton pattern implementation.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>__call__</code>: Initializes and returns the Singleton instance.</li>
</ul>


<h3><code>JsonFormatter</code></h3>

<p><strong>Description</strong>: Custom formatter for logging in JSON format.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>format</code>(record: logging.LogRecord) -&gt; str: Format the log record as JSON.</li>
</ul>


<h3><code>Logger</code></h3>

<p><strong>Description</strong>: Singleton logger class with methods for console, file, and JSON logging.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>__init__</code>(): Initializes the Logger instance.</li>
<li><code>_configure_logger</code>(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -&gt; logging.Logger: Configures and returns a logger.</li>
<li><code>initialize_loggers</code>(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''): Initializes loggers for console, file, and JSON output.</li>
<li><code>_format_message</code>(message, ex=None, color=None): Returns formatted message with optional color and exception information.</li>
<li><code>_ex_full_info</code>(ex): Provides detailed exception information, including the file, function, and line number where the log was called.</li>
<li><code>log</code>(level, message, ex=None, exc_info=False, color=None): Logs messages at a specified level with optional color and exception information.</li>
<li><code>info</code>(message, ex=None, exc_info=False, colors: Optional[tuple] = None): Logs an info message.</li>
<li><code>success</code>(message, ex=None, exc_info=False, colors: Optional[tuple] = None): Logs a success message.</li>
<li><code>warning</code>(message, ex=None, exc_info=False, colors: Optional[tuple] = None): Logs a warning message.</li>
<li><code>debug</code>(message, ex=None, exc_info=True, colors: Optional[tuple] = None): Logs a debug message.</li>
<li><code>error</code>(message, ex=None, exc_info=True, colors: Optional[tuple] = None): Logs an error message.</li>
<li><code>critical</code>(message, ex=None, exc_info=True, colors: Optional[tuple] = None): Logs a critical message.</li>
</ul>

<h2>Functions</h2>

<!-- No functions are defined, only classes are included -->