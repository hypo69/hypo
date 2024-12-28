# Анализ кода модуля popup.js

**Качество кода**
8
 -  Плюсы
        - Код разбит на функции, что способствует лучшей читаемости и поддержке.
        - Используются константы для магических значений, что повышает читаемость.
        - Обработчики событий добавляются после загрузки DOM, что является хорошей практикой.
        -  Функции используют `Promise` для асинхронных операций, что улучшает производительность.
        -  Код использует `Object.create(null)` для создания объектов без прототипа, что может быть полезно в некоторых случаях.
 -  Минусы
    -  Отсутствует документация в формате RST.
    -  Используется `try-catch` без логирования ошибок.
    -  Много повторяющегося кода, например, при обработке видимости элементов.
    -  Некоторые функции и переменные не имеют четкого описания, что затрудняет понимание их назначения.
    -  Присутствует дублирование кода при отправке сообщений.

**Рекомендации по улучшению**
1. **Добавить документацию:**
   -  Добавить docstring для модуля, функций и переменных в формате RST.
   -  Описать назначение каждой функции и её параметров.
2. **Улучшить обработку ошибок:**
   -  Использовать `logger.error` для логирования ошибок вместо `try-catch` без обработки.
3. **Рефакторинг:**
   -  Упростить функции `changeContextVisible`, `changeResolverVisible`, `changeFrameIdVisible` и `changeFrameDesignationVisible`, объединив их в одну более общую функцию.
   -  Вынести дублирующийся код отправки сообщений в отдельную функцию.
4.  **Улучшить читаемость:**
   -  Использовать более описательные имена переменных.
   -  Разделить сложные функции на более мелкие.
5.  **Унифицировать отправку сообщений**
     - Создать единую функцию для отправки сообщений, которая будет принимать необходимые параметры.
     - Это позволит избежать дублирования кода и сделает код более поддерживаемым.
6. **Использование `j_loads` или `j_loads_ns`**:
   - В текущем коде нет загрузки JSON, но если она потребуется, следует использовать  `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.

**Оптимизиробанный код**
```python
"""
Модуль для управления попапом расширения Try XPath.
=========================================================================================

Этот модуль отвечает за логику работы попапа расширения, включая взаимодействие с пользовательским интерфейсом,
отправку сообщений в контентный скрипт и обработку ответов.

Пример использования
--------------------

.. code-block:: javascript

    // Этот код исполняется в контексте popup.html
    // и обрабатывает взаимодействие пользователя с интерфейсом.

"""
import logging

