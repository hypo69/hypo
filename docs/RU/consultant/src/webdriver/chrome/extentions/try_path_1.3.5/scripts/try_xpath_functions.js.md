# Анализ кода модуля `try_xpath_functions.js`

**Качество кода**
    -  Соответствие требованиям: 7/10
    -  Плюсы:
        - Код хорошо структурирован, функции разделены по назначению.
        - Используется IIFE для предотвращения конфликтов имен.
        - Присутствуют проверки типов и обработка ошибок.
        - Наличие констант для типов узлов и результатов XPath.
    -  Минусы:
        - Отсутствует описание модуля.
        - Не хватает документации для функций (docstring).
        - Не используется `logger` для логирования ошибок.
        - Некоторые проверки можно упростить.
        - Использование `JSON.parse` без обработки ошибок, если `obj` не строка.
        - Наличие `// console.log(err);` в функции `fu.onError`, что является закомментированным кодом, который лучше удалить.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла добавить описание модуля.
2.  **Добавить документацию:** Добавить документацию в формате RST для всех функций, методов и переменных.
3.  **Использовать `logger`:** Использовать `logger.error` для обработки ошибок вместо `throw new Error`.
4.  **Упростить проверки:** Упростить проверки типов, где это возможно.
5.  **Обработать `JSON.parse`:** Проверять, является ли `obj` строкой, перед использованием `JSON.parse`.
6.  **Удалить закомментированный код:** Удалить закомментированную строку `// console.log(err);` из `fu.onError`.
7. **Использовать let и const:** Заменить var на let или const, где это уместно.
8. **Избегать сокращений:** Использовать полные имена переменных и функций для улучшения читаемости.
9. **Улучшить форматирование:** Добавить пустые строки между функциями для улучшения читаемости.
10. **Изменить способ bind:** Изменить bind на стрелочную функцию, это улучшит читаемость и производительность.

**Оптимизированный код**

