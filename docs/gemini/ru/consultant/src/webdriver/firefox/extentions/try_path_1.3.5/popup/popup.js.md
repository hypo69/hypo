# Анализ кода модуля popup.js

**Качество кода**
8
 -  Плюсы
    - Код разбит на функции, что улучшает читаемость.
    - Используются константы для магических значений, что улучшает поддержку.
    -  Есть обработка событий.
    - Код следует принципу разделения ответственности.
 -  Минусы
    -  Много повторений кода, особенно в функциях `change...Visible`.
    -  Используются устаревшие конструкции `var`, лучше `const` и `let`.
    -  Обработка ошибок не везде явная.
    -  Функция `collectPopupState` не документирована.
    -  Не хватает комментариев к функциям.

**Рекомендации по улучшению**

1. **Улучшить обработку ошибок**:
    -   Добавить обработку ошибок с использованием `logger.error` для более информативного логирования, а не просто `catch(fu.onError)`.
2. **Рефакторинг функций**:
    -   Функции `changeContextVisible`, `changeResolverVisible`, `changeFrameIdVisible` и `changeFrameDesignationVisible` можно объединить в одну более общую функцию для управления видимостью элементов, чтобы убрать дублирование кода.
3. **Использовать `const` и `let`**:
    -   Заменить `var` на `const` или `let` там, где это уместно.
4. **Добавить документацию**:
    -   Добавить reStructuredText docstrings к функциям и методам, а также к модулю.
5. **Улучшить читаемость**:
    -   Разбить длинные цепочки вызовов на несколько строк для улучшения читаемости.
6. **Убрать дублирование**:
    -   Удалить дублирование кода в обработке событий `addEventListener`.
7. **Использовать async/await**:
     - Там где это возможно, использовать `async/await` для лучшей читаемости асинхронного кода.
8. **Изменить структуру**:
    -  Использовать более явную структуру для определения обработчиков событий, чтобы можно было легко добавлять и изменять их.

