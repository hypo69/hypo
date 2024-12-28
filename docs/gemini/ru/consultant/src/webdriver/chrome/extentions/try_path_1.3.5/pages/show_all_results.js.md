## Анализ кода модуля show_all_results.js

**Качество кода**
    7
 -  Плюсы
        - Код достаточно структурирован и понятен.
        - Используются функции для создания URL скачивания и текстового представления данных.
        - Присутствует обработка событий для элементов управления (кнопки).
        - Код использует `browser.runtime.sendMessage` для взаимодействия с расширением.
 -  Минусы
    -  Отсутствует обработка ошибок при взаимодействии с `browser.runtime.sendMessage`.
    -  Не используются константы для ключей и заголовков, что снижает читаемость.
    -  Не хватает docstring для функций, что усложняет понимание их назначения.
    -  Код не использует `logger` для логирования ошибок.
    -  Используется `var` вместо `let` и `const`.
    -  Многократное использование `document.getElementById` может быть оптимизировано с помощью кеширования элементов.

**Рекомендации по улучшению**

1.  **Добавить docstring:**
    *   Добавить docstring к функциям `showAllResults`, `makeTextDownloadUrl`, `makeInfoText`, `makeConvertedInfoText`.

2.  **Использовать `logger`:**
    *   Заменить `console.error` на `logger.error` для логирования ошибок.
    *   Добавить try-except блоки для обработки ошибок при вызове `browser.runtime.sendMessage` и `fu.updateDetailsTable`.

3.  **Использовать константы:**
    *   Определить константы для ключей, заголовков и других повторяющихся строк.

4.  **Кешировать элементы:**
    *   Кешировать результаты вызовов `document.getElementById` для повышения производительности.

5.  **Использовать `let` и `const`:**
    *   Заменить `var` на `let` и `const` в соответствии с современными стандартами JavaScript.

6.  **Улучшить читаемость:**
    *   Разбить длинные строки на несколько строк для улучшения читаемости кода.
    *   Добавить комментарии к сложным частям кода.

7.  **Обработка ошибок:**
    *   Добавить обработку ошибок для асинхронных операций с использованием `async/await` и `try/catch`.

