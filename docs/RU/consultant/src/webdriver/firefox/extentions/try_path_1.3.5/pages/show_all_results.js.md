# Анализ кода модуля show_all_results.js

**Качество кода**
7
 -  Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    - Используются понятные имена переменных.
    - Присутствует обработка событий `click` для элементов таблицы.
    - Присутствует функция для создания URL для скачивания текста.
 -  Минусы
    - Отсутствуют docstring для функций.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Обработка ошибок `fu.onError` не совсем подходит, лучше использовать `logger.error`.
    - Отсутствуют импорты.
    - Не используются константы для ключей `detailKeys`, `headerValues`.
    - Код использует `var` вместо `const` и `let`.
    -  Используется `document.getElementById` несколько раз, что может быть оптимизировано.

**Рекомендации по улучшению**

1.  Добавить docstring к каждой функции для лучшей читаемости и понимания кода.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `fu.onError` на `logger.error` для более точной обработки ошибок.
4.  Добавить необходимые импорты.
5.  Использовать константы для ключей `detailKeys`, `headerValues`.
6.  Заменить `var` на `const` и `let`.
7.  Оптимизировать повторные вызовы `document.getElementById` путем сохранения ссылок на элементы.
8.  Разделить код на более мелкие функции для улучшения читаемости и поддержки.
9.  Использовать форматирование строк f-string.
10. Добавить комментарии к блокам кода для объяснения их назначения.

