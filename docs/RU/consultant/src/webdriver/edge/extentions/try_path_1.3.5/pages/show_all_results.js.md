# Анализ кода модуля show_all_results.js

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем, с четким разделением на функции.
    - Используются осмысленные имена переменных и функций.
    - Код содержит обработку событий для взаимодействия с элементами страницы.
    - Присутствует функциональность для экспорта данных в текстовый файл.
    - Используются `browser.runtime.sendMessage` и `browser.tabs.sendMessage` для обмена сообщениями с расширением.
- Минусы
    - Не хватает обработки ошибок при получении данных от `browser.runtime.sendMessage` и `browser.tabs.sendMessage`.
    - Отсутствует описание модуля и документация к функциям.
    - Используется `catch(fu.onError)`, что может скрыть ошибки. Необходимо использовать `from src.logger.logger import logger` для логирования.
    - Некоторые участки кода можно сделать более лаконичными, например, преобразование данных в текстовый формат.
    - Нет импорта необходимых модулей, в частности `from src.logger.logger import logger`

**Рекомендации по улучшению**

1.  **Добавить описание модуля:**
    - В начале файла добавить описание модуля с использованием docstring.

2.  **Добавить документацию к функциям:**
    - Добавить docstring к каждой функции, описывая ее назначение, параметры и возвращаемые значения.

3.  **Улучшить обработку ошибок:**
    - Заменить `catch(fu.onError)` на использование `logger.error` для логирования ошибок с подробной информацией.

4.  **Оптимизировать код:**
    - Рассмотреть возможность использования более лаконичного синтаксиса для преобразования данных в текст.

5.  **Добавить импорты:**
    - Добавить импорты необходимых модулей, в частности `from src.logger.logger import logger`

6.  **Использовать константы:**
    - Заменить магические строки на константы (например, "Type", "Name", "Value", "textContent").

7. **Улучшить читаемость `makeTextDownloadUrl`**
    - Добавить имя переменной для blob, для улучшения читаемости кода
    - Добавить обработку ошибок если URL не создался

**Оптимизированный код**

