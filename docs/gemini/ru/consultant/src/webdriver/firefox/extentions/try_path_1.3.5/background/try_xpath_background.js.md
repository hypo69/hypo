# Анализ кода модуля `try_xpath_background.js`

**Качество кода**
8
-  Плюсы
    - Код разбит на логические блоки, что облегчает его понимание.
    - Используются асинхронные операции, что хорошо для неблокирующего выполнения.
    - Присутствует обработка ошибок с использованием `catch(fu.onError)`.
    - Код использует `browser.storage.onChanged` для прослушивания изменений в хранилище, что позволяет динамически обновлять параметры.
-  Минусы
    - Отсутствуют docstring для функций и модуля, что затрудняет понимание назначения кода без его детального изучения.
    - Код содержит магические строки типа `presence_of_element_located` в сообщениях, что снижает читаемость и усложняет модификацию.
    - Многократное использование конструкции `{"timeout":0,"timeout_for_event":"presence_of_element_located","event": ...}` может быть заменено на константу.
    - Использование `XMLHttpRequest` для загрузки CSS может быть заменено на более современный `fetch`.
    - `Object.create(null)` для создания `genericListener.listeners` может быть заменено на более читаемый `{}`, если прототип не важен.

**Рекомендации по улучшению**

1.  Добавить docstring к модулю, функциям и переменным в формате reStructuredText (RST), чтобы улучшить читаемость и документированность кода.
2.  Заменить магические строки `presence_of_element_located` на константу для улучшения читаемости и упрощения поддержки.
3.  Использовать `fetch` вместо `XMLHttpRequest` для загрузки CSS, так как это более современный подход.
4.  Заменить `Object.create(null)` на `{}` для создания `genericListener.listeners`, если прототип не требуется.
5.  Внедрить более явную обработку ошибок с использованием `logger.error` и избегать избыточного `try-except` в обработчиках сообщений.
6.  Улучшить именование переменных, сделав его более описательным.
7.  Обеспечить консистентное использование промисов и `async/await`, где это уместно.
8.   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для фоновой обработки расширения try_xpath
==================================================

Этот модуль содержит функции для обработки сообщений от контентных скриптов,
загрузки CSS, управления состоянием всплывающего окна и хранения опций расширения.
Он также прослушивает изменения в хранилище и динамически обновляет параметры.

Пример использования
--------------------

Пример обработки сообщения от контентного скрипта:

.. code-block:: javascript

   browser.runtime.sendMessage({"event": "showAllResults", "results": {...}});

