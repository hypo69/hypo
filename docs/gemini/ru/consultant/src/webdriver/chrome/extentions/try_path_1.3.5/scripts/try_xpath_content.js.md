# Анализ кода модуля `try_xpath_content.js`

**Качество кода**
7
- Плюсы
    - Код разбит на функции, что делает его более читаемым и поддерживаемым.
    - Используются константы для строк и атрибутов, что уменьшает вероятность ошибок.
    - Присутствует обработка ошибок, хотя и не всегда в оптимальном стиле.
    - Есть механизм предотвращения многократного выполнения скрипта `tx.isContentLoaded`.
- Минусы
    - Много кода в глобальной области видимости.
    - Используются устаревшие конструкции типа `Object.create(null)`.
    - Не все ошибки обрабатываются с использованием `logger.error`.
    - Комментарии не соответствуют формату reStructuredText (RST).
    - Некоторые функции не имеют docstring.
    - Имена переменных и функций не всегда соответствуют общепринятым стандартам (например, `desi` вместо `designation`).
    - Обработка сообщений от расширения и фреймов не всегда логична и понятна.
    - Код использует `browser.runtime.sendMessage` для отправки сообщений, что является специфичным для расширений браузера и не может быть использовано в других контекстах без адаптации.
    - Присутствует устаревший метод `Object.create(null)` вместо использования простых литералов `{}`,
    - В коде много мест, где можно было бы использовать более идиоматичные способы для написания кода на JavaScript
    - Не всегда понятно какие данные и в каком формате передаются и как происходит взаимодействие между компонентами расширения.
    - Использование `window.addEventListener("message", ...)` для обмена сообщениями между фреймами и основным окном усложняет понимание логики и может привести к проблемам с масштабированием.
    - Не хватает документации для функций и переменных.

**Рекомендации по улучшению**

1.  **Импорты и зависимости:**
    *   Добавить импорт `logger` из `src.logger.logger` для логирования ошибок.
    *   Убедиться, что все необходимые функции из `tryxpath` и `tryxpath.functions` импортируются правильно.

2.  **Формат документации:**
    *   Переписать все комментарии в формате RST, включая описание модуля, функций и переменных.
    *   Добавить docstring к каждой функции.

3.  **Обработка ошибок:**
    *   Заменить стандартные блоки `try-except` на использование `logger.error` для логирования ошибок.
    *   Обеспечить обработку всех возможных исключений.

4.  **Имена переменных и функций:**
    *   Привести имена переменных и функций к единому стилю (например, camelCase).
    *   Использовать более описательные имена.

5.  **Структура кода:**
    *   Разделить код на более мелкие функции для повышения читаемости и повторного использования.
    *   Инкапсулировать некоторые переменные и функции в объекты или замыкания, чтобы уменьшить глобальную область видимости.

6. **Безопасность:**
    * Внимательно проверить места, где происходит обращение к `window.frames` и `window.parent`, чтобы избежать потенциальных ошибок безопасности.

7. **Улучшение стиля:**
  * Использовать литералы объектов `{}`, вместо устаревшего `Object.create(null)`
  * Использовать `const` везде, где это возможно, вместо `var`

**Оптимизированный код**

