## <алгоритм>

1.  **Инициализация:**
    *   При загрузке окна (событие `load`):
        *   Получение элементов DOM (кнопки, поля ввода, переключатели и т.д.) из HTML-документа.
        *   Установка слушателей событий для элементов (например, `click` для кнопок, `keypress` для полей ввода).
        *   Добавление заголовка таблицы для результатов и контекстных деталей (`fu.createDetailTableHeader()`).
        *   Отправка запроса на добавление стилей в popup (`requestInsertStyleToPopup`).
        *   Отправка запроса на восстановление состояния popup (`requestRestorePopupState`).

2.  **Обработка событий:**
    *   **`click` на "execute":**
        *   Создание сообщения `execute` с данными о выражениях XPath, методах и типах результатов (`makeExecuteMessage()`).
        *   Отправка сообщения в указанный фрейм (`sendToSpecifiedFrame()`).
    *   **`keypress` в полях ввода выражений (XPath):**
        *   Если нажата клавиша Enter (и не Shift), отправляется сообщение `execute`.
    *   **`click` на заголовках "context", "resolver", "frame designation", "frame id":**
        *   Изменение видимости соответствующих блоков (скрытие/показ) (`changeContextVisible`, `changeResolverVisible`, `changeFrameDesignationVisible`, `changeFrameIdVisible`).
    *   **`click` на "help-body":**
        *   Изменение видимости всех элементов с классом "help" (`changeHelpVisible`).
    *   **`click` на "focus-designated-frame":**
        *   Отправка сообщения `focusFrame` в указанный фрейм с выражением для фрейма (`frameDesignationExpression.value`).
    *   **`click` на "get-all-frame-id":**
        *   Очистка списка фреймов.
        *   Добавление опции "Manual".
        *   Запрос всех фреймов (`browser.tabs.executeScript`) и отправка им сообщения `"addFrameId"`.
    *   **`click` на "show-previous-results", "focus-frame", "show-all-results", "set-style", "reset-style", "set-all-style", "reset-all-style":**
        *   Отправка соответствующих сообщений в нужный фрейм или активную вкладку (`sendToSpecifiedFrame` или `sendToActiveTab`).
    *   **`click` на `contextTbody` (контекстная таблица):**
        *   Если кликнут `button`, отправляется сообщение `focusContextItem` в связанную вкладку, чтобы выделить элемент в контексте.
    *   **`click` на "previous-details-page", "move-details-page", "next-details-page":**
        *   Отображение соответствующей страницы деталей результатов (`showDetailsPage`).
    *   **`click` на `resultsTbody` (таблица результатов):**
        *   Если кликнута `button`, отправляется сообщение `focusItem` в связанную вкладку, чтобы выделить элемент результата.
    *   **`unload` (закрытие окна):**
        *   Сбор состояния popup (`collectPopupState()`) и отправка сообщения `storePopupState` для сохранения.
3.  **Взаимодействие с контент-скриптами:**
    *   Функция `sendToActiveTab(msg, opts)` отправляет сообщение активной вкладке.
    *   Функция `sendToSpecifiedFrame(msg)` отправляет сообщение в определенный фрейм, предварительно проверяя наличие скриптов.
    *   Функция `execContentScript()` внедряет скрипты `try_xpath_functions.js` и `try_xpath_content.js` во все фреймы.
4.  **Обработка сообщений:**
    *   Функция `genericListener` обрабатывает входящие сообщения, перенаправляя их в соответствующие обработчики:
        *   **`showResultsInPopup`**: Показывает результаты поиска в popup (сообщение, детали, количество, id фрейма).
        *   **`restorePopupState`**: Восстанавливает состояние popup из сохраненных данных.
        *   **`insertStyleToPopup`**: Добавляет стили в popup.
        *    **`addFrameId`**: Добавляет идентификатор фрейма в список идентификаторов фреймов.
5.  **Функции `showDetailsPage`:**
    *   Отображает страницу деталей в таблице результатов с учетом размера страницы и текущего индекса.
6.  **Функции `collectPopupState`:**
    *   Собирает состояние элементов интерфейса popup в объект для сохранения.
