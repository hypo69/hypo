# Анализ кода модуля try_xpath_content.js

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Присутствуют комментарии, описывающие основные блоки кода.
    - Используется `Map` для хранения данных, что обеспечивает более эффективную работу с ключами.
    - Функции стараются быть чистыми и выполнять одну конкретную задачу.
-  Минусы
    -  Отсутствует документация в формате reStructuredText (RST) для функций, классов и переменных.
    - Используются стандартные блоки `try-except`, что не соответствует требованиям.
    - Некоторые переменные объявлены с `var` вместо `const` или `let`.
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Имена переменных и функций местами не соответствуют стилю ранее обработанных файлов.

**Рекомендации по улучшению**

1.  Добавить документацию в формате reStructuredText (RST) для всех функций, переменных и модуля.
2.  Заменить использование `var` на `const` или `let` там, где это возможно.
3.  Заменить стандартные блоки `try-except` на обработку ошибок с использованием `logger.error`.
4.  Привести имена переменных и функций в соответствие с ранее обработанными файлами.
5.  Добавить проверки на наличие необходимых ключей в объектах сообщений для предотвращения ошибок.
6.  Улучшить читаемость кода за счёт более подробных комментариев.

**Оптимизированный код**

```python
"""
Модуль для обработки XPath запросов и управления стилями на веб-странице.
=========================================================================================

Этот модуль содержит функции для выполнения XPath запросов, управления стилями элементов на странице,
взаимодействия с фоном расширения и обработки сообщений от других частей расширения.

Пример использования
--------------------

Пример инициализации модуля:

.. code-block:: javascript

    (function (window, undefined) {
        "use strict";
        // ... код модуля ...
    })(window);
"""
import { logger } from '../../../src/logger/logger';
(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    # prevent multiple execution
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
     * @type {Object}
     * @description Объект, содержащий атрибуты для элементов.
     */
    let attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"        
    };

    let prevMsg;
    let executionCount = 0;
    let inBlankWindow = false;
    let currentDocument = null;
    let contextItem = dummyItem;
    let currentItems = dummyItems;
    let focusedItem = dummyItem;
    let focusedAncestorItems = dummyItems;
    let currentCss = null;
    /**
     * @type {Map<Document, HTMLStyleElement>}
     * @description Map для хранения HTMLStyleElement для каждого документа.
     */
    const insertedStyleElements = new Map();
    /**
     * @type {Object}
     * @description Объект для отслеживания истекших CSS стилей.
     */
    const expiredCssSet = Object.create(null);
    /**
     * @type {Map<HTMLElement | Attr, Object>}
     * @description Map для хранения оригинальных атрибутов элементов.
     */
    let originalAttributes = new Map();
    
    /**
     * Сохраняет и устанавливает атрибут для элемента.
     *
     * @param {string} attr Имя атрибута.
     * @param {string} value Значение атрибута.
     * @param {HTMLElement | Attr} item Элемент, которому нужно установить атрибут.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };

    /**
     * Сохраняет и устанавливает атрибут индекса для набора элементов.
     *
     * @param {string} attr Имя атрибута.
     * @param {Array<HTMLElement | Attr>} items Массив элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };

    /**
     * Проверяет, является ли элемент фокусируемым.
     *
     * @param {HTMLElement | Attr} item Элемент для проверки.
     * @returns {boolean} True, если элемент фокусируемый, иначе - False.
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
     * Устанавливает фокус на элемент.
     *
     * @param {HTMLElement | Attr} item Элемент для фокуса.
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
     * Устанавливает основные атрибуты для элементов.
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
     * Сбрасывает переменные и подготавливает к следующему выполнению.
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
     * Создает строку с типом результата XPath.
     *
     * @param {number} resultType Тип результата XPath.
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
     * Обновляет CSS стили, отправляя сообщение расширению.
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
     * Получает массив фреймов на основе спецификации.
     *
     * @param {string} spec Спецификация фрейма в виде JSON строки.
     * @returns {Array<HTMLIFrameElement>} Массив фреймов.
     * @throws {Error} Если спецификация недействительна.
     */
    function getFrames(spec) {
        try {
             var inds = JSON.parse(spec);
         } catch(e) {
            logger.error('Ошибка парсинга JSON', e);
            throw new Error("Invalid specification. [" + spec + "]");
        }

        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return fu.getFrameAncestry(inds).reverse();
        } else {
            throw new Error("Invalid specification. [" + spec + "]");
        }
    };

    /**
     * Разбирает обозначение фрейма.
     *
     * @param {string} frameDesi Обозначение фрейма в виде JSON строки.
     * @returns {Array<number>} Массив индексов фреймов.
     * @throws {Error} Если обозначение недействительно.
     */
    function parseFrameDesignation(frameDesi) {
        try{
        var inds = JSON.parse(frameDesi);
        } catch(e) {
           logger.error('Ошибка парсинга JSON', e);
           throw new Error("Invalid specification. [" + frameDesi + "]");
        }

        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return inds;
        } else {
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }
    };

     /**
      * Прослеживает фреймы в пустых окнах.
      *
      * @param {Array<number>} desi Массив индексов фреймов.
      * @param {Window} win Окно, в котором нужно начать отслеживание.
      * @returns {Object} Объект, содержащий результат отслеживания.
      */
    function traceBlankWindows(desi, win) {
        win = win || window;
        const result = Object.create(null);

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
     * Обрабатывает изменение CSS стилей.
     *
     * @param {string} newCss Новый CSS стиль.
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
        # If newCss and currentCss are the same string do nothing.
    };

    /**
     * Находит фрейм по сообщению.
     *
     * @param {MessageEvent} event Событие сообщения.
     * @param {Window} win Окно, в котором нужно искать фрейм.
     * @returns {HTMLIFrameElement | null} Найденный фрейм.
     */
    function findFrameByMessage(event, win) {
        if (!event || !event.data || !Number.isInteger(event.data.frameIndex)) {
             logger.error('Некорректные данные в событии при поиске фрейма.');
             return null;
        }
        const ind = event.data.frameIndex;
        let subWin;
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    };
      /**
       * Устанавливает слушатель сообщений для фокусировки фрейма.
       *
       * @param {Window} win Окно, для которого нужно установить слушатель.
       * @param {boolean} isBlankWindow Флаг, указывающий, является ли окно пустым.
       */
    function setFocusFrameListener(win, isBlankWindow) {
         let localUpdateCss;
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
     * Инициализирует пустое окно.
     *
     * @param {Window} win Пустое окно для инициализации.
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
       * @param {Document} doc Документ, для которого нужно найти родительский элемент.
       * @returns {HTMLElement | null} Родительский элемент или null.
       */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };

    /**
     * Обновляет стили в указанном документе.
     *
     * @param {Document} doc Документ, в котором нужно обновить стили.
     */
    function updateStyleElement(doc) {
        let css = currentCss || "";
        css = styleElementHeader + css;

        const style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }

        const parent = findStyleParent(doc);
        if (parent) {
            let newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    };

      /**
       * Обновляет стили во всех вставленных элементах style.
       */
    function updateAllStyleElements() {
        let css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };

       /**
       * Удаляет элемент style из документа.
       *
       * @param {Document} doc Документ, из которого нужно удалить элемент style.
       */
    function removeStyleElement(doc) {
        const elem = insertedStyleElements.get(doc);
        
        if (!elem) {
            return;
        }

        const parent = elem.parentNode;
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    };

    /**
     * Удаляет все элементы style из всех документов.
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
     * Создает объект сообщения с результатом по умолчанию.
     *
     * @returns {Object} Объект сообщения с результатом по умолчанию.
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
     * @param {Object} message Сообщение от расширения.
     * @param {Object} sender Отправитель сообщения.
     * @param {Function} sendResponse Функция для отправки ответа.
     */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
     /**
      * @type {Object}
      * @description Объект, хранящий слушатели сообщений.
      */
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Устанавливает информацию о контенте.
     *
     * @param {Object} message Сообщение с информацией о контенте.
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
     * Выполняет XPath запрос.
     *
     * @param {Object} message Сообщение с параметрами запроса.
     * @param {Object} sender Отправитель сообщения.
     */
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();

        updateCss();

        const sendMsg = Object.create(null);
        const main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        const mainType = fu.getxpathResultNum(main.resultType);
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
            const cont = message.context;
            const contType = fu.getxpathResultNum(cont.resultType);
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

        let mainRes;
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
    };

    /**
     * Фокусирует элемент по индексу.
     *
     * @param {Object} message Сообщение с индексом элемента.
     */
    genericListener.listeners.focusItem = function(message) {
         if (!message || !Number.isInteger(message.executionId) || !Number.isInteger(message.index)) {
            logger.error('Некорректные данные в сообщении при фокусе элемента.');
            return;
        }
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(currentItems[message.index]);
        }
    };

    /**
     * Фокусирует контекстный элемент.
     *
     * @param {Object} message Сообщение с идентификатором выполнения.
     */
    genericListener.listeners.focusContextItem = function(message) {
         if (!message || !Number.isInteger(message.executionId)) {
            logger.error('Некорректные данные в сообщении при фокусе контекста.');
            return;
        }
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(contextItem);
        }
    };

    /**
     * Фокусирует фрейм.
     *
     * @param {Object} message Сообщение с информацией о фрейме.
     */
    genericListener.listeners.focusFrame = function(message) {
        let win = window;
        if (!message) {
            logger.error('Некорректные данные в сообщении при фокусе фрейма.');
            return;
        }
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
     * Запрашивает отображение результатов в попапе.
     */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };
      /**
       * Запрашивает отображение всех результатов.
       */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    };

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
     * Завершает вставку CSS стилей.
     *
     * @param {Object} message Сообщение с CSS стилями.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        const css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };

    /**
     * Завершает удаление CSS стилей.
     *
     * @param {Object} message Сообщение с CSS стилями.
     */
    genericListener.listeners.finishRemoveCss = function (message) {
        const css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };

     /**
      * Слушатель изменений в хранилище.
      * @param {Object} changes Объект с изменениями в хранилище
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
      * Слушатель сообщений от окна.
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

    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });

})(window);
```