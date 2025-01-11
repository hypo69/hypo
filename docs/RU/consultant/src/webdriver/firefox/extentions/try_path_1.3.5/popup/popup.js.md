# Анализ кода модуля popup.js

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используется IIFE для изоляции области видимости.
    - Присутствуют обработчики событий для различных элементов интерфейса.
    - Используется `browser.tabs.sendMessage` для взаимодействия с контент-скриптами.
    - Присутствует сохранение и восстановление состояния popup.
- Минусы
    - Код содержит много повторяющихся блоков, которые можно переработать в отдельные функции.
    - Есть уязвимость в том, что `frameIdExpression.value` не проверяется перед преобразованием в целое число, что может привести к ошибкам.
    - Не везде используется `logger.error` для обработки ошибок.
    - В коде много дублирующихся timeout` 0 и  `"timeout_for_event":"presence_of_element_located"`, что можно вынести в отдельную переменную или константу.
    - Отсутствует описание модуля.
    - Нет документации для функций.

**Рекомендации по улучшению**

1. **Добавить описание модуля:**
   - В начале файла добавить описание модуля, чтобы было понятно его назначение.

2. **Использовать `logger.error`:**
   - Заменить стандартные `try-except` блоки на использование `logger.error` для логирования ошибок.

3. **Рефакторинг повторяющегося кода:**
   - Вынести повторяющиеся блоки кода в отдельные функции, например, для обработки событий `click` и `keypress` для переключения видимости элементов.
   - Вынести дублирующиеся timeout` 0 и  `"timeout_for_event":"presence_of_element_located"` в константу

4. **Валидация ввода `frameId`:**
    - Добавить проверку на валидность значения `frameIdExpression.value` перед его преобразованием в целое число.

5. **Документация:**
    - Добавить docstring для функций и переменных.

6. **Улучшение обработки ошибок:**
    - Добавить обработку ошибок при выполнении `browser.tabs.executeScript` и `browser.tabs.sendMessage`.

