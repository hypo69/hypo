## Анализ кода модуля show_all_results.js

**Качество кода**

7
-  Плюсы
    - Код достаточно хорошо структурирован и читаем.
    - Используется IIFE (Immediately Invoked Function Expression) для изоляции области видимости.
    - Есть обработка событий `click` для элементов таблицы.
    - Данные для отображения и экспорта подготавливаются отдельно.
    - Присутствует обработка ошибок через `.catch(fu.onError)`.
-  Минусы
    -  Отсутствует явное указание типа для переменных `tx`, `fu` и `document`.
    -  Используется `document.getElementById` многократно, что может быть оптимизировано.
    -  Нет комментариев в формате RST.
    -  Не используется `logger` для логирования ошибок.
    -  Используется `JSON.stringify` без обработки возможных ошибок.
    -  Функции `makeTextDownloadUrl`, `makeInfoText` и `makeConvertedInfoText` не имеют документации.
    -  Многократное использование `document.getElementById` может привести к снижению производительности.
    -  Не проверяется наличие элементов в DOM перед обращением к ним, что может вызвать ошибки, если элемент не найден.

**Рекомендации по улучшению**

1.  **Добавить документацию:**
    - Добавить docstring в формате RST для всех функций, чтобы сделать код более понятным и поддерживаемым.
2.  **Улучшить обработку ошибок:**
    - Использовать `logger.error` для логирования ошибок вместо `catch(fu.onError)`.
3.  **Улучшить читаемость и производительность:**
    - Кешировать результаты `document.getElementById` для часто используемых элементов.
    - Проверять наличие элементов в DOM перед обращением к ним.
4.  **Обработка JSON:**
    - Добавить `try-except` для обработки ошибок при `JSON.stringify`.
5.  **Явное объявление типов:**
    -  Добавить `/** @type {type} */` комментарии для переменных `tx`, `fu` и `document`, чтобы было понятно, что это за переменные.
6.  **Импорты:**
    - Добавить необходимые импорты `from src.logger.logger import logger`

**Оптимизиробанный код**

