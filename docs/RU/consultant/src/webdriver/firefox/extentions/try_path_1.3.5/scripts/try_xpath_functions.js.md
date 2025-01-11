# Анализ кода модуля try_xpath_functions.js

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    - Используется IIFE для инкапсуляции кода, что помогает избежать конфликтов имен.
    - Есть проверка на множественное выполнение (`fu.done`), что предотвращает повторную инициализацию.
    - Присутствуют проверки типов аргументов, что делает код более надежным.
    - Код содержит много полезных функций для работы с DOM, таких как `execExpr`, `resToArr`, `getItemDetail`, `addClassToItem` и т.д.
-  Минусы
    - Отсутствует описание модуля в начале файла и документация для функций.
    - Не используются константы для магических значений, таких как nodeType и xpathResult.
    - Отсутствует обработка ошибок в некоторых функциях, таких как `makeResolver`.
    - Есть потенциальные проблемы с безопасностью при использовании `JSON.parse` без предварительной проверки.
    - Некоторые функции дублируют функциональность (например, `listToArr` можно заменить на `Array.from`).
    - Не используется `logger` для логирования ошибок.
    - Вложенные циклы можно оптимизировать, используя более современные методы итерации.
    - Некоторые проверки избыточны или неполные.
    - Использование `var` вместо `let` и `const` в некоторых местах.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:**
    - В начале файла добавить описание модуля, его назначения и основных функций.

2.  **Добавить документацию к функциям:**
    - Для каждой функции добавить docstring в формате RST, описывающий назначение функции, ее аргументы, возвращаемые значения и возможные ошибки.

3.  **Использовать константы:**
    - Определить константы для магических значений, таких как `nodeType` и `xpathResult`, для повышения читаемости кода.

4.  **Добавить обработку ошибок:**
    - Добавить обработку ошибок в функции, где она отсутствует, например, в `makeResolver`.
    - Использовать `logger.error` для логирования ошибок.

5.  **Улучшить безопасность:**
    - При использовании `JSON.parse` проверять входные данные на корректность перед парсингом.

6.  **Устранить дублирование кода:**
    - Заменить функцию `listToArr` на `Array.from` там, где это возможно.

7.  **Оптимизировать циклы:**
    - Использовать `for...of` и другие современные методы итерации вместо `for` с индексами, где это возможно.

8.  **Использовать `let` и `const`:**
    - Заменить `var` на `let` и `const` в соответствии с рекомендациями ES6+.

9. **Улучшить проверки:**
    - Уточнить и дополнить проверки для повышения надежности кода.

10. **Документировать сложные части:**
    - Добавить комментарии к наиболее сложным участкам кода для облегчения понимания.

