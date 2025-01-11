# Анализ кода модуля `try_xpath_background.js`

**Качество кода**
8
-  Плюсы
    -   Код хорошо структурирован, с использованием функций для разделения логики.
    -   Используется `Promise` для асинхронных операций.
    -   Обработчики событий (`browser.runtime.onMessage`, `browser.storage.onChanged`) используются корректно.
    -   Присутствует обработка ошибок через `catch(fu.onError)`.
-  Минусы
    -   Не хватает документации в формате RST для функций и модуля.
    -   Отсутствует импорт `logger` из `src.logger`.
    -   Используется стандартный `XMLHttpRequest` вместо `fetch` для загрузки CSS.
    -   Использование `then().then()` может быть заменено на `async/await` для большей читаемости.
    -  `genericListener.listeners` объявлен как `Object.create(null)`, что может привести к проблемам с расширением. Лучше использовать обычный объект `{}`.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля и функций.
2.  Импортировать `logger` из `src.logger.logger` для логирования ошибок.
3.  Использовать `fetch` вместо `XMLHttpRequest` для загрузки CSS.
4.  Использовать `async/await` для упрощения асинхронного кода.
5.  Заменить `Object.create(null)` на `{}` при объявлении `genericListener.listeners`.
6.  Добавить обработку ошибок в `browser.storage.onChanged`
7.  Удалить  `"timeout":0,"timeout_for_event":"presence_of_element_located"` так как этот ключ не используется
8.  Добавить проверку `id` и `frameId` на существование

**Оптимизированный код**