```python
"""
Модуль для отображения результатов XPath запросов в расширении Firefox.
===================================================================

Этот модуль отвечает за отображение результатов XPath запросов, полученных
от фоновой страницы, в HTML-странице расширения. Он также предоставляет
возможность экспорта результатов в текстовый файл.

Функции:
    - showAllResults: Отображает результаты запроса на странице.
    - makeTextDownloadUrl: Создает URL для скачивания текстового файла.
    - makeInfoText: Формирует текстовое представление результатов.
    - makeConvertedInfoText: Формирует текстовое представление результатов с JSON.
"""
from src.logger.logger import logger
# from src.utils.jjson import j_loads_ns  # TODO: Возможно потребуется
# from typing import Any, Dict, List  # TODO: Возможно потребуется
# TODO: Уточнить какие импорты нужны

(function (window, undefined) {
    "use strict";

    /** @type {tryxpath} */
    var tx = tryxpath;
    /** @type {tryxpath.functions} */
    var fu = tryxpath.functions;
    /** @type {Document} */
    var document = window.document;

    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;

    /**
     * Отображает результаты XPath запроса на странице.
     *
     * :param results: Объект с результатами запроса.
     * :type results: dict
     */
    function showAllResults(results) {
        try {
            var messageElement = document.getElementById("message");
            var titleElement = document.getElementById("title");
            var urlElement = document.getElementById("url");
            var frameIdElement = document.getElementById("frame-id");

            if (messageElement) {
                messageElement.textContent = results.message;
            }
            if (titleElement) {
                 titleElement.textContent = results.title;
            }
            if (urlElement) {
                urlElement.textContent = results.href;
            }
            if (frameIdElement) {
                frameIdElement.textContent = results.frameId;
            }

        }
        except Exception as ex:
            logger.error('Ошибка при установке основных текстовых полей', ex)
            return

        if (results.context) {
             try:
                let cont = results.context;
                var contextMethodElement = document.getElementById("context-method");
                var contextExpressionElement = document.getElementById("context-expression");
                var contextSpecifiedResultTypeElement = document.getElementById("context-specified-result-type");
                var contextResultTypeElement = document.getElementById("context-result-type");
                var contextResolverElement = document.getElementById("context-resolver");
                var contTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0];
                if (contextMethodElement) {
                     contextMethodElement.textContent = cont.method;
                }
                if (contextExpressionElement) {
                     contextExpressionElement.textContent = cont.expression;
                }
                if (contextSpecifiedResultTypeElement) {
                     contextSpecifiedResultTypeElement.textContent = cont.specifiedResultType;
                }
                if (contextResultTypeElement) {
                     contextResultTypeElement.textContent = cont.resultType;
                }
                if (contextResolverElement) {
                    contextResolverElement.textContent = cont.resolver;
                }


                if (cont.itemDetail) {
                    fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                        "headerValues": headerValues,
                        "detailKeys": detailKeys
                    }).catch(function(error){
                         logger.error('Ошибка при обновлении таблицы context-detail', error)
                    });
                }
             except Exception as ex:
                logger.error('Ошибка при установке context полей', ex)
                return
        } else {
             try:
                var area = document.getElementById("context-area");
                if(area && area.parentNode){
                     area.parentNode.removeChild(area);
                }
             except Exception as ex:
                logger.error('Ошибка при удалении context area', ex)
                return
        }
        try:
            var main = results.main;
            var mainMethodElement = document.getElementById("main-method");
            var mainExpressionElement = document.getElementById("main-expression");
            var mainSpecifiedResultTypeElement = document.getElementById("main-specified-result-type");
            var mainResultTypeElement = document.getElementById("main-result-type");
            var mainResolverElement = document.getElementById("main-resolver");
            var mainCountElement = document.getElementById("main-count");
            var mainTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0];

            if(mainMethodElement){
               mainMethodElement.textContent = main.method;
            }
            if(mainExpressionElement){
               mainExpressionElement.textContent = main.expression;
            }
            if(mainSpecifiedResultTypeElement){
              mainSpecifiedResultTypeElement.textContent = main.specifiedResultType;
            }
            if (mainResultTypeElement){
              mainResultTypeElement.textContent = main.resultType;
            }
            if(mainResolverElement){
                mainResolverElement.textContent = main.resolver;
            }
            if(mainCountElement){
                mainCountElement.textContent = main.itemDetails.length;
            }


            fu.updateDetailsTable(mainTbody, main.itemDetails, {
                "headerValues": headerValues,
                "detailKeys": detailKeys
            }).catch(function(error){
                logger.error('Ошибка при обновлении таблицы main-details', error)
            });
        except Exception as ex:
              logger.error('Ошибка при установке main полей', ex)
              return
    };

    /**
     * Создает URL для скачивания текстового файла.
     *
     * :param text: Текст для скачивания.
     * :type text: str
     * :return: URL для скачивания.
     * :rtype: str
     */
    function makeTextDownloadUrl(text) {
        return URL.createObjectURL(new Blob([text], { "type": "text/plain"}));
    };

    /**
     * Формирует текстовое представление результатов.
     *
     * :param results: Объект с результатами запроса.
     * :type results: dict
     * :return: Текстовое представление результатов.
     * :rtype: str
     */
    function makeInfoText(results) {
        let cont = results.context;
        let main = results.main;
        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression:              ${cont.expression}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\n${headerValues.join(", ")}\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ")}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression:              ${main.expression}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\n${["Index"].concat(headerValues).join(", ")}\n${main.itemDetails.map((detail, ind) => {
          return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {
              "index": val => { return ind; }
          });
      }).join("\\n")}\n`;
    };

    /**
     * Формирует текстовое представление результатов с JSON.
     *
     * :param results: Объект с результатами запроса.
     * :type results: dict
     * :return: Текстовое представление результатов с JSON.
     * :rtype: str
     */
    function makeConvertedInfoText(results) {
        let cont = results.context;
        let main = results.main;
        let contextExpression, mainExpression
        try:
            contextExpression = JSON.stringify(cont.expression)
        except Exception as ex:
            logger.error('Ошибка при преобразовании context expression в JSON', ex)
            contextExpression = "error"
        try:
            mainExpression = JSON.stringify(main.expression)
        except Exception as ex:
            logger.error('Ошибка при преобразовании main expression в JSON', ex)
            mainExpression = "error"

        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression(JSON):        ${contextExpression}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ", {\n    "value": JSON.stringify,\n    "textContent": JSON.stringify\n})}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression(JSON):        ${mainExpression}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n${main.itemDetails.map((detail, ind) => {\n      return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {\n          "index": val => { return ind; },\n          "value": JSON.stringify,\n          "textContent": JSON.stringify\n      });\n  }).join("\\n")}\n`;
    };

    window.addEventListener("load", function() {
         browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            if (results) {
                relatedTabId = results.tabId;
                relatedFrameId = results.frameId;
                executionId = results.executionId;

                let expoText = document.getElementById("export-text");
                if(expoText){
                    expoText.setAttribute(
                        "download", `tryxpath-${results.title}.txt`);
                    expoText.href =  makeTextDownloadUrl(makeInfoText(results));
                }


                let expoPartConv = document.getElementById(
                    "export-partly-converted");
                if(expoPartConv){
                    expoPartConv.setAttribute(
                       "download", `tryxpath-converted-${results.title}.txt`);
                    expoPartConv.href =  makeTextDownloadUrl(
                        makeConvertedInfoText(results));
                }


                showAllResults(results);
            }
        }).catch(function(error) {
            logger.error('Ошибка при получении результатов от background script', error);
        });


        var contDetail = document.getElementById("context-detail");
        if(contDetail){
            contDetail.addEventListener("click", function(event) {
                var target = event.target;
                if (target.tagName.toLowerCase() === "button") {
                    browser.tabs.sendMessage(relatedTabId, {
                        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                        "executionId": executionId
                    }, {
                        "frameId": relatedFrameId
                    }).catch(function(error){
                        logger.error('Ошибка при отправке сообщения focusContextItem', error);
                    });
                }
            });
        }



        var mainDetails = document.getElementById("main-details");
        if(mainDetails){
             mainDetails.addEventListener("click", function(event) {
                var target = event.target;
                if (target.tagName.toLowerCase() === "button") {
                    let ind = parseInt(target.getAttribute("data-index"), 10);
                    browser.tabs.sendMessage(relatedTabId, {
                        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                        "executionId": executionId,
                        "index": ind
                    }, {
                        "frameId": relatedFrameId
                    }).catch(function(error){
                        logger.error('Ошибка при отправке сообщения focusItem', error);
                    });
                }
             });
        }

    });

})(window);