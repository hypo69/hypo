## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

1.  **Инициализация**:
    *   Код выполняется в анонимной самовызывающейся функции, создавая локальную область видимости.
    *   Объявляются переменные `tx` (сокращение от `tryxpath`), `fu` (сокращение от `tryxpath.functions`), `document`, `detailKeys`, `headerValues`, `relatedTabId`, `relatedFrameId`, `executionId`.

2.  **`showAllResults(results)`**:
    *   Принимает объект `results`, содержащий данные для отображения.
    *   Обновляет текстовое содержимое элементов HTML на странице (сообщения, заголовки, URL, идентификаторы фреймов).
    *   Если `results.context` существует:
        *   Извлекает данные контекста и обновляет соответствующие HTML-элементы.
        *   Обновляет таблицу деталей контекста, используя функцию `fu.updateDetailsTable`, которая, вероятно, форматирует и вставляет данные в таблицу.
        *   Пример: `results.context` может быть объектом типа
        `{ method: 'querySelector', expression: '//div', specifiedResultType: 7, resultType: 4, resolver: null, itemDetail: { type: 'element', name: 'DIV', value: '<div>Example</div>', textContent: 'Example' }}`
    *   Если `results.context` отсутствует, удаляет соответствующий раздел HTML.
    *   Извлекает данные основного результата (`results.main`) и обновляет соответствующие HTML-элементы, включая количество элементов и таблицу деталей.
        *   Пример: `results.main` может быть объектом типа
        `{ method: 'querySelectorAll', expression: '//p', specifiedResultType: 7, resultType: 4, resolver: null, itemDetails: [{ type: 'element', name: 'P', value: '<p>Text1</p>', textContent: 'Text1' }, { type: 'element', name: 'P', value: '<p>Text2</p>', textContent: 'Text2' }] }`

3.  **`makeTextDownloadUrl(text)`**:
    *   Принимает текстовую строку `text`.
    *   Создает URL для загрузки файла, используя `URL.createObjectURL` и `Blob`, что позволяет загружать текстовый файл в браузере.

4.  **`makeInfoText(results)`**:
    *   Принимает объект `results`.
    *   Формирует текстовое представление данных `results` с основной информацией и деталями в удобочитаемом виде.
    *   Использует `fu.makeDetailText` для форматирования деталей.

5.  **`makeConvertedInfoText(results)`**:
    *   Принимает объект `results`.
    *   Аналогично `makeInfoText`, но преобразует значения `value` и `textContent` в JSON-строки.

6.  **`window.addEventListener("load", function(){ ... })`**:
    *   Устанавливает обработчик события `load` для окна браузера.
    *   После загрузки страницы отправляет сообщение `loadResults` в фоновое расширение браузера.
    *   Получает результаты, устанавливает значения `relatedTabId`, `relatedFrameId`, `executionId`
    *   Формирует URL-адреса для экспорта данных и устанавливает их в атрибуты ссылок для скачивания (`export-text`, `export-partly-converted`).
        *   Используются `makeInfoText` и `makeConvertedInfoText` для формирования данных для экспорта.
        *   Обновляет содержимое HTML с помощью `showAllResults`.
    *   Добавляет обработчики событий `click` для таблиц деталей контекста и основных результатов.
        *   При клике на кнопку в этих таблицах отправляется сообщение в расширение браузера для фокуса на соответствующем элементе.
            *   Сообщение `focusContextItem` для таблицы контекста
            *   Сообщение `focusItem` для таблицы основных результатов с индексом элемента.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало загрузки страницы] --> LoadEvent[Событие 'load']
    LoadEvent --> SendMessage[Отправка сообщения 'loadResults']
    SendMessage --> Response[Получение данных из background.js]
    Response -- Данные есть --> SetVars[Установка relatedTabId, relatedFrameId, executionId]
    Response -- Данных нет --> ErrorHandle[Обработка ошибки]
    SetVars --> CreateExportUrls[Создание URL для экспорта]
    CreateExportUrls --> CallShowAllResults[Вызов showAllResults(results)]
     
    CallShowAllResults --> UpdateHtml[Обновление HTML элементов с результатами]
    UpdateHtml --> AddContextListener[Добавление обработчика клика для контекста]
    UpdateHtml --> AddMainListener[Добавление обработчика клика для основных результатов]    
    
    AddContextListener --> ContextClick[Событие клика в таблице контекста]
    ContextClick -- Клик на кнопке --> SendContextFocusMsg[Отправка сообщения 'focusContextItem' в background.js]
     ContextClick -- Клик не на кнопке --> None
    
    AddMainListener --> MainClick[Событие клика в таблице основных результатов]
    MainClick -- Клик на кнопке --> GetIndex[Получение индекса элемента]
    GetIndex --> SendMainFocusMsg[Отправка сообщения 'focusItem' в background.js с индексом]
     MainClick -- Клик не на кнопке --> None
    
    CreateExportUrls --> MakeText[Формирование текстового представления данных]
    MakeText --> CreateUrl[Создание URL для скачивания файла]
     MakeText --> MakeConvertedText[Формирование JSON-представления данных]
        MakeConvertedText --> CreateJsonUrl[Создание URL для скачивания JSON-файла]
    CreateUrl --> SetDownloadLink[Установка download link атрибута]
      CreateJsonUrl --> SetDownloadJsonLink[Установка JSON download link атрибута]
       SetDownloadLink -->  None
       SetDownloadJsonLink -->  None
    ErrorHandle --> None
    SendContextFocusMsg --> None
    SendMainFocusMsg --> None
    
    subgraph showAllResults
        UpdateHtml
    end
    
    subgraph Export
       MakeText
        CreateUrl
         MakeConvertedText
            CreateJsonUrl
            SetDownloadLink
             SetDownloadJsonLink
    end
