# Анализ кода модуля try_xpath_background.js

**Качество кода**
7
- Плюсы
    - Код использует асинхронные операции с `Promise`, что хорошо для неблокирующего поведения.
    - Применение `browser.runtime.onMessage.addListener` для обработки сообщений от других частей расширения.
    - Организация слушателей сообщений в `genericListener.listeners`.
    - Разделение логики на функции.
    - Использование `browser.storage.sync.get` для загрузки настроек расширения.
- Минусы
    - Отсутствуют docstring для функций и переменных.
    - Использование `XMLHttpRequest` вместо более современного `fetch` для загрузки CSS.
    - Дублирование кода при отправке сообщений с `timeout` и `timeout_for_event`
    -  Многократное использование  `browser.tabs.sendMessage`  с одинаковыми параметрами.
    -  Не всегда используется `logger.error` для обработки ошибок, а используется `fu.onError`.
    -  Нет обработки ошибок при загрузке CSS из `browser.storage.sync.get`.
    -  Код недостаточно документирован (нет docstring).

**Рекомендации по улучшению**
1. **Документирование кода:**
   - Добавить docstring для всех функций, переменных и модулей в формате reStructuredText (RST).
2. **Использование `fetch`:**
   - Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3. **Логирование ошибок:**
   - Использовать `logger.error` вместо `fu.onError` для более информативного логирования ошибок.
4. **Упрощение отправки сообщений:**
   - Создать функцию-обёртку для отправки сообщений с `timeout` и `timeout_for_event`, чтобы избежать дублирования кода.
5. **Обработка ошибок:**
   - Добавить обработку ошибок при загрузке CSS из `browser.storage.sync.get`.
   - Проверять успешность выполнения `browser.tabs.insertCSS` и `browser.tabs.removeCSS` с помощью `then` и `catch`.
6. **Рефакторинг:**
    - Переименовать переменные, например `tx` и `fu` на более понятные `try_xpath` и `try_xpath_functions`.
    - Удалить излишние `return true` там, где он не нужен.
    - Вынести повторяющиеся части кода в отдельные функции (например, отправку сообщений с общими параметрами).
7.  **Использовать J_LOADS:**
    - Проверить необходимость использования `j_loads` или `j_loads_ns` при работе с json.
8.  **Сократить дублирование кода**
    - Удалить дублирование кода при отправке сообщений, вынеся общие параметры в отдельную функцию.

