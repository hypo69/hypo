html
<h1>Bot Handler Module Documentation</h1>

<h2>Overview</h2>
<p>This module defines the <code>BotHandler</code> class, responsible for handling commands received by a bot, particularly those related to fetching price information from a source like OneTab.</p>

<h2>Classes</h2>

<h3><code>BotHandler</code></h3>

<p><strong>Description</strong>: The <code>BotHandler</code> class is designed to process incoming commands, focusing on extracting data from URLs, like OneTab, and triggering scenarios for generating price quotes.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>mexiron</code> (<code>Mexiron</code>): An instance of the <code>Mexiron</code> class, used to execute price quotation scenarios.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(<code>webdriver_name: Optional[str] = 'firefox'</code>):
    <p><strong>Description</strong>: Initializes the <code>BotHandler</code> instance.  It selects the appropriate webdriver based on the input parameter. Logs a message indicating that the handler has started.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>webdriver_name</code> (<code>Optional[str]</code>, optional): The name of the webdriver to use (firefox, chrome, or edge). Defaults to 'firefox'.</li>
    </ul>
  </li>
  <li><code>handle_url</code>(<code>update: Update, context: CallbackContext</code>) -> <code>Any</code>:
    <p><strong>Description</strong>: Handles incoming URLs, specifically those from OneTab, to extract price, name, and URLs for generating price quotes. Replies with a success or error message based on the outcome of the <code>mexiron.run_scenario</code> call.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>update</code> (<code>Update</code>): The update object containing the received message.</li>
      <li><code>context</code> (<code>CallbackContext</code>): The context object for the bot.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Any</code>: Returns a value based on the result of the scenario execution (e.g., True for successful execution).</li>
    </ul>
  </li>
  <li><code>get_data_from_onetab</code>(<code>response: str</code>) -> <code>list[int | float, str, list] | bool</code>:
    <p><strong>Description</strong>: Extracts price, name, and URLs from the given OneTab response.  Returns `False` if any data is missing.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>response</code> (<code>str</code>): The response string from OneTab.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list[int | float, str, list] | bool</code>: A list containing extracted price, name, and URLs, or `False` if extraction failed.</li>
    </ul>
  </li>
  <li><code>handle_next_command</code>(<code>update: Update</code>) -> <code>None</code>:
    <p><strong>Description</strong>: Handles the '--next' command and related commands, querying an AI model for an answer.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>update</code> (<code>Update</code>): The update object containing the received message.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Catches exceptions during question reading and displays an appropriate error message to the user.</li>
    </ul>
  </li>
   <li><code>fetch_target_urls_onetab</code>(<code>one_tab_url: str</code>) -> <code>list[str] | bool</code>:
    <p><strong>Description</strong>: Fetches target URLs from a OneTab URL. Handles data extraction from the HTML response, including error handling. Returns a list of URLs or `False` if any error occurs.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>one_tab_url</code> (<code>str</code>): The URL to extract the links from.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list[str] | bool</code>: A list of extracted URLs if successful; otherwise, returns `False`.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>requests.exceptions.RequestException</code>: Handles errors related to the HTTP request.</li>
      <li><code>ValueError</code>: Catches errors related to converting the price to an integer.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>
<!-- Add function documentation here if any -->

</body>
</html>