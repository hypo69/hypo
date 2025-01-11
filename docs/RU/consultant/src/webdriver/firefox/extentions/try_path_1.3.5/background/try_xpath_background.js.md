# Анализ кода модуля try_xpath_background.js

**Качество кода**
8
-  Плюсы
    - Код разбит на функции, что делает его более читаемым и поддерживаемым.
    - Используется `browser.runtime.onMessage.addListener` для обработки сообщений, что является стандартным подходом для расширений браузера.
    - Применяется `browser.storage.onChanged.addListener` для отслеживания изменений в хранилище, что позволяет динамически обновлять параметры расширения.
    - Используются Promise для асинхронных операций, что позволяет избежать callback hell.
    -  Код использует `browser.runtime.getURL` для получения URL ресурсов расширения, что является правильным подходом.
-  Минусы
    -  Отсутствует обработка ошибок при отправке сообщений через `browser.tabs.sendMessage`.
    -  Отсутствуют docstring для функций.
    -  Много однотипных сообщений для `browser.tabs.sendMessage` с одинаковыми `timeout` и `timeout_for_event`.
    -  Используются сокращения `tx`, `fu` без пояснений.
    -  Отсутствует описание модуля в начале файла.

**Рекомендации по улучшению**

1. **Документирование кода**: Добавить docstring для всех функций, переменных и модуля с описанием их назначения и параметров.
2. **Обработка ошибок**: Добавить обработку ошибок при отправке сообщений `browser.tabs.sendMessage` с помощью `logger.error`.
3. **Унификация сообщений**: Создать константы для часто используемых параметров сообщений `browser.tabs.sendMessage` (например, `timeout` и `timeout_for_event`).
4. **Улучшение читаемости**: Избегать сокращений `tx`, `fu` или добавить их определения как константы с понятными именами.
5. **Логирование**: Использовать `logger` для вывода информации о происходящих событиях и ошибках.
6. **Удаление избыточных `return`**:  В некоторых местах можно убрать `return true` если нет дополнительной логики.
7.  **Использовать константы**: Вынести повторяющиеся строки в константы.

