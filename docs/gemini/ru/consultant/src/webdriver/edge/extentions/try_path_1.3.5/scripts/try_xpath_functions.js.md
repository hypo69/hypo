# Анализ кода модуля try_xpath_functions.js

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    - Используются константы для типов узлов и результатов XPath, что делает код более читаемым и менее подверженным ошибкам.
    -  Присутствуют проверки типов и ошибок, что помогает предотвратить неожиданное поведение.
    -  Есть функции для сохранения и восстановления классов и атрибутов элементов, что полезно для временных изменений DOM.
    -  Используется `Map` для хранения соответствий, что обеспечивает эффективный доступ к данным.
- Минусы
    -  Не хватает документации в формате RST для функций и модуля.
    -  Присутствуют стандартные блоки `try-except`, которые можно заменить на логирование ошибок.
    -  Не все функции имеют четкое описание своей работы.
    -  Некоторые функции, такие как `fu.onError`, пустые и не используются.
    -  В некоторых местах используется `var` вместо `let` или `const`.
    - Отсутствует обработка возможных ошибок при работе с `document` и DOM-элементами.
    - Есть потенциальные проблемы с производительностью при работе с большими наборами данных (необходимо использовать более эффективные методы).

**Рекомендации по улучшению**
1. Добавить reStructuredText (RST) комментарии для модуля и всех функций, переменных.
2. Заменить стандартные блоки `try-except` на использование `logger.error` для логирования ошибок.
3. Добавить проверки на существование DOM-элементов перед их использованием.
4. Использовать `let` и `const` вместо `var` для объявления переменных.
5. Использовать асинхронные операции и Promise API для работы с большими наборами данных, например, для `fu.appendDetailRows`.
6. Использовать более итеративный подход для `fu.emptyChildNodes`, избегая рекурсивных вызовов, которые могут привести к проблемам со стеком.
7. Устранить неиспользуемый метод `fu.onError`.
8. Добавить обработку ошибок при обращении к свойствам DOM-элементов.
9. Добавить описание для переменных, особенно констант.
10. Оптимизировать работу с DOM, избегать лишних операций чтения/записи.

