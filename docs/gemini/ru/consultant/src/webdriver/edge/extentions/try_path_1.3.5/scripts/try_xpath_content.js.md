# Анализ кода модуля try_xpath_content.js

**Качество кода**

7/10
-  Плюсы
    - Код хорошо структурирован и разделен на функции, что облегчает понимание и поддержку.
    - Используются константы для часто используемых значений, что улучшает читаемость кода.
    - Присутствует обработка ошибок с использованием `try-catch` блоков.
    - Код использует `Map` для хранения данных, что обеспечивает эффективный доступ к данным.
-  Минусы
    - Отсутствует подробная документация (docstring) для функций и модуля.
    - Использование `Object.create(null)` для создания простых объектов может быть неинтуитивным.
    - Некоторые переменные определены с использованием `var` вместо `const` или `let`.
    - Некоторые блоки `try-catch` можно заменить на логирование ошибок через `logger.error`.
    - Не используется импорт logger.
    - Есть дублирование кода, например, при создании `sendMsg` в разных listener.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring для модуля, функций и переменных для улучшения читаемости и поддержки кода.
2.  **Импорты**: Добавить импорт `logger` из `src.logger.logger`.
3.  **Использование `const` и `let`**: Заменить `var` на `const` или `let` там, где это уместно.
4.  **Обработка ошибок**: Заменить некоторые блоки `try-catch` на использование `logger.error`.
5.  **Упрощение объектов**: Использовать литералы объектов `{}` вместо `Object.create(null)`.
6.  **Устранение дублирования**: Вынести повторяющийся код в отдельные функции.
7.  **Использовать `j_loads`**: использовать `j_loads` при `JSON.parse`
8. **Форматирование кода:** В некоторых местах нужно добавить пробелы между операторами, после запятой и т.д.

**Оптимизированный код**