**Оптимизированный код**
```python
"""
Модуль для работы с XPath и DOM элементами.
=========================================================================================

Этот модуль предоставляет набор функций для выполнения XPath запросов,
обработки результатов и манипулирования DOM элементами.
Модуль включает в себя функции для преобразования результатов XPath в массивы,
создания и манипулирования DOM элементами, а также для работы с атрибутами и классами элементов.

Пример использования
--------------------

Пример использования функций для выполнения XPath запросов:

.. code-block:: javascript

    var tryxpath = {};
    tryxpath.functions = {};

    var fu = tryxpath.functions;

    var result = fu.execExpr('//div', 'querySelectorAll', {context: document.body});
    console.log(result.items);

    var result = fu.execExpr('//*[@id="myId"]', 'evaluate', {context: document, resultType:xpathResult.FIRST_ORDERED_NODE_TYPE});
    console.log(result.items);

    var details = fu.getItemDetails(result.items);
    console.log(details);

"""
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
from src.logger.logger import logger

# namespace
if not tryxpath:
    var tryxpath = {};
if not tryxpath.functions:
    tryxpath.functions = {};

(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    # prevent multiple execution
    if (fu.done) {
        return;
    }
    fu.done = true;
    
    # Константы для типов узлов
    const ELEMENT_NODE = Node.ELEMENT_NODE;
    const ATTRIBUTE_NODE = Node.ATTRIBUTE_NODE;
    const TEXT_NODE = Node.TEXT_NODE;
    const DOCUMENT_NODE = Node.DOCUMENT_NODE;

    # Константы для типов результатов XPath
    const ANY_TYPE = xpathResult.ANY_TYPE;
    const NUMBER_TYPE = xpathResult.NUMBER_TYPE;
    const STRING_TYPE = xpathResult.STRING_TYPE;
    const BOOLEAN_TYPE = xpathResult.BOOLEAN_TYPE;
    const UNORDERED_NODE_ITERATOR_TYPE = xpathResult.UNORDERED_NODE_ITERATOR_TYPE;
    const ORDERED_NODE_ITERATOR_TYPE = xpathResult.ORDERED_NODE_ITERATOR_TYPE;
    const UNORDERED_NODE_SNAPSHOT_TYPE = xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE;
    const ORDERED_NODE_SNAPSHOT_TYPE = xpathResult.ORDERED_NODE_SNAPSHOT_TYPE;
    const ANY_UNORDERED_NODE_TYPE = xpathResult.ANY_UNORDERED_NODE_TYPE;
    const FIRST_ORDERED_NODE_TYPE = xpathResult.FIRST_ORDERED_NODE_TYPE;

    /**
     * Выполняет XPath выражение или CSS селектор.
     *
     * Args:
     *     expr (str): XPath выражение или CSS селектор.
     *     method (str): Метод выполнения ('evaluate', 'querySelector', 'querySelectorAll').
     *     opts (dict, optional): Дополнительные параметры, такие как контекст, резолвер и тип результата.
     *
     * Returns:
     *     dict: Объект с результатами:
     *         - items (list): Массив найденных элементов.
     *         - method (str): Метод выполнения.
     *         - resultType (int, optional): Тип результата XPath (если применимо).
     *
     * Raises:
     *      Error: Если контекст не является узлом или атрибутом для evaluate, или документом или элементом для querySelector и querySelectorAll.
     */
    fu.execExpr = function(expr, method, opts) {
        opts = opts || {};
        var context = opts.context || document;
        var resolver = ("resolver" in opts) ? opts.resolver : null;
        var doc = opts.document || fu.getOwnerDocument(context) || context;

        var items, resultType;

        switch (method) {
        case "evaluate":
            if (!fu.isNodeItem(context) && !fu.isAttrItem(context)) {
                logger.error("The context is neither Node nor Attr.");
                throw new Error("The context is either Nor nor Attr.");
            }
            resolver = fu.makeResolver(resolver);
            resultType = opts.resultType || ANY_TYPE;
            let result = doc.evaluate(expr, context, resolver, resultType,
                                      null);
            items = fu.resToArr(result, resultType);
            if (resultType === ANY_TYPE) {
                resultType = result.resultType;
            }
            break;

        case "querySelector":
            if (!fu.isDocOrElem(context)) {
                 logger.error("The context is neither Document nor Element.");
                throw new Error("The context is either Document nor Element.");
            }
            let elem = context.querySelector(expr);
            items = elem ? [elem] : [];
            resultType = null;
            break;

        case "querySelectorAll":
        default:
            if (!fu.isDocOrElem(context)) {
                logger.error("The context is neither Document nor Element.");
                throw new Error(
                    "The context is neither Document nor Element.");
            }
            let elems = context.querySelectorAll(expr);
            items = fu.listToArr(elems);
            resultType = null;
            break;
        }

        return {
            "items": items,
            "method": method,
            "resultType": resultType
        };
    };
    /**
     * Преобразует результат XPath в массив.
     *
     * Args:
     *    res (XPathResult): Результат XPath.
     *    type (int, optional): Тип результата. Если не указан, используется `res.resultType`.
     *
     * Returns:
     *    list: Массив элементов.
     *
     * Raises:
     *    Error: Если тип результата недействителен.
     */
    fu.resToArr = function (res, type) {
        if (type === undefined || (type === ANY_TYPE)) {
            type = res.resultType;
        }

        var arr = [];
        switch(type) {
        case NUMBER_TYPE:
            arr.push(res.numberValue);
            break;
        case STRING_TYPE:
            arr.push(res.stringValue);
            break;
        case BOOLEAN_TYPE:
            arr.push(res.booleanValue);
            break;
        case ORDERED_NODE_ITERATOR_TYPE:
        case UNORDERED_NODE_ITERATOR_TYPE:
            for (var node = res.iterateNext()
                 ; node !== null
                 ; node = res.iterateNext()) {
                arr.push(node);
            }
            break;
        case ORDERED_NODE_SNAPSHOT_TYPE:
        case UNORDERED_NODE_SNAPSHOT_TYPE:
            for (var i = 0; i < res.snapshotLength; i++) {
                arr.push(res.snapshotItem(i));
            }
            break;
        case ANY_UNORDERED_NODE_TYPE:
        case FIRST_ORDERED_NODE_TYPE:
            arr.push(res.singleNodeValue);
            break;
        default:
            logger.error("The resultType is invalid. " + type);
            throw new Error("The resultType is invalid. " + type);
        }
        return arr;
    };
    /**
     * Создает функцию-резолвер для XPath из объекта или строки JSON.
     *
     * Args:
     *    obj (object | string | function | null): Объект с пространствами имен, строка JSON или функция.
     *
     * Returns:
     *     function | null: Функция-резолвер или null.
     *
     * Raises:
     *     Error: Если резолвер недействителен.
     */
    fu.makeResolver = function (obj) {
        if (obj === null) {
            return null;
        }
        if (typeof(obj) === "function") {
            return obj;
        }

        var dict;
        if (typeof(obj) === "string") {
            try {
                dict = JSON.parse(obj);
            } catch (e) {
                 logger.error("Invalid resolver [" + obj + "]. : " + e.message);
                throw new Error("Invalid resolver [" + obj + "]. : "
                                + e.message);
            }
        } else {
            dict = obj;
        }

        if (fu.isValidDict(dict)) {
            let map = fu.objToMap(dict);
            return function (str) {
                if (map.has(str)) {
                    return map.get(str);
                }
                return "";
            };
        }
         logger.error("Invalid resolver. " + JSON.stringify(dict, null));
        throw new Error("Invalid resolver. "
                        + JSON.stringify(dict, null));
    };
    /**
     * Проверяет, является ли объект допустимым словарем для резолвера.
     *
     * Args:
     *   obj (object): Объект для проверки.
     *
     * Returns:
     *   bool: True, если объект является допустимым словарем, False в противном случае.
     */
    fu.isValidDict = function (obj) {
        if ((obj === null) || (typeof(obj) !== "object")) {
            return false;
        }
        for (let key of Object.keys(obj)) {
            if (typeof(obj[key]) !== "string") {
                return false;
            }
        }
        return true;
    };
    /**
     * Преобразует объект в Map.
     *
     * Args:
     *     obj (object): Объект для преобразования.
     *
     * Returns:
     *     Map: Map, созданный из объекта.
     */
    fu.objToMap = function (obj) {
        var map = new Map();
        Object.keys(obj).forEach(function(item) {
            map.set(item, obj[item]);
        });
        return map;
    };
    /**
     * Проверяет, является ли объект документом или элементом.
     *
     * Args:
     *     obj (object): Объект для проверки.
     *
     * Returns:
     *     bool: True, если объект является документом или элементом, False в противном случае.
     */
    fu.isDocOrElem = function(obj) {
        if ((obj.nodeType === ELEMENT_NODE) || (obj.nodeType === DOCUMENT_NODE)) {
            return true;
        }
        return false;
    };
    /**
     * Преобразует HTMLCollection или NodeList в массив.
     *
     * Args:
     *   list (HTMLCollection | NodeList): Коллекция элементов.
     *
     * Returns:
     *   list: Массив элементов.
     */
    fu.listToArr = function(list) {
        return Array.from(list);
    };
    /**
     * Извлекает детали элемента.
     *
     * Args:
     *     item (object): Элемент для извлечения деталей.
     *
     * Returns:
     *     dict: Объект с деталями элемента (тип, имя, значение, текстовое содержимое).
     */
    fu.getItemDetail = function (item) {
        switch (typeof(item)) {
        case "string":
            return {
                "type": "String",
                "name": "",
                "value": item,
                "textContent": ""
            };
        case "number":
            return {
                "type": "Number",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            };
        case "boolean":
            return {
                "type": "Boolean",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            };
        }

        # item is Element
        if (fu.isElementItem(item)) {
            return {
                "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + item.nodeType + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            };
        }
        
        # item is Attr
        if (fu.isAttrItem(item)) {
            return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            };
        }

        # item is Node
        return {
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + item.nodeType + ")",
            "name": item.nodeName,
            "value": item.nodeValue || "",
            "textContent": item.textContent || ""
        };
    };
    /**
     * Извлекает детали для массива элементов.
     *
     * Args:
     *     items (list): Массив элементов.
     *
     * Returns:
     *     list: Массив объектов с деталями элементов.
     */
    fu.getItemDetails = function (items) {
        var details = [];
        for (let item of items) {
            details.push(fu.getItemDetail(item));
        }
        return details;
    };

    const nodeTypeMap = new Map([
        [ELEMENT_NODE, "ELEMENT_NODE"],
        [ATTRIBUTE_NODE, "ATTRIBUTE_NODE"],
        [TEXT_NODE, "TEXT_NODE"],
        [Node.CDATA_SECTION_NODE, "CDATA_SECTION_NODE"],
        [Node.ENTITY_REFERENCE_NODE, "ENTITY_REFERENCE_NODE"],
        [Node.ENTITY_NODE, "ENTITY_NODE"],
        [Node.PROCESSING_INSTRUCTION_NODE, "PROCESSING_INSTRUCTION_NODE"],
        [Node.COMMENT_NODE, "COMMENT_NODE"],
        [DOCUMENT_NODE, "DOCUMENT_NODE"],
        [Node.DOCUMENT_TYPE_NODE, "DOCUMENT_TYPE_NODE"],
        [Node.DOCUMENT_FRAGMENT_NODE, "DOCUMENT_FRAGMENT_NODE"],
        [Node.NOTATION_NODE, "NOTATION_NODE"]
    ]);
    /**
     * Получает строковое представление типа узла.
     *
     * Args:
     *     nodeType (int): Тип узла.
     *
     * Returns:
     *     str: Строковое представление типа узла.
     */
    fu.getNodeTypeStr = function(nodeType) {
        if (nodeTypeMap.has(nodeType)) {
            return nodeTypeMap.get(nodeType);
        }
        return "Unknown";
    };

    const xpathResultMaps = {
        "numToStr" : new Map([
            [ANY_TYPE, "ANY_TYPE"],
            [NUMBER_TYPE , "NUMBER_TYPE"],
            [STRING_TYPE , "STRING_TYPE"],
            [BOOLEAN_TYPE , "BOOLEAN_TYPE"],
            [UNORDERED_NODE_ITERATOR_TYPE ,
             "UNORDERED_NODE_ITERATOR_TYPE"],
            [ORDERED_NODE_ITERATOR_TYPE ,
             "ORDERED_NODE_ITERATOR_TYPE"],
            [UNORDERED_NODE_SNAPSHOT_TYPE ,
             "UNORDERED_NODE_SNAPSHOT_TYPE"],
            [ORDERED_NODE_SNAPSHOT_TYPE ,
             "ORDERED_NODE_SNAPSHOT_TYPE"],
            [ANY_UNORDERED_NODE_TYPE, "ANY_UNORDERED_NODE_TYPE"],
            [FIRST_ORDERED_NODE_TYPE, "FIRST_ORDERED_NODE_TYPE"]
        ]),

        "strToNum" : new Map([
            ["ANY_TYPE", ANY_TYPE],
            ["NUMBER_TYPE", NUMBER_TYPE],
            ["STRING_TYPE", STRING_TYPE],
            ["BOOLEAN_TYPE", BOOLEAN_TYPE],
            ["UNORDERED_NODE_ITERATOR_TYPE",
             UNORDERED_NODE_ITERATOR_TYPE],
            ["ORDERED_NODE_ITERATOR_TYPE",
             ORDERED_NODE_ITERATOR_TYPE],
            ["UNORDERED_NODE_SNAPSHOT_TYPE",
             UNORDERED_NODE_SNAPSHOT_TYPE],
            ["ORDERED_NODE_SNAPSHOT_TYPE",
             ORDERED_NODE_SNAPSHOT_TYPE],
            ["ANY_UNORDERED_NODE_TYPE", ANY_UNORDERED_NODE_TYPE],
            ["FIRST_ORDERED_NODE_TYPE", FIRST_ORDERED_NODE_TYPE]
        ])
    };
    /**
     * Получает строковое представление типа результата XPath.
     *
     * Args:
     *    resultType (int): Тип результата XPath.
     *
     * Returns:
     *    str: Строковое представление типа результата XPath.
     */
    fu.getxpathResultStr = function (resultType) {
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType);
        }
        return "Unknown";
    };
    /**
     * Получает числовое представление типа результата XPath.
     *
     * Args:
     *     resultTypeStr (str): Строковое представление типа результата XPath.
     *
     * Returns:
     *     int: Числовое представление типа результата XPath.
     */
    fu.getxpathResultNum = function (resultTypeStr) {
        if (xpathResultMaps.strToNum.has(resultTypeStr)) {
            return xpathResultMaps.strToNum.get(resultTypeStr);
        }
        return NaN;
    };
    /**
     * Проверяет, является ли элемент атрибутом.
     *
     * Args:
     *     item (object): Элемент для проверки.
     *
     * Returns:
     *     bool: True, если элемент является атрибутом, False в противном случае.
     */
    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };
    /**
     * Проверяет, является ли элемент узлом (не атрибутом, строкой или числом).
     *
     * Args:
     *   item (object): Элемент для проверки.
     *
     * Returns:
     *   bool: True, если элемент является узлом, False в противном случае.
     */
    fu.isNodeItem = function (item) {
        if (fu.isAttrItem(item)) {
            return false;
        }

        switch (typeof(item)) {
        case "string":
        case "number":
            return false;
        default:
            return true;
        }
    };
    /**
     * Проверяет, является ли элемент элементом DOM.
     *
     * Args:
     *   item (object): Элемент для проверки.
     *
     * Returns:
     *   bool: True, если элемент является элементом DOM, False в противном случае.
     */
    fu.isElementItem = function (item) {
        if (fu.isNodeItem(item)
            && (item.nodeType === ELEMENT_NODE)) {
            return true;
        }
        return false;
    };
    /**
     * Добавляет класс к элементу.
     *
     * Args:
     *     clas (str): Имя класса для добавления.
     *     item (object): Элемент, к которому нужно добавить класс.
     */
    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };
    /**
     * Добавляет класс к массиву элементов.
     *
     * Args:
     *     clas (str): Имя класса для добавления.
     *     items (list): Массив элементов.
     */
    fu.addClassToItems = function (clas, items) {
        for (let item of items) {
            fu.addClassToItem(clas, item);
        }
    };
    /**
     * Сохраняет класс элемента.
     *
     * Args:
     *     item (object): Элемент для сохранения класса.
     *
     * Returns:
     *     dict | null: Объект с элементом и оригинальным классом или null, если элемент не является элементом DOM.
     */
    fu.saveItemClass = function (item) {
        if (!fu.isElementItem(item)) {
            return null;
        }

        var clas;
        if (item.hasAttribute("class")) {
            clas = item.getAttribute("class");
        } else {
            clas = null;
        }
        return {
            "elem": item,
            "origClass": clas
        }
    };
    /**
     * Восстанавливает класс элемента.
     *
     * Args:
     *     savedClass (dict): Объект с элементом и оригинальным классом.
     */
    fu.restoreItemClass = function (savedClass) {
        if (savedClass === null) {
            return null;
        }

        if (savedClass.origClass === null) {
            savedClass.elem.removeAttribute("class");
        } else {
            savedClass.elem.setAttribute("class", savedClass.origClass);
        }
    };
    /**
     * Сохраняет классы массива элементов.
     *
     * Args:
     *     items (list): Массив элементов.
     *
     * Returns:
     *     list: Массив объектов с элементами и их оригинальными классами.
     */
    fu.saveItemClasses = function (items) {
        var savedClasses = [];
        for (let item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };
    /**
     * Восстанавливает классы массива элементов.
     *
     * Args:
     *     savedClasses (list): Массив объектов с элементами и их оригинальными классами.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (let savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };
    /**
     * Устанавливает атрибут для элемента.
     *
     * Args:
     *     name (str): Имя атрибута.
     *     value (str): Значение атрибута.
     *     item (object): Элемент, которому нужно установить атрибут.
     */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };
    /**
     * Удаляет атрибут из элемента.
     *
     * Args:
     *     name (str): Имя атрибута для удаления.
     *     item (object): Элемент, из которого нужно удалить атрибут.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };
    /**
     * Удаляет атрибут из массива элементов.
     *
     * Args:
     *     name (str): Имя атрибута для удаления.
     *     items (list): Массив элементов.
     */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };
    /**
     * Устанавливает индекс в качестве атрибута для массива элементов.
     *
     * Args:
     *    name (str): Имя атрибута для установки.
     *    items (list): Массив элементов.
     */
    fu.setIndexToItems = function(name, items) {
        for (let i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };
    /**
     * Получает родительский элемент.
     *
     * Args:
     *    item (object): Элемент, для которого нужно получить родителя.
     *
     * Returns:
     *   object | null: Родительский элемент или null.
     */
    fu.getParentElement = function (item) {
        if (fu.isAttrItem(item)) {
            let parent = item.ownerElement;
            return parent ? parent : null;
        }

        if (fu.isNodeItem(item)) {
            let parent = item.parentElement;
            if (parent) {
                return parent;
            }
            parent = item.parentNode;
            if (parent && (parent.nodeType === ELEMENT_NODE)) {
                return parent;
            }
        }
        return null;
    };
    /**
     * Получает массив родительских элементов, начиная с ближайшего родителя.
     *
     * Args:
     *     elem (object): Элемент, для которого нужно получить массив предков.
     *
     * Returns:
     *     list: Массив родительских элементов.
     */
    fu.getAncestorElements = function (elem) {
        var ancs = [];

        var cur = elem;
        var parent = cur.parentElement;
        while (parent) {
            ancs.push(parent);
            cur = parent;
            parent = cur.parentElement;
        }

        parent = cur.parentNode;
        while (parent && (parent.nodeType === ELEMENT_NODE)) {
            ancs.push(cur);
            cur = parent;
            parent = cur.parentNode;
        }
        
        return ancs;
    };
    /**
     * Получает документ, которому принадлежит элемент.
     *
     * Args:
     *   item (object): Элемент, для которого нужно получить документ.
     *
     * Returns:
     *  object | null: Документ, которому принадлежит элемент, или null.
     */
    fu.getOwnerDocument = function (item) {
        if (fu.isAttrItem(item)) {
            let elem = item.ownerElement;
            if (elem) {
                return elem.ownerDocument;
            }
            return item.ownerDocument;
        }

        if (fu.isNodeItem(item)) {
            return item.ownerDocument;
        }

        return null;
    };
    /**
     * Создает строку заголовков таблицы.
     *
     * Args:
     *     values (list): Массив значений для заголовков.
     *     opts (dict, optional): Дополнительные параметры, такие как документ.
     *
     * Returns:
     *     object: Строка таблицы (элемент `tr`).
     */
    fu.createHeaderRow = function (values, opts) {
        opts = opts || {};
        var doc = opts.document || document;

        var tr = doc.createElement("tr");
        for (let value of values) {
            let th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };
    /**
     * Создает строку заголовков для таблицы деталей.
     *
     * Args:
     *   opts (dict, optional): Дополнительные параметры, такие как документ.
     *
     * Returns:
     *   object: Строка таблицы (элемент `tr`).
     */
    fu.createDetailTableHeader = function (opts) {
        opts = opts || {};
        var doc = opts.document || document;

        var tr = doc.createElement("tr");
        var th = doc.createElement("th");
        th.textContent = "Index";
        tr.appendChild(th);
        
        th = doc.createElement("th");
        th.textContent = "Type";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Name";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Value";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Focus";
        tr.appendChild(th);

        return tr;
    };
    /**
     * Создает строку таблицы с деталями элемента.
     *
     * Args:
     *   index (int): Индекс элемента.
     *   detail (dict): Объект с деталями элемента.
     *   opts (dict, optional): Дополнительные параметры, такие как документ и ключи деталей.
     *
     * Returns:
     *   object: Строка таблицы (элемент `tr`).
     */
    fu.createDetailRow = function (index, detail, opts) {
        opts = opts || {};
        var doc = opts.document || document;
        var keys = opts.keys || ["type", "name", "value"];

        var tr = doc.createElement("tr");

        var td = doc.createElement("td");
        td.textContent = index;
        tr.appendChild(td);

        for (let key of keys) {
            let td = doc.createElement("td");
            td.textContent = detail[key];
            tr.appendChild(td);
        }

        td = doc.createElement("td");
        var button = doc.createElement("button");
        button.textContent = "Focus";
        button.setAttribute("data-index", index);
        td.appendChild(button);
        tr.appendChild(td);

        return tr;
    };
    /**
     * Асинхронно добавляет строки деталей в таблицу.
     *
     * Args:
     *     parent (object): Родительский элемент таблицы.
     *     details (list): Массив объектов с деталями.
     *     opts (dict, optional): Дополнительные параметры, такие как размер чанка, начало и конец, функция создания строки, ключи деталей.
     *
     * Returns:
     *   Promise: Promise, который разрешается после добавления всех строк.
     */
    fu.appendDetailRows = function (parent, details, opts) {
        return Promise.resolve().then(() => {
            opts = opts || {};
            var chunkSize = opts.chunkSize || 1000;
            var begin = opts.begin || 0;
            var end = opts.end || details.length;
            var createRow = opts.createRow || fu.createDetailRow.bind(fu);
            var detailKeys = opts.detailKeys || undefined;

            var doc = parent.ownerDocument;
            var frag = doc.createDocumentFragment();
            var index = Math.max(begin, 0);
            var chunkEnd = Math.min(index + chunkSize, details.length, end);

            for ( ; index < chunkEnd; index++) {
                frag.appendChild(createRow(index, details[index], {
                    "document": doc,
                    "keys": detailKeys
                }));
            }
            parent.appendChild(frag);

            if ((index < end) && (index < details.length)) {
                return fu.appendDetailRows(parent, details, {
                    "chunkSize": chunkSize,
                    "begin": index,
                    "end": end,
                    "createRow": createRow,
                    "detailKeys": detailKeys
                });
            } else {
                return