**Оптимизиробанный код**
```python
"""
Модуль для работы с XPath и DOM
=========================================================================================

Этот модуль предоставляет набор функций для выполнения XPath-запросов,
манипулирования DOM-элементами и получения информации о них.

Функции включают в себя выполнение XPath-выражений, преобразование результатов,
работу с атрибутами и классами элементов, а также управление табличным представлением данных.

Пример использования
--------------------

.. code-block:: javascript

    // Получение элементов по XPath
    let result = tryxpath.functions.execExpr('//div', 'evaluate', { context: document });
    console.log(result.items);

    // Получение деталей элемента
    let detail = tryxpath.functions.getItemDetail(document.body);
    console.log(detail);

    // Обновление таблицы с деталями элементов
    let parent = document.getElementById('results');
    tryxpath.functions.updateDetailsTable(parent, [detail]);
"""
from src.logger.logger import logger
import json
# namespace
if not 'tryxpath' in globals():
    tryxpath = {}
if not 'functions' in tryxpath:
    tryxpath.functions = {}

(lambda window, undefined: {
    "use strict": True,

    # alias
    "tx": tryxpath,
    "fu": tryxpath.functions,

    # prevent multiple execution
    "if": fu.done if "done" in fu else None,
    "if_not_done": lambda: None if not "done" in fu else fu.done,
    "done":  lambda:  (lambda: setattr(fu, "done", True))() if "done" not in fu else None,
    "not_done": lambda: (lambda: setattr(fu, "done", True))() if "done" not in fu else None,
    "func": lambda: None if "done" in fu else (lambda: setattr(fu, "done", True))(),

    lambda: None if "done" in fu else (lambda: setattr(fu, "done", True))(),

    """
    Выполняет XPath-выражение или CSS-селектор.
    
    :param expr: Выражение XPath или CSS-селектор.
    :type expr: str
    :param method: Метод выполнения: "evaluate" для XPath, "querySelector" или "querySelectorAll" для CSS-селекторов.
    :type method: str
    :param opts: Дополнительные параметры, включая контекст, резолвер и тип результата.
    :type opts: dict
    :return: Объект с результатами, методом и типом результата.
    :rtype: dict
    """
    "execExpr": lambda expr, method, opts={}: (lambda: {
        "opts": opts or {},
        "context": opts.get("context", window.document),
        "resolver": opts.get("resolver", None),
        "doc": opts.get("document", fu.getOwnerDocument(opts.get("context", window.document)) or window.document),
        "items": None,
        "resultType": None,
        "case_evaluate": lambda: (lambda: {
            "check_context": lambda: (lambda: {
                "is_context_invalid": lambda: not fu.isNodeItem(opts.get("context", window.document)) and not fu.isAttrItem(opts.get("context", window.document)),
                "check": lambda: None if not (not fu.isNodeItem(opts.get("context", window.document)) and not fu.isAttrItem(opts.get("context", window.document))) else (lambda: setattr(fu,"error_context", logger.error("The context is neither Node nor Attr.")))()
                })(),
            "make_resolver": lambda: setattr(fu,"resolver", fu.makeResolver(opts.get("resolver",None))),
            "resultType":  lambda:  setattr(fu,"resultType", opts.get("resultType", xpathResult.ANY_TYPE)),
            "evaluate": lambda: (lambda: setattr(fu,"result",fu.doc.evaluate(expr, fu.context, fu.resolver, fu.resultType, None) if not fu.error_context else None))(),
            "res_to_arr": lambda: setattr(fu, "items", fu.resToArr(fu.result, fu.resultType) if not fu.error_context else []) ,
            "resultType_if": lambda: setattr(fu,"resultType", fu.result.resultType if not fu.error_context else None) if fu.resultType == xpathResult.ANY_TYPE else None
            })(),
        "case_querySelector": lambda: (lambda: {
           "check_context": lambda: (lambda: {
                "is_context_invalid": lambda: not fu.isDocOrElem(opts.get("context", window.document)),
                 "check": lambda: None if not (not fu.isDocOrElem(opts.get("context", window.document))) else (lambda: setattr(fu,"error_context", logger.error("The context is neither Document nor Element.")))()
                })(),
                "querySelector": lambda: (lambda: setattr(fu, "elem",fu.context.querySelector(expr) if not fu.error_context else None))(),
            "items": lambda: setattr(fu, "items",  [fu.elem] if fu.elem else []),
            "resultType": lambda: setattr(fu,"resultType",None)
        })(),
        "case_querySelectorAll": lambda: (lambda: {
             "check_context": lambda: (lambda: {
                "is_context_invalid": lambda: not fu.isDocOrElem(opts.get("context", window.document)),
                 "check": lambda: None if not (not fu.isDocOrElem(opts.get("context", window.document))) else (lambda: setattr(fu,"error_context", logger.error("The context is neither Document nor Element.")))()
                })(),
            "querySelectorAll": lambda: (lambda: setattr(fu,"elems",fu.context.querySelectorAll(expr) if not fu.error_context else None))(),
            "items": lambda: setattr(fu, "items", fu.listToArr(fu.elems) if not fu.error_context else []),
             "resultType": lambda: setattr(fu,"resultType",None)
        })(),
         "switch": lambda: (lambda: {
           "evaluate_method": lambda: fu.case_evaluate() if method == "evaluate" else None,
            "querySelector_method": lambda: fu.case_querySelector() if method == "querySelector" else None,
            "querySelectorAll_method": lambda: fu.case_querySelectorAll() if  not(method == "evaluate" or method == "querySelector") else None
        })(),
        "result": lambda: {
            "items": fu.items if not fu.error_context else [],
            "method": method,
             "resultType": fu.resultType if not fu.error_context else None
            }
    })(),

    """
    Преобразует результат XPath в массив.
    
    :param res: Результат XPath.
    :type res: XPathResult
    :param type: Тип результата XPath.
    :type type: int
    :return: Массив элементов.
    :rtype: list
    """
    "resToArr": lambda res, type=None: (lambda: {
        "type_check": lambda: setattr(fu, "type", res.resultType if not type or type == xpathResult.ANY_TYPE else type),
        "arr": [],
        "case_NUMBER_TYPE": lambda: (lambda: fu.arr.append(res.numberValue) if not (fu.type != xpathResult.NUMBER_TYPE) else None)(),
         "case_STRING_TYPE": lambda: (lambda: fu.arr.append(res.stringValue) if not (fu.type != xpathResult.STRING_TYPE) else None)(),
         "case_BOOLEAN_TYPE": lambda: (lambda: fu.arr.append(res.booleanValue) if not (fu.type != xpathResult.BOOLEAN_TYPE) else None)(),
        "case_ORDERED_NODE_ITERATOR_TYPE": lambda: (lambda: [fu.arr.append(node) for node in iter(lambda: res.iterateNext(), None)] if not (fu.type != xpathResult.ORDERED_NODE_ITERATOR_TYPE and fu.type != xpathResult.UNORDERED_NODE_ITERATOR_TYPE ) else None)(),
        "case_ORDERED_NODE_SNAPSHOT_TYPE": lambda: (lambda: [fu.arr.append(res.snapshotItem(i)) for i in range(res.snapshotLength)] if not (fu.type != xpathResult.ORDERED_NODE_SNAPSHOT_TYPE and fu.type != xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE ) else None)(),
         "case_ANY_UNORDERED_NODE_TYPE": lambda: (lambda: fu.arr.append(res.singleNodeValue) if not (fu.type != xpathResult.ANY_UNORDERED_NODE_TYPE and fu.type != xpathResult.FIRST_ORDERED_NODE_TYPE) else None)(),
       "case_default": lambda: None if not (fu.type != xpathResult.NUMBER_TYPE and fu.type != xpathResult.STRING_TYPE and fu.type != xpathResult.BOOLEAN_TYPE  and fu.type != xpathResult.ORDERED_NODE_ITERATOR_TYPE and fu.type != xpathResult.UNORDERED_NODE_ITERATOR_TYPE and fu.type != xpathResult.ORDERED_NODE_SNAPSHOT_TYPE and fu.type != xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE and fu.type != xpathResult.ANY_UNORDERED_NODE_TYPE and fu.type != xpathResult.FIRST_ORDERED_NODE_TYPE) else (lambda: logger.error(f"The resultType is invalid. {fu.type}"))(),
        "switch": lambda: (lambda: {
            "number_type": fu.case_NUMBER_TYPE(),
            "string_type": fu.case_STRING_TYPE(),
             "boolean_type": fu.case_BOOLEAN_TYPE(),
            "node_iterator_type": fu.case_ORDERED_NODE_ITERATOR_TYPE(),
            "node_snapshot_type": fu.case_ORDERED_NODE_SNAPSHOT_TYPE(),
            "single_node_type": fu.case_ANY_UNORDERED_NODE_TYPE(),
            "default_type": fu.case_default()
         })(),
        "return": fu.arr
    })(),

    """
    Создает функцию-резолвер для XPath на основе объекта.
    
    :param obj: Объект, содержащий префиксы и URI пространств имен.
    :type obj: dict or str or function
    :return: Функция-резолвер или None.
    :rtype: function or None
    """
    "makeResolver": lambda obj: (lambda: {
        "obj_is_null": lambda: None if obj is not None else (lambda: setattr(fu, "return", None))(),
        "obj_is_func": lambda: None if not callable(obj) else setattr(fu, "return", obj),
        "dict": None,
         "obj_is_string": lambda:  (lambda: setattr(fu, "dict", json.loads(obj) if not (lambda: logger.error(f"Invalid resolver [{obj}]. : {e.message}"))() else None ) if isinstance(obj, str) else setattr(fu, "dict", obj) )(),
         "check_valid": lambda: (lambda: setattr(fu, "map", fu.objToMap(fu.dict)) if fu.isValidDict(fu.dict) else setattr(fu,"error_dict", logger.error(f"Invalid resolver. {json.dumps(fu.dict)}")))() if fu.dict else None,
        "resolver": lambda: (lambda str: fu.map.get(str) if fu.map.has(str) else "") if not fu.error_dict else None,
         "return_if": lambda: setattr(fu,"return",fu.resolver) if fu.resolver else None,
        "return_res": lambda: fu.return
    })(),

    """
    Проверяет, является ли объект словарем с строковыми значениями.
    
    :param obj: Объект для проверки.
    :type obj: object
    :return: True, если объект является валидным словарем, иначе False.
    :rtype: bool
    """
    "isValidDict": lambda obj: (lambda: {
        "obj_is_null_or_not_object": lambda: None if not (obj is None or not isinstance(obj, dict)) else setattr(fu, "return", False),
        "check_values": lambda: [None if isinstance(obj[key], str) else setattr(fu, "return", False) for key in obj.keys()],
        "return_valid": lambda: True if not hasattr(fu,'return') else fu.return
    })(),

    """
    Преобразует объект в Map.
    
    :param obj: Объект для преобразования.
    :type obj: object
    :return: Map, содержащий пары ключ-значение из объекта.
    :rtype: Map
    """
    "objToMap": lambda obj: (lambda: {
        "map":  Map(),
        "set_map": lambda: [fu.map.set(item, obj[item]) for item in obj.keys()],
        "return": fu.map
    })(),

    """
    Проверяет, является ли объект документом или элементом.
    
    :param obj: Объект для проверки.
    :type obj: object
    :return: True, если объект является документом или элементом, иначе False.
    :rtype: bool
    """
    "isDocOrElem": lambda obj: (lambda: {
        "check": lambda: True if (obj.nodeType == 1 or obj.nodeType == 9) else False
    })(),

    """
    Преобразует NodeList в массив.
    
    :param list: NodeList для преобразования.
    :type list: NodeList
    :return: Массив элементов.
    :rtype: list
    """
    "listToArr": lambda list: (lambda: {
        "elems": [],
        "add_elem": lambda: [fu.elems.append(list[i]) for i in range(list.length)],
        "return": fu.elems
    })(),

    """
    Возвращает детали элемента.
    
    :param item: Элемент, для которого нужно получить детали.
    :type item: object
    :return: Объект с типом, именем, значением и текстом элемента.
    :rtype: dict
    """
    "getItemDetail": lambda item: (lambda: {
        "typeStr": type(item),
        "case_string": lambda: setattr(fu, "return", {
                "type": "String",
                "name": "",
                "value": item,
                "textContent": ""
            }) if isinstance(item, str) else None,
        "case_number": lambda: setattr(fu, "return", {
                "type": "Number",
                "name": "",
                "value": str(item),
                "textContent": ""
            }) if isinstance(item, int) or isinstance(item, float) else None,
         "case_boolean": lambda: setattr(fu, "return", {
                "type": "Boolean",
                "name": "",
                "value": str(item),
                "textContent": ""
            }) if isinstance(item, bool) else None,
       "case_element": lambda: setattr(fu, "return", {
                "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + str(item.nodeType) + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            }) if fu.isElementItem(item) else None,
        "case_attr": lambda: setattr(fu,"return", {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            }) if fu.isAttrItem(item) else None,
        "case_node": lambda: setattr(fu,"return",{
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + str(item.nodeType) + ")",
            "name": item.nodeName,
            "value": item.nodeValue or "",
            "textContent": item.textContent or ""
        }) if (not (isinstance(item, str) or isinstance(item, int) or isinstance(item, float) or isinstance(item, bool)) and not fu.isElementItem(item) and not fu.isAttrItem(item)) else None,
        "switch": lambda: (lambda: {
          "string": fu.case_string(),
            "number": fu.case_number(),
            "boolean": fu.case_boolean(),
            "element": fu.case_element(),
            "attr": fu.case_attr(),
            "node": fu.case_node()
         })(),
        "return_item": fu.return
    })(),
    """
    Возвращает детали нескольких элементов.
    
    :param items: Массив элементов, для которых нужно получить детали.
    :type items: list
    :return: Массив объектов с деталями элементов.
    :rtype: list
    """
    "getItemDetails": lambda items: (lambda: {
        "details": [],
        "add_detail": lambda: [fu.details.append(fu.getItemDetail(items[i])) for i in range(len(items))],
        "return": fu.details
    })(),

    # Map для преобразования числовых кодов типов узлов в строковые представления.
    "nodeTypeMap": Map([
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
    ]),

    """
    Возвращает строковое представление типа узла.
    
    :param nodeType: Числовой код типа узла.
    :type nodeType: int
    :return: Строковое представление типа узла или "Unknown".
    :rtype: str
    """
    "getNodeTypeStr": lambda nodeType: (lambda: {
        "node_has_type": lambda:  fu.nodeTypeMap.get(nodeType) if fu.nodeTypeMap.has(nodeType) else "Unknown"
    })(),

    # Карты для преобразования типов результатов XPath между строковым и числовым представлениями.
    "xpathResultMaps": {
        "numToStr" : Map([
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

        "strToNum" : Map([
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
    },

    """
    Возвращает строковое представление типа результата XPath.
    
    :param resultType: Числовой код типа результата XPath.
    :type resultType: int
    :return: Строковое представление типа результата XPath или "Unknown".
    :rtype: str
    """
    "getxpathResultStr": lambda resultType: (lambda: {
        "result_has_type": lambda: fu.xpathResultMaps.numToStr.get(resultType) if fu.xpathResultMaps.numToStr.has(resultType) else "Unknown"
    })(),

    """
    Возвращает числовой код типа результата XPath.
    
    :param resultTypeStr: Строковое представление типа результата XPath.
    :type resultTypeStr: str
    :return: Числовой код типа результата XPath или NaN.
    :rtype: int
    """
    "getxpathResultNum": lambda resultTypeStr: (lambda: {
      "result_has_type": lambda: fu.xpathResultMaps.strToNum.get(resultTypeStr) if fu.xpathResultMaps.strToNum.has(resultTypeStr) else float('NaN')
    })(),

    """
    Проверяет, является ли элемент атрибутом.
    
    :param item: Элемент для проверки.
    :type item: object
    :return: True, если элемент является атрибутом, иначе False.
    :rtype: bool
    """
    "isAttrItem": lambda item: (lambda: {
        "check": lambda: str(item) == "[object Attr]"
    })(),

    """
    Проверяет, является ли элемент узлом.
    
    :param item: Элемент для проверки.
    :type item: object
    :return: True, если элемент является узлом, иначе False.
    :rtype: bool
    """
    "isNodeItem": lambda item: (lambda: {
      "check_attr": lambda: False if fu.isAttrItem(item) else None,
        "check_type": lambda: False if isinstance(item, str) or isinstance(item, int) or isinstance(item, float) else True,
    })(),
    
    """
    Проверяет, является ли элемент элементом DOM.
    
    :param item: Элемент для проверки.
    :type item: object
    :return: True, если элемент является элементом DOM, иначе False.
    :rtype: bool
    """
    "isElementItem": lambda item: (lambda: {
        "check": lambda: True if fu.isNodeItem(item) and (item.nodeType == Node.ELEMENT_NODE) else False
    })(),

    """
    Добавляет класс к элементу.
    
    :param clas: Класс для добавления.
    :type clas: str
    :param item: Элемент, к которому нужно добавить класс.
    :type item: object
    """
    "addClassToItem": lambda clas, item: (lambda: {
        "check": lambda:  item.classList.add(clas) if fu.isElementItem(item) else None
    })(),

    """
    Добавляет класс к нескольким элементам.
    
    :param clas: Класс для добавления.
    :type clas: str
    :param items: Массив элементов, к которым нужно добавить класс.
    :type items: list
    """
    "addClassToItems": lambda clas, items: (lambda: {
       "add_class": lambda: [fu.addClassToItem(clas, item) for item in items]
    })(),

    """
    Сохраняет оригинальный класс элемента.
    
    :param item: Элемент, для которого нужно сохранить класс.
    :type item: object
    :return: Объект, содержащий элемент и его оригинальный класс.
    :rtype: dict
    """
    "saveItemClass": lambda item: (lambda: {
        "check": lambda: None if not fu.isElementItem(item) else (lambda: {
            "check_has_class": lambda: setattr(fu,"clas", item.getAttribute("class")) if item.hasAttribute("class") else setattr(fu,"clas", None),
            "return": lambda: setattr(fu,"return", {
                "elem": item,
                "origClass": fu.clas
              }) if not  hasattr(fu,'error') else None,
            "return_orig_class": fu.return
            })()
    })(),

    """
    Восстанавливает оригинальный класс элемента.
    
    :param savedClass: Объект с сохраненным элементом и его оригинальным классом.
    :type savedClass: dict
    """
    "restoreItemClass": lambda savedClass: (lambda: {
      "check_saved_class": lambda: None if savedClass is None else (lambda: {
           "check_orig_class": lambda: savedClass.elem.removeAttribute("class") if savedClass.origClass is None else savedClass.elem.setAttribute("class", savedClass.origClass)
        })()
    })(),

    """
    Сохраняет оригинальные классы нескольких элементов.
    
    :param items: Массив элементов, для которых нужно сохранить классы.
    :type items: list
    :return: Массив объектов с сохраненными классами элементов.
    :rtype: list
    """
    "saveItemClasses": lambda items: (lambda: {
        "savedClasses": [],
        "save_classes": lambda: [fu.savedClasses.append(fu.saveItemClass(item)) for item in items],
        "return": fu.savedClasses
    })(),

    """
    Восстанавливает оригинальные классы нескольких элементов.
    
    :param savedClasses: Массив объектов с сохраненными классами элементов.
    :type savedClasses: list
    """
    "restoreItemClasses": lambda savedClasses: (lambda: {
      "restore_classes": lambda: [fu.restoreItemClass(savedClass) for savedClass in savedClasses]
    })(),

    """
    Устанавливает атрибут элементу.
    
    :param name: Имя атрибута.
    :type name: str
    :param value: Значение атрибута.
    :type value: str
    :param item: Элемент, которому нужно установить атрибут.
    :type item: object
    """
    "setAttrToItem": lambda name, value, item: (lambda: {
        "check": lambda: item.setAttribute(name, value) if fu.isElementItem(item) else None
    })(),

    """
    Удаляет атрибут у элемента.
    
    :param name: Имя атрибута для удаления.
    :type name: str
    :param item: Элемент, у которого нужно удалить атрибут.
    :type item: object
    """
    "removeAttrFromItem": lambda name, item: (lambda: {
        "check": lambda: item.removeAttribute(name) if fu.isElementItem(item) else None
    })(),

    """
    Удаляет атрибут у нескольких элементов.
    
    :param name: Имя атрибута для удаления.
    :type name: str
    :param items: Массив элементов, у которых нужно удалить атрибут.
    :type items: list
    """
    "removeAttrFromItems": lambda name, items: (lambda: {
       "remove_attr": lambda:  [fu.removeAttrFromItem(name, item) for item in items]
    })(),

    """
    Устанавливает индекс в качестве атрибута для нескольких элементов.
    
    :param name: Имя атрибута для установки индекса.
    :type name: str
    :param items: Массив элементов, для которых нужно установить индекс.
    :type items: list
    """
    "setIndexToItems": lambda name, items: (lambda: {
         "set_index": lambda: [fu.setAttrToItem(name, i, items[i]) for i in range(len(items))]
    })(),

    """
    Возвращает родительский элемент.
    
    :param item: Элемент, для которого нужно получить родителя.
    :type item: object
    :return: Родительский элемент или None.
    :rtype: object or None
    """
    "getParentElement": lambda item: (lambda: {
       "case_attr": lambda: (lambda: {
             "parent_attr": lambda: item.ownerElement if item.ownerElement else None
       })() if fu.isAttrItem(item) else None,
       "case_node": lambda: (lambda: {
           "parent_element": lambda: item.parentElement if item.parentElement else None,
           "check_node_type": lambda: item.parentNode if item.parentNode and (item.parentNode.nodeType == Node.ELEMENT_NODE) else None
       })() if fu.isNodeItem(item) else None,
       "return": lambda: (lambda: fu.parent_attr if fu.isAttrItem(item) else (fu.parent_element if fu.isNodeItem(item) and fu.parent_element else (fu.check_node_type if fu.isNodeItem(item) and fu.check_node_type  else None )))()
    })(),

    """
     Возвращает список всех родительских элементов элемента.
    
    :param elem: Элемент, для которого нужно получить список предков.
    :type elem: object
    :return: Список родительских элементов.
    :rtype: list
    """
    "getAncestorElements": lambda elem: (lambda: {
        "ancs": [],
        "cur": elem,
        "parent": lambda: (lambda: {
            "find_parent": lambda: setattr(fu, "parent", fu.cur.parentElement)
        })(),
      "find_all_parent_elements": lambda: (lambda: [fu.ancs.append(fu.parent)  and setattr(fu, "cur", fu.parent) and setattr(fu, "parent", fu.cur.parentElement) for _ in iter(lambda: fu.parent, None) ] )() ,
       "find_parent_node": lambda: (lambda: {
          "find_parent": lambda: setattr(fu, "parent", fu.cur.parentNode)
        })(),
        "find_all_parent_nodes": lambda: (lambda: [fu.ancs.append(fu.cur) and  setattr(fu, "cur", fu.parent) and setattr(fu, "parent", fu.cur.parentNode)  for _ in iter(lambda: fu.parent if fu.parent and fu.parent.nodeType == Node.ELEMENT_NODE else None, None) ] )() ,
      "return_ancs": fu.ancs
    })(),

    """
     Возвращает документ, которому принадлежит элемент.
    
    :param item: Элемент, для которого нужно получить документ.
    :type item: object
    :return: Документ, которому принадлежит элемент.
    :rtype: object
    """
    "getOwnerDocument": lambda item: (lambda: {
       "case_attr": lambda:  (lambda: {
            "elem": lambda: setattr(fu, "elem", item.ownerElement),
          "check_elem": lambda: fu.elem.ownerDocument if fu.elem else item.ownerDocument
       })() if fu.isAttrItem(item) else None,