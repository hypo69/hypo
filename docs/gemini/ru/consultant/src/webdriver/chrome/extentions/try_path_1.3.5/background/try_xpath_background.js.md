# Анализ кода модуля try_xpath_background.js

**Качество кода**
8
-  Плюсы
    - Код разбит на функции, что улучшает читаемость и поддержку.
    - Используется `browser.runtime.onMessage.addListener` для обработки сообщений, что соответствует стандартам расширений браузера.
    - Применяются Promise для асинхронных операций, что способствует более эффективному коду.
    - Код использует `browser.storage.onChanged.addListener` для отслеживания изменений в хранилище, обеспечивая динамическое обновление.
 -  Минусы
    - Отсутствуют docstring для функций и переменных, что затрудняет понимание кода.
    - Не все ошибки обрабатываются с помощью `logger.error`, что может привести к проблемам с отслеживанием ошибок.
    - Присутствует избыточное использование `try-except`, которое можно заменить на обработку ошибок с помощью `logger.error`.
    - Код использует  `XMLHttpRequest`  вместо `fetch`, который является более современным.
    - Отсутствует проверка на наличие `sender.tab` и `sender.frameId` перед их использованием.

**Рекомендации по улучшению**
1. Добавить docstring для всех функций и переменных в формате reStructuredText (RST) для улучшения читаемости и документирования кода.
2. Использовать `from src.logger.logger import logger` для логирования ошибок и заменить стандартные блоки `try-except` на `logger.error`.
3. Применить `fetch` вместо `XMLHttpRequest` для загрузки CSS, это сделает код более современным и эффективным.
4. Добавить проверку на наличие `sender.tab` и `sender.frameId` перед их использованием, чтобы избежать ошибок.
5. Использовать более современные методы для работы с DOM и CSS, например, `insertCSS` и `removeCSS` с `Promise` для более надежной работы.
6. Переписать существующие комментарии в формате reStructuredText (RST).
7. Использовать более конкретные сообщения в логах, чтобы упростить отладку.

**Оптимизированный код**
```python
"""
Модуль фоновой обработки для расширения try_xpath.
=========================================================================================

Этот модуль обрабатывает сообщения от контентных скриптов и управляет состоянием popup,
а также загружает и применяет CSS стили.
"""
from src.logger.logger import logger
# import browser from webextensions-api-types
# import XMLHttpRequest from webextensions-api-types
(function (window, undefined) {
    "use strict";

    # Объявление псевдонимов для объектов tryxpath и его функций
    var tx = tryxpath;
    var fu = tryxpath.functions;

    # Инициализация переменных для хранения состояния popup, CSS, результатов и атрибутов
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
     * :return: Promise, который разрешается с загруженным CSS или отклоняется с ошибкой.
     */
    function loadDefaultCss() {
       return fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
            .then(response => {
                if (!response.ok) {
                     # Логирование ошибки при неудачной загрузке CSS
                    logger.error(`Ошибка загрузки CSS: ${response.status} ${response.statusText}`);
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .catch(error => {
                 # Логирование ошибки при загрузке CSS
                logger.error(`Ошибка загрузки CSS: ${error}`);
                throw error;
            });
    }
    /**
     * Слушатель для обработки сообщений из контентных скриптов.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция для отправки ответа.
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
     * Сохраняет состояние popup.
     *
     * :param message: Объект сообщения с состоянием popup.
     */
    genericListener.listeners.storePopupState = function (message) {
        popupState = message.state;
    }

    /**
     * Запрашивает восстановление состояния popup.
     *
     * :param message: Объект сообщения.
     */
    genericListener.listeners.requestRestorePopupState = function (message) {
        browser.runtime.sendMessage({
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "restorePopupState",
            "state": popupState
        });
    };
    /**
     * Запрашивает вставку CSS в popup.
     *
     */
    genericListener.listeners.requestInsertStyleToPopup = function () {
        browser.runtime.sendMessage({
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "insertStyleToPopup",
            "css": popupCss
        });
    };
    /**
     * Отображает все результаты на новой вкладке.
     *
     * :param message: Объект сообщения с результатами.
     * :param sender: Объект отправителя.
     */
    genericListener.listeners.showAllResults = function(message, sender) {
        delete message.event;
        results = message;
        results.tabId = sender.tab.id;
        results.frameId = sender.frameId;
        browser.tabs.create({ "url": "/pages/show_all_results.html" });
    };
    /**
     * Загружает результаты.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция для отправки ответа.
     * :return: true.
     */
    genericListener.listeners.loadResults = function (message, sender,
                                                      sendResponse) {
        sendResponse(results);
        return true;
    };
    /**
     * Обновляет CSS на вкладке.
     *
     * :param message: Объект сообщения с CSS.
     * :param sender: Объект отправителя.
     */
    genericListener.listeners.updateCss = async function (message, sender) {
          # Проверка существования sender.tab и sender.frameId
        if (!sender || !sender.tab || sender.frameId === undefined) {
            logger.error("Некорректный отправитель сообщения", sender);
            return;
        }
        var id = sender.tab.id;
        var frameId = sender.frameId;

        # Удаление устаревших стилей
        for (let removeCss in message.expiredCssSet) {
            try {
                 await browser.tabs.removeCSS(id, {
                    "code": removeCss,
                    "matchAboutBlank": true,
                    "frameId": frameId
                });
                # Отправка сообщения об успешном удалении CSS
                 await browser.tabs.sendMessage(id, {
                     "timeout":0,"timeout_for_event":"presence_of_element_located","event": "finishRemoveCss",
                     "css": removeCss
                 }, {
                     "frameId": frameId
                 });
            } catch (error) {
                logger.error(`Ошибка при удалении CSS: ${error}`, error)
            }

        }

         try {
            # Вставка нового CSS
            await browser.tabs.insertCSS(id, {
                "code": css,
                "cssOrigin": "author",
                "matchAboutBlank": true,
                "frameId": frameId
            });
            # Отправка сообщения об успешной вставке CSS
             await browser.tabs.sendMessage(id, {
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "finishInsertCss",
                "css": css
            }, {
                "frameId": frameId
            });
        } catch (error) {
             # Логирование ошибки при вставке CSS
            logger.error(`Ошибка при вставке CSS: ${error}`, error);
        }
    };
    /**
     * Загружает опции.
     *
     * :param message: Объект сообщения.
     * :param sender: Объект отправителя.
     * :param sendResponse: Функция для отправки ответа.
     * :return: true.
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
        # Проверка существования sender.tab и sender.frameId
        if (!sender || !sender.tab || sender.frameId === undefined) {
            logger.error("Некорректный отправитель сообщения", sender);
            return;
        }
        browser.tabs.sendMessage(sender.tab.id, {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "setContentInfo",
            "attributes": attributes
        }, {
            "frameId": sender.frameId
        });
    };

     # Слушатель изменений в хранилище
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

    # Получение данных из хранилища и загрузка CSS
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
    }).catch(fu.onError);

})(window);