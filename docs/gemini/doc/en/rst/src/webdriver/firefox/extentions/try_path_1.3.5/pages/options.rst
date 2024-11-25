options.js
==========

.. automodule:: hypotez.src.webdriver.firefox.extentions.try_path_1.3.5.pages.options
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: isValidAttrName
    :noindex:

.. autofunction:: isValidAttrNames
    :noindex:

.. autofunction:: isValidStyleLength
    :noindex:

.. autofunction:: loadDefaultCss
    :noindex:

.. autofunction:: extractBodyStyles
    :noindex:

.. autofunction:: createPopupCss
    :noindex:


Global Variables
---------------

.. autovariable:: elementAttr
.. autovariable:: contextAttr
.. autovariable:: focusedAttr
.. autovariable:: ancestorAttr
.. autovariable:: frameAttr
.. autovariable:: frameAncestorAttr
.. autovariable:: style
.. autovariable:: popupBodyWidth
.. autovariable:: popupBodyHeight
.. autovariable:: message
.. autovariable:: testElement
.. autovariable:: defaultAttributes
.. autovariable:: defaultPopupBodyStyles


Description
-----------

This JavaScript file (`options.js`) handles the options page for the Try XPath extension.  It allows users to configure various attributes and CSS styles for the extension's behavior.  The script interacts with browser APIs (`browser.runtime`, `browser.storage.sync`) to persist user settings.  The page contains input fields for attributes, CSS styles, and a save button.  The "Show Default" button resets the configuration to the default values.  Error handling and validation are included to ensure user input is valid.