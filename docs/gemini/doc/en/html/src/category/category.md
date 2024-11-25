html
<h1>Module src.category</h1>

<h2>Overview</h2>
<p>This module handles category operations, primarily focused on PrestaShop.  It's currently designed to work with PrestaShop data.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Stores the current mode of operation, currently set to 'dev'.</p>


<h2>Classes</h2>

<h3><code>Category</code></h3>

<p><strong>Description</strong>: Represents product categories. Inherits from <code>PrestaCategory</code>.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>credentials</code> (dict): Stores API credentials.  Defaults to None.</li>
</ul>

<p><strong>Methods</strong>:</p>

<h4><code>__init__</code></h4>

<pre><code>python
def __init__(self, api_credentials, *args, **kwards) -> None:
    """
    Initializes the Category object.

    Args:
        api_credentials (dict): API credentials for accessing the PrestaShop API.
        *args:  Variable length argument list (not documented).
        **kwards: Arbitrary keyword arguments (not documented).
    """
</code></pre>


<h4><code>get_parents</code></h4>

<pre><code>python
def get_parents(self, id_category, dept):
    """ Retrieves parent categories.

    Args:
        id_category: The ID of the category.
        dept:  Depth level (not documented).

    Returns:
        list: A list of parent categories (not documented).
    """
</code></pre>


<h4><code>crawl_categories_async</code></h4>

<pre><code>python
async def crawl_categories_async(self, url, depth, driver, locator, dump_file, id_category_default, category: dict = None):
    """ Asynchronous recursive function to traverse categories and build a hierarchical dictionary.

    Args:
        url (str): The URL of the page to traverse.
        depth (int): The depth of recursion.
        driver: Instance of Selenium webdriver.
        locator (dict): Xpath locator for finding category links.
        dump_file (Path): File to save the hierarchical dictionary.
        id_category_default (int): Default category ID.
        category (dict, optional): Dictionary representing a category. Defaults to None.

    Returns:
        dict: Hierarchical dictionary representing categories and their URLs.

    Raises:
        Exception: If errors occur during processing.
    """
</code></pre>


<h4><code>crawl_categories</code></h4>

<pre><code>python
def crawl_categories(self, url, depth: int, driver, locator: dict, dump_file: Path, id_category_default, category: dict = {}):
    """ Recursive function to traverse categories on a website and build a hierarchical dictionary.

    Args:
        url (str): The URL of the page to traverse.
        depth (int): The depth of recursion.
        driver: Instance of Selenium webdriver.
        locator (dict): Xpath locator for finding category links.
        dump_file (Path): File to save the hierarchical dictionary.
        id_category_default (int): Default category ID.
        category (dict, optional): Dictionary representing a category. Defaults to an empty dictionary.

    Returns:
        dict: Hierarchical dictionary representing categories and their URLs.

    Raises:
        Exception: If errors occur during processing.
    """
</code></pre>


<h2>Functions</h2>

<h3><code>check_duplicate_url</code></h3>

<pre><code>python
def check_duplicate_url(dictionary, url) -> bool:
    """ Checks if a given URL already exists in the hierarchical dictionary.

    Args:
        dictionary (dict): The hierarchical dictionary to check.
        url (str): The URL to check for duplicates.

    Returns:
        bool: True if the URL already exists, False otherwise.
    """
</code></pre>

<h3><code>compare_and_print_new_keys</code></h3>

<pre><code>python
def compare_and_print_new_keys(current_dict, file_path):
    """ Compares current values with those in a file.

    Args:
        current_dict (dict): The current dictionary for comparison.
        file_path (str): Path to the file containing data for comparison.

    Prints keys that are missing in the current dictionary.
    """
</code></pre>