```javascript
/*
 Модуль для работы с XPath в контексте расширения браузера.
 =========================================================================================

 Этот модуль содержит функции для выполнения XPath запросов, управления стилями и взаимодействия с фреймами.

 Пример использования
 --------------------

 .. code-block:: javascript

   // Выполнение XPath запроса
   genericListener.listeners.execute(message, sender);

   // Фокусировка на элементе
   genericListener.listeners.focusItem(message);

   // Обновление стилей
   genericListener.listeners.setStyle();
 */
import { logger } from '../../logger/logger.js';

(function (window, undefined) {
    "use strict";

    // alias
    const tx = tryxpath;
    const fu = tryxpath.functions;

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
    const insertedStyleElements = new Map();
    const expiredCssSet = Object.create(null);
    let originalAttributes = new Map();
    

    /**
     * Сохраняет и устанавливает атрибут для элемента.
     *
     * :param attr: Имя атрибута.
     * :param value: Значение атрибута.
     * :param item: Элемент, для которого нужно установить атрибут.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    }

    /**
     * Сохраняет и устанавливает атрибут индекса для списка элементов.
     *
     * :param attr: Имя атрибута.
     * :param items: Список элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    }

     /**
     * Проверяет, является ли элемент фокусируемым.
     *
     * :param item: Элемент для проверки.
     * :return: True, если элемент фокусируемый, иначе False.
     */
    function isFocusable(item) {
        if (!item) {
            return false;
        }
        if (fu.isNodeItem(item) || fu.isAttrItem(item)) {
            return true;
        }
        return false;
    }

    /**
     * Фокусирует элемент и устанавливает соответствующие атрибуты.
     *
     * :param item: Элемент для фокусировки.
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
    }
    
    /**
     * Устанавливает основные атрибуты для контекстного элемента и списка элементов.
     */
    function setMainAttrs() {
        if (contextItem !== null) {
            setAttr(attributes.context, "true", contextItem);
        }
        setIndex(attributes.element, currentItems);
    }

    /**
     * Восстанавливает оригинальные атрибуты элементов.
     */
    function restoreAttrs() {
        fu.restoreItemAttrs(originalAttributes);
        originalAttributes = new Map();
    }

    /**
     * Сбрасывает предыдущие значения и устанавливает начальные значения переменных.
     */
    function resetPrev() {
        restoreAttrs();

        contextItem = dummyItem;
        currentItems = dummyItems;
        focusedItem = dummyItem;
        focusedAncestorItems = dummyItems;

        prevMsg = createResultMessage();
        executionCount++;
    }

    /**
     * Создает строку с типом результата XPath.
     *
     * :param resultType: Тип результата.
     * :return: Строка с типом результата.
     */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    }

    /**
     * Обновляет стили CSS, если есть изменения.
     */
    function updateCss() {
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    }

    /**
     * Получает фреймы на основе спецификации.
     *
     * :param spec: Спецификация фреймов в виде JSON.
     * :return: Массив фреймов.
     * :raises Error: Если спецификация неверна.
     */
    function getFrames(spec) {
        try {
             const inds = JSON.parse(spec);
             if (fu.isNumberArray(inds) && (inds.length > 0)) {
                 return fu.getFrameAncestry(inds).reverse();
             } else {
                throw new Error("Invalid specification. [" + spec + "]");
            }
        } catch (e){
            logger.error('Ошибка при парсинге спецификации фреймов', e)
            return [];
        }
       
    }

    /**
     * Разбирает обозначение фрейма из JSON.
     *
     * :param frameDesi: Обозначение фрейма в виде JSON.
     * :return: Массив индексов фреймов.
     * :raises Error: Если обозначение неверно.
     */
    function parseFrameDesignation(frameDesi) {
        try {
             const inds = JSON.parse(frameDesi);
             if (fu.isNumberArray(inds) && (inds.length > 0)) {
                return inds;
             } else {
                 throw new Error("Invalid specification. [" + frameDesi + "]");
             }
        }  catch (e){
            logger.error('Ошибка при парсинге обозначения фрейма', e)
            return [];
        }
    }

    /**
     * Отслеживает пустые окна на основе их обозначения.
     *
     * :param desi: Массив индексов фреймов.
     * :param win: Начальное окно.
     * :return: Объект с результатами отслеживания.
     */
     function traceBlankWindows(desi, win) {
        win = win || window;
        const result = {};
    
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
    }

    /**
     * Обрабатывает изменения CSS.
     *
     * :param newCss: Новый CSS.
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
    }
    
    /**
     * Находит элемент фрейма по сообщению.
     *
     * :param event: Событие сообщения.
     * :param win: Окно.
     * :return: Элемент фрейма.
     */
    function findFrameByMessage(event, win) {
        let ind = event.data.frameIndex;
        let subWin;
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    }

    /**
     * Устанавливает слушатель сообщений для фокусировки на фрейме.
     *
     * :param win: Окно.
     * :param isBlankWindow: Флаг, указывающий, является ли окно пустым.
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
     }

    /**
     * Инициализирует пустое окно.
     *
     * :param win: Окно.
     */
    function initBlankWindow(win) {
        if (!win.tryxpath) {
            win.tryxpath = {};
        }

        if (win.tryxpath.isInitialized) {
            return;
        }
        win.tryxpath.isInitialized = true;

        setFocusFrameListener(win, true);
    }

    /**
     * Находит родительский элемент для стиля.
     *
     * :param doc: Документ.
     * :return: Родительский элемент.
     */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    }

    /**
     * Обновляет элемент стиля.
     *
     * :param doc: Документ.
     */
    function updateStyleElement(doc) {
        let css = currentCss || "";
        css = styleElementHeader + css;

        let style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }

        let parent = findStyleParent(doc);
        if (parent) {
            let newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    }

    /**
     * Обновляет все элементы стиля.
     */
    function updateAllStyleElements() {
        let css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    }

    /**
     * Удаляет элемент стиля.
     *
     * :param doc: Документ.
     */
    function removeStyleElement(doc) {
        let elem = insertedStyleElements.get(doc);
        
        if (!elem) {
            return;
        }

        let parent = elem.parentNode;
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    }

    /**
     * Удаляет все элементы стиля.
     */
    function removeAllStyleElements() {
         for (let [doc, elem] of insertedStyleElements) {
            let parent = elem.parentNode;
            if (parent) {
                parent.removeChild(elem);
            }
        }
        insertedStyleElements.clear();
    }

    /**
     * Создает объект сообщения о результате.
     *
     * :return: Объект сообщения о результате.
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
    }

    /**
     * Слушатель сообщений для обработки событий.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     * :param sendResponse: Функция для отправки ответа.
     */
     function genericListener(message, sender, sendResponse) {
        let listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    }
    genericListener.listeners = {};
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Устанавливает информацию о контенте.
     *
     * :param message: Сообщение.
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
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     */
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();

        updateCss();

        const sendMsg = {};
        const main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        const mainType = fu.getxpathResultNum(main.resultType);
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
                 const desi = parseFrameDesignation(message.frameDesignation);
                const res = traceBlankWindows(desi, window);
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
    };

    /**
     * Фокусирует элемент из результата запроса.
     *
     * :param message: Сообщение.
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
     * Фокусирует контекстный элемент.
     *
     * :param message: Сообщение.
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
     * Фокусирует фрейм.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.focusFrame = function(message) {
        let win = window;
        if ("frameDesignation" in message) {
           try {
                const desi = parseFrameDesignation(message.frameDesignation);
                 const res = traceBlankWindows(desi, window);
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
     * Сбрасывает стиль.
     */
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };

    /**
     * Устанавливает стиль.
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
     * Завершает вставку CSS.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        let css = message.css;
        currentCss = css;
        delete expiredCssSet[css];
        updateAllStyleElements();
    };

    /**
     * Завершает удаление CSS.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.finishRemoveCss = function (message) {
         let css = message.css;
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
    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });
})(window);
```