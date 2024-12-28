# Анализ кода модуля popup.js

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются функции для обработки событий и управления видимостью элементов.
    - Присутствует обработка сообщений от контент-скрипта.
    - Код старается избегать дублирования, используя функции `sendToActiveTab` и `sendToSpecifiedFrame`.
 -  Минусы
    - Отсутствует явная документация (docstrings) для функций и переменных.
    - Используются устаревшие конструкции `var` вместо `const` и `let` в некоторых местах.
    - Присутствует избыточное использование `Promise.resolve().then(...)` в `sendToSpecifiedFrame`, которое можно упростить.
    - Код содержит magic strings (например, "execute", "focusFrame"), которые лучше вынести в константы.
    - Некоторые функции имеют повторяющуюся логику, например, `changeContextVisible`, `changeResolverVisible`, `changeFrameIdVisible`, `changeFrameDesignationVisible`.
    - Обработка ошибок в основном осуществляется через `catch(e => { showError(...) })`, что можно улучшить, используя `logger.error`.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstrings в формате RST для всех функций, методов и переменных.
2.  **Импорты**: Добавить импорт `logger` для логирования ошибок.
3.  **Переменные**: Заменить `var` на `const` и `let` там, где это уместно.
4.  **Упрощение кода**: Упростить `sendToSpecifiedFrame`, удалив избыточный `Promise.resolve().then(...)`.
5.  **Константы**: Вынести magic strings в константы.
6.  **Рефакторинг**: Вынести повторяющуюся логику в отдельные функции.
7.  **Обработка ошибок**: Использовать `logger.error` для логирования ошибок вместо `showError`.
8.  **Улучшение читаемости**: Разделить большие блоки кода на более мелкие, чтобы улучшить читаемость.

