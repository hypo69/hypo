# Анализ кода модуля `try_xpath_functions.js`

**Качество кода: 7/10**
   -  **Плюсы:**
        - Код разбит на функции, что делает его более читаемым и поддерживаемым.
        - Используются строгие режимы (`"use strict"`).
        - Есть функции для работы с DOM, XPath и другими типами данных.
        - Проверка типов данных перед использованием.
        - Наличие функции для обработки ошибок `onError` .
   -  **Минусы:**
        - Отсутствует документация в формате reStructuredText (RST) для функций и переменных.
        - Обработка ошибок не всегда логируется, используется простой `console.log`.
        -  Много `try-catch` блоков без логирования ошибок, которые могут быть заменены на `logger.error`.
        -  Некоторые функции можно улучшить, например, `fu.listToArr` может быть заменен на `Array.from()`.
        -  Присутствуют устаревшие конструкции, такие как `var`, вместо `let` и `const`.

**Рекомендации по улучшению:**

1.  **Документация:**
    - Добавить docstring в формате RST ко всем функциям, методам и переменным.
    - Описать назначение каждого модуля.
2.  **Логирование:**
    - Использовать `from src.logger.logger import logger` для логирования ошибок.
    - Заменить `console.log(err)` на `logger.error(err)`.
    - Добавить логирование в `try-catch` блоки.
3.  **Рефакторинг:**
    - Использовать `let` и `const` вместо `var` там, где это возможно.
    - Упростить `fu.listToArr` с помощью `Array.from()`.
    - Проверить и улучшить производительность функций, которые обрабатывают большие объемы данных, таких как `appendDetailRows`.
    -  Устранить дублирование кода, например, в функциях `fu.saveAttrForItem` и `fu.saveAttrForItems`.
4.  **Обработка ошибок:**
    -  Избегать избыточного использования стандартных блоков `try-except`. Предпочитать обработку ошибок с помощью `logger.error`.
    -  Добавить более информативные сообщения об ошибках.
5. **Оптимизация:**
    -   Проверить и оптимизировать функции для работы с Map.
6. **Соответствие стандартам:**
    - Привести код к единому стилю, используя `ESLint` или `Prettier`.
    -  Соблюдать snake_case нотацию для переменных.
    - Проверить все импорты.

**Оптимизированный код:**