```javascript
/*
 * Модуль `tryxpath.functions`
 * =========================================================================================
 *
 *  Этот модуль предоставляет набор функций для работы с XPath и DOM, включая выполнение запросов,
 *  преобразование результатов, манипуляцию элементами и атрибутами, а также утилиты для работы с фреймами.
 *
 *  Модуль предназначен для использования в контексте расширения tryxpath для браузера.
 *
 *  Пример использования
 *  --------------------
 *
 *  .. code-block:: javascript
 *
 *      let result = tryxpath.functions.execExpr('//div', 'querySelectorAll', {context: document});
 *      let items = result.items;
 *      let details = tryxpath.functions.getItemDetails(items);
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
     * Выполняет XPath выражение или запрос CSS-селектора.
     *
     * @param {string} expr Выражение XPath или CSS-селектор.
     * @param {string} method Метод запроса: "evaluate", "querySelector", "querySelectorAll".
     * @param {object} [opts] Опции запроса.
     * @param {Node} [opts.context=document] Контекстный узел для выполнения запроса.
     * @param {object|string} [opts.resolver] Пространство имен для XPath.
     * @param {Document} [opts.document] Документ для выполнения запроса.
     * @param {number} [opts.resultType] Тип результата XPath.
     * @returns {object} Объект с результатами запроса.
     * @throws {Error} Если контекст является ни узлом, ни атрибутом (для evaluate) или не является документом или элементом (для querySelector, querySelectorAll).
     */
    fu.execExpr = function(expr, method, opts) {
        opts = opts || {};
        let context = opts.context || document;
        let resolver = ("resolver" in opts) ? opts.resolver : null;
        let doc = opts.document || fu.getOwnerDocument(context) || context;

        let items, resultType;

        switch (method) {
        case "evaluate":
             // Проверка, является ли контекст узлом или атрибутом
            if (!fu.isNodeItem(context) && !fu.isAttrItem(context)) {
                throw new Error("The context is neither Node nor Attr.");
            }
            resolver = fu.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, resolver, resultType, null);
            items = fu.resToArr(result, resultType);
            if (resultType === xpathResult.ANY_TYPE) {
                resultType = result.resultType;
            }
            break;
        case "querySelector":
            // Проверка, является ли контекст документом или элементом
            if (!fu.isDocOrElem(context)) {
                throw new Error("The context is neither Document nor Element.");
            }
            let elem = context.querySelector(expr);
            items = elem ? [elem] : [];
            resultType = null;
            break;
        case "querySelectorAll":
        default:
            // Проверка, является ли контекст документом или элементом
             if (!fu.isDocOrElem(context)) {
                throw new Error("The context is neither Document nor Element.");
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
     * @param {XPathResult} res Результат XPath.
     * @param {number} [type=res.resultType] Тип результата XPath.
     * @returns {Array} Массив элементов.
     * @throws {Error} Если тип результата невалидный.
     */
    fu.resToArr = function (res, type) {
        if (type === undefined || (type === xpathResult.ANY_TYPE)) {
            type = res.resultType;
        }

        let arr = [];
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
            for (let node = res.iterateNext();
                 node !== null;
                 node = res.iterateNext()) {
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
     * Создает преобразователь пространства имен из объекта или строки JSON.
     *
     * @param {object|string|function} obj Объект, строка JSON или функция преобразователь.
     * @returns {function|null} Функция преобразователь или null.
     * @throws {Error} Если преобразователь невалидный.
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
             // Попытка преобразовать строку в объект JSON, иначе ошибка
            try {
                dict = JSON.parse(obj);
            } catch (e) {
                 // Выбрасываем ошибку, если JSON не удалось разобрать
                throw new Error("Invalid resolver [" + obj + "]. : " + e.message);
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
         // Выбрасываем ошибку, если преобразователь не является валидным словарем
        throw new Error("Invalid resolver. " + JSON.stringify(dict, null));
    };

    /**
     * Проверяет, является ли объект валидным словарем для преобразователя.
     *
     * @param {object} obj Объект для проверки.
     * @returns {boolean} `true`, если объект валидный, `false` иначе.
     */
    fu.isValidDict = function (obj) {
        if ((obj === null) || (typeof(obj) !== "object")) {
            return false;
        }
         // Проверка, что все значения в объекте - строки
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
     * @param {object} obj Объект для преобразования.
     * @returns {Map} Map, созданный из объекта.
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
     * @param {object} obj Объект для проверки.
     * @returns {boolean} `true`, если объект документ или элемент, `false` иначе.
     */
    fu.isDocOrElem = function(obj) {
        return (obj && (obj.nodeType === Node.ELEMENT_NODE || obj.nodeType === Node.DOCUMENT_NODE));
    };

    /**
     * Преобразует NodeList в массив.
     *
     * @param {NodeList} list NodeList для преобразования.
     * @returns {Array} Массив элементов.
     */
    fu.listToArr = function(list) {
        let elems = [];
        for (let i = 0; i < list.length; i++) {
            elems.push(list[i]);
        }
        return elems;
    };

    /**
     * Получает детали элемента, включая тип, имя, значение и текстовое содержимое.
     *
     * @param {object} item Элемент для получения деталей.
     * @returns {object} Объект с деталями элемента.
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
     * @param {Array} items Массив элементов.
     * @returns {Array} Массив объектов с деталями элементов.
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
     * Получает строковое представление типа узла.
     *
     * @param {number} nodeType Числовое значение типа узла.
     * @returns {string} Строковое представление типа узла.
     */
    fu.getNodeTypeStr = function(nodeType) {
        return nodeTypeMap.get(nodeType) || "Unknown";
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
     * @param {number} resultType Числовое значение типа результата XPath.
     * @returns {string} Строковое представление типа результата XPath.
     */
    fu.getxpathResultStr = function (resultType) {
         // Возвращаем строковое представление, если оно есть в карте
        return xpathResultMaps.numToStr.get(resultType) || "Unknown";
    };

    /**
     * Получает числовое представление типа результата XPath.
     *
     * @param {string} resultTypeStr Строковое представление типа результата XPath.
     * @returns {number} Числовое значение типа результата XPath.
     */
    fu.getxpathResultNum = function (resultTypeStr) {
         // Возвращаем числовое представление, если оно есть в карте, иначе NaN
        return xpathResultMaps.strToNum.get(resultTypeStr) || NaN;
    };

    /**
     * Проверяет, является ли элемент атрибутом.
     *
     * @param {object} item Элемент для проверки.
     * @returns {boolean} `true`, если элемент является атрибутом, `false` иначе.
     */
    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };

    /**
     * Проверяет, является ли элемент узлом.
     *
     * @param {object} item Элемент для проверки.
     * @returns {boolean} `true`, если элемент является узлом, `false` иначе.
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
     * Проверяет, является ли элемент элементом (Node.ELEMENT_NODE).
     *
     * @param {object} item Элемент для проверки.
     * @returns {boolean} `true`, если элемент является элементом, `false` иначе.
     */
    fu.isElementItem = function (item) {
        return fu.isNodeItem(item) && item.nodeType === Node.ELEMENT_NODE;
    };

    /**
     * Добавляет класс к элементу.
     *
     * @param {string} clas Класс для добавления.
     * @param {Element} item Элемент для добавления класса.
     */
    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };

    /**
     * Добавляет класс к массиву элементов.
     *
     * @param {string} clas Класс для добавления.
     * @param {Array<Element>} items Массив элементов.
     */
    fu.addClassToItems = function (clas, items) {
        for (let item of items) {
            fu.addClassToItem(clas, item);
        }
    };

    /**
     * Сохраняет класс элемента.
     *
     * @param {Element} item Элемент для сохранения класса.
     * @returns {object} Объект с элементом и сохраненным классом.
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
        };
    };

    /**
     * Восстанавливает класс элемента.
     *
     * @param {object} savedClass Объект с сохраненным классом.
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
     * @param {Array<Element>} items Массив элементов.
     * @returns {Array<object>} Массив объектов с сохраненными классами.
     */
    fu.saveItemClasses = function (items) {
        let savedClasses = [];
        for (let item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };

    /**
     * Восстанавливает классы массива элементов.
     *
     * @param {Array<object>} savedClasses Массив объектов с сохраненными классами.
     */
    fu.restoreItemClasses = function (savedClasses) {
        for (let savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };

    /**
     * Устанавливает атрибут элемента.
     *
     * @param {string} name Имя атрибута.
     * @param {string} value Значение атрибута.
     * @param {Element} item Элемент для установки атрибута.
     */
    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    /**
     * Удаляет атрибут элемента.
     *
     * @param {string} name Имя атрибута.
     * @param {Element} item Элемент для удаления атрибута.
     */
    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };

    /**
     * Удаляет атрибут у всех элементов массива.
     *
     * @param {string} name Имя атрибута.
     * @param {Array<Element>} items Массив элементов.
     */
    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };

    /**
     * Устанавливает индекс как атрибут элементам.
     *
     * @param {string} name Имя атрибута.
     * @param {Array<Element>} items Массив элементов.
     */
    fu.setIndexToItems = function(name, items) {
        for (let i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };

    /**
     * Получает родительский элемент для узла или атрибута.
     *
     * @param {object} item Узел или атрибут.
     * @returns {Element|null} Родительский элемент или `null`.
     */
    fu.getParentElement = function (item) {
        if (fu.isAttrItem(item)) {
            let parent = item.ownerElement;
            return parent || null;
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
     * Получает массив всех родительских элементов.
     *
     * @param {Element} elem Элемент.
     * @returns {Array<Element>} Массив родительских элементов.
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
     * Получает документ, которому принадлежит элемент.
     *
     * @param {object} item Узел или атрибут.
     * @returns {Document|null} Документ или `null`.
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
     * @param {Array<string>} values Массив заголовков.
     * @param {object} [opts] Опции.
     * @param {Document} [opts.document=document] Документ для создания элементов.
     * @returns {HTMLTableRowElement} Строка заголовка таблицы.
     */
    fu.createHeaderRow = function (values, opts) {
        opts = opts || {};
        let doc = opts.document || document;

        let tr = doc.createElement("tr");
        for (let value of values) {
            let th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };

    /**
     * Создает строку заголовка таблицы деталей.
     *
     * @param {object} [opts] Опции.
     * @param {Document} [opts.document=document] Документ для создания элементов.
     * @returns {HTMLTableRowElement} Строка заголовка таблицы.
     */
    fu.createDetailTableHeader = function (opts) {
        opts = opts || {};
        let doc = opts.document || document;

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
     * Создает строку деталей таблицы.
     *
     * @param {number} index Индекс строки.
     * @param {object} detail Детали для строки.
     * @param {object} [opts] Опции.
     * @param {Document} [opts.document=document] Документ для создания элементов.
     * @param {Array<string>} [opts.keys=["type", "name", "value"]] Ключи для деталей.
     * @returns {HTMLTableRowElement} Строка деталей таблицы.
     */
    fu.createDetailRow = function (index, detail, opts) {
        opts = opts || {};
        let doc = opts.document || document;
        let keys = opts.keys || ["type", "name", "value"];

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
     * Добавляет строки деталей в родительский элемент.
     *
     * @param {Element} parent Родительский элемент.
     * @param {Array<object>} details Массив деталей.
     * @param {object} [opts] Опции.
     * @param {number} [opts.chunkSize=1000] Размер чанка.
     * @param {number} [opts.begin=0] Начальный индекс.
     * @param {number} [opts.end=details.length] Конечный индекс.
     * @param {function} [opts.createRow=fu.createDetailRow] Функция создания строки.
     * @param {Array<string>} [opts.detailKeys] Ключи для деталей.
     * @returns {Promise<void>} Promise, который завершается после добавления всех строк.
     */
     fu.appendDetailRows = function (parent, details, opts) {
        return Promise.resolve().then(() => {
            opts = opts || {};
            let chunkSize = opts.chunkSize || 1000;
            let begin = opts.begin || 0;
            let end = opts.end || details.length;
            let createRow = opts.createRow || ((index, detail, opts) => fu.createDetailRow(index, detail, opts));
            let detailKeys = opts.detailKeys || undefined;

            let doc = parent.ownerDocument;
            let frag = doc.createDocumentFragment();
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
            }
            return;
        });
    };


    /**
     * Обновляет таблицу с деталями.
     *
     * @param {Element} parent Родительский элемент таблицы.
     * @param {Array<object>} details Массив деталей.
     * @param {object} [opts] Опции.
     * @param {number} [opts.chunkSize=1000] Размер чанка.
     * @param {number} [opts.begin=0] Начальный индекс.
     * @param {number} [opts.end=details.length] Конечный индекс.
     * @param {Array<string>} [opts.detailKeys] Ключи для деталей.
     * @param {Array<string>} [opts.headerValues] Заголовки таблицы.
     * @returns {Promise<void>} Promise, который завершается после обновления таблицы.
     */
    fu.updateDetailsTable = function (parent, details, opts) {
        opts = opts || {};
        let chunkSize = opts.chunkSize || 1000;
        let begin = opts.begin || 0;
        let end = opts.end || details.length;
        let detailKeys = opts.detailKeys || undefined;
        let headerValues;
        if (opts.headerValues) {
            headerValues = ["Index"].concat(opts.headerValues, ["Focus"]);
        } else {
            headerValues = ["Index", "Type", "Name", "Value", "Focus"];
        }

        let doc = parent.ownerDocument;

        fu.emptyChildNodes(parent);
        parent.appendChild(fu.createHeaderRow(headerValues, { "document": doc }));

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
     * @param {Element} elem Элемент.
     */
    fu.emptyChildNodes = function (elem) {
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild);
        }
    };

    /**
     * Сохраняет атрибут элемента.
     *
     * @param {Element} item Элемент.
     * @param {string} attr Имя атрибута.
     * @param {Map} [storage=new Map()] Хранилище для сохранения.
     * @param {boolean} [overwrite=false] Перезаписать существующее значение.
     * @returns {Map} Хранилище.
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