**Оптимизированный код**
```python
"""
Модуль для управления popup окном расширения try_xpath.
=========================================================================================

Этот модуль обрабатывает взаимодействие пользователя с popup окном расширения,
включая отправку запросов на выполнение XPath запросов в контент скриптах,
обработку результатов и управление отображением элементов интерфейса.
"""

from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns


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
    # Объявление констант для типов событий
    const EXECUTE_EVENT = "execute";
    const FOCUS_FRAME_EVENT = "focusFrame";
    const INITIALIZE_BLANK_WINDOWS_EVENT = "initializeBlankWindows";
    const REQUEST_SHOW_RESULTS_IN_POPUP_EVENT = "requestShowResultsInPopup";
    const FOCUS_CONTEXT_ITEM_EVENT = "focusContextItem";
    const FOCUS_ITEM_EVENT = "focusItem";
    const STORE_POPUP_STATE_EVENT = "storePopupState";
    const REQUEST_INSERT_STYLE_TO_POPUP_EVENT = "requestInsertStyleToPopup";
    const REQUEST_RESTORE_POPUP_STATE_EVENT = "requestRestorePopupState";
    const ADD_FRAME_ID_EVENT = "addFrameId";
    const SET_STYLE_EVENT = "setStyle";
    const RESET_STYLE_EVENT = "resetStyle";
    const REQUEST_SHOW_ALL_RESULTS_EVENT = "requestShowAllResults"

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
     * :param msg: Объект сообщения для отправки.
     * :param opts: Объект с дополнительными параметрами.
     * :return: Promise с результатом отправки сообщения.
     */
    function sendToActiveTab(msg, opts) {
        const options = opts || {};
        return browser.tabs.query({
            "active": true,
            "currentWindow": true
        }).then(tabs => {
            return browser.tabs.sendMessage(tabs[0].id, msg, options);
        });
    };


    /**
     * Отправляет сообщение в указанный фрейм.
     *
     * :param msg: Объект сообщения для отправки.
     * :return: Promise с результатом отправки сообщения.
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
           logger.error('Ошибка выполнения скрипта для проверки фрейма', e)
            return
        }


        try {
            await execContentScript();
            await sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": INITIALIZE_BLANK_WINDOWS_EVENT });
            await sendToActiveTab(msg, { "frameId": frameId });
        }
        catch (e) {
           logger.error('An error occurred. The frameId may be incorrect.', e)
            showError("An error occurred. The frameId may be incorrect.", frameId);
        }
    };


    /**
     * Собирает состояние popup окна.
     *
     * :return: Объект с текущим состоянием popup.
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
    };


    /**
     * Изменяет видимость блока контекста.
     */
    function changeContextVisible() {
        changeVisibility(contextCheckbox, contextBody);
    };

    /**
     * Изменяет видимость блока резолвера.
     */
    function changeResolverVisible() {
        changeVisibility(resolverCheckbox, resolverBody);
    };

    /**
     * Изменяет видимость блока frameId.
     */
    function changeFrameIdVisible() {
         changeVisibility(frameIdCheckbox, frameIdBody);
    };

     /**
     * Изменяет видимость блока frameDesignation.
     */
    function changeFrameDesignationVisible() {
        changeVisibility(frameDesignationCheckbox, frameDesignationBody);
    };


    /**
     * Изменяет видимость элемента на основе состояния чекбокса.
     *
     * :param checkbox: HTML элемент чекбокса.
     * :param body: HTML элемент, видимость которого нужно изменить.
     */
    function changeVisibility(checkbox, body) {
         if (checkbox.checked) {
             body.classList.remove(noneClass);
         } else {
             body.classList.add(noneClass);
         }
    }


    /**
     * Изменяет видимость элементов помощи.
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
    };


    /**
     * Создает сообщение для выполнения XPath запроса.
     *
     * :return: Объект сообщения для отправки контент-скрипту.
     */
    function makeExecuteMessage() {
        const msg = Object.create(null);
        msg.event = EXECUTE_EVENT;

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
    };


    /**
     * Получает ID указанного фрейма.
     *
     * :return: ID фрейма или 0, если фрейм не указан.
     */
    function getSpecifiedFrameId() {
        if (!frameIdCheckbox.checked) {
            return 0;
        }
        const id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
        if (id === "manual") {
            return parseInt(frameIdExpression.value, 10);
        }
        return parseInt(id, 10);
    };


    /**
     * Выполняет скрипты контента.
     *
     * :return: Promise, который разрешается после выполнения всех скриптов.
     */
    function execContentScript() {
        return browser.tabs.executeScript({
            "file": "/scripts/try_xpath_functions.js",
            "matchAboutBlank": true,
            "runAt": "document_start",
            "allFrames": true
        }).then(() => {
            return browser.tabs.executeScript({
                "file": "/scripts/try_xpath_content.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "allFrames": true
            });
        });
    };


    /**
     * Отправляет сообщение на выполнение XPath запроса.
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    };


    /**
     * Обрабатывает нажатие клавиши Enter в полях ввода.
     *
     * :param event: Событие клавиатуры.
     */
    function handleExprEnter(event) {
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    };


    /**
     * Отображает страницу с деталями.
     *
     * :param index: Индекс страницы для отображения.
     */
    function showDetailsPage(index) {
        const max = Math.floor(resultedDetails.length / detailsPageSize);

        if (!Number.isInteger(index)) {
            index = 0;
        }
        index = Math.max(0, index);
        index = Math.min(index, max);

        const scrollY = window.scrollY;
        const scrollX = window.scrollX;

        fu.updateDetailsTable(resultsTbody, resultedDetails, {
            "begin": index * detailsPageSize,
            "end": (index * detailsPageSize) + detailsPageSize,
        }).then(() => {
            detailsPageCount.value = index + 1;
            detailsPageIndex = index;
            window.scrollTo(scrollX, scrollY);
        }).catch(fu.onError);
    };


    /**
     * Отображает сообщение об ошибке.
     *
     * :param message: Текст сообщения об ошибке.
     * :param frameId: ID фрейма, в котором произошла ошибка.
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
            .catch(fu.onError);
        showDetailsPage(0);
    };


    /**
     * Общий обработчик сообщений.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя сообщения.
     * :param sendResponse: Функция для отправки ответа.
     * :return: Результат работы обработчика.
     */
    function genericListener(message, sender, sendResponse) {
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик показа результатов в popup окне.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя сообщения.
     */
    genericListener.listeners.showResultsInPopup = function (message, sender) {
        relatedTabId = sender.tab.id;
        relatedFrameId = sender.frameId;
        executionId = message.executionId;

        resultsMessage.textContent = message.message;
        resultedDetails = message.main.itemDetails;
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = sender.frameId;

        if (message.context && message.context.itemDetail) {
            fu.updateDetailsTable(contextTbody, [message.context.itemDetail])
                .catch(fu.onError);
        }

        showDetailsPage(detailsPageIndex);
    };


    /**
     * Обработчик восстановления состояния popup.
     *
     * :param message: Объект сообщения с состоянием.
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
        
        sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": REQUEST_SHOW_RESULTS_IN_POPUP_EVENT });
    };


    /**
     * Обработчик вставки стилей в popup.
     *
     * :param message: Объект сообщения со стилями.
     */
    genericListener.listeners.insertStyleToPopup = function (message) {
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    };


    /**
     * Обработчик добавления ID фрейма.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя сообщения.
     */
    genericListener.listeners.addFrameId = function (message, sender) {
        const opt = document.createElement("option");
        opt.setAttribute("data-frame-id", sender.frameId);
        opt.textContent = sender.frameId;
        frameIdList.appendChild(opt);
    };

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
                   "timeout":0,"timeout_for_event":"presence_of_element_located", "event": FOCUS_FRAME_EVENT,
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
                try {
                    browser.tabs.executeScript({
                        "code": "browser.runtime.sendMessage"
                            + `({"event":"${ADD_FRAME_ID_EVENT}"});`,
                        "matchAboutBlank": true,
                        "runAt": "document_start",
                        "allFrames": true
                    })
                } catch (e){
                    logger.error('Ошибка при выполнении скрипта для получения id фрейма', e)
                }

            });

        document.getElementById("show-previous-results").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": REQUEST_SHOW_RESULTS_IN_POPUP_EVENT});
            });

        document.getElementById("focus-frame").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": FOCUS_FRAME_EVENT });
            });

       document.getElementById("show-all-results").addEventListener(
            "click", () => {
                sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": REQUEST_SHOW_ALL_RESULTS_EVENT });
            });

        document.getElementById("open-options").addEventListener(
            "click", () => {
                browser.runtime.openOptionsPage();
            });

        document.getElementById("set-style").addEventListener("click", () => {
            sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": SET_STYLE_EVENT });
        });

        document.getElementById("reset-style").addEventListener("click", () => {
            sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": RESET_STYLE_EVENT });
        });

        document.getElementById("set-all-style").addEventListener(
            "click", () => {
                sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": SET_STYLE_EVENT });
            });

        document.getElementById("reset-all-style").addEventListener(
            "click", () => {
                sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": RESET_STYLE_EVENT });
            });


        contextTbody.addEventListener("click", event => {
            if (event.target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": FOCUS_CONTEXT_ITEM_EVENT,
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
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": FOCUS_ITEM_EVENT,
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
                 "timeout":0,"timeout_for_event":"presence_of_element_located","event": STORE_POPUP_STATE_EVENT,
                "state": state
            });
        });

        resultsTbody.appendChild(fu.createDetailTableHeader());
        contextTbody.appendChild(fu.createDetailTableHeader());

        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": REQUEST_INSERT_STYLE_TO_POPUP_EVENT});
        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": REQUEST_RESTORE_POPUP_STATE_EVENT });
    });


})(window);