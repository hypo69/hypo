# Модуль `try_xpath_functions`

## Обзор

Данный модуль предоставляет функции для выполнения XPath выражений, поиска элементов с помощью CSS селекторов и работы с полученными результатами. Он предназначен для работы с DOM (Document Object Model) и позволяет извлекать информацию из веб-страниц.

## Оглавление

- [Модуль `try_xpath_functions`](#модуль-try_xpath_functions)
- [Обзор](#обзор)
- [Функции](#функции)
    - [`execExpr`](#execexpr)
    - [`resToArr`](#resToArr)
    - [`makeResolver`](#makeresolver)
    - [`isValidDict`](#isvaliddict)
    - [`objToMap`](#objtomap)
    - [`isDocOrElem`](#isdocorelem)
    - [`listToArr`](#listtoarr)
    - [`getItemDetail`](#getitemdetail)
    - [`getItemDetails`](#getitemdetails)
    - [`getNodeTypeStr`](#getnodetypestr)
    - [`getxpathResultStr`](#getxpathresultstr)
    - [`getxpathResultNum`](#getxpathresultnum)
    - [`isAttrItem`](#isattritem)
    - [`isNodeItem`](#isnodeitem)
    - [`isElementItem`](#iselementitem)
    - [`addClassToItem`](#addclasstoitem)
    - [`addClassToItems`](#addclasstoitems)
    - [`saveItemClass`](#saveitemclass)
    - [`restoreItemClass`](#restoreitemclass)
    - [`saveItemClasses`](#saveitemclasses)
    - [`restoreItemClasses`](#restoreitemclasses)
    - [`setAttrToItem`](#setattrtoitem)
    - [`removeAttrFromItem`](#removeattrfromitem)
    - [`removeAttrFromItems`](#removeattrfromitems)
    - [`setIndexToItems`](#setindextoitems)
    - [`getParentElement`](#getparentelement)
    - [`getAncestorElements`](#getancestorlements)
    - [`getOwnerDocument`](#getownerdocument)
    - [`createHeaderRow`](#createheaderrow)
    - [`createDetailTableHeader`](#createdetailtableheader)
    - [`createDetailRow`](#createdetailrow)
    - [`appendDetailRows`](#appenddetailrows)
    - [`updateDetailsTable`](#updatedetailstable)
    - [`emptyChildNodes`](#emptychildnodes)
    - [`saveAttrForItem`](#saveattrforitem)
    - [`saveAttrForItems`](#saveattrforitems)
    - [`restoreItemAttrs`](#restoreitemattrs)
    - [`getFrameAncestry`](#getframeancestry)
    - [`isNumberArray`](#isnumberarray)
    - [`onError`](#onerror)
    - [`isBlankWindow`](#isblankwindow)
    - [`collectBlankWindows`](#collectblankwindows)
    - [`findFrameElement`](#findframeelement)
    - [`findFrameIndex`](#findframeindex)
    - [`makeDetailText`](#makedetailtext)


## Функции

### `execExpr`

**Описание**: Выполняет XPath выражение или CSS селектор на заданном контексте.

**Параметры**:
- `expr` (str): XPath выражение или CSS селектор.
- `method` (str): Метод выполнения. Может быть "evaluate", "querySelector" или "querySelectorAll".
- `opts` (Optional[dict], optional): Опции выполнения.
    - `context` (object): Контекст для выполнения выражения (например, `document`, `element`).
    - `resolver` (Optional[function | string]): Функция или строковое представление JSON для разрешения параметров.
    - `document` (object): Документ для использования в случае, если контекст не является документом.


**Возвращает**:
- `dict`: Словарь с результатами выполнения.
    - `items` (list): Список найденных элементов или значений.
    - `method` (str): Используемый метод выполнения.
    - `resultType` (Optional[number]): Тип результата.


**Вызывает исключения**:
- `Error`: Возникает при некорректном контексте или XPath выражении.


### `resToArr`

**Описание**: Преобразует результат выполнения XPath выражения в массив.

**Параметры**:
- `res` (object): Результат выполнения XPath.
- `type` (number): Тип результата.


**Возвращает**:
- `list`: Массив результатов.

**Вызывает исключения**:
- `Error`: Возникает при некорректном типе результата.


### `makeResolver`

**Описание**: Создает функцию-разрешитель для параметров XPath.

**Параметры**:
- `obj` (Optional[function | string | dict]): Функция или JSON-представление объекта для разрешения параметров.


**Возвращает**:
- `function | None`: Функция-разрешитель или `None`.


**Вызывает исключения**:
- `Error`: Возникает при некорректном формате объекта разрешения.


... (Остальные функции аналогичным образом документированы)