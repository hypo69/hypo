## АНАЛИЗ КОДА: `show_all_results.js`

### 1. <алгоритм>

1.  **Инициализация:**
    *   Скрипт начинается с анонимной самовызывающейся функции, передавая `window` в качестве параметра. Это ограничивает область видимости переменных.
    *   Создаются псевдонимы `tx` для `tryxpath` и `fu` для `tryxpath.functions`.
    *   Получается ссылка на объект `document` из `window`.
    *   Определяются массивы `detailKeys` (ключи деталей) и `headerValues` (значения заголовков).
    *   Объявляются переменные `relatedTabId`, `relatedFrameId` и `executionId`, которые будут использоваться для передачи информации о текущей вкладке и выполнении.

    *Пример:*
    ```javascript
    var tx = tryxpath;
    var fu = tryxpath.functions;
    var document = window.document;
    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId; // undefined
    var relatedFrameId; // undefined
    var executionId;  // undefined
    ```

2.  **`showAllResults(results)` Function:**
    *   Эта функция принимает объект `results`, содержащий результаты XPath запроса.
    *   Обновляет текстовое содержимое HTML-элементов (message, title, url, frame-id) значениями из `results`.
    *   Обрабатывает контекст (context) результатов. Если контекст существует:
        *   Обновляет HTML-элементы (context-method, context-expression и т. д.) с данными из контекста.
        *   Обновляет таблицу деталей контекста (context-detail) с помощью функции `fu.updateDetailsTable` с использованием `itemDetail`.
        *   Если контекста нет, удаляет элемент `context-area` из DOM.
    *   Обрабатывает основные (main) результаты:
        *   Обновляет HTML-элементы (main-method, main-expression и т. д.) с данными из `main`.
        *   Обновляет таблицу деталей основных результатов (main-details) с помощью функции `fu.updateDetailsTable` с использованием `itemDetails`.
   
    *Пример:*
    ```javascript
     let results = {
        message: "XPath query successful",
        title: "Example Page",
        href: "https://example.com",
        frameId: 0,
        context: {
            method: "evaluate",
            expression: "/html/body/div",
            specifiedResultType: 9,
            resultType: 4,
            resolver: null,
            itemDetail: {
                type: "DIV",
                name: "",
                value: "...",
                textContent: "Hello"
            }
        },
        main: {
            method: "evaluate",
            expression: "//p",
            specifiedResultType: 7,
            resultType: 1,
            resolver: null,
            itemDetails: [
                {type: "P", name: "", value: "...", textContent: "Paragraph 1"},
                {type: "P", name: "", value: "...", textContent: "Paragraph 2"},
            ]
        }
    };
    showAllResults(results)
    // После выполнения функции, HTML-элементы обновляются
    ```

3.  **`makeTextDownloadUrl(text)` Function:**
    *   Создает URL-адрес для скачивания файла с текстом.
    *   Использует `URL.createObjectURL` и `Blob` для создания временного URL.
   
    *Пример:*
    ```javascript
    let text = "Example download text";
    let downloadUrl = makeTextDownloadUrl(text);
    // downloadUrl = "blob:http://localhost:8080/34e049f6-18d2-4026-a8a3-176b08e40119"
    ```

4.  **`makeInfoText(results)` Function:**
    *   Формирует текстовое представление результатов, включая информацию о контексте и основных результатах.
    *   Использует шаблонные строки для построения текста.
    *   Вызывает `fu.makeDetailText` для форматирования деталей.
   
    *Пример:*
    ```javascript
    let results = {
    ... // результаты из предыдущего примера
    };
    let infoText = makeInfoText(results);
    // infoText = "[Information]\nMessage:     XPath query successful\nTitle:       Example Page\nURL:         https://example.com\nframeId:     0\n\n[Context information]\nMethod:                  evaluate\nExpression:              /html/body/div\nSpecified resultType:    9\nresultType:              4\nResolver:                null\n\n[Context detail]\nType, Name, Value, textContent\nDIV, , ..., Hello\n\n[Main information]\nMethod:                  evaluate\nExpression:              //p\nSpecified resultType:    7\nresultType:              1\nResolver:                null\nCount:                   2\n\n[Main details]\nIndex, Type, Name, Value, textContent\n0, P, , ..., Paragraph 1\n1, P, , ..., Paragraph 2\n"
    ```