```

**Описание зависимостей в `mermaid`:**

*   **`Start`**: Начальная точка процесса загрузки страницы.
*   **`LoadEvent`**: Событие `load`, которое запускает основную логику после загрузки страницы.
*   **`SendMessage`**: Отправка сообщения `loadResults` в фоновое расширение (background.js) для запроса данных.
*   **`Response`**: Получение данных от фонового расширения.
*   **`SetVars`**: Установка переменных `relatedTabId`, `relatedFrameId`, `executionId` из полученных данных.
*   **`CreateExportUrls`**: Функция создает ссылки для скачивания текстовых файлов.
*   **`CallShowAllResults`**: Вызов функции `showAllResults` для отображения результатов.
*  **`UpdateHtml`**: Обновление HTML-элементов на странице с полученными результатами.
*   **`AddContextListener`**: Добавление обработчика событий клика для контекстной таблицы.
*   **`AddMainListener`**: Добавление обработчика событий клика для таблицы основных результатов.
*   **`ContextClick`**: Обработка клика в таблице контекста.
*   **`SendContextFocusMsg`**: Отправка сообщения для фокуса контекстного элемента.
*   **`MainClick`**: Обработка клика в таблице основных результатов.
*  **`GetIndex`**: Получение индекса элемента из атрибута.
*   **`SendMainFocusMsg`**: Отправка сообщения для фокуса элемента с индексом.
*   **`ErrorHandle`**: Обработка ошибок при получении данных.
*  **`MakeText`**: Формирует текстовое представление данных для скачивания.
*    **`MakeConvertedText`**: Формирует JSON представление данных для скачивания.
*   **`CreateUrl`**: Создает URL для скачивания обычного текстового файла.
*    **`CreateJsonUrl`**: Создает URL для скачивания JSON текстового файла.
* **`SetDownloadLink`**: Устанавливает атрибут `download` для ссылки.
* **`SetDownloadJsonLink`**: Устанавливает атрибут `download` для ссылки с JSON данными.

## <объяснение>

**Импорты:**

*   В данном коде нет явных импортов через `import` или `require`. Вместо этого код использует переменные `tryxpath` и `tryxpath.functions`, которые предполагаются уже определенными в глобальной области видимости или предоставлены через контекст выполнения. `tryxpath` предположительно является основным объектом, содержащим логику расширения, а `tryxpath.functions` - объект с утилитарными функциями.
    *   **`tryxpath`** (сокращено до `tx`):  Это, вероятно, основной объект, содержащий функционал расширения для работы с XPath.
    *   **`tryxpath.functions`** (сокращено до `fu`): Это объект, который содержит вспомогательные функции, такие как `updateDetailsTable`, `onError`, `makeDetailText`.

**Классы:**

*   В коде нет явного определения классов. Вся логика реализована с помощью функций и замыканий.

**Функции:**

*   **`showAllResults(results)`**:
    *   **Аргументы**: `results` - объект, содержащий данные для отображения, включая `message`, `title`, `href`, `frameId`, `context` (опционально), и `main`.
    *   **Возвращаемое значение**: Нет (функция изменяет DOM).
    *   **Назначение**: Обновляет HTML-элементы на странице с информацией, полученной из `results`. Отображает результаты выполнения XPath, включая контекст и основные данные.
    *   **Пример**: `showAllResults({message: "Success", title: "XPath Results", href: "http://example.com", frameId: 1, context: {method: "querySelector", expression: "//div", specifiedResultType: 7, resultType: 4, resolver: null, itemDetail: {type: "element", name: "DIV", value: "<div>Example</div>", textContent: "Example"}}, main: {method: "querySelectorAll", expression: "//p", specifiedResultType: 7, resultType: 4, resolver: null, itemDetails: [{type: "element", name: "P", value: "<p>Text1</p>", textContent: "Text1"}, {type: "element", name: "P", value: "<p>Text2</p>", textContent: "Text2"}]}})`
*   **`makeTextDownloadUrl(text)`**:
    *   **Аргументы**: `text` - строка текста, которую нужно сделать доступной для скачивания.
    *   **Возвращаемое значение**: URL, который можно использовать для скачивания текстового файла.
    *   **Назначение**: Создает URL для скачивания текстового файла.
    *   **Пример**: `makeTextDownloadUrl("Hello, world!")` вернет строку типа `"blob:http://localhost:3000/some-unique-id"`
*   **`makeInfoText(results)`**:
    *   **Аргументы**: `results` - объект, содержащий данные для форматирования.
    *   **Возвращаемое значение**: Строка, представляющая собой текстовое описание данных из `results`.
    *   **Назначение**: Формирует удобочитаемое текстовое представление данных, включая информацию о контексте и основных результатах.
    *   **Пример**: `makeInfoText({message: "Success", title: "XPath Results", href: "http://example.com", frameId: 1, context: {method: "querySelector", expression: "//div", specifiedResultType: 7, resultType: 4, resolver: null, itemDetail: {type: "element", name: "DIV", value: "<div>Example</div>", textContent: "Example"}}, main: {method: "querySelectorAll", expression: "//p", specifiedResultType: 7, resultType: 4, resolver: null, itemDetails: [{type: "element", name: "P", value: "<p>Text1</p>", textContent: "Text1"}, {type: "element", name: "P", value: "<p>Text2</p>", textContent: "Text2"}]}})`
*   **`makeConvertedInfoText(results)`**:
    *   **Аргументы**: `results` - объект, содержащий данные для форматирования.
    *   **Возвращаемое значение**: Строка, представляющая собой текстовое описание данных из `results` с JSON-преобразованием.
    *   **Назначение**: Формирует текстовое представление данных, где значения `value` и `textContent` представлены в формате JSON.
    *   **Пример**: `makeConvertedInfoText({message: "Success", title: "XPath Results", href: "http://example.com", frameId: 1, context: {method: "querySelector", expression: "//div", specifiedResultType: 7, resultType: 4, resolver: null, itemDetail: {type: "element", name: "DIV", value: "<div>Example</div>", textContent: "Example"}}, main: {method: "querySelectorAll", expression: "//p", specifiedResultType: 7, resultType: 4, resolver: null, itemDetails: [{type: "element", name: "P", value: "<p>Text1</p>", textContent: "Text1"}, {type: "element", name: "P", value: "<p>Text2</p>", textContent: "Text2"}]}})`
*   **`window.addEventListener("load", function() { ... })`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Обработчик события `load` окна браузера. Запускает основную логику: отправляет сообщение для получения результатов, обрабатывает результаты, устанавливает обработчики кликов для таблиц.

**Переменные:**

*   **`tx`**: Алиас для `tryxpath`.
*   **`fu`**: Алиас для `tryxpath.functions`.
*   **`document`**: Ссылка на объект `document`.
*   **`detailKeys`**: Массив строк, представляющий ключи для деталей (например, `type`, `name`, `value`, `textContent`).
*   **`headerValues`**: Массив строк, представляющий заголовки для таблицы деталей.
*   **`relatedTabId`**: Идентификатор вкладки, с которой связаны результаты.
*   **`relatedFrameId`**: Идентификатор фрейма, с которого связаны результаты.
*   **`executionId`**: Идентификатор выполнения запроса.

**Потенциальные ошибки и области для улучшения:**

*   **Зависимость от глобальных переменных**: Код полагается на существование глобальных переменных `tryxpath` и `tryxpath.functions`, что может привести к ошибкам, если они не определены. Лучше использовать модульную систему или передавать зависимости.
*   **Обработка ошибок**: Обработка ошибок ограничена вызовом `fu.onError`. Желательно добавить более детальную обработку ошибок.
*   **DOM-манипуляции**: Код напрямую манипулирует DOM, что может быть медленным. Можно рассмотреть использование виртуального DOM или библиотеки для эффективного обновления.
*   **Зависимость от DOM структуры**: Код сильно зависит от конкретной структуры HTML-страницы. Любые изменения в структуре могут привести к сбоям. Можно использовать CSS-селекторы для более надежной привязки к DOM.
*   **Безопасность**: Использование `URL.createObjectURL` без отзыва URL может привести к утечке памяти.  Желательно после загрузки удалять URL.

**Цепочка взаимосвязей с другими частями проекта:**

1.  **`background.js`**: Фоновый скрипт расширения. Он отвечает за отправку сообщения `loadResults` и получение данных.
2.  **`tryxpath.js`**: Ядро расширения, которое предоставляет функции для работы с XPath и, вероятно, объект `tryxpath`.
3.  **`header.py`**: В данном файле отсутствует импорт `header`, но если бы он был, он бы определял корень проекта и загружал глобальные настройки.
4.  **`content.js`**: Скрипт, выполняющийся на странице, который использует `tryxpath` для выполнения XPath-запросов и отправляет результаты.

Данный скрипт `show_all_results.js` является частью пользовательского интерфейса расширения, которое отображает результаты выполнения XPath запросов, полученных из других частей расширения. Он получает данные, отображает их в HTML, позволяет скачать как текст или JSON и позволяет сфокусироваться на найденных элементах.