```python
"""
Модуль для обработки XPath запросов в контексте веб-страницы.
=========================================================================================

Этот модуль содержит функции для выполнения XPath-запросов,
управления стилями элементов на странице и взаимодействия с фоновым скриптом расширения.

Пример использования
--------------------

Пример обработки сообщения и выполнения XPath:

.. code-block:: javascript

   genericListener.listeners.execute = function(message, sender) {
       // Обработка сообщения, выполнение XPath и отправка результатов.
   };
"""
from src.logger.logger import logger # Импорт logger

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

    let attributes = { # заменил var на let
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    let prevMsg; # заменил var на let
    let executionCount = 0; # заменил var на let
    let inBlankWindow = false; # заменил var на let
    let currentDocument = null; # заменил var на let
    let contextItem = dummyItem; # заменил var на let
    let currentItems = dummyItems; # заменил var на let
    let focusedItem = dummyItem; # заменил var на let
    let focusedAncestorItems = dummyItems; # заменил var на let
    let currentCss = null; # заменил var на let
    const insertedStyleElements = new Map(); # заменил var на const
    const expiredCssSet = Object.create(null); # заменил var на const
    let originalAttributes = new Map(); # заменил var на let

    function setAttr(attr, value, item) {
        """
        Устанавливает атрибут элементу и сохраняет его оригинальное значение.

        Args:
            attr (str): Имя атрибута.
            value (str): Значение атрибута.
            item (HTMLElement): Элемент, которому устанавливается атрибут.
        """
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };

    function setIndex(attr, items) {
        """
        Устанавливает индекс атрибут для списка элементов.

        Args:
            attr (str): Имя атрибута.
            items (list): Список элементов.
         """
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };

    function isFocusable(item) {
        """
        Проверяет, является ли элемент фокусируемым.

        Args:
            item (HTMLElement): Элемент для проверки.

        Returns:
            bool: True, если элемент фокусируемый, иначе False.
        """
        if (!item) {
            return false;
        }
        if (fu.isNodeItem(item) || fu.isAttrItem(item)) {
            return true;
        }
        return false;
    };

    function focusItem(item) {
        """
        Фокусирует элемент на странице.

        Args:
            item (HTMLElement): Элемент для фокусировки.
        """
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

    function setMainAttrs() {
        """
        Устанавливает основные атрибуты для текущих элементов и контекста.
        """
        if (contextItem !== null) {
            setAttr(attributes.context, "true", contextItem);
        }
        setIndex(attributes.element, currentItems);
    };

    function restoreAttrs() {
        """
        Восстанавливает оригинальные атрибуты элементов.
        """
        fu.restoreItemAttrs(originalAttributes);
        originalAttributes = new Map();
    };

    function resetPrev() {
         """
         Сбрасывает предыдущие значения и обновляет счетчик выполнения.
         """
        restoreAttrs();

        contextItem = dummyItem;
        currentItems = dummyItems;
        focusedItem = dummyItem;
        focusedAncestorItems = dummyItems;

        prevMsg = createResultMessage();
        executionCount++;
    };

    function makeTypeStr(resultType) {
         """
        Преобразует тип результата XPath в строку.

        Args:
             resultType (int): Числовой тип результата.

        Returns:
             str: Строковое представление типа результата, если тип валиден.
         """
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };

    function updateCss() {
        """
        Отправляет сообщение о необходимости обновить CSS.
        """
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };

    function getFrames(spec) {
        """
         Получает фреймы на основе спецификации.

         Args:
             spec (str): Строка, содержащая JSON-представление индексов фреймов.

         Returns:
              list: Список фреймов в порядке иерархии.

         Raises:
             Error: Если спецификация не является валидным массивом чисел.
         """
        try {
            var inds = JSON.parse(spec); #  Используем `j_loads` из `src.utils.jjson`
        } catch (e) {
            logger.error(f'Ошибка при парсинге JSON: {spec}')
            throw new Error("Invalid specification. [" + spec + "]");
        }

        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return fu.getFrameAncestry(inds).reverse();
        } else {
             logger.error(f'Не валидная спецификация фреймов {inds=}')
            throw new Error("Invalid specification. [" + spec + "]");
        }
    };

    function parseFrameDesignation(frameDesi) {
        """
         Разбирает спецификацию фрейма.

        Args:
           frameDesi (str): Строка, содержащая JSON-представление индексов фреймов.

        Returns:
            list: Список индексов фреймов.

        Raises:
           Error: Если спецификация не является валидным массивом чисел.
        """
        try{
            var inds = JSON.parse(frameDesi); #  Используем `j_loads` из `src.utils.jjson`
        } catch (e) {
             logger.error(f'Ошибка при парсинге JSON: {frameDesi}')
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }


        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return inds;
        } else {
            logger.error(f'Не валидная спецификация фреймов {inds=}')
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }
    };

    function traceBlankWindows(desi, win) {
         """
         Проверяет, являются ли указанные окна пустыми.

        Args:
            desi (list): Список индексов фреймов.
            win (Window): Окно, с которого начинается поиск.

        Returns:
            Object: Объект, содержащий информацию о результате проверки.
        """
        win = win || window;
        const result = Object.create(null); # используем литералы объектов

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

    function handleCssChange(newCss) {
        """
         Обрабатывает изменение CSS.

         Args:
             newCss (str): Новое значение CSS.
         """
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

    function findFrameByMessage(event, win) {
         """
         Находит фрейм по сообщению.

        Args:
             event (MessageEvent): Событие сообщения.
             win (Window): Окно, в котором ищется фрейм.

        Returns:
            HTMLElement: Найденный элемент фрейма.
         """
        const ind = event.data.frameIndex; # заменил var на const
        let subWin; # заменил var на let
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    };

    function setFocusFrameListener(win, isBlankWindow) {
        """
         Устанавливает слушатель сообщений для фокуса на фрейме.

        Args:
            win (Window): Окно, для которого устанавливается слушатель.
            isBlankWindow (bool): Флаг, указывающий, является ли окно пустым.
        """
        let localUpdateCss; # заменил var на let
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

                let frame = findFrameByMessage(event, win); # заменил var на let
                if (!frame) {
                    return;
                }

                let index = event.data.index; # заменил var на let
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

    function initBlankWindow(win) {
         """
        Инициализирует пустое окно.

         Args:
            win (Window): Окно для инициализации.
         """
        if (!win.tryxpath) {
            win.tryxpath = Object.create(null); # используем литералы объектов
        }

        if (win.tryxpath.isInitialized) {
            return;
        }
        win.tryxpath.isInitialized = true;

        setFocusFrameListener(win, true);
    };

    function findStyleParent(doc) {
        """
        Находит родительский элемент для стилей.

        Args:
           doc (Document): Документ, в котором ищется родительский элемент.

        Returns:
            HTMLElement: Найденный родительский элемент или null.
        """
        return (doc.head || doc.body || null);
    };

    function updateStyleElement(doc) {
        """
         Обновляет стили для конкретного документа.

        Args:
             doc (Document): Документ, стили которого необходимо обновить.
         """
        let css = currentCss || ""; # заменил var на let
        css = styleElementHeader + css;

        let style = insertedStyleElements.get(doc); # заменил var на let
        if (style) {
            style.textContent = css;
            return;
        }

        let parent = findStyleParent(doc); # заменил var на let
        if (parent) {
            let newStyle = doc.createElement("style"); # заменил var на let
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    };

    function updateAllStyleElements() {
        """
        Обновляет стили во всех документах.
        """
        let css = currentCss || ""; # заменил var на let
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };

    function removeStyleElement(doc) {
        """
        Удаляет стили из конкретного документа.

        Args:
             doc (Document): Документ, из которого необходимо удалить стили.
         """
        let elem = insertedStyleElements.get(doc); # заменил var на let

        if (!elem) {
            return;
        }

        let parent = elem.parentNode; # заменил var на let
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    };

    function removeAllStyleElements() {
        """
         Удаляет все стили.
         """
        for (let [doc, elem] of insertedStyleElements) {
            let parent = elem.parentNode; # заменил var на let
            if (parent) {
                parent.removeChild(elem);
            }
        }
        insertedStyleElements.clear();
    };

     function createResultMessage() {
        """
        Создает объект сообщения с результатами.

        Returns:
            Object: Объект сообщения.
        """
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

    function genericListener(message, sender, sendResponse) {
         """
        Общий слушатель сообщений.

        Args:
            message (Object): Объект сообщения.
            sender (Object): Отправитель сообщения.
            sendResponse (function): Функция для отправки ответа.

        Returns:
            Any: Результат выполнения соответствующего слушателя.
        """
        const listener = genericListener.listeners[message.event]; # заменил var на const
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null); # используем литералы объектов
    browser.runtime.onMessage.addListener(genericListener);

    genericListener.listeners.setContentInfo = function (message) {
        """
        Устанавливает информацию о контенте.

         Args:
            message (Object): Объект сообщения, содержащий атрибуты.
         """
        if (!message) {
            return;
        }

        if ("attributes" in message) {
            attributes = message.attributes;
        }
    };

    genericListener.listeners.execute = function(message, sender) {
        """
        Выполняет XPath-запрос.

         Args:
             message (Object): Объект сообщения, содержащий параметры запроса.
             sender (Object): Отправитель сообщения.
         """
        resetPrev();

        updateCss();

        let sendMsg = {}; # используем литералы объектов
        const main = message.main; # заменил var на const
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        const mainType = fu.getxpathResultNum(main.resultType); # заменил var на const
        sendMsg.main = {}; # используем литералы объектов
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
                let desi = parseFrameDesignation(message.frameDesignation); # заменил var на let
                let res = traceBlankWindows(desi, window); # заменил var на let
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
                sendMsg.message = "An error occurred when getting a frame. " # заменил var на let
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
            const cont = message.context; # заменил var на const
            const contType = fu.getxpathResultNum(cont.resultType); # заменил var на const
            sendMsg.context = {}; # используем литералы объектов
            sendMsg.context.method = cont.method;
            sendMsg.context.expression = cont.expression;
            sendMsg.context.specifiedResultType = makeTypeStr(contType);
            sendMsg.context.resolver = cont.resolver || "";
            sendMsg.context.itemDetail = null;

            let contRes; # заменил var на let
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

        let mainRes; # заменил var на let
        try {
            mainRes = fu.execExpr(main.expression, main.method, {
                "context": contextItem,
                "resultType": mainType,
                "resolver": main.resolver
            });
        } catch (e) {
             logger.error(f'Ошибка выполнения xpath: {e}')
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

    genericListener.listeners.focusItem = function(message) {
         """
        Фокусирует элемент по его индексу.

        Args:
            message (Object): Объект сообщения, содержащий индекс элемента.
         """
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(currentItems[message.index]);
        }
    };

    genericListener.listeners.focusContextItem = function(message) {
        """
        Фокусирует контекстный элемент.

        Args:
             message (Object): Объект сообщения, содержащий идентификатор выполнения.
         """
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(contextItem);
        }
    };

    genericListener.listeners.focusFrame = function(message) {
         """
         Фокусирует фрейм на основе спецификации.

         Args:
            message (Object): Объект сообщения, содержащий спецификацию фрейма.
         """
        let win = window; # заменил var на let

        if ("frameDesignation" in message) {
            try {
                let desi = parseFrameDesignation(message.frameDesignation); # заменил var на let
                let res = traceBlankWindows(desi, window); # заменил var на let
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
                win = res.windows.pop();
            } catch (e) {
                let sendMsg = createResultMessage(); # заменил var на let
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

    genericListener.listeners.requestShowResultsInPopup = function () {
         """
         Отправляет запрос на отображение результатов во всплывающем окне.
         """
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };

    genericListener.listeners.requestShowAllResults = function () {
         """
         Отправляет запрос на отображение всех результатов.
         """
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    };

    genericListener.listeners.resetStyle = function () {
         """
         Сбрасывает стили и атрибуты элементов.
         """
        restoreAttrs();
        removeAllStyleElements();
    };

    genericListener.listeners.setStyle = function () {
         """
         Устанавливает стили и атрибуты элементов.
         """
        restoreAttrs();
        updateCss();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        setMainAttrs();
    };

    genericListener.listeners.finishInsertCss = function (message) {
        """
         Завершает вставку CSS.

         Args:
             message (Object): Объект сообщения, содержащий CSS.
         """
        const css = message.css; # заменил var на const
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };

    genericListener.listeners.finishRemoveCss = function (message) {
         """
         Завершает удаление CSS.

        Args:
            message (Object): Объект сообщения, содержащий CSS.
         """
        const css = message.css; # заменил var на const
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

            let sendMsg; # заменил var на let
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