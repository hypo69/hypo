html
<h1>Module: hypotez/src/endpoints/advertisement/facebook/start_event.py</h1>

<h2>Overview</h2>
<p>This module contains the logic for sending events to Facebook groups. It utilizes the FacebookPromoter class and WebDriver to interact with the Facebook platform.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the mode of operation (currently set to 'dev').</p>

<h2>Imports</h2>

<p>Imports necessary modules for various functionalities including mathematical operations, time management, JSON handling, WebDriver interactions, Facebook promotional logic, and logging.</p>
<ul>
  <li><code>math</code>: For mathematical functions.</li>
  <li><code>header</code>: (Assuming a custom module). Used for potential header related tasks.</li>
  <li><code>time</code>: For time-related functions.</li>
  <li><code>src.utils.jjson</code>: For JSON loading.</li>
  <li><code>src.webdriver</code>: For interacting with the web driver.</li>
  <li><code>src.endpoints.advertisement.facebook</code>: For Facebook promotional methods.</li>
  <li><code>src.logger</code>: For logging.</li>
</ul>


<h2>Classes</h2>

<h3><code>Driver</code></h3>
<p><strong>Description</strong>:  (Assumed class from src.webdriver, implementation omitted)</p>
<p><strong>Methods</strong>:</p>

<ul>
    <li><code>get_url(url: str)</code>: Retrieves and navigates to a specified URL.</li>

</ul>


<h3><code>FacebookPromoter</code></h3>
<p><strong>Description</strong>: (Assumed class, implementation omitted).  Handles promotion of events to Facebook groups.</p>
<p><strong>Methods</strong>:</p>
<ul>
  <li><code>run_events(events_names: list, group_file_paths: list)</code>: Runs the promotion events.</li>
</ul>


<h2>Functions</h2>

(None defined in this module)


<h2>Variables</h2>

<h3><code>filenames</code></h3>
<p><strong>Description</strong>: A list of file names containing data for the Facebook groups to send events to.</p>
<p><strong>Type</strong>: <code>list[str]</code></p>
<pre><code class="language-python">filenames:list[str] = [ "my_managed_groups.json", ... ]</code></pre>


<h3><code>excluded_filenames</code></h3>
<p><strong>Description</strong>: A list of file names to exclude when processing Facebook groups.</p>
<p><strong>Type</strong>: <code>list[str]</code></p>
<pre><code class="language-python">excluded_filenames:list[str] = ["my_managed_groups.json",]</code></pre>

<h3><code>events_names</code></h3>
<p><strong>Description</strong>: A list of event names to be processed.</p>
<p><strong>Type</strong>: <code>list</code></p>
<pre><code class="language-python">events_names:list = ["choice_day_01_10"]</code></pre>

<h3><code>promoter</code></h3>
<p><strong>Description</strong>: An instance of the <code>FacebookPromoter</code> class.</p>
<p><strong>Type</strong>: <code>FacebookPromoter</code></p>


<h2>Code Logic</h2>

<p>The code initializes a <code>Driver</code> object, navigates to Facebook, and then creates a <code>FacebookPromoter</code> object.  It enters a loop that continuously runs the <code>run_events</code> method until interrupted, logging progress.  This pattern suggests a continuous campaign promotion process.</p>

<h2>Error Handling</h2>

<p>The code includes a <code>try...except KeyboardInterrupt</code> block to gracefully handle the interruption of the script, providing a more user-friendly experience.</p>