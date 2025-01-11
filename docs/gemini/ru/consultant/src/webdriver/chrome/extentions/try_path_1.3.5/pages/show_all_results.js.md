# Анализ кода модуля `show_all_results.js`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, используются функции для разделения логики.
    - Присутствуют комментарии, объясняющие назначение переменных и блоков кода.
    - Используются `addEventListener` для обработки событий.
    - Код адаптирован для работы с расширениями браузера.
-  Минусы
    - Отсутствует документация в формате RST для функций и переменных.
    - Используется устаревший синтаксис `var` вместо `let` и `const` (частично исправлено).
    - Отсутствует обработка ошибок внутри функций, вместо этого используется `fu.onError`.
    - Использование `JSON.stringify` для `value` и `textContent` в `makeConvertedInfoText` может быть не оптимальным, если данные уже являются строками.

**Рекомендации по улучшению**

1.  **Добавить документацию:**
    - Добавить docstring в формате RST к каждой функции для описания её назначения, параметров и возвращаемых значений.
2.  **Использовать `let` и `const`:**
    - Заменить `var` на `let` для переменных, значения которых могут изменяться, и на `const` для констант.
3.  **Обработка ошибок:**
    - Заменить `fu.onError` на явную обработку ошибок с использованием `logger.error` для более точного логирования.
4.  **Улучшить форматирование:**
    - Сделать код более читаемым, добавив пробелы и пустые строки для разделения логических блоков.
5.  **Оптимизация `makeConvertedInfoText`:**
    - Проверить необходимость использования `JSON.stringify` для `value` и `textContent`, если они и так строки, то можно его убрать.
6.  **Добавить импорт `logger`:**
    -  Импортировать `logger` из `src.logger.logger`.

**Оптимизированный код**

```python
"""
Модуль для отображения результатов XPath запросов.
=========================================================================================

Этот модуль отвечает за отображение результатов выполнения XPath запросов, полученных из расширения браузера.
Он обрабатывает данные, форматирует их и отображает в HTML-странице, а также предоставляет
возможность экспорта результатов в текстовые файлы.

"""

from src.logger.logger import logger # Импорт logger


(function (window, undefined) {
    "use strict";

    # alias
    const tx = tryxpath; # Используем const для неизменяемых переменных
    const fu = tryxpath.functions; # Используем const для неизменяемых переменных

    const document = window.document; # Используем const для неизменяемых переменных

    const detailKeys = ["type", "name", "value", "textContent"]; # Используем const для неизменяемых переменных
    const headerValues = ["Type", "Name", "Value", "textContent"]; # Используем const для неизменяемых переменных
    let relatedTabId; # Используем let так как значение может меняться
    let relatedFrameId; # Используем let так как значение может меняться
    let executionId; # Используем let так как значение может меняться

    /**
     * Отображает результаты XPath запроса на странице.
     *
     * @param {object} results - Объект с результатами запроса.
     * @param {string} results.message - Сообщение.
     * @param {string} results.title - Заголовок.
     * @param {string} results.href - URL.
     * @param {number} results.frameId - ID фрейма.
     * @param {object} results.context - Контекстные данные.
     * @param {object} results.main - Основные данные.
     *
     */
    function showAllResults(results) {
        document.getElementById("message").textContent = results.message;
        document.getElementById("title").textContent = results.title;
        document.getElementById("url").textContent = results.href;
        document.getElementById("frame-id").textContent = results.frameId;

        if (results.context) {
            const cont = results.context; # Используем const для неизменяемых переменных
            document.getElementById("context-method").textContent = cont.method;
            document.getElementById("context-expression").textContent = cont.expression;
            document.getElementById("context-specified-result-type").textContent = cont.specifiedResultType;
            document.getElementById("context-result-type").textContent = cont.resultType;
            document.getElementById("context-resolver").textContent = cont.resolver;
            const contTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0]; # Используем const для неизменяемых переменных
            if (cont.itemDetail) {
                fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                    "headerValues": headerValues,
                    "detailKeys": detailKeys
                }).catch(error => logger.error("Ошибка при обновлении таблицы деталей контекста", error)); # Используем стрелочную функцию и logger.error
            }
        } else {
            const area = document.getElementById("context-area"); # Используем const для неизменяемых переменных
            area.parentNode.removeChild(area);
        }

        const main = results.main; # Используем const для неизменяемых переменных
        document.getElementById("main-method").textContent = main.method;
        document.getElementById("main-expression").textContent = main.expression;
        document.getElementById("main-specified-result-type").textContent = main.specifiedResultType;
        document.getElementById("main-result-type").textContent = main.resultType;
        document.getElementById("main-resolver").textContent = main.resolver;
        document.getElementById("main-count").textContent = main.itemDetails.length;
        const mainTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0]; # Используем const для неизменяемых переменных
        fu.updateDetailsTable(mainTbody, main.itemDetails, {
            "headerValues": headerValues,
            "detailKeys": detailKeys
        }).catch(error => logger.error("Ошибка при обновлении таблицы основных деталей", error)); # Используем стрелочную функцию и logger.error
    };

    /**
     * Создает URL для скачивания текстового файла.
     *
     * @param {string} text - Текст для скачивания.
     * @returns {string} URL для скачивания файла.
     */
    function makeTextDownloadUrl(text) {
        return URL.createObjectURL(new Blob([text], { "type": "text/plain"}));
    };

    /**
     * Создает текстовое представление результатов запроса.
     *
     * @param {object} results - Объект с результатами запроса.
     * @returns {string} Текстовое представление результатов.
     */
    function makeInfoText(results) {
        const cont = results.context; # Используем const для неизменяемых переменных
        const main = results.main; # Используем const для неизменяемых переменных
        return `[Information]
