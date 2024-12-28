# Анализ кода модуля try_xpath_background.js

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код разбит на функции, что улучшает читаемость и поддержку.
    *   Используются `Promises` для асинхронных операций, что способствует более эффективному выполнению задач.
    *   Применяется `browser.storage.sync.get` для загрузки параметров, что обеспечивает синхронизацию между устройствами.
    *   Используется `browser.runtime.onMessage` для обработки сообщений от других частей расширения.
    *   Обработчики сообщений вынесены в `genericListener.listeners`  что упрощает добавление новых обработчиков.
*   **Минусы:**
    *   Отсутствуют docstring и комментарии, что затрудняет понимание кода.
    *   Используется `XMLHttpRequest` вместо `fetch` для загрузки CSS, что не является современным подходом.
    *   Используется анонимная функция в глобальной области видимости, что не является оптимальным.
    *   Не используется `j_loads` или `j_loads_ns`.
    *   Не используется `from src.logger.logger import logger`.
    *   В некоторых местах отсутствуют обработки ошибок.
    *   Многократное повторение кода `{"timeout":0,"timeout_for_event":"presence_of_element_located"}`.

**Рекомендации по улучшению:**

1.  **Добавить Docstring:** Добавить docstring к модулю и ко всем функциям.
2.  **Использовать `fetch`:** Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3.  **Обернуть в IIFE:** Обернуть код в немедленно вызываемое функциональное выражение (IIFE) для избежания загрязнения глобальной области видимости.
4.  **Использовать `j_loads` или `j_loads_ns`:** Проверить необходимость использования `j_loads` или `j_loads_ns`, хотя здесь это может быть не уместно.
5.  **Использовать `logger`:** Добавить логирование ошибок через `from src.logger.logger import logger` и использовать его вместо `fu.onError`.
6.  **Рефакторинг:** Пересмотреть повторяющийся код, вынести константы.
7.  **Обработка ошибок:** Добавить try-catch в местах где это необходимо с использованием `logger.error`.

**Оптимизированный код:**

