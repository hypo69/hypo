# Анализ кода модуля `try_xpath_content.js`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    *   Используются константы для строк и атрибутов, что улучшает поддерживаемость кода.
    *   Присутствует обработка ошибок, хотя она могла бы быть улучшена.
    *   Код учитывает различные типы элементов, включая фреймы и пустые окна.
    *   Активно используется `browser.runtime.sendMessage` для взаимодействия с расширением.
    *   Используется `Map` для хранения данных, что является хорошей практикой.
*   **Минусы:**
    *   Не все функции имеют документацию в формате reStructuredText.
    *   Некоторые блоки try-except можно заменить на более явную обработку ошибок через `logger.error`.
    *   Используется `JSON.parse` вместо `j_loads`.
    *   Не все переменные имеют описательные имена.
    *   Присутствует избыточное использование `Object.create(null)`.

**Рекомендации по улучшению:**

1.  **Документация:** Добавить reStructuredText (RST) docstring ко всем функциям, методам и переменным.
2.  **Импорты:**  Добавить необходимые импорты. В данном файле используется `browser`, который предполагает, что он предоставляется средой выполнения расширения. Но для большей ясности можно добавить комментарий о том, что этот объект предоставляет browser API.
3.  **Обработка ошибок:** Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error` там, где это уместно.
4.  **Использование `j_loads`:** Заменить `JSON.parse` на `j_loads` или `j_loads_ns`.
5.  **Улучшение именования:** Переименовать переменные для большей ясности.
6.  **Устранение избыточности:** Убрать `Object.create(null)` там, где достаточно простого литерала объекта `{}`.
7.  **Добавить комментарии**: Добавить комментарии в коде для лучшего понимания.

**Оптимизированный код:**

```python
"""
Модуль для управления и взаимодействия с контентом страницы для расширения Try XPath.
======================================================================================

Этот модуль обеспечивает взаимодействие расширения Try XPath с контентом веб-страницы.
Он обрабатывает сообщения от расширения, выполняет XPath-запросы, управляет стилями,
фокусировкой элементов и фреймами.

:var attributes: Объект, содержащий атрибуты для элементов, используемые расширением.
:vartype attributes: dict
:var prevMsg: Последнее отправленное сообщение.
:vartype prevMsg: dict
:var executionCount: Счетчик выполненных запросов.
:vartype executionCount: int
:var inBlankWindow: Флаг, указывающий, выполняется ли код в пустом окне.
:vartype inBlankWindow: bool
:var currentDocument: Текущий документ, на котором выполняются операции.
:vartype currentDocument: Document
:var contextItem: Текущий контекстный элемент для XPath-запросов.
:vartype contextItem: Node
:var currentItems: Список текущих элементов, полученных после выполнения XPath.
:vartype currentItems: list
:var focusedItem: Текущий элемент, находящийся в фокусе.
:vartype focusedItem: Node
:var focusedAncestorItems: Список предковых элементов текущего элемента в фокусе.
:vartype focusedAncestorItems: list
:var currentCss: Текущий CSS, применяемый к странице.
:vartype currentCss: str
:var insertedStyleElements: Карта стилей, вставленных на страницу.
:vartype insertedStyleElements: Map
:var expiredCssSet: Набор устаревших стилей CSS.
:vartype expiredCssSet: set
:var originalAttributes: Карта оригинальных атрибутов элементов.
:vartype originalAttributes: Map

"""
# from src.logger.logger import logger # TODO: добавить логгер
# from src.utils.jjson import j_loads, j_loads_ns # TODO: добавить j_loads

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    // prevent multiple execution
    if (tx.isContentLoaded) {
        return;
    }
    tx.isContentLoaded = true;

    const dummyItem = "";
    const dummyItems = [];
    const invalidExecutionId = NaN;
    const styleElementHeader
          = "/* This style element was inserted by browser add-on, Try xpath."
          + " If you want to remove this element, please click the reset"
          + " style button in the popup. */\\n";

    /**
      * @type {object} attributes - Атрибуты используемые для элементов
      * @property {string} element - Атрибут для элемента.
      * @property {string} context - Атрибут для контекста.
      * @property {string} focused - Атрибут для фокуса.
      * @property {string} focusedAncestor - Атрибут для предка в фокусе.
      * @property {string} frame - Атрибут для фрейма.
      * @property {string} frameAncestor - Атрибут для предка фрейма.
      */
    var attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"        
    };

    var prevMsg;
    var executionCount = 0;
    var inBlankWindow = false;
    var currentDocument = null;
    var contextItem = dummyItem;
    var currentItems = dummyItems;
    var focusedItem = dummyItem;
    var focusedAncestorItems = dummyItems;
    var currentCss = null;
    var insertedStyleElements = new Map();
    var expiredCssSet = Object.create(null);
    var originalAttributes = new Map();
    
    /**
      * Сохраняет оригинальные атрибуты элемента и устанавливает новые.
      *
      * :param attr: Имя атрибута.
      * :type attr: str
      * :param value: Значение атрибута.
      * :type value: str
      * :param item: Элемент, атрибут которого нужно изменить.
      * :type item: Node
      */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };

    /**
      * Сохраняет оригинальные атрибуты для списка элементов и устанавливает индексы.
      *
      * :param attr: Имя атрибута.
      * :type attr: str
      * :param items: Список элементов, атрибуты которых нужно изменить.
      * :type items: list
      */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };

    /**
      * Проверяет, может ли элемент получить фокус.
      *
      * :param item: Элемент для проверки.
      * :type item: Node
      * :returns: True если элемент может получить фокус, False в противном случае.
      * :rtype: bool
      */
    function isFocusable(item) {
        if (!item) {
            return false;
        }
        if (fu.isNodeItem(item) || fu.isAttrItem(item)) {
            return true;
        }
        return false;
    };

     /**
      * Устанавливает фокус на элемент и подсвечивает его.
      *
      * :param item: Элемент, на который нужно установить фокус.
      * :type item: Node
      */
    function focusItem(item) {
        fu.removeAttrFromItem(attributes.focused, focusedItem);
        fu.removeAttrFromItems(attributes.focusedAncestor,
                               focusedAncestorItems);
        

        if (!isFocusable(item)) {
            return;
        }

        if (fu.isElementItem(item)) {
            focusedItem = item;
        } else {
            focusedItem = fu.getParentElement(item);
        }

        focusedAncestorItems = fu.getAncestorElements(focusedItem);

        setAttr(attributes.focused, "true", focusedItem);
        setIndex(attributes.focusedAncestor, focusedAncestorItems);

        focusedItem.blur();
        focusedItem.focus();
        focusedItem.scrollIntoView();
    };

     /**
      * Устанавливает основные атрибуты для контекстного элемента и списка элементов.
      */
    function setMainAttrs() {
        if (contextItem !== null) {
            setAttr(attributes.context, "true", contextItem);
        }
        setIndex(attributes.element, currentItems);
    };

    /**
      * Восстанавливает оригинальные атрибуты элементов.
      */
    function restoreAttrs() {
        fu.restoreItemAttrs(originalAttributes);
        originalAttributes = new Map();
    };

    /**
      * Сбрасывает предыдущие результаты и подготавливает к новому выполнению.
      */
    function resetPrev() {
        restoreAttrs();

        contextItem = dummyItem;
        currentItems = dummyItems;
        focusedItem = dummyItem;
        focusedAncestorItems = dummyItems;

        prevMsg = createResultMessage();
        executionCount++;
    };

    /**
      * Создает строку типа для результата XPath.
      *
      * :param resultType: Тип результата.
      * :type resultType: int
      * :returns: Строка, представляющая тип результата.
      * :rtype: str
      */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };

    /**
      * Отправляет сообщение для обновления CSS, если есть изменения.
      */
    function updateCss() {
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };

    /**
      * Получает список фреймов на основе спецификации.
      *
      * :param spec: Спецификация фреймов.
      * :type spec: str
      * :returns: Список фреймов.
      * :rtype: list
      * :raises Error: Если спецификация невалидна.
      */
    function getFrames(spec) {
        var inds = JSON.parse(spec);
        
        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return fu.getFrameAncestry(inds).reverse();
        } else {
            throw new Error("Invalid specification. [" + spec + "]");
        }
    };

    /**
      * Парсит спецификацию фрейма.
      *
      * :param frameDesi: Строка спецификации фрейма.
      * :type frameDesi: str
      * :returns: Массив индексов фреймов.
      * :rtype: list
      * :raises Error: Если спецификация невалидна.
      */
    function parseFrameDesignation(frameDesi) {
        var inds = JSON.parse(frameDesi);
        
        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return inds;
        } else {
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }
    };

     /**
      * Проверяет наличие пустых окон в иерархии фреймов.
      *
      * :param desi: Массив индексов фреймов.
      * :type desi: list
      * :param win: Начальное окно.
      * :type win: Window
      * :returns: Объект с результатами проверки.
      * :rtype: object
      */
    function traceBlankWindows(desi, win) {
        win = win || window;
        var result = Object.create(null);

        result.windows = [];
        for (let i = 0; i < desi.length; i++) {
            let frameInd = desi[i];
            if ((frameInd <= -1) || (frameInd >= win.frames.length)) {
                result.failedWindow = null;
                result.success = false;
                return result;
            }
            win = win.frames[frameInd];
            if (!fu.isBlankWindow(win)) {
                result.failedWindow = win;
                result.success = false;
                return result;
            }
            result.windows.push(win);
        }

        result.success = true;
        return result;
    };

    /**
     * Обрабатывает изменения в CSS.
     *
     * :param newCss: Новый CSS.
     * :type newCss: str
     */
    function handleCssChange(newCss) {
        if (currentCss === null) {
            if (newCss in expiredCssSet) {
                currentCss = newCss;
                delete expiredCssSet[newCss];
            }
        } else if (newCss !== currentCss) {
            if (newCss in expiredCssSet) {
                currentCss = newCss;
                delete expiredCssSet[newCss];
            } else {
                expiredCssSet[currentCss] = true;
                currentCss = null;
            }
        }
        // If newCss and currentCss are the same string do nothing.
    };

    /**
     * Находит фрейм по сообщению.
     *
     * :param event: Событие сообщения.
     * :type event: MessageEvent
     * :param win: Текущее окно.
     * :type win: Window
     * :returns: Элемент фрейма.
     * :rtype: HTMLIFrameElement
     */
    function findFrameByMessage(event, win) {
        var ind = event.data.frameIndex;
        var subWin;
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    };

    /**
      * Устанавливает слушатель событий для фокуса фрейма.
      *
      * :param win: Окно, к которому нужно привязать слушателя.
      * :type win: Window
      * :param isBlankWindow: Флаг, является ли окно пустым.
      * :type isBlankWindow: bool
      */
    function setFocusFrameListener(win, isBlankWindow) {
        var localUpdateCss;
        if (isBlankWindow) {
            localUpdateCss = updateStyleElement.bind(null, win.document);
        } else {
            localUpdateCss = updateCss;
        }

        win.addEventListener("message", (event) => {
            if (event.data
                && event.data.message === "tryxpath-focus-frame"
                && Number.isInteger(event.data.index)
                && Number.isInteger(event.data.frameIndex)) {

                let frame = findFrameByMessage(event, win);
                if (!frame) {
                    return;
                }

                let index = event.data.index;
                localUpdateCss();
                setAttr(attributes.frame, index, frame);
                setIndex(attributes.frameAncestor,
                         fu.getAncestorElements(frame));
                if (win === win.top) {
                    frame.blur();
                    frame.focus();
                    frame.scrollIntoView();
                } else {
                    win.parent.postMessage({
                        "message": "tryxpath-focus-frame",
                        "index": ++index,
                        "frameIndex": fu.findFrameIndex(win, win.parent)
                    }, "*");
                }
            }
        });
    };

    /**
      * Инициализирует пустые окна.
      *
      * :param win: Окно для инициализации.
      * :type win: Window
      */
    function initBlankWindow(win) {
        if (!win.tryxpath) {
            win.tryxpath = Object.create(null);
        }

        if (win.tryxpath.isInitialized) {
            return;
        }
        win.tryxpath.isInitialized = true;

        setFocusFrameListener(win, true);
    };

    /**
      * Находит родительский элемент для стилей.
      *
      * :param doc: Документ, для которого нужно найти родителя.
      * :type doc: Document
      * :returns: Родительский элемент.
      * :rtype: Node
      */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };

     /**
      * Обновляет стили для документа.
      *
      * :param doc: Документ, стили которого нужно обновить.
      * :type doc: Document
      */
    function updateStyleElement(doc) {
        var css = currentCss || "";
        css = styleElementHeader + css;

        var style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }

        var parent = findStyleParent(doc);
        if (parent) {
            let newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    };

     /**
      * Обновляет стили во всех вставленных элементах.
      */
    function updateAllStyleElements() {
        var css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };

     /**
      * Удаляет элемент стиля из документа.
      *
      * :param doc: Документ, из которого нужно удалить стиль.
      * :type doc: Document
      */
    function removeStyleElement(doc) {
        var elem = insertedStyleElements.get(doc);
        
        if (!elem) {
            return;
        }

        var parent = elem.parentNode;
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    };

    /**
      * Удаляет все элементы стилей.
      */
    function removeAllStyleElements() {
        for (let [doc, elem] of insertedStyleElements) {
            let parent = elem.parentNode;
            if (parent) {
                parent.removeChild(elem);
            }
        }
        insertedStyleElements.clear();
    };

    /**
      * Создает сообщение о результате по умолчанию.
      *
      * :returns: Объект сообщения с результатами по умолчанию.
      * :rtype: dict
      */
    function createResultMessage() {
        return {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "showResultsInPopup",
            "executionId": invalidExecutionId,
            "href": "",
            "title": "",
            "message": "There is no result.",
            "main": {
                "method": "evaluate",
                "expression": "",
                "specifiedResultType": "ANY_TYPE(0)",
                "resolver": "",
                "itemDetails": []
            }
        };        
    };

     /**
      * Обрабатывает сообщения от расширения.
      *
      * :param message: Сообщение от расширения.
      * :type message: dict
      * :param sender: Отправитель сообщения.
      * :type sender: object
      * :param sendResponse: Функция для отправки ответа.
      * :type sendResponse: function
      */
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    // browser - это объект, предоставляемый API браузера, и не требует импорта.
    browser.runtime.onMessage.addListener(genericListener);

    /**
      * Устанавливает информацию о контенте.
      *
      * :param message: Сообщение с информацией о контенте.
      * :type message: dict
      */
    genericListener.listeners.setContentInfo = function (message) {
        if (!message) {
            return;
        }

        if ("attributes" in message) {
            attributes = message.attributes;
        }
    };

    /**
      * Выполняет XPath запрос и отправляет результаты.
      *
      * :param message: Сообщение с данными для выполнения запроса.
      * :type message: dict
      * :param sender: Отправитель сообщения.
      * :type sender: object
      */
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();

        updateCss();

        var sendMsg = {};
        var main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        var mainType = fu.getxpathResultNum(main.resultType);
        sendMsg.main = {};
        sendMsg.main.method = main.method;
        sendMsg.main.expression = main.expression;
        sendMsg.main.specifiedResultType = makeTypeStr(mainType);
        sendMsg.main.resultType = "";
        sendMsg.main.resolver = main.resolver || "";
        sendMsg.main.itemDetails = [];

        contextItem = document;
        currentDocument = document;

        if ("frameDesignation" in message) {
            sendMsg.frameDesignation = message.frameDesignation;

            try {
                let desi = parseFrameDesignation(message.frameDesignation);
                let res = traceBlankWindows(desi, window);
                if (!res.success) {
                    if (res.failedWindow === null) {
                        throw new Error(
                            "The specified frame does not exist.");
                    } else {
                        res.failedWindow.postMessage({
                            "message": "tryxpath-request-message-to-popup",
                            "messageId": 1
                        }, "*");
                        return;
                    }
                }
                contextItem = res.windows.pop().document;
            } catch (e) {
                sendMsg.message = "An error occurred when getting a frame. "
                    + e.message;
                 # Отправка сообщения об ошибке через runtime API браузера
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }

            inBlankWindow = true;
            currentDocument = contextItem;
        }

        if (inBlankWindow) {
            removeStyleElement(currentDocument);
        }

        if (message.context) {
            let cont = message.context;
            let contType = fu.getxpathResultNum(cont.resultType);
            sendMsg.context = {};
            sendMsg.context.method = cont.method;
            sendMsg.context.expression = cont.expression;
            sendMsg.context.specifiedResultType = makeTypeStr(contType);
            sendMsg.context.resolver = cont.resolver || "";
            sendMsg.context.itemDetail = null;

            let contRes;
            try {
                contRes = fu.execExpr(cont.expression, cont.method, {
                    "context": contextItem,
                    "resultType": contType,
                    "resolver": cont.resolver
                });
            } catch (e) {
                sendMsg.message = "An error occurred when getting a context. "
                    + e.message;
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }

            if (contRes.items.length === 0) {
                sendMsg.message = "A context is not found.";
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }
            contextItem = contRes.items[0];

            sendMsg.context.resultType = makeTypeStr(contRes.resultType);
            sendMsg.context.itemDetail = fu.getItemDetail(contextItem);
        }

        var mainRes;
        try {
            mainRes = fu.execExpr(main.expression, main.method, {
                "context": contextItem,
                "resultType": mainType,
                "resolver": main.resolver
            });
        } catch (e) {
             # Отправка сообщения об ошибке через runtime API браузера
            sendMsg.message = "An error occurred when getting nodes. "
                + e.message;
            browser.runtime.sendMessage(sendMsg);
            prevMsg = sendMsg;
            return;
        }
        currentItems = mainRes.items;

        sendMsg.message = "Success.";
        sendMsg.main.resultType = makeTypeStr(mainRes.resultType);
        sendMsg.main.itemDetails = fu.getItemDetails(currentItems);
        browser.runtime.sendMessage(sendMsg);
        prevMsg = sendMsg;

        setMainAttrs();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        return;
    }

    /**
      * Устанавливает фокус на элемент из списка результатов.
      *
      * :param message: Сообщение с индексом элемента для фокуса.
      * :type message: dict
      */
    genericListener.listeners.focusItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(currentItems[message.index]);
        }
    };

    /**
      * Устанавливает фокус на контекстный элемент.
      *
      * :param message: Сообщение с данными о контекстном элементе.
      * :type message: dict
      */
    genericListener.listeners.focusContextItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(contextItem);
        }
    };

    /**
      * Устанавливает фокус на фрейм.
      *
      * :param message: Сообщение с данными для фокуса фрейма.
      * :type message: dict
      */
    genericListener.listeners.focusFrame = function(message) {
        var win = window;

        if ("frameDesignation" in message) {
            try {
                let desi = parseFrameDesignation(message.frameDesignation);
                let res = traceBlankWindows(desi, window);
                if (!res.success) {
                    let msg;
                    if (res.failedWindow === null) {
                        throw new Error(
                            "The specified frame does not exist.");
                    } else {
                        res.failedWindow.postMessage({
                            "message": "tryxpath-request-message-to-popup",
                            "messageId": 1
                        }, "*");
                        return;
                    }
                }
                win = res.windows.pop();
            } catch (e) {
                let sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when focusing a frame. "
                    + e.message;
                browser.runtime.sendMessage(sendMsg);
                return;
            }
        }

        if (win !== win.top) {
            win.parent.postMessage({
                "message": "tryxpath-focus-frame",
                "index": 0,
                "frameIndex": fu.findFrameIndex(win, win.parent)
            }, "*");
        }
    };

    /**
      * Запрашивает показ результатов в popup.
      */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };

    /**
      * Запрашивает показ всех результатов.
      */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }

    /**
      * Сбрасывает стили.
      */
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };

    /**
      * Устанавливает стили.
      */
    genericListener.listeners.setStyle = function () {
        restoreAttrs();
        updateCss();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        setMainAttrs();
    };

    /**
      * Завершает вставку стилей.
      *
      * :param message: Сообщение с CSS.
      * :type message: dict
      */
    genericListener.listeners.finishInsertCss = function (message) {
        var css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };

     /**
      * Завершает удаление стилей.
      *
      * :param message: Сообщение с CSS.
      * :type message: dict
      */
    genericListener.listeners.finishRemoveCss = function (message) {
        var css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };

     /**
      * Обрабатывает изменения в хранилище браузера.
      */
    browser.storage.onChanged.addListener(changes => {
        if (changes.attributes && ("newValue" in changes.attributes)) {
            attributes = changes.attributes.newValue;
        }
        if (changes.css && ("newValue" in changes.css)) {
            handleCssChange(changes.css.newValue);
        }
    });

     /**
      * Обрабатывает сообщения от других фреймов.
      */
    window.addEventListener("message", event => {
        if (event.data
            && (event.data.message === "tryxpath-request-message-to-popup")) {

            let sendMsg;
            switch (event.data.messageId) {
            case 0:
                sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when getting a frame. "
                    + "There is a frame having frameId.";
                browser.runtime.sendMessage(sendMsg);
                break;
            case 1:
                sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when focusing a frame. "
                    + "There is a frame having frameId.";
                browser.runtime.sendMessage(sendMsg);
                break;
            default:
                break;
            }
        }
    });

    prevMsg = createResultMessage();
    setFocusFrameListener(window, false);
     # Отправка запроса на установку информации о контенте через runtime API браузера
    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });

})(window);
```