from src.logger.logger import logger

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

    var mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
        contextWay, contextExpression, resolverHeader, resolverBody,
        resolverCheckbox, resolverExpression, frameDesignationHeader,
        frameDesignationCheckbox, frameDesignationBody,
        frameDesignationExpression, frameIdHeader, frameIdCheckbox,
        frameIdBody, frameIdList, frameIdExpression, resultsMessage,
        resultsTbody, contextTbody, resultsCount, resultsFrameId,
        detailsPageCount, helpBody, helpCheckbox;

    var relatedTabId = invalidTabId;
    var relatedFrameId = invalidFrameId;
    var executionId = invalidExecutionId;
    var resultedDetails = [];
    const detailsPageSize = 50;
    var detailsPageIndex = 0;

    /**
     * Отправляет сообщение активной вкладке.
     *
     * :param msg: Объект сообщения для отправки.
     * :param opts: Дополнительные опции для отправки сообщения.
     * :return: Promise, который разрешается с результатом отправки сообщения.
     */
    function sendToActiveTab(msg, opts) {
        var opts = opts || {};
        return browser.tabs.query({
            "active": true,
            "currentWindow": true
        }).then(tabs => {
            return browser.tabs.sendMessage(tabs[0].id, msg, opts);
        });
    };

     /**
      * Отправляет сообщение указанному фрейму.
      *
      * :param msg: Объект сообщения для отправки.
      * :return: Promise, который разрешается после отправки сообщения.
      */
    async function sendToSpecifiedFrame(msg) {
        var frameId = getSpecifiedFrameId();
         try {
            # код выполняет проверку, существует ли frame.
             const res = await browser.tabs.executeScript({
                "file": "/scripts/try_xpath_check_frame.js",
                "matchAboutBlank": true,
                "runAt": "document_start",
                "frameId": frameId
            });
            if (!res[0]) {
                # если фрейм не существует, код исполняет контентный скрипт.
                 await execContentScript();
            }
            # код отправляет сообщение с фреймом.
             await sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "initializeBlankWindows" });
             await sendToActiveTab(msg, { "frameId": frameId });
        }
        catch (e) {
            # если происходит ошибка, код показывает сообщение об ошибке.
            showError("An error occurred. The frameId may be incorrect.",
                      frameId);
            logger.error("An error occurred while sending message to specified frame", e)
        }
    };

    /**
     * Собирает состояние попапа.
     *
     * :return: Объект, содержащий состояние попапа.
     */
    function collectPopupState() {
        var state = Object.create(null);
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
     * :param element: DOM-элемент, видимость которого необходимо изменить.
     * :param isVisible: Булево значение, определяющее видимость (true - показать, false - скрыть).
     */
    function changeVisible(element, isVisible) {
      if (isVisible) {
        element.classList.remove(noneClass);
      } else {
        element.classList.add(noneClass);
      }
    }

    /**
     * Изменяет видимость контекстной панели.
     */
    function changeContextVisible () {
        changeVisible(contextBody, contextCheckbox.checked);
    };

    /**
     * Изменяет видимость панели резолвера.
     */
    function changeResolverVisible () {
         changeVisible(resolverBody, resolverCheckbox.checked);
    };

    /**
     * Изменяет видимость панели ID фрейма.
     */
    function changeFrameIdVisible () {
         changeVisible(frameIdBody, frameIdCheckbox.checked);
    };

     /**
      * Изменяет видимость панели назначения фрейма.
      */
    function changeFrameDesignationVisible() {
       changeVisible(frameDesignationBody, frameDesignationCheckbox.checked);
    };

    /**
     * Изменяет видимость элементов помощи.
     */
    function changeHelpVisible() {
        var helps = document.getElementsByClassName(helpClass);
        for (var i = 0; i < helps.length; i++) {
            changeVisible(helps[i], helpCheckbox.checked);
        }
    };

    /**
     * Создает объект сообщения для выполнения.
     *
     * :return: Объект сообщения для выполнения.
     */
    function makeExecuteMessage() {
        var msg = Object.create(null);
        msg.event = "execute";

        var resol;
        if (resolverCheckbox.checked) {
            resol = resolverExpression.value;
        } else {
            resol = null;
        }

        var way = mainWay.selectedOptions[0];
        msg.main = Object.create(null);
        msg.main.expression = mainExpression.value;
        msg.main.method = way.getAttribute("data-method");
        msg.main.resultType = way.getAttribute("data-type");
        msg.main.resolver = resol;

        if (contextCheckbox.checked) {
            let way = contextWay.selectedOptions[0];
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
     * Возвращает ID указанного фрейма.
     *
     * :return: ID фрейма.
     */
    function getSpecifiedFrameId () {
        if (!frameIdCheckbox.checked) {
            return 0;
        }
        var id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
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
     * Отправляет сообщение для выполнения.
     */
    function sendExecute() {
        sendToSpecifiedFrame(makeExecuteMessage());
    };

    /**
     * Обрабатывает нажатие клавиши Enter в поле выражения.
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
      * Отображает страницу с деталями.
      *
      * :param index: Индекс страницы для отображения.
      */
    function showDetailsPage(index) {
        var max = Math.floor(resultedDetails.length / detailsPageSize);

        if (!Number.isInteger(index)) {
            index = 0;
        }
        index = Math.max(0, index);
        index = Math.min(index, max);

        var scrollY = window.scrollY;
        var scrollX = window.scrollX;

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
      * :return: Результат обработки сообщения.
      */
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Обработчик сообщения для отображения результатов в попапе.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя сообщения.
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
     * Обработчик сообщения для восстановления состояния попапа.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.restorePopupState = function (message) {
        var state = message.state;

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
     * Обработчик сообщения для вставки стилей в попап.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.insertStyleToPopup = function(message) {
        var style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    };

    /**
     * Обработчик сообщения для добавления ID фрейма.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя сообщения.
     */
    genericListener.listeners.addFrameId = function (message, sender) {
        var opt = document.createElement("option");
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

                var opt = document.createElement("option");
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
                var count = parseInt(detailsPageCount.value, 10);
                showDetailsPage(count - 1);
            });
        document.getElementById("next-details-page").addEventListener(
            "click", () => {
                showDetailsPage(detailsPageIndex + 1);
            });

        resultsTbody.addEventListener("click", event => {
            var target = event.target;
            if (target.tagName.toLowerCase() === "button") {
                let ind = parseInt(target.getAttribute("data-index"), 10);
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
            var state = collectPopupState();
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