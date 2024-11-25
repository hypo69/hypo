try_xpath_background.js
=======================

This file contains the background script for the Try XPath extension. It handles various communication channels with the popup and content scripts, manages data storage, and dynamically updates styles.

.. automodule:: try_path_1_3_5.background.try_xpath_background
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: try_xpath_background.loadDefaultCss
.. autofunction:: try_xpath_background.genericListener
.. autofunction:: try_xpath_background.genericListener.storePopupState
.. autofunction:: try_xpath_background.genericListener.requestRestorePopupState
.. autofunction:: try_xpath_background.genericListener.requestInsertStyleToPopup
.. autofunction:: try_xpath_background.genericListener.showAllResults
.. autofunction:: try_xpath_background.genericListener.loadResults
.. autofunction:: try_xpath_background.genericListener.updateCss
.. autofunction:: try_xpath_background.genericListener.loadOptions
.. autofunction:: try_xpath_background.genericListener.requestSetContentInfo