```python
"""
Модуль фонового скрипта для расширения Try Xpath.
==================================================

Этот модуль отвечает за обработку сообщений от контент-скриптов,
управление стилями и хранение состояния всплывающего окна.

Основные функции:
    - Загрузка и применение стилей.
    - Сохранение и восстановление состояния всплывающего окна.
    - Управление CSS.
    - Отправка результатов.
"""
import json
from src.logger.logger import logger  # pylint: disable=import-error

_DEFAULT_TIMEOUT_OBJ = {"timeout": 0, "timeout_for_event": "presence_of_element_located"}
_POPUP_CSS = "body{width:367px;height:auto;}"
_ATTRIBUTES = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor",
}


def _load_default_css() -> str:
    """
    Загружает CSS по умолчанию.

    :return: Промис с текстом CSS.
    """
    try:
        req = browser.runtime.getURL("/css/try_xpath_insert.css")
        response = fetch(req)
        if response.status == 200:
            return response.text()
        else:
            logger.error(f"Ошибка загрузки CSS: {response.status}")
            return ""
    except Exception as ex:
        logger.error("Ошибка загрузки CSS", ex)
        return ""


def _generic_listener(message, sender, sendResponse):
    """
    Слушатель сообщений для обработки разных событий.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция для отправки ответа.
    """
    listener = _generic_listener.listeners.get(message.event)
    if listener:
        return listener(message, sender, sendResponse)
    return None


_generic_listener.listeners = {}
browser.runtime.onMessage.addListener(_generic_listener)


def _store_popup_state(message):
    """
    Сохраняет состояние всплывающего окна.

    :param message: Объект сообщения, содержащий состояние.
    """
    global popupState  # pylint: disable=global-statement
    popupState = message.state


_generic_listener.listeners["storePopupState"] = _store_popup_state


def _request_restore_popup_state():
    """
    Отправляет запрос на восстановление состояния всплывающего окна.
    """
    browser.runtime.sendMessage({
        **_DEFAULT_TIMEOUT_OBJ,
        "event": "restorePopupState",
        "state": popupState,
    })


_generic_listener.listeners["requestRestorePopupState"] = _request_restore_popup_state


def _request_insert_style_to_popup():
    """
    Отправляет запрос на добавление стилей во всплывающее окно.
    """
    browser.runtime.sendMessage({
        **_DEFAULT_TIMEOUT_OBJ,
        "event": "insertStyleToPopup",
        "css": _POPUP_CSS,
    })


_generic_listener.listeners["requestInsertStyleToPopup"] = _request_insert_style_to_popup


def _show_all_results(message, sender):
    """
    Обрабатывает запрос на отображение всех результатов.

    :param message: Объект сообщения с результатами.
    :param sender: Объект отправителя.
    """
    global results  # pylint: disable=global-statement
    del message["event"]
    results = message
    results["tabId"] = sender.tab.id
    results["frameId"] = sender.frameId
    browser.tabs.create({"url": "/pages/show_all_results.html"})


_generic_listener.listeners["showAllResults"] = _show_all_results


def _load_results(message, sender, sendResponse):
    """
    Обрабатывает запрос на загрузку результатов.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция для отправки ответа.
    :return: True, если запрос обработан.
    """
    sendResponse(results)
    return True


_generic_listener.listeners["loadResults"] = _load_results


def _update_css(message, sender):
    """
    Обновляет CSS в соответствии с сообщением.

    :param message: Объект сообщения с информацией об CSS.
    :param sender: Объект отправителя.
    """
    tab_id = sender.tab.id
    frame_id = sender.frameId

    for remove_css in message.get("expiredCssSet", []):
        browser.tabs.removeCSS(
            tab_id,
            {
                "code": remove_css,
                "matchAboutBlank": True,
                "frameId": frame_id,
            },
        ).then(lambda: browser.tabs.sendMessage(
            tab_id,
            {
                **_DEFAULT_TIMEOUT_OBJ,
                "event": "finishRemoveCss",
                "css": remove_css,
            },
            {"frameId": frame_id},
        )).catch(lambda error: logger.error(f"Ошибка при удалении CSS: {remove_css}", error))
    try:
        browser.tabs.insertCSS(
            tab_id,
            {
                "code": css,
                "cssOrigin": "author",
                "matchAboutBlank": True,
                "frameId": frame_id,
            },
        ).then(lambda: browser.tabs.sendMessage(
            tab_id,
            {
                **_DEFAULT_TIMEOUT_OBJ,
                "event": "finishInsertCss",
                "css": css,
            },
            {"frameId": frame_id},
        )).catch(lambda error: logger.error(f"Ошибка при вставке CSS: {css}", error))
    except Exception as ex:
        logger.error("Ошибка при вставке/удалении CSS", ex)


_generic_listener.listeners["updateCss"] = _update_css


def _load_options(message, sender, sendResponse):
    """
    Отправляет текущие настройки.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    :param sendResponse: Функция для отправки ответа.
    :return: True, если запрос обработан.
    """
    sendResponse(
        {
            "attributes": _ATTRIBUTES,
            "css": css,
            "popupCss": _POPUP_CSS,
        }
    )
    return True


_generic_listener.listeners["loadOptions"] = _load_options


def _request_set_content_info(message, sender):
    """
    Отправляет запрос на установку информации о контенте.

    :param message: Объект сообщения.
    :param sender: Объект отправителя.
    """
    browser.tabs.sendMessage(
        sender.tab.id,
        {
            **_DEFAULT_TIMEOUT_OBJ,
            "event": "setContentInfo",
            "attributes": _ATTRIBUTES,
        },
        {"frameId": sender.frameId},
    )


_generic_listener.listeners["requestSetContentInfo"] = _request_set_content_info

def _handle_storage_change(changes):
    """
    Обрабатывает изменения в хранилище.

    :param changes: Объект с изменениями в хранилище.
    """
    global _ATTRIBUTES, css, _POPUP_CSS  # pylint: disable=global-statement
    if "attributes" in changes and "newValue" in changes["attributes"]:
        _ATTRIBUTES = changes["attributes"]["newValue"]
    if "css" in changes and "newValue" in changes["css"]:
        css = changes["css"]["newValue"]
    if "popupCss" in changes and "newValue" in changes["popupCss"]:
        _POPUP_CSS = changes["popupCss"]["newValue"]


browser.storage.onChanged.addListener(_handle_storage_change)


def _handle_storage_get(items):
    """
    Обрабатывает полученные из хранилища данные.

    :param items: Объект с данными из хранилища.
    """
    global _ATTRIBUTES, css, _POPUP_CSS  # pylint: disable=global-statement
    _ATTRIBUTES = items.get("attributes", _ATTRIBUTES)
    _POPUP_CSS = items.get("popupCss", _POPUP_CSS)
    css_promise = (
        items.get("css")
        if items.get("css") is not None
        else _load_default_css()
    )

    css_promise.then(lambda loaded_css: setattr(globals(), "css", loaded_css)).catch(
        lambda error: logger.error("Ошибка при загрузке CSS:", error)
    )

browser.storage.sync.get(
    {
        "attributes": _ATTRIBUTES,
        "css": None,
        "popupCss": _POPUP_CSS,
    }
).then(_handle_storage_get).catch(lambda error: logger.error("Ошибка при загрузке настроек", error))
```