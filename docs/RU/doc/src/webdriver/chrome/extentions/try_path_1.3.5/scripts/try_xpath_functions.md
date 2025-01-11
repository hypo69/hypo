# Модуль `try_xpath_functions`

## Обзор

Этот модуль содержит функции для работы с XPath и CSS-селекторами в JavaScript.  Он предоставляет методы для оценки XPath выражений, выбора элементов по CSS-селекторам, обработки результатов запросов и работы с атрибутами элементов.

## Оглавление

- [Модуль try_xpath_functions](#модуль-try_xpath_functions)
- [Обзор](#обзор)
- [Функции](#функции)
    - [`execExpr`](#execExpr)
    - [`resToArr`](#resToArr)
    - [`makeResolver`](#makeResolver)
    - [`isValidDict`](#isValidDict)
    - [`objToMap`](#objToMap)
    - [`isDocOrElem`](#isDocOrElem)
    - [`listToArr`](#listToArr)
    - [`getItemDetail`](#getItemDetail)
    - [`getItemDetails`](#getItemDetails)
    - [`getNodeTypeStr`](#getNodeTypeStr)
    - [`getxpathResultStr`](#getxpathResultStr)
    - [`getxpathResultNum`](#getxpathResultNum)
    - [`isAttrItem`](#isAttrItem)
    - [`isNodeItem`](#isNodeItem)
    - [`isElementItem`](#isElementItem)
    - [`addClassToItem`](#addClassToItem)
    - [`addClassToItems`](#addClassToItems)
    - [`saveItemClass`](#saveItemClass)
    - [`restoreItemClass`](#restoreItemClass)
    - [`saveItemClasses`](#saveItemClasses)
    - [`restoreItemClasses`](#restoreItemClasses)
    - [`setAttrToItem`](#setAttrToItem)
    - [`removeAttrFromItem`](#removeAttrFromItem)
    - [`removeAttrFromItems`](#removeAttrFromItems)
    - [`setIndexToItems`](#setIndexToItems)
    - [`getParentElement`](#getParentElement)
    - [`getAncestorElements`](#getAncestorElements)
    - [`getOwnerDocument`](#getOwnerDocument)
    - [`createHeaderRow`](#createHeaderRow)
    - [`createDetailTableHeader`](#createDetailTableHeader)
    - [`createDetailRow`](#createDetailRow)
    - [`appendDetailRows`](#appendDetailRows)
    - [`updateDetailsTable`](#updateDetailsTable)
    - [`emptyChildNodes`](#emptyChildNodes)
    - [`saveAttrForItem`](#saveAttrForItem)
    - [`saveAttrForItems`](#saveAttrForItems)
    - [`restoreItemAttrs`](#restoreItemAttrs)
    - [`getFrameAncestry`](#getFrameAncestry)
    - [`isNumberArray`](#isNumberArray)
    - [`onError`](#onError)
    - [`isBlankWindow`](#isBlankWindow)
    - [`collectBlankWindows`](#collectBlankWindows)
    - [`findFrameElement`](#findFrameElement)
    - [`findFrameIndex`](#findFrameIndex)
    - [`makeDetailText`](#makeDetailText)

## Функции

### `execExpr`

**Описание**: Выполняет XPath или CSS-выражение на заданном контексте.

**Параметры**:
- `expr` (str): XPath или CSS-выражение для выполнения.
- `method` (str): Тип выполнения ("evaluate", "querySelector", "querySelectorAll").
- `opts` (dict, optional): Опции для выполнения.
    - `context` (Node, optional): Контекст для выполнения выражения (по умолчанию `document`).
    - `resolver` (function|str|dict, optional): Резолвер для XPath выражений. Может быть функцией, строкой JSON или объектом.
    - `resultType` (int, optional): Тип результата.

**Возвращает**:
- dict: Результат выполнения с полями `items`, `method` и `resultType`. `items` содержит список результата, `method` - использованный метод выполнения, `resultType` - тип результата XPath. Возвращает `None` при ошибке.

**Вызывает исключения**:
- `Error`: Возникает при неверном контексте.


### `resToArr`
(и другие функции)

... (Здесь необходимо добавить документацию для остальных функций, следуя указанному формату.)