**Оптимизиробанный код**
```python
"""
Модуль для управления popup окном расширения Try XPath.
=========================================================

Этот модуль отвечает за взаимодействие с пользовательским интерфейсом
popup окна, обработку событий и отправку сообщений в контентные скрипты.

Он включает в себя функциональность для:
    - Отображения и скрытия различных секций popup окна.
    - Сбора и сохранения состояния popup окна.
    - Отправки команд на выполнение XPath выражений.
    - Отображения результатов выполнения XPath выражений.
    - Управления стилями элементов.
    - Переключения между страницами результатов.

Пример использования
--------------------

.. code-block:: javascript

    // Инициализация popup окна
    (function (window) {
        "use strict";
        // ... код ...
    })(window);
"""
import src.utils.jjson as jjson
from src.logger.logger import logger

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


    def sendToActiveTab(msg, opts):
        """
        Отправляет сообщение активной вкладке.

        :param msg: Сообщение для отправки.
        :type msg: dict
        :param opts: Опции для отправки сообщения.
        :type opts: dict
        :return: Promise
        """
        opts = opts || {};
        return browser.tabs.query({
            "active": true,
            "currentWindow": true
        }).then(tabs => {
            return browser.tabs.sendMessage(tabs[0].id, msg, opts);
        });
    };


    def sendToSpecifiedFrame(msg):
        """
         Отправляет сообщение в указанный фрейм.

        :param msg: Сообщение для отправки.
        :type msg: dict
        :return: Promise
        """
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
            showError("An error occurred. The frameId may be incorrect.",
                      frameId);
        });
    };

    def collectPopupState():
         """
        Собирает состояние popup окна.

        :return: Состояние popup окна.
        :rtype: dict
        """
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

    def changeVisible(element, isVisible):
        """
        Изменяет видимость элемента.

        :param element: DOM-элемент.
        :param isVisible: Флаг видимости.
        :type isVisible: bool
        """
        if (isVisible) {
            element.classList.remove(noneClass);
        } else {
            element.classList.add(noneClass);
        }
    };


    def changeContextVisible():
         """
        Управляет видимостью блока контекста.
        """
        changeVisible(contextBody, contextCheckbox.checked);
    };


    def changeResolverVisible():
         """
        Управляет видимостью блока резолвера.
        """
        changeVisible(resolverBody, resolverCheckbox.checked);
    };

    def changeFrameIdVisible():
         """
        Управляет видимостью блока идентификатора фрейма.
        """
        changeVisible(frameIdBody, frameIdCheckbox.checked);
    };

    def changeFrameDesignationVisible():
         """
        Управляет видимостью блока обозначения фрейма.
        """
         changeVisible(frameDesignationBody, frameDesignationCheckbox.checked);
    };

    def changeHelpVisible():
         """
        Управляет видимостью блока помощи.
        """
        const helps = document.getElementsByClassName(helpClass);
        const isChecked = helpCheckbox.checked;
        for (let i = 0; i < helps.length; i++) {
            changeVisible(helps[i], isChecked);
        }
    };

    def makeExecuteMessage():
        """
        Создает сообщение для выполнения XPath запроса.

        :return: Сообщение для выполнения.
        :rtype: dict
        """
        const msg = Object.create(null);
        msg.event = "execute";

        let resol;
        if (resolverCheckbox.checked) {
            resol = resolverExpression.value;
        } else {
            resol = null;
        }

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

    def getSpecifiedFrameId():
        """
         Возвращает идентификатор фрейма.

        :return: Идентификатор фрейма.
        :rtype: int
        """
        if (!frameIdCheckbox.checked) {
            return 0;
        }
        const id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
        if (id === "manual") {
            return parseInt(frameIdExpression.value, 10);
        }
        return parseInt(id, 10);
    };

    def execContentScript():
        """
        Выполняет контентные скрипты.

        :return: Promise
        """
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

    def sendExecute():
         """
        Отправляет команду на выполнение XPath.
        """
        sendToSpecifiedFrame(makeExecuteMessage());
    };

    def handleExprEnter(event):
         """
        Обрабатывает нажатие Enter в полях ввода.

        :param event: Событие клавиатуры.
        """
        if ((event.key === "Enter") && !event.shiftKey) {
            event.preventDefault();
            sendExecute();
        }
    };

    def showDetailsPage(index):
         """
         Отображает страницу с деталями результатов.

        :param index: Индекс страницы для отображения.
        :type index: int
        """
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
        }).catch(e => logger.error('Ошибка при обновлении таблицы деталей', e));
    };

    def showError(message, frameId):
        """
        Отображает сообщение об ошибке.

        :param message: Сообщение об ошибке.
        :type message: str
        :param frameId: Идентификатор фрейма.
        :type frameId: int
        """
        relatedTabId = invalidTabId;
        relatedFrameId = invalidFrameId;
        executionId = invalidExecutionId;

        resultsMessage.textContent = message;
        resultedDetails = [];
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = frameId;

        fu.updateDetailsTable(contextTbody, [])
            .catch(e => logger.error('Ошибка при обновлении таблицы контекста', e));
        showDetailsPage(0);
    };

    def genericListener(message, sender, sendResponse):
        """
         Общий обработчик сообщений.

        :param message: Сообщение.
        :type message: dict
        :param sender: Отправитель сообщения.
        :type sender: object
        :param sendResponse: Функция для отправки ответа.
        :type sendResponse: function
        """
        const listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    genericListener.listeners.showResultsInPopup = function (message, sender){
        """
        Обрабатывает сообщение с результатами XPath запроса.

        :param message: Сообщение с результатами.
        :type message: dict
        :param sender: Отправитель сообщения.
        :type sender: object
        """
        relatedTabId = sender.tab.id;
        relatedFrameId = sender.frameId;
        executionId = message.executionId;

        resultsMessage.textContent = message.message;
        resultedDetails = message.main.itemDetails;
        resultsCount.textContent = resultedDetails.length;
        resultsFrameId.textContent = sender.frameId;

        if (message.context && message.context.itemDetail) {
            fu.updateDetailsTable(contextTbody, [message.context.itemDetail])
                .catch(e => logger.error('Ошибка при обновлении таблицы контекста', e));
        }

        showDetailsPage(detailsPageIndex);
    };

    genericListener.listeners.restorePopupState = function (message) {
        """
         Обрабатывает сообщение о восстановлении состояния popup окна.

        :param message: Сообщение с сохраненным состоянием.
        :type message: dict
        """
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

    genericListener.listeners.insertStyleToPopup = function(message) {
        """
         Обрабатывает сообщение о вставке стилей в popup окно.

        :param message: Сообщение со стилями.
        :type message: dict
        """
        const style = document.createElement("style");
        style.textContent = message.css;
        document.head.appendChild(style);
    };

    genericListener.listeners.addFrameId = function (message, sender) {
        """
        Обрабатывает сообщение о добавлении ID фрейма.

        :param message: Сообщение.
        :type message: dict
        :param sender: Отправитель сообщения.
        :type sender: object
        """
        const opt = document.createElement("option");
        opt.setAttribute("data-frame-id", sender.frameId);
        opt.textContent = sender.frameId;
        frameIdList.appendChild(opt);
    };

    window.addEventListener("load", () => {
        """
        Инициализация popup окна при загрузке.
        """
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

        const eventHandlers = {
            "help-body": {
                "click": changeHelpVisible,
                "keypress": changeHelpVisible
            },
            "execute": {
                 "click": sendExecute
             },
            "main-expression": {
                "keypress": handleExprEnter
            },
            "context-header": {
                "click": changeContextVisible,
                "keypress": changeContextVisible
            },
           "context-expression": {
               "keypress": handleExprEnter
           },
           "resolver-header": {
               "click": changeResolverVisible,
               "keypress": changeResolverVisible
           },
            "resolver-expression": {
                 "keypress": handleExprEnter
             },
            "frame-designation-header": {
                "click": changeFrameDesignationVisible,
                "keypress": changeFrameDesignationVisible
             },
            "frame-designation-expression": {
                "keypress": handleExprEnter
            },
           "focus-designated-frame": {
                 "click": () => {
                     sendToSpecifiedFrame({
                         "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusFrame",
                         "frameDesignation": frameDesignationExpression.value
                     });
                 }
            },
            "frame-id-header": {
                "click": changeFrameIdVisible,
                "keypress": changeFrameIdVisible
            },
           "frame-id-expression": {
                "keypress": handleExprEnter
            },
            "get-all-frame-id": {
                "click": () => {
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
                     }).catch(e => logger.error('Ошибка при получении списка frame id', e));
                }
             },
            "show-previous-results": {
                "click": () => {
                    sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowResultsInPopup"});
                 }
            },
            "focus-frame": {
                 "click": () => {
                    sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusFrame"});
                 }
            },
            "show-all-results": {
                 "click": () => {
                     sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestShowAllResults" });
                  }
            },
            "open-options": {
                 "click": () => {
                    browser.runtime.openOptionsPage();
                 }
            },
            "set-style": {
                "click": () => {
                  sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setStyle" });
                }
            },
            "reset-style": {
                "click": () => {
                   sendToSpecifiedFrame({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "resetStyle" });
                 }
            },
            "set-all-style": {
                "click": () => {
                     sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setStyle" });
                }
            },
             "reset-all-style": {
                 "click": () => {
                      sendToActiveTab({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "resetStyle" });
                 }
            },
            "previous-details-page": {
                "click": () => {
                    showDetailsPage(detailsPageIndex - 1);
                }
            },
            "move-details-page": {
                "click": () => {
                    const count = parseInt(detailsPageCount.value, 10);
                    showDetailsPage(count - 1);
                }
            },
            "next-details-page": {
                 "click": () => {
                    showDetailsPage(detailsPageIndex + 1);
                 }
            }
        };


        for (const elementId in eventHandlers) {
            const element = document.getElementById(elementId);
            if (element) {
                for (const eventType in eventHandlers[elementId]) {
                    element.addEventListener(eventType, eventHandlers[elementId][eventType]);
                }
            }
        }

        contextTbody.addEventListener("click", event => {
            if (event.target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId,
                }, {
                    "frameId": relatedFrameId
                }).catch(e => logger.error('Ошибка при отправке сообщения о фокусе на контекстный элемент', e));
            }
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
                }).catch(e => logger.error('Ошибка при отправке сообщения о фокусе на элемент', e));
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