7.  **Функции `getSpecifiedFrameId`:**
    *   Определяет идентификатор фрейма на основе выбранного значения из списка или из поля ввода.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало: Загрузка popup.js] --> Initialize[Инициализация DOM элементов и слушателей событий]
    Initialize --> AddListeners[Добавление слушателей событий]
    AddListeners --> GenericListener[Установка слушателя сообщений browser.runtime.onMessage]

    GenericListener --> CheckMessageEvent{Проверка message.event}
    CheckMessageEvent -- "showResultsInPopup" --> ShowResults[Отображение результатов в popup]
    CheckMessageEvent -- "restorePopupState" --> RestoreState[Восстановление состояния popup]
    CheckMessageEvent -- "insertStyleToPopup" --> InsertStyle[Вставка стилей в popup]
    CheckMessageEvent -- "addFrameId" --> AddFrameIdToList[Добавление id фрейма в список]
    CheckMessageEvent -- Другое --> IgnoreMessage[Игнорировать сообщение]


    AddListeners --> ExecuteButtonClick{Клик на кнопке "execute"}
    ExecuteButtonClick --> MakeExecuteMessage[Создание сообщения execute]
    MakeExecuteMessage --> SendToSpecifiedFrame[Отправка сообщения в определенный фрейм]
    
    AddListeners --> KeypressOnExpression{Нажатие клавиши в полях ввода (XPath)}
     KeypressOnExpression -- Enter --> MakeExecuteMessage
     KeypressOnExpression -- Другая клавиша --> Continue[Продолжить]

    AddListeners --> ContextHeaderClick{Клик на заголовке "context"}
    ContextHeaderClick --> ChangeContextVisibility[Изменение видимости блока "context"]

    AddListeners --> ResolverHeaderClick{Клик на заголовке "resolver"}
    ResolverHeaderClick --> ChangeResolverVisibility[Изменение видимости блока "resolver"]

    AddListeners --> FrameDesignationHeaderClick{Клик на заголовке "frame designation"}
    FrameDesignationHeaderClick --> ChangeFrameDesignationVisibility[Изменение видимости блока "frame designation"]

     AddListeners --> FrameIdHeaderClick{Клик на заголовке "frame id"}
    FrameIdHeaderClick --> ChangeFrameIdVisibility[Изменение видимости блока "frame id"]

    AddListeners --> HelpBodyClick{Клик на "help-body"}
    HelpBodyClick --> ChangeHelpVisibility[Изменение видимости элементов "help"]
    
    AddListeners --> FocusDesignatedFrameClick{Клик на "focus-designated-frame"}
     FocusDesignatedFrameClick --> SendFocusDesignatedFrameMessage[Отправка сообщения focusFrame в определенный фрейм]
     
     AddListeners --> GetAllFrameIdClick{Клик на "get-all-frame-id"}
     GetAllFrameIdClick -->  ClearFrameIdList[Очистка списка id фреймов]
     ClearFrameIdList -->  AddManualFrameId[Добавление опции "manual"]
      AddManualFrameId --> RequestAllFrameId[Запрос всех id фреймов]

    AddListeners --> ShowPreviousResultsClick{Клик на "show-previous-results"}
    ShowPreviousResultsClick --> SendRequestShowResultsInPopup[Отправка запроса на показ предыдущих результатов]

    AddListeners --> FocusFrameClick{Клик на "focus-frame"}
    FocusFrameClick --> SendFocusFrameMessage[Отправка сообщения focusFrame в определенный фрейм]

    AddListeners --> ShowAllResultsClick{Клик на "show-all-results"}
     ShowAllResultsClick --> SendRequestShowAllResults[Отправка запроса на показ всех результатов]
    
    AddListeners --> SetStyleClick{Клик на "set-style"}
    SetStyleClick --> SendSetStyleMessageToFrame[Отправка сообщения setStyle в определенный фрейм]
     
     AddListeners --> ResetStyleClick{Клик на "reset-style"}
     ResetStyleClick --> SendResetStyleMessageToFrame[Отправка сообщения resetStyle в определенный фрейм]

    AddListeners --> SetAllStyleClick{Клик на "set-all-style"}
    SetAllStyleClick --> SendSetStyleMessageToActiveTab[Отправка сообщения setStyle в активную вкладку]
     
      AddListeners --> ResetAllStyleClick{Клик на "reset-all-style"}
     ResetAllStyleClick --> SendResetStyleMessageToActiveTab[Отправка сообщения resetStyle в активную вкладку]

    AddListeners --> ContextTbodyClick{Клик на таблице contextTbody}
    ContextTbodyClick -- "Клик на button" --> SendFocusContextItemMessage[Отправка сообщения focusContextItem]
    ContextTbodyClick -- Другой клик --> Continue

    AddListeners --> PreviousDetailsPageClick{Клик на "previous-details-page"}
    PreviousDetailsPageClick --> ShowPreviousDetailsPage[Отображение предыдущей страницы деталей]

    AddListeners --> MoveDetailsPageClick{Клик на "move-details-page"}
    MoveDetailsPageClick --> ShowSelectedDetailsPage[Отображение выбранной страницы деталей]

    AddListeners --> NextDetailsPageClick{Клик на "next-details-page"}
    NextDetailsPageClick --> ShowNextDetailsPage[Отображение следующей страницы деталей]

    AddListeners --> ResultsTbodyClick{Клик на таблице resultsTbody}
    ResultsTbodyClick -- "Клик на button" --> SendFocusItemMessage[Отправка сообщения focusItem]
    ResultsTbodyClick -- Другой клик --> Continue
     
    AddListeners --> UnloadWindow{Закрытие popup}
     UnloadWindow --> CollectPopupState[Сбор состояния popup]
     CollectPopupState --> StorePopupState[Отправка сообщения для сохранения состояния]
   
    SendToSpecifiedFrame --> CheckContentScript[Проверка на наличие try_xpath скриптов]
     CheckContentScript -- "Скрипты не найдены"--> ExecContentScript[Внедрение скриптов try_xpath_functions.js и try_xpath_content.js]
     CheckContentScript -- "Скрипты найдены"--> SendMessageToFrame[Отправка сообщения в указанный frame]
     
    ExecContentScript --> SendMessageToFrame
    SendMessageToFrame -->  HandleResponseFromFrame[Обработка ответа фрейма]
    
    ShowResults --> UpdateResultsDisplay[Обновление интерфейса с результатами]
    RestoreState --> ApplyPopupState[Применение сохраненного состояния]
    InsertStyle --> AddStyleToHead[Добавление стилей в head]
    AddFrameIdToList --> AppendFrameId[Добавление id фрейма в список]
     ShowPreviousDetailsPage --> ShowDetailsPage
     ShowSelectedDetailsPage --> ShowDetailsPage
      ShowNextDetailsPage --> ShowDetailsPage

    SendRequestShowResultsInPopup --> SendMessageToFrame
     SendFocusDesignatedFrameMessage --> SendMessageToFrame
    SendRequestShowAllResults --> SendMessageToFrame
    SendFocusFrameMessage --> SendMessageToFrame
    SendSetStyleMessageToFrame --> SendMessageToFrame
    SendResetStyleMessageToFrame --> SendMessageToFrame
    SendSetStyleMessageToActiveTab --> SendMessageToActiveTab
     SendResetStyleMessageToActiveTab --> SendMessageToActiveTab
     SendFocusContextItemMessage --> SendMessageToFrame
     SendFocusItemMessage --> SendMessageToFrame
        StorePopupState --> SendMessageToBackground[Отправка сообщения в background.js]
     
      SendMessageToActiveTab --> HandleResponseFromActiveTab[Обработка ответа активной вкладки]
    
