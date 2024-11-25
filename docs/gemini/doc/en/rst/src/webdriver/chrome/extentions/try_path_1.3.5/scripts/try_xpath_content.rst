try_xpath_content.js
=====================

This JavaScript file implements the Try XPath browser extension's core logic
for handling XPath queries and updating the browser's display. It manages
various aspects such as updating the CSS, focusing items, handling frame
navigations, and communication with the popup UI.


.. automodule:: hypotez.src.webdriver.chrome.extentions.try_path_1.3.5.scripts.try_xpath_content
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: tryxpath
.. autofunction:: tx
.. autofunction:: fu
.. autofunction:: setAttr
.. autofunction:: setIndex
.. autofunction:: isFocusable
.. autofunction:: focusItem
.. autofunction:: setMainAttrs
.. autofunction:: restoreAttrs
.. autofunction:: resetPrev
.. autofunction:: makeTypeStr
.. autofunction:: updateCss
.. autofunction:: getFrames
.. autofunction:: parseFrameDesignation
.. autofunction:: traceBlankWindows
.. autofunction:: handleCssChange
.. autofunction:: findFrameByMessage
.. autofunction:: setFocusFrameListener
.. autofunction:: initBlankWindow
.. autofunction:: findStyleParent
.. autofunction:: updateStyleElement
.. autofunction:: updateAllStyleElements
.. autofunction:: removeStyleElement
.. autofunction:: removeAllStyleElements
.. autofunction:: createResultMessage
.. autofunction:: genericListener
.. autofunction:: genericListener.listeners.setContentInfo
.. autofunction:: genericListener.listeners.execute
.. autofunction:: genericListener.listeners.focusItem
.. autofunction:: genericListener.listeners.focusContextItem
.. autofunction:: genericListener.listeners.focusFrame
.. autofunction:: genericListener.listeners.requestShowResultsInPopup
.. autofunction:: genericListener.listeners.requestShowAllResults
.. autofunction:: genericListener.listeners.resetStyle
.. autofunction:: genericListener.listeners.setStyle
.. autofunction:: genericListener.listeners.finishInsertCss
.. autofunction:: genericListener.listeners.finishRemoveCss