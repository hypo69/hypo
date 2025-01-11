## Анализ кода `show_all_results.js`

### 1. <алгоритм>

**Пошаговая блок-схема:**

1. **Инициализация:**
   -  Объявляются переменные: `tx` (алиас для `tryxpath`), `fu` (алиас для `tryxpath.functions`), `document` (ссылка на объект `document`), `detailKeys` (массив ключей деталей), `headerValues` (массив заголовков таблицы), `relatedTabId`, `relatedFrameId`, `executionId`.
   
   _Пример_:
     - `tx` = `tryxpath`
     - `fu` = `tryxpath.functions`
     - `detailKeys` = `["type", "name", "value", "textContent"]`
     - `headerValues` = `["Type", "Name", "Value", "textContent"]`
    
2.  **`showAllResults(results)` Function:**
    -   Устанавливает текст для элементов DOM (например, `message`, `title`, `url`, `frame-id`) на основе данных из объекта `results`.
    -   **Обработка контекста (`results.context`)**:
        -   Если `results.context` существует, устанавливает текст для элементов, связанных с контекстом (`context-method`, `context-expression`, `context-specified-result-type`, `context-result-type`, `context-resolver`).
        -   Обновляет таблицу деталей контекста (`context-detail`) с помощью `fu.updateDetailsTable`.
        -   Если `results.context` не существует, удаляет область контекста из DOM.
    -   **Обработка основных результатов (`results.main`)**:
        -   Устанавливает текст для элементов, связанных с основными результатами (`main-method`, `main-expression`, `main-specified-result-type`, `main-result-type`, `main-resolver`, `main-count`).
        -   Обновляет таблицу деталей основных результатов (`main-details`) с помощью `fu.updateDetailsTable`.

    _Пример_: 
    ```
    results = {
        message: "Test Message",
        title: "Test Title",
        href: "test.com",
        frameId: 1,
        context: {
            method: "xpath",
            expression: "//div",
            specifiedResultType: "ANY_TYPE",
            resultType: "ELEMENT_NODE",
            resolver: "default",
            itemDetail: { type: "div", name: "test", value: "content", textContent: "text" }
        },
        main: {
             method: "xpath",
             expression: "//span",
             specifiedResultType: "ANY_TYPE",
             resultType: "ELEMENT_NODE",
             resolver: "default",
             itemDetails: [{ type: "span", name: "test", value: "content", textContent: "text" }]
        }
    }
   
    // 1. Заполнение текстовых элементов:
    document.getElementById("message").textContent = "Test Message"; 
    document.getElementById("title").textContent = "Test Title"; 
    document.getElementById("url").textContent = "test.com";
    document.getElementById("frame-id").textContent = 1;
    // 2. Заполнение контекстной информации
    document.getElementById("context-method").textContent = "xpath";
    document.getElementById("context-expression").textContent = "//div";
    document.getElementById("context-specified-result-type").textContent = "ANY_TYPE";
    document.getElementById("context-result-type").textContent = "ELEMENT_NODE";
    document.getElementById("context-resolver").textContent = "default";
    // 3. Заполнение main информации
    document.getElementById("main-method").textContent = "xpath";
    document.getElementById("main-expression").textContent = "//span";
    document.getElementById("main-specified-result-type").textContent = "ANY_TYPE";
    document.getElementById("main-result-type").textContent = "ELEMENT_NODE";
    document.getElementById("main-resolver").textContent = "default";
    document.getElementById("main-count").textContent = 1;

    //4. Обновление таблиц:
    //  fu.updateDetailsTable(...)
    ```

3.  **`makeTextDownloadUrl(text)` Function:**
    -   Создает URL для скачивания текстового содержимого.
    
    _Пример_:
    ```
    text = "some text content";
    // Возвращает ссылку blob:http://....
    makeTextDownloadUrl(text); 
    ```

4.  **`makeInfoText(results)` Function:**
    -   Формирует текстовое представление информации из объекта `results`.
    -   Включает информацию о сообщении, заголовке, URL, frameId, контексте и основных результатах.
    -   Использует `fu.makeDetailText` для форматирования деталей.
        
    _Пример_:
    ```
    results = { ... } // example results object
    // Возвращает сформированную текстовую строку, пригодную для записи в файл.
    makeInfoText(results); 
    ```

5. **`makeConvertedInfoText(results)` Function:**
    -   Формирует текстовое представление информации, как `makeInfoText`, но преобразует значения `value` и `textContent` в JSON-строку.

    _Пример_:
    ```
    results = { ... } // example results object
    // Возвращает сформированную текстовую строку, пригодную для записи в файл с JSON values.
    makeConvertedInfoText(results);
    ```

