# try_xpath_functions.js Documentation

## Overview

This JavaScript file defines functions for interacting with the DOM using XPath expressions and other selection methods.  It provides tools for evaluating XPath expressions, querying elements using `querySelector` and `querySelectorAll`, and managing retrieved results.  The file also includes functions for handling different data types returned by XPath queries (e.g., nodes, numbers, strings).  Additionally, utility methods for working with HTML elements and attributes are included.


## Table of Contents

* [Functions](#functions)
    * [`execExpr`](#execExpr)
    * [`resToArr`](#resToArr)
    * [`makeResolver`](#makeResolver)
    * [`isValidDict`](#isValidDict)
    * [`objToMap`](#objToMap)
    * [`isDocOrElem`](#isDocOrElem)
    * [`listToArr`](#listToArr)
    * [`getItemDetail`](#getItemDetail)
    * [`getItemDetails`](#getItemDetails)
    * [`getNodeTypeStr`](#getNodeTypeStr)
    * [`getxpathResultStr`](#getxpathResultStr)
    * [`getxpathResultNum`](#getxpathResultNum)
    * [`isAttrItem`](#isAttrItem)
    * [`isNodeItem`](#isNodeItem)
    * [`isElementItem`](#isElementItem)
    * [`addClassToItem`](#addClassToItem)
    * [`addClassToItems`](#addClassToItems)
    * [`saveItemClass`](#saveItemClass)
    * [`restoreItemClass`](#restoreItemClass)
    * [`saveItemClasses`](#saveItemClasses)
    * [`restoreItemClasses`](#restoreItemClasses)
    * [`setAttrToItem`](#setAttrToItem)
    * [`removeAttrFromItem`](#removeAttrFromItem)
    * [`removeAttrFromItems`](#removeAttrFromItems)
    * [`setIndexToItems`](#setIndexToItems)
    * [`getParentElement`](#getParentElement)
    * [`getAncestorElements`](#getAncestorElements)
    * [`getOwnerDocument`](#getOwnerDocument)
    * [`createHeaderRow`](#createHeaderRow)
    * [`createDetailTableHeader`](#createDetailTableHeader)
    * [`createDetailRow`](#createDetailRow)
    * [`appendDetailRows`](#appendDetailRows)
    * [`updateDetailsTable`](#updateDetailsTable)
    * [`emptyChildNodes`](#emptyChildNodes)
    * [`saveAttrForItem`](#saveAttrForItem)
    * [`saveAttrForItems`](#saveAttrForItems)
    * [`restoreItemAttrs`](#restoreItemAttrs)
    * [`getFrameAncestry`](#getFrameAncestry)
    * [`isNumberArray`](#isNumberArray)
    * [`onError`](#onError)
    * [`isBlankWindow`](#isBlankWindow)
    * [`collectBlankWindows`](#collectBlankWindows)
    * [`findFrameElement`](#findFrameElement)
    * [`findFrameIndex`](#findFrameIndex)
    * [`makeDetailText`](#makeDetailText)


## Functions

### `execExpr`

**Description**: Executes an XPath expression or a CSS selector on a given context.

**Parameters**:
- `expr` (str): The XPath expression or CSS selector to evaluate.
- `method` (str): The method to use for evaluation ("evaluate", "querySelector", "querySelectorAll").
- `opts` (Optional[dict], optional): An optional dictionary containing additional options:
    - `context` (object, optional): The context node for evaluation. Defaults to the `document` object.
    - `resolver` (function|str|dict, optional): A resolver function or stringified JSON object for evaluating variables within the XPath expression.
    - `document` (object, optional): Override the document context.
    - `resultType` (int, optional): Type of the result to return (e.g., `xpathResult.ANY_TYPE`).

**Returns**:
- `dict`: A dictionary containing the results of the evaluation:
    - `items` (array): An array of items that are evaluated.
    - `method` (str): The method that was used for evaluation.
    - `resultType` (int): The result type returned by the expression.


**Raises**:
- `Error`: Thrown if the `context` is not a valid node or attribute.


### `resToArr`

**(Other function descriptions will follow the same format as above, documenting each function with its parameters, returns, and exceptions.)**

... (rest of the function documentation)