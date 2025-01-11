## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```
3.  **<объяснение>**: Предоставьте подробные объяснения:
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    -   **Переменные**: Их типы и использование.
    -   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

```mermaid
graph TD
    A[Начало: Загрузка popup.js] --> B{Событие "load"};
    B -- Да --> C[Инициализация переменных и DOM элементов];
    C --> D{Событие "click" на "execute"};
    D -- Да --> E[Вызов sendExecute()];
    E --> F[Вызов makeExecuteMessage()];
    F --> G[Формирование сообщения для выполнения скрипта];
    G --> H[Вызов sendToSpecifiedFrame()];
    H --> I{Проверка frameId};
    I -- frameId = 0 --> J[Вызов execContentScript()];
    I -- frameId != 0 --> K[Вызов browser.tabs.executeScript() для try_xpath_check_frame.js];
    K --> L{Результат выполнения скрипта try_xpath_check_frame.js};
    L -- true --> M[Отправка сообщения для выполнения скрипта в указанном frameId];
    L -- false --> J;
    J --> N[Вызов browser.tabs.executeScript() для try_xpath_functions.js и try_xpath_content.js];
    N --> O[Отправка сообщения для выполнения скрипта в указанном frameId];
    O --> P[Получение результата выполнения скрипта от content.js];
    P --> Q[Вызов genericListener.listeners.showResultsInPopup()];
    Q --> R[Отображение результатов в popup];
    C --> S{Событие "click" на "get-all-frame-id"};
    S -- Да --> T[Очистка списка frameId];
    T --> U[Добавление "Manual" option в список frameId];
    U --> V[Вызов browser.tabs.executeScript() для запроса frameId];
    V --> W[Получение frameId от content.js];
    W --> X[Вызов genericListener.listeners.addFrameId()];
     X --> Y[Добавление frameId в список];

    C --> Z{Событие "click" на "show-previous-results"};
    Z -- Да --> AA[Вызов sendToSpecifiedFrame() с requestShowResultsInPopup];
    AA --> O;
     C --> AB{Событие "click" на "focus-frame"};
    AB -- Да --> AC[Вызов sendToSpecifiedFrame() с focusFrame];
     AC --> O;
     C --> AD{Событие "click" на "show-all-results"};
    AD -- Да --> AE[Вызов sendToSpecifiedFrame() с requestShowAllResults];
    AE --> O;
    C --> AF{Событие "click" на "set-style"};
     AF -- Да --> AG[Вызов sendToSpecifiedFrame() с setStyle];
     AG --> O;
     C --> AH{Событие "click" на "reset-style"};
    AH -- Да --> AI[Вызов sendToSpecifiedFrame() с resetStyle];
    AI --> O;
    C --> AJ{Событие "click" на "set-all-style"};
     AJ -- Да --> AK[Вызов sendToActiveTab() с setStyle];
     AK --> O;
     C --> AL{Событие "click" на "reset-all-style"};
    AL -- Да --> AM[Вызов sendToActiveTab() с resetStyle];
    AM --> O;
    C --> AN{Событие "unload"};
    AN -- Да --> AO[Вызов collectPopupState()];
    AO --> AP[Сохранение состояния popup];
     C --> AQ[Запрос стилей и восстановления состояния popup];

     C --> AR{Событие "keypress" в полях ввода};
     AR -- Да --> AS[Вызов handleExprEnter()];
     AS --> AT{Проверка "Enter" и shiftKey};
      AT -- Да --> E;
     AT -- Нет --> AR;

    R --> AU[Отображение контекстных данных при наличии];
    AU --> AV{Событие "click" по строке контекстных данных};
    AV -- Да --> AW[Отправка сообщения с фокусом контекстного элемента в content.js];
    R --> AX[Отображение элементов данных];
    AX --> AY{Событие "click" по элементу данных};
    AY -- Да --> AZ[Отправка сообщения с фокусом элемента в content.js];

    style fill:#f9f,stroke:#333,stroke-width:2px
    classDef main fill:#ccf,stroke:#333,stroke-width:2px
    class C,X,Y,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,AA,AB,AC,AD,AE,AF,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU,AV,AW,AX,AY,AZ  main;
```

**Пример для блока "Формирование сообщения для выполнения скрипта":**

Допустим, у нас есть следующие значения в popup:
*   `mainWay`: XPath
*   `mainExpression`: //div[@id='test']
*   `contextCheckbox` : checked
*   `contextWay`: CSS Selector
*   `contextExpression`: #another_test
*   `resolverCheckbox` : not checked

Тогда функция `makeExecuteMessage()` создаст следующий объект `msg`:
```javascript
{
  event: "execute",
  main: {
    expression: "//div[@id='test']",
    method: "xpath",
    resultType: "ANY",
    resolver: null,
  },
  context: {
     expression: "#another_test",
     method: "css",
     resultType: "ANY",
     resolver: null
  }
}

```
Этот объект передается в функцию `sendToSpecifiedFrame()`.

