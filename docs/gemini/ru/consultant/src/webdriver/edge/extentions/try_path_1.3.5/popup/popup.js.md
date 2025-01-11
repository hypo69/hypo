# Анализ кода модуля popup.js

**Качество кода**
8
-  Плюсы
    - Код разбит на функции, что улучшает читаемость и поддерживаемость.
    - Используются константы для строк и числовых значений, что облегчает поддержку и модификацию кода.
    - Присутствует обработка событий для различных элементов интерфейса, что обеспечивает интерактивность.
    - Используется `Promise` для асинхронных операций, что способствует улучшению производительности и обработки ошибок.
    - Есть механизм сохранения и восстановления состояния попапа, что удобно для пользователя.
-  Минусы
    -   Не хватает документации для функций и переменных, что затрудняет понимание кода.
    -   Используется `var` вместо `let` и `const` в некоторых местах, что может привести к проблемам с областью видимости.
    -   Использование `Object.create(null)` может быть не очевидно для всех разработчиков и требует пояснения.
    -   Много повторяющегося кода, особенно при обработке видимости элементов (например, `changeContextVisible`, `changeResolverVisible` и т.д.).
    -  Отсутствует обработка ошибок в некоторых местах, например, при разборе `frameId` из `frameIdExpression.value`.
    -  Избыточное использование `then` и вложенности `then`, можно переписать с async/await.
    -  Не используется импорт `logger`, для логирования ошибок

**Рекомендации по улучшению**

1.  **Добавить документацию:**
    - Документировать каждую функцию, метод и переменную, используя docstring в формате RST.
2.  **Использовать `let` и `const`:**
    - Заменить `var` на `let` или `const` в зависимости от необходимости изменения переменной.
3.  **Упростить создание объектов:**
    - Использовать литералы объектов `{}` вместо `Object.create(null)` там, где это возможно.
4.  **Рефакторинг функций:**
    - Объединить функции для изменения видимости в одну, принимающую элемент и класс в качестве параметров.
5.  **Добавить обработку ошибок:**
    - Добавить обработку ошибок, особенно при преобразовании `frameId` в число.
6. **Использовать async/await:**
   - Переписать цепочки `then` с использованием `async/await`.
7.  **Импортировать и использовать `logger`:**
    - Импортировать `logger` из `src.logger` и использовать для логирования ошибок.
8.  **Улучшить именование переменных и функций:**
    - Использовать более информативные имена для переменных и функций.

**Оптимизированный код**

