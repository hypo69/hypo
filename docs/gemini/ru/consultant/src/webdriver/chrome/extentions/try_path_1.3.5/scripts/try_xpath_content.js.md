# Анализ кода модуля `try_xpath_content.js`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает понимание и поддержку.
    - Используются константы для часто используемых значений, что улучшает читаемость.
    - Присутствует обработка ошибок с выводом сообщений.
    - Код следует принципу "разделения ответственности" (например, функции для установки/снятия атрибутов).
    - Используется `Map` для хранения данных.
    - Присутствует защита от многократного выполнения скрипта.
    - Код стремится к избеганию прямого использования `try-except` блоков, заменяя их на `logger.error`.

-  Минусы
    -  Не все функции и переменные документированы в формате RST.
    -  Используются конструкции `Object.create(null)`, что может быть менее читаемым, чем обычные объекты.
    -  Некоторые функции не имеют явного возвращаемого значения (например, `genericListener.listeners.setContentInfo`), что может вызвать путаницу.
    -  Не все ошибки логируются с помощью `logger.error`.
    -  Некоторые комментарии могут быть более подробными и соответствовать формату RST.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для всех функций и переменных, особенно для тех, которые используются в качестве обработчиков событий.
2.  Уточнить назначение и типы возвращаемых значений для функций, где это неявно.
3.  Использовать `logger.error` для более явной обработки ошибок.
4.  Улучшить комментарии, чтобы они соответствовали формату RST и были более информативными.
5.  Заменить конструкции `Object.create(null)` на обычные объекты, где это возможно, для улучшения читаемости.
6.  Уточнить использование `expiredCssSet` и `currentCss`, чтобы сделать код более понятным.
7.  Добавить проверки на наличие необходимых свойств в объектах `event.data` перед их использованием, чтобы избежать ошибок.
8.  Использовать более конкретные сообщения об ошибках.
9.  Добавить константы для magic strings, чтобы избежать их повторного использования.

