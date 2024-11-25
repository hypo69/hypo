html
<h1>try_xpath_functions.js</h1>

<h2>Overview</h2>
<p>This JavaScript file defines functions for evaluating XPath expressions, querying elements using querySelector and querySelectorAll, and working with the results.  It provides methods for handling various XPath result types and interacting with DOM elements.</p>

<h2>Functions</h2>

<h3><code>execExpr</code></h3>

<p><strong>Description</strong>: Executes an XPath expression or a query selector on a given context.  It returns an object containing the results (an array of items), the execution method, and the result type.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>expr</code> (str): The XPath expression or query selector string.</li>
  <li><code>method</code> (str): The execution method ("evaluate", "querySelector", or "querySelectorAll").</li>
  <li><code>opts</code> (dict, optional): An optional object containing additional options, such as the context for the execution (e.g., `document`, an element) and a resolver function for XPath.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: An object containing the following fields:
    <ul>
      <li><code>items</code> (array): An array of the results. This depends on the `method` and XPath result types.</li>
      <li><code>method</code> (str): The execution method used.</li>
      <li><code>resultType</code> (int or null): The XPath result type (if applicable), otherwise null.</li>
    </ul>
  </li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the context is not a valid node (e.g., not a Document or an Element).</li>
</ul>


<h3><code>resToArr</code></h3>

<p><strong>Description</strong>: Converts the result of an XPath evaluation to an array, handling different XPath result types.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>res</code> (object): The XPath result object.</li>
  <li><code>type</code> (int, optional): The XPath result type. If undefined, it defaults to `res.resultType`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>array</code>: An array of nodes or other result values.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the provided `resultType` is invalid.</li>
</ul>



<h3><code>makeResolver</code></h3>

<p><strong>Description</strong>: Creates a resolver function for XPath expressions, handling different input types (string, object, and functions).</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>obj</code> (object | function | string, optional): The resolver input. Can be a function, a string representing a JSON object, or an object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>function</code>: A resolver function that maps a string to a value from the input object.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Error</code>: If the input resolver is invalid (not a valid JSON string or object).</li>
</ul>


<!-- ... other function descriptions (e.g., makeResolver, isValidDict, objToMap, etc.) ... -->

<!-- ... Include more functions with similar formatting ... -->
```
```javascript