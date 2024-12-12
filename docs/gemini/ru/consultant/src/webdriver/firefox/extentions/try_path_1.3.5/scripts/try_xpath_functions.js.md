# Анализ кода модуля `try_xpath_functions.js`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, функции логически разделены и выполняют конкретные задачи.
    - Использование `Map` для хранения данных, таких как `nodeTypeMap` и `xpathResultMaps`, улучшает производительность и читаемость.
    - Код соответствует стандартам JavaScript, включая использование `"use strict"`.
    - Присутствует обработка различных типов результатов XPath, что обеспечивает гибкость.
    - Код использует промисы для асинхронных операций.
- Минусы
    - Отсутствует явное документирование функций и переменных в формате reStructuredText (RST).
    - Присутствуют блоки try-catch без логирования ошибок.
    - Использование `console.log(err)` в `fu.onError` не подходит для продакшн среды, необходима замена на `logger.error`.
    - Некоторые функции, такие как `fu.onError`, могут быть более информативными.
    - Некоторые функции не имеют проверок на `null` или `undefined` перед их использованием, что может привести к ошибкам.
    - Передача `null` как значения по умолчанию в `fu.makeResolver` может вызвать неочевидное поведение.

**Рекомендации по улучшению**

1.  **Документирование**: Добавить docstring в формате reStructuredText (RST) для всех функций, переменных и модулей.
2.  **Логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок вместо блоков `try-catch` без обработки.
3.  **Обработка ошибок**: Улучшить обработку ошибок, добавив `logger.error` с подробным описанием ошибки.
4.  **Проверки на null/undefined**: Добавить проверки на `null` и `undefined` перед использованием переменных.
5.  **Уточнить параметры**: Сделать параметры функций более явными и понятными.
6.  **Улучшить читаемость**: Улучшить читаемость кода, разбив большие функции на более мелкие.

**Оптимизированный код**

