popup.js
==========

This file contains JavaScript code for a browser popup.  It handles user interactions,
communicates with the background script, and displays results from XPath queries.
It manages the visibility of various UI elements based on user selections,
sends messages to the active tab (and specified frame), and updates the display
of results in the popup, including pagination.  It also manages
restoring the popup's state.


.. automodule:: hypotez.src.webdriver.firefox.extentions.try_path_1.3.5.popup.popup
    :members:
    :undoc-members:
    :show-inheritance:

Functions
--------

.. autofunction:: sendToActiveTab
.. autofunction:: sendToSpecifiedFrame
.. autofunction:: collectPopupState
.. autofunction:: changeContextVisible
.. autofunction:: changeResolverVisible
.. autofunction:: changeFrameIdVisible
.. autofunction:: changeFrameDesignationVisible
.. autofunction:: changeHelpVisible
.. autofunction:: makeExecuteMessage
.. autofunction:: getSpecifiedFrameId
.. autofunction:: execContentScript
.. autofunction:: sendExecute
.. autofunction:: handleExprEnter
.. autofunction:: showDetailsPage
.. autofunction:: showError
.. autofunction:: genericListener