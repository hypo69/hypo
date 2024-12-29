## <алгоритм>

1. **Инициализация**:
   - При загрузке страницы (`window.addEventListener("load", function() { ... })`):
     - Отправляется сообщение `loadResults` в `browser.runtime`.
     - Получаются данные `results` (объект с информацией о результатах XPath).
     - Сохраняются `relatedTabId`, `relatedFrameId`, и `executionId` из `results`.

2. **Обработка данных результатов**:
   - **Создание ссылок для скачивания текстовых файлов**:
     - Создаются ссылки для скачивания текстовых представлений результатов:
       - `export-text`: обычный текст (`makeInfoText(results)`).
       - `export-partly-converted`: частично преобразованный текст с JSON (`makeConvertedInfoText(results)`).
   - **Отображение данных**:
     - Вызывается функция `showAllResults(results)` для отображения результатов на странице:
       - Заполняются поля HTML элементами: `message`, `title`, `url`, `frame-id`, `context-*`, `main-*` на основе `results`.
       - Обновляется таблица деталей контекста (`context-detail`) и таблицы основных результатов (`main-details`).

3. **Обработка кликов по кнопкам в таблицах**:
   - **Контекстная таблица (`context-detail`)**:
     - Устанавливается обработчик клика.
     - При клике на `<button>` отправляется сообщение `focusContextItem` в `browser.tabs` с `relatedTabId` и `relatedFrameId`, `executionId`.
   - **Основная таблица результатов (`main-details`)**:
     - Устанавливается обработчик клика.
     - При клике на `<button>`:
       - Извлекается индекс элемента из атрибута `data-index`.
       - Отправляется сообщение `focusItem` в `browser.tabs` с `relatedTabId`, `relatedFrameId`, `executionId` и `index`.

4. **Функции**:
   - **`showAllResults(results)`**:
     - Получает объект `results` (содержит message, title, url, frameId, context, main).
     - Отображает данные из `results` в HTML элементах на странице.
     - Обновляет таблицы с деталями контекста и основными результатами.
     - **Пример**: `results` может содержать: `{ message: "XPath found 3 elements", title: "Example page", href: "http://example.com", frameId: 0, context: { method: "evaluate", expression: "/html", ... }, main: { method: "evaluate", expression: "//div", itemDetails: [ { type: "ELEMENT_NODE", name: "DIV", value: "<div/>", textContent: "" } ] } }`
   - **`makeTextDownloadUrl(text)`**:
     - Создает URL для скачивания текстового содержимого.
     - Возвращает `URL.createObjectURL(new Blob([text], { "type": "text/plain"}));`
   - **`makeInfoText(results)`**:
     - Создаёт текстовое представление всех данных `results`.
     - Строит текстовые блоки: `[Information]`, `[Context information]`, `[Context detail]`, `[Main information]`, `[Main details]`.
     - Использует `fu.makeDetailText` для форматирования деталей.
     - **Пример**: Создаёт текстовый отчёт, включая все детали элементов.
   - **`makeConvertedInfoText(results)`**:
     - Создаёт текстовое представление данных `results`, но значения элементов  используют `JSON.stringify`.
     - Строит текстовые блоки: `[Information]`, `[Context information]`, `[Context detail]`, `[Main information]`, `[Main details]`.
     - Использует `fu.makeDetailText` для форматирования деталей.
     - **Пример**: Создаёт текстовый отчёт, где `value` и `textContent` представлены в JSON.
   