```

## <объяснение>

### Импорты:
-   `tryxpath` и `tryxpath.functions`: Предположительно, это пользовательские модули, которые предоставляют функциональность для работы с XPath и другими операциями, связанными с поиском элементов на веб-странице. Вероятно, что `tryxpath` это основной модуль, а `tryxpath.functions` это модуль с различными утилитами. `tryxpath` в данном коде,  объявлен как `tx`,  а  `tryxpath.functions` как `fu`. Так же, как можно предположить, данные библиотеки располагаются в том же пакете `src`.
-  `browser` - это API браузера, предоставляющее доступ к функциям расширения (вкладки, сообщения и т.д.).

### Переменные:
-   `noneClass`, `helpClass`: Строковые константы для CSS-классов. Используются для управления видимостью элементов (например, `.none` для скрытия).
-   `invalidTabId`, `invalidExecutionId`, `invalidFrameId`: Константы, представляющие некорректные значения для идентификаторов.
-   `mainWay`, `mainExpression`, `contextCheckbox` и др.: Переменные для хранения ссылок на DOM-элементы (поля ввода, кнопки, списки и т. д.).
-   `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для отслеживания текущей вкладки, фрейма и идентификатора выполнения.
-   `resultedDetails`: Массив для хранения деталей результатов XPath.
-   `detailsPageSize`, `detailsPageIndex`: Константы и переменные для пагинации результатов.
-   `window`: Ссылка на глобальный объект `window`.