Message:     ${results.message}
Title:       ${results.title}
URL:         ${results.href}
frameId:     ${results.frameId}

${!cont ? "" : `[Context information]
Method:                  ${cont.method}
Expression:              ${cont.expression}
Specified resultType:    ${cont.specifiedResultType}
resultType:              ${cont.resultType}
Resolver:                ${cont.resolver}

[Context detail]
${headerValues.join(", ")}
${fu.makeDetailText(cont.itemDetail, detailKeys, ", ")}
`}
[Main information]
Method:                  ${main.method}
Expression:              ${main.expression}
Specified resultType:    ${main.specifiedResultType}
resultType:              ${main.resultType}
Resolver:                ${main.resolver}
Count:                   ${main.itemDetails.length}

[Main details]
${["Index"].concat(headerValues).join(", ")}
${main.itemDetails.map((detail, ind) => {
      return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {
          "index": val => { return ind; }
      });
  }).join("\\n")}
`;
    };

    /**
     * Создает текстовое представление результатов запроса с преобразованными данными в JSON.
     *
     * @param {object} results - Объект с результатами запроса.
     * @returns {string} Текстовое представление результатов с JSON преобразованиями.
     */
    function makeConvertedInfoText(results) {
        const cont = results.context; # Используем const для неизменяемых переменных
        const main = results.main; # Используем const для неизменяемых переменных
        return `[Information]
Message:     ${results.message}
Title:       ${results.title}
URL:         ${results.href}
frameId:     ${results.frameId}

${!cont ? "" : `[Context information]
Method:                  ${cont.method}
Expression(JSON):        ${JSON.stringify(cont.expression)}
Specified resultType:    ${cont.specifiedResultType}
resultType:              ${cont.resultType}
Resolver:                ${cont.resolver}

[Context detail]
Type, Name, Value(JSON), textContent(JSON)
${fu.makeDetailText(cont.itemDetail, detailKeys, ", ", {
    "value": JSON.stringify,
    "textContent": JSON.stringify
})}
`}
[Main information]
Method:                  ${main.method}
Expression(JSON):        ${JSON.stringify(main.expression)}
Specified resultType:    ${main.specifiedResultType}
resultType:              ${main.resultType}
Resolver:                ${main.resolver}
Count:                   ${main.itemDetails.length}

[Main details]
Index, Type, Name, Value(JSON), textContent(JSON)
${main.itemDetails.map((detail, ind) => {
      return fu.makeDetailText(detail, ["index"].concat(detailKeys), ", ", {
          "index": val => { return ind; },
          "value": JSON.stringify,
          "textContent": JSON.stringify
      });
  }).join("\\n")}
`;
    };

    window.addEventListener("load", function() {
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            if (results) {
                relatedTabId = results.tabId;
                relatedFrameId = results.frameId;
                executionId = results.executionId;

                const expoText = document.getElementById("export-text"); # Используем const для неизменяемых переменных
                expoText.setAttribute("download", `tryxpath-${results.title}.txt`);
                expoText.href = makeTextDownloadUrl(makeInfoText(results));
                const expoPartConv = document.getElementById("export-partly-converted"); # Используем const для неизменяемых переменных
                expoPartConv.setAttribute("download", `tryxpath-converted-${results.title}.txt`);
                expoPartConv.href = makeTextDownloadUrl(makeConvertedInfoText(results));

                showAllResults(results);
            }
        }).catch(error => logger.error("Ошибка при получении результатов", error)); # Используем стрелочную функцию и logger.error

        const contDetail = document.getElementById("context-detail"); # Используем const для неизменяемых переменных
        contDetail.addEventListener("click", function(event) {
            const target = event.target; # Используем const для неизменяемых переменных
            if (target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId
                }, {
                    "frameId": relatedFrameId
                });
            }
        });

        const mainDetails = document.getElementById("main-details"); # Используем const для неизменяемых переменных
        mainDetails.addEventListener("click", function(event) {
            const target = event.target; # Используем const для неизменяемых переменных
            if (target.tagName.toLowerCase() === "button") {
                const ind = parseInt(target.getAttribute("data-index"), 10); # Используем const для неизменяемых переменных
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