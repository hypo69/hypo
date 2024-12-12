# Анализ кода модуля `try_xpath_background.js`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован, используются функции для разделения логики.
    -   Применение `browser.runtime.onMessage.addListener` для обработки сообщений.
    -   Использование `Promise` для асинхронных операций.
    -   Код использует `browser.storage.sync.get` для синхронизации настроек.
    -   Обработка ошибок с использованием `catch(fu.onError)`.
-   Минусы
    -   Отсутствуют docstring для функций и переменных.
    -   Используются магические строки в `browser.runtime.sendMessage` и `browser.tabs.sendMessage`.
    -   Не всегда понятно, какие данные передаются в сообщениях.
    -   Использование `XMLHttpRequest` для загрузки CSS, что может быть заменено на `fetch`.
    -   Не хватает комментариев, объясняющих логику работы отдельных блоков.
    -   Используется `Object.create(null)` без четкого объяснения.

**Рекомендации по улучшению**

1.  **Добавить Docstrings**: Добавить docstring к каждой функции, включая описание параметров и возвращаемых значений.
2.  **Использовать константы для сообщений**: Заменить магические строки на константы для `event` в `browser.runtime.sendMessage` и `browser.tabs.sendMessage`, чтобы избежать опечаток и сделать код более читаемым.
3.  **Уточнить данные сообщений**: В комментариях указать, какие данные передаются в сообщениях.
4.  **Заменить `XMLHttpRequest` на `fetch`**: Использовать `fetch` для загрузки CSS, так как это более современный API.
5.  **Добавить комментарии к логике блоков**: Комментировать каждый логический блок кода, чтобы было понятно, что он делает.
6.  **Уточнить назначение `Object.create(null)`**: Добавить комментарий, объясняющий, почему используется `Object.create(null)`.
7.  **Использовать `logger.error`**: Заменить `catch(fu.onError)` на `logger.error` для логирования ошибок.
8.  **Унифицировать передачу параметров** : Привести к одному виду передачу параметров в `browser.runtime.sendMessage` и `browser.tabs.sendMessage`. Использовать один ключ `payload` и передавать все параметры в нем.

**Оптимизированный код**

