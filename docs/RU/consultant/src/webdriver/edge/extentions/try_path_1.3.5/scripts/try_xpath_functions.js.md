# Анализ кода модуля `try_xpath_functions.js`

**Качество кода**

-  Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы:
        -   Код хорошо структурирован и разбит на функции, что облегчает понимание и поддержку.
        -   Используются константы для `nodeTypeMap` и `xpathResultMaps`, что улучшает читаемость и консистентность.
        -   Присутствуют комментарии, объясняющие назначение некоторых частей кода.
        -   Код избегает глобальных переменных, используя замыкания для инкапсуляции переменных внутри модуля.
    -   Минусы:
        -   Отсутствует подробная документация в формате RST для функций и модуля.
        -   Используются `var` вместо `let` и `const` для объявления переменных.
        -   Не все функции имеют docstring, что затрудняет понимание их предназначения.
        -   Многократное использование `opts = opts || {};` можно заменить на дефолтные значения параметров.
        -   Используется `Promise.resolve().then(...)` для асинхронности, что можно улучшить с помощью `async/await`.
        -   В некоторых местах обработка ошибок отсутствует или слишком проста.
        -   Некоторые функции, например, `onError`,  не используются и их можно удалить.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring в формате RST для всех функций, методов и модуля.
2.  **Объявление переменных:** Заменить `var` на `let` и `const` везде, где это возможно.
3.  **Параметры функций:** Использовать дефолтные значения параметров вместо `opts = opts || {}`.
4.  **Асинхронность:** Использовать `async/await` вместо `Promise.resolve().then(...)`.
5.  **Обработка ошибок:** Добавить обработку ошибок с использованием `logger.error` и улучшить обработку исключений.
6.  **Удаление неиспользуемого кода:** Убрать неиспользуемую функцию `onError`.
7.  **Форматирование кода:** Привести код к единому стилю, добавить отступы и переносы строк для лучшей читаемости.
8.  **Именование переменных и функций:** Проверить и при необходимости привести имена переменных и функций к единому стилю и соответствию ранее обработанным файлам.

**Оптимизированный код**