**Пример для блока "Отправка сообщения для выполнения скрипта в указанном frameId":**

Предположим, frameId равен 2. Функция `sendToSpecifiedFrame()` отправит сообщение `msg` с frameId: 2 в content script, который будет выполняться в контексте этого frame.

## <mermaid>

```mermaid
graph LR
    subgraph popup.js
        A[sendToActiveTab(message, options)]
        B[sendToSpecifiedFrame(message)]
        C[collectPopupState()]
        D[changeContextVisible()]
        E[changeResolverVisible()]
        F[changeFrameIdVisible()]
        G[changeFrameDesignationVisible()]
        H[changeHelpVisible()]
        I[makeExecuteMessage()]
        J[getSpecifiedFrameId()]
        K[execContentScript()]
        L[sendExecute()]
        M[handleExprEnter(event)]
        N[showDetailsPage(index)]
        O[showError(message, frameId)]
        P[genericListener(message, sender, sendResponse)]
    end
    subgraph try_xpath_functions.js
        Q[updateDetailsTable(tbody, items, options)]
        R[onError(error)]
        S[createDetailTableHeader()]
        T[emptyChildNodes(node)]
    end
    subgraph browser API
        U[browser.tabs.query(queryInfo)]
        V[browser.tabs.sendMessage(tabId, message, options)]
        W[browser.tabs.executeScript(executeScriptOptions)]
        X[browser.runtime.onMessage.addListener(listener)]
        Y[browser.runtime.sendMessage(message)]
        Z[browser.runtime.openOptionsPage()]
    end
    A --> V
    B --> J
    B --> W
    B --> A
    L --> B
     M --> L
     N --> Q
     N --> R
    O --> Q
     P --> P
    genericListener.listeners.showResultsInPopup --> N
    genericListener.listeners.showResultsInPopup --> Q
    genericListener.listeners.restorePopupState --> B
     genericListener.listeners.addFrameId --> Z
    K --> W
    I --> J

     Q --> R
    Y --> X
     Z --> X
    

     classDef browserAPI fill:#ccf,stroke:#333,stroke-width:2px
     class U,V,W,X,Y,Z browserAPI;
```

**Зависимости:**

*   `popup.js` использует функции `updateDetailsTable`, `onError`, `createDetailTableHeader`, `emptyChildNodes` из `try_xpath_functions.js` для обработки и отображения данных в таблицах.
*   `popup.js` взаимодействует с API браузера (через `browser.*`) для отправки и получения сообщений, выполнения скриптов и управления вкладками.
*  `popup.js`  использует DOM API (`window`, `document`) для доступа и управления элементами HTML.
*   `try_xpath_functions.js` не зависит от других скриптов, это библиотека функций.

## <объяснение>

**Импорты:**

*   `tryxpath` и `tryxpath.functions`: Это кастомные объекты, которые предположительно содержат необходимые функции для работы с XPath, CSS-селекторами и другими операциями, используемые для обработки и отображения результатов. Они определены в `/scripts/try_xpath_functions.js`.
*   `browser`: Это API браузера, который используется для взаимодействия с браузером, отправки сообщений, выполнения скриптов и т.д.

**Переменные:**