```javascript
/*
 * Модуль для работы с XPath и DOM
 * =========================================================================================
 *
 * Этот модуль содержит набор функций для выполнения XPath-запросов и манипуляций с DOM.
 *
 * Функции предоставляют методы для выполнения запросов, преобразования результатов, работы с атрибутами и классами элементов, а также для сбора информации о фреймах.
 *
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
    var tx = tryxpath;
    var fu = tryxpath.functions;

    // prevent multiple execution
    if (fu.done) {
        return;
    }
    fu.done = true;
    
    /**
     * Выполняет XPath выражение или CSS селектор.
     *
     * :param expr: Выражение XPath или CSS селектор.
     * :param method: Метод выполнения запроса ("evaluate", "querySelector", "querySelectorAll").
     * :param opts: Опции запроса, включая контекст, резолвер и тип результата.
     * :return: Объект с результатами, методом и типом результата.
     *
     * :raises Error: Если контекст не является узлом или атрибутом, если передан неверный метод запроса, если контекст не является документом или элементом.
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
                throw new Error("The context is either Nor nor Attr.");
            }
            resolver = fu.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, resolver, resultType,
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
     * :return: Массив с результатами.
     * :raises Error: Если тип результата невалидный.
     */
    fu.resToArr = function (res, type) {
        if (type === undefined || (type === xpathResult.ANY_TYPE)) {
            type = res.resultType;
        }

        var arr = [];
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
            for (var node = res.iterateNext()
                 ; node !== null
                 ; node = res.iterateNext()) {
                arr.push(node);
            }
            break;
        case xpathResult.ORDERED_NODE_SNAPSHOT_TYPE :
        case xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE :
            for (var i = 0; i < res.snapshotLength; i++) {
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
     * Создаёт резолвер пространства имён.
     *
     * :param obj: Резолвер как объект, строка JSON или функция.
     * :return: Функция резолвера.
     * :raises Error: Если резолвер невалидный.
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
        throw new Error("Invalid resolver. "
                        + JSON.stringify(dict, null));
    };

    /**
     * Проверяет, является ли объект валидным словарём для резолвера.
     *
     * :param obj: Объект для проверки.
     * :return: True, если объект валидный словарь, иначе False.
     */
    fu.isValidDict = function (obj) {
        if ((obj === null) || (typeof(obj) !== "object")) {
            return false;
        }
        for (var key of Object.keys(obj)) {
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
     * :return: Map с данными из объекта.
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
     * :param obj: Объект для проверки.
     * :return: True, если объект является документом или элементом, иначе False.
     */
    fu.isDocOrElem = function(obj) {
        if ((obj && obj.nodeType === 1) || (obj && obj.nodeType === 9)) {
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
        var elems = [];
        for (var i = 0; i < list.length; i++) {
            elems.push(list[i]);
        }
        return elems;
    };

    /**
     * Возвращает детали элемента.
     *
     * :param item: Элемент для получения деталей.
     * :return: Объект с типом, именем, значением и текстом элемента.
     */
    fu.getItemDetail = function (item) {
        var typeStr = typeof(item);

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
     * Возвращает детали для массива элементов.
     *
     * :param items: Массив элементов.
     * :return: Массив объектов с деталями элементов.
     */
    fu.getItemDetails = function (items) {
        var details = [];
        for (var i = 0; i < items.length; i++) {
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
     * Возвращает строку, представляющую тип узла.
     *
     * :param nodeType: Тип узла.
     * :return: Строка с названием типа узла.
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
     * Возвращает строку, представляющую тип результата XPath.
     *
     * :param resultType: Тип результата XPath.
     * :return: Строка с названием типа результата.
     */
    fu.getxpathResultStr = function (resultType) {
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType);
        }
        return "Unknown";
    };

     /**
     * Возвращает число, представляющее тип результата XPath.
     *
     * :param resultTypeStr: Строка с названием типа результата XPath.
     * :return: Число с типом результата.
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
     * :return: True, если элемент является атрибутом, иначе False.
     */
    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };

    /**
     * Проверяет, является ли элемент узлом.
     *
     * :param item: Элемент для проверки.
     * :return: True, если элемент является узлом, иначе False.
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
     * :return: True, если элемент является элементом DOM, иначе False.
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
     * :param clas: Название класса.
     * :param item: Элемент для добавления класса.
     */
    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };

    /**
     * Добавляет класс к массиву элементов.
     *
     * :param clas: Название класса.
     * :param items: Массив элементов.
     */
    fu.addClassToItems = function (clas, items) {
        for (var item of items) {
            fu.addClassToItem(clas, item);
        }
    };

    /**
     * Сохраняет класс элемента.
     *
     * :param item: Элемент для сохранения класса.
     * :return: Объект с элементом и оригинальным классом.
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
     * :param savedClass: Объект с сохранённым классом.
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
     * :return: Массив объектов с сохранёнными классами.
     */
    fu.saveItemClasses = function (items) {
        var savedClasses = [];
        for (var item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };

    /**
     * Восстанавливает классы массива элементов.
     *
     * :param savedClasses: Массив объектов с сохранёнными классами.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (var savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };

    /**
     * Устанавливает атрибут элементу.
     *
     * :param name: Название атрибута.
     * :param value: Значение атрибута.
     * :param item: Элемент для установки атрибута.
     */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    /**
     * Удаляет атрибут из элемента.
     *
     * :param name: Название атрибута.
     * :param item: Элемент для удаления атрибута.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };

     /**
     * Удаляет атрибут из массива элементов.
     *
     * :param name: Название атрибута.
     * :param items: Массив элементов для удаления атрибута.
     */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };

     /**
     * Устанавливает индекс как атрибут элементам.
     *
     * :param name: Название атрибута.
     * :param items: Массив элементов для установки индекса.
     */
    fu.setIndexToItems = function(name, items) {
        for (var i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };

    /**
     * Возвращает родительский элемент.
     *
     * :param item: Элемент, для которого необходимо найти родителя.
     * :return: Родительский элемент или null.
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
     * Возвращает список родительских элементов.
     *
     * :param elem: Элемент, для которого необходимо найти предков.
     * :return: Массив родительских элементов.
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
        while (parent && (parent.nodeType === Node.ELEMENT_NODE)) {
            ancs.push(cur);
            cur = parent;
            parent = cur.parentNode;
        }
        
        return ancs;
    };

    /**
     * Возвращает объект документа для элемента.
     *
     * :param item: Элемент, для которого необходимо получить документ.
     * :return: Объект документа или null.
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
     * Создаёт строку заголовка таблицы.
     *
     * :param values: Массив значений для ячеек заголовка.
     * :param opts: Опции, например document.
     * :return: Строка заголовка таблицы.
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
     * Создаёт строку заголовка таблицы с деталями.
     *
     * :param opts: Опции, например document.
     * :return: Строка заголовка таблицы с деталями.
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
     * Создаёт строку таблицы с деталями элемента.
     *
     * :param index: Индекс элемента.
     * :param detail: Объект с деталями элемента.
     * :param opts: Опции, например document и ключи.
     * :return: Строка таблицы с деталями элемента.
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
     * Добавляет строки с деталями в таблицу.
     *
     * :param parent: Родительский элемент таблицы.
     * :param details: Массив объектов с деталями.
     * :param opts: Опции, например размер чанка, начало, конец, ключи.
     * :return: Промис, разрешающийся после добавления всех строк.
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
                return ;
            }
        });
    };

    /**
     * Обновляет таблицу с деталями.
     *
     * :param parent: Родительский элемент таблицы.
     * :param details: Массив объектов с деталями.
     * :param opts: Опции, например размер чанка, начало, конец, ключи, значения заголовков.
     * :return: Промис, разрешающийся после обновления таблицы.
     */
    fu.updateDetailsTable = function (parent, details, opts) {
        opts = opts || {};
        var chunkSize = opts.chunkSize || 1000;
        var begin = opts.begin || 0;
        var end = opts.end || details.length;
        var detailKeys = opts.detailKeys || undefined;
        var headerValues;
        if (opts.headerValues) {
            headerValues = ["Index"].concat(opts.headerValues, ["Focus"]);
        } else {
            headerValues = ["Index", "Type", "Name", "Value", "Focus"];
        }

        var doc = parent.ownerDocument;

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
     * Очищает дочерние узлы элемента.
     *
     * :param elem: Элемент для очистки.
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
     * :param attr: Название атрибута.
     * :param storage: Хранилище атрибутов.
     * :param overwrite: Флаг перезаписи.
     * :return: Хранилище атрибутов.
     */
    fu.saveAttrForItem = function(item, attr, storage, overwrite) {
        storage = storage || new Map();
        
        if (!fu.isElementItem(item)) {
            return storage;
        }

        var elemStor;
        if (storage.has(item)) {
            elemStor = storage.get(item);
        } else {
            elemStor = new Map();
            storage.set(item, elemStor);
        }
        
        var val = item.hasAttribute(attr) ? item.getAttribute(attr)
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
     * :param attr: Название атрибута.
     * :param storage: Хранилище атрибутов.
     * :param overwrite: Флаг перезаписи.
     * :return: Хранилище атрибутов.
     */
    fu.saveAttrForItems = function(items, attr, storage, overwrite) {
        storage = storage || new Map();

        for (var item of items) {
            fu.saveAttrForItem(item, attr, storage, overwrite);
        }

        return storage;
    };

    /**
     * Восстанавливает атрибуты элементов.
     *
     * :param storage: Хранилище атрибутов.
     */
    fu.restoreItemAttrs = function (storage) {
        for (var [elem, elemStor] of storage) {
            for (var [attr, value] of elemStor) {
                if (value === null) {
                    elem.removeAttribute(attr);
                } else {
                    elem.setAttribute(attr, value);
                }
            }
        }
    };

    /**
     * Возвращает массив фреймов на основе индексов.
     *
     * :param inds: Массив индексов фреймов.
     * :param win: Окно, в котором ищем фреймы.
     * :return: Массив фреймов.
     * :raises Error: Если фрейм не существует или отказано в доступе.
     */
    fu.getFrameAncestry = function (inds, win) {
        win = win || window;

        var frames = [];
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
        };
        return frames;
    };

    /**
     * Проверяет, является ли массив массивом чисел.
     *
     * :param arr: Массив для проверки.
     * :return: True, если массив пустой или содержит только числа, иначе False.
     */
    fu.isNumberArray = function (arr) {
        if (!Array.isArray(arr)) {
            return false;
        }

        for (var item of arr) {
            if