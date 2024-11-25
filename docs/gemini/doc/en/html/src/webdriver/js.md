html
<h1>Module src.webdriver.js</h1>

<h2>Overview</h2>
<p>This module provides JavaScript utility functions for interacting with a web page, extending the capabilities of Selenium WebDriver. It includes functions for making invisible DOM elements visible, retrieving page metadata (like ready state, referrer, and language), and managing browser focus.</p>

<h2>Classes</h2>

<h3><code>JavaScript</code></h3>

<p><strong>Description</strong>: Provides JavaScript utility functions for interacting with a web page.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>
    <p><strong>Description</strong>: Initializes the JavaScript helper with a Selenium WebDriver instance.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>driver</code> (WebDriver): Selenium WebDriver instance to execute JavaScript.</li>
    </ul>
  </li>
  <li><code>unhide_DOM_element</code>
    <p><strong>Description</strong>: Makes an invisible DOM element visible by modifying its style properties.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>element</code> (WebElement): The WebElement object to make visible.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool</code>: True if the script executes successfully, False otherwise.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Description of the situation in which the exception is raised (e.g., error executing the script).</li>
    </ul>
  </li>
  <li><code>ready_state</code>
    <p><strong>Description</strong>: Retrieves the document loading status.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: 'loading' if the document is still loading, 'complete' if loading is finished. Returns an empty string if there's an error.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Description of the situation in which the exception is raised (e.g., error retrieving the ready state).</li>
    </ul>
  </li>
  <li><code>window_focus</code>
    <p><strong>Description</strong>: Sets focus to the browser window using JavaScript.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Description of the situation in which the exception is raised (e.g., error executing the focus script).</li>
    </ul>
  </li>
  <li><code>get_referrer</code>
    <p><strong>Description</strong>: Retrieves the referrer URL of the current document.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The referrer URL, or an empty string if unavailable.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Description of the situation in which the exception is raised (e.g., error retrieving the referrer).</li>
    </ul>
  </li>
  <li><code>get_page_lang</code>
    <p><strong>Description</strong>: Retrieves the language of the current page.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str</code>: The language code of the page, or an empty string if unavailable.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: Description of the situation in which the exception is raised (e.g., error retrieving the page language).</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>
<!-- No functions defined in this module -->