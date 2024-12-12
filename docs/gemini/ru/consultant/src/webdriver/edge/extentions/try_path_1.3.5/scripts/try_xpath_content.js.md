# Анализ кода модуля try_xpath_content.js

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код достаточно хорошо структурирован и разбит на функции.
    *   Используются константы для атрибутов, что улучшает читаемость и облегчает поддержку.
    *   Есть обработка сообщений от расширения.
    *   Функции разделены по назначению и легко читаются.
*   **Минусы:**
    *   Не все функции имеют docstring, что затрудняет понимание их назначения.
    *   Отсутствует логирование ошибок с использованием `logger.error`.
    *   Много `try-catch` блоков, которые можно заменить на логирование ошибок.
    *   Некоторые переменные объявлены с `var` вместо `const` или `let`.
    *   Обработка ошибок в основном сводится к формированию сообщений для пользователя, но не логируются для отладки.
    *   Не все комментарии написаны в формате RST.
    *   Сложная логика управления стилями, которая может быть упрощена.
    *   Используется много `Object.create(null)`, что может быть не всегда оптимально.

**Рекомендации по улучшению:**

1.  **Добавить docstring:** Ко всем функциям, методам и переменным добавить docstring в формате RST для улучшения читаемости и поддержки кода.
2.  **Логирование ошибок:** Использовать `from src.logger.logger import logger` для логирования ошибок вместо `try-catch` блоков, где это возможно.
3.  **Переменные:** Использовать `const` и `let` вместо `var` для объявления переменных.
4.  **Упрощение логики:** Упростить логику управления стилями.
5.  **Форматирование:** Привести все комментарии в RST формат.
6.  **Использовать `j_loads`:** заменить `JSON.parse` на `j_loads` из `src.utils.jjson`.
7.  **Улучшить обработку ошибок:** Заменить формирование сообщений об ошибках на использование `logger.error` с выводом стектрейса.
8.  **Рефакторинг:** Использовать более современные методы javascript.

**Оптимизированный код:**

