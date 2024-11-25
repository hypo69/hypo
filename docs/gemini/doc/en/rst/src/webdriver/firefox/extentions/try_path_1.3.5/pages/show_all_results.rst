show_all_results.js
====================

This JavaScript file handles the display of search results in a web page. It receives results from a browser extension, updates the UI elements, and allows interaction with the results.  It utilizes tryxpath functions for data processing.


Functions
--------

.. autofunction:: showAllResults
   :noindex:
   :param results: (object): The search results object containing data for the query.
   :returns: None
   :raises: None


.. autofunction:: makeTextDownloadUrl
   :noindex:
   :param text: (string): The text to be downloaded.
   :returns: (string): The URL for downloading the text.
   :raises: None


.. autofunction:: makeInfoText
   :noindex:
   :param results: (object): The search results object containing data for the query.
   :returns: (string): The formatted text for download, including context and main information.
   :raises: None


.. autofunction:: makeConvertedInfoText
   :noindex:
   :param results: (object): The search results object containing data for the query.
   :returns: (string): The formatted, converted text for download. Includes JSON representation of expression values.
   :raises: None