```python
"""
Модуль для управления popup окном расширения.
=========================================================================================

Этот модуль содержит JavaScript код для управления popup окном расширения,
обрабатывает взаимодействие с контент скриптом и сохраняет состояние.
"""

from src.logger import logger #  импортируем logger

(function (window) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    const noneClass = "none";
    const helpClass = "help";
    const invalidTabId = browser.tabs.TAB_ID_NONE;
    const invalidExecutionId = NaN;
    const invalidFrameId = -1;

    # Объявление переменных для элементов DOM
    var mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
        contextWay, contextExpression, resolverHeader, resolverBody,
        resolverCheckbox, resolverExpression, frameDesignationHeader,
        frameDesignationCheckbox, frameDesignationBody,
        frameDesignationExpression, frameIdHeader, frameIdCheckbox,
        frameIdBody, frameIdList, frameIdExpression, resultsMessage,
        resultsTbody, contextTbody, resultsCount, resultsFrameId,
        detailsPageCount, helpBody, helpCheckbox;

    # Объявление переменных для хранения состояния
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
     * @param {object} [opts] - Дополнительные опции для `browser.tabs.sendMessage`.
     * @returns {Promise<any>} - Promise с результатом отправки сообщения.
     */
    async function sendToActiveTab(msg, opts) {
        opts = opts || {};
        try {
            const tabs = await browser.tabs.query({
                "active": true,
                "currentWindow": true
            });
            return browser.tabs.sendMessage(tabs[0].id, msg, opts);
        } catch (e) {
            logger.error('Ошибка отправки сообщения активной вкладке', e)
        }

    };

   /**
     * Отправляет сообщение указанному фрейму.
     *
     * @param {object} msg - Сообщение для отправки.
     * @returns {Promise<void>} - Promise, который разрешается после отправки сообщения.
     */
    async function sendToSpecifiedFrame(msg) {
        const frameId = getSpecifiedFrameId();
        try {
           let ress =  await browser.tabs.executeScript({
                "file": "/scripts/try_xpath_check_frame.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "frameId": frameId
            });
            if (!ress[0]) {
                await execContentScript();
            }
            await sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "initializeBlankWindows" });
            await sendToActiveTab(msg, { "frameId": frameId });
        } catch (e) {
            logger.error('Произошла ошибка. frameId может быть неверным.', e)
            showError("An error occurred. The frameId may be incorrect.", frameId);
        }
    };

     /**
     * Собирает состояние popup окна.
     *
     * @returns {object} - Объект с текущим состоянием popup.
     */
    function collectPopupState() {
        const state = {};
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
    };

    /**
     * Изменяет видимость элемента.
     *
     * @param {HTMLElement} element - DOM элемент, видимость которого нужно изменить.
     * @param {boolean} isVisible -  флаг, указывающий, нужно ли показать или скрыть элемент.
     */
    function changeVisible(element, isVisible) {
        if (isVisible) {
            element.classList.remove(noneClass);
        } else {
            element.classList.add(noneClass);
        }
    };

     /**
     * Изменяет видимость контекстного блока.
     */
    function changeContextVisible() {
        changeVisible(contextBody, contextCheckbox.checked);
    };

    /**
     * Изменяет видимость блока с настройками резолвера.
     */
    function changeResolverVisible() {
       changeVisible(resolverBody, resolverCheckbox.checked);
    };

    /**
     * Изменяет видимость блока с настройками frame ID.
     */
    function changeFrameIdVisible() {
         changeVisible(frameIdBody, frameIdCheckbox.checked);
    };

    /**
     * Изменяет видимость блока с настройками назначения фрейма.
     */
    function changeFrameDesignationVisible() {
        changeVisible(frameDesignationBody, frameDesignationCheckbox.checked);
    };

    /**
     * Изменяет видимость элементов помощи.
     */
    function changeHelpVisible() {
         const helps = document.getElementsByClassName(helpClass);
        for (let i = 0; i < helps.length; i++) {
            changeVisible(helps[i], helpCheckbox.checked);
        }
    };

    /**
     * Создает сообщение для выполнения скрипта.
     *
     * @returns {object} - Сообщение для отправки.
     */
    function makeExecuteMessage() {
        const msg = {};
        msg.event = "execute";

        const resol = resolverCheckbox.checked ? resolverExpression.value : null;

        const way = mainWay.selectedOptions[0];
        msg.main = {};
        msg.main.expression = mainExpression.value;
        msg.main.method = way.getAttribute("data-method");
        msg.main.resultType = way.getAttribute("data-type");
        msg.main.resolver = resol;

        if (contextCheckbox.checked) {
            const way = contextWay.selectedOptions[0];
             msg.context = {};
             msg.context.expression = contextExpression.value;
             msg.context.method = way.getAttribute("data-method");
             msg.context.resultType = way.getAttribute("data-type");
             msg.context.resolver = resol;
        }

        if (frameDesignationCheckbox.checked) {
            msg.frameDesignation = frameDesignationExpression.value;
        }

        return msg;
    };

    /**
     * Получает ID указанного фрейма.
     *
     * @returns {number} - ID фрейма.
     */
    function getSpecifiedFrameId() {
        if (!frameIdCheckbox.checked) {
            return 0;
        }
        const id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
        if (id === "manual") {
            const manualId = parseInt(frameIdExpression.value, 10);
            if (isNaN(manualId)) {
                logger.error(`Некорректный manual id = ${frameIdExpression.value}`)
                return 0
            }
            return manualId;
        }
         const parsedId = parseInt(id, 10);
         if (isNaN(parsedId)) {
            logger.error(`Некорректный id = ${id}`)
            return 0
        }
        return parsedId
    };

    /**
     * Выполняет контент скрипты.
     *
     * @returns {Promise<void>} - Promise, который разрешается после выполнения скриптов.
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
        }
        catch (e) {
            logger.error('Ошибка выполнения контент скрипта', e)
        }
    };


    /**
     * Отправляет сообщение на выполнение.
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    };

    /**
     * Обрабатывает нажатие клавиши Enter в текстовом поле.
     *
     * @param {KeyboardEvent} event - Событие клавиатуры.
     */
    function handleExprEnter(event) {
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    };

    /**
     * Показывает страницу с деталями результата.
     *
     * @param {number} index - Индекс страницы.
     */
    async function showDetailsPage(index) {
         let max = Math.floor(resultedDetails.length / detailsPageSize);

        if (!Number.isInteger(index)) {
            index = 0;
        }
        index = Math.max(0, index);
        index = Math.min(index, max);

        let scrollY = window.scrollY;
        let scrollX = window.scrollX;

        try {
            await fu.updateDetailsTable(resultsTbody, resultedDetails, {
                "begin": index * detailsPageSize,
                "end": (index * detailsPageSize) + detailsPageSize,
            });
            detailsPageCount.value = index + 1;
            detailsPageIndex = index;
            window.scrollTo(scrollX, scrollY);
        } catch (e) {
           logger.error('Ошибка при обновлении таблицы деталей', e)
        }
    };

    /**
     * Показывает сообщение об ошибке.
     *
     * @param {string} message - Сообщение об ошибке.
     * @param {number} frameId - ID фрейма.
     */
    async function showError(message, frameId) {
        relatedTabId = invalidTabId;
        relatedFrameId = invalidFrameId;
        executionId = invalidExecutionId;

        resultsMessage.textContent = message;
        resultedDetails = [];
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = frameId;
        
        try{
            await fu.updateDetailsTable(contextTbody, [])
        }
        catch(e){
           logger.error('Ошибка при обновлении контекстной таблицы', e)
        }

         showDetailsPage(0);
    };

   /**
     * Общий обработчик сообщений.
     *
     * @param {object} message - Сообщение.
     * @param {object} sender - Отправитель сообщения.
     * @param {function} sendResponse - Функция для отправки ответа.
     * @returns {any} - Результат работы обработчика.
     */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = {};;
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик сообщений для отображения результатов в popup.
     *
     * @param {object} message - Сообщение.
     * @param {object} sender - Отправитель сообщения.
     */
    genericListener.listeners.showResultsInPopup = async function (message, sender) {
        relatedTabId = sender.tab.id;
        relatedFrameId = sender.frameId;
        executionId = message.executionId;

        resultsMessage.textContent = message.message;
        resultedDetails = message.main.itemDetails;
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = sender.frameId;

        if (message.context && message.context.itemDetail) {
            try {
               await fu.updateDetailsTable(contextTbody, [message.context.itemDetail]);
            }
            catch (e) {
                logger.error('Ошибка при обновлении таблицы контекстных деталей', e)
            }

        }

        showDetailsPage(detailsPageIndex);
    };

    /**
     * Обработчик сообщений для восстановления состояния popup.
     *
     * @param {object} message - Сообщение.
     */
    genericListener.listeners.restorePopupState = async function (message) {
        const state = message.state;

        if (state) {
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
        try {
            await sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowResultsInPopup" });
        }
         catch(e){
                logger.error('Ошибка при отправке сообщения в requestShowResultsInPopup', e)
        }
    };

    /**
     * Обработчик сообщений для вставки стилей в popup.
     *
     * @param {object} message - Сообщение.
     */
    genericListener.listeners.insertStyleToPopup = function(message) {
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    };

    /**
     * Обработчик сообщений для добавления ID фрейма.
     *
     * @param {object} message - Сообщение.
     * @param {object} sender - Отправитель сообщения.
     */
    genericListener.listeners.addFrameId = function (message, sender) {
        const opt = document.createElement("option");
        opt.setAttribute("data-frame-id", sender.frameId);
        opt.textContent = sender.frameId;
        frameIdList.appendChild(opt);
    };

     /**
     * Обработчик события загрузки окна.
     */
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
                }).catch(fu.onError);
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
                });
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
                });
            }
        });

        window.addEventListener("unload", () => {
            const state = collectPopupState();
            browser.runtime.sendMessage({
                 "timeout":0,"timeout_for_event":"presence_of_element_located","event": "storePopupState",
                "state": state
            });
        });

        resultsTbody.appendChild(fu.createDetailTableHeader());
        contextTbody.appendChild(fu.createDetailTableHeader());

        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestInsertStyleToPopup"});
        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestRestorePopupState" });
    });


})(window);