"""
import json

from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

# Alias для упрощения доступа
tx = tryxpath
fu = tryxpath.functions

#: Состояние всплывающего окна.
popupState = None

#: CSS для всплывающего окна.
popupCss = "body{width:367px;height:auto;}"

#: Результаты, полученные от контентного скрипта.
results = {}

#: CSS, применяемый к странице.
css = ""

#: Атрибуты, используемые для идентификации элементов.
attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}

#: Константа для таймаута и события 'presence_of_element_located'.
MESSAGE_OPTIONS = {"timeout": 0, "timeout_for_event": "presence_of_element_located"}


async def load_default_css() -> str:
    """
    Загружает CSS по умолчанию из файла.

    :return: CSS текст.
    :raises: Exception: В случае ошибки загрузки CSS.
    """
    try:
        response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
        return await response.text()
    except Exception as ex:
        logger.error(f"Ошибка при загрузке CSS: {ex}")
        raise

def generic_listener(message: dict, sender: dict, sendResponse: callable) -> bool:
    """
    Общий обработчик сообщений.

    Вызывает соответствующий обработчик на основе события в сообщении.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция обратного вызова для отправки ответа.
    :return: True, если сообщение было обработано.
    """
    listener = generic_listener.listeners.get(message.get("event"))
    if listener:
        return listener(message, sender, sendResponse)
    return False

generic_listener.listeners = {}

browser.runtime.onMessage.addListener(generic_listener)


def store_popup_state(message: dict) -> None:
    """
    Сохраняет состояние всплывающего окна.

    :param message: Объект сообщения, содержащий состояние всплывающего окна.
    """
    global popupState
    popupState = message.get("state")


generic_listener.listeners["storePopupState"] = store_popup_state


def request_restore_popup_state(message: dict) -> None:
    """
    Отправляет запрос на восстановление состояния всплывающего окна.

    :param message: Объект сообщения.
    """
    browser.runtime.sendMessage({
        **MESSAGE_OPTIONS,
        "event": "restorePopupState",
        "state": popupState
    })


generic_listener.listeners["requestRestorePopupState"] = request_restore_popup_state


def request_insert_style_to_popup() -> None:
    """
    Отправляет запрос на вставку CSS в всплывающее окно.
    """
    browser.runtime.sendMessage({
        **MESSAGE_OPTIONS,
        "event": "insertStyleToPopup",
        "css": popupCss
    })


generic_listener.listeners["requestInsertStyleToPopup"] = request_insert_style_to_popup


def show_all_results(message: dict, sender: dict) -> None:
    """
    Сохраняет результаты и открывает страницу для отображения всех результатов.

    :param message: Объект сообщения, содержащий результаты.
    :param sender: Объект отправителя.
    """
    global results
    del message["event"]
    results = message
    results["tabId"] = sender["tab"]["id"]
    results["frameId"] = sender["frameId"]
    browser.tabs.create({"url": "/pages/show_all_results.html"})


generic_listener.listeners["showAllResults"] = show_all_results


def load_results(message: dict, sender: dict, sendResponse: callable) -> bool:
    """
    Отправляет сохраненные результаты обратно отправителю.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция обратного вызова для отправки ответа.
    :return: True, если результаты отправлены.
    """
    sendResponse(results)
    return True


generic_listener.listeners["loadResults"] = load_results


async def update_css(message: dict, sender: dict) -> None:
    """
    Обновляет CSS на странице.

    Удаляет устаревший CSS и вставляет новый.

    :param message: Объект сообщения, содержащий набор устаревшего CSS.
    :param sender: Объект отправителя.
    """
    id = sender["tab"]["id"]
    frameId = sender["frameId"]
    expired_css_set = message.get("expiredCssSet", [])
    for remove_css in expired_css_set:
        try:
            await browser.tabs.removeCSS(id, {
                "code": remove_css,
                "matchAboutBlank": True,
                "frameId": frameId
            })
            await browser.tabs.sendMessage(id, {
                **MESSAGE_OPTIONS,
                "event": "finishRemoveCss",
                "css": remove_css
            }, {"frameId": frameId})
        except Exception as ex:
            logger.error(f"Ошибка при удалении CSS: {ex}")
    try:
         await browser.tabs.insertCSS(id, {
            "code": css,
            "cssOrigin": "author",
            "matchAboutBlank": True,
            "frameId": frameId
         })
         await browser.tabs.sendMessage(id, {
                **MESSAGE_OPTIONS,
                "event": "finishInsertCss",
                "css": css
          }, {"frameId": frameId})
    except Exception as ex:
         logger.error(f"Ошибка при вставке CSS: {ex}")

generic_listener.listeners["updateCss"] = update_css


def load_options(message: dict, sender: dict, sendResponse: callable) -> bool:
    """
    Отправляет опции расширения отправителю.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция обратного вызова для отправки ответа.
    :return: True, если опции отправлены.
    """
    sendResponse({
        "attributes": attributes,
        "css": css,
        "popupCss": popupCss
    })
    return True


generic_listener.listeners["loadOptions"] = load_options


def request_set_content_info(message: dict, sender: dict) -> None:
    """
    Отправляет запрос на установку информации о контенте.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    """
    browser.tabs.sendMessage(sender["tab"]["id"], {
        **MESSAGE_OPTIONS,
        "event": "setContentInfo",
        "attributes": attributes
    }, {"frameId": sender["frameId"]})


generic_listener.listeners["requestSetContentInfo"] = request_set_content_info


def handle_storage_change(changes: dict, area: str) -> None:
    """
    Обрабатывает изменения в хранилище.

    Обновляет соответствующие переменные при изменении.

    :param changes: Объект изменений в хранилище.
    :param area: Область хранилища.
    """
    global attributes, css, popupCss
    if "attributes" in changes and "newValue" in changes["attributes"]:
        attributes = changes["attributes"]["newValue"]
    if "css" in changes and "newValue" in changes["css"]:
        css = changes["css"]["newValue"]
    if "popupCss" in changes and "newValue" in changes["popupCss"]:
        popupCss = changes["popupCss"]["newValue"]


browser.storage.onChanged.addListener(handle_storage_change)


async def load_initial_data() -> None:
    """
    Загружает начальные данные из хранилища.
    """
    global attributes, css, popupCss
    items = await browser.storage.sync.get({
        "attributes": attributes,
        "css": None,
        "popupCss": popupCss
    })
    attributes = items["attributes"]
    popupCss = items["popupCss"]
    if items["css"] is not None:
        css = items["css"]
    else:
        css = await load_default_css()


load_initial_data().catch(fu.onError)
```