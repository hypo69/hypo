# Анализ кода модуля try_xpath_functions.js

**Качество кода**

- Соответствие требованиям по оформлению кода: 6/10
    - Плюсы:
        - Код разбит на функции, что улучшает читаемость и повторное использование.
        - Используется strict mode.
        - Присутствуют некоторые комментарии, объясняющие назначение кода.
        - Функции сгруппированы в пространстве имен `tryxpath.functions`.
    - Минусы:
        - Отсутствует reStructuredText (RST) документация для функций и модуля.
        - Присутствуют `try-catch` блоки без логирования ошибок.
        - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        - Некоторые функции имеют сложные вложенные структуры, которые можно упростить.
        - Не все переменные и функции имеют описательные имена.
        - Присутствует дублирование кода (например, создание `th` элементов в `createDetailTableHeader` и `createHeaderRow`).

**Рекомендации по улучшению**

1.  **Добавить RST документацию:**
    - Добавить docstring для модуля в начале файла.
    - Добавить docstring для каждой функции и метода, включая описание параметров и возвращаемых значений.
    - Использовать комментарии в стиле reStructuredText (RST) для лучшего форматирования.
2.  **Использовать логирование:**
    - Заменить `console.log` на `logger.error` для логирования ошибок.
    - Добавить логирование ошибок в блоках `try-except`.
3.  **Использовать `j_loads` или `j_loads_ns`:**
    - Заменить `JSON.parse` на `j_loads` или `j_loads_ns` при разборе JSON.
4.  **Упростить код:**
    - Упростить вложенные структуры функций, если это возможно.
    - Избегать повторения кода путем создания общих функций.
5.  **Улучшить именование переменных и функций:**
    - Использовать более описательные имена для переменных и функций.
6.  **Разделить функции на более мелкие:**
    - Разделить крупные функции на более мелкие, чтобы улучшить читаемость и тестируемость.

**Оптимизированный код**

