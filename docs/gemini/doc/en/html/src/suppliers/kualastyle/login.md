html
<h1>Module: src.suppliers.kualastyle.login</h1>

<h2>Overview</h2>
<p>This module contains functions for supplier login.</p>

<h2>Functions</h2>

<h3><code>login</code></h3>

<p><strong>Description</strong>: Function for logging in a supplier.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if login successful, <code>False</code> otherwise.</li>
</ul>


<h3><code>close_pop_up</code></h3>

<p><strong>Description</strong>: Function to close pop-up windows.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>s</code>: Supplier object.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>bool</code>: <code>True</code> if pop-up closed successfully, <code>False</code> otherwise.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Generic exception for errors during pop-up closure.</li>
</ul>

<p><strong>Details</strong>: This function retrieves the supplier's driver and locator for the pop-up close button. It navigates to the supplier's website, waits for the pop-up to appear and then tries to close it using the locator. If any exception occurs during this process, a warning message is logged.</p>