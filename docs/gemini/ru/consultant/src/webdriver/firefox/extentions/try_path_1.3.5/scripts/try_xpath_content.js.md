# Анализ кода модуля `try_xpath_content.js`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что улучшает читаемость и поддержку.
    - Используются константы для строк и значений, что облегчает модификацию и понимание.
    - Присутствует обработка ошибок, хотя и в основном через try-catch, которая должна быть переделана.
    - Есть механизм для сохранения и восстановления атрибутов элементов.
    - Имеется поддержка работы с фреймами.
-  Минусы
    - Отсутствуют docstring для функций и переменных.
    -  Много стандартных блоков `try-except`, которые можно заменить на `logger.error`.
    -  Не все функции используют возможности `fu` (tryxpath.functions).
    -  Смешивание стилей написания кода (например, использование `var` и `let`/`const`).
    -  Использование `Object.create(null)` выглядит избыточным в некоторых местах.
    -  Многократное использование `browser.runtime.sendMessage` с одними и теми же параметрами.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring в формате RST для всех функций и переменных.
2.  **Логирование**: Использовать `logger.error` для логирования ошибок вместо `try-catch` блоков.
3.  **Использование `fu`**: Пересмотреть код и использовать `fu` там, где это возможно, для унификации доступа к DOM.
4.  **Стиль кода**: Привести код к единому стилю, использовать `const` для констант, `let` для изменяемых переменных.
5. **Упрощение кода**: Упростить создание сообщений, чтобы уменьшить повторения и улучшить читаемость.
6. **Убрать `Object.create(null)`**:  Заменить на обычные объекты, где это уместно.
7.  **Унификация**: Избегать дублирования кода, например, при отправке сообщений.
8.  **Обработка ошибок в фреймах**: Сделать обработку ошибок в фреймах более явной.
9. **Улучшить обработку CSS**: Сделать более явным добавление и удаление CSS стилей.
10. **Более ясная работа с атрибутами**: Добавить пояснения к сохранению и восстановлению атрибутов.

**Оптимизированный код**

