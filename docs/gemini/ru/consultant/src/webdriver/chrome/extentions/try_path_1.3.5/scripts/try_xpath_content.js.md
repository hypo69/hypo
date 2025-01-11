# Анализ кода модуля try_xpath_content.js

**Качество кода:**

-   **Соответствие требованиям по оформлению кода**: 7/10
    -   **Плюсы:**
        - Код достаточно хорошо структурирован и разбит на функции.
        - Используются константы для магических значений.
        - Присутствует обработка сообщений от расширения.
    -   **Минусы:**
        -  Отсутствует описание модуля в начале файла.
        -  Отсутствует документация для функций.
        -  Используются стандартные конструкции `try-catch`, но не везде где это необходимо.
        -  В некоторых местах используется `Object.create(null)` вместо обычных литералов объектов `{}`.
        -  Не везде применяется `logger.error` для обработки ошибок.
        -  Используется `var` вместо `let` и `const`.
        -  Некоторые переменные объявлены в начале файла, но используются только в отдельных функциях.
        -  Некоторые функции слишком длинные и выполняют несколько задач.
        -  Смешивание `var` и `const` может привести к путанице.
        -  Много мест где есть `return;` без пояснений.

**Рекомендации по улучшению:**

1.  **Добавить описание модуля:**
    -   В начало файла нужно добавить описание модуля, его назначения и основные принципы работы.

2.  **Документировать функции:**
    -   Добавить docstring для каждой функции, описывая ее назначение, параметры, возвращаемое значение и возможные ошибки.

3.  **Использовать `logger.error` для обработки ошибок:**
    -   Заменить стандартные `try-catch` на обработку ошибок с помощью `logger.error`.
    -   Для каждого `try-catch` необходимо оставлять комментарий, что именно этот блок делает.

4.  **Перейти на `let` и `const`:**
    -   Использовать `let` вместо `var` для переменных, которые могут изменяться, и `const` для констант.

5.  **Разделить длинные функции на более мелкие:**
    -   Разбить большие функции на более мелкие, чтобы каждая из них выполняла одну конкретную задачу.
    -   Это улучшит читаемость и упростит тестирование кода.

6.  **Упростить создание объектов:**
    -   Использовать `{}` вместо `Object.create(null)` для создания простых объектов, где прототип не нужен.

7.  **Использовать более информативные имена переменных:**
    -   Имена переменных должны быть более описательными и отражать их назначение.

8.  **Удалить неиспользуемые переменные:**
    -   Удалить или переместить переменные, которые объявлены в начале файла, но используются только в отдельных функциях, ближе к месту использования.

9.  **Унифицировать стиль кода:**
    -   Привести весь код к единому стилю, чтобы он был более читаемым и понятным.

10. **Удалить избыточные комментарии и `return;`:**
     -  Удалить комментарии, которые не несут полезной информации.
     -  Добавить более понятные комментарии к операторам `return;`.

**Оптимизированный код:**