```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
/**
 * Модуль для отображения результатов выполнения XPath запросов.
 * =========================================================================================
 *
 * Этот модуль отвечает за отображение результатов XPath запросов, полученных из расширения
 * tryxpath. Он отображает результаты в табличном виде и предоставляет возможность экспорта
 * данных в текстовый файл.
 *
 * Функциональность:
 * - Получение данных от расширения через `browser.runtime.sendMessage`.
 * - Отображение информации о запросе, контексте и найденных элементах.
 * - Экспорт данных в текстовый файл.
 * - Взаимодействие с элементами страницы через `browser.tabs.sendMessage`.
 *
 */
(function (window, undefined) {
    "use strict";
    
    // import logger
    //TODO: from src.logger.logger import logger
    
    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;
    
    // Константы для ключей и заголовков
    var DETAIL_KEYS = ["type", "name", "value", "textContent"];
    var HEADER_VALUES = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;
    
    /**
     * Функция для отображения всех результатов на странице.
     * @param {Object} results - Объект с результатами запроса.
     * @param {string} results.message - Сообщение.
     * @param {string} results.title - Заголовок.
     * @param {string} results.href - URL.
     * @param {string} results.frameId - ID фрейма.
     * @param {Object} results.context - Объект с информацией о контексте.
     * @param {Object} results.main - Объект с основной информацией.
     */
    function showAllResults(results) {
        // устанавливаем текст сообщения
        document.getElementById("message").textContent = results.message;
        // устанавливаем текст заголовка
        document.getElementById("title").textContent = results.title;
        // устанавливаем текст URL
        document.getElementById("url").textContent = results.href;
        // устанавливаем текст frameId
        document.getElementById("frame-id").textContent = results.frameId;
    
        // проверка наличия контекста
        if (results.context) {
            let cont = results.context;
            // устанавливаем метод контекста
            document.getElementById("context-method").textContent = cont.method;
            // устанавливаем выражение контекста
            document.getElementById("context-expression").textContent = cont.expression;
            // устанавливаем тип результата контекста
            document.getElementById("context-specified-result-type").textContent = cont.specifiedResultType;
            // устанавливаем результирующий тип контекста
            document.getElementById("context-result-type").textContent = cont.resultType;
            // устанавливаем резолвер контекста
            document.getElementById("context-resolver").textContent = cont.resolver;
            // получаем tbody элемента контекста
            let contTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0];
             // Проверяем наличие деталей контекста и обновляем таблицу
            if (cont.itemDetail) {
                 // Обновляем таблицу с деталями контекста
                fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                    "headerValues": HEADER_VALUES,
                    "detailKeys": DETAIL_KEYS
                }).catch(function(error) {
                    // Логируем ошибку
                    //TODO: logger.error("Ошибка при обновлении таблицы контекста", error);
                     console.error("Ошибка при обновлении таблицы контекста", error)
                });
            }
        } else {
            // если контекста нет, удаляем область контекста
            let area = document.getElementById("context-area");
            area.parentNode.removeChild(area);
        }
        
        var main = results.main;
         // устанавливаем метод main
        document.getElementById("main-method").textContent = main.method;
         // устанавливаем выражение main
        document.getElementById("main-expression").textContent = main.expression;
         // устанавливаем тип результата main
        document.getElementById("main-specified-result-type").textContent = main.specifiedResultType;
         // устанавливаем результирующий тип main
        document.getElementById("main-result-type").textContent = main.resultType;
         // устанавливаем резолвер main
        document.getElementById("main-resolver").textContent = main.resolver;
         // устанавливаем количество элементов main
        document.getElementById("main-count").textContent = main.itemDetails.length;
        
        // получаем tbody элемента main
        var mainTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0];
        // Обновляем таблицу с деталями main
        fu.updateDetailsTable(mainTbody, main.itemDetails, {
            "headerValues": HEADER_VALUES,
            "detailKeys": DETAIL_KEYS
        }).catch(function(error) {
             // Логируем ошибку
            //TODO: logger.error("Ошибка при обновлении таблицы main", error);
            console.error("Ошибка при обновлении таблицы main", error);
        });
    }
    /**
     * Создает URL для скачивания текстового файла.
     *
     * @param {string} text - Текст для скачивания.
     * @returns {string} URL для скачивания файла.
    */
    function makeTextDownloadUrl(text) {
       try{
           const blob = new Blob([text], { "type": "text/plain"});
            return URL.createObjectURL(blob);
        }catch (error){
            // Логируем ошибку
            //TODO: logger.error("Ошибка при создании URL для скачивания", error);
            console.error("Ошибка при создании URL для скачивания", error)
            return ''
        }
    }
     /**
     * Формирует текстовое представление информации о результатах.
     *
     * @param {Object} results - Объект с результатами запроса.
     * @returns {string} Текстовое представление информации.
     */
    function makeInfoText(results) {
        let cont = results.context;
        let main = results.main;
        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression:              ${cont.expression}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\n${HEADER_VALUES.join(", ")}\n${fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ", ")}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression:              ${main.expression}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\n${["Index"].concat(HEADER_VALUES).join(", ")}\n${main.itemDetails.map((detail, ind) => {
          return fu.makeDetailText(detail, ["index"].concat(DETAIL_KEYS), ", ", {
              "index": val => { return ind; }
          });
      }).join("\\n")}\n`;
    }
    /**
     * Формирует текстовое представление информации о результатах с JSON преобразованием.
     *
     * @param {Object} results - Объект с результатами запроса.
     * @returns {string} Текстовое представление информации с JSON преобразованием.
     */
    function makeConvertedInfoText(results) {
        let cont = results.context;
        let main = results.main;
        return `[Information]\nMessage:     ${results.message}\nTitle:       ${results.title}\nURL:         ${results.href}\nframeId:     ${results.frameId}\n\n${!cont ? "" : `[Context information]\nMethod:                  ${cont.method}\nExpression(JSON):        ${JSON.stringify(cont.expression)}\nSpecified resultType:    ${cont.specifiedResultType}\nresultType:              ${cont.resultType}\nResolver:                ${cont.resolver}\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\n${fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ", ", {
            "value": JSON.stringify,
            "textContent": JSON.stringify
        })}\n`}\n[Main information]\nMethod:                  ${main.method}\nExpression(JSON):        ${JSON.stringify(main.expression)}\nSpecified resultType:    ${main.specifiedResultType}\nresultType:              ${main.resultType}\nResolver:                ${main.resolver}\nCount:                   ${main.itemDetails.length}\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n${main.itemDetails.map((detail, ind) => {
          return fu.makeDetailText(detail, ["index"].concat(DETAIL_KEYS), ", ", {
              "index": val => { return ind; },
              "value": JSON.stringify,
              "textContent": JSON.stringify
          });
      }).join("\\n")}\n`;
    }

    window.addEventListener("load", function() {
         // Отправляем сообщение для получения результатов
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            if (results) {
                relatedTabId = results.tabId;
                relatedFrameId = results.frameId;
                executionId = results.executionId;
                // получаем элемент для экспорта текста
                let expoText = document.getElementById("export-text");
                // устанавливаем атрибут download для экспорта текста
                expoText.setAttribute("download", `tryxpath-${results.title}.txt`);
                // устанавливаем href для экспорта текста
                expoText.href = makeTextDownloadUrl(makeInfoText(results));
                // получаем элемент для экспорта частично преобразованного текста
                let expoPartConv = document.getElementById("export-partly-converted");
                 // устанавливаем атрибут download для экспорта частично преобразованного текста
                expoPartConv.setAttribute("download", `tryxpath-converted-${results.title}.txt`);
                 // устанавливаем href для экспорта частично преобразованного текста
                expoPartConv.href = makeTextDownloadUrl(makeConvertedInfoText(results));
               // отображаем все результаты
                showAllResults(results);
            }
        }).catch(function(error) {
            // Логируем ошибку
            //TODO: logger.error("Ошибка при получении результатов из background", error);
            console.error("Ошибка при получении результатов из background", error);
        });
        
        var contDetail = document.getElementById("context-detail");
        contDetail.addEventListener("click", function(event) {
            var target = event.target;
            // Проверяем, что клик был по кнопке
            if (target.tagName.toLowerCase() === "button") {
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId
                }, {
                    "frameId": relatedFrameId
                }).catch(function(error) {
                    // Логируем ошибку
                    //TODO: logger.error("Ошибка при отправке сообщения focusContextItem", error);
                    console.error("Ошибка при отправке сообщения focusContextItem", error);
                });;
            }
        });
        
        var mainDetails = document.getElementById("main-details");
        mainDetails.addEventListener("click", function(event) {
            var target = event.target;
             // Проверяем, что клик был по кнопке
            if (target.tagName.toLowerCase() === "button") {
                let ind = parseInt(target.getAttribute("data-index"), 10);
                browser.tabs.sendMessage(relatedTabId, {
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                    "executionId": executionId,
                    "index": ind
                }, {
                    "frameId": relatedFrameId
                }).catch(function(error) {
                    // Логируем ошибку
                    //TODO: logger.error("Ошибка при отправке сообщения focusItem", error);
                    console.error("Ошибка при отправке сообщения focusItem", error);
                });
            }
        });
    });

})(window);