```python
"""
Модуль для управления контентом веб-страницы с целью поиска элементов с использованием XPath.
================================================================================================

Модуль `try_xpath_content.js` является частью расширения для браузера и предоставляет функциональность для
выполнения XPath запросов на веб-странице и отображения результатов в пользовательском интерфейсе расширения.
Модуль взаимодействует с фоновым скриптом расширения, отправляя сообщения для отображения результатов и обработки
изменений в стилях CSS. Модуль также обрабатывает события focus и scroll для выделения найденных элементов на странице.

.. note::
    Этот модуль предназначен для работы в контексте веб-страницы.
    Он получает сообщения от фонового скрипта и выполняет операции непосредственно на странице.

"""
import json
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
# /* This Source Code Form is subject to the terms of the Mozilla Public
#  * License, v. 2.0. If a copy of the MPL was not distributed with this
#  * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

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
     * Сохраняет и устанавливает атрибут для элемента.
     *
     * :param attr: Атрибут для установки.
     * :param value: Значение атрибута.
     * :param item: Элемент, которому устанавливается атрибут.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };

    /**
     * Сохраняет и устанавливает атрибут для списка элементов.
     *
     * :param attr: Атрибут для установки.
     * :param items: Список элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };

    /**
     * Проверяет, является ли элемент доступным для фокусировки.
     *
     * :param item: Проверяемый элемент.
     * :return: True, если элемент доступен для фокусировки, иначе False.
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
     * :param item: Элемент, на который устанавливается фокус.
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
     * Устанавливает основные атрибуты для контекстного и текущих элементов.
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
     * Сбрасывает предыдущие результаты.
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
     * Создаёт строковое представление типа результата XPath.
     *
     * :param resultType: Тип результата XPath.
     * :return: Строковое представление типа результата.
     */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };

    /**
     * Обновляет стили CSS, отправляя сообщение расширению.
     */
    function updateCss() {
       # Проверяется, нужно ли обновить CSS.
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)) {
           # Отправляется сообщение расширению для обновления CSS.
            browser.runtime.sendMessage({
                "timeout":0,
                "timeout_for_event":"presence_of_element_located",
                "event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };

    /**
     * Получает фреймы на основе спецификации.
     *
     * :param spec: Строка, представляющая спецификацию фреймов.
     * :return: Массив фреймов.
     * :raises Error: Если спецификация неверна.
     */
    function getFrames(spec) {
        try {
             #  Парсинг спецификации фреймов из JSON.
            var inds = JSON.parse(spec);
             #  Проверка, что спецификация - массив чисел.
            if (fu.isNumberArray(inds) && (inds.length > 0)) {
                 # Возвращается массив фреймов.
                return fu.getFrameAncestry(inds).reverse();
            } else {
                throw new Error("Invalid specification. [" + spec + "]");
            }
        }
        catch (e) {
            logger.error("Ошибка при получении фреймов", e)
             #   Возвращается пустой массив в случае ошибки.
            return [];
        }
    };

    /**
     * Парсит обозначение фрейма.
     *
     * :param frameDesi: Строка, представляющая обозначение фрейма.
     * :return: Массив индексов фреймов.
     * :raises Error: Если обозначение неверно.
     */
    function parseFrameDesignation(frameDesi) {
         #  Парсинг обозначения фреймов из JSON.
        var inds = JSON.parse(frameDesi);
         # Проверка, что обозначение - массив чисел.
        if (fu.isNumberArray(inds) && (inds.length > 0)) {
             # Возвращается массив индексов фреймов.
            return inds;
        } else {
             #  Выбрасывается ошибка, если обозначение неверно.
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }
    };

    /**
     * Проверяет наличие фреймов с указанными индексами.
     *
     * :param desi: Массив индексов фреймов.
     * :param win: Родительское окно.
     * :return: Объект с результатами проверки фреймов.
     */
    function traceBlankWindows(desi, win) {
        win = win || window;
        var result = {};

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
     * Обрабатывает изменение CSS, обновляя текущий CSS и список устаревших стилей.
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
        # Если newCss и currentCss - одна и та же строка, ничего не происходит.
    };

    /**
     * Находит элемент фрейма по сообщению.
     *
     * :param event: Событие сообщения.
     * :param win: Родительское окно.
     * :return: Элемент фрейма.
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
     * Устанавливает слушателя сообщений для фрейма.
     *
     * :param win: Окно фрейма.
     * :param isBlankWindow: Является ли окно пустым.
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
     * Инициализирует пустое окно.
     *
     * :param win: Окно для инициализации.
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
    };

    /**
     * Находит родительский элемент для стилей.
     *
     * :param doc: Документ для поиска.
     * :return: Родительский элемент для стилей.
     */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };

    /**
     * Обновляет стили в элементе style.
     *
     * :param doc: Документ, в котором обновляется стиль.
     */
    function updateStyleElement(doc) {
         #  Получение текущего CSS или пустой строки.
        var css = currentCss || "";
         #  Добавление заголовка к CSS.
        css = styleElementHeader + css;

         # Получение style элемента из Map.
        var style = insertedStyleElements.get(doc);
         #  Обновление текста, если style существует.
        if (style) {
            style.textContent = css;
            return;
        }

         #  Поиск родителя для style элемента.
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
     * Обновляет все стили в элементах style.
     */
    function updateAllStyleElements() {
         #  Получение текущего CSS или пустой строки.
        var css = currentCss || "";
         #  Добавление заголовка к CSS.
        css = styleElementHeader + css;
         # Перебор Map и обновление текста в style.
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };

    /**
     * Удаляет элемент style.
     *
     * :param doc: Документ, из которого удаляется стиль.
     */
    function removeStyleElement(doc) {
         #  Получение элемента style из Map.
        var elem = insertedStyleElements.get(doc);
         #  Выход, если элемент не найден.
        if (!elem) {
            return;
        }

         #  Получение родителя элемента style.
        var parent = elem.parentNode;
        if (parent) {
             #  Удаление элемента style из родителя.
            parent.removeChild(elem);
        }
        # Удаление элемента из Map.
        insertedStyleElements.delete(doc);
    };

    /**
     * Удаляет все элементы style.
     */
    function removeAllStyleElements() {
         #  Перебор всех style элементов и удаление их.
        for (let [doc, elem] of insertedStyleElements) {
            let parent = elem.parentNode;
            if (parent) {
                parent.removeChild(elem);
            }
        }
        # Очистка Map.
        insertedStyleElements.clear();
    };

    /**
     * Создаёт объект сообщения результата по умолчанию.
     *
     * :return: Объект сообщения результата.
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
     * Вызывает соответствующий обработчик сообщения.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     * :param sendResponse: Функция для отправки ответа.
     * :return: Результат выполнения обработчика.
     */
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = {};
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обрабатывает сообщение для установки информации о контенте.
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
     * Обрабатывает сообщение для выполнения XPath запроса.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     */
    genericListener.listeners.execute = function(message, sender) {
         #  Сброс предыдущих результатов.
        resetPrev();

         #  Обновление CSS.
        updateCss();

         # Создание объекта сообщения.
        var sendMsg = {};
        var main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

         # Получение числового значения типа результата XPath.
        var mainType = fu.getxpathResultNum(main.resultType);
        sendMsg.main = {};
        sendMsg.main.method = main.method;
        sendMsg.main.expression = main.expression;
        sendMsg.main.specifiedResultType = makeTypeStr(mainType);
        sendMsg.main.resultType = "";
        sendMsg.main.resolver = main.resolver || "";
        sendMsg.main.itemDetails = [];

         #  Установка контекстного элемента как документа.
        contextItem = document;
        currentDocument = document;

         # Обработка спецификации фрейма.
        if ("frameDesignation" in message) {
            sendMsg.frameDesignation = message.frameDesignation;

            try {
                 #  Получение спецификации фрейма.
                let desi = parseFrameDesignation(message.frameDesignation);
                 # Проверка пустых окон.
                let res = traceBlankWindows(desi, window);
                if (!res.success) {
                    if (res.failedWindow === null) {
                        throw new Error(
                            "The specified frame does not exist.");
                    } else {
                         # Отправка сообщения в фрейм.
                        res.failedWindow.postMessage({
                            "message": "tryxpath-request-message-to-popup",
                            "messageId": 1
                        }, "*");
                        return;
                    }
                }
                # Обновление контекстного элемента.
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

         # Удаление стилей для пустых окон.
        if (inBlankWindow) {
            removeStyleElement(currentDocument);
        }

         # Обработка контекста.
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

             # Проверка наличия контекста.
            if (contRes.items.length === 0) {
                sendMsg.message = "A context is not found.";
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }
             #  Обновление контекстного элемента.
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

         #  Установка основных атрибутов.
        setMainAttrs();
        if (inBlankWindow) {
             #  Обновление стилей для пустых окон.
            updateStyleElement(currentDocument);
        }
        return;
    }

    /**
     * Обрабатывает сообщение для установки фокуса на элемент.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.focusItem = function(message) {
         # Проверяет, что сообщение относится к текущему выполнению.
        if (message.executionId === executionCount) {
             # Обновление стилей в пустом окне.
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
             # Установка фокуса на элемент.
            focusItem(currentItems[message.index]);
        }
    };

    /**
     * Обрабатывает сообщение для установки фокуса на контекстный элемент.
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
     * Обрабатывает сообщение для установки фокуса на фрейм.
     *
     * :param message: Сообщение.
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
                         # Отправка сообщения в фрейм.
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
         # Отправка сообщения для установки фокуса на фрейм.
        if (win !== win.top) {
            win.parent.postMessage({
                "message": "tryxpath-focus-frame",
                "index": 0,
                "frameIndex": fu.findFrameIndex(win, win.parent)
            }, "*");
        }
    };

    /**
     * Обрабатывает запрос на отображение результатов во всплывающем окне.
     */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };

    /**
     * Обрабатывает запрос на отображение всех результатов.
     */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }

    /**
     * Обрабатывает запрос на сброс стилей.
     */
    genericListener.listeners.resetStyle = function () {
         # Восстановление атрибутов.
        restoreAttrs();
         #  Удаление всех элементов style.
        removeAllStyleElements();
    };

    /**
     * Обрабатывает запрос на установку стилей.
     */
    genericListener.listeners.setStyle = function () {
         # Восстановление атрибутов.
        restoreAttrs();
         # Обновление CSS.
        updateCss();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
         # Установка основных атрибутов.
        setMainAttrs();
    };

    /**
     * Обрабатывает завершение добавления CSS.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        var css = message.css;
        currentCss = css;
        delete expiredCssSet[css];
         # Обновление стилей.
        updateAllStyleElements();
    };

    /**
     * Обрабатывает завершение удаления CSS.
     *
     * :param message: Сообщение.
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

     #  Инициализация сообщения по умолчанию.
    prevMsg = createResultMessage();
     #  Установка слушателя для фрейма.
    setFocusFrameListener(window, false);

    browser.runtime.sendMessage({
        "timeout":0,
        "timeout_for_event":"presence_of_element_located",
        "event": "requestSetContentInfo"
    });

})(window);
```