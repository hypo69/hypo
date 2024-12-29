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

## Алгоритм

```mermaid
graph LR
    A[Начало: Загрузка popup.js] --> B{window.addEventListener("load")};
    B -- "Событие 'load'" --> C[Инициализация переменных и элементов DOM];
    C --> D{Установка слушателей событий};
    D -- "Клик на execute" --> E[Сбор данных из формы: makeExecuteMessage()];
    E --> F[Отправка сообщения в текущую вкладку: sendToSpecifiedFrame()];
    F --> G[Выполнение скриптов в указанном фрейме: execContentScript()];
    G --> H[Отправка сообщения с данными: sendToActiveTab()];
    D -- "Нажатие Enter в поле ввода" --> I[Вызов sendExecute: handleExprEnter()];
    I --> E;
    D -- "Изменение видимости блоков" --> J[Изменение видимости блоков changeContextVisible(), changeResolverVisible(), changeFrameIdVisible(), changeFrameDesignationVisible(), changeHelpVisible()];
    D -- "Событие: browser.runtime.onMessage" --> K[Обработка сообщений genericListener()];
    K -- "Событие: showResultsInPopup" --> L[Отображение результатов в popup: genericListener.listeners.showResultsInPopup()];
    K -- "Событие: restorePopupState" --> M[Восстановление состояния popup: genericListener.listeners.restorePopupState()];
     K -- "Событие: insertStyleToPopup" --> N[Вставка стилей в popup: genericListener.listeners.insertStyleToPopup()];
    K -- "Событие: addFrameId" --> O[Добавление frameId в список: genericListener.listeners.addFrameId()];
     D -- "Событие: Клик на таблице результатов" --> P[Фокусировка на элементе: browser.tabs.sendMessage()];
      D -- "Событие: Клик на контекстной таблице" --> Q[Фокусировка на контекстном элементе: browser.tabs.sendMessage()];
        D -- "Событие: Клик на кнопки пагинации" --> R[Изменение страницы деталей: showDetailsPage()];
        R --> S{Обновление таблицы результатов: fu.updateDetailsTable()};
    D -- "Событие unload" --> T[Сохранение состояния popup: collectPopupState()];
    T --> U[Отправка сообщения о сохранении состояния: browser.runtime.sendMessage()];
    U--> V[Завершение работы];
     
    
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style V fill:#ccf,stroke:#333,stroke-width:2px
```

## Mermaid

