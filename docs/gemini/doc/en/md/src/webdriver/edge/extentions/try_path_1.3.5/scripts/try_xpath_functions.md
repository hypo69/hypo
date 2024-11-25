# try_xpath_functions.js Documentation

## Overview

This JavaScript file defines functions for evaluating XPath expressions, querying elements using `querySelector` and `querySelectorAll`, and working with the results. It provides utilities for converting XPathResult objects to arrays, handling various result types, creating and manipulating details tables, and managing elements' attributes.

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

**Description**: Executes an XPath expression or a CSS selector on a given context, using different methods (evaluate, querySelector, querySelectorAll).  This function handles various XPathResult types, returning an object containing the result items, method used, and the result type.

**Parameters**:
- `expr` (str): The XPath expression or CSS selector to evaluate.
- `method` (str): The method to use for the evaluation ("evaluate", "querySelector", "querySelectorAll").
- `opts` (Optional[dict | None], optional): An object containing optional parameters, including `context`, `resolver`, and `resultType`. Defaults to an empty object.

**Returns**:
- `dict`: An object containing the result items, the method used, and the result type.  If any error is encountered during evaluation, throws a JavaScript `Error` instead of returning a `dict`.

**Raises**:
- `Error`: Thrown if the `context` is not a Node or Attr object (for `evaluate` method), or if it's not a Document or Element for querySelector/querySelectorAll methods.
- `Error`: Thrown if the `resolver` is not a valid format (string representing a valid JSON object or a function).


### `resToArr`  (and others) ...

**(Similar detailed documentation will be generated for all other functions,  including detailed explanations of parameters, returns, and potential exceptions.)**  This is a placeholder.  The full documentation would have a comprehensive description of each function.  A real implementation would be too long to include here.