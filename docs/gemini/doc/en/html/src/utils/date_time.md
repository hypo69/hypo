html
<h1>Module date_time</h1>

<h2>Overview</h2>
<p>This module provides functions for checking if the current time falls within a specified interval, optionally with a timeout.  It's useful for scheduling operations that should only run during specific time periods.</p>

<h2>Classes</h2>

<h3><code>TimeoutCheck</code></h3>

<p><strong>Description</strong>: This class encapsulates the time interval checking functionality with optional timeouts.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool</code>
    <p><strong>Description</strong>: Checks if the current time is within the specified interval.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>start (time):</code> Start of the interval (default is 23:00).</li>
      <li><code>end (time):</code> End of the interval (default is 06:00).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool:</code> True if the current time is within the interval, False otherwise.</li>
    </ul>
  </li>
  <li><code>interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool</code>
    <p><strong>Description</strong>: Checks if the current time is within the specified interval with a timeout.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>timeout (int):</code> Time in seconds to wait for the interval check.</li>
      <li><code>start (time):</code> Start of the interval (default is 23:00).</li>
      <li><code>end (time):</code> End of the interval (default is 06:00).</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>bool:</code> True if the current time is within the interval and response within timeout, False if not or timeout occurs.</li>
    </ul>
  </li>
  <li><code>get_input(self)</code>
    <p><strong>Description</strong>: Prompts the user for input.</p>
    <p><strong>Returns</strong>:</p> <ul>
      <li>No explicit return</li>
    </ul>

  </li>
  <li><code>input_with_timeout(self, timeout: int = 5) -> str | None</code>
    <p><strong>Description</strong>: Waits for user input with a timeout.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>timeout (int):</code> Time in seconds to wait for input.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>str | None:</code> The input from the user if available, otherwise <code>None</code> if a timeout occurs.</li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>
<p>(None)</p>