### Функции:
-   `sendToActiveTab(msg, opts)`:
    *   **Аргументы**:
        *   `msg` (Object): Объект сообщения для отправки.
        *   `opts` (Object, опционально): Дополнительные опции для отправки сообщения.
    *   **Возвращает**: `Promise`: Промис, разрешающийся после отправки сообщения.
    *   **Назначение**: Отправляет сообщение активной вкладке текущего окна. Сначала получает активную вкладку, а затем отправляет сообщение, используя `browser.tabs.sendMessage`.
    *   **Пример:**
        ```javascript
        sendToActiveTab({ event: "myEvent", data: "someData" })
          .then(() => console.log("Сообщение отправлено"));
        ```
-   `sendToSpecifiedFrame(msg)`:
    *   **Аргументы**:
        *   `msg` (Object): Объект сообщения для отправки.
    *   **Возвращает**: `Promise`: Промис, разрешающийся после отправки сообщения или в случае ошибки.
    *   **Назначение**: Отправляет сообщение в определенный фрейм. Перед отправкой проверяет наличие скрипта `try_xpath_check_frame.js` в указанном фрейме. Если скрипта нет, то внедряет `try_xpath_functions.js` и `try_xpath_content.js` скрипты.
        *   Если произошла ошибка при отправке сообщения, выводит сообщение об ошибке `showError`.
    *   **Пример:**
    ```javascript
    sendToSpecifiedFrame({event:"doSomething", value: "test"})
      .then(() => console.log("Сообщение отправлено в определенный frame"));
    ```
-   `collectPopupState()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: `Object`: Объект с состоянием popup.
    *   **Назначение**: Собирает состояние всех элементов управления popup для дальнейшего сохранения.
-   `changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: Нет.
    *   **Назначение**: Управляют видимостью соответствующих блоков popup, добавляя или удаляя CSS-класс `none`.
-   `makeExecuteMessage()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: `Object`: Объект сообщения для события `execute` с данными из полей ввода.
    *   **Назначение**: Создает сообщение с данными из полей ввода для отправки контент скрипту. Сообщение содержит выражения XPath, методы и т.д. в зависимости от выбранных опций в popup.
-    `getSpecifiedFrameId()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: `Number`: Идентификатор фрейма.
    *   **Назначение**: Получает идентификатор фрейма из списка или поля ввода в зависимости от выбранных параметров.