```python
"""
Модуль для управления расширением Try XPath в фоновом режиме.
==============================================================

Этот модуль управляет состоянием всплывающего окна, стилями CSS,
атрибутами элементов и передачей данных между фоновым скриптом и
вкладками браузера. Он использует API браузера для
взаимодействия с вкладками, хранилищем и обменом сообщениями.

"""
import src.utils.jjson as jjson
from src.logger.logger import logger

#   import  browser from 'webextension-polyfill' # TODO  добавить в сборку
# from browser import runtime

(function (window, undefined) {
    "use strict";

    #  alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var popupState = null;
    var popupCss = "body{width:367px;height:auto;}";
    var results = {};
    var css = "";
    var attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    const MSG_EVENT = {
        RESTORE_POPUP_STATE: "restorePopupState",
        INSERT_STYLE_TO_POPUP: "insertStyleToPopup",
        FINISH_REMOVE_CSS: "finishRemoveCss",
        FINISH_INSERT_CSS: "finishInsertCss",
        SET_CONTENT_INFO: "setContentInfo"
    }
    /**
     * Загружает CSS по умолчанию из файла.
     *
     * :return: Promise, разрешающийся с текстом CSS, или отклоняющийся в случае ошибки.
     * :rtype: Promise<string>
     */
    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.text();
                })
                .then(text => resolve(text))
                .catch(error => {
                     logger.error("Ошибка при загрузке CSS по умолчанию", error)
                    reject(error)

                });
        });
    }

    /**
     *  Общий обработчик сообщений.
     *
     *  :param message: Объект сообщения.
     *  :type message: object
     *  :param sender: Объект отправителя сообщения.
     *  :type sender: object
     *  :param sendResponse: Функция обратного вызова для отправки ответа.
     *  :type sendResponse: function
     *  :return: Результат выполнения соответствующего обработчика.
     */
    function genericListener(message, sender, sendResponse) {
         # Вызов соответствующего обработчика, если он существует
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    }
    #  Объект для хранения обработчиков сообщений
    genericListener.listeners = Object.create(null); # Используется для создания объекта без прототипа Object для избежания возможных конфликтов
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Сохраняет состояние всплывающего окна.
     *
     * :param message: Объект сообщения, содержащий состояние.
     * :type message: object
     */
    genericListener.listeners.storePopupState = function (message) {
        popupState = message.state;
    }

    /**
     * Запрашивает восстановление состояния всплывающего окна.
     *
     * :param message: Объект сообщения.
     * :type message: object
     */
    genericListener.listeners.requestRestorePopupState = function (message) {
        browser.runtime.sendMessage({
            "timeout":0,
            "timeout_for_event":"presence_of_element_located",
            "event": MSG_EVENT.RESTORE_POPUP_STATE,
            "payload": { "state": popupState }
        });
    };

    /**
     * Запрашивает вставку стиля во всплывающее окно.
     *
     * :param message: Объект сообщения.
     * :type message: object
     */
    genericListener.listeners.requestInsertStyleToPopup = function () {
        browser.runtime.sendMessage({
             "timeout":0,
            "timeout_for_event":"presence_of_element_located",
            "event": MSG_EVENT.INSERT_STYLE_TO_POPUP,
            "payload": { "css": popupCss }
        });
    };

    /**
     *  Отображает все результаты поиска.
     *
     * :param message: Объект сообщения с результатами.
     * :type message: object
     * :param sender: Объект отправителя сообщения.
     * :type sender: object
     */
    genericListener.listeners.showAllResults = function(message, sender) {
         # Удаление поля 'event' из сообщения
        delete message.event;
        results = message;
        results.tabId = sender.tab.id;
        results.frameId = sender.frameId;
        browser.tabs.create({ "url": "/pages/show_all_results.html" });
    };

    /**
     *  Загружает результаты.
     *
     * :param message: Объект сообщения.
     * :type message: object
     * :param sender: Объект отправителя сообщения.
     * :type sender: object
     * :param sendResponse: Функция обратного вызова для отправки ответа.
     * :type sendResponse: function
     * :return: True для асинхронного ответа.
     * :rtype: bool
     */
    genericListener.listeners.loadResults = function (message, sender,
                                                      sendResponse) {
        sendResponse(results);
        return true;
    };

    /**
     * Обновляет стили CSS на вкладке.
     *
     * :param message: Объект сообщения, содержащий удаляемые и добавляемые стили.
     * :type message: object
     * :param sender: Объект отправителя сообщения.
     * :type sender: object
     */
    genericListener.listeners.updateCss = function (message, sender) {
        var id = sender.tab.id;
        var frameId = sender.frameId;

        # Итерация по удаляемым стилям
        for (let removeCss in message.expiredCssSet) {
            browser.tabs.removeCSS(id, {
                "code": removeCss,
                "matchAboutBlank": true,
                "frameId": frameId
            }).then(() => {
                return browser.tabs.sendMessage(id, {
                    "timeout":0,
                    "timeout_for_event":"presence_of_element_located",
                    "event": MSG_EVENT.FINISH_REMOVE_CSS,
                   "payload": { "css": removeCss }
                }, {
                    "frameId": frameId
                });
            }).catch((error) => logger.error("Ошибка при удалении CSS", error));
        }

        browser.tabs.insertCSS(id, {
            "code":css,
            "cssOrigin": "author",
            "matchAboutBlank": true,
            "frameId": frameId
        }).then(() => {
            return browser.tabs.sendMessage(id, {
                 "timeout":0,
                "timeout_for_event":"presence_of_element_located",
                "event": MSG_EVENT.FINISH_INSERT_CSS,
                "payload": { "css": css }
            }, {
                "frameId": frameId
            });
        }).catch((error) => logger.error("Ошибка при вставке CSS", error));
    };

    /**
     * Загружает опции.
     *
     * :param message: Объект сообщения.
     * :type message: object
     * :param sender: Объект отправителя сообщения.
     * :type sender: object
     * :param sendResponse: Функция обратного вызова для отправки ответа.
     * :type sendResponse: function
     * :return: True для асинхронного ответа.
     * :rtype: bool
     */
    genericListener.listeners.loadOptions = function (message, sender,
                                                      sendResponse) {
        sendResponse({
            "attributes": attributes,
            "css": css,
            "popupCss": popupCss
        });
        return true;
    };

    /**
     * Запрашивает установку информации о контенте.
     *
     * :param message: Объект сообщения.
     * :type message: object
     * :param sender: Объект отправителя сообщения.
     * :type sender: object
     */
    genericListener.listeners.requestSetContentInfo = function (message,
                                                                sender) {
        browser.tabs.sendMessage(sender.tab.id, {
             "timeout":0,
            "timeout_for_event":"presence_of_element_located",
            "event": MSG_EVENT.SET_CONTENT_INFO,
            "payload": { "attributes": attributes }
        }, {
            "frameId": sender.frameId
        });
    };

    #  Слушатель изменений в хранилище
    browser.storage.onChanged.addListener(changes => {
        if (changes.attributes && ("newValue" in changes.attributes)) {
            attributes = changes.attributes.newValue;
        }
        if (changes.css && ("newValue" in changes.css)) {
            css = changes.css.newValue;
        }
        if (changes.popupCss && ("newValue" in changes.popupCss)) {
            popupCss = changes.popupCss.newValue;
        }
    });

    #  Получение настроек из хранилища
    browser.storage.sync.get({
        "attributes": attributes,
        "css": null,
        "popupCss": popupCss
    }).then(items => {
        attributes = items.attributes;
        popupCss = items.popupCss;
        if (items.css !== null) {
            return items.css;
        } else {
            return loadDefaultCss();
        }
    }).then(loadedCss => {
        css = loadedCss;
    }).catch((error) => logger.error("Ошибка при загрузке настроек из хранилища", error));

})(window);
```