# Модуль try_xpath_functions.js

## Обзор

Этот модуль предоставляет функции для работы с XPath, querySelector и querySelectorAll в JavaScript. Он позволяет выполнять запросы XPath, получать результаты в различных форматах (узлы, числа, строки и т.д.), обрабатывать исключения и предоставлять дополнительные утилиты для работы с DOM-элементами.

## Оглавление

* [Функции](#функции)
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

## Функции

### `execExpr`

**Описание**: Выполняет XPath, querySelector или querySelectorAll запрос.

**Параметры**:
- `expr` (str): XPath выражение или CSS селектор.
- `method` (str): Тип запроса ("evaluate", "querySelector", "querySelectorAll").
- `opts` (dict, optional): Опции.  Может содержать:
    - `context` (Node | Document): Контекст для выполнения запроса. По умолчанию `document`.
    - `resolver` (function | str | dict, optional): Функция-разрешитель или строка с JSON-представлением словаря для разрешения атрибутов в XPath. По умолчанию `null`.
    - `resultType` (int, optional): Тип результата XPath запроса. По умолчанию `xpathResult.ANY_TYPE`.
    - `document` (Document, optional): Документ для выполнения запроса.

**Возвращает**:
- `dict`: Словарь с результатами:
    - `items` (list): Список результатов запроса.
    - `method` (str): Использованный метод.
    - `resultType` (int | None): Тип результата.

**Вызывает исключения**:
- `Error`: Возникает при некорректном контексте для методов `evaluate`, `querySelector`, `querySelectorAll`.
- `Error`: Возникает при невалидном формате `resolver` (строка не может быть обработана).


### `resToArr`
... (Описание других функций аналогично)
```