6.  **`window.addEventListener("load", function() { ... })`:**
    -   Выполняется после загрузки страницы.
    -   Отправляет сообщение `browser.runtime.sendMessage` с событием `loadResults` для получения результатов.
    -   Обрабатывает полученные результаты:
        -   Сохраняет `tabId`, `frameId`, `executionId`.
        -   Устанавливает атрибуты `download` и `href` для элементов `export-text` и `export-partly-converted`, используя `makeTextDownloadUrl`, `makeInfoText` и `makeConvertedInfoText`.
        -   Вызывает `showAllResults` для отображения данных.
    -   Устанавливает обработчики событий `click` для таблиц `context-detail` и `main-details`:
        -   При клике на кнопку в таблице отправляет сообщения `focusContextItem` или `focusItem` с соответствующими данными (индекс для `main-details`).

  
   _Пример_:
        ```
        //При загрузке страницы:
        // 1. Отправляется сообщение браузеру с запросом results.
        browser.runtime.sendMessage({"event":"loadResults"}).then(results => {
            // 2. Устанавливаются значения, если результаты получены.
            relatedTabId = results.tabId;
            relatedFrameId = results.frameId;
            executionId = results.executionId;
            // 3. Экспорт данных.
            expoText.href =  makeTextDownloadUrl(makeInfoText(results));
            expoPartConv.href =  makeTextDownloadUrl(makeConvertedInfoText(results));
            // 4. Отображение результатов в интерфейсе.
            showAllResults(results);
            //  Обработчик контекста
             contDetail.addEventListener("click", function(event) {
                if (event.target.tagName.toLowerCase() === "button") {
                 // Отправка сообщения браузеру о фокусе контекстного элемента
                   browser.tabs.sendMessage(relatedTabId, { ... });
                }
             });
           //  Обработчик mainDetails
             mainDetails.addEventListener("click", function(event) {
                if (event.target.tagName.toLowerCase() === "button") {
                  //Отправка сообщения браузеру о фокусе элемента
                   browser.tabs.sendMessage(relatedTabId, { ... });
                }
            });
       }).catch(fu.onError);
      ```


### 2. <mermaid>

```mermaid
flowchart TD
    subgraph Initialization
        A[Initialize Variables] --> B(Alias tryxpath and functions);
        B --> C(Get Document Object);
        C --> D(Define Detail Keys);
        D --> E(Define Header Values);
        E --> F(Initialize IDs);
    end

    subgraph showAllResults Function
        G(showAllResults(results)) --> H{results.context?};
        H -- Yes --> I(Set Context Info);
        I --> J(Update Context Details Table);
        H -- No --> K(Remove Context Area);
         J --> L(Set Main Info);
         K --> L;
        L --> M(Update Main Details Table);
       
    end

    subgraph makeTextDownloadUrl Function
         N(makeTextDownloadUrl(text)) --> O(Create Blob URL);
    end

    subgraph makeInfoText Function
        P(makeInfoText(results)) --> Q(Extract Context and Main);
        Q --> R(Format Information Text);
    end
    
     subgraph makeConvertedInfoText Function
        S(makeConvertedInfoText(results)) --> T(Extract Context and Main);
        T --> U(Format Information Text with JSON);
    end

    subgraph EventListener
        V(window.addEventListener("load")) --> W(Send "loadResults" message);
        W --> X{Results Received?};
        X -- Yes --> Y(Save tabId, frameId, executionId);
        Y --> Z(Set Download Links for Text/JSON Data);
        Z --> AA(Call showAllResults(results));
        X -- No --> AB(Handle Error);
        AA --> AC(Add click listener to context details table);
        AA --> AD(Add click listener to main details table);
         AC --> AE{Click on Button};
          AE -- Yes --> AF(Send "focusContextItem" message to tab);
          AD --> AG{Click on Button};
          AG -- Yes --> AH(Send "focusItem" message to tab);
          AF --> AI(End);
          AH --> AI;

    end

    Initialization --> showAllResults Function;
    showAllResults Function --> EventListener;
    makeTextDownloadUrl Function --> EventListener;
    makeInfoText Function --> EventListener;
    makeConvertedInfoText Function --> EventListener;
```

**Объяснение зависимостей:**
-   `Initialization` подготавливает основные переменные и константы, необходимые для работы скрипта.
-   `showAllResults`  функция отвечает за визуализацию данных на странице. Она зависит от `Initialization` и вызывается в рамках `EventListener`.
-   `makeTextDownloadUrl` создает URL для скачивания текста, она вызывается внутри `EventListener`.
-    `makeInfoText` формирует текст для скачивания, вызывается в `EventListener`.
-   `makeConvertedInfoText` формирует текст для скачивания с JSON значениями, вызывается в `EventListener`.
-   `EventListener` является основным обработчиком событий загрузки страницы и кликов по элементам таблиц, объединяет работу остальных функций и взаимодействует с браузерным API для отправки сообщений.

### 3. <объяснение>

**Импорты:**

-   В данном коде нет явных инструкций `import`. Код использует глобальный объект `tryxpath` (алиасированный как `tx`) и его свойства, а также глобальный объект `window` и `document`. `browser` - это API расширения браузера.

**Классы:**

-   В предоставленном коде нет явных определений классов. Он использует JavaScript в функциональном стиле с замыканиями и обработчиками событий.

