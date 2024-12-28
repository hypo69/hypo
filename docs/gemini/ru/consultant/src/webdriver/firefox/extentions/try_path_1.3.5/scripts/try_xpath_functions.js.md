# Анализ кода модуля `try_xpath_functions.js`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используются namespace для предотвращения конфликтов имен.
    - Присутствует проверка на множественное выполнение.
    - Код содержит много полезных функций для работы с DOM и XPath.
    - Активно используются Map для хранения данных.
    - Есть функции для работы с фреймами.

-  Минусы
    - Не хватает docstring для функций и переменных.
    - Используются `try-catch` без логирования ошибок.
    - Есть места, где можно упростить код, например, использование `forEach` вместо циклов `for`.
    - Использование `console.log` для отладки (закомментировано), лучше использовать `logger`.
    - Не все функции возвращают значения явно.
    - Использование `undefined` вместо `null` в некоторых местах.

**Рекомендации по улучшению**

1. **Добавить docstring:**
   - Добавить docstring в формате reStructuredText (RST) для всех функций, переменных и констант.
   - Описать параметры, возвращаемые значения и назначение каждой функции.

2. **Использовать `logger`:**
   - Заменить `console.log` на `logger.debug` для отладки.
   - В `try-catch` блоках использовать `logger.error` для логирования ошибок и выводить информацию об исключении.

3. **Улучшить обработку ошибок:**
   - Вместо `try-catch` с пустым блоком использовать `logger.error` для логирования ошибок.
   - В функциях, которые возвращают `null`, явно указывать это в docstring.
   - Добавить проверки на наличие нужных свойств у объектов перед их использованием.

4. **Оптимизация кода:**
   - Использовать `for...of` вместо циклов `for` для итерации по массивам.
   - Избегать лишних проверок `undefined` и `null` там, где это не нужно.
   - Использовать `const` вместо `var` там, где это уместно.
   - Использовать  `Array.from(list)` вместо `fu.listToArr(list)`.
    
5. **Улучшить читаемость:**
    - Добавить комментарии к сложным участкам кода.
    - Привести код в соответствие с Python style guide.
6. **Привести в соответствие с другими файлами**
    -  Переименовать `fu` в `func`.
    -  Переименовать `tx` в `try_xpath`.

**Оптимизиробанный код**