```python
"""
Модуль для обработки XPath запросов и отображения результатов в браузере.
=========================================================================================

Этот модуль содержит функции для обработки XPath запросов,
выполнения их в контексте текущей веб-страницы или iframe,
и отображения результатов в виде стилизованных элементов.
Модуль также обрабатывает сообщения от расширения браузера,
устанавливает фокус на найденные элементы и управляет стилями.

Основные функции:
  - execute: Выполняет XPath запрос и отправляет результаты в расширение.
  - focusItem: Устанавливает фокус на найденный элемент.
  - focusContextItem: Устанавливает фокус на контекстный элемент.
  - focusFrame: Устанавливает фокус на указанный iframe.
  - setStyle: Применяет стили к элементам на странице.
  - resetStyle: Сбрасывает стили.

Пример использования:
--------------------

.. code-block:: javascript

    // Отправка сообщения для выполнения XPath запроса
    browser.runtime.sendMessage({
        "event": "execute",
        "main": {
            "method": "evaluate",
            "expression": "//div",
            "resultType": "7"
        }
    });
"""
from src.logger.logger import logger

(function (window, undefined) {
    "use strict";

    # alias
    const tx = tryxpath;
    const fu = tryxpath.functions;

    # предотвращение многократного выполнения
    if (tx.isContentLoaded) {
        return;
    }
    tx.isContentLoaded = true;

    const dummyItem = "";
    const dummyItems = [];
    const invalidExecutionId = NaN;
    const styleElementHeader = "/* This style element was inserted by browser add-on, Try xpath."
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
     * Сохраняет и устанавливает атрибут элемента.
     *
     * @param {string} attr - Имя атрибута.
     * @param {string} value - Значение атрибута.
     * @param {Element} item - Целевой элемент.
     */
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    }

    /**
     * Сохраняет и устанавливает индексы для набора элементов.
     *
     * @param {string} attr - Имя атрибута.
     * @param {Array<Element>} items - Массив элементов.
     */
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    }

    /**
     * Проверяет, является ли элемент фокусируемым.
     *
     * @param {Element} item - Проверяемый элемент.
     * @returns {boolean} - Возвращает true, если элемент может быть в фокусе, иначе false.
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
     * Устанавливает фокус на элемент, сохраняя предыдущий фокус.
     *
     * @param {Element} item - Целевой элемент для установки фокуса.
     */
    function focusItem(item) {
        fu.removeAttrFromItem(attributes.focused, focusedItem);
        fu.removeAttrFromItems(attributes.focusedAncestor, focusedAncestorItems);

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
     * Устанавливает основные атрибуты для контекстного и текущих элементов.
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
     * Сбрасывает переменные и счетчики для нового запроса.
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
     * Создает строку из типа результата XPath.
     *
     * @param {number} resultType - Тип результата XPath.
     * @returns {string} - Строковое представление типа результата.
     */
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    }

    /**
     * Обновляет стили CSS, отправляя сообщение в расширение.
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
     * Получает массив фреймов по их спецификации.
     *
     * @param {string} spec - Строка спецификации фреймов.
     * @returns {Array<Window>} - Массив окон фреймов.
     * @throws {Error} Если спецификация неверна.
     */
    function getFrames(spec) {
        try {
            const inds = JSON.parse(spec);

            if (fu.isNumberArray(inds) && (inds.length > 0)) {
                return fu.getFrameAncestry(inds).reverse();
            } else {
                throw new Error(`Invalid specification. [${spec}]`);
            }
        } catch (e) {
            logger.error('Ошибка при парсинге спецификации фреймов', e)
            throw e
        }
    }

     /**
     * Парсит строку спецификации фрейма в массив индексов.
     *
     * @param {string} frameDesi - Строка спецификации фрейма.
     * @returns {Array<number>} - Массив индексов фреймов.
     * @throws {Error} Если спецификация неверна.
     */
    function parseFrameDesignation(frameDesi) {
      try{
          const inds = JSON.parse(frameDesi);

          if (fu.isNumberArray(inds) && (inds.length > 0)) {
              return inds;
          } else {
            throw new Error(`Invalid specification. [${frameDesi}]`);
          }
        } catch (e) {
          logger.error('Ошибка при парсинге дескриптора фрейма', e)
          throw e
        }
    }

    /**
     * Проверяет наличие фреймов в "пустых" окнах.
     *
     * @param {Array<number>} desi - Массив индексов фреймов.
     * @param {Window} win - Начальное окно для поиска.
     * @returns {object} - Объект с результатами поиска.
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
    }

    /**
     * Обрабатывает изменение CSS, обновляя текущий стиль и список устаревших стилей.
     *
     * @param {string} newCss - Новый CSS.
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
         # Если newCss и currentCss являются одинаковой строкой, ничего не делаем.
    }

     /**
     * Находит фрейм по сообщению.
     *
     * @param {object} event - Объект события сообщения.
     * @param {Window} win - Окно для поиска фрейма.
     * @returns {Element|null} - Найденный элемент фрейма или null.
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
    }

    /**
     * Устанавливает слушатель сообщений для фокуса фрейма.
     *
     * @param {Window} win - Целевое окно.
     * @param {boolean} isBlankWindow - Флаг, указывающий, является ли окно "пустым".
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

                const frame = findFrameByMessage(event, win);
                if (!frame) {
                    return;
                }

                const index = event.data.index;
                localUpdateCss();
                setAttr(attributes.frame, index, frame);
                setIndex(attributes.frameAncestor, fu.getAncestorElements(frame));
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
     * Инициализирует "пустое" окно, устанавливая необходимые свойства и слушатели.
     *
     * @param {Window} win - Целевое окно.
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
    }

    /**
     * Находит родительский элемент для вставки стилей.
     *
     * @param {Document} doc - Документ, в котором нужно найти родителя.
     * @returns {HTMLElement|null} - Родительский элемент или null.
     */
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    }

    /**
     * Обновляет стили CSS в элементе <style> в указанном документе.
     *
     * @param {Document} doc - Документ, в котором нужно обновить стили.
     */
    function updateStyleElement(doc) {
        let css = currentCss || "";
        css = styleElementHeader + css;

        let style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }

        const parent = findStyleParent(doc);
        if (parent) {
            const newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    }

    /**
     * Обновляет все элементы <style> на странице.
     */
    function updateAllStyleElements() {
        let css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    }

    /**
     * Удаляет элемент <style> из документа.
     *
     * @param {Document} doc - Документ, из которого нужно удалить элемент.
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
    }

    /**
     * Удаляет все элементы <style> на странице.
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
     * Создает шаблон сообщения результата.
     *
     * @returns {object} - Шаблон сообщения результата.
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
     * Общий обработчик сообщений от расширения.
     *
     * @param {object} message - Объект сообщения.
     * @param {object} sender - Объект отправителя.
     * @param {function} sendResponse - Функция для отправки ответа.
     * @returns {*} - Результат работы слушателя.
     */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    }
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Слушатель для установки информации о содержимом.
     *
     * @param {object} message - Объект сообщения.
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
     * Слушатель для выполнения XPath запроса.
     *
     * @param {object} message - Объект сообщения с данными для выполнения запроса.
     * @param {object} sender - Объект отправителя сообщения.
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
                const desi = parseFrameDesignation(message.frameDesignation);
                const res = traceBlankWindows(desi, window);
                if (!res.success) {
                   if (res.failedWindow === null) {
                      throw new Error("The specified frame does not exist.");
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
                sendMsg.message = `An error occurred when getting a frame. ${e.message}`;
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
              sendMsg.message = `An error occurred when getting a context. ${e.message}`;
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
          sendMsg.message = `An error occurred when getting nodes. ${e.message}`;
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
    }

    /**
     * Слушатель для установки фокуса на элемент.
     *
     * @param {object} message - Объект сообщения с данными элемента.
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
     * Слушатель для установки фокуса на контекстный элемент.
     *
     * @param {object} message - Объект сообщения с данными контекстного элемента.
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
     * Слушатель для установки фокуса на фрейм.
     *
     * @param {object} message - Объект сообщения с данными фрейма.
     */
    genericListener.listeners.focusFrame = function(message) {
      let win = window;

        if ("frameDesignation" in message) {
            try {
                const desi = parseFrameDesignation(message.frameDesignation);
                const res = traceBlankWindows(desi, window);
                if (!res.success) {
                  let msg
                   if (res.failedWindow === null) {
                        throw new Error("The specified frame does not exist.");
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
                sendMsg.message = `An error occurred when focusing a frame. ${e.message}`;
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
     * Слушатель для запроса показа результатов в popup.
     */
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };

    /**
     * Слушатель для запроса показа всех результатов.
     */
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }

    /**
     * Слушатель для сброса стилей.
     */
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };

    /**
     * Слушатель для установки стилей.
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
     * Слушатель для завершения вставки CSS.
     *
     * @param {object} message - Объект сообщения с CSS.
     */
    genericListener.listeners.finishInsertCss = function (message) {
        const css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };

    /**
     * Слушатель для завершения удаления CSS.
     *
     * @param {object} message - Объект сообщения с CSS.
     */
    genericListener.listeners.finishRemoveCss = function (message) {
        const css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };

    /**
     * Слушатель для изменений в хранилище браузера.
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
     * Слушатель для сообщений от фреймов.
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