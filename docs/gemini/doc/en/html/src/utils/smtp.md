html
<h1>SMTP Email Interface Module</h1>

<h2>Overview</h2>
<p>This module provides functionality to send and receive emails using an SMTP or IMAP server. It includes functions for sending emails using SMTP and retrieving emails using IMAP.  Crucially, it emphasizes security and robust error handling by avoiding hardcoding credentials and logging exceptions for debugging purposes.  It also handles various MIME formats and potential encoding issues during email retrieval.</p>

<h2>Configuration</h2>
<p>Configuration is handled by the <code>_connection</code> dictionary.  **Crucially, do not hardcode credentials in this file**. Instead, retrieve credentials from environment variables, as shown in the example, to improve security.</p>

<h2>Functions</h2>

<h3><code>send</code></h3>

<p><strong>Description</strong>: Sends an email using the SMTP server specified in the <code>_connection</code> dictionary.  Returns <code>True</code> on success, <code>False</code> on failure. Includes detailed error logging.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>subject</code> (str, optional): The subject of the email. Defaults to an empty string.</li>
  <li><code>body</code> (str, optional): The body of the email. Defaults to an empty string.</li>
  <li><code>to</code> (str, optional): The recipient's email address. Defaults to a value from `_connection`.  This default value is set in the module, but is retrievable from the `_connection` dictionary.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if the email was sent successfully, <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception raised during the SMTP connection or email sending process is logged.</li>
</ul>


<h3><code>receive</code></h3>

<p><strong>Description</strong>: Retrieves emails from an IMAP server and returns them as a list of dictionaries. Returns <code>None</code> on error. Includes detailed error logging.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>imap_server</code> (str): The IMAP server address.</li>
  <li><code>user</code> (str): The IMAP user account.</li>
  <li><code>password</code> (str): The IMAP user password.</li>
  <li><code>folder</code> (str, optional): The email folder to retrieve from (default is 'inbox').</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Optional[List[Dict[str, str]]]</code>: A list of dictionaries, each representing an email with keys for 'subject', 'from', and 'body'. Returns <code>None</code> if there's an error.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception raised during the IMAP connection or email retrieval process is logged.</li>
</ul>