5.  **`makeConvertedInfoText(results)` Function:**
    *   Похожа на `makeInfoText`, но преобразует значения `value` и `textContent` в JSON-строку, используя `JSON.stringify`.
    
    *Пример:*
    ```javascript
    let results = {
        ... // результаты из предыдущего примера
    };
    let convertedInfoText = makeConvertedInfoText(results);
    // convertedInfoText = "[Information]\nMessage:     XPath query successful\nTitle:       Example Page\nURL:         https://example.com\nframeId:     0\n\n[Context information]\nMethod:                  evaluate\nExpression(JSON):        "/html/body/div"\nSpecified resultType:    9\nresultType:              4\nResolver:                null\n\n[Context detail]\nType, Name, Value(JSON), textContent(JSON)\nDIV, , "...", "Hello"\n\n[Main information]\nMethod:                  evaluate\nExpression(JSON):        "//p"\nSpecified resultType:    7\nresultType:              1\nResolver:                null\nCount:                   2\n\n[Main details]\nIndex, Type, Name, Value(JSON), textContent(JSON)\n0, P, , "...", "Paragraph 1"\n1, P, , "...", "Paragraph 2"\n"
    ```

6.  **`window.addEventListener("load", ...)` Function:**
    *   Добавляет обработчик события `load`, который выполняется после загрузки страницы.
    *   Отправляет сообщение `browser.runtime.sendMessage({"event":"loadResults"})` для получения результатов.
    *   После получения результатов:
        *   Сохраняет `tabId`, `frameId` и `executionId` из результатов.
        *   Создает URL для скачивания текста (обычного и сконвертированного) и устанавливает их в ссылки на странице.
        *   Вызывает `showAllResults` для отображения результатов на странице.
    *   Добавляет обработчики события `click` для таблиц деталей (контекстной и основной):
        *   При клике на кнопку в таблице, отправляет сообщение `browser.tabs.sendMessage` на вкладку с запросом на фокусировку элемента.
        
    *Пример:*
    ```javascript
    // При загрузке страницы, отправляется сообщение loadResults и
    // обрабатываются результаты
    // При клике на кнопку в таблице деталей (контекстной или основной)
    // отправляется сообщение focusContextItem или focusItem
    ```

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Start: Page Load] --> LoadResults[Send "loadResults" to background script];
    LoadResults --> ReceiveResults{Receive Results?}
    ReceiveResults -- Yes --> StoreInfo[Store tabId, frameId, executionId]
    StoreInfo --> GenerateDownloadUrls[Generate download URLs for text and converted text]
    GenerateDownloadUrls --> DisplayResults[Call showAllResults(results)]
    ReceiveResults -- No --> ErrorHandler[Call fu.onError]
    DisplayResults --> SetupContextClick[Setup click listener for context details table]
    DisplayResults --> SetupMainClick[Setup click listener for main details table]
    SetupContextClick --> ContextClick{Context Details Clicked?}
     ContextClick -- Yes --> SendFocusContextItem[Send "focusContextItem" to tab]
    ContextClick -- No --> SetupMainClick
    SetupMainClick --> MainClick{Main Details Clicked?}
     MainClick -- Yes --> SendFocusItem[Send "focusItem" to tab]
    MainClick -- No --> End[End]
    SendFocusContextItem --> End
    SendFocusItem --> End
    ErrorHandler --> End
  