**Оптимизированный код**
```python
"""
Модуль для управления фоновыми процессами расширения Try Xpath.
=================================================================

Этот модуль обрабатывает сообщения от других частей расширения,
управляет состоянием всплывающего окна, загружает и применяет стили,
а также взаимодействует с хранилищем для сохранения и загрузки настроек.

Основные функции:
    - Загрузка и применение стилей CSS.
    - Обработка сообщений для управления состоянием всплывающего окна.
    - Взаимодействие с хранилищем для сохранения и загрузки настроек.
"""
from src.logger.logger import logger
#from src.utils.jjson import j_loads, j_loads_ns # TODO добавить если нужно использовать j_loads

#    /* This Source Code Form is subject to the terms of the Mozilla Public
#     * License, v. 2.0. If a copy of the MPL was not distributed with this
#     * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#
(function (window, undefined) {
    "use strict";
    # Объявление переменных и констант
    # alias
    var try_xpath = tryxpath;
    var try_xpath_functions = tryxpath.functions;

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

    /**
     * Загружает CSS по умолчанию из файла.
     *
     * :return: Promise с текстом CSS.
     */
    function loadDefaultCss() {
        return fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
            .then(response => {
                if (!response.ok) {
                    # Логирование ошибки при неудачном запросе
                    logger.error(f'Ошибка загрузки CSS: {response.status} {response.statusText}')
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
           # Обработка ошибок при загрузке CSS
            .catch(error => {
               logger.error(f'Ошибка при загрузке CSS: {error}')
               return "";
        });
    }

    /**
     * Отправляет сообщение с общими параметрами.
     *
     * :param tabId: ID вкладки.
     * :param message: Объект сообщения для отправки.
     * :param frameId: ID фрейма.
     * :return: Promise с результатом отправки сообщения.
     */
    function sendMessageToTab(tabId, message, frameId) {
          # Выполняет отправку сообщения на вкладку с заданными параметрами
        return browser.tabs.sendMessage(tabId, {
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            ...message
        }, {
            "frameId": frameId
        }).catch(error => {
            # Логирование ошибки при отправке сообщения
              logger.error(f'Ошибка отправки сообщения: {error}')
        });
    }

    /**
     * Общий обработчик сообщений.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция обратного вызова.
     * :return: Результат выполнения слушателя.
     */
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    }
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);

    /**
     * Сохраняет состояние всплывающего окна.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.storePopupState = function (message) {
        popupState = message.state;
    }

    /**
     * Запрашивает восстановление состояния всплывающего окна.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.requestRestorePopupState = function (message) {
       # Отправка запроса на востановление состояния всплывающего окна
        browser.runtime.sendMessage({
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "restorePopupState",
            "state": popupState
        });
    };

    /**
     * Запрашивает вставку стилей во всплывающее окно.
     */
    genericListener.listeners.requestInsertStyleToPopup = function () {
       # Отправка запроса на вставку стилей во всплывающее окно
        browser.runtime.sendMessage({
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "insertStyleToPopup",
            "css": popupCss
        });
    };

    /**
     * Отображает все результаты.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     */
    genericListener.listeners.showAllResults = function(message, sender) {
        delete message.event;
        results = message;
        results.tabId = sender.tab.id;
        results.frameId = sender.frameId;
         # Создание новой вкладки для отображения результатов
        browser.tabs.create({ "url": "/pages/show_all_results.html" });
    };

    /**
     * Загружает результаты.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция обратного вызова.
     * :return: `true`, если обработка выполнена.
     */
    genericListener.listeners.loadResults = function (message, sender,
                                                      sendResponse) {
        sendResponse(results);
        return true;
    };

    /**
     * Обновляет стили CSS на странице.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     */
    genericListener.listeners.updateCss = async function (message, sender) {
        var id = sender.tab.id;
        var frameId = sender.frameId;

        for (let removeCss in message.expiredCssSet) {
            try {
                # Код удаляет CSS
                await browser.tabs.removeCSS(id, {
                    "code": removeCss,
                    "matchAboutBlank": true,
                    "frameId": frameId
                });
                # Код отправляет сообщение об окончании удаления CSS
                await sendMessageToTab(id, { "event": "finishRemoveCss", "css": removeCss }, frameId);
            }
             # Логирование ошибки при удалении CSS
            catch(error){
                 logger.error(f'Ошибка удаления CSS: {error}')
                 
            }
        }
        try {
            # Код вставляет CSS
            await browser.tabs.insertCSS(id, {
                "code": css,
                "cssOrigin": "author",
                "matchAboutBlank": true,
                "frameId": frameId
            });
           # Код отправляет сообщение об окончании вставки CSS
            await sendMessageToTab(id, { "event": "finishInsertCss", "css": css }, frameId);
        }
         # Логирование ошибки при вставке CSS
        catch(error){
            logger.error(f'Ошибка вставки CSS: {error}')
        }
    };


    /**
     * Загружает опции.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция обратного вызова.
     * :return: `true`, если обработка выполнена.
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
     * :param sender: Объект отправителя.
     */
    genericListener.listeners.requestSetContentInfo = function (message,
                                                                sender) {
        # Код отправляет сообщение на вкладку с запросом на установку информации о контенте
        browser.tabs.sendMessage(sender.tab.id, {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setContentInfo",
            "attributes": attributes
        }, {
            "frameId": sender.frameId
        });
    };

    # Код обрабатывает изменения в хранилище
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

    # Код получает данные из хранилища
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
    }).catch(error =>{
         # Логирование ошибки при загрузке CSS из хранилища
            logger.error(f'Ошибка при загрузке настроек из хранилища: {error}')
    });

})(window);