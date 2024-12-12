## АНАЛИЗ КОДА:

### <алгоритм>

1.  **Инициализация**:
    *   Устанавливаются алиасы `tx` для `tryxpath` и `fu` для `tryxpath.functions`.
    *   Получается объект `document` из `window`.
    *   Определяются массивы `detailKeys` и `headerValues` для отображения данных в таблицах.
    *   Инициализируются переменные `relatedTabId`, `relatedFrameId` и `executionId`.

2.  **Функция `showAllResults(results)`**:
    *   Получает объект `results`, содержащий информацию об XPath-запросе и его результатах.
    *   Обновляет элементы `textContent` для элементов HTML, таких как `message`, `title`, `url`, `frame-id` данными из `results`.
    *   **Обработка `context`**:
        *   Если `results.context` существует, извлекаются его свойства (например, `method`, `expression` и т.д.) и используются для обновления HTML-элементов на странице.
        *   Вызывает `fu.updateDetailsTable` для отображения деталей контекста (`itemDetail`) в таблице.
        *   Если `results.context` не существует, то удаляется элемент `context-area` из DOM.
    *   **Обработка `main`**:
        *   Аналогично `context`, извлекает свойства `main` и обновляет соответствующие HTML-элементы.
        *   Вызывает `fu.updateDetailsTable` для отображения деталей main (`itemDetails`) в таблице.

3.  **Функция `makeTextDownloadUrl(text)`**:
    *   Принимает текстовую строку `text`.
    *   Создаёт объект `Blob` с типом `text/plain`.
    *   Создаёт URL для скачивания из объекта `Blob` и возвращает его.

4.  **Функция `makeInfoText(results)`**:
    *   Формирует текстовое представление данных из объекта `results` для скачивания.
    *   Включает информацию о `message`, `title`, `url`, `frameId`.
    *   Если есть `context`, то добавляет информацию о `context` и его детали.
    *   Добавляет информацию о `main` и его детали, включая индекс каждого элемента.

5.  **Функция `makeConvertedInfoText(results)`**:
    *   Аналогично `makeInfoText(results)`, но данные `value` и `textContent` преобразуются в JSON.

6.  **Событие `window.addEventListener("load", ...)`**:
    *   После загрузки страницы:
        *   Отправляет сообщение `browser.runtime.sendMessage({"event":"loadResults"})` для получения результатов.
        *   При получении `results`:
            *   Сохраняет значения `tabId`, `frameId`, и `executionId`.
            *   Устанавливает атрибуты `download` и `href` для элементов `export-text` и `export-partly-converted`, создавая ссылки для скачивания текстовых файлов.
            *   Вызывает функцию `showAllResults` для отображения полученных данных на странице.
        *   Добавляет слушателей событий `click` к элементам `context-detail` и `main-details`:
            *   При клике на кнопку в таблице (например, "button"):
                *   Отправляет сообщение `browser.tabs.sendMessage` для фокусировки на элементе контекста или на конкретном элементе из `main`.
                *   Передает `executionId` и `index` (для `main`) для последующей обработки.

### <mermaid>

