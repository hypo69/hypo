# Анализ кода модуля options.js

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Используются функции для переиспользования кода, такие как `isValidAttrName`, `isValidAttrNames`, `isValidStyleLength`, `loadDefaultCss`, `extractBodyStyles`, `createPopupCss`.
    - Присутствуют обработчики событий для кнопок "Сохранить" и "Показать по умолчанию".
    - Код читаем, с понятными именами переменных и функций.
    - Проверка на валидность атрибутов и стилей.
- Минусы
    - Отсутствует обработка ошибок при работе с `browser.storage.sync.set`.
    - Использован `XMLHttpRequest` вместо `fetch`.
    - Нет комментариев в формате reStructuredText.
    - Использование `var` вместо `const` или `let`.
    - Не используются возможности async/await.
    - Отсутствует логирование ошибок.

**Рекомендации по улучшению**
1.  Добавить комментарии в формате reStructuredText для функций и переменных.
2.  Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3.  Использовать `async/await` для асинхронных операций, таких как `browser.runtime.sendMessage` и `browser.storage.sync.set`.
4.  Добавить логирование ошибок с помощью `logger.error`.
5.  Использовать `const` вместо `var` для неизменяемых переменных.
6.  Удалить неиспользуемые переменные, такие как `tx`.
7.  Упростить код `extractBodyStyles`, используя деструктуризацию.
8.  Обработать ошибку в `browser.runtime.sendMessage`.
9.  Добавить обработку ошибок в `browser.storage.sync.set` с использованием `logger.error`.
10. Улучшить читаемость кода, разделив блоки на более мелкие.

