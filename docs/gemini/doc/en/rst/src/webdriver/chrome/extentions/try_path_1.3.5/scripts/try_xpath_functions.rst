try_xpath_functions.js Documentation
==================================

This file contains JavaScript functions for evaluating XPath expressions,
querying elements using `querySelector` and `querySelectorAll`, and
manipulating HTML elements. It defines functions for converting
XPath evaluation results to arrays, creating and manipulating tables,
handling different result types, and managing element attributes and
classes.


.. automodule:: hypotez.src.webdriver.chrome.extentions.try_path_1.3.5.scripts.try_xpath_functions
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: tryxpath.functions.execExpr
.. autofunction:: tryxpath.functions.resToArr
.. autofunction:: tryxpath.functions.makeResolver
.. autofunction:: tryxpath.functions.isValidDict
.. autofunction:: tryxpath.functions.objToMap
.. autofunction:: tryxpath.functions.isDocOrElem
.. autofunction:: tryxpath.functions.listToArr
.. autofunction:: tryxpath.functions.getItemDetail
.. autofunction:: tryxpath.functions.getItemDetails
.. autofunction:: tryxpath.functions.getNodeTypeStr
.. autofunction:: tryxpath.functions.getxpathResultStr
.. autofunction:: tryxpath.functions.getxpathResultNum
.. autofunction:: tryxpath.functions.isAttrItem
.. autofunction:: tryxpath.functions.isNodeItem
.. autofunction:: tryxpath.functions.isElementItem
.. autofunction:: tryxpath.functions.addClassToItem
.. autofunction:: tryxpath.functions.addClassToItems
.. autofunction:: tryxpath.functions.saveItemClass
.. autofunction:: tryxpath.functions.restoreItemClass
.. autofunction:: tryxpath.functions.saveItemClasses
.. autofunction:: tryxpath.functions.restoreItemClasses
.. autofunction:: tryxpath.functions.setAttrToItem
.. autofunction:: tryxpath.functions.removeAttrFromItem
.. autofunction:: tryxpath.functions.removeAttrFromItems
.. autofunction:: tryxpath.functions.setIndexToItems
.. autofunction:: tryxpath.functions.getParentElement
.. autofunction:: tryxpath.functions.getAncestorElements
.. autofunction:: tryxpath.functions.getOwnerDocument
.. autofunction:: tryxpath.functions.createHeaderRow
.. autofunction:: tryxpath.functions.createDetailTableHeader
.. autofunction:: tryxpath.functions.createDetailRow
.. autofunction:: tryxpath.functions.appendDetailRows
.. autofunction:: tryxpath.functions.updateDetailsTable
.. autofunction:: tryxpath.functions.emptyChildNodes
.. autofunction:: tryxpath.functions.saveAttrForItem
.. autofunction:: tryxpath.functions.saveAttrForItems
.. autofunction:: tryxpath.functions.restoreItemAttrs
.. autofunction:: tryxpath.functions.getFrameAncestry
.. autofunction:: tryxpath.functions.isNumberArray
.. autofunction:: tryxpath.functions.onError
.. autofunction:: tryxpath.functions.isBlankWindow
.. autofunction:: tryxpath.functions.collectBlankWindows
.. autofunction:: tryxpath.functions.findFrameElement
.. autofunction:: tryxpath.functions.findFrameIndex
.. autofunction:: tryxpath.functions.makeDetailText