```mermaid
flowchart TD
    Start[Start: window.onload event] --> sendMessage[browser.runtime.sendMessage({"event":"loadResults"})]
    sendMessage --> handleResults{Получены результаты?}
    handleResults -- Да --> setValues[Сохранить: relatedTabId, relatedFrameId, executionId]
    setValues --> createDownloadLinks[Создать ссылки для скачивания]
    createDownloadLinks --> showResults[Вызвать: showAllResults(results)]
    handleResults -- Нет --> onError[Вызвать: fu.onError]
    
    showResults --> updateHTML[Обновить HTML с: results.message, results.title и т.д.]
    updateHTML --> checkContext{Есть ли results.context?}
    checkContext -- Да --> updateContextInfo[Обновить информацию контекста]
    updateContextInfo --> updateContextDetails[Вызвать: fu.updateDetailsTable(context)]
    checkContext -- Нет --> removeContextArea[Удалить: context-area]

    updateContextDetails -- Готово --> updateMainInfo[Обновить информацию: main]
    removeContextArea --> updateMainInfo
    
    updateMainInfo --> updateMainDetails[Вызвать: fu.updateDetailsTable(main)]
    updateMainDetails -- Готово --> addEventListeners[Добавить слушатели click к detail-таблицам]
    
    addEventListeners --> handleContextClick{Клик на кнопке в context?}
    handleContextClick -- Да --> sendContextFocusMessage[browser.tabs.sendMessage (focusContextItem)]
    handleContextClick -- Нет --> handleMainClick{Клик на кнопке в main?}
    
    handleMainClick -- Да --> sendMainFocusMessage[browser.tabs.sendMessage (focusItem)]
    handleMainClick -- Нет --> End[Конец]

    sendContextFocusMessage --> End
    sendMainFocusMessage --> End
        
    subgraph "Функции"
        direction LR
        showAllResults
        makeTextDownloadUrl
        makeInfoText
        makeConvertedInfoText
    end
    
    subgraph "События"
      direction LR
      window.onload
      click_context
      click_main
    end
```

**Зависимости:**

*   **`tryxpath`**:
    *   `var tx = tryxpath;`:  Используется как алиас для доступа к функциональности `tryxpath` (скорее всего, это глобальный объект, предоставленный расширением).
    *   `var fu = tryxpath.functions;`: Используется для доступа к функциям, предоставляемым `tryxpath`.
*   **`window`**:
    *   `var document = window.document;`:  Для доступа к DOM текущей страницы.
    *   `window.addEventListener("load", function() { ... });`:  Для обработки события полной загрузки страницы.
*   **`browser.runtime`**:
    *   `browser.runtime.sendMessage({"event":"loadResults"})`:  Для отправки сообщения расширению с запросом результатов.
*   **`browser.tabs`**:
    *   `browser.tabs.sendMessage(relatedTabId, { ... }, { "frameId": relatedFrameId });`: Для отправки сообщения на вкладку, в которой было выполнено XPath-выражение, с указанием фрейма, в котором это произошло.
*   **`URL`**:
    *   `URL.createObjectURL(new Blob([text], { "type": "text/plain"}));`:  Для создания URL для скачивания текстового файла.
*   **`Blob`**:
    *   `new Blob([text], { "type": "text/plain"})`: Для создания блоба с текстовыми данными.
* **`JSON`**:
    * `JSON.stringify`: Для преобразования данных в JSON формат.

### <объяснение>

**Импорты**:

*   В данном коде нет явных импортов с использованием `import`. Вместо этого, код полагается на глобальные объекты, предоставляемые средой расширения браузера, такие как `tryxpath`, `window`, `browser`, `URL`, `Blob` и `JSON`.

**Классы**:

*   В этом коде нет объявленных классов.

**Функции**:

*   **`showAllResults(results)`**:
    *   **Аргументы**: `results` - объект, содержащий данные о результате XPath-запроса (message, title, url, frameId, context, main).
    *   **Возвращаемое значение**: Нет (функция void).
    *   **Назначение**: Обновляет HTML-элементы на странице с информацией из `results` и отображает таблицы с результатами.
        *   **Пример**:
            ```javascript
            let resultsData = {
                message: "XPath запрос выполнен успешно",
                title: "Результаты XPath",
                href: "https://example.com",
                frameId: 0,
                context: {
                    method: "evaluate",
                    expression: "//div",
                    specifiedResultType: 9,
                    resultType: 8,
                    resolver: null,
                    itemDetail: {
                      type: 'ELEMENT',
                      name: 'div',
                      value: '<div>Example</div>',
                      textContent: 'Example'
                    }
                },
                main: {
                    method: "evaluate",
                    expression: "//div[@class='container']",
                    specifiedResultType: 7,
                    resultType: 9,
                    resolver: null,
                    itemDetails: [{
                        type: 'ELEMENT',
                        name: 'div',
                        value: '<div>Item 1</div>',
                        textContent: 'Item 1'
                      },
                      {
                        type: 'ELEMENT',
                        name: 'div',
                        value: '<div>Item 2</div>',
                        textContent: 'Item 2'
                    }]
                }
            };
            showAllResults(resultsData); // Обновляет страницу с этими данными
            ```