```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    /**
     * Модуль для взаимодействия со страницей и выполнения XPath запросов.
     *
     * Содержит функции для выделения элементов на странице, добавления стилей,
     * и управления фреймами.
     *
     */

    // alias
    const tx = tryxpath;
    const fu = tryxpath.functions;
    // # Объявление псевдонимов для доступа к функциям `tryxpath`

    // prevent multiple execution
    if (tx.isContentLoaded) {
        return;
    }
    tx.isContentLoaded = true;
    // # Проверка, был ли уже загружен контент для избежания повторного выполнения

    const dummyItem = "";
    const dummyItems = [];
    const invalidExecutionId = NaN;
    const styleElementHeader
          = "/* This style element was inserted by browser add-on, Try xpath."
          + " If you want to remove this element, please click the reset"
          + " style button in the popup. */\\n";
    // # Объявление констант для использования в коде

    let attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"        
    };
    // # Объявление объекта с атрибутами для элементов

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
    const originalAttributes = new Map();
    // # Объявление переменных для хранения текущего состояния

    /**
     * Устанавливает атрибут элементу и сохраняет его оригинальное значение.
     *
     * :param attr: Атрибут для установки.
     * :param value: Значение атрибута.
     * :param item: Элемент, которому устанавливается атрибут.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };
    // # Функция устанавливает атрибут элементу и сохраняет исходный атрибут

    /**
     * Устанавливает индекс элементам и сохраняет их оригинальные значения атрибутов.
     *
     * :param attr: Атрибут для установки.
     * :param items: Массив элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };
    // # Функция устанавливает индекс элементам и сохраняет исходные атрибуты

    /**
     * Проверяет, является ли элемент фокусируемым.
     *
     * :param item: Элемент для проверки.
     * :return: `true`, если элемент фокусируемый, иначе `false`.
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
    // # Функция проверяет, является ли элемент фокусируемым

    /**
     * Фокусирует элемент и подсвечивает его родительские элементы.
     *
     * :param item: Элемент для фокусировки.
     */
    function focusItem(item) {
        fu.removeAttrFromItem(attributes.focused, focusedItem);
        fu.removeAttrFromItems(attributes.focusedAncestor,
                               focusedAncestorItems);
        // # Удаляет атрибуты фокуса с предыдущих элементов
        

        if (!isFocusable(item)) {
            return;
        }
        // # Проверяет, является ли элемент фокусируемым

        if (fu.isElementItem(item)) {
            focusedItem = item;
        } else {
            focusedItem = fu.getParentElement(item);
        }
        // # Устанавливает `focusedItem` на элемент или его родительский элемент, если передан атрибут

        focusedAncestorItems = fu.getAncestorElements(focusedItem);
        // # Получает список родительских элементов `focusedItem`

        setAttr(attributes.focused, "true", focusedItem);
        setIndex(attributes.focusedAncestor, focusedAncestorItems);
        // # Устанавливает атрибуты фокуса на элементе и его родительских элементах

        focusedItem.blur();
        focusedItem.focus();
        focusedItem.scrollIntoView();
         // # Устанавливает фокус на элементе
    };
    // # Функция устанавливает фокус на элемент и подсвечивает его предков

    /**
     * Устанавливает основные атрибуты для контекстного элемента и текущих элементов.
     */
    function setMainAttrs() {
        if (contextItem !== null) {
            setAttr(attributes.context, "true", contextItem);
        }
        setIndex(attributes.element, currentItems);
    };
    // # Функция устанавливает основные атрибуты для контекста и текущих элементов

    /**
     * Восстанавливает оригинальные атрибуты элементов.
     */
    function restoreAttrs() {
        fu.restoreItemAttrs(originalAttributes);
        originalAttributes.clear();
    };
     // # Функция восстанавливает исходные атрибуты элементов

    /**
     * Сбрасывает состояние и подготавливает к следующему выполнению.
     */
    function resetPrev() {
        restoreAttrs();
        // # Восстанавливает исходные атрибуты

        contextItem = dummyItem;
        currentItems = dummyItems;
        focusedItem = dummyItem;
        focusedAncestorItems = dummyItems;
         // # Сбрасывает переменные состояния

        prevMsg = createResultMessage();
        executionCount++;
         // # Создает сообщение результата и инкрементирует счетчик выполнения
    };
    // # Функция сбрасывает предыдущие результаты

    /**
     * Формирует строку с типом результата XPath.
     *
     * :param resultType: Числовой код типа результата.
     * :return: Строка с типом результата или пустая строка.
     */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };
    // # Функция формирует строку с типом результата XPath

    /**
     * Обновляет CSS стили, отправляя сообщение в расширение.
     *
     */
    function updateCss() {
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };
     // # Функция отправляет сообщение для обновления CSS

     /**
     * Извлекает массив индексов фреймов из строки спецификации.
     *
     * :param spec: Строка спецификации фреймов в формате JSON.
     * :return: Массив индексов фреймов.
     * :raises Error: Если спецификация неверна.
     */
    function getFrames(spec) {
        try {
            const inds = j_loads(spec);
            if (fu.isNumberArray(inds) && (inds.length > 0)) {
               return fu.getFrameAncestry(inds).reverse();
            } else {
                throw new Error("Invalid specification. [" + spec + "]");
            }
        } catch (e) {
            logger.error(`Ошибка при разборе спецификации фрейма: ${spec}`, e);
            throw new Error(`Ошибка при разборе спецификации фрейма: ${e.message}`);
        }

    };
    // # Функция для получения фреймов по спецификации

     /**
      * Разбирает строку, представляющую обозначение фрейма.
      *
      * :param frameDesi: Строка в формате JSON, представляющая индексы фреймов.
      * :return: Массив числовых индексов фреймов.
      * :raises Error: Если строка не является корректным массивом чисел.
      */
    function parseFrameDesignation(frameDesi) {
         try {
            const inds = j_loads(frameDesi);
            if (fu.isNumberArray(inds) && (inds.length > 0)) {
                return inds;
            } else {
                throw new Error("Invalid specification. [" + frameDesi + "]");
            }
         } catch (e) {
             logger.error(`Ошибка при разборе обозначения фрейма: ${frameDesi}`, e);
             throw new Error(`Ошибка при разборе обозначения фрейма: ${e.message}`);
        }
    };
     // # Функция для разбора обозначения фрейма

     /**
      * Отслеживает окна, которые являются пустыми фреймами.
      *
      * :param desi: Массив индексов фреймов.
      * :param win: Начальное окно для отслеживания.
      * :return: Объект с результатами отслеживания.
      *         Объект содержит:
      *           - `windows`: Массив окон-фреймов.
      *           - `failedWindow`: Окно, в котором не удалось найти фрейм, или `null`.
      *           - `success`: Логическое значение, показывающее, успешно ли отслеживание.
      */
    function traceBlankWindows(desi, win) {
        win = win || window;
        const result = Object.create(null);

        result.windows = [];
        for (let i = 0; i < desi.length; i++) {
            const frameInd = desi[i];
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
    // # Функция отслеживает пустые окна

    /**
     * Обрабатывает изменение CSS стилей.
     *
     * :param newCss: Новая CSS строка.
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
     // # Функция обрабатывает изменения CSS стилей

     /**
      * Находит элемент фрейма по сообщению.
      *
      * :param event: Событие сообщения.
      * :param win: Окно, в котором искать фрейм.
      * :return: Найденный элемент фрейма или `undefined`, если не найден.
      */
    function findFrameByMessage(event, win) {
        const ind = event.data.frameIndex;
        let subWin;
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    };
     // # Функция находит фрейм по сообщению

    /**
     * Устанавливает слушатель сообщений для фрейма для установки фокуса.
     *
     * :param win: Окно, для которого устанавливается слушатель.
     * :param isBlankWindow: Флаг, указывающий, является ли окно пустым.
     */
    function setFocusFrameListener(win, isBlankWindow) {
        let localUpdateCss;
        if (isBlankWindow) {
            localUpdateCss = updateStyleElement.bind(null, win.document);
        } else {
            localUpdateCss = updateCss;
        }
        // # Назначает функцию обновления стилей

        win.addEventListener("message", (event) => {
            if (event.data
                && event.data.message === "tryxpath-focus-frame"
                && Number.isInteger(event.data.index)
                && Number.isInteger(event.data.frameIndex)) {
                // # Проверяет, соответствует ли сообщение нужному формату
                
                const frame = findFrameByMessage(event, win);
                if (!frame) {
                    return;
                }
                // # Находит фрейм по сообщению

                const index = event.data.index;
                localUpdateCss();
                setAttr(attributes.frame, index, frame);
                setIndex(attributes.frameAncestor,
                         fu.getAncestorElements(frame));
                // # Устанавливает атрибуты фрейма и его предков

                if (win === win.top) {
                    frame.blur();
                    frame.focus();
                    frame.scrollIntoView();
                     // # Устанавливает фокус на фрейм, если это верхнее окно
                } else {
                    win.parent.postMessage({
                        "message": "tryxpath-focus-frame",
                        "index": ++index,
                        "frameIndex": fu.findFrameIndex(win, win.parent)
                    }, "*");
                    // # Отправляет сообщение родительскому окну для фокуса
                }
            }
        });
    };
     // # Функция устанавливает слушатель фокуса на фрейм

    /**
     * Инициализирует пустой фрейм, устанавливая слушатель сообщений.
     *
     * :param win: Окно фрейма для инициализации.
     */
    function initBlankWindow(win) {
        if (!win.tryxpath) {
            win.tryxpath = Object.create(null);
        }

        if (win.tryxpath.isInitialized) {
            return;
        }
        win.tryxpath.isInitialized = true;
        // # Устанавливает флаг инициализации

        setFocusFrameListener(win, true);
    };
    // # Функция инициализирует пустое окно

    /**
     * Находит родительский элемент для вставки стилей.
     *
     * :param doc: Документ, в котором искать родителя.
     * :return: Родительский элемент или `null`.
     */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };
    // # Функция находит родителя для стилей

    /**
     * Обновляет или добавляет элемент стилей в документ.
     *
     * :param doc: Документ, в котором обновлять стили.
     */
    function updateStyleElement(doc) {
        let css = currentCss || "";
        css = styleElementHeader + css;
        // # Формирует CSS строку

        let style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }
        // # Обновляет существующий стиль, если он есть

        const parent = findStyleParent(doc);
        if (parent) {
            const newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
             // # Создает и добавляет новый стиль, если нет существующего
        }
    };
    // # Функция обновляет стили

    /**
     * Обновляет все элементы стилей во всех документах.
     */
    function updateAllStyleElements() {
        let css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };
    // # Функция обновляет все стили

    /**
     * Удаляет элемент стилей из документа.
     *
     * :param doc: Документ, из которого удалять стили.
     */
    function removeStyleElement(doc) {
        const elem = insertedStyleElements.get(doc);
        
        if (!elem) {
            return;
        }
        // # Проверяет, существует ли элемент стиля

        const parent = elem.parentNode;
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    };
     // # Функция удаляет стили из документа

    /**
     * Удаляет все элементы стилей из всех документов.
     */
    function removeAllStyleElements() {
        for (let [doc, elem] of insertedStyleElements) {
            const parent = elem.parentNode;
            if (parent) {
                parent.removeChild(elem);
            }
        }
        insertedStyleElements.clear();
    };
    // # Функция удаляет все элементы стилей

    /**
     * Создает объект сообщения результата по умолчанию.
     *
     * :return: Объект сообщения с результатами.
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
     // # Функция создает объект сообщения с результатами

     /**
      * Слушатель сообщений от расширения.
      *
      * :param message: Объект сообщения.
      * :param sender: Объект отправителя сообщения.
      * :param sendResponse: Функция для отправки ответа.
      */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);
    // # Слушатель сообщений от расширения

    /**
     * Устанавливает информацию о содержимом, такую как атрибуты.
     *
     * :param message: Объект сообщения с информацией.
     */
    genericListener.listeners.setContentInfo = function (message) {
        if (!message) {
            return;
        }

        if ("attributes" in message) {
            attributes = message.attributes;
        }
    };
     // # Функция для установки информации о контенте

    /**
     * Обрабатывает выполнение XPath запроса.
     *
     * :param message: Объект сообщения с данными запроса.
     * :param sender: Объект отправителя сообщения.
     */
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();
        // # Сбрасывает предыдущие результаты

        updateCss();
        // # Обновляет CSS

        const sendMsg = Object.create(null);
        const main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";
        // # Инициализирует объект сообщения

        const mainType = fu.getxpathResultNum(main.resultType);
        sendMsg.main = Object.create(null);
        sendMsg.main.method = main.method;
        sendMsg.main.expression = main.expression;
        sendMsg.main.specifiedResultType = makeTypeStr(mainType);
        sendMsg.main.resultType = "";
        sendMsg.main.resolver = main.resolver || "";
        sendMsg.main.itemDetails = [];
        // # Заполняет объект сообщения данными главного запроса

        contextItem = document;
        currentDocument = document;
        // # Устанавливает контекстный элемент и текущий документ

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
                 logger.error(`Ошибка при получении фрейма: ${e.message}`, e)
                return;
            }
            // # Обрабатывает ошибки при получении фрейма

            inBlankWindow = true;
            currentDocument = contextItem;
            // # Устанавливает флаг пустого окна и текущий документ
        }

        if (inBlankWindow) {
            removeStyleElement(currentDocument);
        }
        // # Удаляет стили из пустого окна

        if (message.context) {
            const cont = message.context;
            const contType = fu.getxpathResultNum(cont.resultType);
            sendMsg.context = Object.create(null);
            sendMsg.context.method = cont.method;
            sendMsg.context.expression = cont.expression;
            sendMsg.context.specifiedResultType = makeTypeStr(contType);
            sendMsg.context.resolver = cont.resolver || "";
            sendMsg.context.itemDetail = null;
             // # Заполняет объект сообщения данными контекстного запроса

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
                logger.error(`Ошибка при получении контекста: ${e.message}`, e)
                return;
            }
            // # Выполняет запрос контекста

            if (contRes.items.length === 0) {
                sendMsg.message = "A context is not found.";
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }
             // # Проверяет, найден ли контекст
            contextItem = contRes.items[0];

            sendMsg.context.resultType = makeTypeStr(contRes.resultType);
            sendMsg.context.itemDetail = fu.getItemDetail(contextItem);
        }
        // # Записывает результат контекстного запроса

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
            logger.error(`Ошибка при выполнении XPath: ${e.message}`, e);
            return;
        }
         // # Выполняет главный запрос

        currentItems = mainRes.items;
        // # Сохраняет результаты главного запроса

        sendMsg.message = "Success.";
        sendMsg.main.resultType = makeTypeStr(mainRes.resultType);
        sendMsg.main.itemDetails = fu.getItemDetails(currentItems);
        browser.runtime.sendMessage(sendMsg);
        prevMsg = sendMsg;
        // # Записывает результаты главного запроса

        setMainAttrs();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
         // # Устанавливает основные атрибуты и обновляет стили, если это пустой фрейм
        return;
    }
    // # Функция обрабатывает выполнение запроса

    /**
     * Фокусирует элемент из результатов запроса.
     *
     * :param message: Объект сообщения с индексом элемента.
     */
    genericListener.listeners.focusItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(currentItems[message.index]);
        }
    };
    // # Функция фокусирует элемент

    /**
     * Фокусирует контекстный элемент.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.focusContextItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(contextItem);
        }
    };
    // # Функция фокусирует контекстный элемент

    /**
     * Фокусирует фрейм.
     *
     * :param message: Объект сообщения с данными фрейма.
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
                const sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when focusing a frame. "
                    + e.message;
                browser.runtime.sendMessage(sendMsg);
                logger.error(`Ошибка при фокусе на фрейме: ${e.message}`, e);
                return;
            }
        }
        // # Обрабатывает фокус на фрейме

        if (win !== win.top) {
            win.parent.postMessage({
                "message": "tryxpath-focus-frame",
                "index": 0,
                "frameIndex": fu.findFrameIndex(win, win.parent)
            }, "*");
        }
         // # Отправляет сообщение родительскому окну для фокуса
    };
    // # Функция обрабатывает фокус фрейма

    /**
     * Запрашивает повторный показ результатов в попапе.
     */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };
    // # Функция запрашивает показ результатов в попапе

    /**
     * Запрашивает показ всех результатов.
     */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }
    // # Функция запрашивает показ всех результатов

    /**
     * Сбрасывает стили и атрибуты элементов.
     */
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };
     // # Функция сбрасывает стили

    /**
     * Устанавливает стили и атрибуты элементов.
     */
    genericListener.listeners.setStyle = function () {
        restoreAttrs();
        updateCss();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        setMainAttrs();
    };
    // # Функция устанавливает стили

    /**
     * Завершает вставку CSS стилей.
     *
     * :param message: Объект сообщения с CSS.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        const css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };
     // # Функция завершает вставку CSS

    /**
     * Завершает удаление CSS стилей.
     *
     * :param message: Объект сообщения с CSS.
     */
    genericListener.listeners.finishRemoveCss = function (message) {
        const css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };
     // # Функция завершает удаление CSS

    browser.storage.onChanged.addListener(changes => {
        if (changes.attributes && ("newValue" in changes.attributes)) {
            attributes = changes.attributes.newValue;
        }
        if (changes.css && ("newValue" in changes.css)) {
            handleCssChange(changes.css.newValue);
        }
    });
     // # Слушатель изменений в хранилище

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
    // # Слушатель сообщений окна

    prevMsg = createResultMessage();
    setFocusFrameListener(window, false);
    // # Создает сообщение результата и устанавливает слушатель фокуса на фрейм

    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });
    // # Отправляет сообщение для запроса информации о контенте
    
    const { j_loads, j_loads_ns } = require('../../../utils/jjson');
    const { logger } = require('../../../logger/logger');

})(window);
```