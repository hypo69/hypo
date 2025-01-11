# Анализ кода модуля popup.js

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    - Используются константы для хранения значений, что улучшает читаемость.
    - Присутствует обработка событий для взаимодействия с пользователем.
    - Есть механизм для сохранения и восстановления состояния popup.
    - Код использует `browser.tabs.sendMessage` для взаимодействия с контент-скриптами.
    - Использование `Promise` для асинхронных операций.
    - Наличие комментариев, объясняющих предназначение кода.
- Минусы
    - Не везде используется `logger` для обработки ошибок, в основном используется `fu.onError`.
    - Некоторые блоки try-except можно заменить на `logger.error`.
    - Отсутствует docstring для модуля и функций.
    - Некоторые переменные не имеют явного типа.
    -  Некоторые строки кода превышают рекомендованную длину.
    -  В коде много дублирующегося кода в обработке событий.
    -   Используются устаревшие подходы `var`.
    -  Не используется `j_loads` или `j_loads_ns`.
    -  В коде присутсвует `...`

**Рекомендации по улучшению**

1.  **Добавить docstring**: Добавить docstring для модуля и всех функций, чтобы улучшить читаемость и документирование кода.
2.  **Использовать `logger`**: Заменить `fu.onError` на `logger.error` для обработки ошибок и добавить более информативные сообщения.
3.  **Удалить try-except**: Заменить некоторые блоки `try-except` на обработку ошибок через `logger.error`.
4.  **Типизация**: Добавить явную типизацию для переменных, где это возможно, для улучшения читаемости.
5.  **Удалить `var`**: Заменить `var` на `let` или `const`.
6.  **Разбить длинные строки**: Разбить длинные строки на несколько строк для улучшения читаемости.
7.  **Рефакторинг дублирующегося кода**: Вынести дублирующийся код в отдельные функции.
8. **Удалить `...`**: Заменить  `...`  на конкретную обработку.
9.  **Использовать j_loads**: Заменить `json.load` на `j_loads` или `j_loads_ns`.

**Оптимизированный код**