**Оптимизированный код**
```python
"""
Модуль для управления настройками расширения TryXPath.
======================================================

Этот модуль предоставляет функциональность для управления атрибутами,
стилями и параметрами всплывающего окна расширения TryXPath.

"""

import json
from src.logger.logger import logger

# alias
#var tx = tryxpath; # Удален неиспользуемый алиас
fu = tryxpath.functions # Сохраняем алиас для функций

document = window.document

#: Словарь атрибутов по умолчанию.
defaultAttributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}

#: Стили всплывающего окна по умолчанию.
defaultPopupBodyStyles = {
    "width": "367px",
    "height": "auto"
}

#: Глобальные переменные для элементов DOM и параметров.
elementAttr = None
contextAttr = None
focusedAttr = None
ancestorAttr = None
frameAttr = None
frameAncestorAttr = None
style = None
popupBodyWidth = None
popupBodyHeight = None
message = None
testElement = None # Перенесено объявление вверх

def isValidAttrName(name: str) -> bool:
    """
    Проверяет, является ли имя атрибута допустимым.

    :param name: Имя атрибута для проверки.
    :return: True, если имя атрибута допустимо, False в противном случае.
    """
    try:
        # Код пытается установить атрибут с заданным именем.
        testElement.setAttribute(name, "testValue")
        return True
    except Exception as e:
        logger.error(f'Недопустимое имя атрибута: {name}', exc_info=True)
        return False

def isValidAttrNames(names: dict) -> bool:
    """
    Проверяет, являются ли все имена атрибутов в словаре допустимыми.

    :param names: Словарь имен атрибутов для проверки.
    :return: True, если все имена атрибутов допустимы, False в противном случае.
    """
    for p in names:
        # Код проверяет каждое имя атрибута на допустимость.
        if not isValidAttrName(names[p]):
            return False
    return True

def isValidStyleLength(length: str) -> bool:
    """
    Проверяет, является ли длина стиля допустимой.

    :param length: Длина стиля для проверки.
    :return: True, если длина стиля допустима, False в противном случае.
    """
    # Код проверяет длину стиля на соответствие формату "auto" или "XXpx".
    return /^auto$|^[1-9]\d*px$/.test(length)

async def loadDefaultCss() -> str:
    """
    Загружает CSS по умолчанию из файла.

    :return: CSS текст.
    """
    try:
        # Код выполняет загрузку css файла
        response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
        return await response.text()
    except Exception as ex:
       logger.error("Ошибка загрузки CSS по умолчанию", exc_info=True)
       return ""


def extractBodyStyles(css: str) -> dict:
    """
    Извлекает стили ширины и высоты из CSS.

    :param css: CSS текст, из которого нужно извлечь стили.
    :return: Словарь со стилями ширины и высоты.
    """
    # Код ищет в css стили ширины и высоты.
    match = /width:(.+?);.*height:(.+?);/.exec(css)
    if match:
        # Код возвращает стили если они найдены.
       return { "width": match[1], "height": match[2] }
    else:
        # Код возвращает пустые стили если стили не найдены.
        return { "width": "", "height": "" }

def createPopupCss(bodyStyles: dict) -> str:
    """
    Создает CSS для всплывающего окна.

    :param bodyStyles: Словарь со стилями ширины и высоты.
    :return: Строка с CSS для всплывающего окна.
    """
    # Код создаёт css для всплывающего окна
    return "body{width:" + bodyStyles["width"] + ";height:" + bodyStyles["height"] + ";}"

async def loadOptions():
    """
    Загружает сохраненные опции и устанавливает значения элементов DOM.
    """
    try:
        # Код отправляет сообщение для получения текущих настроек.
        res = await browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" })

        elementAttr.value = res["attributes"]["element"]
        contextAttr.value = res["attributes"]["context"]
        focusedAttr.value = res["attributes"]["focused"]
        ancestorAttr.value = res["attributes"]["focusedAncestor"]
        frameAttr.value = res["attributes"]["frame"]
        frameAncestorAttr.value = res["attributes"]["frameAncestor"]

        style.value = res["css"]

        bodyStyles = extractBodyStyles(res["popupCss"])
        popupBodyWidth.value = bodyStyles["width"]
        popupBodyHeight.value = bodyStyles["height"]

    except Exception as ex:
        logger.error("Ошибка при загрузке опций", exc_info=True)


async def saveOptions():
    """
    Сохраняет текущие опции в хранилище и отображает сообщение о результате.
    """
    # Код считывает значения из DOM элементов
    styleValue = style.value
    attrs = {}
    attrs["element"] = elementAttr.value
    attrs["context"] = contextAttr.value
    attrs["focused"] = focusedAttr.value
    attrs["focusedAncestor"] = ancestorAttr.value
    attrs["frame"] = frameAttr.value
    attrs["frameAncestor"] = frameAncestorAttr.value
    bodyStyles = {}
    bodyStyles["width"] = popupBodyWidth.value
    bodyStyles["height"] = popupBodyHeight.value

    if not isValidAttrNames(attrs):
        message.textContent = "There is a invalid attribute."
        return

    if not (isValidStyleLength(bodyStyles["width"]) and isValidStyleLength(bodyStyles["height"])):
        message.textContent = "There is a invalid style."
        return

    try:
        # Код сохраняет настройки в хранилище
        await browser.storage.sync.set({
            "attributes": attrs,
            "css": styleValue,
            "popupCss": createPopupCss(bodyStyles)
        })
        message.textContent = "Success. Please click the \"Set style\" button in the popup to apply new options."
    except Exception as err:
        logger.error("Ошибка при сохранении опций", exc_info=True)
        message.textContent = "Failure. " + err.message


async def showDefaultOptions():
    """
    Устанавливает значения по умолчанию для всех опций и обновляет DOM.
    """
    # Код устанавливает значения по умолчанию в DOM
    elementAttr.value = defaultAttributes["element"]
    contextAttr.value = defaultAttributes["context"]
    focusedAttr.value = defaultAttributes["focused"]
    ancestorAttr.value = defaultAttributes["focusedAncestor"]
    frameAttr.value = defaultAttributes["frame"]
    frameAncestorAttr.value = defaultAttributes["frameAncestor"]
    
    try:
        # Код выполняет загрузку дефолтного css
        css = await loadDefaultCss()
        style.value = css
    except Exception as ex:
        logger.error("Ошибка при загрузке дефолтного CSS", exc_info=True)

    popupBodyWidth.value = defaultPopupBodyStyles["width"]
    popupBodyHeight.value = defaultPopupBodyStyles["height"]


window.addEventListener("load", async () => {
    # Код инициализирует DOM элементы
    elementAttr = document.getElementById("element-attribute")
    contextAttr = document.getElementById("context-attribute")
    focusedAttr = document.getElementById("focused-attribute")
    ancestorAttr = document.getElementById("ancestor-attribute")
    frameAttr = document.getElementById("frame-attribute")
    frameAncestorAttr = document.getElementById("frame-ancestor-attribute")
    style = document.getElementById("style")
    popupBodyWidth = document.getElementById("popup-body-width")
    popupBodyHeight = document.getElementById("popup-body-height")
    message = document.getElementById("message")
    testElement = document.createElement("div")

    await loadOptions()

    document.getElementById("save").addEventListener("click", async () => {
        await saveOptions()
    })

    document.getElementById("show-default").addEventListener("click", async () => {
        await showDefaultOptions()
    })
})