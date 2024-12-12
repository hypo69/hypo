# Анализ кода модуля `popup.js`

**Качество кода: 7/10**
- **Плюсы:**
    - Код хорошо структурирован и разбит на функции, что делает его более читаемым и поддерживаемым.
    - Используются константы для строк и числовых значений, что улучшает читаемость и облегчает сопровождение кода.
    - Присутствует обработка событий для элементов интерфейса.
    - Код использует промисы для асинхронных операций, что является хорошей практикой.
    - Большая часть кода покрыта комментариями.
- **Минусы:**
    - Отсутствуют docstring для функций, что усложняет понимание их назначения и параметров.
    - Не используются `j_loads` или `j_loads_ns`.
    - Избыточное использование `try-catch` блоков, которые можно заменить на `logger.error`.
    - Некоторые переменные объявлены с использованием `var` вместо `const` или `let`.
    - Код содержит дублирование логики обработки событий и UI (например, `changeContextVisible`, `changeResolverVisible` и т.д.).
    - Обработка ошибок не всегда достаточно информативна, не хватает логирования.

**Рекомендации по улучшению:**

1.  Добавить docstring к функциям, методам и классам для улучшения понимания их работы.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Убрать избыточные `try-except` блоки и заменить их на обработку ошибок с помощью `logger.error`.
4.  Использовать `const` или `let` вместо `var` там, где это уместно.
5.  Оптимизировать код за счет устранения дублирования логики.
6.  Добавить более подробные сообщения об ошибках в лог.
7. Использовать `j_loads` или `j_loads_ns` для работы с json.
8. Все комментарии переписать в формате reStructuredText (RST).

**Оптимизированный код:**

```python
"""
Модуль для управления popup окном расширения try_xpath.
=========================================================================================

Этот модуль отвечает за обработку событий в popup окне расширения, 
включая взаимодействие с пользовательским интерфейсом, отправку сообщений в контентные скрипты, 
а также сохранение и восстановление состояния popup окна.

"""
import json # импортируем модуль json
from src.logger.logger import logger # импортируем logger

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

    # Объявляем переменные для работы с элементами интерфейса
    var mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
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
     * :return: Promise, который разрешается после отправки сообщения.
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
     * Отправляет сообщение указанному фрейму.
     *
     * :param msg: Сообщение для отправки.
     * :return: Promise, который разрешается после отправки сообщения.
     */
    function sendToSpecifiedFrame(msg) {
        const frameId = getSpecifiedFrameId();
        return Promise.resolve().then(() => {
            return browser.tabs.executeScript({
                "file": "/scripts/try_xpath_check_frame.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "frameId": frameId
            });
        }).then(ress => {
            if (ress[0]) {
                return;
            }
            return execContentScript();
        }).then(() => {
            return sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "initializeBlankWindows" });
        }).then(() => {
            return sendToActiveTab(msg, { "frameId": frameId });
        }).catch(e => {
            logger.error(`An error occurred. The frameId may be incorrect. frameId: ${frameId}`, e) # Логируем ошибку
            showError("An error occurred. The frameId may be incorrect.",
                      frameId);
        });
    };

    /**
     * Собирает текущее состояние popup окна.
     *
     * :return: Объект, содержащий текущее состояние popup окна.
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
     *
     */
    function changeContextVisible () {
        if (contextCheckbox.checked) {
            contextBody.classList.remove(noneClass);
        } else {
            contextBody.classList.add(noneClass);
        }
    };

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
    };

    /**
     * Изменяет видимость блока выбора frameId.
     *
     */
    function changeFrameIdVisible () {
        if (frameIdCheckbox.checked) {
            frameIdBody.classList.remove(noneClass);
        } else {
            frameIdBody.classList.add(noneClass);
        }
    };

    /**
     * Изменяет видимость блока обозначения фрейма.
     *
     */
    function changeFrameDesignationVisible() {
        if (frameDesignationCheckbox.checked) {
            frameDesignationBody.classList.remove(noneClass);
        } else {
            frameDesignationBody.classList.add(noneClass);
        }
    };

    /**
     * Изменяет видимость блока помощи.
     *
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
     * Формирует сообщение для выполнения запроса.
     *
     * :return: Объект сообщения для отправки.
     */
    function makeExecuteMessage() {
        const msg = Object.create(null);
        msg.event = "execute";

        let resol = resolverCheckbox.checked ? resolverExpression.value : null;


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
     * Возвращает идентификатор указанного фрейма.
     *
     * :return: Идентификатор фрейма или 0, если не выбран.
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
    };

    /**
     * Выполняет контентные скрипты.
     *
     * :return: Promise, который разрешается после выполнения скриптов.
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
     * Отправляет запрос на выполнение.
     *
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    };

    /**
     * Обрабатывает нажатие Enter в полях ввода.
     *
     * :param event: Событие клавиатуры.
     */
    function handleExprEnter (event) {
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    };

    /**
     * Отображает страницу деталей результатов.
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
     * :param message: Сообщение об ошибке.
     * :param frameId: Идентификатор фрейма, где произошла ошибка.
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
     * Универсальный обработчик сообщений.
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
    };
    genericListener.listeners = Object.create(null);;
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик сообщения для отображения результатов.
     *
     * :param message: Сообщение с результатами.
     * :param sender: Отправитель сообщения.
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
                .catch(fu.onError);
        }

        showDetailsPage(detailsPageIndex);
    };

    /**
     * Обработчик сообщения для восстановления состояния popup окна.
     *
     * :param message: Сообщение с состоянием.
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
    };

    /**
     * Обработчик сообщения для вставки стилей в popup окно.
     *
     * :param message: Сообщение со стилями.
     */
    genericListener.listeners.insertStyleToPopup = function(message) {
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    };

    /**
     * Обработчик сообщения для добавления идентификатора фрейма.
     *
     * :param message: Сообщение.
     * :param sender: Отправитель сообщения.
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
```