```javascript
/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
/**
 * Модуль предоставляет набор функций для работы с XPath и DOM.
 * =========================================================================================
 *
 * Этот модуль содержит функции для выполнения XPath запросов,
 * получения информации об элементах DOM, работы с классами элементов,
 * сохранения и восстановления атрибутов, а также для работы с фреймами.
 *
 *
 * .. code-block:: javascript
 *
 *      // Пример использования функции для выполнения XPath
 *      let result = try_xpath.functions.execExpr('//div', 'querySelectorAll', {context: document});
 *      console.log(result.items);
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
    var try_xpath = tryxpath;
    var func = tryxpath.functions;
    
    from src.logger.logger import logger # импортируем logger

    // prevent multiple execution
    if (func.done) {
        return;
    }
    func.done = true;
    
    /**
     * Выполняет XPath выражение или запрос CSS.
     *
     * :param expr: XPath выражение или CSS селектор.
     * :param method: Метод выполнения запроса: "evaluate", "querySelector", "querySelectorAll".
     * :param opts: Объект с параметрами, такими как `context`, `resolver`, `document`, `resultType`.
     * :return: Объект с результатами запроса, содержащий массив `items`, метод запроса `method`, и тип результата `resultType`.
     * :raises Error: Если контекст не является узлом или атрибутом для метода "evaluate" или не является документом или элементом для "querySelector" или "querySelectorAll".
     *
     * .. code-block:: javascript
     *
     *   // Пример использования
     *   let result = func.execExpr('//div', 'querySelectorAll', {context: document});
     *   console.log(result.items);
     */
    func.execExpr = function(expr, method, opts) {
        opts = opts || {};
        var context = opts.context || document;
        var resolver = ("resolver" in opts) ? opts.resolver : null;
        var doc = opts.document || func.getOwnerDocument(context) || context;

        var items, resultType;

        switch (method) {
        case "evaluate":
            if (!func.isNodeItem(context) && !func.isAttrItem(context)) {
                logger.error("The context is either Nor nor Attr.");
                throw new Error("The context is either Nor nor Attr.");
            }
            resolver = func.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, resolver, resultType,
                                      null);
            items = func.resToArr(result, resultType);
            if (resultType === xpathResult.ANY_TYPE) {
                resultType = result.resultType;
            }
            break;

        case "querySelector":
            if (!func.isDocOrElem(context)) {
                logger.error("The context is either Document nor Element.");
                throw new Error("The context is either Document nor Element.");
            }
            let elem = context.querySelector(expr);
            items = elem ? [elem] : [];
            resultType = null;
            break;

        case "querySelectorAll":
        default:
            if (!func.isDocOrElem(context)) {
                logger.error("The context is neither Document nor Element.");
                throw new Error(
                    "The context is neither Document nor Element.");
            }
            let elems = context.querySelectorAll(expr);
            items = func.listToArr(elems);
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
     * :param res: Результат выполнения XPath запроса.
     * :param type: Тип результата XPath.
     * :return: Массив элементов, полученных из результата.
     * :raises Error: Если тип результата `resultType` не поддерживается.
     *
     * .. code-block:: javascript
     *
     *   // Пример использования
     *   let result = document.evaluate('//div', document, null, xpathResult.ORDERED_NODE_ITERATOR_TYPE, null);
     *   let arr = func.resToArr(result, xpathResult.ORDERED_NODE_ITERATOR_TYPE);
     *   console.log(arr);
     */
    func.resToArr = function (res, type) {
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
            logger.error(`The resultType is invalid. ${type}`);
            throw new Error("The resultType is invalid. " + type);
        }
        return arr;
    };
    
    /**
     * Создает функцию-резолвер для XPath из объекта или строки JSON.
     *
     * :param obj: Объект или строка JSON, представляющая пространство имен для резолвера.
     * :return: Функция-резолвер, используемая в `doc.evaluate`.
     * :raises Error: Если `obj` не является допустимым JSON или объектом.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *    let resolver = func.makeResolver('{"myprefix": "http://example.com"}');
     *   let result = document.evaluate('//myprefix:div', document, resolver, xpathResult.ANY_TYPE, null);
     */
    func.makeResolver = function (obj) {
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
                 logger.error(`Invalid resolver [${obj}]. : ${e.message}`);
                throw new Error("Invalid resolver [" + obj + "]. : "
                                + e.message);                
            }
        } else {
            dict = obj;
        }

        if (func.isValidDict(dict)) {
            let map = func.objToMap(dict);
            return function (str) {
                if (map.has(str)) {
                    return map.get(str);
                }
                return "";
            };
        }
        logger.error(`Invalid resolver. ${JSON.stringify(dict, null)}`);
        throw new Error("Invalid resolver. "
                        + JSON.stringify(dict, null));
    };

    /**
     * Проверяет, является ли объект допустимым словарем (объектом со строковыми значениями).
     *
     * :param obj: Проверяемый объект.
     * :return: `true`, если объект является допустимым словарем, `false` в противном случае.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let isValid = func.isValidDict({"key1": "value1", "key2": "value2"});
     *   console.log(isValid);
     */
    func.isValidDict = function (obj) {
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
     * :param obj: Исходный объект.
     * :return: Map, созданный на основе объекта.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *  let map = func.objToMap({"key1": "value1", "key2": "value2"});
     *   console.log(map);
     */
    func.objToMap = function (obj) {
        var map = new Map();
        Object.keys(obj).forEach(function(item) {
            map.set(item, obj[item]);
        });
        return map;
    };

    /**
     * Проверяет, является ли объект документом или элементом.
     *
     * :param obj: Проверяемый объект.
     * :return: `true`, если объект является документом или элементом, `false` в противном случае.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let isDocOrElem = func.isDocOrElem(document.body);
     *   console.log(isDocOrElem);
     */
    func.isDocOrElem = function(obj) {
        if ((obj.nodeType === 1) || (obj.nodeType === 9)) {
            return true;
        }
        return false;
    };

    /**
     * Преобразует NodeList в массив.
     *
     * :param list: NodeList для преобразования.
     * :return: Массив элементов, полученных из NodeList.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let nodeList = document.querySelectorAll('div');
     *   let array = func.listToArr(nodeList);
     *   console.log(array);
     */
    func.listToArr = function(list) {
         return Array.from(list);
    };

    /**
     * Возвращает подробную информацию об элементе DOM.
     *
     * :param item: Элемент DOM, для которого необходимо получить информацию.
     * :return: Объект с детальной информацией об элементе, включая тип, имя, значение и текстовое содержимое.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let detail = func.getItemDetail(document.body);
     *   console.log(detail);
     */
    func.getItemDetail = function (item) {
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
        if (func.isElementItem(item)) {
            return {
                "type": "Node " + func.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + item.nodeType + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            };
        }
        
        // item is Attr
        if (func.isAttrItem(item)) {
            return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            };
        }

        // item is Node
        return {
            "type": "Node " + func.getNodeTypeStr(item.nodeType) + "(nodeType="
                + item.nodeType + ")",
            "name": item.nodeName,
            "value": item.nodeValue || "",
            "textContent": item.textContent || ""
        };
    };

    /**
     * Возвращает массив подробной информации для массива элементов DOM.
     *
     * :param items: Массив элементов DOM.
     * :return: Массив объектов с подробной информацией о каждом элементе.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let items = document.querySelectorAll('div');
     *   let details = func.getItemDetails(items);
     *   console.log(details);
     */
    func.getItemDetails = function (items) {
        var details = [];
        for (var i = 0; i < items.length; i++) {
            details.push(func.getItemDetail(items[i]));
        }
        return details;
    };

    /**
     *  Сопоставление числовых кодов типов узлов с их строковыми представлениями.
     */
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
     * :param nodeType: Числовой код типа узла.
     * :return: Строковое представление типа узла.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let nodeTypeStr = func.getNodeTypeStr(Node.ELEMENT_NODE);
     *   console.log(nodeTypeStr);
     */
    func.getNodeTypeStr = function(nodeType) {
        if (nodeTypeMap.has(nodeType)) {
            return nodeTypeMap.get(nodeType);
        }
        return "Unknown";
    };

    /**
     * Сопоставление числовых и строковых представлений типов результатов XPath.
     */
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
     * :param resultType: Числовой код типа результата XPath.
     * :return: Строковое представление типа результата.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let resultTypeStr = func.getxpathResultStr(xpathResult.NUMBER_TYPE);
     *   console.log(resultTypeStr);
     */
    func.getxpathResultStr = function (resultType) {
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType);
        }
        return "Unknown";
    };

    /**
     * Получает числовой код типа результата XPath по его строковому представлению.
     *
     * :param resultTypeStr: Строковое представление типа результата XPath.
     * :return: Числовой код типа результата XPath.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *  let resultTypeNum = func.getxpathResultNum("NUMBER_TYPE");
     *   console.log(resultTypeNum);
     */
    func.getxpathResultNum = function (resultTypeStr) {
        if (xpathResultMaps.strToNum.has(resultTypeStr)) {
            return xpathResultMaps.strToNum.get(resultTypeStr);
        }
        return NaN;
    };

     /**
      * Проверяет, является ли элемент атрибутом.
      *
      * :param item: Элемент для проверки.
      * :return: `true`, если элемент является атрибутом, `false` в противном случае.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *   let isAttr = func.isAttrItem(document.body.attributes[0]);
      *  console.log(isAttr);
      */
    func.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };
    
    /**
      * Проверяет, является ли элемент узлом (не строкой или числом).
      *
      * :param item: Элемент для проверки.
      * :return: `true`, если элемент является узлом, `false` в противном случае.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *   let isNode = func.isNodeItem(document.body);
      *   console.log(isNode);
      */
    func.isNodeItem = function (item) {
        if (func.isAttrItem(item)) {
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
     * :return: `true`, если элемент является элементом DOM, `false` в противном случае.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let isElement = func.isElementItem(document.body);
     *   console.log(isElement);
     */
    func.isElementItem = function (item) {
        if (func.isNodeItem(item)
            && (item.nodeType === Node.ELEMENT_NODE)) {
            return true;
        }
        return false;
    };

    /**
      * Добавляет класс к элементу DOM.
      *
      * :param clas: Класс для добавления.
      * :param item: Элемент DOM.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *   func.addClassToItem('my-class', document.body);
      */
    func.addClassToItem = function (clas, item) {
        if (func.isElementItem(item)) {
            item.classList.add(clas);
        }
    };

    /**
      * Добавляет класс к массиву элементов DOM.
      *
      * :param clas: Класс для добавления.
      * :param items: Массив элементов DOM.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *   func.addClassToItems('my-class', document.querySelectorAll('div'));
      */
    func.addClassToItems = function (clas, items) {
        for (var item of items) {
            func.addClassToItem(clas, item);
        }
    };

    /**
     * Сохраняет исходный класс элемента DOM.
     *
     * :param item: Элемент DOM.
     * :return: Объект, содержащий элемент и его исходный класс.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *  let savedClass = func.saveItemClass(document.body);
     *   console.log(savedClass);
     */
    func.saveItemClass = function (item) {
        if (!func.isElementItem(item)) {
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
     * Восстанавливает исходный класс элемента DOM.
     *
     * :param savedClass: Объект, содержащий элемент и его исходный класс.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let savedClass = func.saveItemClass(document.body);
     *   func.restoreItemClass(savedClass);
     */
    func.restoreItemClass = function (savedClass) {
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
     * Сохраняет исходные классы массива элементов DOM.
     *
     * :param items: Массив элементов DOM.
     * :return: Массив объектов, содержащих элементы и их исходные классы.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *  let savedClasses = func.saveItemClasses(document.querySelectorAll('div'));
     *   console.log(savedClasses);
     */
    func.saveItemClasses = function (items) {
        var savedClasses = [];
        for (var item of items) {
            savedClasses.push(func.saveItemClass(item));
        }
        return savedClasses;
    };

    /**
     * Восстанавливает исходные классы массива элементов DOM.
     *
     * :param savedClasses: Массив объектов, содержащих элементы и их исходные классы.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let savedClasses = func.saveItemClasses(document.querySelectorAll('div'));
     *   func.restoreItemClasses(savedClasses);
     */
    func.restoreItemClasses = function (savedClasses) {
        for (var savedClass of savedClasses) {
            func.restoreItemClass(savedClass);
        }
    };
    
    /**
     * Устанавливает атрибут элементу DOM.
     *
     * :param name: Имя атрибута.
     * :param value: Значение атрибута.
     * :param item: Элемент DOM.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   func.setAttrToItem('data-test', '123', document.body);
     */
    func.setAttrToItem = function(name, value, item) {
        if (func.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    /**
      * Удаляет атрибут у элемента DOM.
      *
      * :param name: Имя атрибута для удаления.
      * :param item: Элемент DOM.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *  func.removeAttrFromItem('data-test', document.body);
      */
    func.removeAttrFromItem = function(name, item) {
        if (func.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };

    /**
      * Удаляет атрибут у массива элементов DOM.
      *
      * :param name: Имя атрибута для удаления.
      * :param items: Массив элементов DOM.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *  func.removeAttrFromItems('data-test', document.querySelectorAll('div'));
      */
    func.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            func.removeAttrFromItem(name, item);
        });
    };

    /**
     * Устанавливает атрибут индекса для каждого элемента в массиве.
     *
     * :param name: Имя атрибута.
     * :param items: Массив элементов DOM.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   func.setIndexToItems('data-index', document.querySelectorAll('div'));
     */
    func.setIndexToItems = function(name, items) {
        for (var i = 0; i < items.length; i++) {
            func.setAttrToItem(name, i, items[i]);
        }
    };

    /**
     * Получает родительский элемент DOM.
     *
     * :param item: Элемент DOM.
     * :return: Родительский элемент или `null`, если родитель не найден.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let parent = func.getParentElement(document.body);
     *   console.log(parent);
     */
    func.getParentElement = function (item) {
         if (func.isAttrItem(item)) {
            let parent = item.ownerElement;
            return parent || null;
        }

        if (func.isNodeItem(item)) {
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
     * Получает массив родительских элементов DOM элемента.
     *
     * :param elem: Элемент DOM.
     * :return: Массив родительских элементов DOM.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let ancestors = func.getAncestorElements(document.body);
     *   console.log(ancestors);
     */
    func.getAncestorElements = function (elem) {
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
      * Возвращает владельца документа для элемента DOM.
      *
      * :param item: Элемент DOM.
      * :return: Владелец документа или null, если документ не найден.
      *
      * .. code-block:: javascript
      *   // Пример использования
      *  let ownerDocument = func.getOwnerDocument(document.body);
      *   console.log(ownerDocument);
      */
    func.getOwnerDocument = function (item) {
         if (func.isAttrItem(item)) {
            let elem = item.ownerElement;
             if (elem) {
                return elem.ownerDocument;
            }
            return item.ownerDocument;
        }

        if (func.isNodeItem(item)) {
            return item.ownerDocument;
        }

        return null;
    };

    /**
     * Создает строку заголовка таблицы.
     *
     * :param values: Массив текстовых значений для ячеек заголовка.
     * :param opts: Объект с параметрами, такими как `document`.
     * :return: Строка `<tr>` с заголовками `<th>`.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let header = func.createHeaderRow(['Index', 'Type', 'Name'], {document: document});
     *   console.log(header);
     */
    func.createHeaderRow = function (values, opts) {
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
     * Создает строку заголовка таблицы с деталями элементов.
     *
     * :param opts: Объект с параметрами, такими как `document`.
     * :return: Строка `<tr>` с заголовками `<th>` для таблицы деталей.
     *
     * .. code-block:: javascript
     *   // Пример использования
     *   let header = func.createDetailTableHeader({document: document});
     *   console.log(header);
     */
    func.createDetailTableHeader = function (opts) {
        opts = opts || {};
        var doc = opts.document || document;

        var tr