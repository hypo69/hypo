# Анализ кода модуля try_xpath_content.js

**Качество кода**
7
- Плюсы
    - Код разбит на функции, что упрощает его понимание и поддержку.
    - Используется `Map` для хранения данных, что более эффективно, чем использование объектов.
    - Присутствует обработка ошибок.
    - Есть механизм для предотвращения многократного выполнения кода.
- Минусы
    - Код не документирован.
    - Отсутствуют проверки типов для аргументов функций.
    - Некоторые блоки `try-catch` можно заменить на более конкретную обработку ошибок.
    - Присутствуют магические строки, которые можно вынести в константы.
    - Не все переменные и функции имеют понятные имена.
    - Присутствует дублирование кода, например, при создании `sendMsg`.

**Рекомендации по улучшению**

1.  **Документирование**: Добавить docstring к модулю и каждой функции.
2.  **Импорты**: Добавить необходимые импорты, если они нужны.
3.  **Типизация**: Добавить аннотации типов, где это необходимо.
4.  **Обработка ошибок**: Использовать `logger.error` вместо `try-except`, где это возможно.
5.  **Рефакторинг**: Вынести повторяющиеся фрагменты кода в отдельные функции.
6.  **Именование**: Использовать более понятные имена для переменных и функций.
7. **Константы**: Вынести магические строки в константы.
8. **Улучшение обработки сообщений**: Добавить обработку сообщений с использованием `match-case` (если это применимо) для улучшения читаемости и структуры.

**Оптимизированный код**