```javascript
/*
 * Модуль содержит функции для работы с XPath, DOM элементами, и преобразования данных.
 * ==================================================================================
 *
 *  Этот модуль предоставляет набор функций для выполнения XPath запросов, манипулирования
 *  DOM элементами, и преобразования различных типов данных.
 *
 *  Примеры использования:
 *  --------------------
 *  Пример выполнения XPath запроса:
 *
 *  .. code-block:: javascript
 *
 *      let result = tryxpath.functions.execExpr("//div", "evaluate", {context: document});
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
     * Выполняет XPath выражение или CSS селектор.
     *
     * :param expr: XPath выражение или CSS селектор.
     * :param method: Метод выполнения запроса: "evaluate", "querySelector", "querySelectorAll".
     * :param opts: Объект с опциями, такими как контекст, резолвер и тип результата.
     * :return: Объект с результатами запроса, методом и типом результата.
     *
     *  Примеры использования:
     *  --------------------
     *  Пример выполнения XPath запроса:
     *
     *  .. code-block:: javascript
     *
     *      let result = tryxpath.functions.execExpr("//div", "evaluate", {context: document});
     *      console.log(result.items);
     *
     *  Пример выполнения querySelector запроса:
     *
     *  .. code-block:: javascript
     *
     *      let result = tryxpath.functions.execExpr(".my-class", "querySelector", {context: document});
     *      console.log(result.items);
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
                    throw new Error("The context is neither Node nor Attr.");
                }
                const resolved = fu.makeResolver(resolver);
                resultType = opts.resultType || XPathResult.ANY_TYPE;
                let result;
                try{
                     result = doc.evaluate(expr, context, resolved, resultType, null);
                } catch (e) {
                    logger.error(`Ошибка выполнения xpath выражения ${expr}`, e);
                    return {
                        "items": [],
                        "method": method,
                        "resultType": null
                    };
                }
                items = fu.resToArr(result, resultType);
                if (resultType === XPathResult.ANY_TYPE) {
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
     * :param res: Результат XPath.
     * :param type: Тип результата.
     * :return: Массив элементов.
     */
    fu.resToArr = function (res, type) {
        if (type === undefined || (type === XPathResult.ANY_TYPE)) {
            type = res.resultType;
        }

        let arr = [];
        switch(type) {
            case XPathResult.NUMBER_TYPE :
                arr.push(res.numberValue);
                break;
            case XPathResult.STRING_TYPE :
                arr.push(res.stringValue);
                break;
            case XPathResult.BOOLEAN_TYPE :
                arr.push(res.booleanValue);
                break;
            case XPathResult.ORDERED_NODE_ITERATOR_TYPE :
            case XPathResult.UNORDERED_NODE_ITERATOR_TYPE :
                for (let node = res.iterateNext()
                    ; node !== null
                    ; node = res.iterateNext()) {
                    arr.push(node);
                }
                break;
            case XPathResult.ORDERED_NODE_SNAPSHOT_TYPE :
            case XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE :
                for (let i = 0; i < res.snapshotLength; i++) {
                    arr.push(res.snapshotItem(i));
                }
                break;
            case XPathResult.ANY_UNORDERED_NODE_TYPE :
            case XPathResult.FIRST_ORDERED_NODE_TYPE :
                arr.push(res.singleNodeValue);
                break;
            default :
                throw new Error("The resultType is invalid. " + type);
        }
        return arr;
    };
    /**
     * Создает резолвер пространства имен из объекта.
     *
     * :param obj: Объект или строка в формате JSON, представляющая пространство имен.
     * :return: Функция резолвера.
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
                logger.error(`Неверный резолвер ${obj}: ${e.message}`, e)
                return () => "";
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
         logger.error(`Неверный формат резолвера ${JSON.stringify(dict)}`)
         return () => "";
    };

    /**
     * Проверяет, является ли объект допустимым словарем.
     *
     * :param obj: Объект для проверки.
     * :return: True, если объект является допустимым словарем, иначе False.
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
     * :param obj: Объект для преобразования.
     * :return: Map, содержащий пары ключ-значение из объекта.
     */
    fu.objToMap = function (obj) {
        let map = new Map();
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
        if ((obj.nodeType === Node.ELEMENT_NODE) || (obj.nodeType === Node.DOCUMENT_NODE)) {
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
        return Array.from(list)
    };
    /**
     * Возвращает детали элемента.
     *
     * :param item: Элемент для анализа.
     * :return: Объект с деталями элемента.
     */
    fu.getItemDetail = function (item) {
        let typeStr = typeof(item);

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
     * Возвращает детали массива элементов.
     *
     * :param items: Массив элементов для анализа.
     * :return: Массив объектов с деталями элементов.
     */
    fu.getItemDetails = function (items) {
        let details = [];
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
     * Возвращает строковое представление типа узла.
     *
     * :param nodeType: Числовое значение типа узла.
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
            [XPathResult.ANY_TYPE, "ANY_TYPE"],
            [XPathResult.NUMBER_TYPE , "NUMBER_TYPE"],
            [XPathResult.STRING_TYPE , "STRING_TYPE"],
            [XPathResult.BOOLEAN_TYPE , "BOOLEAN_TYPE"],
            [XPathResult.UNORDERED_NODE_ITERATOR_TYPE ,
                "UNORDERED_NODE_ITERATOR_TYPE"],
            [XPathResult.ORDERED_NODE_ITERATOR_TYPE ,
                "ORDERED_NODE_ITERATOR_TYPE"],
            [XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE ,
                "UNORDERED_NODE_SNAPSHOT_TYPE"],
            [XPathResult.ORDERED_NODE_SNAPSHOT_TYPE ,
                "ORDERED_NODE_SNAPSHOT_TYPE"],
            [XPathResult.ANY_UNORDERED_NODE_TYPE, "ANY_UNORDERED_NODE_TYPE"],
            [XPathResult.FIRST_ORDERED_NODE_TYPE, "FIRST_ORDERED_NODE_TYPE"]
        ]),

        "strToNum" : new Map([
            ["ANY_TYPE", XPathResult.ANY_TYPE],
            ["NUMBER_TYPE", XPathResult.NUMBER_TYPE],
            ["STRING_TYPE", XPathResult.STRING_TYPE],
            ["BOOLEAN_TYPE", XPathResult.BOOLEAN_TYPE],
            ["UNORDERED_NODE_ITERATOR_TYPE",
                XPathResult.UNORDERED_NODE_ITERATOR_TYPE],
            ["ORDERED_NODE_ITERATOR_TYPE",
                XPathResult.ORDERED_NODE_ITERATOR_TYPE],
            ["UNORDERED_NODE_SNAPSHOT_TYPE",
                XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE],
            ["ORDERED_NODE_SNAPSHOT_TYPE",
                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE],
            ["ANY_UNORDERED_NODE_TYPE", XPathResult.ANY_UNORDERED_NODE_TYPE],
            ["FIRST_ORDERED_NODE_TYPE", XPathResult.FIRST_ORDERED_NODE_TYPE]
        ])
    };
    /**
     * Возвращает строковое представление типа результата XPath.
     *
     * :param resultType: Числовое значение типа результата XPath.
     * :return: Строковое представление типа результата XPath.
     */
    fu.getxpathResultStr = function (resultType) {
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType);
        }
        return "Unknown";
    };
    /**
     * Возвращает числовое представление типа результата XPath из строки.
     *
     * :param resultTypeStr: Строковое представление типа результата XPath.
     * :return: Числовое значение типа результата XPath.
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
     * Проверяет, является ли элемент элементом.
     *
     * :param item: Элемент для проверки.
     * :return: True, если элемент является элементом, иначе False.
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
     * :param clas: Имя класса для добавления.
     * :param item: Элемент, которому нужно добавить класс.
     */
    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };
    /**
     * Добавляет класс к массиву элементов.
     *
     * :param clas: Имя класса для добавления.
     * :param items: Массив элементов, которым нужно добавить класс.
     */
    fu.addClassToItems = function (clas, items) {
        for (let item of items) {
            fu.addClassToItem(clas, item);
        }
    };
    /**
     * Сохраняет оригинальный класс элемента.
     *
     * :param item: Элемент, класс которого нужно сохранить.
     * :return: Объект, содержащий элемент и его оригинальный класс.
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
     * Восстанавливает оригинальный класс элемента.
     *
     * :param savedClass: Объект, содержащий элемент и его оригинальный класс.
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
     * Сохраняет оригинальные классы массива элементов.
     *
     * :param items: Массив элементов, классы которых нужно сохранить.
     * :return: Массив объектов, содержащих элементы и их оригинальные классы.
     */
    fu.saveItemClasses = function (items) {
        let savedClasses = [];
        for (let item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };
    /**
     * Восстанавливает оригинальные классы массива элементов.
     *
     * :param savedClasses: Массив объектов, содержащих элементы и их оригинальные классы.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (let savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };
    /**
     * Устанавливает атрибут для элемента.
     *
     * :param name: Имя атрибута.
     * :param value: Значение атрибута.
     * :param item: Элемент, которому нужно установить атрибут.
     */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };
    /**
     * Удаляет атрибут из элемента.
     *
     * :param name: Имя атрибута для удаления.
     * :param item: Элемент, из которого нужно удалить атрибут.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };
    /**
     * Удаляет атрибут из массива элементов.
     *
     * :param name: Имя атрибута для удаления.
     * :param items: Массив элементов, из которых нужно удалить атрибут.
     */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };
    /**
     * Устанавливает индекс для массива элементов.
     *
     * :param name: Имя атрибута для установки индекса.
     * :param items: Массив элементов, которым нужно установить индекс.
     */
    fu.setIndexToItems = function(name, items) {
        for (let i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };
    /**
     * Возвращает родительский элемент.
     *
     * :param item: Элемент, для которого нужно получить родительский элемент.
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
     * Возвращает массив всех родительских элементов.
     *
     * :param elem: Элемент, для которого нужно получить массив родительских элементов.
     * :return: Массив родительских элементов.
     */
    fu.getAncestorElements = function (elem) {
        let ancs = [];

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
     * Возвращает документ, которому принадлежит элемент.
     *
     * :param item: Элемент, для которого нужно получить документ.
     * :return: Документ, которому принадлежит элемент.
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
     * :param values: Массив значений для заголовка.
     * :param opts: Объект с опциями, например, документ.
     * :return: Строка заголовка таблицы.
     */
    fu.createHeaderRow = function (values, opts) {
        opts = opts || {};
        const doc = opts.document || document;

        let tr = doc.createElement("tr");
        for (let value of values) {
            let th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };
    /**
     * Создает заголовок таблицы с деталями.
     *
     * :param opts: Объект с опциями, например, документ.
     * :return: Строка заголовка таблицы с деталями.
     */
    fu.createDetailTableHeader = function (opts) {
        opts = opts || {};
        const doc = opts.document || document;

        let tr = doc.createElement("tr");
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
     * :param index: Индекс элемента.
     * :param detail: Объект с деталями элемента.
     * :param opts: Объект с опциями, например, документ и ключи деталей.
     * :return: Строка таблицы с деталями.
     */
    fu.createDetailRow = function (index, detail, opts) {
        opts = opts || {};
        const doc = opts.document || document;
        const keys = opts.keys || ["type", "name", "value"];

        let tr = doc.createElement("tr");

        let td = doc.createElement("td");
        td.textContent = index;
        tr.appendChild(td);

        for (let key of keys) {
            let td = doc.createElement("td");
            td.textContent = detail[key];
            tr.appendChild(td);
        }

        td = doc.createElement("td");
        let button = doc.createElement("button");
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
     * :param opts: Объект с опциями, например, размер чанка, начало, конец, функция создания строки.
     * :return: Promise, который разрешается, когда все строки добавлены.
     */
    fu.appendDetailRows = function (parent, details, opts) {
        return Promise.resolve().then(() => {
            opts = opts || {};
            const chunkSize = opts.chunkSize || 1000;
            let begin = opts.begin || 0;
            const end = opts.end || details.length;
            const createRow = opts.createRow || fu.createDetailRow.bind(fu);
            const detailKeys = opts.detailKeys || undefined;

            const doc = parent.ownerDocument;
            const frag = doc.createDocumentFragment();
            let index = Math.max(begin, 0);
            let chunkEnd = Math.min(index + chunkSize, details.length, end);

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
     * :param opts: Объект с опциями, например, размер чанка, начало, конец, ключи деталей и значения заголовков.
     * :return: Promise, который разрешается, когда таблица обновлена.
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
     * Удаляет все дочерние узлы элемента.
     *
     * :param elem: Элемент, дочерние узлы которого нужно удалить.
     */
    fu.emptyChildNodes = function (elem) {
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild);
        }
    };
    /**
     * Сохраняет атрибут элемента.
     *
     * :param item: Элемент, атрибут которого нужно сохранить.
     * :param attr: Имя атрибута.
     * :param storage: Map для хранения атрибутов.
     * :param overwrite: Флаг, указывающий, нужно ли перезаписывать существующий атрибут.
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
      * Сохраняет атрибуты для массива элементов.
      *
      * :param items: Массив элементов, атрибуты которых нужно сохранить.
      * :param attr: Имя атрибута.
      * :param storage: Map для хранения атрибутов.
      * :param overwrite: Флаг, указывающий, нужно ли перезаписывать существующий атрибут.
      * :return: Map с сохраненными атрибутами.
      */
    fu.saveAttrForItems = function(items, attr, storage, overwrite) {
        storage = storage || new Map();

        for (let item of items) {
            fu.saveAttrForItem(item, attr, storage, overwrite);
        }

        return storage;
    };
    /**
     * Восстанавливает атрибуты элементов из хранилища.
     *
     * :param storage: Map с сохраненными атрибутами.
     */
    fu.restoreItemAttrs