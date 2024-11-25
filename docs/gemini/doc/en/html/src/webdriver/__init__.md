html
<h1>Module: hypotez.src.webdriver</h1>

<h2>Overview</h2>
<p>This module provides various WebDriver implementations for interacting with web browsers.  It currently supports Chrome, Firefox, Edge, and other potential browser integrations.  It also includes a CrawleePython class which will need further documentation.  The module's primary purpose is to facilitate browser automation for various web-related tasks.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: This constant defines the current mode of operation for the WebDriver.  Currently set to 'dev'.</p>


<h2>Classes</h2>

<h3><code>Driver</code></h3>

<p><strong>Description</strong>:  Base class for all WebDriver implementations.  It likely contains common functionalities shared by different drivers.</p>


<h3><code>Chrome</code></h3>

<p><strong>Description</strong>: Implementation for controlling the Chrome browser.</p>


<h3><code>Firefox</code></h3>

<p><strong>Description</strong>: Implementation for controlling the Firefox browser.</p>


<h3><code>Edge</code></h3>

<p><strong>Description</strong>: Implementation for controlling the Microsoft Edge browser.</p>


<h3><code>BS</code></h3>

<p><strong>Description</strong>:  Likely implementation related to Beautiful Soup for web scraping.</p>


<h3><code>Playwrid</code></h3>

<p><strong>Description</strong>: Likely implementation for Playwright browser automation.</p>


<h3><code>CrawleePython</code></h3>

<p><strong>Description</strong>: This class is responsible for performing web crawling operations.  More detailed documentation is needed to describe its functionalities, parameters, and expected return values.</p>



<h2>Modules Imported</h2>

<p>This module imports the following modules:</p>

<ul>
<li><code>.driver</code>: Likely contains the base driver class.</li>
<li><code>.chrome</code>: Contains the Chrome driver implementation.</li>
<li><code>.firefox</code>: Contains the Firefox driver implementation.</li>
<li><code>.edge</code>: Contains the Edge driver implementation.</li>
<li><code>.bs</code>: Likely Beautiful Soup related functions.</li>
<li><code>.playwright</code>: Playwright related functions.</li>
<li><code>.crawlee_python</code>: Defines the CrawleePython class (needs more documentation).</li>
</ul>