```python
"""
Модуль для управления popup расширения try_xpath.
==================================================

Этот модуль отвечает за логику работы всплывающего окна (popup) расширения,
включая взаимодействие с пользовательским интерфейсом, обработку сообщений
от контент-скриптов, выполнение Xpath запросов и отображение результатов.

Пример использования
--------------------

Пример инициализации popup и отправки Xpath запроса:

.. code-block:: javascript

    // Инициализация popup происходит автоматически при открытии
    // Получение элементов DOM
    // Отправка запроса на выполнение Xpath
    sendExecute();
"""
from src.logger.logger import logger  # импортируем logger
(function (window) {
    "use strict";

    # alias
    const tx = tryxpath;
    const fu = tryxpath.functions;

    const document = window.document;

    const noneClass = "none";
    const helpClass = "help";
    const invalidTabId = browser.tabs.TAB_ID_NONE;
    const invalidExecutionId = NaN;
    const invalidFrameId = -1;

    let mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
        contextWay, contextExpression, resolverHeader, resolverBody,
        resolverCheckbox, resolverExpression, frameDesignationHeader,
        frameDesignationCheckbox, frameDesignationBody,
        frameDesignationExpression, frameIdHeader, frameIdCheckbox,
        frameIdBody, frameIdList, frameIdExpression, resultsMessage,
        resultsTbody, contextTbody, resultsCount, resultsFrameId,
        detailsPageCount, helpBody, helpCheckbox;

    let relatedTabId = invalidTabId;
    let relatedFrameId = invalidFrameId;
    let executionId = invalidExecutionId;
    let resultedDetails = [];
    const detailsPageSize = 50;
    let detailsPageIndex = 0;

    /**
     * Отправляет сообщение активной вкладке.
     *
     * @param {object} msg - Сообщение для отправки.
     * @param {object} opts - Дополнительные опции.
     * @returns {Promise} - Promise, который разрешается с результатом отправки сообщения.
    */
    function sendToActiveTab(msg, opts = {}) {
        return browser.tabs.query({
            "active": true,
            "currentWindow": true
        }).then(tabs => {
            return browser.tabs.sendMessage(tabs[0].id, msg, opts);
        });
    }

    /**
     * Отправляет сообщение указанному фрейму.
     *
     * @param {object} msg - Сообщение для отправки.
     * @returns {Promise} - Promise, который разрешается после отправки сообщения.
    */
    async function sendToSpecifiedFrame(msg) {
        const frameId = getSpecifiedFrameId();
        try {
            await browser.tabs.executeScript({
                "file": "/scripts/try_xpath_check_frame.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "frameId": frameId
            });
        } catch (e) {
            logger.error("Ошибка при выполнении скрипта проверки фрейма", e);
            showError("An error occurred. The frameId may be incorrect.", frameId);
            return;
        }


        try {
           await sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "initializeBlankWindows" });
           await sendToActiveTab(msg, { "frameId": frameId });

        } catch (e) {
            logger.error("Ошибка при отправке сообщения во фрейм", e);
            showError("An error occurred. The frameId may be incorrect.", frameId);
        }
    };

     /**
      * Собирает текущее состояние popup.
      *
      * @returns {object} - Объект, содержащий состояние popup.
    */
    function collectPopupState() {
        const state = Object.create(null);
        state.helpCheckboxChecked = helpCheckbox.checked;
        state.mainWayIndex = mainWay.selectedIndex;
        state.mainExpressionValue = mainExpression.value;
        state.contextCheckboxChecked = contextCheckbox.checked;
        state.contextWayIndex = contextWay.selectedIndex;
        state.contextExpressionValue = contextExpression.value;
        state.resolverCheckboxChecked = resolverCheckbox.checked;
        state.resolverExpressionValue = resolverExpression.value;
        state.frameDesignationCheckboxChecked
            = frameDesignationCheckbox.checked;
        state.frameDesignationExpressionValue
            = frameDesignationExpression.value;
        state.frameIdCheckboxChecked = frameIdCheckbox.checked;

        state.specifiedFrameId = getSpecifiedFrameId();
        state.detailsPageIndex = detailsPageIndex;
        return state;
    }

    /**
      * Изменяет видимость блока контекста.
      */
    function changeContextVisible () {
        if (contextCheckbox.checked) {
            contextBody.classList.remove(noneClass);
        } else {
            contextBody.classList.add(noneClass);
        }
    }

    /**
      * Изменяет видимость блока резолвера.
      */
    function changeResolverVisible () {
        if (resolverCheckbox.checked) {
            resolverBody.classList.remove(noneClass);
        } else {
            resolverBody.classList.add(noneClass);
        }
    }

    /**
      * Изменяет видимость блока frameId.
      */
    function changeFrameIdVisible () {
        if (frameIdCheckbox.checked) {
            frameIdBody.classList.remove(noneClass);
        } else {
            frameIdBody.classList.add(noneClass);
        }
    }

    /**
     * Изменяет видимость блока frameDesignation.
     */
    function changeFrameDesignationVisible() {
        if (frameDesignationCheckbox.checked) {
            frameDesignationBody.classList.remove(noneClass);
        } else {
            frameDesignationBody.classList.add(noneClass);
        }
    }

    /**
     * Изменяет видимость блока помощи.
     */
    function changeHelpVisible() {
        const helps = document.getElementsByClassName(helpClass);
        for (let i = 0; i < helps.length; i++) {
          if (helpCheckbox.checked) {
                helps[i].classList.remove(noneClass);
            } else {
                helps[i].classList.add(noneClass);
            }
        }
    }

    /**
      * Создает сообщение для выполнения запроса.
      *
      * @returns {object} - Объект сообщения для выполнения запроса.
     */
    function makeExecuteMessage() {
        const msg = Object.create(null);
        msg.event = "execute";

        const resol = resolverCheckbox.checked ? resolverExpression.value : null;

        const way = mainWay.selectedOptions[0];
        msg.main = Object.create(null);
        msg.main.expression = mainExpression.value;
        msg.main.method = way.getAttribute("data-method");
        msg.main.resultType = way.getAttribute("data-type");
        msg.main.resolver = resol;

        if (contextCheckbox.checked) {
            const way = contextWay.selectedOptions[0];
            msg.context = Object.create(null);
            msg.context.expression = contextExpression.value;
            msg.context.method = way.getAttribute("data-method");
            msg.context.resultType = way.getAttribute("data-type");
            msg.context.resolver = resol;
        }

        if (frameDesignationCheckbox.checked) {
            msg.frameDesignation = frameDesignationExpression.value;
        }

        return msg;
    }

    /**
      * Получает идентификатор указанного фрейма.
      *
      * @returns {number} - Идентификатор фрейма.
     */
    function getSpecifiedFrameId () {
        if (!frameIdCheckbox.checked) {
            return 0;
        }
        const id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
        if (id === "manual") {
            return parseInt(frameIdExpression.value, 10);
        }
        return parseInt(id, 10);
    }

    /**
      * Выполняет контент-скрипты.
     */
    async function execContentScript() {
       try {
        await browser.tabs.executeScript({
            "file": "/scripts/try_xpath_functions.js",
            "matchAboutBlank": true,
            "runAt": "document_start",
            "allFrames": true
        });
        await browser.tabs.executeScript({
            "file": "/scripts/try_xpath_content.js",
            "matchAboutBlank": true,
            "runAt": "document_start",
            "allFrames": true
        });
        } catch (e) {
          logger.error("Ошибка при выполнении контент-скриптов", e);
        }
    }

    /**
     * Отправляет сообщение на выполнение запроса.
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    }


     /**
      * Обрабатывает нажатие клавиши Enter в поле ввода выражения.
      *
      * @param {object} event - Объект события.
     */
    function handleExprEnter (event) {
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    }

    /**
      * Отображает страницу с деталями.
      *
      * @param {number} index - Индекс страницы.
     */
    async function showDetailsPage(index) {
        const max = Math.floor(resultedDetails.length / detailsPageSize);

        if (!Number.isInteger(index)) {
            index = 0;
        }
        index = Math.max(0, index);
        index = Math.min(index, max);

        const scrollY = window.scrollY;
        const scrollX = window.scrollX;

        try {
             await fu.updateDetailsTable(resultsTbody, resultedDetails, {
                "begin": index * detailsPageSize,
                "end": (index * detailsPageSize) + detailsPageSize,
             });
             detailsPageCount.value = index + 1;
             detailsPageIndex = index;
             window.scrollTo(scrollX, scrollY);
         } catch (e) {
             logger.error("Ошибка при обновлении таблицы деталей", e);
         }
    }

    /**
      * Отображает сообщение об ошибке.
      *
      * @param {string} message - Сообщение об ошибке.
      * @param {number} frameId - Идентификатор фрейма.
     */
    function showError(message, frameId) {
        relatedTabId = invalidTabId;
        relatedFrameId = invalidFrameId;
        executionId = invalidExecutionId;

        resultsMessage.textContent = message;
        resultedDetails = [];
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = frameId;

        fu.updateDetailsTable(contextTbody, [])
            .catch(e => logger.error("Ошибка при обновлении таблицы контекста", e));
        showDetailsPage(0);
    }

    /**
      * Общий обработчик сообщений.
      *
      * @param {object} message - Сообщение.
      * @param {object} sender - Отправитель сообщения.
      * @param {function} sendResponse - Функция для отправки ответа.
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
     * Обработчик сообщения для отображения результатов в popup.
     *
     * @param {object} message - Сообщение с результатами.
     * @param {object} sender - Отправитель сообщения.
     */
    genericListener.listeners.showResultsInPopup = function (message, sender){
        relatedTabId = sender.tab.id;
        relatedFrameId = sender.frameId;
        executionId = message.executionId;

        resultsMessage.textContent = message.message;
        resultedDetails = message.main.itemDetails;
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = sender.frameId;

        if (message.context && message.context.itemDetail) {
            fu.updateDetailsTable(contextTbody, [message.context.itemDetail])
                 .catch(e => logger.error("Ошибка при обновлении таблицы контекста", e));
        }

        showDetailsPage(detailsPageIndex);
    }

    /**
      * Обработчик сообщения для восстановления состояния popup.
      *
      * @param {object} message - Сообщение с сохраненным состоянием.
     */
    genericListener.listeners.restorePopupState = function (message) {
        const state = message.state;

        if (state !== null) {
            helpCheckbox.checked = state.helpCheckboxChecked;
            mainWay.selectedIndex = state.mainWayIndex;
            mainExpression.value = state.mainExpressionValue;
            contextCheckbox.checked = state.contextCheckboxChecked;
            contextWay.selectedIndex = state.contextWayIndex;
            contextExpression.value = state.contextExpressionValue;
            resolverCheckbox.checked = state.resolverCheckboxChecked;
            resolverExpression.value = state.resolverExpressionValue;
            frameDesignationCheckbox.checked
                = state.frameDesignationCheckboxChecked;
            frameDesignationExpression.value
                = state.frameDesignationExpressionValue;
            frameIdCheckbox.checked = state.frameIdCheckboxChecked;
            frameIdExpression.value = state.specifiedFrameId;

            detailsPageIndex = state.detailsPageIndex;
        }

        changeHelpVisible();
        changeContextVisible();
        changeResolverVisible();
        changeFrameDesignationVisible();
        changeFrameIdVisible();

        sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowResultsInPopup" });
    }

    /**
      * Обработчик сообщения для вставки стилей в popup.
      *
      * @param {object} message - Сообщение со стилями CSS.
    */
    genericListener.listeners.insertStyleToPopup = function(message) {
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    }

    /**
      * Обработчик сообщения для добавления идентификатора фрейма.
      *
      * @param {object} message - Сообщение.
      * @param {object} sender - Отправитель сообщения.
     */
    genericListener.listeners.addFrameId = function (message, sender) {
        const opt = document.createElement("option");
        opt.setAttribute("data-frame-id", sender.frameId);
        opt.textContent = sender.frameId;
        frameIdList.appendChild(opt);
    }

    window.addEventListener("load", () => {
        helpBody = document.getElementById("help-body");
        helpCheckbox = document.getElementById("help-switch");
        mainWay = document.getElementById("main-way");
        mainExpression = document.getElementById("main-expression");
        contextHeader = document.getElementById("context-header");
        contextCheckbox = document.getElementById("context-switch");
        contextBody = document.getElementById("context-body");
        contextWay = document.getElementById("context-way");
        contextExpression = document.getElementById("context-expression");
        resolverHeader = document.getElementById("resolver-header");
        resolverCheckbox = document.getElementById("resolver-switch");
        resolverBody = document.getElementById("resolver-body");
        resolverExpression = document.getElementById("resolver-expression");
        frameDesignationHeader = document.getElementById(
            "frame-designation-header");
        frameDesignationCheckbox = document.getElementById(
            "frame-designation-switch");
        frameDesignationBody = document.getElementById(
            "frame-designation-body");
        frameDesignationExpression = document.getElementById(
            "frame-designation-expression");
        frameIdHeader = document.getElementById("frame-id-header");
        frameIdCheckbox = document.getElementById("frame-id-switch");
        frameIdBody = document.getElementById("frame-id-body");
        frameIdList = document.getElementById("frame-id-list");
        frameIdExpression = document.getElementById("frame-id-expression");
        resultsMessage = document.getElementById("results-message");
        resultsCount = document.getElementById("results-count");
        resultsFrameId = document.getElementById("results-frame-id");
        resultsTbody = document.getElementById("results-details")
            .getElementsByTagName("tbody")[0];
        contextTbody = document.getElementById("context-detail")
            .getElementsByTagName("tbody")[0];
        detailsPageCount = document.getElementById("details-page-count");

        helpBody.addEventListener("click", changeHelpVisible);
        helpBody.addEventListener("keypress", changeHelpVisible);

        document.getElementById("execute").addEventListener("click",
                                                            sendExecute);
        mainExpression.addEventListener("keypress", handleExprEnter);

        contextHeader.addEventListener("click", changeContextVisible);
        contextHeader.addEventListener("keypress", changeContextVisible);
        contextExpression.addEventListener("keypress", handleExprEnter);

        resolverHeader.addEventListener("click", changeResolverVisible);
        resolverHeader.addEventListener("keypress", changeResolverVisible);
        resolverExpression.addEventListener("keypress", handleExprEnter);

        frameDesignationHeader.addEventListener(
            "click", changeFrameDesignationVisible);
        frameDesignationHeader.addEventListener(
            "keypress", changeFrameDesignationVisible);
        frameDesignationExpression.addEventListener(
            "keypress", handleExprEnter);

        document.getElementById("focus-designated-frame").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusFrame",
                    "frameDesignation": frameDesignationExpression.value
                });
            });

        frameIdHeader.addEventListener("click", changeFrameIdVisible);
        frameIdHeader.addEventListener("keypress", changeFrameIdVisible);
        frameIdExpression.addEventListener("keypress", handleExprEnter);
        document.getElementById("get-all-frame-id").addEventListener(
            "click", () => {
                fu.emptyChildNodes(frameIdList);
                const opt = document.createElement("option");
                opt.setAttribute("data-frame-id", "manual");
                opt.textContent = "Manual";
                frameIdList.appendChild(opt);

                browser.tabs.executeScript({
                    "code": "browser.runtime.sendMessage"
                        + "({\\"event\\":\\"addFrameId\\"});",
                    "matchAboutBlank": true,
                    "runAt": "document_start",
                    "allFrames": true
                }).catch(e => logger.error("Ошибка при выполнении скрипта для получения id фреймов", e));
            });

        document.getElementById("show-previous-results").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowResultsInPopup"});
            });

        document.getElementById("focus-frame").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusFrame"});
            });

        document.getElementById("show-all-results").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowAllResults" });
            });

        document.getElementById("open-options").addEventListener(
            "click", () => {
                browser.runtime.openOptionsPage();
            });

        document.getElementById("set-style").addEventListener("click", () => {
            sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setStyle" });
        });

        document.getElementById("reset-style").addEventListener("click",()=> {
            sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "resetStyle" });
        });

        document.getElementById("set-all-style").addEventListener(
            "click", () => {
                sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setStyle" });
            });

        document.getElementById("reset-all-style").addEventListener(
            "click",()=> {
                sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "resetStyle" });
            });


        contextTbody.addEventListener("click", event => {
            if (event.target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId,
                }, {
                    "frameId": relatedFrameId
                }).catch(e => logger.error("Ошибка при отправке сообщения focusContextItem", e));
            }
        });

        document.getElementById("previous-details-page").addEventListener(
            "click", () => {
                showDetailsPage(detailsPageIndex - 1);
            });
        document.getElementById("move-details-page").addEventListener(
            "click", () => {
                const count = parseInt(detailsPageCount.value, 10);
                showDetailsPage(count - 1);
            });
        document.getElementById("next-details-page").addEventListener(
            "click", () => {
                showDetailsPage(detailsPageIndex + 1);
            });

        resultsTbody.addEventListener("click", event => {
            const target = event.target;
            if (target.tagName.toLowerCase() === "button") {
                const ind = parseInt(target.getAttribute("data-index"), 10);
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                    "executionId": executionId,
                    "index": ind
                }, {
                    "frameId": relatedFrameId
                }).catch(e => logger.error("Ошибка при отправке сообщения focusItem", e));
            }
        });

        window.addEventListener("unload", () => {
            const state = collectPopupState();
             browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "storePopupState",
                "state": state
            }).catch(e => logger.error("Ошибка при отправке сообщения storePopupState", e));
        });

        resultsTbody.appendChild(fu.createDetailTableHeader());
        contextTbody.appendChild(fu.createDetailTableHeader());

       browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestInsertStyleToPopup"}).catch(e => logger.error("Ошибка при отправке сообщения requestInsertStyleToPopup", e));
       browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestRestorePopupState" }).catch(e => logger.error("Ошибка при отправке сообщения requestRestorePopupState", e));
    });


})(window);