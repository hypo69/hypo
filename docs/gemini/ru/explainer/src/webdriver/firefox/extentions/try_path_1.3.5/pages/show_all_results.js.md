## <алгоритм>

1. **Инициализация:**
   - Устанавливаются псевдонимы для `tryxpath` (`tx`) и `tryxpath.functions` (`fu`).
   - Получается ссылка на объект `document` текущего окна.
   - Определяются массивы `detailKeys` и `headerValues` для отображения деталей в таблицах.
   - Объявляются переменные `relatedTabId`, `relatedFrameId`, `executionId` для хранения идентификаторов.

2. **`showAllResults(results)`:**
   - Функция принимает объект `results` с данными для отображения.
   - Заполняет элементы HTML на странице значениями из `results` (сообщение, заголовок, URL, frameId).
   - **Обработка `context`:**
     - Проверяет наличие `results.context`.
     - Если есть, заполняет HTML элементами значениями из `results.context` (метод, выражение, типы результатов, резолвер).
     - Находит `tbody` элемент таблицы `context-detail` и обновляет его данными из `cont.itemDetail` при помощи `fu.updateDetailsTable`.
     - Если `results.context` нет, то удаляет блок `context-area` из DOM.
   - **Обработка `main`:**
     - Заполняет HTML элементами значениями из `results.main` (метод, выражение, типы результатов, резолвер, кол-во элементов).
     - Находит `tbody` элемент таблицы `main-details` и обновляет его данными из `main.itemDetails` при помощи `fu.updateDetailsTable`.

3. **`makeTextDownloadUrl(text)`:**
   - Принимает текст.
   - Создает `Blob` объект из текста.
   - Создает URL для скачивания `Blob` объекта.
   - Возвращает созданный URL.

4. **`makeInfoText(results)`:**
   - Принимает объект `results` с данными.
   - Формирует строку с текстовым представлением данных `results` (сообщение, заголовок, URL, frameId, контекст, главные данные, детали).
   -  Использует `fu.makeDetailText` для форматирования данных деталей.
   - Возвращает сформированную строку.

5.  **`makeConvertedInfoText(results)`:**
   - Принимает объект `results` с данными.
   - Формирует строку с текстовым представлением данных `results`, но значения и текстовое содержимое преобразуется в JSON-формат.
   - Использует `fu.makeDetailText` для форматирования данных деталей.
   - Возвращает сформированную строку.

6.  **Обработчик события `load`:**
   - Добавляется слушатель события `load` на объект `window`.
   - При загрузке страницы отправляет сообщение `loadResults` в фоновый скрипт браузера `browser.runtime.sendMessage`.
   - Обрабатывает ответ (Promise) от фонового скрипта:
     - Сохраняет `tabId`, `frameId` и `executionId` из ответа.
     - Получает элементы экспорта текста и устанавливает значения атрибута `download` и `href` для скачивания.
     - Вызывает `showAllResults` для отображения результатов на странице.
   - Обрабатывает ошибки, возникшие при получении сообщения или при рендеринге страницы.

7.  **Обработчик события `click` для `context-detail`:**
   - Добавляет обработчик события `click` на таблицу `context-detail`.
   - При клике на кнопку (тег `button`) отправляет сообщение `focusContextItem` в фоновый скрипт для фокусировки контекста, передавая `executionId` и `frameId`.

8.  **Обработчик события `click` для `main-details`:**
   - Добавляет обработчик события `click` на таблицу `main-details`.
   - При клике на кнопку (тег `button`):
     - Получает индекс выбранной строки из атрибута `data-index`.
     - Отправляет сообщение `focusItem` в фоновый скрипт для фокусировки элемента, передавая `executionId`, `frameId` и `index`.

**Поток данных:**

