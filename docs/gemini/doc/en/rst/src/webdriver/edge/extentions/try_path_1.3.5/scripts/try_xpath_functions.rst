try_xpath_functions.js
=======================

This JavaScript file defines functions for evaluating XPath expressions,
selecting elements using query selectors, and working with the results.
It provides methods for handling various XPath result types, obtaining
element details, and manipulating element attributes.

.. automodule:: try_xpath_functions
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: try_xpath_functions.execExpr
   :noindex:

   :param expr: (str): The XPath expression to evaluate.
   :param method: (str): The method to use for evaluation.  Valid options are `evaluate`, `querySelector`, and `querySelectorAll`.
   :param opts: (dict, optional): An object containing optional parameters.  Defaults to `{}`.
       :param context: (object, optional): The context for evaluation. Defaults to `document`.
       :param resolver: (function|dict|str, optional):  A resolver function or a string representing a JSON resolver. Defaults to `null`.
       :param resultType: (str|int, optional):  The desired XPath result type.  Defaults to `xpathResult.ANY_TYPE`.
       :param document: (object, optional): The Document object. Defaults to global `document`.
   :returns: (dict): A dictionary containing the result items, method used, and result type.
   :raises: Error:  Raised if the context is invalid.

.. autofunction:: try_xpath_functions.resToArr
   :noindex:

   :param res: (object): The XPath result object.
   :param type: (int, optional): The desired result type. Defaults to the result type from the `res` object.
   :returns: (list): A list of evaluated result items based on the provided type.
   :raises: Error: Raised if the result type is invalid.


.. autofunction:: try_xpath_functions.makeResolver
   :noindex:

   :param obj: (function|dict|str): A resolver function, JSON string, or dictionary.
   :returns: (function): A function to resolve the string parameter.
   :raises: Error:  Raised if the resolver is invalid.

.. autofunction:: try_xpath_functions.isValidDict
   :noindex:

   :param obj: (dict): The object to check.
   :returns: (bool): `True` if the object is a valid dictionary, otherwise `False`.

.. autofunction:: try_xpath_functions.objToMap
   :noindex:

   :param obj: (dict): The dictionary to convert.
   :returns: (Map): A Map object containing the dictionary's key-value pairs.


.. autofunction:: try_xpath_functions.isDocOrElem
   :noindex:

   :param obj: (object): The object to check.
   :returns: (bool): `True` if the object is a Document or Element object, otherwise `False`.

.. autofunction:: try_xpath_functions.listToArr
   :noindex:

   :param list: (list): The list to convert.
   :returns: (list): A copy of the input list.


.. autofunction:: try_xpath_functions.getItemDetail
   :noindex:

   :param item: (object): The item to get details from.
   :returns: (dict): A dictionary containing the item's details.
   :raises: TypeError:  Raised for unsupported item types (e.g., non-string/number/boolean/node).

.. autofunction:: try_xpath_functions.getItemDetails
   :noindex:

   :param items: (list): A list of items.
   :returns: (list): A list of dictionaries containing the details of each item.

.. autofunction:: try_xpath_functions.getNodeTypeStr
   :noindex:
   :param nodeType: (int): The node type.
   :returns: (str): The string representation of the node type.

.. autofunction:: try_xpath_functions.getxpathResultStr
   :noindex:

   :param resultType: (int): The XPath result type.
   :returns: (str): The string representation of the result type.

.. autofunction:: try_xpath_functions.getxpathResultNum
   :noindex:

   :param resultTypeStr: (str): The string representation of the XPath result type.
   :returns: (int): The integer representation of the result type, or `NaN` if the string is invalid.


.. autofunction:: try_xpath_functions.isAttrItem
   :noindex:

   :param item: (object): The item to check.
   :returns: (bool): `True` if the item is an Attr object, otherwise `False`.

.. autofunction:: try_xpath_functions.isNodeItem
   :noindex:

   :param item: (object): The item to check.
   :returns: (bool): `True` if the item is a Node object, otherwise `False`.


.. autofunction:: try_xpath_functions.isElementItem
   :noindex:

   :param item: (object): The item to check.
   :returns: (bool): `True` if the item is an Element object, otherwise `False`.

.. autofunction:: try_xpath_functions.addClassToItem
   :noindex:

   :param clas: (str): The class to add.
   :param item: (object): The element to add the class to.


.. autofunction:: try_xpath_functions.addClassToItems
   :noindex:

   :param clas: (str): The class to add.
   :param items: (list): A list of elements to add the class to.

.. autofunction:: try_xpath_functions.saveItemClass
   :noindex:

   :param item: (object): The element to save the class of.
   :returns: (dict): A dictionary containing the element and its original class.
   :raises TypeError: If the item is not an Element.


.. autofunction:: try_xpath_functions.restoreItemClass
   :noindex:

   :param savedClass: (dict): The saved class information.
   :raises TypeError: If the saved class is not a dictionary or the element is not an Element.


.. autofunction:: try_xpath_functions.saveItemClasses
   :noindex:

   :param items: (list): A list of elements to save the classes of.
   :returns: (list): A list of dictionaries containing the saved classes.


.. autofunction:: try_xpath_functions.restoreItemClasses
   :noindex:

   :param savedClasses: (list): The list of saved classes to restore.

.. autofunction:: try_xpath_functions.setAttrToItem
   :noindex:

   :param name: (str): The name of the attribute.
   :param value: (str): The value of the attribute.
   :param item: (object): The element to set the attribute on.

.. autofunction:: try_xpath_functions.removeAttrFromItem
   :noindex:

   :param name: (str): The name of the attribute to remove.
   :param item: (object): The element to remove the attribute from.

.. autofunction:: try_xpath_functions.removeAttrFromItems
   :noindex:

   :param name: (str): The name of the attribute to remove.
   :param items: (list): The list of elements to remove the attribute from.

.. autofunction:: try_xpath_functions.setIndexToItems
   :noindex:

   :param name: (str): The name of the attribute to set.
   :param items: (list): The list of elements to set the attribute on.

.. autofunction:: try_xpath_functions.getParentElement
   :noindex:
   :param item: (object): The element or attribute to get the parent from.
   :returns: (object | None): The parent element if found, otherwise `None`.


.. autofunction:: try_xpath_functions.getAncestorElements
   :noindex:
   :param elem: (object): The element to find the ancestors of.
   :returns: (list): A list of ancestor elements.


.. autofunction:: try_xpath_functions.getOwnerDocument
   :noindex:
   :param item: (object): The element or attribute to get the owner document from.
   :returns: (object | None): The owner document if found, otherwise `None`.


.. autofunction:: try_xpath_functions.createHeaderRow
   :noindex:
   :param values: (list): A list of header values.
   :param opts: (dict, optional): An object containing optional parameters. Defaults to `{}`.
       :param document: (object, optional): The document object. Defaults to `document`.
   :returns: (object): The created header row (`<tr>`).

.. autofunction:: try_xpath_functions.createDetailTableHeader
   :noindex:
   :param opts: (dict, optional): An object containing optional parameters. Defaults to `{}`.
       :param document: (object, optional): The document object. Defaults to `document`.
   :returns: (object): The created detail table header (`<tr>`).

.. autofunction:: try_xpath_functions.createDetailRow
   :noindex:
   :param index: (int): The row index.
   :param detail: (dict): The row details.
   :param opts: (dict, optional): An object containing optional parameters. Defaults to `{}`.
       :param document: (object, optional): The document object. Defaults to `document`.
       :param keys: (list, optional): A list of keys to include in the row. Defaults to `["type", "name", "value"]`.
   :returns: (object): The created detail row (`<tr>`).

.. autofunction:: try_xpath_functions.appendDetailRows
   :noindex:
   :param parent: (object): The parent element to append the rows to.
   :param details: (list): The list of details to append.
   :param opts: (dict, optional): An object containing optional parameters. Defaults to `{}`.
   :raises TypeError: If parent is not an element.

.. autofunction:: try_xpath_functions.updateDetailsTable
   :noindex:
   :param parent: (object): The parent element to update.
   :param details: (list): The details to display in the table.
   :param opts: (dict, optional): An object containing optional parameters. Defaults to `{}`.


.. autofunction:: try_xpath_functions.emptyChildNodes
   :noindex:

   :param elem: (object): The element to clear.

.. autofunction:: try_xpath_functions.saveAttrForItem
   :noindex:
   :param item: (object): The element to save the attribute of.
   :param attr: (str): The name of the attribute to save.
   :param storage: (Map): The storage to save the attributes to.
   :param overwrite: (bool): Whether to overwrite existing attribute values.
   :returns: (Map): The updated storage.
   :raises TypeError: If the item is not an Element.


.. autofunction:: try_xpath_functions.saveAttrForItems
   :noindex:
   :param items: (list): The elements to save attributes of.
   :param attr: (str): The name of the attribute.
   :param storage: (Map): The storage to save the attributes to.
   :param overwrite: (bool): Whether to overwrite existing attribute values.
   :returns: (Map): The updated storage.

.. autofunction:: try_xpath_functions.restoreItemAttrs
   :noindex:
   :param storage: (Map): The storage containing the attributes to restore.
   :raises TypeError: If the storage is not a Map.


.. autofunction:: try_xpath_functions.getFrameAncestry
   :noindex:
   :param inds: (list): A list of frame indices.
   :param win: (object, optional): The window object. Defaults to `window`.
   :returns: (list): A list of frame elements.
   :raises Error: Raised if a frame does not exist or access is denied.


.. autofunction:: try_xpath_functions.isNumberArray
   :noindex:
   :param arr: (list): The array to check.
   :returns: (bool): `True` if all elements in the array are numbers, otherwise `False`.


.. autofunction:: try_xpath_functions.onError
   :noindex:
   :param err: (object): The error object.

.. autofunction:: try_xpath_functions.isBlankWindow
   :noindex:
   :param win: (object): The window object to check.
   :returns: (bool): `True` if the window's location is "about:blank", otherwise `False`.


.. autofunction:: try_xpath_functions.collectBlankWindows
   :noindex:
   :param top: (object): The top-level window object.
   :returns: (list): A list of blank windows.


.. autofunction:: try_xpath_functions.findFrameElement
   :noindex:
   :param win: (object): The window object.
   :param parent: (object): The parent element.
   :returns: (object | None): The frame element if found, otherwise `None`.


.. autofunction:: try_xpath_functions.findFrameIndex
   :noindex:
   :param win: (object): The window object to find.
   :param parent: (object): The parent window.
   :returns: (int): The index of the window in the parent's frames array, or -1 if not found.


.. autofunction:: try_xpath_functions.makeDetailText
   :noindex:
   :param detail: (dict): The details to format.
   :param keys: (list): The keys to use for formatting.
   :param separator: (str, optional): The separator to use. Defaults to ", ".
   :param replacers: (dict, optional): A dictionary of replacer functions for specific keys. Defaults to an empty object.
   :returns: (str): The formatted text.