*   **`makeTextDownloadUrl(text)`**:
    *   **Аргументы**: `text` - строка, которую нужно поместить в файл.
    *   **Возвращаемое значение**: URL для скачивания файла.
    *   **Назначение**: Создаёт URL для скачивания текстового файла.
        *   **Пример**:
            ```javascript
            let textData = "Some text for download";
            let downloadUrl = makeTextDownloadUrl(textData); // Возвращает URL для скачивания textData
            ```

*   **`makeInfoText(results)`**:
    *   **Аргументы**: `results` - объект результатов.
    *   **Возвращаемое значение**: Строка с отформатированной текстовой информацией о результатах.
    *   **Назначение**: Форматирует текстовое представление результатов XPath для скачивания.
        *   **Пример**:
            ```javascript
            let resultsData = { // ... some data
             };
            let infoText = makeInfoText(resultsData); // Возвращает отформатированную строку с инфо
            ```

*    **`makeConvertedInfoText(results)`**:
    *    **Аргументы**: `results` - объект результатов.
    *    **Возвращаемое значение**: Строка с отформатированной текстовой информацией о результатах с данными JSON.
    *    **Назначение**: Форматирует текстовое представление результатов XPath для скачивания с данными в формате JSON.
        *   **Пример**:
            ```javascript
            let resultsData = { // ... some data
             };
            let convertedInfoText = makeConvertedInfoText(resultsData); // Возвращает отформатированную строку с инфо
            ```
**Переменные**:

*   `tx`: Алиас для `tryxpath`.
*   `fu`: Алиас для `tryxpath.functions`.
*   `document`: Объект `document` для доступа к DOM.
*   `detailKeys`: Массив строк с ключами для деталей (например, `type`, `name`, `value`, `textContent`).
*   `headerValues`: Массив строк с заголовками для таблиц (например, `Type`, `Name`, `Value`, `textContent`).
*   `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения идентификаторов вкладки, фрейма и идентификатора выполнения текущего XPath-запроса.

**Потенциальные ошибки и области для улучшения**:

*   **Отсутствие обработки ошибок**: Код использует `catch(fu.onError)`, но не предоставляет конкретной обработки ошибок в случае сбоев.
*   **Магические строки**: В коде много магических строк (например, "message", "title", "export-text"), которые было бы лучше вынести в константы.
*   **Зависимость от DOM**: Код очень сильно привязан к DOM-структуре HTML-страницы, что затрудняет его повторное использование.
*   **Недостаточная типизация**: В коде используется слабая типизация JavaScript, что затрудняет понимание типов данных.
*   **Обработка событий**: Код не обрабатывает возможные ошибки при отправке сообщений с `browser.tabs.sendMessage`.
* **Отсутствует проверка `results`:** В коде не происходит никакой проверки, если `results` пришло `null` или `undefined`.

**Цепочка взаимосвязей**:

1.  **Расширение браузера**: Расширение инициирует XPath-запрос в контенте страницы.
2.  **Фоновая страница расширения**: Фоновая страница обрабатывает XPath-запрос и отправляет результаты.
3.  **`show_all_results.js`**: Этот скрипт получает результаты с фоновой страницы через `browser.runtime.sendMessage`, обновляет DOM с результатами, создает ссылки для скачивания и добавляет обработчики событий.
4.  **Контентная страница**: При клике на кнопку в таблице результатов, `show_all_results.js` отправляет сообщение на контентную страницу, чтобы сфокусироваться на элементе на этой странице.

**Взаимодействие с `tryxpath.functions`**:
    *  `fu.updateDetailsTable`: используется для обновления таблицы с деталями на основе переданных данных.
    *  `fu.onError`: используется в блоках `catch` для обработки ошибок.
    *   `fu.makeDetailText`: используется для формирования текстового представления деталей.