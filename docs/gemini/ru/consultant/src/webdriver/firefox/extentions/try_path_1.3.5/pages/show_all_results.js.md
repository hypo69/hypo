## Анализ кода модуля `show_all_results.js`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и логически разделен на функции.
    - Используются понятные имена переменных и функций.
    - Присутствует обработка ошибок с использованием `catch(fu.onError)`.
    - Код соответствует стандартам JavaScript ES6.
- Минусы
    -  Отсутствует описание модуля в формате reStructuredText (RST).
    -  Отсутствуют docstring для функций.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Использование глобальных переменных `relatedTabId`, `relatedFrameId` и `executionId` без четкого указания области видимости.
    - Избыточное использование `document.getElementById`.
    - Смешивание форматирования строк (использование ` и  `).
    - В некоторых местах отсутствует проверка типов данных.

**Рекомендации по улучшению**

1.  **Добавить описание модуля**: Добавить описание модуля в формате reStructuredText (RST) в начале файла.
2.  **Добавить docstring**: Добавить docstring для всех функций в формате reStructuredText (RST).
3.  **Импортировать `logger`**: Добавить импорт `logger` из `src.logger.logger` и использовать его для логирования ошибок.
4.  **Использовать `j_loads` или `j_loads_ns`**: Хотя в этом файле нет операций загрузки JSON, рекомендуется использовать их по стандарту проекта, если это потребуется в будущем.
5.  **Управление глобальными переменными**: По возможности, следует избегать глобальных переменных или явно определять их область видимости.
6.  **Кэшировать элементы DOM**:  Кэшировать результаты `document.getElementById` для избежания повторных поисков.
7.  **Унифицировать форматирование строк**: Использовать только один тип кавычек для строк.
8.  **Проверка типов данных**: Добавить проверку типов данных перед их использованием.

**Оптимизированный код**

