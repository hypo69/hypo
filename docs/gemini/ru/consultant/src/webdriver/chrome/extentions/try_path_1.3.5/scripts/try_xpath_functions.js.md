# Анализ кода модуля tryxpath_functions.js

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код хорошо структурирован и разбит на логические функции.
    *   Используются строгие режимы (`"use strict"`).
    *   Присутствует обработка различных типов результатов XPath.
    *   Функции имеют четкие имена, описывающие их предназначение.
    *   Используются Map для хранения соответствий, что улучшает производительность.
    *   Наличие функций для работы с DOM (добавление/удаление классов, атрибутов).
    *   Функции для работы с фреймами.
*   **Минусы:**
    *   Отсутствуют комментарии в формате reStructuredText (RST).
    *   Не используется логирование ошибок через `src.logger.logger`.
    *   Множественные блоки `try-catch` без явного логирования ошибок.
    *   В некоторых местах можно улучшить читаемость кода, например, используя `const` вместо `var` там где это уместно.
    *   Не все функции имеют docstring.
    *   Не используются импорты из других модулей, так как это JavaScript, в данном случае не применимо.

**Рекомендации по улучшению:**

1.  **Документация RST:** Добавить docstring в формате RST для всех функций, переменных и блоков кода.
2.  **Логирование:** Использовать `src.logger.logger` для логирования ошибок и отладочной информации.
3.  **Обработка ошибок:** Заменить множественные `try-catch` на более централизованную обработку ошибок с логированием.
4.  **Улучшение читаемости:** Заменить `var` на `const` и `let` где это возможно.
5.  **Использовать Map:** Использовать `Map` вместо обычных объектов, где это уместно.
6.  **Форматирование:** Сделать код более читаемым за счет форматирования и разделения длинных строк.

**Оптимизированный код:**