```mermaid
flowchart TD
    A[Start: window.addEventListener("load")] --> B{browser.runtime.sendMessage: {"event":"loadResults"}};
    B --> C{Promise: results};
    C -- results --> D[Set IDs and export links];
    D --> E[makeTextDownloadUrl: makeInfoText(results)];
    D --> F[makeTextDownloadUrl: makeConvertedInfoText(results)];
    D --> G[showAllResults(results)];
    C -- error --> H[fu.onError];
    G --> I{context}
        I --yes--> J[Update HTML: cont data]
        J--> K[fu.updateDetailsTable: cont.itemDetail]
        K-->L[update table context-detail]
        I --no--> M[Remove context area]
    G --> N[Update HTML: main data];
    N --> O[fu.updateDetailsTable: main.itemDetails]
        O-->P[update table main-details]
    P-->Q{context-detail.addEventListener("click")}
    Q--click on button-->R{browser.tabs.sendMessage: focusContextItem, executionId, frameId}
    P-->S{main-details.addEventListener("click")}
    S--click on button-->T{get row index}
    T-->U{browser.tabs.sendMessage: focusItem, executionId, frameId, index}
    R-->END
    U-->END
    M-->N
    L-->N
```

## <mermaid>

```mermaid
flowchart TD
    subgraph tryxpath
    A[tryxpath] --> B(tryxpath.functions)
    end

    C[window] --> D[document]
    E[detailKeys: Array]
    F[headerValues: Array]
    G[relatedTabId]
    H[relatedFrameId]
    I[executionId]

    J[showAllResults(results)]
        J --> D
        J --> B
        J --> E
        J --> F
    K[makeTextDownloadUrl(text)]
        K --> L(Blob)
        L --> M(URL.createObjectURL)
    N[makeInfoText(results)]
        N --> B
        N --> E
        N --> F
    O[makeConvertedInfoText(results)]
         O --> B
         O --> E
         O --> F
         O --> JSON.stringify
    P[window.addEventListener("load")]
        P --> Q{browser.runtime.sendMessage: event:"loadResults"}
        Q --> R{Promise<results>}
        R --> G
        R --> H
        R --> I
        R --> K
        R --> N
        R --> O
        R --> J
        R --> S{error:fu.onError}
    T[context-detail.addEventListener("click")]
         T --click on button--> U{browser.tabs.sendMessage: "focusContextItem", executionId, frameId}
         U-->G
         U-->H
    V[main-details.addEventListener("click")]
         V --click on button--> W{browser.tabs.sendMessage: "focusItem", executionId, frameId, index}
         W-->G
         W-->H
         W-->I
```

**Объяснение зависимостей Mermaid:**

- `tryxpath` и `tryxpath.functions`: Код использует псевдонимы `tx` и `fu` для доступа к функциональности библиотеки `tryxpath`. В диаграмме показано, что `tryxpath.functions` является частью `tryxpath`.
- `window` и `document`: Скрипт работает в контексте окна браузера, поэтому использует объекты `window` и `document` для доступа к DOM и другим функциям браузера.
- `detailKeys` и `headerValues`: Массивы строк для обработки табличных данных.
- `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения идентификаторов связанных вкладок, фреймов и выполнения.
- `showAllResults`: Функция для отображения результатов на странице.
- `makeTextDownloadUrl`: Функция для создания URL для скачивания текста.
- `makeInfoText` и `makeConvertedInfoText`: Функции для форматирования текстовой информации с различными вариантами представления данных.
- `window.addEventListener("load")`: Обработчик события загрузки страницы, который устанавливает начальные значения и отправляет сообщение в фоновый скрипт.
- `context-detail.addEventListener("click")` и `main-details.addEventListener("click")`: Обработчики событий клика по таблицам деталей.
- `Blob` и `URL.createObjectURL`: Используются для создания URL для скачивания.
- `JSON.stringify`: Используется для преобразования значений в формат JSON.
- `browser.runtime.sendMessage` и `browser.tabs.sendMessage`: Используются для обмена сообщениями между расширением и фоновым скриптом.

## <объяснение>

**Импорты:**
- В данном коде нет явных импортов модулей. Вместо этого используется глобальный объект `tryxpath` и его свойство `functions`.
- `tryxpath` (как `tx`) и `tryxpath.functions` (как `fu`) являются частью расширения Firefox, что подразумевает использование их API.

**Переменные:**
- `tx` (alias `tryxpath`): Псевдоним для доступа к библиотеке `tryxpath`.
- `fu` (alias `tryxpath.functions`): Псевдоним для доступа к функциям `tryxpath`.
- `document`: Ссылка на объект DOM текущего окна.
- `detailKeys`: Массив строк, содержащий ключи для деталей.
- `headerValues`: Массив строк, содержащий заголовки столбцов для таблиц.
- `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения идентификаторов вкладки, фрейма и выполнения.

