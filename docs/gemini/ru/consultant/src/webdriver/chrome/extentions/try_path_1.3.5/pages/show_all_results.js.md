# Анализ кода модуля `show_all_results.js`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и понятен.
    - Используются константы для ключей и заголовков таблиц.
    - Функции четко выполняют свои задачи.
    - Обработка ошибок присутствует (через `catch(fu.onError)`).
    - Есть экспорт результатов в текстовом виде.
- Минусы
    - Не хватает docstring для функций и переменных.
    - Стандартные блоки `try-except` не используются, но `fu.onError` выполняет ту же функцию, хотя это не совсем явно.
    - Некоторые имена переменных могли бы быть более выразительными.
    - Не используется `logger` для записи ошибок и отладочной информации.
    - Не все функции документированы в формате RST.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  **Документирование**: Добавить docstring в формате RST для всех функций, переменных и модуля.
2.  **Логирование**: Заменить `fu.onError` на использование `logger.error` для более гибкого и подробного логирования ошибок.
3.  **Именование**: Пересмотреть имена переменных для большей ясности, если это необходимо.
4.  **Импорты**: Убедиться, что все необходимые импорты присутствуют, в данном случае это `logger` из `src.logger.logger`.
5.  **Обработка ошибок**: Вместо `catch(fu.onError)` использовать `try-except` с логированием через `logger.error`.
6.  **JSON**:  Не требуется использовать `j_loads` или `j_loads_ns` так как не происходит загрузка `json` из файла.
7.  **Общая структура**: Убедиться, что все функции и переменные следуют общему стилю кодирования.

**Оптимизированный код**