**Оптимизированный код**
```python
"""
Модуль для отображения результатов XPath запросов в расширении.
=================================================================

Этот модуль отвечает за отображение результатов XPath запросов,
полученных от фонового скрипта расширения, на странице `show_all_results.html`.
Он включает в себя функции для форматирования данных и создания интерактивных элементов.
"""
import json
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

# Константы для ключей и заголовков
DETAIL_KEYS = ["type", "name", "value", "textContent"]
HEADER_VALUES = ["Type", "Name", "Value", "textContent"]
INDEX_KEY = "index"

# Кеширование элементов DOM
document = window.document
MESSAGE_ELEMENT = document.getElementById("message")
TITLE_ELEMENT = document.getElementById("title")
URL_ELEMENT = document.getElementById("url")
FRAME_ID_ELEMENT = document.getElementById("frame-id")
CONTEXT_METHOD_ELEMENT = document.getElementById("context-method")
CONTEXT_EXPRESSION_ELEMENT = document.getElementById("context-expression")
CONTEXT_SPECIFIED_RESULT_TYPE_ELEMENT = document.getElementById("context-specified-result-type")
CONTEXT_RESULT_TYPE_ELEMENT = document.getElementById("context-result-type")
CONTEXT_RESOLVER_ELEMENT = document.getElementById("context-resolver")
CONTEXT_DETAIL_TBODY = document.getElementById("context-detail").getElementsByTagName("tbody")[0]
CONTEXT_AREA = document.getElementById("context-area")
MAIN_METHOD_ELEMENT = document.getElementById("main-method")
MAIN_EXPRESSION_ELEMENT = document.getElementById("main-expression")
MAIN_SPECIFIED_RESULT_TYPE_ELEMENT = document.getElementById("main-specified-result-type")
MAIN_RESULT_TYPE_ELEMENT = document.getElementById("main-result-type")
MAIN_RESOLVER_ELEMENT = document.getElementById("main-resolver")
MAIN_COUNT_ELEMENT = document.getElementById("main-count")
MAIN_DETAILS_TBODY = document.getElementById("main-details").getElementsByTagName("tbody")[0]
EXPORT_TEXT_ELEMENT = document.getElementById("export-text")
EXPORT_PARTLY_CONVERTED_ELEMENT = document.getElementById("export-partly-converted")
CONTEXT_DETAIL_ELEMENT = document.getElementById("context-detail")
MAIN_DETAILS_ELEMENT = document.getElementById("main-details")

# alias
tx = tryxpath
fu = tryxpath.functions


def showAllResults(results: dict) -> None:
    """
    Отображает результаты XPath запроса на странице.

    :param results: Объект, содержащий результаты запроса.
    :type results: dict
    """
    MESSAGE_ELEMENT.textContent = results.message
    TITLE_ELEMENT.textContent = results.title
    URL_ELEMENT.textContent = results.href
    FRAME_ID_ELEMENT.textContent = results.frameId

    if results.context:
        cont = results.context
        CONTEXT_METHOD_ELEMENT.textContent = cont.method
        CONTEXT_EXPRESSION_ELEMENT.textContent = cont.expression
        CONTEXT_SPECIFIED_RESULT_TYPE_ELEMENT.textContent = cont.specifiedResultType
        CONTEXT_RESULT_TYPE_ELEMENT.textContent = cont.resultType
        CONTEXT_RESOLVER_ELEMENT.textContent = cont.resolver

        if cont.itemDetail:
            fu.updateDetailsTable(CONTEXT_DETAIL_TBODY, [cont.itemDetail], {
                "headerValues": HEADER_VALUES,
                "detailKeys": DETAIL_KEYS
            }).catch(lambda ex: logger.error(f"Ошибка при обновлении таблицы context detail: {ex}"))
    else:
        CONTEXT_AREA.parentNode.removeChild(CONTEXT_AREA)

    main = results.main
    MAIN_METHOD_ELEMENT.textContent = main.method
    MAIN_EXPRESSION_ELEMENT.textContent = main.expression
    MAIN_SPECIFIED_RESULT_TYPE_ELEMENT.textContent = main.specifiedResultType
    MAIN_RESULT_TYPE_ELEMENT.textContent = main.resultType
    MAIN_RESOLVER_ELEMENT.textContent = main.resolver
    MAIN_COUNT_ELEMENT.textContent = main.itemDetails.length

    fu.updateDetailsTable(MAIN_DETAILS_TBODY, main.itemDetails, {
        "headerValues": HEADER_VALUES,
        "detailKeys": DETAIL_KEYS
    }).catch(lambda ex: logger.error(f"Ошибка при обновлении таблицы main detail: {ex}"))


def makeTextDownloadUrl(text: str) -> str:
    """
    Создает URL для скачивания текстового файла.

    :param text: Текст для скачивания.
    :type text: str
    :return: URL для скачивания.
    :rtype: str
    """
    return URL.createObjectURL(new Blob([text], { "type": "text/plain"}))


def makeInfoText(results: dict) -> str:
    """
    Создает текстовое представление результатов XPath запроса.

    :param results: Объект, содержащий результаты запроса.
    :type results: dict
    :return: Текстовое представление результатов.
    :rtype: str
    """
    cont = results.context
    main = results.main
    text = f"[Information]\nMessage:     {results.message}\nTitle:       {results.title}\nURL:         {results.href}\nframeId:     {results.frameId}\n\n"
    if cont:
        text += f"[Context information]\nMethod:                  {cont.method}\nExpression:              {cont.expression}\nSpecified resultType:    {cont.specifiedResultType}\nresultType:              {cont.resultType}\nResolver:                {cont.resolver}\n\n[Context detail]\n{', '.join(HEADER_VALUES)}\n{fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ', ')}\n"

    text += f"[Main information]\nMethod:                  {main.method}\nExpression:              {main.expression}\nSpecified resultType:    {main.specifiedResultType}\nresultType:              {main.resultType}\nResolver:                {main.resolver}\nCount:                   {main.itemDetails.length}\n\n[Main details]\n{['Index'] + HEADER_VALUES.join(', ')}\n"
    text += "\n".join(
        fu.makeDetailText(detail, [INDEX_KEY] + DETAIL_KEYS, ', ', {INDEX_KEY: lambda val: ind})
            for ind, detail in enumerate(main.itemDetails)
    )
    return text


def makeConvertedInfoText(results: dict) -> str:
    """
    Создает текстовое представление результатов XPath запроса с JSON-сериализацией.

    :param results: Объект, содержащий результаты запроса.
    :type results: dict
    :return: Текстовое представление результатов с JSON-сериализацией.
    :rtype: str
    """
    cont = results.context
    main = results.main
    text = f"[Information]\nMessage:     {results.message}\nTitle:       {results.title}\nURL:         {results.href}\nframeId:     {results.frameId}\n\n"
    if cont:
        text += f"[Context information]\nMethod:                  {cont.method}\nExpression(JSON):        {json.dumps(cont.expression)}\nSpecified resultType:    {cont.specifiedResultType}\nresultType:              {cont.resultType}\nResolver:                {cont.resolver}\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\n{fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ', ', {'value': json.dumps, 'textContent': json.dumps})}\n"
    text += f"[Main information]\nMethod:                  {main.method}\nExpression(JSON):        {json.dumps(main.expression)}\nSpecified resultType:    {main.specifiedResultType}\nresultType:              {main.resultType}\nResolver:                {main.resolver}\nCount:                   {main.itemDetails.length}\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n"
    text += "\n".join(
        fu.makeDetailText(detail, [INDEX_KEY] + DETAIL_KEYS, ', ',
                       {INDEX_KEY: lambda val: ind, 'value': json.dumps, 'textContent': json.dumps})
            for ind, detail in enumerate(main.itemDetails)
    )

    return text


window.addEventListener("load", lambda: (
    browser.runtime.sendMessage({"event":"loadResults"})
        .then(results => {
            if results:
                relatedTabId = results.tabId
                relatedFrameId = results.frameId
                executionId = results.executionId

                EXPORT_TEXT_ELEMENT.setAttribute(
                    "download", f"tryxpath-{results.title}.txt")
                EXPORT_TEXT_ELEMENT.href = makeTextDownloadUrl(makeInfoText(results))
                EXPORT_PARTLY_CONVERTED_ELEMENT.setAttribute(
                    "download", f"tryxpath-converted-{results.title}.txt")
                EXPORT_PARTLY_CONVERTED_ELEMENT.href = makeTextDownloadUrl(
                    makeConvertedInfoText(results))

                showAllResults(results)
        })
        .catch(lambda ex: logger.error(f"Ошибка при получении результатов: {ex}"))
    )
)
# устанавливаем слушатель на контекст
CONTEXT_DETAIL_ELEMENT.addEventListener("click", lambda event: (
    (target := event.target) and
    target.tagName.toLowerCase() == "button" and
    browser.tabs.sendMessage(relatedTabId, {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "focusContextItem",
        "executionId": executionId
    }, {"frameId": relatedFrameId})
))

# устанавливаем слушатель на главные детали
MAIN_DETAILS_ELEMENT.addEventListener("click", lambda event: (
    (target := event.target) and
    target.tagName.toLowerCase() == "button" and
    (ind := int(target.getAttribute("data-index"), 10)) and
    browser.tabs.sendMessage(relatedTabId, {
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "focusItem",
        "executionId": executionId,
        "index": ind
    }, {"frameId": relatedFrameId})
))