## <mermaid>
```mermaid
flowchart TD
    A[Start: Window Load Event] --> B{Send Message: "loadResults" to browser.runtime}
    B --> C{Receive: Results from browser.runtime}
    C -- Results Exists --> D[Store: relatedTabId, relatedFrameId, executionId]
    D --> E[Create Download Links: Export Text]
    E --> F[Create Download Links: Export Partly Converted Text]
    F --> G[Call: showAllResults(results)]
    G --> H{Add Listener: Context Detail Table Click}
    H --> I{Add Listener: Main Details Table Click}
     
    C -- Results Does Not Exist --> J[Catch Error with fu.onError]
  
    I -- Click Event --> K{Check Target is Button}
    K -- Yes --> L[Get Index from Button data-index]
    L --> M[Send Message: "focusItem" to browser.tabs]
    M --> N[End]
    K -- No --> N
    
    H -- Click Event --> O{Check Target is Button}
    O -- Yes --> P[Send Message: "focusContextItem" to browser.tabs]
    P --> N
    O -- No --> N
    
    subgraph showAllResults
    SA[showAllResults(results)]-->SB[Set Text Content: message, title, url, frameId]
    SB --> SC{Check: results.context exists?}
    SC -- Yes --> SD[Set Text Content: context-method, context-expression, ..., context-resolver]
    SD --> SE[Update Context Detail Table]
    SC -- No --> SF[Remove: context-area]
    SF --> SG[Set Text Content: main-method, main-expression, ..., main-resolver, count]
    SG --> SH[Update Main Details Table]
    end
    G --> SA
    
    subgraph updateDetailsTable
    UA[updateDetailsTable()] --> UB[Loop through Item Details]
    UB --> UC[Create table rows and cells using detailKeys]
    UC --> UD[Append rows to table]
    end
    SE --> UA
    SH --> UA
```
### Объяснение зависимостей `mermaid`:
-   **`flowchart TD`**: Объявляет диаграмму потока (flowchart) с направлением слева направо (TD).
-   **`Start: Window Load Event`**: Начальная точка, срабатывает при полной загрузке HTML страницы.
-   **`Send Message: "loadResults" to browser.runtime`**: Отправка сообщения для получения данных, связанных с результатами поиска XPath.
-   **`Receive: Results from browser.runtime`**: Получение данных, отправленных из `browser.runtime` (например, из фонового скрипта расширения).
-   **`Store: relatedTabId, relatedFrameId, executionId`**: Сохранение идентификаторов для дальнейшего взаимодействия с браузером.
-   **`Create Download Links: Export Text`**: Создание ссылки для скачивания текстовой версии результатов.
-   **`Create Download Links: Export Partly Converted Text`**: Создание ссылки для скачивания текстовой версии результатов с преобразованными данными (JSON).
-    **`Call: showAllResults(results)`**: Вызов функции для отображения полученных данных на странице.
-   **`Add Listener: Context Detail Table Click`**: Установка прослушивателя событий клика на таблице контекстных деталей.
-   **`Add Listener: Main Details Table Click`**: Установка прослушивателя событий клика на таблице основных деталей.
-   **`Check Target is Button`**: Проверка, был ли клик по кнопке внутри таблицы.
-   **`Get Index from Button data-index`**: Извлечение индекса элемента, на который был сделан клик.
-   **`Send Message: "focusItem" to browser.tabs`**: Отправка сообщения в конкретную вкладку браузера для выделения элемента.
-   **`Send Message: "focusContextItem" to browser.tabs`**: Отправка сообщения в конкретную вкладку браузера для выделения контекстного элемента.
-   **`Catch Error with fu.onError`**: Обработка ошибок, возникающих в процессе выполнения асинхронных операций.
-   **`showAllResults` subgraph**: Изображение внутреннего устройства функции showAllResults
-   **`updateDetailsTable` subgraph**: Изображение внутреннего устройства функции updateDetailsTable

## <объяснение>

### Импорты:
- **`tryxpath`**: Предположительно, это глобальная переменная или объект, предоставляемый средой расширения, содержащий основные функции для работы с XPath.
- **`tryxpath.functions`**:  Объект, содержащий набор вспомогательных функций, таких как `updateDetailsTable`, `onError`, `makeDetailText`, `updateDetailsTable`.

### Классы:
В данном коде нет определения классов. Весь код находится в анонимной самовызывающейся функции.

### Функции:
- **`showAllResults(results)`**:
  - **Аргументы**: `results` - объект, содержащий результаты выполнения XPath-запроса.
  - **Назначение**: Обновляет HTML-элементы на странице данными из `results`. Заполняет текстовые поля и обновляет таблицы деталей.
  - **Пример**:
     ```javascript
     showAllResults({
       message: 'XPath found 3 elements',
       title: 'Test Page',
       href: 'http://example.com',
       frameId: 0,
       context: {
           method: 'evaluate',
           expression: '/html',
           specifiedResultType: 0,
           resultType: 0,
           resolver: null,
            itemDetail: {
               type: "ELEMENT_NODE",
               name: "HTML",
               value: "<html/>",
               textContent: ""
           }
        },
       main: {
         method: 'evaluate',
         expression: '//div',
         specifiedResultType: 7,
         resultType: 7,
         resolver: null,
         itemDetails: [
             { type: "ELEMENT_NODE", name: "DIV", value: "<div/>", textContent: "text1" },
             { type: "ELEMENT_NODE", name: "DIV", value: "<div/>", textContent: "text2" },
         ]
       }
     });
    ```