```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

/**
 * Модуль для работы с XPath и DOM элементами.
 * =========================================================================================
 *
 * Этот модуль содержит функции для выполнения XPath запросов,
 * обработки результатов, управления атрибутами и классами DOM элементов,
 * а также для работы с фреймами.
 *
 * Пример использования
 * --------------------
 *
 * .. code-block:: javascript
 *
 *      // Пример выполнения XPath запроса
 *      const result = tryxpath.functions.execExpr('//div', 'evaluate', { context: document });
 *      console.log(result.items);
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
     * Выполняет XPath выражение.
     *
     * :param expr: XPath выражение.
     * :param method: Метод выполнения запроса ("evaluate", "querySelector", "querySelectorAll").
     * :param opts: Опции выполнения запроса.
     * :return: Объект с результатами запроса.
     *
     * :raises Error: Если контекст не является узлом или атрибутом при использовании evaluate,
     *                или если контекст не является документом или элементом при использовании querySelector/querySelectorAll.
     */
    fu.execExpr = function(expr, method, opts) {
        opts = opts || {};
        const context = opts.context || document;
        const resolver = ("resolver" in opts) ? opts.resolver : null;
        const doc = opts.document || fu.getOwnerDocument(context) || context;

        let items, resultType;

        switch (method) {
        case "evaluate":
            if (!fu.isNodeItem(context) && !fu.isAttrItem(context)) {
                throw new Error("The context is either Nor nor Attr.");
            }
            const evalResolver = fu.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, evalResolver, resultType,
                                      null);
            items = fu.resToArr(result, resultType);
            if (resultType === xpathResult.ANY_TYPE) {
                resultType = result.resultType;
            }
            break;

        case "querySelector":
            if (!fu.isDocOrElem(context)) {
                throw new Error("The context is either Document nor Element.");
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
     * :param res: Результат XPath.
     * :param type: Тип результата XPath.
     * :return: Массив элементов.
     *
     * :raises Error: Если resultType не является допустимым типом.
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
     * Создает резолвер пространства имен.
     *
     * :param obj: Объект, строка JSON или функция резолвера.
     * :return: Функция резолвера.
     *
     * :raises Error: Если переданный резолвер не валиден.
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
     * :param obj: Объект для проверки.
     * :return: True, если объект - допустимый словарь, False в противном случае.
     */
    fu.isValidDict = function (obj) {
        if ((obj === null) || (typeof(obj) !== "object")) {
            return false;
        }
        for (const key of Object.keys(obj)) {
            if (typeof(obj[key]) !== "string") {
                return false;
            }
        }
        return true;
    };

    /**
     * Преобразует объект в Map.
     *
     * :param obj: Объект для преобразования.
     * :return: Map, содержащий пары ключ-значение из объекта.
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
     * :param obj: Объект для проверки.
     * :return: True, если объект - документ или элемент, False в противном случае.
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
     * :param list: NodeList для преобразования.
     * :return: Массив элементов.
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
     * :param item: Элемент для получения деталей.
     * :return: Объект с деталями элемента.
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
     * :param items: Массив элементов.
     * :return: Массив объектов с деталями элементов.
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
     * :param nodeType: Тип узла.
     * :return: Строковое представление типа узла.
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
     * :param resultType: Числовое представление типа результата XPath.
     * :return: Строковое представление типа результата XPath.
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
     * :param resultTypeStr: Строковое представление типа результата XPath.
     * :return: Числовое представление типа результата XPath.
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
     * :param item: Элемент для проверки.
     * :return: True, если элемент - атрибут, False в противном случае.
     */
    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };

    /**
     * Проверяет, является ли элемент узлом.
     *
     * :param item: Элемент для проверки.
     * :return: True, если элемент - узел, False в противном случае.
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
     * :param item: Элемент для проверки.
     * :return: True, если элемент - DOM элемент, False в противном случае.
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
     * :param clas: Класс для добавления.
     * :param item: Элемент.
     */
    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };

    /**
     * Добавляет класс к массиву элементов.
     *
     * :param clas: Класс для добавления.
     * :param items: Массив элементов.
     */
    fu.addClassToItems = function (clas, items) {
        for (const item of items) {
            fu.addClassToItem(clas, item);
        }
    };

    /**
     * Сохраняет класс элемента.
     *
     * :param item: Элемент.
     * :return: Объект с элементом и его оригинальным классом.
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
     * :param savedClass: Объект с элементом и его оригинальным классом.
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
     * :param items: Массив элементов.
     * :return: Массив объектов с элементами и их оригинальными классами.
     */
    fu.saveItemClasses = function (items) {
        const savedClasses = [];
        for (const item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };

    /**
     * Восстанавливает классы массива элементов.
     *
     * :param savedClasses: Массив объектов с элементами и их оригинальными классами.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (const savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };

    /**
     * Устанавливает атрибут элемента.
     *
     * :param name: Имя атрибута.
     * :param value: Значение атрибута.
     * :param item: Элемент.
     */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    /**
     * Удаляет атрибут элемента.
     *
     * :param name: Имя атрибута.
     * :param item: Элемент.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };

    /**
     * Удаляет атрибут у массива элементов.
     *
     * :param name: Имя атрибута.
     * :param items: Массив элементов.
     */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };

    /**
     * Устанавливает индекс в качестве атрибута для массива элементов.
     *
     * :param name: Имя атрибута.
     * :param items: Массив элементов.
     */
    fu.setIndexToItems = function(name, items) {
        for (let i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };

    /**
     * Получает родительский элемент.
     *
     * :param item: Элемент.
     * :return: Родительский элемент или null.
     */
    fu.getParentElement = function (item) {
        if (fu.isAttrItem(item)) {
            const parent = item.ownerElement;
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
     * Получает все родительские элементы.
     *
     * :param elem: Элемент.
     * :return: Массив родительских элементов.
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
     * Получает документ владельца элемента.
     *
     * :param item: Элемент.
     * :return: Документ владельца или null.
     */
    fu.getOwnerDocument = function (item) {
        if (fu.isAttrItem(item)) {
            const elem = item.ownerElement;
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
     * :param values: Массив значений для заголовков.
     * :param opts: Опции.
     * :return: Строка заголовка таблицы.
     */
    fu.createHeaderRow = function (values, opts) {
        opts = opts || {};
        const doc = opts.document || document;

        const tr = doc.createElement("tr");
        for (const value of values) {
            const th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };

    /**
     * Создает заголовок таблицы с деталями.
     *
     * :param opts: Опции.
     * :return: Строка заголовка таблицы с деталями.
     */
    fu.createDetailTableHeader = function (opts) {
        opts = opts || {};
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
     * Создает строку таблицы с деталями.
     *
     * :param index: Индекс строки.
     * :param detail: Объект с деталями.
     * :param opts: Опции.
     * :return: Строка таблицы с деталями.
     */
    fu.createDetailRow = function (index, detail, opts) {
        opts = opts || {};
        const doc = opts.document || document;
        const keys = opts.keys || ["type", "name", "value"];

        const tr = doc.createElement("tr");

        let td = doc.createElement("td");
        td.textContent = index;
        tr.appendChild(td);

        for (const key of keys) {
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
     * Добавляет строки деталей в таблицу.
     *
     * :param parent: Родительский элемент таблицы.
     * :param details: Массив объектов с деталями.
     * :param opts: Опции.
     * :return: Promise, который разрешается после добавления всех строк.
     */
    fu.appendDetailRows = function (parent, details, opts) {
        return Promise.resolve().then(() => {
            opts = opts || {};
            const chunkSize = opts.chunkSize || 1000;
            const begin = opts.begin || 0;
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
                return ;
            }
        });
    };

    /**
     * Обновляет таблицу с деталями.
     *
     * :param parent: Родительский элемент таблицы.
     * :param details: Массив объектов с деталями.
     * :param opts: Опции.
     * :return: Promise, который разрешается после обновления таблицы.
     */
    fu.updateDetailsTable = function (parent, details, opts) {
        opts = opts || {};
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
     * :param elem: Элемент.
     */
    fu.emptyChildNodes = function (elem) {
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild);
        }
    };

    /**
     * Сохраняет атрибут элемента.
     *
     * :param item: Элемент.
     * :param attr: Имя атрибута.
     * :param storage: Map для хранения атрибутов.
     * :param overwrite: Флаг перезаписи атрибута.
     * :return: Map с сохраненными атрибутами.
     */
    fu.saveAttrForItem = function(item, attr, storage, overwrite) {
        storage = storage || new Map();

        if (!fu.isElementItem(item)) {
            return storage;
        }

        let elemStor;
        if (storage.has(item)) {
            elemStor = storage.get(item);
        } else {
            elemStor = new Map();
            storage.set(item, elemStor);
        }

        const val = item.hasAttribute(attr) ? item.getAttribute(attr)
            : null;

        if (overwrite || !elemStor.has(attr)) {
            elemStor.set(attr, val);
        }

        return storage;
    };

    /**
     * Сохраняет атрибуты массива элементов.
     *
     * :param items: Массив элементов.
     * :param attr: Имя атрибута.
     * :param storage: Map для хранения атрибутов.
     * :param overwrite: Флаг перезаписи атрибута.
     * :return: Map с сохраненными атрибутами.
     */
    fu.saveAttrForItems = function(items, attr, storage, overwrite) {
        storage = storage || new Map();

        for (const item of items) {
            fu.saveAttrForItem(item, attr, storage, overwrite);
        }

        return storage;
    };

    /**
     * Восстанавливает атрибуты массива элементов.
     *
     * :param storage: Map с сохраненными атрибутами.
     */
    fu.restoreItemAttrs = function (storage) {
        for (const [elem, elemStor] of storage) {
            for (const [attr, value] of elemStor) {
                if (value === null) {
                    elem.removeAttribute(attr);
                } else {
                    elem.setAttribute(attr, value);
                }
            }
        }
    };

    /**
     * Получает предков фрейма.
     *
     * :param inds: Массив индексов фреймов.
     * :param win: Окно.
     * :return: Массив фреймов.
     *
     * :raises Error: Если фрейм не существует или нет доступа к нему.
     */
    fu.getFrameAncestry = function (inds, win) {
        win = win || window;

        const frames = [];
        for (let i = 0; i < inds.length; i++) {
            win = win.frames[inds[i]];
            if (!win) {
                throw new Error("The specified frame does not exist.");
            }
            let frame;
            try {
                frame = win.frameElement;
            } catch (e) {
                throw new Error("Access denied.");
            }
            frames.push(frame);
        }
        return frames;
    };

    /**
     * Проверяет, является ли массив числовым.
     *
     * :param arr: Массив для проверки.
     * :return: True, если массив числовой, False в противном случае.
     */
    fu.isNumberArray = function (arr) {
        if (!Array.isArray(arr)) {
            return false;
        }

        for (const item of arr) {
            if (typeof(item) !== "number") {
                return false;
            }
        }

        return