```python
"""
Модуль для отображения результатов XPath-запросов.
=========================================================================================

Этот модуль отвечает за отображение результатов XPath-запросов в HTML-странице расширения.
Он получает данные от фонового скрипта, отображает их на странице и предоставляет возможность
экспортировать результаты в текстовый файл.

"""
# alias
from src.logger.logger import logger  #  Импорт logger для логирования ошибок

try:
    from src.utils.jjson import j_loads, j_loads_ns # импорт для загрузки json
except ImportError:
    logger.error("Ошибка импорта j_loads, j_loads_ns")
    ...


(function (window, undefined) {
    "use strict";

    var tx = tryxpath;
    var fu = tryxpath.functions;
    var document = window.document;
    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId = null;  # Используем null как начальное значение, если данные еще не получены
    var relatedFrameId = null; # Используем null как начальное значение, если данные еще не получены
    var executionId = null; # Используем null как начальное значение, если данные еще не получены

    var messageElement = document.getElementById("message"); # Кэшируем элементы DOM
    var titleElement = document.getElementById("title");
    var urlElement = document.getElementById("url");
    var frameIdElement = document.getElementById("frame-id");
    var contextMethodElement = document.getElementById("context-method");
    var contextExpressionElement = document.getElementById("context-expression");
    var contextSpecifiedResultTypeElement = document.getElementById("context-specified-result-type");
    var contextResultTypeElement = document.getElementById("context-result-type");
    var contextResolverElement = document.getElementById("context-resolver");
    var contextDetailTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0];
    var contextArea = document.getElementById("context-area");
    var mainMethodElement = document.getElementById("main-method");
    var mainExpressionElement = document.getElementById("main-expression");
    var mainSpecifiedResultTypeElement = document.getElementById("main-specified-result-type");
    var mainResultTypeElement = document.getElementById("main-result-type");
    var mainResolverElement = document.getElementById("main-resolver");
    var mainCountElement = document.getElementById("main-count");
    var mainDetailsTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0];
    var expoTextElement = document.getElementById("export-text");
    var expoPartConvElement = document.getElementById("export-partly-converted");
    var contDetail = document.getElementById("context-detail");
    var mainDetails = document.getElementById("main-details");



    /**
     * Отображает результаты XPath-запроса на странице.
     *
     * :param results: Объект с результатами, содержащий message, title, href, frameId, context и main.
     * :type results: object
     */
    function showAllResults(results) {
      try {
          if (!results) {
                logger.error("Результаты не определены");
                return;
          }
            messageElement.textContent = results.message;
            titleElement.textContent = results.title;
            urlElement.textContent = results.href;
            frameIdElement.textContent = results.frameId;


            if (results.context) {
                let cont = results.context;
                contextMethodElement.textContent = cont.method;
                contextExpressionElement.textContent = cont.expression;
                contextSpecifiedResultTypeElement.textContent = cont.specifiedResultType;
                contextResultTypeElement.textContent = cont.resultType;
                contextResolverElement.textContent = cont.resolver;

                if (cont.itemDetail) {
                  fu.updateDetailsTable(contextDetailTbody, [cont.itemDetail], {
                        "headerValues": headerValues,
                        "detailKeys": detailKeys
                  }).catch(fu.onError);
                }
            } else {
                if (contextArea && contextArea.parentNode) { # Проверяем, существует ли элемент перед удалением
                    contextArea.parentNode.removeChild(contextArea);
                }
            }

        var main = results.main;
            mainMethodElement.textContent = main.method;
            mainExpressionElement.textContent = main.expression;
            mainSpecifiedResultTypeElement.textContent = main.specifiedResultType;
            mainResultTypeElement.textContent = main.resultType;
            mainResolverElement.textContent = main.resolver;
            mainCountElement.textContent = main.itemDetails.length;

            fu.updateDetailsTable(mainDetailsTbody, main.itemDetails, {
                "headerValues": headerValues,
                "detailKeys": detailKeys
            }).catch(fu.onError);

        }  catch (ex) {
             logger.error("Ошибка при отображении результатов:", ex);
              ...
        }
    }
    /**
     * Создает URL для скачивания текста.
     *
     * :param text: Текст для скачивания.
     * :type text: str
     * :return: URL для скачивания.
     * :rtype: str
     */
    function makeTextDownloadUrl(text) {
       try {
            return URL.createObjectURL(new Blob([text], { "type": "text/plain"}));
       }  catch (ex) {
           logger.error("Ошибка при создании URL для скачивания:", ex);
           return '';
       }
    }

     /**
     * Формирует текстовое представление информации о результатах.
     *
     * :param results: Объект с результатами, содержащий message, title, href, frameId, context и main.
     * :type results: object
     * :return: Текстовое представление информации.
     * :rtype: str
     */
    function makeInfoText(results) {
        try {
            let cont = results.context;
            let main = results.main;
            return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression:              ${cont.expression}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\n${headerValues.join(", ")}\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ")}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression:              ${main.expression}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\n${["Index"].concat(headerValues).join(", ")}\n${main.itemDetails.map((detail, ind) => {
                    return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {
                      "index": val => { return ind; }
                      });
                }).join("\\n")}\n`;
          }  catch (ex) {
                logger.error("Ошибка при формировании текстового представления информации:", ex);
                 return '';
        }
    }
    /**
      * Формирует текстовое представление информации с JSON-конвертацией значений.
      *
      * :param results: Объект с результатами, содержащий message, title, href, frameId, context и main.
      * :type results: object
      * :return: Текстовое представление информации с JSON-конвертацией.
      * :rtype: str
      */
    function makeConvertedInfoText(results) {
      try {
            let cont = results.context;
            let main = results.main;
              return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression(JSON):        ${JSON.stringify(cont.expression)}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ", {
                "value": JSON.stringify,
                "textContent": JSON.stringify
            })}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression(JSON):        ${JSON.stringify(main.expression)}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n${main.itemDetails.map((detail, ind) => {
              return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {
                "index": val => { return ind; },
                "value": JSON.stringify,
                "textContent": JSON.stringify
                });
            }).join("\\n")}\n`;
          }  catch (ex) {
              logger.error("Ошибка при формировании JSON представления:", ex);
              return '';
        }
    }

    window.addEventListener("load", function() {
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            if (results) {
                relatedTabId = results.tabId;
                relatedFrameId = results.frameId;
                executionId = results.executionId;
                expoTextElement.setAttribute(
                  "download", `tryxpath-${results.title}.txt`);
                expoTextElement.href =  makeTextDownloadUrl(makeInfoText(results));
                expoPartConvElement.setAttribute(
                  "download", `tryxpath-converted-${results.title}.txt`);
                expoPartConvElement.href =  makeTextDownloadUrl(
                  makeConvertedInfoText(results));
                showAllResults(results);
            }
        }).catch(fu.onError);


        contDetail.addEventListener("click", function(event) {
            var target = event.target;
            if (target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId
                }, {
                    "frameId": relatedFrameId
                });
            }
        });


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
                });
            }
        });
    });

})(window);