**Оптимизированный код**
```python
"""
Модуль для отображения результатов поиска XPath на странице расширения.
======================================================================

Модуль `show_all_results.js` предназначен для отображения результатов выполнения XPath запросов
в расширении браузера. Он получает данные о результатах через сообщение от фонового скрипта и
отображает их в HTML-странице, позволяя пользователю просматривать детали каждого найденного элемента,
экспортировать результаты в текстовый файл, а также подсвечивать выбранные элементы на исходной странице.

Основные возможности модуля:
    - Отображение основных данных запроса (сообщение, заголовок, URL, ID фрейма).
    - Отображение информации о контексте запроса (метод, выражение, тип результата).
    - Отображение деталей найденных элементов в виде таблицы.
    - Экспорт результатов в текстовый файл с форматированием JSON.
    - Подсветка элемента при клике на строку в таблице.

Пример использования
--------------------
Для просмотра результатов, необходимо отправить сообщение `loadResults` из фонового скрипта в этот модуль.
После получения данных, результаты будут отображены на странице.
"""
from src.logger.logger import logger
#   Импорт модуля logger для логирования ошибок

(function (window, undefined) {
    "use strict";
    # Устанавливаем строгий режим для избежания ошибок

    // alias
    const tx = tryxpath;
    #  Объявляем константу tx как сокращение для tryxpath
    const fu = tryxpath.functions;
    # Объявляем константу fu как сокращение для tryxpath.functions

    const document = window.document;
    # Объявляем константу document как ссылку на объект document

    const DETAIL_KEYS = ["type", "name", "value", "textContent"];
    # Объявляем константу DETAIL_KEYS для ключей деталей
    const HEADER_VALUES = ["Type", "Name", "Value", "textContent"];
    # Объявляем константу HEADER_VALUES для заголовков таблицы
    let relatedTabId;
    # Объявляем переменную relatedTabId для хранения ID вкладки
    let relatedFrameId;
    # Объявляем переменную relatedFrameId для хранения ID фрейма
    let executionId;
    # Объявляем переменную executionId для хранения ID выполнения

    /**
     * Функция для отображения всех результатов в HTML.
     *
     * Args:
     *  results (object): Объект с результатами поиска, содержащий message, title, href, frameId,
     *  context и main.
     *
     *  Результаты отображаются в соответствующих элементах HTML страницы.
    */
    function showAllResults(results) {
        # Функция отображает результаты в соответствующих элементах HTML страницы.
        document.getElementById("message").textContent = results.message;
        #  Заполняем элемент message текстом сообщения
        document.getElementById("title").textContent = results.title;
        #  Заполняем элемент title текстом заголовка
        document.getElementById("url").textContent = results.href;
        #  Заполняем элемент url текстом URL
        document.getElementById("frame-id").textContent = results.frameId;
        #  Заполняем элемент frame-id текстом ID фрейма

        if (results.context) {
            #  Проверяем наличие контекстных данных
            const cont = results.context;
            #  Объявляем константу cont как ссылку на контекстные данные
            document.getElementById("context-method").textContent = cont.method;
            #  Заполняем элемент context-method методом контекста
            document.getElementById("context-expression").textContent = cont.expression;
            #  Заполняем элемент context-expression выражением контекста
            document.getElementById("context-specified-result-type").textContent = cont.specifiedResultType;
            #  Заполняем элемент context-specified-result-type типом результата контекста
            document.getElementById("context-result-type").textContent = cont.resultType;
             #  Заполняем элемент context-result-type типом результата
            document.getElementById("context-resolver").textContent = cont.resolver;
            #  Заполняем элемент context-resolver резолвером
            const contTbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0];
            #  Получаем tbody элемента context-detail
            if (cont.itemDetail) {
                 #  Проверяем наличие itemDetail в контексте
                fu.updateDetailsTable(contTbody, [cont.itemDetail], {
                     # Обновляем таблицу деталей контекста
                    "headerValues": HEADER_VALUES,
                    # передаём заголовки таблицы
                    "detailKeys": DETAIL_KEYS
                     # передаём ключи для извлечения данных
                }).catch(error => logger.error("Ошибка при обновлении таблицы деталей контекста", error));
                 #  Перехватываем и логируем ошибку при обновлении таблицы
            }
        } else {
             # Если контекстных данных нет
            const area = document.getElementById("context-area");
             #  Получаем элемент context-area
            area.parentNode.removeChild(area);
             # Удаляем context-area из DOM
        }

        const main = results.main;
         #  Объявляем константу main как ссылку на основные результаты
        document.getElementById("main-method").textContent = main.method;
        #  Заполняем элемент main-method методом
        document.getElementById("main-expression").textContent = main.expression;
        #  Заполняем элемент main-expression выражением
        document.getElementById("main-specified-result-type").textContent = main.specifiedResultType;
        #  Заполняем элемент main-specified-result-type типом результата
        document.getElementById("main-result-type").textContent = main.resultType;
        #  Заполняем элемент main-result-type типом результата
        document.getElementById("main-resolver").textContent = main.resolver;
        #  Заполняем элемент main-resolver резолвером
        document.getElementById("main-count").textContent = main.itemDetails.length;
        #  Заполняем элемент main-count количеством найденных элементов
        const mainTbody = document.getElementById("main-details").getElementsByTagName("tbody")[0];
        # Получаем tbody элемента main-details
        fu.updateDetailsTable(mainTbody, main.itemDetails, {
            # Обновляем таблицу основных деталей
            "headerValues": HEADER_VALUES,
            # передаём заголовки таблицы
            "detailKeys": DETAIL_KEYS
            # передаём ключи для извлечения данных
        }).catch(error => logger.error("Ошибка при обновлении таблицы основных деталей", error));
         #  Перехватываем и логируем ошибку при обновлении таблицы
    }
    /**
     * Функция для создания URL для скачивания текстового файла.
     *
     * Args:
     *   text (str): Текст для сохранения в файл.
     * Returns:
     *   (str): URL для скачивания файла.
     */
    function makeTextDownloadUrl(text) {
        # Функция создаёт URL для скачивания текстового файла.
        return URL.createObjectURL(new Blob([text], { "type": "text/plain"}));
        # Возвращает URL для скачивания файла
    }
    /**
     * Функция для формирования текстовой информации о результатах.
     *
     * Args:
     *   results (object): Объект с результатами поиска.
     * Returns:
     *  (str): Текстовая информация о результатах.
     */
    function makeInfoText(results) {
        # Функция формирует текстовую информацию о результатах.
        const cont = results.context;
        #  Объявляем константу cont как ссылку на контекстные данные
        const main = results.main;
        #  Объявляем константу main как ссылку на основные результаты
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
${HEADER_VALUES.join(", ")}
${fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ", ")}
`}
[Main information]
Method:                  ${main.method}
Expression:              ${main.expression}
Specified resultType:    ${main.specifiedResultType}
resultType:              ${main.resultType}
Resolver:                ${main.resolver}
Count:                   ${main.itemDetails.length}