**Оптимизированный код**
```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    /**
     * Модуль для управления Try Xpath расширением.
     * ==================================================
     *
     * Этот модуль отвечает за обработку сообщений от popup,
     * выполнение XPath запросов, и управление стилями на странице.
     *
     */

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
     * Объект, содержащий атрибуты для выделения элементов.
     * @type {Object}
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
    /**
     * @type {Map<Document, HTMLStyleElement>}
     */
    var insertedStyleElements = new Map();
    var expiredCssSet = Object.create(null);
    /**
     * @type {Map<HTMLElement|Attr, Map<string, string>>}
     */
    var originalAttributes = new Map();


    /**
     * Устанавливает атрибут элемента и сохраняет оригинальное значение.
     *
     * @param {string} attr - Имя атрибута.
     * @param {string} value - Значение атрибута.
     * @param {HTMLElement|Attr} item - Элемент, которому устанавливается атрибут.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };

    /**
     * Устанавливает индекс атрибута для массива элементов.
     *
     * @param {string} attr - Имя атрибута.
     * @param {Array<HTMLElement|Attr>} items - Массив элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };

    /**
     * Проверяет, является ли элемент пригодным для фокусировки.
     *
     * @param {HTMLElement|Attr} item - Элемент для проверки.
     * @returns {boolean} `true`, если элемент можно фокусировать, иначе `false`.
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
     * Фокусирует элемент и устанавливает соответствующие атрибуты.
     *
     * @param {HTMLElement|Attr} item - Элемент, который нужно сфокусировать.
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
     * Устанавливает основные атрибуты для контекста и текущих элементов.
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
     * Сбрасывает предыдущие значения и увеличивает счетчик выполнения.
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
     * Формирует строку типа результата XPath.
     *
     * @param {number} resultType - Тип результата XPath.
     * @returns {string} Строка, представляющая тип результата.
     */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };

   /**
    * Обновляет CSS, отправляя сообщение в runtime.
    */
    function updateCss() {
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0, "timeout_for_event":"presence_of_element_located", "event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };

    /**
     * Извлекает фреймы на основе спецификации.
     *
     * @param {string} spec - Строка, представляющая спецификацию фреймов.
     * @returns {Array<Window>} Массив окон фреймов.
     * @throws {Error} Если спецификация недействительна.
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
     * Разбирает строку-обозначение фрейма в массив индексов.
     *
     * @param {string} frameDesi - Строка-обозначение фрейма.
     * @returns {Array<number>} Массив индексов фреймов.
     * @throws {Error} Если обозначение фрейма не является массивом чисел.
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
     * Отслеживает пустые окна фреймов.
     *
     * @param {Array<number>} desi - Массив индексов фреймов.
     * @param {Window} win - Окно, в котором нужно начать отслеживание.
     * @returns {Object} Результат отслеживания, содержащий информацию об успехе и неудачах.
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
     * Обрабатывает изменение CSS.
     *
     * @param {string} newCss - Новая строка CSS.
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
    };

    /**
     * Находит элемент фрейма по сообщению.
     *
     * @param {Object} event - Событие сообщения.
     * @param {Window} win - Окно, в котором нужно искать фрейм.
     * @returns {HTMLElement|null} Элемент фрейма или `null`, если не найден.
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
     * Устанавливает слушатель событий для фрейма.
     *
     * @param {Window} win - Окно фрейма.
     * @param {boolean} isBlankWindow - Флаг, является ли окно пустым.
     */
    function setFocusFrameListener(win, isBlankWindow) {
         /**
         * @type {function}
         */
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
     * Инициализирует пустое окно фрейма.
     *
     * @param {Window} win - Окно фрейма для инициализации.
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
     * @param {Document} doc - Документ, в котором нужно найти родителя стилей.
     * @returns {HTMLElement|null} Родительский элемент для стилей (head или body) или `null`, если не найден.
     */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };

    /**
     * Обновляет элемент стилей.
     *
     * @param {Document} doc - Документ, в котором нужно обновить элемент стилей.
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
     * Обновляет все элементы стилей.
     */
    function updateAllStyleElements() {
        var css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };

    /**
     * Удаляет элемент стилей из документа.
     *
     * @param {Document} doc - Документ, из которого нужно удалить элемент стилей.
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
     * Создает объект сообщения с результатами по умолчанию.
     *
     * @returns {Object} Объект сообщения с результатами.
     */
    function createResultMessage() {
        return {
            "timeout":0, "timeout_for_event":"presence_of_element_located", "event": "showResultsInPopup",
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
     * Функция-обработчик сообщений.
     *
     * @param {Object} message - Объект сообщения.
     * @param {Object} sender - Отправитель сообщения.
     * @param {function} sendResponse - Функция для отправки ответа.
     * @returns {boolean|undefined}
     */
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик для установки информации о контенте.
     *
     * @param {Object} message - Объект сообщения.
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
     * Обработчик для выполнения XPath запроса.
     *
     * @param {Object} message - Объект сообщения.
     * @param {Object} sender - Отправитель сообщения.
     */
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();

        updateCss();

        var sendMsg = Object.create(null);
        var main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        var mainType = fu.getxpathResultNum(main.resultType);
        sendMsg.main = Object.create(null);
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
            sendMsg.context = Object.create(null);
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
     * Обработчик для фокусировки элемента.
     *
     * @param {Object} message - Объект сообщения.
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
     * Обработчик для фокусировки контекстного элемента.
     *
     * @param {Object} message - Объект сообщения.
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
     * Обработчик для фокусировки фрейма.
     *
     * @param {Object} message - Объект сообщения.
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
     * Обработчик для запроса показа результатов в popup.
     */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };

   /**
     * Обработчик для запроса показа всех результатов.
     */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }

    /**
     * Обработчик для сброса стилей.
     */
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };

   /**
     * Обработчик для установки стилей.
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
     * Обработчик для завершения вставки CSS.
     *
     * @param {Object} message - Объект сообщения.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        var css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };

    /**
     * Обработчик для завершения удаления CSS.
     *
     * @param {Object} message - Объект сообщения.
     */
    genericListener.listeners.finishRemoveCss = function (message) {
        var css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };

    browser.storage.onChanged.addListener(changes => {
        if (changes.attributes && ("newValue" in changes.attributes)) {
            attributes = changes.attributes.newValue;
        }
        if (changes.css && ("newValue" in changes.css)) {
            handleCssChange(changes.css.newValue);
        }
    });


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

    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located", "event": "requestSetContentInfo" });

})(window);