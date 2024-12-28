# Анализ кода модуля popup.js

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используются константы для классов и значений, что повышает читаемость.
    - Присутствуют обработчики событий для элементов интерфейса.
    - Код использует асинхронные операции с `Promise`, что соответствует современным стандартам.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST) для функций и переменных.
    - Не используется `logger` для логирования ошибок.
    - Некоторые блоки try-except отсутствуют, что может привести к необработанным ошибкам.
    - Использование `Object.create(null)` для создания объектов может быть не совсем понятным для всех разработчиков.
    - Не все переменные объявлены с использованием `const` или `let`.

**Рекомендации по улучшению**

1. **Документация**: Добавить docstring в формате RST для всех функций и переменных.
2. **Логирование**: Использовать `logger.error` для обработки и логирования ошибок вместо стандартных блоков `try-catch`.
3. **Управление ошибками**: Добавить обработку ошибок в асинхронных операциях и в местах, где это необходимо.
4. **Объявление переменных**: Использовать `const` для констант и `let` для переменных.
5. **Упрощение создания объектов**: Использовать литералы объектов `{}` вместо `Object.create(null)` там, где это уместно.
6. **Импорты**: Добавить необходимые импорты, такие как `logger`.

**Оптимизированный код**

```python
"""
Модуль для управления popup окном расширения try_path.
======================================================

Этот модуль отвечает за взаимодействие с пользователем через popup окно,
отправку запросов в content script и обработку ответов.

Основные функции:
    - Управление видимостью элементов popup окна.
    - Отправка сообщений в content script для выполнения XPath запросов.
    - Отображение результатов выполнения запросов.
    - Сохранение и восстановление состояния popup окна.

Пример использования
--------------------

Запуск popup окна расширения и взаимодействие с его элементами.
"""
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

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

    # Объявление переменных для элементов popup
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
     * :param msg: Сообщение для отправки.
     * :param opts: Опции для отправки сообщения.
     * :return: Promise с результатом отправки.
     */
    function sendToActiveTab(msg, opts) {
        opts = opts || {};
        return browser.tabs.query({
            "active": true,
            "currentWindow": true
        }).then(tabs => {
            return browser.tabs.sendMessage(tabs[0].id, msg, opts);
        });
    }


    /**
     * Отправляет сообщение в указанный фрейм.
     *
     * :param msg: Сообщение для отправки.
     * :return: Promise с результатом отправки.
     */
    async function sendToSpecifiedFrame(msg) {
        const frameId = getSpecifiedFrameId();
        try {
            const ress = await browser.tabs.executeScript({
                "file": "/scripts/try_xpath_check_frame.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "frameId": frameId
            });
            if (!ress[0]) {
                await execContentScript();
            }
            await sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "initializeBlankWindows" });
            return await sendToActiveTab(msg, { "frameId": frameId });
        } catch (e) {
            logger.error("An error occurred. The frameId may be incorrect.", e);
            showError("An error occurred. The frameId may be incorrect.",
                    frameId);
        }
    }

    /**
     * Собирает состояние popup окна.
     *
     * :return: Объект с состоянием popup.
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
    }

    /**
     * Изменяет видимость блока контекста.
     *
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
     *
     */
    function changeResolverVisible () {
        if (resolverCheckbox.checked) {
            resolverBody.classList.remove(noneClass);
        } else {
            resolverBody.classList.add(noneClass);
        }
    }

    /**
     * Изменяет видимость блока выбора фрейма по ID.
     *
     */
    function changeFrameIdVisible () {
        if (frameIdCheckbox.checked) {
            frameIdBody.classList.remove(noneClass);
        } else {
            frameIdBody.classList.add(noneClass);
        }
    }

    /**
     * Изменяет видимость блока выбора фрейма по designation.
     *
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
     *
     */
    function changeHelpVisible() {
        const helps = document.getElementsByClassName(helpClass);
        if (helpCheckbox.checked) {
            for (let i = 0; i < helps.length; i++) {
                helps[i].classList.remove(noneClass);
            }
        } else {
            for (let i = 0; i < helps.length; i++) {
                helps[i].classList.add(noneClass);
            }
        }
    }


    /**
     * Создает сообщение для выполнения запроса.
     *
     * :return: Объект с сообщением для выполнения запроса.
     */
    function makeExecuteMessage() {
        const msg = {};
        msg.event = "execute";

        let resol;
        if (resolverCheckbox.checked) {
            resol = resolverExpression.value;
        } else {
            resol = null;
        }

        const way = mainWay.selectedOptions[0];
        msg.main = {};
        msg.main.expression = mainExpression.value;
        msg.main.method = way.getAttribute("data-method");
        msg.main.resultType = way.getAttribute("data-type");
        msg.main.resolver = resol;

        if (contextCheckbox.checked) {
            let way = contextWay.selectedOptions[0];
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
    }


    /**
     * Возвращает ID указанного фрейма.
     *
     * :return: ID фрейма.
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
     * Выполняет content script.
     *
     * :return: Promise с результатом выполнения.
     */
    async function execContentScript() {
        await browser.tabs.executeScript({
            "file": "/scripts/try_xpath_functions.js",
            "matchAboutBlank": true,
            "runAt": "document_start",
            "allFrames": true
        });
        return await browser.tabs.executeScript({
            "file": "/scripts/try_xpath_content.js",
            "matchAboutBlank": true,
            "runAt": "document_start",
            "allFrames": true
        });
    }


    /**
     * Отправляет сообщение на выполнение.
     *
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    }

    /**
     * Обрабатывает нажатие клавиши Enter в полях ввода.
     *
     * :param event: Событие нажатия клавиши.
     */
    function handleExprEnter (event) {
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    }

    /**
     * Отображает страницу с результатами.
     *
     * :param index: Индекс страницы для отображения.
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
            logger.error("Error updating details table", e);
        }
    }


    /**
     * Отображает сообщение об ошибке.
     *
     * :param message: Сообщение об ошибке.
     * :param frameId: ID фрейма, в котором произошла ошибка.
     */
    async function showError(message, frameId) {
        relatedTabId = invalidTabId;
        relatedFrameId = invalidFrameId;
        executionId = invalidExecutionId;

        resultsMessage.textContent = message;
        resultedDetails = [];
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = frameId;

        try {
            await fu.updateDetailsTable(contextTbody, []);
        } catch (e) {
             logger.error("Error updating context table", e);
        }
        showDetailsPage(0);
    }


    /**
     * Обрабатывает входящие сообщения.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     * :param sendResponse: Функция для отправки ответа.
     * :return: Результат работы обработчика.
     */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    }
    genericListener.listeners = {};
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик сообщения showResultsInPopup.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
     */
    genericListener.listeners.showResultsInPopup = async function (message, sender){
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
            } catch (e) {
                logger.error("Error updating context table", e);
            }
        }

        showDetailsPage(detailsPageIndex);
    }

    /**
     * Обработчик сообщения restorePopupState.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.restorePopupState = function (message) {
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

        sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowResultsInPopup" });
    }

    /**
     * Обработчик сообщения insertStyleToPopup.
     *
     * :param message: Сообщение.
     */
    genericListener.listeners.insertStyleToPopup = function(message) {
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    }

    /**
     * Обработчик сообщения addFrameId.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
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
                }).catch(e => logger.error("Error adding frame id", e));
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
```