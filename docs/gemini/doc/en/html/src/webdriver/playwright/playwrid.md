html
<h1>Playwrid Crawler</h1>

<h2>Overview</h2>
<p>This code defines a subclass of <code>PlaywrightCrawler</code> called <code>Playwrid</code>. It provides additional functionality such as the ability to set custom browser settings, profiles, and launch options using Playwright.</p>
<p>
    <a href="https://chatgpt.com/share/67428d3f-6b18-800d-a585-eb414eef60e2">More Details</a>
</p>

<h2>Classes</h2>

<h3><code>Playwrid</code></h3>

<p><strong>Description</strong>: Subclass of <code>PlaywrightCrawler</code> that provides additional functionality.</p>

<p><strong>Attributes</strong>:</p>
<ul>
    <li><code>driver_name</code> (str): 'playwrid'</li>
    <li><code>context</code> (object): None</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
    <li><code>__init__</code></li>
    <li><code>_load_settings</code></li>
    <li><code>_set_launch_options</code></li>
    <li><code>start</code></li>
    <li><code>current_url</code></li>
</ul>

<h3><code>__init__</code></h3>

<p><strong>Description</strong>: Initializes the Playwright Crawler with the specified launch options, settings, and user agent.</p>

<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>settings_name</code> (Optional[str], optional): Name of the settings file to use. Defaults to None.</li>
    <li><code>user_agent</code> (Optional[Dict[str, Any]], optional): A dictionary containing user agent settings. Defaults to None.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
    <li>N/A</li>
</ul>

<h3><code>_load_settings</code></h3>

<p><strong>Description</strong>: Loads the settings for the Playwrid Crawler.</p>

<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>settings_name</code> (Optional[str], optional): Name of the settings file to use. Defaults to None.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
    <li><code>SimpleNamespace</code>: A SimpleNamespace object containing the settings.</li>
</ul>

<h3><code>_set_launch_options</code></h3>

<p><strong>Description</strong>: Configures the launch options for the Playwright Crawler.</p>

<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>settings</code> (SimpleNamespace): A SimpleNamespace object containing launch settings.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
    <li><code>dict</code>: A dictionary with launch options for Playwright.</li>
</ul>

<h3><code>start</code></h3>

<p><strong>Description</strong>: Starts the Playwrid Crawler and navigates to the specified URL.</p>

<p><strong>Parameters</strong>:</p>
<ul>
    <li><code>url</code> (str): The URL to navigate to.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
    <li>Exception: Any exception that occurs during the crawling process.</li>
</ul>

<h3><code>current_url</code></h3>

<p><strong>Description</strong>: Property to get the current URL.</p>


<p><strong>Returns</strong>:</p>

<ul>
 <li><code>...</code>: Returns a value representing the current URL.</li>
</ul>


<hr/>