```python
"""
Модуль для фоновой работы расширения Try XPath.
===================================================

Этот модуль обрабатывает сообщения от контент-скриптов и всплывающих окон,
управляет стилями и хранит состояние.
"""
from src.logger.logger import logger

# alias
# var tx = tryxpath;
# var fu = tryxpath.functions;

popupState = None
popupCss = "body{width:367px;height:auto;}"
results = {}
css = ""
attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}

async def loadDefaultCss():
    """
    Загружает CSS по умолчанию из файла.

    Returns:
        str: Содержимое CSS файла.
    """
    try:
        response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
        if not response.ok:
            logger.error(f"Failed to fetch default CSS, status: {response.status}")
            return ""
        return await response.text()
    except Exception as e:
        logger.error("Error loading default CSS:", e)
        return ""

def genericListener(message, sender, sendResponse):
    """
     Обрабатывает входящие сообщения и вызывает соответствующий обработчик.

     Args:
         message (dict): Объект сообщения.
         sender (object): Объект отправителя сообщения.
         sendResponse (function): Функция для отправки ответа.
     Returns:
         bool | None: Возвращает True, если функция должна удерживать канал связи, иначе None.
    """
    listener = genericListener.listeners.get(message.event)
    if listener:
        return listener(message, sender, sendResponse)

genericListener.listeners = {}
browser.runtime.onMessage.addListener(genericListener)

def storePopupState(message):
    """
    Сохраняет состояние всплывающего окна.

    Args:
        message (dict): Сообщение, содержащее состояние всплывающего окна.
    """
    global popupState
    popupState = message.state

genericListener.listeners['storePopupState'] = storePopupState

def requestRestorePopupState(message):
    """
    Запрашивает восстановление состояния всплывающего окна.

    Args:
        message (dict): Сообщение запроса.
    """
    browser.runtime.sendMessage({
        "event": "restorePopupState",
        "state": popupState
    })

genericListener.listeners['requestRestorePopupState'] = requestRestorePopupState


def requestInsertStyleToPopup(message):
    """
    Запрашивает вставку стилей во всплывающее окно.
    """
    browser.runtime.sendMessage({
        "event": "insertStyleToPopup",
        "css": popupCss
    })

genericListener.listeners['requestInsertStyleToPopup'] = requestInsertStyleToPopup

def showAllResults(message, sender):
    """
    Сохраняет результаты и открывает страницу со всеми результатами.
    Args:
         message (dict):  Объект сообщения.
         sender (object): Объект отправителя сообщения.
    """
    global results
    del message.event
    results = message
    results["tabId"] = sender.tab.id
    results["frameId"] = sender.frameId
    browser.tabs.create({"url": "/pages/show_all_results.html"})

genericListener.listeners['showAllResults'] = showAllResults

def loadResults(message, sender, sendResponse):
    """
     Отправляет сохраненные результаты.

     Args:
         message (dict): Объект сообщения.
         sender (object): Объект отправителя сообщения.
         sendResponse (function): Функция для отправки ответа.
     Returns:
         bool: Возвращает True, чтобы сохранить канал связи открытым.
    """
    sendResponse(results)
    return True

genericListener.listeners['loadResults'] = loadResults

async def updateCss(message, sender):
    """
     Обновляет CSS на странице.

     Args:
        message (dict): Сообщение, содержащее данные для обновления CSS.
        sender (object): Объект отправителя сообщения.
    """
    id = sender.tab.id
    frameId = sender.frameId
    if not id or not frameId:
        logger.error(f'Не верные данные tabId: {id=}  frameId: {frameId=}')
        return

    for removeCss in message.expiredCssSet:
        try:
            await browser.tabs.removeCSS(id, {
                "code": removeCss,
                "matchAboutBlank": True,
                "frameId": frameId
            })
            await browser.tabs.sendMessage(id, {
                 "event": "finishRemoveCss",
                "css": removeCss
            }, {
                "frameId": frameId
            })
        except Exception as e:
            logger.error(f"Error removing CSS {removeCss=}:", e)

    try:
        await browser.tabs.insertCSS(id, {
            "code": css,
            "cssOrigin": "author",
            "matchAboutBlank": True,
            "frameId": frameId
        })
        await browser.tabs.sendMessage(id, {
             "event": "finishInsertCss",
             "css": css
        }, {
            "frameId": frameId
        })
    except Exception as e:
       logger.error(f"Error inserting CSS {css=}:", e)


genericListener.listeners['updateCss'] = updateCss

def loadOptions(message, sender, sendResponse):
    """
    Отправляет параметры.

    Args:
        message (dict): Объект сообщения.
        sender (object): Объект отправителя сообщения.
        sendResponse (function): Функция для отправки ответа.
     Returns:
         bool: Возвращает True, чтобы сохранить канал связи открытым.
    """
    sendResponse({
        "attributes": attributes,
        "css": css,
        "popupCss": popupCss
    })
    return True

genericListener.listeners['loadOptions'] = loadOptions

def requestSetContentInfo(message, sender):
    """
    Отправляет информацию о контенте.

     Args:
         message (dict): Объект сообщения.
         sender (object): Объект отправителя сообщения.
    """
    browser.tabs.sendMessage(sender.tab.id, {
        "event": "setContentInfo",
        "attributes": attributes
    }, {
        "frameId": sender.frameId
    })

genericListener.listeners['requestSetContentInfo'] = requestSetContentInfo

def handleStorageChange(changes):
    """
    Обрабатывает изменения в хранилище.

    Args:
        changes (dict): Объект, содержащий информацию об изменениях в хранилище.
    """
    global attributes, css, popupCss
    if changes.get("attributes") and "newValue" in changes["attributes"]:
        attributes = changes["attributes"]["newValue"]
    if changes.get("css") and "newValue" in changes["css"]:
        css = changes["css"]["newValue"]
    if changes.get("popupCss") and "newValue" in changes["popupCss"]:
        popupCss = changes["popupCss"]["newValue"]


browser.storage.onChanged.addListener(handleStorageChange)


async def init():
    """
    Инициализирует расширение, загружает параметры и CSS.
    """
    global attributes, popupCss, css
    try:
        items = await browser.storage.sync.get({
            "attributes": attributes,
            "css": None,
            "popupCss": popupCss
        })
        attributes = items["attributes"]
        popupCss = items["popupCss"]
        css = items["css"] if items["css"] is not None else await loadDefaultCss()
    except Exception as e:
        logger.error("Error initializing extension:", e)
init()