```python
"""
Модуль try_xpath_content.js для расширения Firefox, предоставляющий функциональность для работы с XPath и CSS.
===========================================================================================================

Этот модуль включает в себя функции для выполнения XPath запросов, управления стилями CSS,
а также для обработки сообщений от расширения.

Модуль обрабатывает события фокуса, изменения CSS и предоставляет функционал для
визуализации результатов XPath запросов на веб-странице.

"""
from src.logger.logger import logger # Импортируем logger
import json
from typing import Any
from pathlib import Path

# Объявляем константы
STYLE_ELEMENT_HEADER = "/* This style element was inserted by browser add-on, Try xpath." \
                      " If you want to remove this element, please click the reset" \
                      " style button in the popup. */\\n"
DUMMY_ITEM = ""
DUMMY_ITEMS = []
INVALID_EXECUTION_ID = float('NaN')
MESSAGE_TRYXPATH_FOCUS_FRAME = "tryxpath-focus-frame"
MESSAGE_TRYXPATH_REQUEST_TO_POPUP = "tryxpath-request-message-to-popup"
MESSAGE_SHOW_RESULTS_IN_POPUP = "showResultsInPopup"
MESSAGE_SHOW_ALL_RESULTS = "showAllResults"
MESSAGE_ERROR_OCCURRED_FRAME = "An error occurred when getting a frame. "
MESSAGE_ERROR_OCCURRED_FOCUS_FRAME = "An error occurred when focusing a frame. "
MESSAGE_CONTEXT_NOT_FOUND = "A context is not found."
MESSAGE_SUCCESS = "Success."
MESSAGE_ERROR_OCCURRED_NODES = "An error occurred when getting nodes. "
MESSAGE_NO_RESULT = "There is no result."


#   alias
#   Сохраняем ссылку на объект tryxpath для удобства
tx = tryxpath
#   Сохраняем ссылку на объект functions для удобства
fu = tryxpath.functions


# prevent multiple execution
# Проверяем, был ли уже загружен контент, и выходим, если это так
if tx.isContentLoaded:
    #  если контент уже загружен, то выходим
    return
#  Устанавливаем флаг, что контент загружен
tx.isContentLoaded = True


#  Объявляем переменные и константы
attributes = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}

prevMsg = None
executionCount = 0
inBlankWindow = False
currentDocument = None
contextItem = DUMMY_ITEM
currentItems = DUMMY_ITEMS
focusedItem = DUMMY_ITEM
focusedAncestorItems = DUMMY_ITEMS
currentCss = None
insertedStyleElements = {}
expiredCssSet = {}
originalAttributes = {}

def setAttr(attr: str, value: str, item: Any) -> None:
    """
    Устанавливает атрибут элементу, сохраняя его предыдущее значение.

    Args:
        attr (str): Название атрибута.
        value (str): Значение атрибута.
        item (Any): Элемент, которому нужно установить атрибут.
    """
    fu.saveAttrForItem(item, attr, originalAttributes)
    fu.setAttrToItem(attr, value, item)

def setIndex(attr: str, items: list[Any]) -> None:
    """
    Устанавливает индекс атрибута для элементов.

    Args:
        attr (str): Название атрибута.
        items (list[Any]): Список элементов.
    """
    fu.saveAttrForItems(items, attr, originalAttributes)
    fu.setIndexToItems(attr, items)


def isFocusable(item: Any) -> bool:
    """
    Проверяет, является ли элемент фокусируемым.

    Args:
        item (Any): Элемент для проверки.

    Returns:
        bool: True, если элемент фокусируемый, иначе False.
    """
    if not item:
        return False
    if fu.isNodeItem(item) or fu.isAttrItem(item):
        return True
    return False

def focusItem(item: Any) -> None:
    """
    Фокусирует на элементе, устанавливая соответствующие атрибуты.

    Args:
        item (Any): Элемент для фокусировки.
    """
    fu.removeAttrFromItem(attributes.get("focused"), focusedItem)
    fu.removeAttrFromItems(attributes.get("focusedAncestor"), focusedAncestorItems)

    if not isFocusable(item):
        return

    if fu.isElementItem(item):
        focusedItem = item
    else:
        focusedItem = fu.getParentElement(item)

    focusedAncestorItems = fu.getAncestorElements(focusedItem)

    setAttr(attributes.get("focused"), "true", focusedItem)
    setIndex(attributes.get("focusedAncestor"), focusedAncestorItems)

    focusedItem.blur()
    focusedItem.focus()
    focusedItem.scrollIntoView()

def setMainAttrs() -> None:
    """
    Устанавливает основные атрибуты для контекстного элемента и текущих элементов.
    """
    if contextItem is not DUMMY_ITEM:
        setAttr(attributes.get("context"), "true", contextItem)
    setIndex(attributes.get("element"), currentItems)

def restoreAttrs() -> None:
    """
    Восстанавливает оригинальные атрибуты элементов.
    """
    fu.restoreItemAttrs(originalAttributes)
    originalAttributes = {}

def resetPrev() -> None:
    """
    Сбрасывает предыдущие значения и создает сообщение с результатом.
    """
    restoreAttrs()
    global contextItem
    contextItem = DUMMY_ITEM
    global currentItems
    currentItems = DUMMY_ITEMS
    global focusedItem
    focusedItem = DUMMY_ITEM
    global focusedAncestorItems
    focusedAncestorItems = DUMMY_ITEMS
    global prevMsg
    prevMsg = createResultMessage()
    global executionCount
    executionCount += 1

def makeTypeStr(resultType: int | str) -> str:
    """
    Создает строковое представление типа результата.

    Args:
        resultType (int | str): Тип результата.

    Returns:
        str: Строковое представление типа.
    """
    if isinstance(resultType, int) and (resultType == resultType):
        return f"{fu.getxpathResultStr(resultType)}({resultType})"
    return ""


def updateCss() -> None:
    """
     Отправляет сообщение для обновления CSS, если есть изменения.
    """
    if (currentCss is None) or (len(expiredCssSet) > 0):
        browser.runtime.sendMessage({
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
            "expiredCssSet": expiredCssSet
        })

def getFrames(spec: str) -> list[Any]:
    """
    Получает список фреймов на основе спецификации.

    Args:
        spec (str): Спецификация фреймов в формате JSON.

    Returns:
        list[Any]: Список фреймов.

    Raises:
        Error: Если спецификация не валидна.
    """
    try:
        inds = json.loads(spec)
        if fu.isNumberArray(inds) and (len(inds) > 0):
            return fu.getFrameAncestry(inds).reverse()
        else:
            raise ValueError(f"Invalid specification. [{spec}]")
    except Exception as e:
        logger.error(f'Ошибка при получении фреймов {e}')
        raise

def parseFrameDesignation(frameDesi: str) -> list[int]:
    """
    Парсит обозначение фрейма.

    Args:
        frameDesi (str): Обозначение фрейма в формате JSON.

    Returns:
        list[int]: Список индексов фреймов.

     Raises:
        Error: Если обозначение фрейма не валидно.
    """
    try:
        inds = json.loads(frameDesi)
        if fu.isNumberArray(inds) and (len(inds) > 0):
            return inds
        else:
            raise ValueError(f"Invalid specification. [{frameDesi}]")
    except Exception as e:
         logger.error(f'Ошибка при парсинге обозначения фрейма {e}')
         raise

def traceBlankWindows(desi: list[int], win: Any = None) -> dict[str, Any]:
    """
    Отслеживает пустые окна на основе обозначения.

    Args:
        desi (list[int]): Список индексов фреймов.
        win (Any, optional): Окно для начала отслеживания. По умолчанию текущее окно.

    Returns:
        dict[str, Any]: Результат отслеживания. Содержит список окон, флаг успеха
         и окно, где произошла ошибка (если есть).
    """
    win = win or window
    result = {"windows": [], "failedWindow": None, "success": True}
    try:
        for frameInd in desi:
            if (frameInd <= -1) or (frameInd >= len(win.frames)):
                result["failedWindow"] = None
                result["success"] = False
                return result

            win = win.frames[frameInd]
            if not fu.isBlankWindow(win):
                result["failedWindow"] = win
                result["success"] = False
                return result
            result["windows"].append(win)
    except Exception as e:
          logger.error(f'Ошибка при отслеживании пустых окон {e}')
          result["failedWindow"] = None
          result["success"] = False
    return result


def handleCssChange(newCss: str) -> None:
    """
    Обрабатывает изменение CSS.

    Args:
        newCss (str): Новый CSS.
    """
    global currentCss
    if currentCss is None:
        if newCss in expiredCssSet:
            currentCss = newCss
            del expiredCssSet[newCss]
    elif newCss != currentCss:
        if newCss in expiredCssSet:
            currentCss = newCss
            del expiredCssSet[newCss]
        else:
            expiredCssSet[currentCss] = True
            currentCss = None
    # If newCss and currentCss are the same string do nothing.


def findFrameByMessage(event: Any, win: Any) -> Any:
    """
    Находит фрейм по сообщению.

    Args:
        event (Any): Событие сообщения.
        win (Any): Окно, в котором искать фрейм.

    Returns:
        Any: Найденный фрейм.
    """
    ind = event.data.get("frameIndex")
    if ind >= 0:
        subWin = win.frames[ind]
    else:
        subWin = event.source
    return fu.findFrameElement(subWin, win)


def setFocusFrameListener(win: Any, isBlankWindow: bool) -> None:
    """
    Устанавливает слушатель сообщений для фокуса фрейма.

    Args:
        win (Any): Окно, для которого устанавливается слушатель.
        isBlankWindow (bool): Флаг, указывающий, является ли окно пустым.
    """
    if isBlankWindow:
        localUpdateCss = updateStyleElement.bind(None, win.document)
    else:
        localUpdateCss = updateCss

    win.addEventListener("message", (event) => {
        data = event.data
        if data and data.get("message") == MESSAGE_TRYXPATH_FOCUS_FRAME and isinstance(data.get("index"), int) and isinstance(data.get("frameIndex"), int):
            frame = findFrameByMessage(event, win)
            if not frame:
                return
            index = data.get("index")
            localUpdateCss()
            setAttr(attributes.get("frame"), index, frame)
            setIndex(attributes.get("frameAncestor"), fu.getAncestorElements(frame))
            if win == win.top:
                frame.blur()
                frame.focus()
                frame.scrollIntoView()
            else:
                win.parent.postMessage({
                    "message": MESSAGE_TRYXPATH_FOCUS_FRAME,
                    "index": index + 1,
                    "frameIndex": fu.findFrameIndex(win, win.parent)
                }, "*")
    })

def initBlankWindow(win: Any) -> None:
    """
    Инициализирует пустое окно.

    Args:
        win (Any): Пустое окно для инициализации.
    """
    if not win.tryxpath:
        win.tryxpath = {}

    if win.tryxpath.get("isInitialized"):
        return
    win.tryxpath["isInitialized"] = True
    setFocusFrameListener(win, True)

def findStyleParent(doc: Any) -> Any:
    """
    Находит родительский элемент для стилей.

    Args:
        doc (Any): Документ, в котором искать родителя.

    Returns:
        Any: Родительский элемент (head или body).
    """
    return doc.head or doc.body or None

def updateStyleElement(doc: Any) -> None:
    """
    Обновляет или создает элемент стиля в документе.

    Args:
        doc (Any): Документ, в котором нужно обновить стили.
    """
    css = currentCss or ""
    css = STYLE_ELEMENT_HEADER + css

    style = insertedStyleElements.get(doc)
    if style:
        style.textContent = css
        return

    parent = findStyleParent(doc)
    if parent:
        newStyle = doc.createElement("style")
        newStyle.textContent = css
        newStyle.setAttribute("type", "text/css")
        parent.appendChild(newStyle)
        insertedStyleElements[doc] = newStyle

def updateAllStyleElements() -> None:
    """
    Обновляет все элементы стиля.
    """
    css = currentCss or ""
    css = STYLE_ELEMENT_HEADER + css
    for doc, elem in insertedStyleElements.items():
        elem.textContent = css

def removeStyleElement(doc: Any) -> None:
    """
    Удаляет элемент стиля из документа.

    Args:
        doc (Any): Документ, из которого нужно удалить стиль.
    """
    elem = insertedStyleElements.get(doc)
    if not elem:
        return

    parent = elem.parentNode
    if parent:
        parent.removeChild(elem)
    del insertedStyleElements[doc]

def removeAllStyleElements() -> None:
    """
    Удаляет все элементы стиля.
    """
    for doc, elem in insertedStyleElements.items():
        parent = elem.parentNode
        if parent:
            parent.removeChild(elem)
    insertedStyleElements.clear()

def createResultMessage() -> dict[str, Any]:
    """
    Создает базовое сообщение с результатом.

    Returns:
        dict[str, Any]: Сообщение с базовыми данными.
    """
    return {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": MESSAGE_SHOW_RESULTS_IN_POPUP,
        "executionId": INVALID_EXECUTION_ID,
        "href": "",
        "title": "",
        "message": MESSAGE_NO_RESULT,
        "main": {
            "method": "evaluate",
            "expression": "",
            "specifiedResultType": "ANY_TYPE(0)",
            "resolver": "",
            "itemDetails": []
        }
    }


def genericListener(message: Any, sender: Any, sendResponse: Any) -> Any:
    """
    Общий слушатель сообщений.

    Args:
        message (Any): Сообщение.
        sender (Any): Отправитель сообщения.
        sendResponse (Any): Функция для отправки ответа.
    """
    listener = genericListener.listeners.get(message.get("event"))
    if listener:
        return listener(message, sender, sendResponse)

genericListener.listeners = {}
browser.runtime.onMessage.addListener(genericListener)

def setContentInfo(message: Any) -> None:
    """
    Устанавливает информацию о контенте.

    Args:
         message (Any): Сообщение с информацией о контенте.
    """
    if not message:
        return
    global attributes
    if "attributes" in message:
        attributes = message.get("attributes")

genericListener.listeners["setContentInfo"] = setContentInfo


def execute(message: Any, sender: Any) -> None:
    """
    Выполняет XPath запрос и отправляет результат.

    Args:
        message (Any): Сообщение с запросом.
        sender (Any): Отправитель сообщения.
    """
    resetPrev()
    updateCss()

    sendMsg = createResultMessage()
    main = message.get("main")
    sendMsg["event"] = MESSAGE_SHOW_RESULTS_IN_POPUP
    sendMsg["executionId"] = executionCount
    sendMsg["href"] = window.location.href
    sendMsg["title"] = window.document.title
    sendMsg["frameDesignation"] = ""

    mainType = fu.getxpathResultNum(main.get("resultType"))
    sendMsg["main"]["method"] = main.get("method")
    sendMsg["main"]["expression"] = main.get("expression")
    sendMsg["main"]["specifiedResultType"] = makeTypeStr(mainType)
    sendMsg["main"]["resultType"] = ""
    sendMsg["main"]["resolver"] = main.get("resolver") or ""
    sendMsg["main"]["itemDetails"] = []

    global contextItem
    contextItem = document
    global currentDocument
    currentDocument = document

    if "frameDesignation" in message:
        sendMsg["frameDesignation"] = message.get("frameDesignation")
        try:
            desi = parseFrameDesignation(message.get("frameDesignation"))
            res = traceBlankWindows(desi, window)
            if not res.get("success"):
                if res.get("failedWindow") is None:
                     raise ValueError("The specified frame does not exist.")
                else:
                    res.get("failedWindow").postMessage({
                        "message": MESSAGE_TRYXPATH_REQUEST_TO_POPUP,
                        "messageId": 1
                    }, "*")
                    return
            global inBlankWindow
            contextItem = res.get("windows").pop().document
        except Exception as e:
            sendMsg["message"] = MESSAGE_ERROR_OCCURRED_FRAME + str(e)
            browser.runtime.sendMessage(sendMsg)
            global prevMsg
            prevMsg = sendMsg
            return
        inBlankWindow = True
        currentDocument = contextItem

    if inBlankWindow:
        removeStyleElement(currentDocument)

    if message.get("context"):
        cont = message.get("context")
        contType = fu.getxpathResultNum(cont.get("resultType"))
        sendMsg["context"] = {}
        sendMsg["context"]["method"] = cont.get("method")
        sendMsg["context"]["expression"] = cont.get("expression")
        sendMsg["context"]["specifiedResultType"] = makeTypeStr(contType)
        sendMsg["context"]["resolver"] = cont.get("resolver") or ""
        sendMsg["context"]["itemDetail"] = None

        try:
            contRes = fu.execExpr(cont.get("expression"), cont.get("method"), {
                "context": contextItem,
                "resultType": contType,
                "resolver": cont.get("resolver")
            })
        except Exception as e:
             sendMsg["message"] = "An error occurred when getting a context. " + str(e)
             browser.runtime.sendMessage(sendMsg)
             prevMsg = sendMsg
             return
        if len(contRes.get("items")) == 0:
            sendMsg["message"] = MESSAGE_CONTEXT_NOT_FOUND
            browser.runtime.sendMessage(sendMsg)
            prevMsg = sendMsg
            return

        contextItem = contRes.get("items")[0]
        sendMsg["context"]["resultType"] = makeTypeStr(contRes.get("resultType"))
        sendMsg["context"]["itemDetail"] = fu.getItemDetail(contextItem)

    try:
        mainRes = fu.execExpr(main.get("expression"), main.get("method"), {
            "context": contextItem,
            "resultType": mainType,
            "resolver": main.get("resolver")
        })
    except Exception as e:
        sendMsg["message"] = MESSAGE_ERROR_OCCURRED_NODES + str(e)
        browser.runtime.sendMessage(sendMsg)
        prevMsg = sendMsg
        return
    global currentItems
    currentItems = mainRes.get("items")
    sendMsg["message"] = MESSAGE_SUCCESS
    sendMsg["main"]["resultType"] = makeTypeStr(mainRes.get("resultType"))
    sendMsg["main"]["itemDetails"] = fu.getItemDetails(currentItems)
    browser.runtime.sendMessage(sendMsg)
    prevMsg = sendMsg
    setMainAttrs()
    if inBlankWindow:
        updateStyleElement(currentDocument)

genericListener.listeners["execute"] = execute

def focusItemListener(message: Any) -> None:
    """
    Фокусирует на элементе из списка результатов.

    Args:
        message (Any): Сообщение с индексом элемента для фокуса.
    """
    if message.get("executionId") == executionCount:
        if inBlankWindow:
            updateStyleElement(currentDocument)
        focusItem(currentItems[message.get("index")])

genericListener.listeners["focusItem"] = focusItemListener

def focusContextItemListener(message: Any) -> None:
    """
    Фокусирует на контекстном элементе.

    Args:
         message (Any): Сообщение для фокуса на контекстном элементе.
    """
    if message.get("executionId") == executionCount:
         if inBlankWindow:
             updateStyleElement(currentDocument)
         focusItem(contextItem)

genericListener.listeners["focusContextItem"] = focusContextItemListener

def focusFrameListener(message: Any) -> None:
    """
    Фокусирует на фрейме.

    Args:
         message (Any): Сообщение с информацией о фрейме для фокуса.
    """
    win = window

    if "frameDesignation" in message:
        try:
            desi = parseFrameDesignation(message.get("frameDesignation"))
            res = traceBlankWindows(desi, window)
            if not res.get("success"):
                 if res.get("failedWindow") is None:
                     raise ValueError("The specified frame does not exist.")
                 else:
                    res.get("failedWindow").postMessage({
                        "message": MESSAGE_TRYXPATH_REQUEST_TO_POPUP,
                        "messageId": 1
                    }, "*")
                    return
            win = res.get("windows").pop()
        except Exception as e:
             sendMsg = createResultMessage()
             sendMsg["message"] = MESSAGE_ERROR_OCCURRED_FOCUS_FRAME + str(e)
             browser.runtime.sendMessage(sendMsg)
             return

    if win != win.top:
        win.parent.postMessage({
            "message": MESSAGE_TRYXPATH_FOCUS_FRAME,
            "index": 0,
            "frameIndex": fu.findFrameIndex(win, win.parent)
        }, "*")

genericListener.listeners["focusFrame"] = focusFrameListener

def requestShowResultsInPopup() -> None:
    """
    Отправляет запрос на отображение результатов в попапе.
    """
    if prevMsg:
        prevMsg["event"] = MESSAGE_SHOW_RESULTS_IN_POPUP
        browser.runtime.sendMessage(prevMsg)

genericListener.listeners["requestShowResultsInPopup"] = requestShowResultsInPopup

def requestShowAllResults() -> None:
    """
    Отправляет запрос на отображение всех результатов.
    """
    if prevMsg:
        prevMsg["event"] = MESSAGE_SHOW_ALL_RESULTS
        browser.runtime.sendMessage(prevMsg)

genericListener.listeners["requestShowAllResults"] = requestShowAllResults

def resetStyle() -> None:
    """
    Сбрасывает стили.
    """
    restoreAttrs()
    removeAllStyleElements()

genericListener.listeners["resetStyle"] = resetStyle

def setStyle() -> None:
    """
    Устанавливает стили.
    """
    restoreAttrs()
    updateCss()
    if inBlankWindow:
        updateStyleElement(currentDocument)
    setMainAttrs()

genericListener.listeners["setStyle"] = setStyle

def finishInsertCss(message: Any) -> None:
    """
    Завершает вставку CSS.

    Args:
        message (Any): Сообщение с CSS для вставки.
    """
    css = message.get("css")
    global currentCss
    currentCss = css
    if css in expiredCssSet:
        del expiredCssSet[css]
    updateAllStyleElements()

genericListener.listeners["finishInsertCss"] = finishInsertCss

def finishRemoveCss(message: Any) -> None:
    """
    Завершает удаление CSS.

    Args:
         message (Any): Сообщение с CSS для удаления.
    """
    css = message.get("css")
    global currentCss
    if css == currentCss:
        currentCss = None
    if css in expiredCssSet:
        del expiredCssSet[css]
genericListener.listeners["finishRemoveCss"] = finishRemoveCss

def storageOnChanged(changes: dict) -> None:
     """
    Обрабатывает изменения в хранилище.

    Args:
       changes (dict): Изменения в хранилище.
    """
     if changes.get("attributes") and ("newValue" in changes.get("attributes")):
         global attributes
         attributes = changes.get("attributes").get("newValue")
     if changes.get("css") and ("newValue" in changes.get("css")):
         handleCssChange(changes.get("css").get("newValue"))
browser.storage.onChanged.addListener(storageOnChanged)


window.addEventListener("message", (event) => {
    data = event.data
    if data and (data.get("message") == MESSAGE_TRYXPATH_REQUEST_TO_POPUP):
        sendMsg = createResultMessage()
        message_id = data.get("messageId")
        if message_id == 0:
            sendMsg["message"] = MESSAGE_ERROR_OCCURRED_FRAME + "There is a frame having frameId."
        elif message_id == 1:
             sendMsg["message"] = MESSAGE_ERROR_OCCURRED_FOCUS_FRAME + "There is a frame having frameId."
        browser.runtime.sendMessage(sendMsg)
})


prevMsg = createResultMessage()
setFocusFrameListener(window, False)

browser.runtime.sendMessage({
    "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "requestSetContentInfo"
})

```