[Main details]
${["Index"].concat(HEADER_VALUES).join(", ")}
${main.itemDetails.map((detail, ind) => {
      return fu.makeDetailText(detail, ["index"].concat(DETAIL_KEYS), ", ", {
          "index": val => { return ind; }
      });
  }).join("\\n")}
`;
        #  Возвращает отформатированную текстовую информацию о результатах
    }
    /**
     * Функция для формирования текстовой информации о результатах с JSON преобразованием.
     *
     * Args:
     *   results (object): Объект с результатами поиска.
     * Returns:
     *   (str): Текстовая информация о результатах с JSON преобразованием.
     */
    function makeConvertedInfoText(results) {
        # Функция формирует текстовую информацию о результатах с преобразованием в JSON.
        const cont = results.context;
        #  Объявляем константу cont как ссылку на контекстные данные
        const main = results.main;
        #  Объявляем константу main как ссылку на основные результаты
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
${fu.makeDetailText(cont.itemDetail, DETAIL_KEYS, ", ", {
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
      return fu.makeDetailText(detail, ["index"].concat(DETAIL_KEYS), ", ", {
          "index": val => { return ind; },
          "value": JSON.stringify,
          "textContent": JSON.stringify
      });
  }).join("\\n")}
`;
        #  Возвращает отформатированную текстовую информацию о результатах с JSON преобразованием
    }

    window.addEventListener("load", function() {
        # Добавляем слушатель события загрузки окна
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            # Отправляем сообщение loadResults и ждем ответа
            if (results) {
                #  Если есть результаты
                relatedTabId = results.tabId;
                #  Сохраняем ID вкладки
                relatedFrameId = results.frameId;
                #  Сохраняем ID фрейма
                executionId = results.executionId;
                #  Сохраняем ID выполнения

                const expoText = document.getElementById("export-text");
                 #  Получаем элемент export-text
                expoText.setAttribute(
                    # Устанавливаем атрибут download
                    "download", `tryxpath-${results.title}.txt`);
                expoText.href =  makeTextDownloadUrl(makeInfoText(results));
                # Устанавливаем ссылку на скачивание текстовой информации
                const expoPartConv = document.getElementById(
                    # Получаем элемент export-partly-converted
                    "export-partly-converted");
                expoPartConv.setAttribute(
                    #  Устанавливаем атрибут download
                    "download", `tryxpath-converted-${results.title}.txt`);
                expoPartConv.href =  makeTextDownloadUrl(
                     # Устанавливаем ссылку на скачивание JSON информации
                   makeConvertedInfoText(results));
                showAllResults(results);
                # Отображаем результаты
            }
        }).catch(error => logger.error("Ошибка при получении результатов", error));
        #  Перехватываем и логируем ошибку при получении результатов

        const contDetail = document.getElementById("context-detail");
         #  Получаем элемент context-detail
        contDetail.addEventListener("click", function(event) {
            #  Добавляем слушатель события клика по таблице контекстных деталей
            const target = event.target;
            #  Получаем цель клика
            if (target.tagName.toLowerCase() === "button") {
                #  Если цель - кнопка
                browser.tabs.sendMessage(relatedTabId, {
                    # Отправляем сообщение фоновому скрипту для фокуса на элементе
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                    "executionId": executionId
                }, {
                    "frameId": relatedFrameId
                });
            }
        });

        const mainDetails = document.getElementById("main-details");
        #  Получаем элемент main-details
        mainDetails.addEventListener("click", function(event) {
             # Добавляем слушатель события клика по таблице основных деталей
            const target = event.target;
             # Получаем цель клика
            if (target.tagName.toLowerCase() === "button") {
                 # Если цель - кнопка
                const ind = parseInt(target.getAttribute("data-index"), 10);
                #  Получаем индекс элемента
                browser.tabs.sendMessage(relatedTabId, {
                    # Отправляем сообщение фоновому скрипту для фокуса на элементе
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