```python
"""
Модуль для отображения результатов XPath запросов
=========================================================================================

Этот модуль отвечает за отображение результатов XPath запросов в пользовательском интерфейсе.
Он получает результаты через сообщения от расширения браузера и отображает их в виде таблиц и текстовых выгрузок.
Модуль также обеспечивает интерактивность, позволяя пользователю фокусироваться на конкретных элементах на странице.

Пример использования
--------------------

Модуль подключается к HTML странице и получает данные через `browser.runtime.sendMessage`.
Результаты отображаются в таблицах и текстовых блоках, а также предоставляется возможность
экспорта в текстовый файл.

"""
from src.logger.logger import logger # Добавлен импорт logger

(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    # Список ключей для деталей
    var detailKeys = ["type", "name", "value", "textContent"];
    # Заголовки для таблицы деталей
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;

    /**
     * Отображает все результаты XPath запроса на странице.
     *
     * @param {Object} results Объект с результатами запроса, включая сообщения, заголовки, URL, и детали.
     *
     * Структура `results` :
     * {
     *   message: string,
     *   title: string,
     *   href: string,
     *   frameId: number,
     *   context: {
     *     method: string,
     *     expression: string,
     *     specifiedResultType: string,
     *     resultType: string,
     *     resolver: string,
     *     itemDetail: object
     *    },
     *    main: {
     *      method: string,
     *      expression: string,
     *      specifiedResultType: string,
     *      resultType: string,
     *      resolver: string,
     *      itemDetails: array
     *    }
     * }
     *
     * @returns {void}
     */
    function showAllResults(results) {
        document.getElementById("message").textContent = results.message;
        document.getElementById("title").textContent = results.title;
        document.getElementById("url").textContent = results.href;
        document.getElementById("frame-id").textContent = results.frameId;

        if (results.context) {
            let cont = results.context;
            document.getElementById("context-method").textContent
                = cont.method;
            document.getElementById("context-expression").textContent
                = cont.expression;
            document.getElementById("context-specified-result-type")
                .textContent
                = cont.specifiedResultType;
            document.getElementById("context-result-type").textContent
                = cont.resultType;
            document.getElementById("context-resolver").textContent
                = cont.resolver;
            let contTbody = document.getElementById("context-detail")
                .getElementsByTagName("tbody")[0];
            if (cont.itemDetail) {
                # Обновление таблицы с деталями контекста
                fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                    "headerValues": headerValues,
                    "detailKeys": detailKeys
                }).catch(err => logger.error('Ошибка при обновлении таблицы деталей контекста', err)); # Заменено fu.onError на logger.error
            }
        } else {
            # Удаление области контекста, если она не существует
            let area = document.getElementById("context-area");
            area.parentNode.removeChild(area);
        }

        var main = results.main;
        document.getElementById("main-method").textContent = main.method;
        document.getElementById("main-expression").textContent
            = main.expression;
        document.getElementById("main-specified-result-type").textContent
            = main.specifiedResultType;
        document.getElementById("main-result-type").textContent
            = main.resultType;
        document.getElementById("main-resolver").textContent = main.resolver;
        document.getElementById("main-count").textContent
            = main.itemDetails.length;
        var mainTbody = document.getElementById("main-details")
            .getElementsByTagName("tbody")[0];
        # Обновление основной таблицы с деталями
        fu.updateDetailsTable(mainTbody, main.itemDetails, {
            "headerValues": headerValues,
            "detailKeys": detailKeys
        }).catch(err => logger.error('Ошибка при обновлении основной таблицы деталей', err)); # Заменено fu.onError на logger.error
    };

    /**
     * Создает URL для скачивания текстового содержимого.
     *
     * @param {string} text Текст для скачивания.
     * @returns {string} URL для скачивания.
     */
    function makeTextDownloadUrl(text) {
        return URL.createObjectURL(new Blob([text], { "type": "text/plain"}));
    };

    /**
     * Формирует текстовое представление информации о результатах.
     *
     * @param {Object} results Объект с результатами запроса.
     * @returns {string} Текстовое представление результатов.
     */
    function makeInfoText(results) {
        let cont = results.context;
        let main = results.main;
        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression:              ${cont.expression}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\n${headerValues.join(", ")}\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ")}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression:              ${main.expression}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\n${["Index"].concat(headerValues).join(", ")}\n${main.itemDetails.map((detail, ind) => {\n      return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {\n          "index": val => { return ind; }\n      });\n  }).join("\\n")}\n`;
    };

    /**
     * Формирует текстовое представление информации о результатах с преобразованием JSON.
     *
     * @param {Object} results Объект с результатами запроса.
     * @returns {string} Текстовое представление результатов с JSON преобразованием.
     */
    function makeConvertedInfoText(results) {
        let cont = results.context;
        let main = results.main;
        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression(JSON):        ${JSON.stringify(cont.expression)}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\n${fu.makeDetailText(cont.itemDetail, detailKeys, ", ", {\n    "value": JSON.stringify,\n    "textContent": JSON.stringify\n})}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression(JSON):        ${JSON.stringify(main.expression)}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n${main.itemDetails.map((detail, ind) => {\n      return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {\n          "index": val => { return ind; },\n          "value": JSON.stringify,\n          "textContent": JSON.stringify\n      });\n  }).join("\\n")}\n`;
    };

    # Обработчик события загрузки страницы
    window.addEventListener("load", function() {
        # Отправка сообщения для получения результатов
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            if (results) {
                relatedTabId = results.tabId;
                relatedFrameId = results.frameId;
                executionId = results.executionId;

                let expoText = document.getElementById("export-text");
                expoText.setAttribute(
                    "download", `tryxpath-${results.title}.txt`);
                expoText.href =  makeTextDownloadUrl(makeInfoText(results));
                let expoPartConv = document.getElementById(
                    "export-partly-converted");
                expoPartConv.setAttribute(
                    "download", `tryxpath-converted-${results.title}.txt`);
                expoPartConv.href =  makeTextDownloadUrl(
                    makeConvertedInfoText(results));
                # Отображение результатов на странице
                showAllResults(results);
            }
        }).catch(err => logger.error('Ошибка при получении и отображении результатов', err)); # Заменено fu.onError на logger.error

        # Обработчик клика на таблице контекста
        var contDetail = document.getElementById("context-detail");
        contDetail.addEventListener("click", function(event) {
            var target = event.target;
            if (target.tagName.toLowerCase() === "button") {
                # Отправка сообщения для фокусировки на элементе контекста
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId
                }, {
                    "frameId": relatedFrameId
                }).catch(err => logger.error('Ошибка при отправке сообщения для фокусировки на элементе контекста', err)); # Добавлено логирование ошибки
            }
        });

        # Обработчик клика на основной таблице
        var mainDetails = document.getElementById("main-details");
        mainDetails.addEventListener("click", function(event) {
            var target = event.target;
            if (target.tagName.toLowerCase() === "button") {
                let ind = parseInt(target.getAttribute("data-index"), 10);
                # Отправка сообщения для фокусировки на элементе основной таблицы
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                    "executionId": executionId,
                    "index": ind
                }, {
                    "frameId": relatedFrameId
                }).catch(err => logger.error('Ошибка при отправке сообщения для фокусировки на элементе основной таблицы', err)); # Добавлено логирование ошибки
            }
        });
    });

})(window);
```