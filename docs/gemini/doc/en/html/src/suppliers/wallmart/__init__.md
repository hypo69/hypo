html
<h1>Module wallmart</h1>

<h2>Overview</h2>
<p>This module provides access to Walmart data through the <code>Graber</code> class.</p>

<h2>Classes</h2>

<h3><code>Graber</code></h3>

<p><strong>Description</strong>: This class is responsible for fetching data from Walmart.</p>

<p><strong>Methods</strong>:</p>
<ul>
<li><code>get_data</code>: Retrieves data from Walmart.
  <ul>
    <li><strong>Description</strong>: Fetches data from Walmart based on specified criteria.</li>
    <li><strong>Parameters</strong>:
      <ul>
        <li><code>criteria</code> (dict): A dictionary of criteria for data filtering.</li>
      </ul>
    </li>
    <li><strong>Returns</strong>:
      <ul>
        <li><code>dict | None</code>: A dictionary containing the fetched data, or <code>None</code> if there was an issue.</li>
      </ul>
    </li>
    <li><strong>Raises</strong>:
        <ul>
            <li><code>WalmartAPIError</code>: Raised when there's an issue connecting to the Walmart API.</li>
            <li><code>InvalidCriteriaError</code>: Raised if the input criteria are invalid.</li>
        </ul>
    </li>
  </ul>
</li>
</ul>


<h2>Functions</h2>

<p>This module does not contain any functions.</p>