**Функции:**

-   **`showAllResults(results)`:**
    -   **Аргументы:** `results` - объект, содержащий данные для отображения (например, `message`, `title`, `href`, `context`, `main`).
    -   **Возвращаемое значение:** Отсутствует (undefined).
    -   **Назначение:** Обновляет содержимое HTML-страницы на основе переданных данных. Использует свойства `results`, такие как `message`, `title`, `url`, а также `context` и `main`. Обновляет HTML-элементы с соответствующими ID (например, `message`, `title`, `url`, `context-method`, `main-count`), а также вызывает `fu.updateDetailsTable` для заполнения таблиц данными.
    -   **Пример:** Вызывается в обработчике события `load` с данными, полученными из расширения.

-   **`makeTextDownloadUrl(text)`:**
    -   **Аргументы:** `text` - строка, которую нужно преобразовать в URL для скачивания.
    -   **Возвращаемое значение:** URL типа blob: для скачивания.
    -   **Назначение:** Создает URL для скачивания текстового контента.
    -   **Пример:** `makeTextDownloadUrl("Это текст для скачивания");` создаст ссылку для скачивания файла с текстом "Это текст для скачивания".

-   **`makeInfoText(results)`:**
    -   **Аргументы:** `results` - объект с данными.
    -   **Возвращаемое значение:** Форматированная строка с информацией.
    -   **Назначение:** Формирует текстовое представление данных, используя шаблонные строки.
    -   **Пример:** `makeInfoText({message: "Test", ...})` создаст строку с форматированным текстом.

-    **`makeConvertedInfoText(results)`:**
    -   **Аргументы:** `results` - объект с данными.
    -   **Возвращаемое значение:** Форматированная строка с информацией (JSON).
    -   **Назначение:** Формирует текстовое представление данных, используя шаблонные строки и преобразуя некоторые значения в JSON-строку.
    -   **Пример:** `makeConvertedInfoText({message: "Test", ...})` создаст строку с форматированным текстом, значения `value` и `textContent` будут представлены в виде JSON.

**Переменные:**

-   **`tx`:** Алиас для `tryxpath`.
-   **`fu`:** Алиас для `tryxpath.functions`. Используется для вызова функций `updateDetailsTable` и `onError`.
-   **`document`:** Ссылка на DOM-объект.
-   **`detailKeys`:** Массив ключей, используемых для отображения деталей (например, `["type", "name", "value", "textContent"]`).
-   **`headerValues`:** Массив заголовков для таблицы деталей (например, `["Type", "Name", "Value", "textContent"]`).
-  **`relatedTabId`**: ID вкладки, с которой связаны результаты.
-  **`relatedFrameId`**: ID фрейма, с которого пришли результаты.
-  **`executionId`**: ID выполнения.

**Объяснение:**

-   Код предназначен для отображения результатов выполнения `tryxpath` в веб-интерфейсе расширения браузера.
-   Он обрабатывает данные, полученные из фонового скрипта расширения через `browser.runtime.sendMessage`.
-   Функция `showAllResults` отвечает за заполнение HTML-элементов данными.
-   Функции `makeTextDownloadUrl`, `makeInfoText`, и `makeConvertedInfoText` генерируют текстовые данные для скачивания, с различием в форматировании.
-   Обработчики событий `click` для таблиц позволяют отправлять сообщения расширению для фокуса на элементах.
-   Использование `tryxpath.functions` указывает на то, что этот код зависит от библиотеки `tryxpath` и её утилит.

**Потенциальные ошибки и области для улучшения:**
-   **Обработка ошибок:** В коде используется `catch(fu.onError)`, но нет детальной обработки ошибок. Стоит предусмотреть более подробную обработку исключений для выявления проблем.
-   **Безопасность:** В `makeConvertedInfoText` используется `JSON.stringify`. Это может вызвать проблемы с безопасностью, если данные приходят из ненадежных источников, но в контексте данного расширения это менее критично.
-   **Читаемость:** Размещение логики обработки данных и обновления DOM в одной функции `showAllResults` может усложнить понимание и дальнейшую поддержку кода. Стоит разбить ее на более мелкие функции.
-   **Повторяемость кода**: Много кода дублируется между `makeInfoText` и `makeConvertedInfoText`, его можно было бы вынести в отдельную функцию с параметром для преобразования данных в JSON.

**Цепочка взаимосвязей с другими частями проекта:**

-   Код взаимодействует с фоновым скриптом расширения через `browser.runtime.sendMessage`. Это означает, что фоновый скрипт должен отправлять сообщения с данными в правильном формате.
-   Код зависит от `tryxpath` и его функций. Библиотека `tryxpath` должна быть определена и доступна.
-   Код является частью UI расширения, который отображает результаты работы `tryxpath` и позволяет управлять элементами на странице.
-   Код отправляет сообщения `focusContextItem` и `focusItem` обратно в фоновый скрипт для фокуса на элементах.