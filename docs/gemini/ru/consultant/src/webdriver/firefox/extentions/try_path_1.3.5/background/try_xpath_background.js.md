# Анализ кода модуля try_xpath_background.js

**Качество кода**
7
-  Плюсы
    - Код разбит на логические блоки, что облегчает понимание его структуры.
    - Используются `Promise` для асинхронных операций, что улучшает обработку событий.
    - Применяется `browser.storage.onChanged` для отслеживания изменений в настройках расширения.
    - Есть обработка ошибок (хотя и простая) через `catch(fu.onError)`.
    - Функция `genericListener` с объектом `listeners` — удачное решение для обработки разных типов сообщений.
-  Минусы
    - Отсутствует подробная документация (docstrings) для функций и переменных.
    - Используется стандартный `XMLHttpRequest` вместо `fetch`, который является более современным API.
    - Обработка ошибок в основном сводится к `fu.onError`, без конкретного логирования.
    - В коде нет явного импорта модуля `src.utils.jjson`.
    - Код не имеет комментариев в формате reStructuredText (RST), как требуется.
    - Код не использует `logger` для логирования.
    - Код излишне использует `try-except`, где можно обойтись проверками.

**Рекомендации по улучшению**
1.  Добавить docstrings в формате RST для всех функций, переменных и модуля.
2.  Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3.  Использовать `logger.error` для более детального логирования ошибок.
4.  Использовать `j_loads` для разбора json (в данном случае не нужно так как json не разбирается).
5.  Добавить необходимые импорты, такие как `from src.logger.logger import logger`.
6.  Избегать излишнего использования `try-except` блоков.
7.  Обеспечить соответствие имен переменных и функций с ранее обработанными файлами.
8.  Добавить подробные комментарии к блокам кода.

