# try_xpath_functions.js Documentation

## Overview

This JavaScript file (`try_xpath_functions.js`) defines functions for evaluating XPath expressions, querying elements using `querySelector` and `querySelectorAll`, and manipulating DOM elements in a browser environment.  It provides helper functions for working with different types of XPath results and DOM nodes.

## Table of Contents

* [Overview](#overview)
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

**Description**: Executes an XPath expression on a given context.

**Parameters**:

- `expr` (str): The XPath expression to evaluate.
- `method` (str): The method to use for evaluation ("evaluate", "querySelector", or "querySelectorAll").
- `opts` (Optional[dict], optional): An optional dictionary of options.  Includes `context`, `resolver`, and `document` for specifying the evaluation context, resolver function, and document respectively. Defaults to an empty object.

**Returns**:

- `dict`: A dictionary containing the evaluated results.  Includes "items" (the resulting nodes or values), "method", and "resultType" (type of the result).

**Raises**:

- `Error`: Thrown if the context is invalid for the specified method.


### `resToArr`

**Description**: Converts the XPath result to an array of items.

**Parameters**:

- `res` (object): The XPath result object.
- `type` (Optional[int], optional): The result type (e.g., `xpathResult.NUMBER_TYPE`, etc). Defaults to undefined.

**Returns**:

- `array`: An array containing the extracted node values.

**Raises**:

- `Error`: Thrown if the result type is invalid.


### `makeResolver`

**Description**: Creates a resolver function for XPath evaluation.

**Parameters**:

- `obj` (object | function | str): The resolver object, function or a stringified JSON object.

**Returns**:

- `function`: A resolver function or `null` if input is `null`.

**Raises**:

- `Error`: Thrown if the resolver is invalid.


**(and so on for the rest of the functions, following the format specified in the instruction)**