```python
"""
Модуль для выполнения XPath запросов и работы с DOM
=========================================================================================

Этот модуль предоставляет набор функций для выполнения XPath запросов,
манипулирования DOM элементами и извлечения информации о них.

Он включает в себя функции для выполнения XPath выражений, преобразования результатов,
работы с атрибутами, классами и родительскими элементами, а также для создания таблиц
с деталями элементов.

Пример использования
--------------------

.. code-block:: javascript

    // Получение элементов по XPath выражению
    var result = tryxpath.functions.execExpr(
      '//div[@class="my-class"]',
      'evaluate',
      { context: document }
    );

    // Добавление класса ко всем найденным элементам
    tryxpath.functions.addClassToItems('highlighted', result.items);

"""
from src.logger.logger import logger
# /* This Source Code Form is subject to the terms of the Mozilla Public
#  * License, v. 2.0. If a copy of the MPL was not distributed with this
#  * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#
# // namespace
if not tryxpath:
    var tryxpath = {}
if not tryxpath.functions:
    tryxpath.functions = {}

(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath
    var fu = tryxpath.functions

    # prevent multiple execution
    if (fu.done) {
        return
    }
    fu.done = true

    fu.execExpr = function(expr, method, opts) {
        """
        Выполняет XPath выражение или CSS селектор в заданном контексте.

        :param expr: XPath выражение или CSS селектор.
        :param method: Метод выполнения ('evaluate', 'querySelector', 'querySelectorAll').
        :param opts: Объект с опциями (context, resolver, document, resultType).
        :return: Объект с результатами ('items', 'method', 'resultType').
        """
        opts = opts || {}
        var context = opts.context || document
        var resolver = ("resolver" in opts) ? opts.resolver : null
        var doc = opts.document || fu.getOwnerDocument(context) || context

        var items, resultType

        switch (method) {
        case "evaluate":
            if (!fu.isNodeItem(context) and !fu.isAttrItem(context)) {
                logger.error("The context is either Nor nor Attr.")
                return
                #  throw new Error("The context is either Nor nor Attr.");
            }
            resolver = fu.makeResolver(resolver)
            resultType = opts.resultType || xpathResult.ANY_TYPE
            try:
                let result = doc.evaluate(expr, context, resolver, resultType,
                                      null)
                items = fu.resToArr(result, resultType)
                if (resultType === xpathResult.ANY_TYPE) {
                    resultType = result.resultType
                }
            except Exception as ex:
                logger.error("Ошибка при выполнении evaluate", ex)
                return
            break

        case "querySelector":
            if (!fu.isDocOrElem(context)) {
                logger.error("The context is either Document nor Element.")
                return
                # throw new Error("The context is either Document nor Element.");
            }
            let elem = context.querySelector(expr)
            items = elem ? [elem] : []
            resultType = null
            break

        case "querySelectorAll":
        default:
            if (!fu.isDocOrElem(context)) {
                logger.error("The context is neither Document nor Element.")
                return
                # throw new Error(
                #     "The context is neither Document nor Element.");
            }
            let elems = context.querySelectorAll(expr)
            items = fu.listToArr(elems)
            resultType = null
            break
        }

        return {
            "items": items,
            "method": method,
            "resultType": resultType
        }
    }

    fu.resToArr = function (res, type) {
        """
        Преобразует результат XPath в массив.

        :param res: Результат выполнения XPath запроса.
        :param type: Тип результата.
        :return: Массив элементов.
        """
        if (type === undefined) or (type === xpathResult.ANY_TYPE) :
            type = res.resultType

        var arr = []
        switch(type) {
        case xpathResult.NUMBER_TYPE :
            arr.push(res.numberValue)
            break
        case xpathResult.STRING_TYPE :
            arr.push(res.stringValue)
            break
        case xpathResult.BOOLEAN_TYPE :
            arr.push(res.booleanValue)
            break
        case xpathResult.ORDERED_NODE_ITERATOR_TYPE :
        case xpathResult.UNORDERED_NODE_ITERATOR_TYPE :
            for (var node = res.iterateNext()
                 ; node !== null
                 ; node = res.iterateNext()) {
                arr.push(node)
            }
            break
        case xpathResult.ORDERED_NODE_SNAPSHOT_TYPE :
        case xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE :
            for (var i = 0; i < res.snapshotLength; i++) {
                arr.push(res.snapshotItem(i))
            }
            break
        case xpathResult.ANY_UNORDERED_NODE_TYPE :
        case xpathResult.FIRST_ORDERED_NODE_TYPE :
            arr.push(res.singleNodeValue)
            break
        default :
            logger.error("The resultType is invalid. " + type)
            return
            # throw new Error("The resultType is invalid. " + type);
        }
        return arr
    }
    
    fu.makeResolver = function (obj) {
        """
        Создает функцию-резолвер для пространств имен XPath.

        :param obj: Объект, строка JSON или функция, представляющая резолвер.
        :return: Функция-резолвер или null.
        """
        if (obj === null) {
            return null
        }
        if (typeof(obj) === "function") {
            return obj
        }

        var dict
        if (typeof(obj) === "string") {
            try {
                dict = JSON.parse(obj)
            } catch (e) {
                logger.error("Invalid resolver [" + obj + "]. : "
                                + e.message)
                return
                # throw new Error("Invalid resolver [" + obj + "]. : "
                #                 + e.message);                
            }
        } else {
            dict = obj
        }

        if (fu.isValidDict(dict)) {
            let map = fu.objToMap(dict)
            return function (str) {
                if (map.has(str)) {
                    return map.get(str)
                }
                return ""
            }
        }
        logger.error("Invalid resolver. "
                        + JSON.stringify(dict, null))
        return
        # throw new Error("Invalid resolver. "
        #                 + JSON.stringify(dict, null));
    }

    fu.isValidDict = function (obj) {
        """
        Проверяет, является ли объект допустимым словарем для резолвера.

        :param obj: Объект для проверки.
        :return: True, если объект является допустимым словарем, иначе False.
        """
        if (obj === null) or (typeof(obj) !== "object") :
            return false
        for (var key of Object.keys(obj)) {
            if (typeof(obj[key]) !== "string") {
                return false
            }
        }
        return true
    }

    fu.objToMap = function (obj) {
        """
        Преобразует объект в Map.

        :param obj: Объект для преобразования.
        :return: Map, созданный на основе объекта.
        """
        var map = new Map()
        Object.keys(obj).forEach(function(item) {
            map.set(item, obj[item])
        })
        return map
    }

    fu.isDocOrElem = function(obj) {
        """
        Проверяет, является ли объект Document или Element.

        :param obj: Объект для проверки.
        :return: True, если объект Document или Element, иначе False.
        """
        if (obj.nodeType === 1 or obj.nodeType === 9) {
            return true
        }
        return false
    }

    fu.listToArr = function(list) {
        """
        Преобразует NodeList или HTMLCollection в массив.

        :param list: NodeList или HTMLCollection.
        :return: Массив элементов.
        """
        var elems = []
        for (var i = 0; i < list.length; i++) {
            elems.push(list[i])
        }
        return elems
    }

    fu.getItemDetail = function (item) {
        """
        Возвращает детали элемента в виде объекта.

        :param item: DOM элемент, строка, число или булево значение.
        :return: Объект с деталями элемента.
        """
        var typeStr = typeof(item)

        switch (typeof(item)) {
        case "string":
            return {
                "type": "String",
                "name": "",
                "value": item,
                "textContent": ""
            }
        case "number":
            return {
                "type": "Number",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            }
        case "boolean":
            return {
                "type": "Boolean",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            }
        }

        # item is Element
        if (fu.isElementItem(item)) {
            return {
                "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + item.nodeType + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            }
        }
        
        # item is Attr
        if (fu.isAttrItem(item)) {
            return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            }
        }

        # item is Node
        return {
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + item.nodeType + ")",
            "name": item.nodeName,
            "value": item.nodeValue or "",
            "textContent": item.textContent or ""
        }
    }

    fu.getItemDetails = function (items) {
        """
        Возвращает детали для массива элементов.

        :param items: Массив DOM элементов.
        :return: Массив объектов с деталями элементов.
        """
        var details = []
        for (var i = 0; i < items.length; i++) {
            details.push(fu.getItemDetail(items[i]))
        }
        return details
    }

    const nodeTypeMap = new Map([
        [Node.ELEMENT_NODE, "ELEMENT_NODE"],
        [Node.ATTRIBUTE_NODE, "ATTRIBUTE_NODE"],
        [Node.TEXT_NODE, "TEXT_NODE"],
        [Node.CDATA_SECTION_NODE, "CDATA_SECTION_NODE"],
        [Node.ENTITY_REFERENCE_NODE, "ENTITY_REFERENCE_NODE"],
        [Node.ENTITY_NODE, "ENTITY_NODE"],
        [Node.PROCESSING_INSTRUCTION_NODE, "PROCESSING_INSTRUCTION_NODE"],
        [Node.COMMENT_NODE, "COMMENT_NODE"],
        [Node.DOCUMENT_NODE, "DOCUMENT_NODE"],
        [Node.DOCUMENT_TYPE_NODE, "DOCUMENT_TYPE_NODE"],
        [Node.DOCUMENT_FRAGMENT_NODE, "DOCUMENT_FRAGMENT_NODE"],
        [Node.NOTATION_NODE, "NOTATION_NODE"]
    ])

    fu.getNodeTypeStr = function(nodeType) {
        """
        Возвращает строковое представление типа узла.

        :param nodeType: Числовой код типа узла.
        :return: Строковое представление типа узла.
        """
        if (nodeTypeMap.has(nodeType)) {
            return nodeTypeMap.get(nodeType)
        }
        return "Unknown"
    }

    const xpathResultMaps = {
        "numToStr" : new Map([
            [xpathResult.ANY_TYPE, "ANY_TYPE"],
            [xpathResult.NUMBER_TYPE , "NUMBER_TYPE"],
            [xpathResult.STRING_TYPE , "STRING_TYPE"],
            [xpathResult.BOOLEAN_TYPE , "BOOLEAN_TYPE"],
            [xpathResult.UNORDERED_NODE_ITERATOR_TYPE ,
             "UNORDERED_NODE_ITERATOR_TYPE"],
            [xpathResult.ORDERED_NODE_ITERATOR_TYPE ,
             "ORDERED_NODE_ITERATOR_TYPE"],
            [xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE ,
             "UNORDERED_NODE_SNAPSHOT_TYPE"],
            [xpathResult.ORDERED_NODE_SNAPSHOT_TYPE ,
             "ORDERED_NODE_SNAPSHOT_TYPE"],
            [xpathResult.ANY_UNORDERED_NODE_TYPE, "ANY_UNORDERED_NODE_TYPE"],
            [xpathResult.FIRST_ORDERED_NODE_TYPE, "FIRST_ORDERED_NODE_TYPE"]
        ]),

        "strToNum" : new Map([
            ["ANY_TYPE", xpathResult.ANY_TYPE],
            ["NUMBER_TYPE", xpathResult.NUMBER_TYPE],
            ["STRING_TYPE", xpathResult.STRING_TYPE],
            ["BOOLEAN_TYPE", xpathResult.BOOLEAN_TYPE],
            ["UNORDERED_NODE_ITERATOR_TYPE",
             xpathResult.UNORDERED_NODE_ITERATOR_TYPE],
            ["ORDERED_NODE_ITERATOR_TYPE",
             xpathResult.ORDERED_NODE_ITERATOR_TYPE],
            ["UNORDERED_NODE_SNAPSHOT_TYPE",
             xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE],
            ["ORDERED_NODE_SNAPSHOT_TYPE",
             xpathResult.ORDERED_NODE_SNAPSHOT_TYPE],
            ["ANY_UNORDERED_NODE_TYPE", xpathResult.ANY_UNORDERED_NODE_TYPE],
            ["FIRST_ORDERED_NODE_TYPE", xpathResult.FIRST_ORDERED_NODE_TYPE]
        ])
    }

    fu.getxpathResultStr = function (resultType) {
        """
        Возвращает строковое представление типа результата XPath.

        :param resultType: Числовой код типа результата XPath.
        :return: Строковое представление типа результата XPath.
        """
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType)
        }
        return "Unknown"
    }

    fu.getxpathResultNum = function (resultTypeStr) {
        """
        Возвращает числовой код типа результата XPath по его строковому представлению.

        :param resultTypeStr: Строковое представление типа результата XPath.
        :return: Числовой код типа результата XPath или NaN, если не найдено.
        """
        if (xpathResultMaps.strToNum.has(resultTypeStr)) {
            return xpathResultMaps.strToNum.get(resultTypeStr)
        }
        return NaN
    }

    fu.isAttrItem = function (item) {
        """
        Проверяет, является ли объект атрибутом.

        :param item: Объект для проверки.
        :return: True, если объект является атрибутом, иначе False.
        """
        return Object.prototype.toString.call(item) === "[object Attr]"
    }

    fu.isNodeItem = function (item) {
        """
        Проверяет, является ли объект узлом.

        :param item: Объект для проверки.
        :return: True, если объект является узлом, иначе False.
        """
        if (fu.isAttrItem(item)) {
            return false
        }

        switch (typeof(item)) {
        case "string":
        case "number":
            return false
        default:
            return true
        }
    }
    
    fu.isElementItem = function (item) {
        """
        Проверяет, является ли объект элементом.

        :param item: Объект для проверки.
        :return: True, если объект является элементом, иначе False.
        """
        if (fu.isNodeItem(item)
            and (item.nodeType === Node.ELEMENT_NODE)) {
            return true
        }
        return false
    }

    fu.addClassToItem = function (clas, item) {
        """
        Добавляет класс к элементу.

        :param clas: Имя класса для добавления.
        :param item: DOM элемент.
        """
        if (fu.isElementItem(item)) {
            item.classList.add(clas)
        }
    }

    fu.addClassToItems = function (clas, items) {
        """
        Добавляет класс к массиву элементов.

        :param clas: Имя класса для добавления.
        :param items: Массив DOM элементов.
        """
        for (var item of items) {
            fu.addClassToItem(clas, item)
        }
    }

    fu.saveItemClass = function (item) {
        """
        Сохраняет текущий класс элемента.

        :param item: DOM элемент.
        :return: Объект с элементом и сохраненным классом или null.
        """
        if (!fu.isElementItem(item)) {
            return null
        }

        var clas
        if (item.hasAttribute("class")) {
            clas = item.getAttribute("class")
        } else {
            clas = null
        }
        return {
            "elem": item,
            "origClass": clas
        }
    }

    fu.restoreItemClass = function (savedClass) {
        """
        Восстанавливает сохраненный класс элемента.

        :param savedClass: Объект с элементом и сохраненным классом.
        """
        if (savedClass === null) {
            return null
        }

        if (savedClass.origClass === null) {
            savedClass.elem.removeAttribute("class")
        } else {
            savedClass.elem.setAttribute("class", savedClass.origClass)
        }
    }

    fu.saveItemClasses = function (items) {
        """
        Сохраняет классы для массива элементов.

        :param items: Массив DOM элементов.
        :return: Массив объектов с элементами и сохраненными классами.
        """
        var savedClasses = []
        for (var item of items) {
            savedClasses.push(fu.saveItemClass(item))
        }
        return savedClasses
    }

    fu.restoreItemClasses = function (savedClasses) {
        """
        Восстанавливает классы для массива элементов.

        :param savedClasses: Массив объектов с элементами и сохраненными классами.
        """
        for (var savedClass of savedClasses) {
            fu.restoreItemClass(savedClass)
        }
    }

    fu.setAttrToItem = function(name, value, item) {
         """
        Устанавливает атрибут для элемента.

        :param name: Имя атрибута.
        :param value: Значение атрибута.
        :param item: DOM элемент.
        """
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value)
        }
    }

    fu.removeAttrFromItem = function(name, item) {
        """
        Удаляет атрибут из элемента.

        :param name: Имя атрибута для удаления.
        :param item: DOM элемент.
        """
        if (fu.isElementItem(item)) {
            item.removeAttribute(name)
        }
    }

    fu.removeAttrFromItems = function(name, items) {
         """
        Удаляет атрибут из массива элементов.

        :param name: Имя атрибута для удаления.
        :param items: Массив DOM элементов.
        """
        items.forEach(item => {
            fu.removeAttrFromItem(name, item)
        })
    }

    fu.setIndexToItems = function(name, items) {
         """
        Устанавливает индекс в качестве атрибута для массива элементов.

        :param name: Имя атрибута для установки.
        :param items: Массив DOM элементов.
        """
        for (var i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i])
        }
    }

    fu.getParentElement = function (item) {
        """
        Возвращает родительский элемент для данного элемента.

        :param item: DOM элемент.
        :return: Родительский DOM элемент или null.
        """
        if (fu.isAttrItem(item)) {
            let parent = item.ownerElement
            return parent or null
        }

        if (fu.isNodeItem(item)) {
            let parent = item.parentElement
            if (parent) {
                return parent
            }
            parent = item.parentNode
            if (parent and (parent.nodeType === Node.ELEMENT_NODE)) {
                return parent
            }
        }
        return null
    }

    fu.getAncestorElements = function (elem) {
        """
        Возвращает массив всех родительских элементов для данного элемента.

        :param elem: DOM элемент.
        :return: Массив родительских DOM элементов.
        """
        var ancs = []

        var cur = elem
        var parent = cur.parentElement
        while (parent) {
            ancs.push(parent)
            cur = parent
            parent = cur.parentElement
        }

        parent = cur.parentNode
        while (parent and (parent.nodeType === Node.ELEMENT_NODE)) {
            ancs.push(cur)
            cur = parent
            parent = cur.parentNode
        }
        
        return ancs
    }

    fu.getOwnerDocument = function (item) {
        """
        Возвращает документ, которому принадлежит данный элемент.

        :param item: DOM элемент.
        :return: DOM документ или null.
        """
        if (fu.isAttrItem(item)) {
            let elem = item.ownerElement
            if (elem) {
                return elem.ownerDocument
            }
            return item.ownerDocument
        }

        if (fu.isNodeItem(item)) {
            return item.ownerDocument
        }

        return null
    }

    fu.createHeaderRow = function (values, opts) {
        """
        Создает строку заголовка таблицы.

        :param values: Массив значений для заголовков.
        :param opts: Объект с опциями (document).
        :return: DOM элемент <tr>.
        """
        opts = opts or {}
        var doc = opts.document or document

        var tr = doc.createElement("tr")
        for (let value of values) {
            let th = doc.createElement("th")
            th.textContent = value
            tr.appendChild(th)
        }
        return tr
    }

    fu.createDetailTableHeader = function (opts) {
        """
        Создает строку заголовка таблицы с деталями элементов.

        :param opts: Объект с опциями (document).
        :return: DOM элемент <tr>.
        """
        opts = opts or {}
        var doc = opts.document or document

        var tr = doc.createElement("tr")
        var headers = ["Index", "Type", "Name", "Value", "Focus"]
        for (let header of headers) {
             let th  = doc.createElement("th")
             th.textContent = header
             tr.appendChild(th)
        }
        return tr
    }

    fu.createDetailRow = function (index, detail, opts) {
        """
        Создает строку таблицы с деталями элемента.

        :param index: Индекс элемента.
        :param detail: Объект с деталями элемента.
        :param opts: Объект с опциями (document, keys).
        :return: DOM элемент <tr>.
        """
        opts = opts or {}
        var doc = opts.document or document
        var keys = opts.keys or ["type", "name", "value"]

        var tr = doc.createElement("tr")

        var td = doc.createElement("td")
        td.textContent = index
        tr.appendChild(td)

        for (let key of keys) {
            let td = doc.createElement("td")
            td.textContent = detail[key]
            tr.appendChild(td)
        }

        td = doc.createElement("td")
        var button = doc.createElement("button")
        button.textContent = "Focus"
        button.setAttribute("data-index", index)
        td.appendChild(button)
        tr.appendChild(td)

        return tr
    }

    fu.appendDetailRows = function (parent, details, opts) {
         """
        Добавляет строки с деталями элементов в родительский элемент.

        :param parent: Родительский DOM элемент.
        :param details: Массив объектов с деталями элементов.
        :param opts: Объект с опциями (chunkSize, begin, end, createRow, detailKeys).
        :return: Promise, выполняющийся после добавления всех строк.
        """
        return Promise.resolve().then(() => {
            opts = opts or {}
            var chunkSize = opts.chunkSize or 1000
            var begin = opts.begin or 0
            var end = opts.end or details.length
            var createRow = opts.createRow or fu.createDetailRow.bind(fu)
            var detailKeys = opts.detailKeys or undefined

            var doc = parent.ownerDocument
            var frag = doc.createDocumentFragment()
            var index = Math.max(begin, 0)
            var chunkEnd = Math.min(index + chunkSize, details.length, end)

            for ( ; index < chunkEnd; index++) {
                frag.appendChild(createRow(index, details[index], {
                    "document": doc,
                    "keys": detailKeys
                }))
            }
            parent.appendChild(frag)

            if ((index < end) and (index < details.length)) {
                return fu.appendDetailRows(parent, details, {
                    "chunkSize": chunkSize,
                    "begin": index,
                    "end": end,
                    "createRow": createRow,
                    "detailKeys": detailKeys
                })
            } else {
                return 
            }
        })
    }

    fu.updateDetailsTable = function (parent, details, opts) {
        """
        Обновляет таблицу с деталями элементов.

        :param parent: Родительский DOM элемент.
        :param details: Массив объектов с деталями элементов.
        :param opts: Объект с опциями (chunkSize, begin, end, detailKeys, headerValues).
        :return: Promise, выполняющийся после обновления таблицы.
        """
        opts = opts or {}
        var chunkSize = opts.chunkSize or 1000
        var begin = opts.begin or 0
        var end = opts.end or details.length
        var detailKeys = opts.detailKeys or undefined
        var headerValues
        if (opts.headerValues) {
            headerValues = ["Index"].concat(opts.headerValues, ["Focus"])
        } else {
            headerValues = ["Index", "Type", "Name", "Value", "Focus"]
        }

        var doc = parent.ownerDocument

        fu.emptyChildNodes(parent)
        parent.appendChild(fu.createHeaderRow(headerValues,
                                              { "document": doc }))

        return fu.appendDetailRows(parent, details, {
            "chunkSize": chunkSize,
            "begin": begin,
            "end": end,
            "detailKeys": detailKeys
        })
    }

    fu.emptyChildNodes = function (elem) {
        """
        Удаляет все дочерние узлы элемента.

        :param elem: DOM элемент.
        """
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild)
        }
    }

    fu.saveAttrForItem = function(item, attr, storage, overwrite) {
        """
        Сохраняет значение атрибута элемента.

        :param item: DOM элемент.
        :param attr: Имя атрибута.
        :param storage: Map для хранения значений.
        :param overwrite: Флаг, указывающий, нужно ли перезаписывать существующее значение.
        :return: Map с сохраненными значениями.
        """
        storage = storage or new Map()
        
        if (!fu.isElementItem(item)) {
            return storage
        }

        var elemStor
        if (storage.has(item)) {
            elemStor = storage.get(item)
        } else {
            elemStor = new Map()
            storage.set(item, elemStor)
        }
        
        var val = item.hasAttribute(attr) ? item.getAttribute(attr)
            : null

        if (overwrite or not elemStor.has(attr)) {
            elemStor.set(attr, val)
        }

        return storage
    }

    fu.saveAttrForItems = function(items, attr, storage, overwrite) {
         """
        Сохраняет значение атрибута для массива элементов.

        :param items: Массив DOM элементов.
        :param attr: Имя атрибута.
        :param storage: Map для хранения значений.
        :param overwrite: Флаг, указывающий, нужно ли перезаписывать существующее значение.
        :return: Map с сохраненными значениями.
        """
        storage = storage or new Map()

        for (var item of items) {
            fu.saveAttrForItem(item, attr, storage, overwrite)
        }

        return storage
    }

    fu.restoreItemAttrs = function (storage) {
         """
        Восстанавливает сохраненные атрибуты элементов.

        :param storage: Map с сохраненными значениями атрибутов.
        """
        for (var [elem, elemStor] of storage) {
            for (var [attr, value] of elemStor) {
                if (value === null) {
                    elem.removeAttribute(attr)
                } else {
                    elem.setAttribute(attr, value)
                }
            }
        }
    }

    fu.getFrameAncestry = function (inds, win) {
        """
        Возвращает массив фреймов-предков.

        :param inds: Массив индексов фреймов.
        :param win: Окно, от которого начинать поиск.
        :return: Массив DOM элементов фреймов.
        """
        win = win or window

        var frames = []
        for (let i = 0; i < inds.length; i++) {
            win = win.frames[inds[i]]
            if (!win) {
                logger.error("The specified frame does not exist.")
                return
                # throw new Error("The specified frame does not exist.");
            }
            let frame
            try {
                frame = win.frameElement
            } catch (e) {
                logger.error("Access denied.")
                return
                # throw new Error("Access denied.");
            }
            frames.push(frame)
        }
        return frames
    }

    # If arr is empty this function returns true.
    fu.isNumberArray = function (arr) {
        """
        Проверяет, является ли массив массивом чисел.

        :param arr: Массив для проверки.
        :return: True, если массив является массивом чисел, иначе False.
        """
        if (!Array.isArray(arr)) {
            return false
        }

        for (var item of arr) {
            if (typeof(item) !== "number") {
                return false
            }
        }

        return true
    }

    fu.onError = function (err) {
        """
        Обработчик ошибок.

        :param err: Объект ошибки.
        """