**Оптимизированный код**
```python
"""
Модуль фонового скрипта для расширения Try XPath.
=========================================================================================

Этот модуль обеспечивает функциональность фонового скрипта для расширения Try XPath,
включая обработку сообщений, управление состоянием всплывающего окна,
взаимодействие с хранилищем браузера и внедрение стилей.

"""
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

# alias
tx = tryxpath
fu = tryxpath.functions

popupState = None
"""Состояние всплывающего окна."""

popupCss = "body{width:367px;height:auto;}"
"""CSS для всплывающего окна по умолчанию."""

results = {}
"""Объект для хранения результатов XPath запросов."""

css = ""
"""CSS для внедрения на страницы."""

attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}
"""Объект для хранения атрибутов элементов."""


def loadDefaultCss() -> Promise:
    """
    Загружает CSS по умолчанию из файла.

    :return: Promise, который резолвится с текстом CSS или реджектится в случае ошибки.
    """
    return new Promise((resolve, reject) => {
        # Код создает новый XMLHttpRequest для загрузки CSS файла
        var req = new XMLHttpRequest();
        # Код открывает GET запрос по URL, полученному от browser.runtime.getURL
        req.open("GET", browser.runtime.getURL("/css/try_xpath_insert.css"));
        # Код устанавливает тип ответа как текст
        req.responseType = "text";
        # Код устанавливает обработчик события изменения состояния запроса
        req.onreadystatechange = function () {
            # Код проверяет, завершен ли запрос
            if (req.readyState === XMLHttpRequest.DONE) {
                # Код резолвит Promise с текстом ответа
                resolve(req.responseText);
            }
        };
        # Код отправляет запрос
        req.send();
    });


def genericListener(message, sender, sendResponse):
    """
     Универсальный обработчик сообщений.

    :param message: Сообщение от контент-скрипта или другого расширения.
    :param sender: Информация об отправителе сообщения.
    :param sendResponse: Функция для отправки ответа.
    :return: Результат вызова обработчика, если он найден.
    """
    # Код получает обработчик из genericListener.listeners по ключу message.event
    listener = genericListener.listeners[message.event];
    # Код проверяет, найден ли обработчик
    if listener:
        # Код вызывает обработчик и возвращает результат
        return listener(message, sender, sendResponse);
    # Если обработчик не найден, функция завершается


# Код создает пустой объект для хранения обработчиков
genericListener.listeners = Object.create(null);
# Код устанавливает слушателя сообщений на событие browser.runtime.onMessage
browser.runtime.onMessage.addListener(genericListener);


def storePopupState(message):
    """
    Сохраняет состояние всплывающего окна.

    :param message: Сообщение с состоянием всплывающего окна.
    """
    # Код сохраняет состояние всплывающего окна
    popupState = message.state;


genericListener.listeners.storePopupState = storePopupState;


def requestRestorePopupState(message):
    """
    Отправляет запрос на восстановление состояния всплывающего окна.

    :param message: Сообщение с запросом на восстановление состояния.
    """
    # Код отправляет сообщение на восстановление состояния всплывающего окна
    browser.runtime.sendMessage({
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "restorePopupState",
        "state": popupState
    });


genericListener.listeners.requestRestorePopupState = requestRestorePopupState;


def requestInsertStyleToPopup():
    """
    Отправляет запрос на вставку стилей во всплывающее окно.
    """
    # Код отправляет сообщение на вставку стилей во всплывающее окно
    browser.runtime.sendMessage({
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "insertStyleToPopup",
        "css": popupCss
    });


genericListener.listeners.requestInsertStyleToPopup = requestInsertStyleToPopup;


def showAllResults(message, sender):
    """
    Сохраняет результаты XPath и открывает новую вкладку для их отображения.

    :param message: Сообщение с результатами.
    :param sender: Информация об отправителе сообщения.
    """
    # Код удаляет событие из сообщения
    del message.event;
    # Код сохраняет результаты
    results = message;
    # Код сохраняет id вкладки
    results.tabId = sender.tab.id;
    # Код сохраняет id фрейма
    results.frameId = sender.frameId;
    # Код открывает новую вкладку для отображения результатов
    browser.tabs.create({"url": "/pages/show_all_results.html"});


genericListener.listeners.showAllResults = showAllResults;


def loadResults(message, sender, sendResponse):
    """
    Отправляет сохраненные результаты XPath по запросу.

    :param message: Сообщение с запросом результатов.
    :param sender: Информация об отправителе сообщения.
    :param sendResponse: Функция для отправки ответа с результатами.
    :return: True, для асинхронного ответа.
    """
    # Код отправляет сохраненные результаты
    sendResponse(results);
    # Код возвращает true для асинхронного ответа
    return True;


genericListener.listeners.loadResults = loadResults;


def updateCss(message, sender):
    """
    Обновляет CSS на странице, удаляя старые и вставляя новые.

    :param message: Сообщение с информацией об устаревших стилях.
    :param sender: Информация об отправителе сообщения.
    """
    # Код получает id вкладки
    id = sender.tab.id;
    # Код получает id фрейма
    frameId = sender.frameId;

    # Код перебирает CSS для удаления
    for removeCss in message.expiredCssSet:
        # Код удаляет CSS
        browser.tabs.removeCSS(id, {
            "code": removeCss,
            "matchAboutBlank": True,
            "frameId": frameId
        }).then(() => {
            # Код отправляет сообщение о завершении удаления CSS
            return browser.tabs.sendMessage(id, {
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "finishRemoveCss",
                "css": removeCss
            }, {
                "frameId": frameId
            });
        }).catch(lambda ex: logger.error(f'Ошибка удаления CSS: {removeCss}', ex));  # Используем лямбду для передачи ex

    # Код вставляет новый CSS
    browser.tabs.insertCSS(id, {
        "code": css,
        "cssOrigin": "author",
        "matchAboutBlank": True,
        "frameId": frameId
    }).then(() => {
        # Код отправляет сообщение о завершении вставки CSS
        return browser.tabs.sendMessage(id, {
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": "finishInsertCss",
            "css": css
        }, {
            "frameId": frameId
        });
    }).catch(lambda ex: logger.error(f'Ошибка вставки CSS: {css}', ex));  # Используем лямбду для передачи ex


genericListener.listeners.updateCss = updateCss;


def loadOptions(message, sender, sendResponse):
    """
    Отправляет текущие настройки расширения.

    :param message: Сообщение с запросом настроек.
    :param sender: Информация об отправителе сообщения.
    :param sendResponse: Функция для отправки ответа с настройками.
    :return: True для асинхронного ответа.
    """
    # Код отправляет настройки расширения
    sendResponse({
        "attributes": attributes,
        "css": css,
        "popupCss": popupCss
    });
    # Код возвращает true для асинхронного ответа
    return True;


genericListener.listeners.loadOptions = loadOptions;


def requestSetContentInfo(message, sender):
    """
    Отправляет сообщение контент-скрипту с информацией о атрибутах.

    :param message: Сообщение с запросом на установку информации.
    :param sender: Информация об отправителе сообщения.
    """
    # Код отправляет сообщение контент-скрипту об установке информации
    browser.tabs.sendMessage(sender.tab.id, {
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "setContentInfo",
        "attributes": attributes
    }, {
        "frameId": sender.frameId
    });


genericListener.listeners.requestSetContentInfo = requestSetContentInfo;


# Код устанавливает слушателя изменений в хранилище
browser.storage.onChanged.addListener(changes => {
    # Код проверяет, есть ли изменения в attributes
    if (changes.attributes and ("newValue" in changes.attributes)):
        # Код обновляет атрибуты
        attributes = changes.attributes.newValue;
    # Код проверяет, есть ли изменения в css
    if (changes.css and ("newValue" in changes.css)):
        # Код обновляет css
        css = changes.css.newValue;
    # Код проверяет, есть ли изменения в popupCss
    if (changes.popupCss and ("newValue" in changes.popupCss)):
        # Код обновляет popupCss
        popupCss = changes.popupCss.newValue;
});


# Код получает настройки из хранилища
browser.storage.sync.get({
    "attributes": attributes,
    "css": None,
    "popupCss": popupCss
}).then(items => {
    # Код устанавливает атрибуты
    attributes = items.attributes;
    # Код устанавливает popupCss
    popupCss = items.popupCss;
    # Код проверяет, есть ли css
    if (items.css is not None):
        # Код возвращает css
        return items.css;
    else:
        # Код загружает css по умолчанию
        return loadDefaultCss();
}).then(loadedCss => {
    # Код устанавливает загруженный css
    css = loadedCss;
}).catch(lambda ex: logger.error('Ошибка при загрузке или установке css', ex)); # Используем лямбду для передачи ex
```