```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

/**
 * Модуль tryxpath.functions
 * =========================================================================================
 *
 * Этот модуль содержит набор функций для работы с XPath и DOM,
 * включая выполнение XPath-выражений, преобразование результатов,
 * получение деталей элементов, управление классами и атрибутами,
 * а также работу с фреймами.
 *
 * Пример использования
 * --------------------
 *
 * Пример использования функции `execExpr`:
 *
 * .. code-block:: javascript
 *
 *   const result = tryxpath.functions.execExpr('//div', 'querySelectorAll', { context: document });
 *   console.log(result.items);
 */

// namespace
if (!tryxpath) {
    var tryxpath = {};
}
if (!tryxpath.functions) {
    tryxpath.functions = {};
}

(function (window, undefined) {
    "use strict";

    // alias
    const tx = tryxpath;
    const fu = tryxpath.functions;

    // prevent multiple execution
    if (fu.done) {
        return;
    }
    fu.done = true;


    /**
     * Выполняет XPath выражение или CSS селектор.
     *
     * Args:
     *     expr (str): XPath выражение или CSS селектор.
     *     method (str): Метод для выполнения (`evaluate`, `querySelector`, `querySelectorAll`).
     *     opts (dict): Дополнительные опции, включая `context`, `resolver`, `document` и `resultType`.
     *
     * Returns:
     *     dict: Объект с результатами, методом и типом результата.
     *
     * Raises:
     *    Error: Если контекст не является узлом или атрибутом при использовании `evaluate`,
     *           или если контекст не является документом или элементом при использовании `querySelector` или `querySelectorAll`.
     */
    fu.execExpr = function(expr, method, opts = {}) {
        const context = opts.context || document;
        const resolver = opts.resolver || null;
        const doc = opts.document || fu.getOwnerDocument(context) || context;

        let items, resultType;

        switch (method) {
        case "evaluate":
            if (!fu.isNodeItem(context) && !fu.isAttrItem(context)) {
                throw new Error("The context is neither Node nor Attr.");
            }
            const resolverFn = fu.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, resolverFn, resultType,
                                      null);
            items = fu.resToArr(result, resultType);
            if (resultType === xpathResult.ANY_TYPE) {
                resultType = result.resultType;
            }
            break;

        case "querySelector":
            if (!fu.isDocOrElem(context)) {
                throw new Error("The context is neither Document nor Element.");
            }
            let elem = context.querySelector(expr);
            items = elem ? [elem] : [];
            resultType = null;
            break;

        case "querySelectorAll":
        default:
            if (!fu.isDocOrElem(context)) {
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
     *     res (XPathResult): Результат XPath.
     *     type (int): Тип результата XPath.
     *
     * Returns:
     *     list: Массив элементов.
     *
     * Raises:
     *     Error: Если resultType невалидный.
     */
    fu.resToArr = function (res, type) {
        if (type === undefined || (type === xpathResult.ANY_TYPE)) {
            type = res.resultType;
        }

        const arr = [];
        switch(type) {
        case xpathResult.NUMBER_TYPE :
            arr.push(res.numberValue);
            break;
        case xpathResult.STRING_TYPE :
            arr.push(res.stringValue);
            break;
        case xpathResult.BOOLEAN_TYPE :
            arr.push(res.booleanValue);
            break;
        case xpathResult.ORDERED_NODE_ITERATOR_TYPE :
        case xpathResult.UNORDERED_NODE_ITERATOR_TYPE :
            for (let node = res.iterateNext()
                 ; node !== null
                 ; node = res.iterateNext()) {
                arr.push(node);
            }
            break;
        case xpathResult.ORDERED_NODE_SNAPSHOT_TYPE :
        case xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE :
            for (let i = 0; i < res.snapshotLength; i++) {
                arr.push(res.snapshotItem(i));
            }
            break;
        case xpathResult.ANY_UNORDERED_NODE_TYPE :
        case xpathResult.FIRST_ORDERED_NODE_TYPE :
            arr.push(res.singleNodeValue);
            break;
        default :
            throw new Error("The resultType is invalid. " + type);
        }
        return arr;
    };

    /**
     * Создает функцию-резолвер для XPath выражений.
     *
     * Args:
     *    obj (object | str | function): Объект, строка JSON или функция, которые будут использоваться в качестве резолвера.
     *
     * Returns:
     *   function: Функция резолвер.
     *
     * Raises:
     *   Error: Если резолвер невалидный.
     */
    fu.makeResolver = function (obj) {
        if (obj === null) {
            return null;
        }
        if (typeof(obj) === "function") {
            return obj;
        }

        let dict;
        if (typeof(obj) === "string") {
            try {
                dict = JSON.parse(obj);
            } catch (e) {
                throw new Error("Invalid resolver [" + obj + "]. : "
                                + e.message);
            }
        } else {
            dict = obj;
        }

        if (fu.isValidDict(dict)) {
            const map = fu.objToMap(dict);
            return function (str) {
                if (map.has(str)) {
                    return map.get(str);
                }
                return "";
            };
        }
        throw new Error("Invalid resolver. "
                        + JSON.stringify(dict, null));
    };

    /**
    * Проверяет, является ли объект допустимым словарем для резолвера.
    *
    * Args:
    *    obj (object): Объект для проверки.
    *
    * Returns:
    *    bool: True, если объект является допустимым словарем, иначе False.
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
    *    obj (object): Объект для преобразования.
    *
    * Returns:
    *    Map: Map, созданный на основе объекта.
    */
    fu.objToMap = function (obj) {
        const map = new Map();
        Object.keys(obj).forEach(function(item) {
            map.set(item, obj[item]);
        });
        return map;
    };

    /**
    * Проверяет, является ли объект документом или элементом.
    *
    * Args:
    *   obj (object): Объект для проверки.
    *
    * Returns:
    *   bool: True, если объект является документом или элементом, иначе False.
    */
    fu.isDocOrElem = function(obj) {
        if ((obj.nodeType === 1) || (obj.nodeType === 9)) {
            return true;
        }
        return false;
    };

    /**
    * Преобразует NodeList в массив.
    *
    * Args:
    *    list (NodeList): NodeList для преобразования.
    *
    * Returns:
    *   list: Массив элементов.
    */
    fu.listToArr = function(list) {
        const elems = [];
        for (let i = 0; i < list.length; i++) {
            elems.push(list[i]);
        }
        return elems;
    };


    /**
     * Получает детали элемента.
     *
     * Args:
     *     item (object): Элемент, для которого нужно получить детали.
     *
     * Returns:
     *     dict: Объект с типом, именем, значением и текстовым содержимым элемента.
     */
    fu.getItemDetail = function (item) {
        const typeStr = typeof(item);

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

        // item is Element
        if (fu.isElementItem(item)) {
            return {
                "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + item.nodeType + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            };
        }

        // item is Attr
        if (fu.isAttrItem(item)) {
            return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            };
        }

        // item is Node
        return {
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + item.nodeType + ")",
            "name": item.nodeName,
            "value": item.nodeValue || "",
            "textContent": item.textContent || ""
        };
    };

    /**
    * Получает детали для массива элементов.
    *
    * Args:
    *     items (list): Массив элементов.
    *
    * Returns:
    *   list: Массив объектов с деталями элементов.
    */
    fu.getItemDetails = function (items) {
        const details = [];
        for (let i = 0; i < items.length; i++) {
            details.push(fu.getItemDetail(items[i]));
        }
        return details;
    };

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
     *    resultTypeStr (str): Строковое представление типа результата XPath.
     *
     * Returns:
     *    int: Числовое представление типа результата XPath или NaN, если строка не найдена.
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
    *    bool: True, если элемент является атрибутом, иначе False.
    */
    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };


    /**
    * Проверяет, является ли элемент узлом.
    *
    * Args:
    *     item (object): Элемент для проверки.
    *
    * Returns:
    *    bool: True, если элемент является узлом, иначе False.
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
    * Проверяет, является ли элемент элементом (HTMLElement).
    *
    * Args:
    *     item (object): Элемент для проверки.
    *
    * Returns:
    *    bool: True, если элемент является элементом, иначе False.
    */
    fu.isElementItem = function (item) {
        if (fu.isNodeItem(item)
            && (item.nodeType === Node.ELEMENT_NODE)) {
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
     *     items (list): Массив элементов, к которым нужно добавить класс.
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
    *    item (object): Элемент, класс которого нужно сохранить.
    *
    * Returns:
    *    dict: Объект с элементом и его исходным классом.
    */
    fu.saveItemClass = function (item) {
        if (!fu.isElementItem(item)) {
            return null;
        }

        let clas;
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
    *    savedClass (dict): Объект с элементом и его сохраненным классом.
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
     *     list: Массив объектов с сохраненными классами.
     */
    fu.saveItemClasses = function (items) {
        const savedClasses = [];
        for (let item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };


    /**
     * Восстанавливает классы массива элементов.
     *
     * Args:
     *     savedClasses (list): Массив объектов с сохраненными классами.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (let savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };


    /**
    * Устанавливает атрибут элемента.
    *
    * Args:
    *    name (str): Имя атрибута.
    *    value (str): Значение атрибута.
    *    item (object): Элемент, которому нужно установить атрибут.
    */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    /**
     * Удаляет атрибут элемента.
     *
     * Args:
     *     name (str): Имя атрибута для удаления.
     *     item (object): Элемент, у которого нужно удалить атрибут.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };


    /**
    * Удаляет атрибут у всех элементов массива.
    *
    * Args:
    *    name (str): Имя атрибута для удаления.
    *    items (list): Массив элементов, у которых нужно удалить атрибут.
    */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };


    /**
     * Устанавливает индекс как атрибут для массива элементов.
     *
     * Args:
     *     name (str): Имя атрибута для установки индекса.
     *     items (list): Массив элементов.
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
     *     item (object): Элемент, для которого нужно получить родительский элемент.
     *
     * Returns:
     *     object | null: Родительский элемент или null, если родителя нет.
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
            if (parent && (parent.nodeType === Node.ELEMENT_NODE)) {
                return parent;
            }
        }
        return null;
    };

    /**
    * Получает список всех родительских элементов для элемента.
    *
    * Args:
    *   elem (object): Элемент, для которого нужно получить список родительских элементов.
    *
    * Returns:
    *   list: Список родительских элементов.
    */
    fu.getAncestorElements = function (elem) {
        const ancs = [];

        let cur = elem;
        let parent = cur.parentElement;
        while (parent) {
            ancs.push(parent);
            cur = parent;
            parent = cur.parentElement;
        }

        parent = cur.parentNode;
        while (parent && (parent.nodeType === Node.ELEMENT_NODE)) {
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
    *    item (object): Элемент.
    *
    * Returns:
    *    object: Документ, которому принадлежит элемент.
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
    * Создает строку заголовка таблицы.
    *
    * Args:
    *     values (list): Массив значений для заголовков.
    *     opts (dict): Дополнительные опции, включая `document`.
    *
    * Returns:
    *   object: Строка заголовка таблицы.
    */
    fu.createHeaderRow = function (values, opts = {}) {
        const doc = opts.document || document;

        const tr = doc.createElement("tr");
        for (let value of values) {
            const th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };


    /**
     * Создает строку заголовка таблицы с деталями.
     *
     * Args:
     *     opts (dict): Дополнительные опции, включая `document`.
     *
     * Returns:
     *     object: Строка заголовка таблицы с деталями.
     */
    fu.createDetailTableHeader = function (opts = {}) {
        const doc = opts.document || document;

        const tr = doc.createElement("tr");
        let th = doc.createElement("th");
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
     *     index (int): Индекс элемента.
     *     detail (dict): Детали элемента.
     *     opts (dict): Дополнительные опции, включая `document` и `keys`.
     *
     * Returns:
     *     object: Строка таблицы с деталями элемента.
     */
    fu.createDetailRow = function (index, detail, opts = {}) {
        const doc = opts.document || document;
        const keys = opts.keys || ["type", "name", "value"];

        const tr = doc.createElement("tr");

        let td = doc.createElement("td");
        td.textContent = index;
        tr.appendChild(td);

        for (let key of keys) {
            let td = doc.createElement("td");
            td.textContent = detail[key];
            tr.appendChild(td);
        }

        td = doc.createElement("td");
        const button = doc.createElement("button");
        button.textContent = "Focus";
        button.setAttribute("data-index", index);
        td.appendChild(button);
        tr.appendChild(td);

        return tr;
    };

    /**
    * Асинхронно добавляет строки с деталями в родительский элемент.
    *
    * Args:
    *    parent (object): Родительский элемент, в который будут добавлены строки.
    *    details (list): Массив деталей элементов.
    *    opts (dict): Дополнительные опции, включая `chunkSize`, `begin`, `end`, `createRow` и `detailKeys`.
    *
    * Returns:
    *    Promise: Промис, который разрешится после добавления всех строк.
    */
    fu.appendDetailRows = async function (parent, details, opts = {}) {
        const chunkSize = opts.chunkSize || 1000;
        let begin = opts.begin || 0;
        const end = opts.end || details.length;
        const createRow = opts.createRow || fu.createDetailRow.bind(fu);
        const detailKeys = opts.detailKeys || undefined;

        const doc = parent.ownerDocument;
        const frag = doc.createDocumentFragment();
        let index = Math.max(begin, 0);
        const chunkEnd = Math.min(index + chunkSize, details.length, end);

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
            return;
        }
    };

    /**
    * Обновляет таблицу с деталями.
    *
    * Args:
    *    parent (object): Родительский элемент таблицы.
    *    details (list): Массив деталей элементов.
    *    opts (dict): Дополнительные опции, включая `chunkSize`, `begin`, `end`, `detailKeys` и `headerValues`.
    *
    * Returns:
    *    Promise: Промис, который разрешится после обновления таблицы.
    */
    fu.updateDetailsTable = async function (parent, details, opts = {}) {
        const chunkSize = opts.chunkSize || 1000;
        const begin = opts.begin || 0;
        const end = opts.end || details.length;
        const detailKeys = opts.detailKeys || undefined;
        let headerValues;
        if (opts.headerValues) {
            headerValues = ["Index"].concat(opts.headerValues, ["Focus"]);
        } else {
            headerValues = ["Index", "Type", "Name", "Value", "Focus"];
        }

        const doc = parent.ownerDocument;

        fu.emptyChildNodes(parent);
        parent.appendChild(fu.createHeaderRow(headerValues,
                                              { "document": doc }));

        return fu.appendDetailRows(parent, details, {
            "chunkSize": chunkSize,
            "begin": begin,
            "end": end,
            "detailKeys": detailKeys
        });
    };

    /**
    * Очищает все дочерние узлы элемента.
    *
    * Args:
    *   elem (object): Элемент, дочерние узлы которого нужно удалить.
    */
    fu.emptyChildNodes = function (elem) {
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild);
        }
    };

    /**
    * Сохраняет значение атрибута для элемента.
    *
    * Args:
    *    item (object): Элемент, атрибут которого нужно сохранить.
    *    attr (str): Имя атрибута.
    *    storage (Map): Map для хранения сохраненных атрибутов.
    *    overwrite (bool): Флаг, указывающий, нужно ли перезаписывать существующее значение атрибута.
    *
    * Returns:
    *   Map: Обновленный Map с сохраненными атрибутами.
    */
    fu.saveAttrForItem = function(item, attr, storage = new Map(), overwrite) {
        if (!fu.isElementItem(item)) {
            return storage;
        }

        let elemStor;
        if