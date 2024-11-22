```rst
hypotez.webdriver.bs
=====================

.. module:: hypotez.webdriver.bs
   :platform: Windows, Unix
   :synopsis: Parse pages with BeautifulSoup and XPath.


Module Description
------------------

This module provides a class (`BS`) for parsing HTML content fetched from files or URLs using BeautifulSoup and XPath.  It supports handling file paths (including Windows paths) and URLs.


Classes
-------

.. autoclass:: hypotez.webdriver.bs.BS
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: hypotez.webdriver.bs.BS.__init__
.. autofunction:: hypotez.webdriver.bs.BS.get_url
.. autofunction:: hypotez.webdriver.bs.BS.execute_locator


Example Usage
------------

The following example demonstrates how to use the `BS` class to fetch and parse HTML content:

.. code-block:: python
    import hypotez.webdriver.bs as bs

    # Create a BS object
    parser = bs.BS()

    # Get HTML from a file
    url_file = 'path/to/your/file.html'  # Replace with an actual file path
    if parser.get_url(url_file):
        # ... now parser.html_content contains parsed content
    else:
       print("Failed to load the file.")

    # Example usage of execute_locator
    locator = SimpleNamespace(attribute="your_attribute", by="CSS", selector="//div[@class='your-class']")

    elements = parser.execute_locator(locator)
    if elements:
        for element in elements:
            print(element.text)


.. note::

    - Replace 'path/to/your/file.html' with the actual path to your HTML file.
    - This example demonstrates getting data from a file.  Handling URLs is similar.
    - The `execute_locator` function requires a `SimpleNamespace` object with specific attributes ('attribute', 'by', 'selector') to locate elements on the webpage.   


.. important::

    - Error handling is implemented in `get_url` to catch potential issues like invalid file paths, network errors, etc.


```