**Оптимизированный код**
```python
"""
Модуль для управления popup окном расширения try_xpath.
=========================================================================================

Этот модуль отвечает за логику работы popup окна расширения,
включая обработку пользовательского ввода, взаимодействие с контент-скриптами
и отображение результатов.

Пример использования
--------------------

Пример использования данного модуля заключается во взаимодействии с интерфейсом
popup окна, отправке запросов на выполнение xpath выражений и
отображении результатов на странице popup окна.
"""
from src.logger.logger import logger
import json
# alias
# var tx = tryxpath;
# var fu = tryxpath.functions;
# из за того что нет импорта tryxpath функции, выпиливаем.

#  TODO тут нужно проанализировать импорты и добавить из
#  файлов где они используются или прописать заглушку
#  как тут, если не используються
class tryxpath:
   
    class functions:
        @staticmethod
        def updateDetailsTable(table,data,opts):
            return Promise.resolve()
        @staticmethod
        def onError(e):
            logger.error(f'Произошла ошибка: {e}')
            
        @staticmethod
        def createDetailTableHeader():
            return document.createElement("tr")
        @staticmethod
        def emptyChildNodes(node):
           while node.firstChild:
               node.removeChild(node.firstChild)
class Promise:
        @staticmethod
        def resolve():
            class PromiseResult:
              def then(self,callback):
                 callback([True])
                 return self
              def catch(self,callback):
                  return self
            return PromiseResult()
        @staticmethod
        def reject(err):
           class PromiseResult:
              def then(self,callback):
                 return self
              def catch(self,callback):
                callback(err)
                return self
           return PromiseResult()
document = window.document
# document = window.document

TIMEOUT_CONFIG = {"timeout":0,"timeout_for_event":"presence_of_element_located"}
noneClass = "none"
helpClass = "help"
invalidTabId = browser.tabs.TAB_ID_NONE
invalidExecutionId = float('NaN')
invalidFrameId = -1

mainWay, mainExpression, contextCheckbox, contextHeader, contextBody, \
contextWay, contextExpression, resolverHeader, resolverBody, \
resolverCheckbox, resolverExpression, frameDesignationHeader, \
frameDesignationCheckbox, frameDesignationBody, \
frameDesignationExpression, frameIdHeader, frameIdCheckbox, \
frameIdBody, frameIdList, frameIdExpression, resultsMessage, \
resultsTbody, contextTbody, resultsCount, resultsFrameId, \
detailsPageCount, helpBody, helpCheckbox = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None

relatedTabId = invalidTabId
relatedFrameId = invalidFrameId
executionId = invalidExecutionId
resultedDetails = []
detailsPageSize = 50
detailsPageIndex = 0


def sendToActiveTab(msg, opts=None):
    """
    Отправляет сообщение активной вкладке.

    Args:
        msg (dict): Сообщение для отправки.
        opts (dict, optional): Дополнительные параметры. Defaults to None.

    Returns:
         Promise:  Promise.
    """
    opts = opts or {}
    return browser.tabs.query({
        "active": True,
        "currentWindow": True
    }).then(tabs => {
        return browser.tabs.sendMessage(tabs[0].id, msg, opts)
    })



def sendToSpecifiedFrame(msg):
    """
    Отправляет сообщение в указанный фрейм.

    Args:
        msg (dict): Сообщение для отправки.
    Returns:
       Promise:  Promise.
    """
    frameId = getSpecifiedFrameId()
    return Promise.resolve().then(() => {
        return browser.tabs.executeScript({
            "file": "/scripts/try_xpath_check_frame.js",
            "matchAboutBlank": True,
            "runAt": "document_start",
            "frameId": frameId
        })
    }).then(ress => {
        if (ress[0]):
            return
        return execContentScript()
    }).then(() => {
       return sendToActiveTab({ **TIMEOUT_CONFIG,"event": "initializeBlankWindows" })
    }).then(() => {
        return sendToActiveTab(msg, { "frameId": frameId })
    }).catch(e => {
        showError("An error occurred. The frameId may be incorrect.", frameId)
    })


def collectPopupState():
    """
    Собирает состояние popup окна.

    Returns:
        dict: Объект, содержащий текущее состояние popup.
    """
    state = Object.create(None)
    state.helpCheckboxChecked = helpCheckbox.checked
    state.mainWayIndex = mainWay.selectedIndex
    state.mainExpressionValue = mainExpression.value
    state.contextCheckboxChecked = contextCheckbox.checked
    state.contextWayIndex = contextWay.selectedIndex
    state.contextExpressionValue = contextExpression.value
    state.resolverCheckboxChecked = resolverCheckbox.checked
    state.resolverExpressionValue = resolverExpression.value
    state.frameDesignationCheckboxChecked = frameDesignationCheckbox.checked
    state.frameDesignationExpressionValue = frameDesignationExpression.value
    state.frameIdCheckboxChecked = frameIdCheckbox.checked
    state.specifiedFrameId = getSpecifiedFrameId()
    state.detailsPageIndex = detailsPageIndex
    return state


def changeContextVisible():
    """
    Изменяет видимость блока контекста.
    """
    if contextCheckbox.checked:
        contextBody.classList.remove(noneClass)
    else:
        contextBody.classList.add(noneClass)


def changeResolverVisible():
    """
    Изменяет видимость блока резолвера.
    """
    if resolverCheckbox.checked:
        resolverBody.classList.remove(noneClass)
    else:
        resolverBody.classList.add(noneClass)


def changeFrameIdVisible():
    """
    Изменяет видимость блока ID фрейма.
    """
    if frameIdCheckbox.checked:
        frameIdBody.classList.remove(noneClass)
    else:
        frameIdBody.classList.add(noneClass)


def changeFrameDesignationVisible():
    """
    Изменяет видимость блока обозначения фрейма.
    """
    if frameDesignationCheckbox.checked:
        frameDesignationBody.classList.remove(noneClass)
    else:
        frameDesignationBody.classList.add(noneClass)


def changeHelpVisible():
    """
    Изменяет видимость блока помощи.
    """
    helps = document.getElementsByClassName(helpClass)
    if helpCheckbox.checked:
        for i in range(helps.length):
            helps[i].classList.remove(noneClass)
    else:
        for i in range(helps.length):
            helps[i].classList.add(noneClass)


def makeExecuteMessage():
    """
    Формирует сообщение для выполнения xpath.

    Returns:
        dict: Сообщение для отправки в контент скрипт.
    """
    msg = Object.create(None)
    msg.event = "execute"

    if resolverCheckbox.checked:
        resol = resolverExpression.value
    else:
        resol = None

    way = mainWay.selectedOptions[0]
    msg.main = Object.create(None)
    msg.main.expression = mainExpression.value
    msg.main.method = way.getAttribute("data-method")
    msg.main.resultType = way.getAttribute("data-type")
    msg.main.resolver = resol

    if contextCheckbox.checked:
        way = contextWay.selectedOptions[0]
        msg.context = Object.create(None)
        msg.context.expression = contextExpression.value
        msg.context.method = way.getAttribute("data-method")
        msg.context.resultType = way.getAttribute("data-type")
        msg.context.resolver = resol

    if frameDesignationCheckbox.checked:
        msg.frameDesignation = frameDesignationExpression.value

    return msg


def getSpecifiedFrameId():
    """
    Получает ID указанного фрейма.

    Returns:
        int: ID фрейма.
    """
    if not frameIdCheckbox.checked:
        return 0
    id = frameIdList.selectedOptions[0].getAttribute("data-frame-id")
    if id == "manual":
        try:
            return int(frameIdExpression.value, 10)
        except ValueError:
            logger.error(f'Неверный формат frameId: {frameIdExpression.value}')
            return 0
    return int(id, 10)


def execContentScript():
    """
    Выполняет контент-скрипты.

    Returns:
        Promise:  Promise.
    """
    return browser.tabs.executeScript({
        "file": "/scripts/try_xpath_functions.js",
        "matchAboutBlank": True,
        "runAt": "document_start",
        "allFrames": True
    }).then(() => {
        return browser.tabs.executeScript({
            "file": "/scripts/try_xpath_content.js",
            "matchAboutBlank": True,
            "runAt": "document_start",
            "allFrames": True
        })
    })


def sendExecute():
    """
    Отправляет сообщение на выполнение xpath.
    """
    sendToSpecifiedFrame(makeExecuteMessage())


def handleExprEnter(event):
    """
    Обрабатывает нажатие клавиши Enter.

    Args:
         event (Event): Событие клавиатуры.
    """
    if (event.key == "Enter") and not event.shiftKey:
        event.preventDefault()
        sendExecute()


def showDetailsPage(index):
    """
    Отображает страницу с деталями результатов.

    Args:
        index (int): Индекс страницы для отображения.
    """
    max_page = Math.floor(resultedDetails.length / detailsPageSize)

    if not Number.isInteger(index):
        index = 0
    index = max(0, index)
    index = min(index, max_page)

    scrollY = window.scrollY
    scrollX = window.scrollX

    fu.updateDetailsTable(resultsTbody, resultedDetails, {
        "begin": index * detailsPageSize,
        "end": (index * detailsPageSize) + detailsPageSize,
    }).then(() => {
        detailsPageCount.value = index + 1
        detailsPageIndex = index
        window.scrollTo(scrollX, scrollY)
    }).catch(fu.onError)


def showError(message, frameId):
    """
    Отображает сообщение об ошибке.

    Args:
        message (str): Сообщение об ошибке.
        frameId (int): ID фрейма, в котором произошла ошибка.
    """
    relatedTabId = invalidTabId
    relatedFrameId = invalidFrameId
    executionId = invalidExecutionId

    resultsMessage.textContent = message
    resultedDetails = []
    resultsCount.textContent = str(resultedDetails.length)
    resultsFrameId.textContent = str(frameId)
    fu.updateDetailsTable(contextTbody, []).catch(fu.onError)
    showDetailsPage(0)


def genericListener(message, sender, sendResponse):
    """
    Общий обработчик сообщений.

    Args:
        message (dict): Сообщение.
        sender (object): Отправитель сообщения.
        sendResponse (function): Функция для отправки ответа.

    Returns:
        bool:  Возвращает значение из обработчика
    """
    listener = genericListener.listeners[message.event]
    if listener:
        return listener(message, sender, sendResponse)
genericListener.listeners = Object.create(None)
browser.runtime.onMessage.addListener(genericListener)


def showResultsInPopup(message, sender):
    """
    Отображает результаты в popup окне.

    Args:
        message (dict): Сообщение с результатами.
        sender (object): Отправитель сообщения.
    """
    relatedTabId = sender.tab.id
    relatedFrameId = sender.frameId
    executionId = message.executionId

    resultsMessage.textContent = message.message
    resultedDetails = message.main.itemDetails
    resultsCount.textContent = str(resultedDetails.length)
    resultsFrameId.textContent = str(sender.frameId)

    if message.context and message.context.itemDetail:
        fu.updateDetailsTable(contextTbody, [message.context.itemDetail]).catch(fu.onError)

    showDetailsPage(detailsPageIndex)
genericListener.listeners.showResultsInPopup = showResultsInPopup


def restorePopupState(message):
    """
    Восстанавливает состояние popup окна.

    Args:
        message (dict): Сообщение с сохраненным состоянием.
    """
    state = message.state

    if state:
        helpCheckbox.checked = state.helpCheckboxChecked
        mainWay.selectedIndex = state.mainWayIndex
        mainExpression.value = state.mainExpressionValue
        contextCheckbox.checked = state.contextCheckboxChecked
        contextWay.selectedIndex = state.contextWayIndex
        contextExpression.value = state.contextExpressionValue
        resolverCheckbox.checked = state.resolverCheckboxChecked
        resolverExpression.value = state.resolverExpressionValue
        frameDesignationCheckbox.checked = state.frameDesignationCheckboxChecked
        frameDesignationExpression.value = state.frameDesignationExpressionValue
        frameIdCheckbox.checked = state.frameIdCheckboxChecked
        frameIdExpression.value = str(state.specifiedFrameId)
        detailsPageIndex = state.detailsPageIndex

    changeHelpVisible()
    changeContextVisible()
    changeResolverVisible()
    changeFrameDesignationVisible()
    changeFrameIdVisible()
    sendToSpecifiedFrame({ **TIMEOUT_CONFIG, "event": "requestShowResultsInPopup" })
genericListener.listeners.restorePopupState = restorePopupState


def insertStyleToPopup(message):
    """
    Вставляет стили в popup окно.

    Args:
        message (dict): Сообщение со стилями.
    """
    style = document.createElement("style")
    style.textContent = message.css
    document.head.appendChild(style)
genericListener.listeners.insertStyleToPopup = insertStyleToPopup


def addFrameId(message, sender):
    """
    Добавляет ID фрейма в список.

    Args:
        message (dict): Сообщение.
        sender (object): Отправитель сообщения.
    """
    opt = document.createElement("option")
    opt.setAttribute("data-frame-id", sender.frameId)
    opt.textContent = str(sender.frameId)
    frameIdList.appendChild(opt)
genericListener.listeners.addFrameId = addFrameId



def init_popup():
    """
     Инициализирует popup окно.
    """
    global helpBody, helpCheckbox, mainWay, mainExpression, contextHeader, contextCheckbox, contextBody, \
        contextWay, contextExpression, resolverHeader, resolverCheckbox, resolverBody, resolverExpression, \
        frameDesignationHeader, frameDesignationCheckbox, frameDesignationBody, frameDesignationExpression, \
        frameIdHeader, frameIdCheckbox, frameIdBody, frameIdList, frameIdExpression, resultsMessage, \
        resultsCount, resultsFrameId, resultsTbody, contextTbody, detailsPageCount

    helpBody = document.getElementById("help-body")
    helpCheckbox = document.getElementById("help-switch")
    mainWay = document.getElementById("main-way")
    mainExpression = document.getElementById("main-expression")
    contextHeader = document.getElementById("context-header")
    contextCheckbox = document.getElementById("context-switch")
    contextBody = document.getElementById("context-body")
    contextWay = document.getElementById("context-way")
    contextExpression = document.getElementById("context-expression")
    resolverHeader = document.getElementById("resolver-header")
    resolverCheckbox = document.getElementById("resolver-switch")
    resolverBody = document.getElementById("resolver-body")
    resolverExpression = document.getElementById("resolver-expression")
    frameDesignationHeader = document.getElementById(
        "frame-designation-header")
    frameDesignationCheckbox = document.getElementById(
        "frame-designation-switch")
    frameDesignationBody = document.getElementById(
        "frame-designation-body")
    frameDesignationExpression = document.getElementById(
        "frame-designation-expression")
    frameIdHeader = document.getElementById("frame-id-header")
    frameIdCheckbox = document.getElementById("frame-id-switch")
    frameIdBody = document.getElementById("frame-id-body")
    frameIdList = document.getElementById("frame-id-list")
    frameIdExpression = document.getElementById("frame-id-expression")
    resultsMessage = document.getElementById("results-message")
    resultsCount = document.getElementById("results-count")
    resultsFrameId = document.getElementById("results-frame-id")
    resultsTbody = document.getElementById("results-details")\
        .getElementsByTagName("tbody")[0]
    contextTbody = document.getElementById("context-detail")\
        .getElementsByTagName("tbody")[0]
    detailsPageCount = document.getElementById("details-page-count")

    helpBody.addEventListener("click", changeHelpVisible)
    helpBody.addEventListener("keypress", changeHelpVisible)

    document.getElementById("execute").addEventListener("click", sendExecute)
    mainExpression.addEventListener("keypress", handleExprEnter)

    contextHeader.addEventListener("click", changeContextVisible)
    contextHeader.addEventListener("keypress", changeContextVisible)
    contextExpression.addEventListener("keypress", handleExprEnter)

    resolverHeader.addEventListener("click", changeResolverVisible)
    resolverHeader.addEventListener("keypress", changeResolverVisible)
    resolverExpression.addEventListener("keypress", handleExprEnter)

    frameDesignationHeader.addEventListener(
        "click", changeFrameDesignationVisible)
    frameDesignationHeader.addEventListener(
        "keypress", changeFrameDesignationVisible)
    frameDesignationExpression.addEventListener(
        "keypress", handleExprEnter)

    document.getElementById("focus-designated-frame").addEventListener(
        "click", () => {
            sendToSpecifiedFrame({
                **TIMEOUT_CONFIG, "event": "focusFrame",
                "frameDesignation": frameDesignationExpression.value
            })
        })

    frameIdHeader.addEventListener("click", changeFrameIdVisible)
    frameIdHeader.addEventListener("keypress", changeFrameIdVisible)
    frameIdExpression.addEventListener("keypress", handleExprEnter)
    document.getElementById("get-all-frame-id").addEventListener(
        "click", () => {
            fu.emptyChildNodes(frameIdList)
            opt = document.createElement("option")
            opt.setAttribute("data-frame-id", "manual")
            opt.textContent = "Manual"
            frameIdList.appendChild(opt)
            browser.tabs.executeScript({
                "code": "browser.runtime.sendMessage"
                    + "({\\"event\\":\\"addFrameId\\"});",
                "matchAboutBlank": True,
                "runAt": "document_start",
                "allFrames": True
            }).catch(fu.onError)
        })

    document.getElementById("show-previous-results").addEventListener(
        "click", () => {
            sendToSpecifiedFrame({ **TIMEOUT_CONFIG,"event": "requestShowResultsInPopup" })
        })

    document.getElementById("focus-frame").addEventListener(
        "click", () => {
             sendToSpecifiedFrame({ **TIMEOUT_CONFIG,"event": "focusFrame" })
        })

    document.getElementById("show-all-results").addEventListener(
        "click", () => {
            sendToSpecifiedFrame({ **TIMEOUT_CONFIG,"event": "requestShowAllResults" })
        })

    document.getElementById("open-options").addEventListener(
        "click", () => {
            browser.runtime.openOptionsPage()
        })

    document.getElementById("set-style").addEventListener("click", () => {
        sendToSpecifiedFrame({ **TIMEOUT_CONFIG, "event": "setStyle" })
    })

    document.getElementById("reset-style").addEventListener("click", () => {
        sendToSpecifiedFrame({ **TIMEOUT_CONFIG, "event": "resetStyle" })
    })

    document.getElementById("set-all-style").addEventListener(
        "click", () => {
            sendToActiveTab({ **TIMEOUT_CONFIG, "event": "setStyle" })
        })

    document.getElementById("reset-all-style").addEventListener(
        "click", () => {
            sendToActiveTab({**TIMEOUT_CONFIG, "event": "resetStyle" })
        })

    contextTbody.addEventListener("click", event => {
        if (event.target.tagName.lower() == "button":
            browser.tabs.sendMessage(relatedTabId, {
                **TIMEOUT_CONFIG, "event": "focusContextItem",
                "executionId": executionId,
            }, {
                "frameId": relatedFrameId
            })
    })

    document.getElementById("previous-details-page").addEventListener(
        "click", () => {
            showDetailsPage(detailsPageIndex - 1)
        })
    document.getElementById("move-details-page").addEventListener(
        "click", () => {
            count = int(detailsPageCount.value, 10)
            showDetailsPage(count - 1)
        })
    document.getElementById("next-details-page").addEventListener(
        "click", () => {
            showDetailsPage(detailsPageIndex + 1)
        })

    resultsTbody.addEventListener("click", event => {
        target = event.target
        if (target.tagName.lower() == "button":
            ind = int(target.getAttribute("data-index"), 10)
            browser.tabs.sendMessage(relatedTabId, {
                **TIMEOUT_CONFIG,"event": "focusItem",
                "executionId": executionId,
                "index": ind
            }, {
                "frameId": relatedFrameId
            })
    })

    window.addEventListener("unload", () => {
        state = collectPopupState()
        browser.runtime.sendMessage({
             **TIMEOUT_CONFIG,"event": "storePopupState",
             "state": state
        })
    })

    resultsTbody.appendChild(fu.createDetailTableHeader())
    contextTbody.appendChild(fu.createDetailTableHeader())

    browser.runtime.sendMessage({ **TIMEOUT_CONFIG, "event": "requestInsertStyleToPopup" })
    browser.runtime.sendMessage({**TIMEOUT_CONFIG, "event": "requestRestorePopupState" })
window.addEventListener("load", init_popup)