try_xpath_functions.js Documentation
===================================

This file contains JavaScript functions for performing XPath expressions,
querying elements using querySelector and querySelectorAll, and handling
various node and attribute manipulations.  It's part of the `try_path`
JavaScript library.


.. automodule:: hypotez.src.webdriver.firefox.extentions.try_path_1.3.5.scripts.try_xpath_functions
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: tryxpath.functions.execExpr
   :noindex:
   :param expr:
   :param method:
   :param opts:
   :returns:

.. autofunction:: tryxpath.functions.resToArr
   :noindex:
   :param res:
   :param type:
   :returns:

.. autofunction:: tryxpath.functions.makeResolver
   :noindex:
   :param obj:
   :returns:

.. autofunction:: tryxpath.functions.isValidDict
   :noindex:
   :param obj:
   :returns:

.. autofunction:: tryxpath.functions.objToMap
   :noindex:
   :param obj:
   :returns:

.. autofunction:: tryxpath.functions.isDocOrElem
   :noindex:
   :param obj:
   :returns:

.. autofunction:: tryxpath.functions.listToArr
   :noindex:
   :param list:
   :returns:

.. autofunction:: tryxpath.functions.getItemDetail
   :noindex:
   :param item:
   :returns:

.. autofunction:: tryxpath.functions.getItemDetails
   :noindex:
   :param items:
   :returns:

.. autofunction:: tryxpath.functions.getNodeTypeStr
   :noindex:
   :param nodeType:
   :returns:


.. autofunction:: tryxpath.functions.getxpathResultStr
   :noindex:
   :param resultType:
   :returns:


.. autofunction:: tryxpath.functions.getxpathResultNum
   :noindex:
   :param resultTypeStr:
   :returns:


.. autofunction:: tryxpath.functions.isAttrItem
   :noindex:
   :param item:
   :returns:


.. autofunction:: tryxpath.functions.isNodeItem
   :noindex:
   :param item:
   :returns:


.. autofunction:: tryxpath.functions.isElementItem
   :noindex:
   :param item:
   :returns:


.. autofunction:: tryxpath.functions.addClassToItem
   :noindex:
   :param clas:
   :param item:


.. autofunction:: tryxpath.functions.addClassToItems
   :noindex:
   :param clas:
   :param items:


.. autofunction:: tryxpath.functions.saveItemClass
   :noindex:
   :param item:
   :returns:


.. autofunction:: tryxpath.functions.restoreItemClass
   :noindex:
   :param savedClass:


.. autofunction:: tryxpath.functions.saveItemClasses
   :noindex:
   :param items:
   :returns:


.. autofunction:: tryxpath.functions.restoreItemClasses
   :noindex:
   :param savedClasses:


.. autofunction:: tryxpath.functions.setAttrToItem
   :noindex:
   :param name:
   :param value:
   :param item:


.. autofunction:: tryxpath.functions.removeAttrFromItem
   :noindex:
   :param name:
   :param item:

.. autofunction:: tryxpath.functions.removeAttrFromItems
   :noindex:
   :param name:
   :param items:


.. autofunction:: tryxpath.functions.setIndexToItems
   :noindex:
   :param name:
   :param items:


.. autofunction:: tryxpath.functions.getParentElement
   :noindex:
   :param item:
   :returns:

.. autofunction:: tryxpath.functions.getAncestorElements
   :noindex:
   :param elem:
   :returns:

.. autofunction:: tryxpath.functions.getOwnerDocument
   :noindex:
   :param item:
   :returns:

.. autofunction:: tryxpath.functions.createHeaderRow
   :noindex:
   :param values:
   :param opts:
   :returns:

.. autofunction:: tryxpath.functions.createDetailTableHeader
   :noindex:
   :param opts:
   :returns:

.. autofunction:: tryxpath.functions.createDetailRow
   :noindex:
   :param index:
   :param detail:
   :param opts:
   :returns:

.. autofunction:: tryxpath.functions.appendDetailRows
   :noindex:
   :param parent:
   :param details:
   :param opts:
   :returns:

.. autofunction:: tryxpath.functions.updateDetailsTable
   :noindex:
   :param parent:
   :param details:
   :param opts:
   :returns:


.. autofunction:: tryxpath.functions.emptyChildNodes
   :noindex:
   :param elem:


.. autofunction:: tryxpath.functions.saveAttrForItem
   :noindex:
   :param item:
   :param attr:
   :param storage:
   :param overwrite:
   :returns:


.. autofunction:: tryxpath.functions.saveAttrForItems
   :noindex:
   :param items:
   :param attr:
   :param storage:
   :param overwrite:
   :returns:


.. autofunction:: tryxpath.functions.restoreItemAttrs
   :noindex:
   :param storage:


.. autofunction:: tryxpath.functions.getFrameAncestry
   :noindex:
   :param inds:
   :param win:
   :returns:

.. autofunction:: tryxpath.functions.isNumberArray
   :noindex:
   :param arr:
   :returns:


.. autofunction:: tryxpath.functions.onError
   :noindex:
   :param err:


.. autofunction:: tryxpath.functions.isBlankWindow
   :noindex:
   :param win:
   :returns:

.. autofunction:: tryxpath.functions.collectBlankWindows
   :noindex:
   :param top:
   :returns:

.. autofunction:: tryxpath.functions.findFrameElement
   :noindex:
   :param win:
   :param parent:
   :returns:

.. autofunction:: tryxpath.functions.findFrameIndex
   :noindex:
   :param win:
   :param parent:
   :returns:


.. autofunction:: tryxpath.functions.makeDetailText
   :noindex:
   :param detail:
   :param keys:
   :param separator:
   :param replacers:
   :returns: