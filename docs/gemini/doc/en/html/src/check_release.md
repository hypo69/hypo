html
<h1>Module check_release</h1>

<h2>Overview</h2>
<p>This module provides a function to check the latest release version of a GitHub repository.</p>

<h2>Functions</h2>

<h3><code>check_latest_release</code></h3>

<p><strong>Description</strong>: Checks the latest release version of a GitHub repository.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>owner</code> (str): The owner of the repository.</li>
  <li><code>repo</code> (str): The name of the repository.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: The latest release version if available, else <code>None</code>.</li>
</ul>


<p><strong>Raises</strong>:</p>
<ul>
</ul>

<pre><code>python
def check_latest_release(owner: str, repo: str) -> str | None:
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    response = requests.get(url)

    if response.status_code == 200:
        latest_release = response.json()
        return latest_release['tag_name']
    else:
        return None  # Explicitly return None
</code></pre>