*   `noneClass`, `helpClass`: Строковые константы, используемые для управления видимостью элементов DOM.
*   `invalidTabId`, `invalidExecutionId`, `invalidFrameId`: Константы, обозначающие невалидные значения для id вкладок, выполнения и фреймов.
*   `mainWay`, `mainExpression`, `contextCheckbox`, `contextHeader`, `contextBody`, `contextWay`, `contextExpression`, `resolverHeader`, `resolverBody`, `resolverCheckbox`, `resolverExpression`, `frameDesignationHeader`, `frameDesignationCheckbox`, `frameDesignationBody`, `frameDesignationExpression`, `frameIdHeader`, `frameIdCheckbox`, `frameIdBody`, `frameIdList`, `frameIdExpression`, `resultsMessage`, `resultsTbody`, `contextTbody`, `resultsCount`, `resultsFrameId`, `detailsPageCount`, `helpBody`, `helpCheckbox`: DOM элементы, полученные через `document.getElementById()` и используемые для взаимодействия с интерфейсом popup.
*   `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения id текущей вкладки, фрейма и выполнения.
*   `resultedDetails`: Массив для хранения данных для отображения в таблице результатов.
*   `detailsPageSize`: Количество элементов для отображения на одной странице результатов.
*   `detailsPageIndex`: Индекс текущей страницы результатов.

**Функции:**

*   `sendToActiveTab(msg, opts)`: Отправляет сообщение `msg` активной вкладке. `opts` является необязательным параметром для передачи дополнительных опций.
*   `sendToSpecifiedFrame(msg)`: Отправляет сообщение `msg` в указанный фрейм. Сначала проверяет, загружен ли скрипт в фрейме, если нет, то загружает. `frameId` получается из `getSpecifiedFrameId()`.
*   `collectPopupState()`: Собирает текущее состояние popup (значения полей, состояние чекбоксов) в объект и возвращает его.
*   `changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`: Управляют видимостью соответствующих блоков в popup на основе состояния чекбоксов.
*   `makeExecuteMessage()`: Создает сообщение `msg` для отправки в контентный скрипт, содержащее информацию о запросе пользователя (метод, выражение, контекст).
*   `getSpecifiedFrameId()`: Получает id фрейма, выбранного пользователем, из списка или поля ввода.
*   `execContentScript()`: Загружает скрипты `try_xpath_functions.js` и `try_xpath_content.js` во все фреймы текущей вкладки.
*   `sendExecute()`: Вызывает `makeExecuteMessage()` и `sendToSpecifiedFrame()` для выполнения запроса.
*   `handleExprEnter(event)`: Обрабатывает нажатие клавиши Enter в полях ввода выражений. Отправляет запрос, если был нажат Enter и не зажат Shift.
*   `showDetailsPage(index)`: Обновляет таблицу результатов, отображая страницу с индексом `index`.
*   `showError(message, frameId)`: Выводит сообщение об ошибке в интерфейсе popup.
*   `genericListener(message, sender, sendResponse)`: Обработчик входящих сообщений от контент-скриптов, вызывает обработчик в `genericListener.listeners`, если он зарегистрирован.
*  `genericListener.listeners.showResultsInPopup(message, sender)`: Обрабатывает сообщение от контент-скрипта с результатами выполнения, отображает их в popup.
*   `genericListener.listeners.restorePopupState(message)`: Восстанавливает состояние popup из сохраненного состояния.
*   `genericListener.listeners.insertStyleToPopup(message)`: Вставляет стили в popup.
*   `genericListener.listeners.addFrameId(message, sender)`: Добавляет `frameId` во всплывающий список frameId.

**Объяснение:**

Этот код является частью расширения для браузера, которое позволяет пользователю выполнять XPath и CSS-запросы на веб-страницах. Он предоставляет интерфейс для ввода запросов, выбора фрейма, отображения результатов и управления видимостью различных частей интерфейса. Основной рабочий процесс:

1.  При загрузке popup-окна инициализируются все DOM-элементы, добавляются слушатели событий на кнопки, заголовки и поля ввода.
2.  Пользователь вводит XPath или CSS запрос, выбирает метод и, возможно, контекст.
3.  При нажатии на кнопку "execute", создается сообщение с запросом и отправляется в контентный скрипт, который выполняется в указанном frame.
4.  Контентный скрипт обрабатывает запрос и отправляет результаты обратно в popup.
5.  Popup отображает результаты в таблице, с возможностью просмотра отдельных деталей и навигации по страницам.
6.  При закрытии popup текущее состояние сохраняется в браузере.
7.  При открытии popup состояние восстанавливается.
8.  При нажатии на кнопку "focus item", контентный скрипт подсвечивает элемент, соответствующий индексу таблицы.

**Потенциальные ошибки и области для улучшения:**

*   Код использует устаревший способ создания объекта через `Object.create(null)`. Лучше использовать литеральную нотацию `{}` для создания обычных объектов.
*   Многократные вызовы `document.getElementById()` могут быть оптимизированы с помощью сохранения ссылок на элементы в переменных, в самом начале загрузки popup.
*   Логика получения `frameId` могла бы быть вынесена в отдельную функцию.
*   Проверка на integer в `showDetailsPage` выглядит избыточной. `Math.max` и `Math.min` уже обрабатывают невалидные входные данные.
*   Код содержит много повторяющихся действий, например, вызов `sendToSpecifiedFrame` с разным `event`, это можно улучшить через рефакторинг.
*   Не используются асинхронные функции, `async/await`, что может усложнить чтение и поддержку.
*  Обработчики событий `click` и `keypress` для заголовков можно перенести на родительский элемент, таким образом, мы избежим добавления обработчика на каждый заголовок, когда достаточно добавить один обработчик на родительский элемент.

**Взаимосвязь с другими частями проекта:**

*   `/scripts/try_xpath_functions.js`: Содержит вспомогательные функции для обработки данных и работы с DOM.
*   `/scripts/try_xpath_content.js`: Выполняется в контексте веб-страницы, обрабатывает запросы от popup и возвращает результаты.
*   Другие части проекта, которые не представлены в этом коде, могут включать настройки, стили, иконки и другие файлы, необходимые для работы расширения.

Этот анализ дает всестороннее представление о коде `popup.js`, его функциональности и связях с другими компонентами проекта.