```mermaid
graph LR
    subgraph popup.js
    A[popup.js: window.addEventListener('load')] --> B(Инициализация DOM элементов и переменных);
    B --> C{Установка слушателей событий};
    C --> D[sendToActiveTab(msg, opts): Отправляет сообщение активной вкладке];
    C --> E[sendToSpecifiedFrame(msg): Отправляет сообщение указанному фрейму];
    C --> F[execContentScript(): Внедряет скрипты в контент];
     C --> G[makeExecuteMessage(): Собирает данные для выполнения запроса];
     C --> H[genericListener(message, sender, sendResponse): Обработчик сообщений];
    H --> I[showResultsInPopup(): Отображает результаты в popup];
    H --> J[restorePopupState(): Восстанавливает состояние popup];
    H --> K[insertStyleToPopup(): Вставляет стили в popup];
     H --> L[addFrameId(): Добавляет ID фрейма в список];
       C --> M[showDetailsPage(index): Показывает страницу с деталями];
         C --> N[collectPopupState(): Собирает состояние popup];
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

## Объяснение

### Импорты

В коде нет явных импортов, но используются переменные `tryxpath` и `tryxpath.functions` (сокращенно `tx` и `fu` соответственно).  Это подразумевает, что `tryxpath` это некий глобальный объект, предоставляемый окружением,  скорее всего, это глобальный объект, внедрённый в контекст расширения.

### Переменные

*   **`noneClass` (string):** `"none"` - CSS класс для скрытия элементов.
*   **`helpClass` (string):** `"help"` - CSS класс для элементов справки.
*   **`invalidTabId` (number):**  `browser.tabs.TAB_ID_NONE` - ID недействительной вкладки.
*   **`invalidExecutionId` (number):** `NaN` - ID недействительного выполнения.
*   **`invalidFrameId` (number):** `-1` - ID недействительного фрейма.
*   **Переменные DOM элементов:** `mainWay`, `mainExpression`, `contextCheckbox` и т.д. -  Ссылки на DOM элементы, используемые для управления интерфейсом.
*   **`relatedTabId` (number):** ID вкладки, связанной с текущим выполнением.
*   **`relatedFrameId` (number):** ID фрейма, связанного с текущим выполнением.
*   **`executionId` (number):** ID текущего выполнения.
*   **`resultedDetails` (array):** Массив деталей результатов.
*   **`detailsPageSize` (number):** Количество деталей на одной странице.
*   **`detailsPageIndex` (number):** Индекс текущей страницы деталей.

### Функции

*   **`sendToActiveTab(msg, opts)`:**
    *   **Аргументы:**
        *   `msg` (object): Сообщение для отправки.
        *   `opts` (object, optional): Дополнительные опции для отправки.
    *   **Назначение:** Отправляет сообщение в активную вкладку. Использует `browser.tabs.query` для получения активной вкладки и `browser.tabs.sendMessage` для отправки сообщения.
    *   **Пример:**
        ```javascript
        sendToActiveTab({ event: "execute", data: "some data" });
        ```
*   **`sendToSpecifiedFrame(msg)`:**
    *   **Аргументы:**
        *   `msg` (object): Сообщение для отправки.
    *   **Назначение:** Отправляет сообщение в указанный фрейм. Сначала внедряет скрипт для проверки доступности фрейма, затем отправляет сообщение.
    *   **Пример:**
        ```javascript
        sendToSpecifiedFrame({ event: "focus", element: "someElement" });
        ```
*   **`collectPopupState()`:**
    *   **Назначение:** Собирает состояние всех элементов формы, таких как значения полей ввода и состояния чекбоксов, для сохранения.
    *   **Возвращает:** Состояние объекта.
*   **`changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`:**
    *   **Назначение:** Управляют видимостью соответствующих разделов формы на основе состояния чекбоксов.
    *   **Пример:**
        ```javascript
         changeContextVisible(); // Скрыть или показать контекстный блок, в зависимости от состояния contextCheckbox
        ```
*   **`makeExecuteMessage()`:**
    *   **Назначение:** Собирает данные из формы для запроса выполнения Xpath.
    *   **Возвращает:** Объект сообщения с данными для выполнения.
    *   **Пример:**
        ```javascript
         makeExecuteMessage(); // возвращает объект со всеми параметрами для execute
        ```
*   **`getSpecifiedFrameId()`:**
    *   **Назначение:** Получает идентификатор фрейма для выполнения. Если не выбран, по умолчанию возвращает `0` (главный фрейм)
    *   **Возвращает:** Числовой ID фрейма.
*    **`execContentScript()`**
      *   **Назначение:** Выполняет скрипты `try_xpath_functions.js` и  `try_xpath_content.js` во всех фреймах текущей вкладки.
      *  **Возвращает:** `Promise`
*   **`sendExecute()`:**
    *   **Назначение:** Отправляет сообщение на выполнение, используя `sendToSpecifiedFrame`.
*   **`handleExprEnter(event)`:**
    *   **Назначение:** Обрабатывает нажатие клавиши "Enter" в текстовых полях, вызывая `sendExecute()`, для отправки запроса.
*   **`showDetailsPage(index)`:**
    *   **Аргументы:**
        *   `index` (number): Индекс страницы для отображения.
    *   **Назначение:** Обновляет таблицу результатов отображая страницу с деталями, используя `fu.updateDetailsTable()`.
*   **`showError(message, frameId)`:**
    *   **Аргументы:**
        *   `message` (string): Сообщение об ошибке.
        *   `frameId` (number): ID фрейма.
    *   **Назначение:** Выводит сообщение об ошибке и сбрасывает состояние.
*  **`genericListener(message, sender, sendResponse)`:**
     *   **Назначение:** Основной обработчик входящих сообщений от контент скриптов. Вызывает соответствующий листенер на основе поля `event`
     *   **Пример:** 
        ```javascript
            genericListener({event:"showResultsInPopup", message:{}},{tab:{id: 1}, frameId: 0})
            // Вызовет genericListener.listeners.showResultsInPopup
        ```
*  **`genericListener.listeners.showResultsInPopup(message, sender)`:**
    *   **Назначение:** Обновляет отображение результатов в popup.
    *  **Пример:**
        ```javascript
            genericListener.listeners.showResultsInPopup({message:{}, main: { itemDetails: [{},{}]}},{tab:{id: 1}, frameId: 0});
        ```
*  **`genericListener.listeners.restorePopupState(message)`:**
    *    **Назначение:** Восстанавливает состояние popup из сохраненных данных.
    *  **Пример:**
        ```javascript
            genericListener.listeners.restorePopupState({state:{mainExpressionValue: "some value" }});
        ```
*  **`genericListener.listeners.insertStyleToPopup(message)`:**
   *   **Назначение:** Вставляет стили в popup.
   *    **Пример:**
        ```javascript
            genericListener.listeners.insertStyleToPopup({css:"body {background-color: red}"});
        ```
*  **`genericListener.listeners.addFrameId(message, sender)`:**
    *   **Назначение:** Добавляет ID фрейма в список выбора.
    *   **Пример:**
        ```javascript
            genericListener.listeners.addFrameId({}, {frameId: 1});
        ```

### Потенциальные ошибки и улучшения

*   **Обработка ошибок:** В коде есть `catch(fu.onError)` в некоторых местах, но более детальная обработка ошибок может быть полезна для отладки.
*   **Состояние popup:** Состояние popup сохраняется и восстанавливается при открытии/закрытии, но может понадобиться более продвинутое управление состоянием (например, при изменении настроек).
*   **Производительность:** При большом количестве деталей, отображение может замедляться. Можно рассмотреть варианты с виртуализацией таблицы.
*   **Использование `Promise.resolve().then()`**: В функции `sendToSpecifiedFrame` использование  `Promise.resolve().then()` выглядит избыточно, так как `browser.tabs.executeScript` возвращает `Promise`
*   **Дублирование `timeout_for_event: "presence_of_element_located"`** В коде много раз встречается  `"timeout":0,"timeout_for_event":"presence_of_element_located"` можно вынести в константу или  параметр по умолчанию.

### Цепочка взаимосвязей с другими частями проекта

1.  **`try_xpath_functions.js`**:  Содержит функции для работы с DOM и выполнения XPath запросов.
2.  **`try_xpath_content.js`**: Содержит логику для взаимодействия с DOM и отправки данных в popup.
3.  **`options.js`**: Этот файл предположительно отвечает за настройки расширения, вызывается при открытии страницы настроек (`browser.runtime.openOptionsPage();`).
4.  **Контент скрипты:** Взаимодействие происходит через `browser.tabs.sendMessage`, что позволяет отправлять данные в обе стороны.

В целом, код представляет собой сложный popup для управления и выполнения XPath запросов на веб-страницах,  используя API браузерных расширений. Он обменивается сообщениями с контент скриптами для выполнения запросов и отображения результатов.