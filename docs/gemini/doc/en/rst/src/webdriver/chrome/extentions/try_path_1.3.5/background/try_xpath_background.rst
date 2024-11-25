try_xpath_background.js
=====================

This file defines the background script for the Try XPath extension.
It handles communication with the popup and content scripts,
managing persistent storage, and loading default styles.
It also allows storing and restoring popup state.


.. automodule:: try_xpath_background
    :members:
    :undoc-members:
    :show-inheritance:


Functions
--------

.. autofunction:: try_xpath_background.loadDefaultCss
.. autofunction:: try_xpath_background.genericListener
.. autofunction:: try_xpath_background.genericListener.listeners.storePopupState
.. autofunction:: try_xpath_background.genericListener.listeners.requestRestorePopupState
.. autofunction:: try_xpath_background.genericListener.listeners.requestInsertStyleToPopup
.. autofunction:: try_xpath_background.genericListener.listeners.showAllResults
.. autofunction:: try_xpath_background.genericListener.listeners.loadResults
.. autofunction:: try_xpath_background.genericListener.listeners.updateCss
.. autofunction:: try_xpath_background.genericListener.listeners.loadOptions
.. autofunction:: try_xpath_background.genericListener.listeners.requestSetContentInfo