-   **`makeTextDownloadUrl(text)`**:
    -   **Аргументы**: `text` - строка, которую нужно преобразовать в URL для скачивания.
    -   **Назначение**: Создает URL для скачивания текстового содержимого.
    -   **Возвращаемое значение**:  URL для скачивания как `URL.createObjectURL(new Blob([text], { "type": "text/plain"}));`
    -   **Пример**:
    ```javascript
    const downloadUrl = makeTextDownloadUrl("This is some text to download");
    console.log(downloadUrl); // Output: "blob:http://localhost:8000/some-blob-hash"
    ```
- **`makeInfoText(results)`**:
    - **Аргументы**: `results` - объект с результатами выполнения XPath-запроса.
    - **Назначение**: Формирует текстовое представление `results`, включая контекстную информацию и детали.
    - **Возвращаемое значение**: Строка с текстовой информацией, готовая для скачивания.
    - **Пример**:
    ```javascript
    const text = makeInfoText(results); // results - объект с данными
    console.log(text); // Output: Строка, форматированная как текстовый отчёт
    ```
- **`makeConvertedInfoText(results)`**:
    - **Аргументы**: `results` - объект с результатами выполнения XPath-запроса.
    - **Назначение**:  Формирует текстовое представление `results`, преобразуя `value` и `textContent` в JSON.
    - **Возвращаемое значение**: Строка с текстовой информацией, готовая для скачивания.
    - **Пример**:
        ```javascript
        const text = makeConvertedInfoText(results); // results - объект с данными
        console.log(text); // Output: Строка, форматированная как текстовый отчёт с JSON значениями
        ```

### Переменные:
-   **`tx`**:  Сокращение для `tryxpath`.
-   **`fu`**:  Сокращение для `tryxpath.functions`.
-   **`document`**:  Ссылка на объект `document` текущего окна.
-   **`detailKeys`**:  Массив строк, представляющих ключи для деталей элементов.
-   **`headerValues`**: Массив строк, представляющих заголовки для таблицы деталей элементов.
-   **`relatedTabId`**:  Идентификатор связанной вкладки браузера.
-   **`relatedFrameId`**:  Идентификатор связанного фрейма (если есть).
-    **`executionId`**: Идентификатор текущего выполнения XPath.
### Детали:
-   Код использует асинхронные операции (`browser.runtime.sendMessage().then()`) для получения данных из фонового скрипта расширения.
-   Код обрабатывает события клика на кнопках в таблицах для отправки сообщений в фоновый скрипт с целью выделения элементов.
-   Используется `URL.createObjectURL` для создания URL скачивания текстовых файлов.
-   Функции `makeInfoText` и `makeConvertedInfoText` формируют текстовые представления результатов, с возможностью частичного преобразования в JSON.

### Потенциальные ошибки и области для улучшения:
- **Обработка ошибок**: Код использует `catch(fu.onError)` для обработки ошибок, но не предоставляет конкретного механизма для отображения ошибок пользователю.
- **Зависимости**:  Код сильно зависит от наличия `tryxpath` и его функций. В случае их отсутствия или изменения может возникнуть ошибка.
- **Масштабируемость**: Если структура `results` изменится, потребуется обновлять функции `showAllResults`, `makeInfoText`, `makeConvertedInfoText`.
- **Улучшение**: Добавление более подробной обработки ошибок, модулизация кода, использование шаблонизатора для HTML, возможность настройки форматов вывода.

### Цепочка взаимосвязей с другими частями проекта:
1. **Фоновый скрипт**: Запрашивает выполнение XPath в контенте страницы, возвращает результаты.
2. **`show_all_results.js`**: Получает результаты из фонового скрипта и отображает их на странице.
3. **Контент скрипт**: Обрабатывает сообщения от `show_all_results.js` и выполняет фокусировку на элементах.
4. **`tryxpath.functions`**: Предоставляет утилитарные функции для обработки результатов, форматирования текста и управления таблицами.

В целом, код обеспечивает отображение и экспорт результатов выполнения XPath-запросов, взаимодействуя с фоновым скриптом расширения и контент-скриптами.