**Оптимизированный код**
```python
"""
Модуль фонового скрипта расширения Try XPath.
=========================================================================================

Этот модуль обрабатывает сообщения от контентных скриптов и всплывающих окон,
управляет состоянием расширения, загружает и применяет стили, а также взаимодействует
с хранилищем браузера для сохранения и извлечения параметров.

"""
from src.logger import logger

# alias
# Код создает псевдоним для объекта tryxpath
tx = tryxpath
# Код создает псевдоним для объекта tryxpath.functions
fu = tryxpath.functions

# Код задает начальное состояние всплывающего окна
popupState = None
# Код задает CSS для всплывающего окна
popupCss = "body{width:367px;height:auto;}"
# Код создает пустой объект для результатов
results = {}
# Код создает пустую строку для CSS
css = ""
# Код создает объект с атрибутами
attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}
#  Константы для сообщений
TIMEOUT_MESSAGE = {"timeout": 0, "timeout_for_event": "presence_of_element_located"}
# Константы для путей
CSS_PATH = "/css/try_xpath_insert.css"

async def loadDefaultCss() -> str:
    """
    Загружает CSS по умолчанию из файла расширения.

    Returns:
        str: CSS текст из файла.
    Raises:
         Exception:  При возникновении ошибки запроса.
    """
    try:
        # Код выполняет запрос на получение CSS
        req =  XMLHttpRequest()
        req.open("GET", browser.runtime.getURL(CSS_PATH))
        req.responseType = "text"
        await new Promise((resolve, reject) => {
                req.onreadystatechange = function () {
                    if (req.readyState === XMLHttpRequest.DONE) {
                        resolve(req.responseText)
                    }
                }
                req.send()
        })
        return req.responseText
    except Exception as ex:
        logger.error('Ошибка при загрузке CSS по умолчанию', ex)
        return ''


def genericListener(message: dict, sender: dict, sendResponse: callable) -> bool | None:
    """
     Обрабатывает сообщения, отправленные из других частей расширения.

    Args:
        message (dict): Объект сообщения.
        sender (dict): Информация об отправителе сообщения.
        sendResponse (callable): Функция обратного вызова для отправки ответа.

    Returns:
        bool | None: Возвращает True если сообщение обработано и требует ответа, иначе None.
    """
    # Код проверяет наличие слушателя для события
    listener = genericListener.listeners.get(message.event)
    if listener:
        # Код вызывает функцию-обработчик сообщения и возвращает результат её выполнения
        return listener(message, sender, sendResponse)
    return None

# Код создает объект для хранения слушателей
genericListener.listeners = {}
# Код добавляет слушателя для сообщений
browser.runtime.onMessage.addListener(genericListener)


def storePopupState(message: dict) -> None:
    """
    Сохраняет состояние всплывающего окна.

    Args:
        message (dict): Объект сообщения, содержащий состояние.
    """
    # Код устанавливает состояние всплывающего окна из сообщения
    global popupState
    popupState = message.state

genericListener.listeners["storePopupState"] = storePopupState

def requestRestorePopupState() -> None:
    """
    Отправляет запрос на восстановление состояния всплывающего окна.
    """
    # Код отправляет сообщение для восстановления состояния всплывающего окна
    browser.runtime.sendMessage({
        **TIMEOUT_MESSAGE,
        "event": "restorePopupState",
        "state": popupState
    })

genericListener.listeners["requestRestorePopupState"] = requestRestorePopupState


def requestInsertStyleToPopup() -> None:
    """
    Отправляет запрос на вставку стилей во всплывающее окно.
    """
    # Код отправляет сообщение для вставки стилей во всплывающее окно
    browser.runtime.sendMessage({
        **TIMEOUT_MESSAGE,
        "event": "insertStyleToPopup",
        "css": popupCss
    })

genericListener.listeners["requestInsertStyleToPopup"] = requestInsertStyleToPopup


def showAllResults(message: dict, sender: dict) -> None:
    """
    Открывает страницу со всеми результатами поиска.

    Args:
        message (dict): Объект сообщения с результатами.
        sender (dict): Информация об отправителе сообщения.
    """
    # Код удаляет событие из сообщения
    del message.event
    # Код сохраняет результаты и информацию об отправителе
    global results
    results = message
    results["tabId"] = sender.tab.id
    results["frameId"] = sender.frameId
    # Код открывает страницу с результатами
    browser.tabs.create({"url": "/pages/show_all_results.html"})

genericListener.listeners["showAllResults"] = showAllResults


def loadResults(message: dict, sender: dict, sendResponse: callable) -> bool:
    """
    Отправляет сохраненные результаты запросившему скрипту.

    Args:
        message (dict): Объект сообщения.
        sender (dict): Информация об отправителе сообщения.
        sendResponse (callable): Функция обратного вызова для отправки ответа.

    Returns:
         bool: True, если ответ отправлен.
    """
    # Код отправляет результаты запросившему скрипту
    sendResponse(results)
    return True

genericListener.listeners["loadResults"] = loadResults


async def updateCss(message: dict, sender: dict) -> None:
    """
    Обновляет CSS на странице, удаляя старый и вставляя новый.

    Args:
        message (dict): Объект сообщения с информацией об устаревших CSS.
        sender (dict): Информация об отправителе сообщения.
    """
    # Код извлекает ID вкладки и ID фрейма
    id = sender.tab.id
    frameId = sender.frameId

    # Код удаляет устаревшие стили
    for removeCss in message.get("expiredCssSet", []):
         try:
            await browser.tabs.removeCSS(id, {
                    "code": removeCss,
                    "matchAboutBlank": True,
                    "frameId": frameId
                })
            # Код отправляет сообщение об окончании удаления
            await browser.tabs.sendMessage(id, {
                **TIMEOUT_MESSAGE,
                "event": "finishRemoveCss",
                "css": removeCss
            }, {"frameId": frameId})

         except Exception as ex:
                logger.error(f'Ошибка при удалении CSS: {removeCss}', ex)
    try:
    # Код вставляет новый CSS
        await browser.tabs.insertCSS(id, {
            "code": css,
            "cssOrigin": "author",
            "matchAboutBlank": True,
            "frameId": frameId
        })
        # Код отправляет сообщение об окончании вставки
        await browser.tabs.sendMessage(id, {
            **TIMEOUT_MESSAGE,
            "event": "finishInsertCss",
            "css": css
        }, {"frameId": frameId})

    except Exception as ex:
        logger.error('Ошибка при вставке нового CSS', ex)

genericListener.listeners["updateCss"] = updateCss


def loadOptions(message: dict, sender: dict, sendResponse: callable) -> bool:
    """
    Отправляет текущие параметры расширения запросившему скрипту.

    Args:
        message (dict): Объект сообщения.
        sender (dict): Информация об отправителе сообщения.
        sendResponse (callable): Функция обратного вызова для отправки ответа.

    Returns:
        bool: True, если ответ отправлен.
    """
    # Код отправляет текущие параметры
    sendResponse({
        "attributes": attributes,
        "css": css,
        "popupCss": popupCss
    })
    return True

genericListener.listeners["loadOptions"] = loadOptions


def requestSetContentInfo(message: dict, sender: dict) -> None:
    """
    Отправляет запрос на установку информации о содержимом страницы.

    Args:
        message (dict): Объект сообщения.
        sender (dict): Информация об отправителе сообщения.
    """
    # Код отправляет сообщение на установку информации о содержимом
    try:
        browser.tabs.sendMessage(sender.tab.id, {
            **TIMEOUT_MESSAGE,
            "event": "setContentInfo",
            "attributes": attributes
        }, {"frameId": sender.frameId})
    except Exception as ex:
       logger.error('Ошибка при отправке сообщения setContentInfo', ex)

genericListener.listeners["requestSetContentInfo"] = requestSetContentInfo

def update_settings(changes: dict) -> None:
    """
    Обновляет локальные переменные при изменении настроек в хранилище.

    Args:
        changes (dict): Объект с изменениями в хранилище.
    """
    # Код обновляет атрибуты, если они были изменены
    global attributes
    if "attributes" in changes and "newValue" in changes["attributes"]:
        attributes = changes["attributes"]["newValue"]
    # Код обновляет CSS, если он был изменен
    global css
    if "css" in changes and "newValue" in changes["css"]:
        css = changes["css"]["newValue"]
     # Код обновляет CSS для попапа, если он был изменен
    global popupCss
    if "popupCss" in changes and "newValue" in changes["popupCss"]:
        popupCss = changes["popupCss"]["newValue"]

# Код добавляет слушателя для изменений в хранилище
browser.storage.onChanged.addListener(update_settings)

async def load_initial_settings() -> None:
     """
     Загружает начальные настройки из хранилища и CSS.
     """
     try:
        # Код извлекает настройки из хранилища
        items = await browser.storage.sync.get({
            "attributes": attributes,
            "css": None,
            "popupCss": popupCss
        })
        global attributes
        attributes = items["attributes"]
        global popupCss
        popupCss = items["popupCss"]

        # Код загружает CSS
        if items["css"] is not None:
            loadedCss = items["css"]
        else:
            loadedCss = await loadDefaultCss()
        global css
        css = loadedCss
     except Exception as ex:
        logger.error('Ошибка при загрузке начальных настроек', ex)

# Код загружает начальные настройки и CSS
load_initial_settings()