-   `execContentScript()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: `Promise`: Промис, разрешающийся после внедрения скриптов.
    *   **Назначение**: Внедряет скрипты `try_xpath_functions.js` и `try_xpath_content.js` во все фреймы текущей вкладки.
-   `sendExecute()`:
    *   **Аргументы**: Нет.
    *   **Возвращает**: Нет.
    *   **Назначение**: Отправляет сообщение `execute` в указанный фрейм, вызывая функцию `sendToSpecifiedFrame`.
-   `handleExprEnter(event)`:
    *   **Аргументы**: `event` (Event): Объект события.
    *   **Возвращает**: Нет.
    *   **Назначение**: Обрабатывает нажатие клавиши Enter в полях ввода выражений. Если нажата Enter (и не Shift), вызывает `sendExecute()` для отправки запроса.
-   `showDetailsPage(index)`:
    *   **Аргументы**: `index` (Number): Индекс страницы для отображения.
    *   **Возвращает**: Нет.
    *   **Назначение**: Отображает страницу деталей результатов на основе заданного индекса. Ограничивает индекс, чтобы он не выходил за границы массива результатов. Использует `fu.updateDetailsTable` для обновления таблицы и управляет прокруткой страницы.
-   `showError(message, frameId)`:
    *   **Аргументы**:
        *   `message` (String): Сообщение об ошибке.
        *   `frameId` (Number): Идентификатор фрейма, где произошла ошибка.
    *   **Возвращает**: Нет.
    *   **Назначение**: Выводит сообщение об ошибке в popup и сбрасывает связанные данные.
-   `genericListener(message, sender, sendResponse)`:
    *   **Аргументы**:
        *   `message` (Object): Объект сообщения.
        *   `sender` (Object): Объект отправителя сообщения.
        *   `sendResponse` (Function): Функция для отправки ответа.
    *   **Возвращает**: Зависит от обработчика
    *   **Назначение**: Принимает сообщения от `browser.runtime.onMessage` и перенаправляет их в соответствующий обработчик на основе `message.event`.
    *   **Пример:**
        ```javascript
        // ...
        genericListener.listeners.showResultsInPopup = function (message, sender){
            // Обработка сообщения
        };
        // ...
        browser.runtime.onMessage.addListener(genericListener);
        ```
    - `genericListener.listeners.showResultsInPopup`:
        *   **Назначение**: Отображает результаты поиска, полученные от контент-скрипта.
    - `genericListener.listeners.restorePopupState`:
        *   **Назначение**: Восстанавливает состояние popup из сохраненных данных.
    - `genericListener.listeners.insertStyleToPopup`:
        *   **Назначение**: Добавляет стили в popup.
    - `genericListener.listeners.addFrameId`:
        *   **Назначение**: Добавляет идентификатор фрейма в список идентификаторов фреймов.

### Потенциальные проблемы и области для улучшения:
-   **Обработка ошибок**: В коде есть обработка ошибок в `sendToSpecifiedFrame`, но в остальных местах, где используются Promise, нет явной обработки ошибок. Это может привести к необработанным исключениям.
-   **Производительность**: Функция `changeHelpVisible` перебирает все элементы с классом `help`, что может быть неэффективно при большом количестве таких элементов.
-   **Код повторяется**:  Много схожего кода для `click` и `keypress` слушателей. Возможно, следует вынести в функцию.
-   **Сложная логика**: Функция `genericListener` имеет сложную логику, которая может стать сложнее с добавлением новых сообщений. Можно было бы использовать более модульный подход.
-   **Зависимость от DOM**: Код имеет сильную зависимость от DOM-структуры popup. Изменение HTML-документа может привести к поломке кода.

### Цепочка взаимосвязей с другими частями проекта:
1.  **`popup.js`** -> **`try_xpath_content.js`**: `popup.js` отправляет сообщения с инструкциями для `try_xpath_content.js` (например, execute, focusItem, focusContextItem).  `try_xpath_content.js` отправляет сообщения с результатами обратно в `popup.js`.
2.  **`popup.js`** -> **`try_xpath_functions.js`**:  `popup.js` внедряет скрипт `try_xpath_functions.js`, но прямого взаимодействия нет. `try_xpath_functions.js` выполняет вспомогательные функции (например, создает структуру таблицы) по запросу от `popup.js`.
3.  **`popup.js`** -> **`background.js`**:  `popup.js` отправляет сообщения `storePopupState`,  `requestInsertStyleToPopup`, `requestRestorePopupState`  в `background.js` для сохранения состояния и других операций.
4.  **`popup.js`** -> **`try_xpath_check_frame.js`**: `popup.js` использует `try_xpath_check_frame.js` для проверки, был ли уже внедрен скрипт в iframe перед отправкой сообщения.
5. **`popup.html`** -> **`popup.js`**: HTML документ (popup) загружает  `popup.js`, которая ищет DOM элементы в HTML и управляет ими.

**Общее описание:**

`popup.js` выступает в роли контроллера для popup-интерфейса расширения. Он получает пользовательский ввод, отправляет сообщения в контент-скрипты (вкладки и фреймы), обрабатывает ответы от них и обновляет интерфейс popup. Также сохраняет и восстанавливает состояние popup, взаимодействуя с `background.js`.