```

**Объяснение зависимостей:**
*   **`Start`**: Начальная точка, когда страница загружается.
*   **`LoadResults`**: Отправляет сообщение `loadResults` фоновому скрипту для получения данных.
*   **`ReceiveResults`**: Проверяет, получены ли результаты от фонового скрипта.
*   **`StoreInfo`**: Сохраняет полученные `tabId`, `frameId`, и `executionId`.
*   **`GenerateDownloadUrls`**: Генерирует ссылки для скачивания обычного и преобразованного текста, вызывая функции `makeTextDownloadUrl`, `makeInfoText` и `makeConvertedInfoText`.
*   **`DisplayResults`**: Отображает результаты на странице, вызывая функцию `showAllResults`.
*   **`SetupContextClick`**: Устанавливает обработчик клика для таблицы деталей контекста.
*   **`SetupMainClick`**: Устанавливает обработчик клика для таблицы основных деталей.
*  **`ContextClick`**: Проверяет клик по кнопке в контекстной таблице.
*   **`MainClick`**: Проверяет клик по кнопке в основной таблице.
*   **`SendFocusContextItem`**: Отправляет сообщение фокуса контекстного элемента на вкладку, если произошло нажатие на кнопку в контекстной таблице.
*  **`SendFocusItem`**: Отправляет сообщение фокуса основного элемента на вкладку, если произошло нажатие на кнопку в основной таблице.
*  **`ErrorHandler`**: Вызывает `fu.onError` в случае ошибки.
*   **`End`**: Конечная точка выполнения скрипта.

### 3. <объяснение>

**Импорты:**

*   `tryxpath`: Объект `tryxpath`, вероятно, является основным API расширения. Он предоставляет доступ к функциям `functions`.
*   `tryxpath.functions`: Содержит вспомогательные функции, такие как `updateDetailsTable`, `makeDetailText` и `onError`.

**Классы:**

*   В данном коде классы не используются.

**Функции:**

*   `showAllResults(results)`:
    *   **Аргументы**: `results` — объект, содержащий результаты XPath запроса.
    *   **Назначение**: Отображает результаты XPath запроса на HTML-странице. Обновляет текстовые элементы, обрабатывает контекст и основные результаты, обновляет таблицы деталей.
    *   **Возвращает**: `undefined`.

*   `makeTextDownloadUrl(text)`:
    *   **Аргументы**: `text` — текстовая строка, которую нужно скачать.
    *   **Назначение**: Создает URL для скачивания текстового файла.
    *   **Возвращает**: URL-адрес в виде строки.

*   `makeInfoText(results)`:
    *   **Аргументы**: `results` — объект, содержащий результаты XPath запроса.
    *   **Назначение**: Формирует текстовое представление результатов запроса, включая информацию о контексте и основных деталях.
    *   **Возвращает**: Текстовая строка с информацией.

*    `makeConvertedInfoText(results)`:
    *   **Аргументы**: `results` — объект, содержащий результаты XPath запроса.
    *    **Назначение**: Формирует текстовое представление результатов запроса, включая информацию о контексте и основных деталях, при этом значения `value` и `textContent` преобразовываются в JSON.
    *   **Возвращает**: Текстовая строка с информацией.
    
**Переменные:**

*   `tx` : Псевдоним для `tryxpath`.
*   `fu`: Псевдоним для `tryxpath.functions`.
*   `document`: Ссылка на объект `document` текущей HTML-страницы.
*   `detailKeys`: Массив строк, определяющих ключи для деталей.
*   `headerValues`: Массив строк, определяющих заголовки для таблицы деталей.
*   `relatedTabId`: Идентификатор вкладки, на которой был выполнен XPath запрос.
*   `relatedFrameId`: Идентификатор фрейма, на котором был выполнен запрос.
*   `executionId`: Идентификатор выполнения XPath запроса.
*   `results`: Объект, содержащий результаты XPath запроса (message, title, href, frameId, context, main).
*   `cont`: Объект контекста, содержащий данные контекстного результата.
*   `main`: Объект основных результатов, содержащий массив itemDetails.
*   `expoText`: HTML-элемент ссылки для скачивания обычного текста.
*   `expoPartConv`: HTML-элемент ссылки для скачивания преобразованного текста.
*   `contDetail`: HTML-элемент таблицы контекстных деталей.
*   `mainDetails`: HTML-элемент таблицы основных деталей.
*   `target`: HTML-элемент, на котором произошло событие click.
*   `ind`: Индекс выбранного элемента в основной таблице.

**Потенциальные ошибки или области для улучшения:**

*   **Обработка ошибок:** Используется общая функция `fu.onError`, но не предоставляется конкретной обработки ошибок на уровне этой страницы, можно добавить логирование или уведомления об ошибках.
*   **Необходимо проверять валидность данных**: Проверять наличие полей `cont` и `itemDetail` в `results` перед их использованием, чтобы избежать ошибок.
*   **Упрощение HTML-обновления**: Вместо многократного обращения к `document.getElementById`, можно кэшировать элементы DOM.
*   **Разделение логики**: Логика формирования текста для скачивания можно вынести в отдельный модуль.

**Цепочка взаимосвязей с другими частями проекта:**

*   **`tryxpath`**: Ядро расширения.
*   **Фоновый скрипт**: Взаимодействие через `browser.runtime.sendMessage` для получения результатов.
*   **Вкладка**: Взаимодействие через `browser.tabs.sendMessage` для фокусировки элементов.
*   **Функции `tryxpath.functions`**: Используются для обновления таблиц и преобразования текста.

В целом, скрипт отвечает за отображение результатов XPath запроса на странице и обеспечение взаимодействия с элементами на веб-странице. Он использует асинхронные вызовы для получения данных от фонового скрипта и отправки сообщений на вкладку.