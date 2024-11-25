html
<h1>hypotez/src/logger/exceptions.py</h1>

<h2>Overview</h2>
<p>This module defines custom exceptions used in the application. It handles errors related to file operations, product fields, KeePass database connections, and PrestaShop WebService errors.  It includes base classes for custom exceptions, specific exceptions for various error types, and provides logging functionality.</p>

<h2>Classes</h2>

<h3><code>CustomException</code></h3>

<p><strong>Description</strong>: Base custom exception class.  Handles logging of the exception and provides a mechanism for dealing with the original exception, if it exists.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>original_exception</code> (Optional[Exception]): The original exception that caused this custom exception, if any.</li>
  <li><code>exc_info</code> (bool): A flag to indicate if exception information should be logged.</li>
</ul>

<p><strong>Method</strong>:</p>
<ul>
  <li><code>__init__</code>(message: str, e: Optional[Exception] = None, exc_info: bool = True): Initializes the CustomException with a message and an optional original exception.  Logs the error and original exception, if available.</li>
  <li><code>handle_exception</code>(): Handles the exception by logging the error and original exception, if available.  Includes a placeholder for recovery logic.</li>
</ul>


<h3><code>FileNotFoundError</code></h3>

<p><strong>Description</strong>: Exception raised when a file is not found.</p>


<h3><code>ProductFieldException</code></h3>

<p><strong>Description</strong>: Exception raised for errors related to product fields.</p>


<h3><code>KeePassException</code></h3>

<p><strong>Description</strong>: Exception raised for errors related to KeePass database connections.  Inherits from multiple KeePass exceptions.</p>


<h3><code>DefaultSettingsException</code></h3>

<p><strong>Description</strong>: Exception raised for issues with default settings.</p>


<h3><code>WebDriverException</code></h3>

<p><strong>Description</strong>: Exception raised for WebDriver related issues.  Inherits from selenium's WebDriverException.</p>


<h3><code>ExecuteLocatorException</code></h3>

<p><strong>Description</strong>: Exception raised for errors related to locator executors.</p>


<h3><code>PrestaShopException</code></h3>

<p><strong>Description</strong>: Generic exception for PrestaShop WebService errors.  Used for handling errors when interacting with the PrestaShop WebService.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>msg</code> (str): A custom error message.</li>
  <li><code>error_code</code> (Optional[int]): The error code returned by PrestaShop.</li>
  <li><code>ps_error_msg</code> (str): The error message from PrestaShop.</li>
  <li><code>ps_error_code</code> (Optional[int]): The PrestaShop error code.</li>
</ul>

<p><strong>Method</strong>:</p>
<ul>
  <li><code>__init__</code>(msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None): Initializes the PrestaShopException with the provided message and error details.</li>
  <li><code>__str__</code>(): Returns the string representation of the exception (defaulting to ps_error_msg or msg).</li>
</ul>


<h3><code>PrestaShopAuthenticationError</code></h3>

<p><strong>Description</strong>: Exception raised for PrestaShop authentication errors (Unauthorized).</p>


<h2>Functions</h2>
<p>(No functions defined in the provided file)</p>

<h2>Module Constants</h2>
<p><code>MODE</code> (str): Holds the value 'dev'.</p>