**Функции:**

1.  **`showAllResults(results)`:**
    - **Аргументы:**
        - `results`: Объект, содержащий информацию о результатах выполнения XPath запроса (текстовое сообщение, title, URL, frameId, контекст, главные данные) .
    - **Назначение:** Обновляет HTML страницу, отображая результаты.
    - **Пример:**
        ```javascript
        showAllResults({
            message: "XPath executed successfully",
            title: "Example Page",
            href: "https://example.com",
            frameId: 0,
            context: {
                method: "evaluate",
                expression: "/html/body",
                specifiedResultType: 9,
                resultType: 9,
                resolver: null,
                itemDetail: {
                    type: "Element",
                    name: "BODY",
                    value: "[object HTMLBodyElement]",
                    textContent: "..."
                }
            },
            main: {
                method: "evaluate",
                expression: "//div",
                specifiedResultType: 7,
                resultType: 7,
                resolver: null,
                itemDetails: [
                    {type: "Element", name: "DIV", value: "[object HTMLDivElement]", textContent: "..."}
                ]
            }
        });
        ```
2.  **`makeTextDownloadUrl(text)`:**
    - **Аргументы:**
        - `text`: Текст для скачивания.
    - **Возвращает:** URL для скачивания текста.
    - **Назначение:** Создает URL для скачивания текстового контента.
    - **Пример:**
        ```javascript
        let downloadUrl = makeTextDownloadUrl("This is a test text.");
        // downloadUrl будет содержать URL для скачивания этого текста
        ```
3.  **`makeInfoText(results)`:**
    - **Аргументы:**
        - `results`: Объект с результатами запроса.
    - **Возвращает:** Строка с текстовым представлением `results` в формате для экспорта.
    - **Назначение:** Форматирует текстовую информацию, используя `fu.makeDetailText`, для отображения в текстовом файле.
    - **Пример:**
        ```javascript
         let infoText = makeInfoText(results);
         // infoText будет содержать отформатированную строку с данными results
        ```

4.  **`makeConvertedInfoText(results)`:**
    - **Аргументы:**
        - `results`: Объект с результатами запроса.
    - **Возвращает:** Строка с текстовым представлением `results`, где `value` и `textContent` преобразованы в JSON.
    - **Назначение:** Форматирует текстовую информацию, преобразовывая `value` и `textContent` в JSON-формат, для отображения в текстовом файле.
    - **Пример:**
        ```javascript
        let convertedInfoText = makeConvertedInfoText(results);
        // convertedInfoText будет содержать отформатированную строку с данными results с JSON данными
        ```
5.  **`window.addEventListener("load", function() {...})`:**
    - **Аргументы:**
        - `load`: Тип события, которое должно отработать.
        - `function() {...}`: Функция, которая будет выполнена по событию.
    - **Назначение:** Инициализация страницы при загрузке. Запрашивает данные результатов у фонового скрипта,  устанавливает параметры для экспорта и отображает результаты на странице.

**Классы:**
- В данном коде нет явного использования классов.

**Потенциальные ошибки и области для улучшения:**
- **Обработка ошибок:**
   - Код использует `catch(fu.onError)`, что является общей обработкой ошибок. Было бы полезно более детально обрабатывать ошибки для понимания причины и лучшей отладки.
- **Отсутствие проверок:**
  - В коде не хватает проверок на наличие элементов перед их использованием `document.getElementById` (что в случае отсутствия элемента может вызвать ошибку).
- **Разделение ответственности:**
    - Можно разнести  функции  `makeTextDownloadUrl`, `makeInfoText` и `makeConvertedInfoText` в отдельный модуль для лучшей организации кода.

**Взаимосвязи с другими частями проекта:**

- **Фоновый скрипт:** Код взаимодействует с фоновым скриптом расширения для получения данных результатов и отправки команд фокусировки элемента (при клике по таблицам деталей).
- **`tryxpath`:** Использует API `tryxpath` для обработки результатов XPath запросов, вероятно, получая их из фонового скрипта.
- **HTML страницы:** Обновляет DOM, взаимодействуя с HTML элементами для отображения информации.

**В целом,** этот код является частью пользовательского интерфейса расширения, который отображает результаты XPath запросов, позволяет скачивать их в текстовом виде и фокусироваться на элементах в DOM.