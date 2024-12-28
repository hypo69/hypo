# Анализ кода модуля show_all_results.js

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и использует функции для разделения логики.
    - Присутствует обработка событий для взаимодействия с элементами DOM.
    - Используются `browser.runtime.sendMessage` и `browser.tabs.sendMessage` для взаимодействия с расширением.
    - Код использует `tryxpath` и его функции (`fu`).
-  Минусы
    - Отсутствуют docstring для функций и переменных, что затрудняет понимание кода.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Используются конструкции `try...catch` без логирования ошибок.
    - Код использует `JSON.stringify` для преобразования данных в текст, что может быть избыточным.
    -  Не хватает обработки ошибок в некоторых частях кода.

**Рекомендации по улучшению**
1. Добавить docstring к функциям и переменным для улучшения читаемости и документирования кода.
2. Использовать `from src.logger.logger import logger` для логирования ошибок вместо стандартного `try...catch`.
3. Заменить `JSON.stringify` на более подходящий способ преобразования данных в текст, если это необходимо.
4. Добавить обработку ошибок при отправке сообщений через `browser.runtime.sendMessage` и `browser.tabs.sendMessage`.
5. Упростить код, где это возможно.

**Оптимизиробанный код**
```python
"""
Модуль для отображения результатов XPath на странице.
=========================================================================================

Этот модуль обрабатывает и отображает результаты выполнения XPath запросов, полученных от расширения.
Он отображает результаты на странице, предоставляет возможность экспорта данных и обеспечивает взаимодействие
с элементами на странице результатов.

"""
# /* This Source Code Form is subject to the terms of the Mozilla Public
#  * License, v. 2.0. If a copy of the MPL was not distributed with this
#  * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

# (function (window, undefined) {
#     "use strict";
#
#     // alias
#     var tx = tryxpath;
#     var fu = tryxpath.functions;
#
#     var document = window.document;
#
#     var detailKeys = ["type", "name", "value", "textContent"];
#     var headerValues = ["Type", "Name", "Value", "textContent"];
#     var relatedTabId;
#     var relatedFrameId;
#     var executionId;
from src.logger.logger import logger  # Импортируем logger


def showAllResults(results):
    """
    Отображает результаты XPath на странице.

    :param results: Объект, содержащий результаты XPath запроса.
    :type results: dict
    """
    try:
        # Код устанавливает текст элементов message, title, url, frame-id
        document.getElementById("message").textContent = results.message
        document.getElementById("title").textContent = results.title
        document.getElementById("url").textContent = results.href
        document.getElementById("frame-id").textContent = results.frameId

        if results.context:
            # Код обрабатывает контекст, если он существует
            cont = results.context
            # Код устанавливает текст элементов context-method, context-expression, context-specified-result-type, context-result-type, context-resolver
            document.getElementById("context-method").textContent = cont.method
            document.getElementById("context-expression").textContent = cont.expression
            document.getElementById("context-specified-result-type").textContent = cont.specifiedResultType
            document.getElementById("context-result-type").textContent = cont.resultType
            document.getElementById("context-resolver").textContent = cont.resolver
            # Код получает элемент tbody для context-detail
            contTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0]
            if cont.itemDetail:
                # Код обновляет таблицу деталей контекста
                fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                    "headerValues": headerValues,
                    "detailKeys": detailKeys
                }).catch(fu.onError)
        else:
            # Код удаляет область контекста, если она не существует
            area = document.getElementById("context-area")
            area.parentNode.removeChild(area)

        # Код обрабатывает основные результаты
        main = results.main
        # Код устанавливает текст элементов main-method, main-expression, main-specified-result-type, main-result-type, main-resolver, main-count
        document.getElementById("main-method").textContent = main.method
        document.getElementById("main-expression").textContent = main.expression
        document.getElementById("main-specified-result-type").textContent = main.specifiedResultType
        document.getElementById("main-result-type").textContent = main.resultType
        document.getElementById("main-resolver").textContent = main.resolver
        document.getElementById("main-count").textContent = main.itemDetails.length
        # Код получает элемент tbody для main-details
        mainTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0]
        # Код обновляет таблицу основных деталей
        fu.updateDetailsTable(mainTbody, main.itemDetails, {
            "headerValues": headerValues,
            "detailKeys": detailKeys
        }).catch(fu.onError)
    except Exception as ex:
        # Код логирует ошибку, если что-то пошло не так при отображении результатов
        logger.error("Ошибка при отображении результатов", ex)


def makeTextDownloadUrl(text):
    """
    Создает URL для скачивания текстового файла.

    :param text: Текст для скачивания.
    :type text: str
    :return: URL для скачивания.
    :rtype: str
    """
    # Код создает URL для скачивания текстового файла
    return URL.createObjectURL(new Blob([text], { "type": "text/plain"}))


def makeInfoText(results):
    """
    Создает текстовое представление результатов для скачивания.

    :param results: Объект, содержащий результаты XPath запроса.
    :type results: dict
    :return: Текстовое представление результатов.
    :rtype: str
    """
    # Код формирует текстовое представление результатов
    cont = results.context
    main = results.main
    return f"""[Information]
Message:     {results.message}
Title:       {results.title}
URL:         {results.href}
frameId:     {results.frameId}

{"" if not cont else f"""[Context information]
Method:                  {cont.method}
Expression:              {cont.expression}
Specified resultType:    {cont.specifiedResultType}
resultType:              {cont.resultType}
Resolver:                {cont.resolver}

[Context detail]
{", ".join(headerValues)}
{fu.makeDetailText(cont.itemDetail, detailKeys, ", ")}
"""}
[Main information]
Method:                  {main.method}
Expression:              {main.expression}
Specified resultType:    {main.specifiedResultType}
resultType:              {main.resultType}
Resolver:                {main.resolver}
Count:                   {main.itemDetails.length}

[Main details]
{", ".join(["Index"] + headerValues)}
{"\\n".join(main.itemDetails.map(lambda detail, ind: fu.makeDetailText(detail, ["index"] + detailKeys, ", ", {
          "index": lambda val: ind
      })))}
"""


def makeConvertedInfoText(results):
    """
    Создает текстовое представление результатов с преобразованными значениями JSON для скачивания.

    :param results: Объект, содержащий результаты XPath запроса.
    :type results: dict
    :return: Текстовое представление результатов с преобразованными значениями.
    :rtype: str
    """
    # Код формирует текстовое представление результатов с преобразованными значениями
    cont = results.context
    main = results.main
    return f"""[Information]
Message:     {results.message}
Title:       {results.title}
URL:         {results.href}
frameId:     {results.frameId}

{"" if not cont else f"""[Context information]
Method:                  {cont.method}
Expression(JSON):        {JSON.stringify(cont.expression)}
Specified resultType:    {cont.specifiedResultType}
resultType:              {cont.resultType}
Resolver:                {cont.resolver}

[Context detail]
Type, Name, Value(JSON), textContent(JSON)
{fu.makeDetailText(cont.itemDetail, detailKeys, ", ", {
    "value": JSON.stringify,
    "textContent": JSON.stringify
})}
"""}
[Main information]
Method:                  {main.method}
Expression(JSON):        {JSON.stringify(main.expression)}
Specified resultType:    {main.specifiedResultType}
resultType:              {main.resultType}
Resolver:                {main.resolver}
Count:                   {main.itemDetails.length}

[Main details]
Index, Type, Name, Value(JSON), textContent(JSON)
{"\\n".join(main.itemDetails.map(lambda detail, ind: fu.makeDetailText(detail, ["index"] + detailKeys, ", ", {
          "index": lambda val: ind,
          "value": JSON.stringify,
          "textContent": JSON.stringify
      })))}
"""


# window.addEventListener("load", function() {
#
#
#         browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
#             if (results) {
#                 relatedTabId = results.tabId;
#                 relatedFrameId = results.frameId;
#                 executionId = results.executionId;
#
#                 let expoText = document.getElementById("export-text");
#                 expoText.setAttribute(
#                     "download", `tryxpath-${results.title}.txt`);
#                 expoText.href =  makeTextDownloadUrl(makeInfoText(results));
#                 let expoPartConv = document.getElementById(
#                     "export-partly-converted");
#                 expoPartConv.setAttribute(
#                     "download", `tryxpath-converted-${results.title}.txt`);
#                 expoPartConv.href =  makeTextDownloadUrl(
#                     makeConvertedInfoText(results));
#
#                 showAllResults(results);
#             }
#         }).catch(fu.onError);
#
#
#         var contDetail = document.getElementById("context-detail");
#         contDetail.addEventListener("click", function(event) {
#             var target = event.target;
#             if (target.tagName.toLowerCase() === "button") {
#                 browser.tabs.sendMessage(relatedTabId, {
#                     "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
#                     "executionId": executionId
#                 }, {
#                     "frameId": relatedFrameId
#                 });
#             }
#         });
#
#         var mainDetails = document.getElementById("main-details");
#         mainDetails.addEventListener("click", function(event) {
#             var target = event.target;
#             if (target.tagName.toLowerCase() === "button") {
#                 let ind = parseInt(target.getAttribute("data-index"), 10);
#                 browser.tabs.sendMessage(relatedTabId, {
#                     "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
#                     "executionId": executionId,
#                     "index": ind
#                 }, {
#                     "frameId": relatedFrameId
#                 });
#             }
#         });
#     });

# window.addEventListener("load", function() {
# Обработчик события загрузки окна
def on_window_load():
    """
    Обработчик события загрузки окна.
    """
    # Код отправляет сообщение для получения результатов
    browser.runtime.sendMessage({"event":"loadResults"}).then(lambda results: {
        # Код обрабатывает полученные результаты
        if results:
            # Код устанавливает значения переменных relatedTabId, relatedFrameId, executionId
            global relatedTabId, relatedFrameId, executionId
            relatedTabId = results.tabId
            relatedFrameId = results.frameId
            executionId = results.executionId

            # Код получает элемент export-text и устанавливает атрибуты download и href
            expoText = document.getElementById("export-text")
            expoText.setAttribute(
                "download", f"tryxpath-{results.title}.txt")
            expoText.href =  makeTextDownloadUrl(makeInfoText(results))
            # Код получает элемент export-partly-converted и устанавливает атрибуты download и href
            expoPartConv = document.getElementById(
                "export-partly-converted")
            expoPartConv.setAttribute(
                "download", f"tryxpath-converted-{results.title}.txt")
            expoPartConv.href =  makeTextDownloadUrl(
                makeConvertedInfoText(results))
            # Код отображает результаты на странице
            showAllResults(results)
    }).catch(lambda ex: logger.error("Ошибка при получении результатов", ex))

    # Код получает элемент context-detail и устанавливает обработчик события click
    contDetail = document.getElementById("context-detail")
    contDetail.addEventListener("click", lambda event: {
        # Код обрабатывает клик на элементе context-detail
        target = event.target
        if target.tagName.lower() == "button":
            # Код отправляет сообщение для фокусировки на элементе контекста
            browser.tabs.sendMessage(relatedTabId, {
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                "executionId": executionId
            }, {
                "frameId": relatedFrameId
            }).catch(lambda ex: logger.error("Ошибка при отправке сообщения для фокусировки на элементе контекста", ex))
    })

    # Код получает элемент main-details и устанавливает обработчик события click
    mainDetails = document.getElementById("main-details")
    mainDetails.addEventListener("click", lambda event: {
        # Код обрабатывает клик на элементе main-details
        target = event.target
        if target.tagName.lower() == "button":
            # Код получает индекс элемента
            ind = int(target.getAttribute("data-index"), 10)
            # Код отправляет сообщение для фокусировки на элементе
            browser.tabs.sendMessage(relatedTabId, {
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                "executionId": executionId,
                "index": ind
            }, {
                "frameId": relatedFrameId
            }).catch(lambda ex: logger.error("Ошибка при отправке сообщения для фокусировки на элементе", ex))
    })


window.addEventListener("load", on_window_load)
# })(window);