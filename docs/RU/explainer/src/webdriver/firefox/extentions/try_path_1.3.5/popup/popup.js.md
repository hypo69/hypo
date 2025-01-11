## <алгоритм>

1. **Инициализация:**
   -  Устанавливаются константы и переменные, включая ссылки на элементы DOM, идентификаторы, массивы для хранения результатов и текущий индекс страницы.
   -  Устанавливаются значения по умолчанию для `relatedTabId`, `relatedFrameId` и `executionId`.
2.  **`sendToActiveTab(msg, opts)`:**
    - Получает активную вкладку текущего окна.
    - Отправляет сообщение `msg` в активную вкладку с указанными опциями `opts`.
    - Пример: `sendToActiveTab({"event": "execute", "data": {}}, {"frameId": 1})` отправит сообщение `{"event": "execute", "data": {}}` во фрейм с идентификатором 1 в активной вкладке.
3.  **`sendToSpecifiedFrame(msg)`:**
    - Определяет идентификатор фрейма с помощью `getSpecifiedFrameId()`.
    - Выполняет скрипт `try_xpath_check_frame.js` в указанном фрейме, чтобы проверить инициализацию.
    - Если скрипт не был инициализирован, выполняет скрипты `try_xpath_functions.js` и `try_xpath_content.js` во всех фреймах.
    - После выполнения скрипта отправляет сообщение с событием `initializeBlankWindows` в активную вкладку.
    - Отправляет сообщение `msg` в указанный фрейм.
    - Обрабатывает ошибку и выводит сообщение об ошибке, если фрейм не найден.
    - Пример: `sendToSpecifiedFrame({"event": "execute", "xpath": "//div"})` отправит сообщение с запросом выполнения xpath в указанный фрейм.
4. **`collectPopupState()`:**
    - Собирает состояние всех элементов управления (флажки, выпадающие списки, текстовые поля) и возвращает объект со всеми значениями.
    - Например,  `{ helpCheckboxChecked: true, mainWayIndex: 0, mainExpressionValue: "//div", ... }`.
5.  **`changeContextVisible()` , `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`:**
    - Переключают видимость соответствующих разделов на основе состояния флажков.
    - Добавляют или удаляют класс `none` для скрытия/отображения элементов.
    - Пример: если `contextCheckbox` установлен, `contextBody` будет виден, иначе скрыт.
6.  **`changeHelpVisible()`:**
    - Переключает видимость элементов с классом `help` на основе состояния флажка `helpCheckbox`.
    - Пример: Если `helpCheckbox` установлен, все элементы с классом `help` будут видимы, иначе скрыты.
7.  **`makeExecuteMessage()`:**
    - Создает сообщение для выполнения XPath-запроса, включая выражения, метод, тип результата и резолвер (если указано).
    - Заполняет сообщение данными из полей ввода и выпадающих списков.
    - Пример: `{ event: "execute", main: { expression: "//div", method: "evaluate", resultType: "ANY_TYPE", resolver: null }, context: { expression: ".//span", method: "evaluate", resultType: "ANY_TYPE", resolver: null } }`
8.  **`getSpecifiedFrameId()`:**
    - Получает идентификатор фрейма, основываясь на выбранном варианте из `frameIdList` или значении из `frameIdExpression`.
    - Если фрейм не выбран, возвращает 0.
    - Если выбрано ручное указание, преобразует значение из текстового поля в число.
    - Пример: Если выбран `frameId` из списка, возвращает его, если выбрано ручное указание, возвращает введенное значение, иначе `0`.
9.  **`execContentScript()`:**
    - Выполняет скрипты `try_xpath_functions.js` и `try_xpath_content.js` во всех фреймах текущей вкладки.
10. **`sendExecute()`:**
    - Вызывает `sendToSpecifiedFrame()` с сообщением, сгенерированным `makeExecuteMessage()`.
11. **`handleExprEnter(event)`:**
    - Обрабатывает нажатие клавиши Enter в полях ввода.
    - Если Enter нажат без Shift, вызывает `sendExecute()` и предотвращает дальнейшее выполнение стандартного действия браузера.
12. **`showDetailsPage(index)`:**
    - Вычисляет максимальный индекс страницы, исходя из размера страницы `detailsPageSize` и количества результатов в `resultedDetails`.
    - Обновляет таблицу результатов, отображая результаты для указанной страницы с помощью `fu.updateDetailsTable()`.
    - Обновляет индекс страницы в `detailsPageIndex`.
    - Восстанавливает позицию скролла.
13. **`showError(message, frameId)`:**
     - Сбрасывает переменные `relatedTabId`, `relatedFrameId`, `executionId`.
     - Отображает сообщение об ошибке, очищает таблицу и устанавливает количество результатов в 0.
14. **`genericListener(message, sender, sendResponse)`:**
     -  Обрабатывает сообщения, полученные от контент скриптов или из других частей расширения.
     -  Вызывает соответствующий обработчик события из `genericListener.listeners`, если он существует.
15. **`genericListener.listeners.showResultsInPopup(message, sender)`:**
    -  Получает данные о результатах из сообщения.
    -  Обновляет результаты на панели.
    -  Вызывает `showDetailsPage` для отображения первой страницы.
16. **`genericListener.listeners.restorePopupState(message)`:**
    -  Восстанавливает состояние элементов управления из сохраненного состояния, полученного в сообщении.
    -  Вызывает `changeHelpVisible()`, `changeContextVisible()`, `changeResolverVisible()`, `changeFrameDesignationVisible()` и `changeFrameIdVisible()` для отображения сохраненного состояния.
    -  Отправляет сообщение для запроса результатов, если это необходимо.
17.  **`genericListener.listeners.insertStyleToPopup(message)`:**
    - Вставляет стили, переданные в сообщении, в `head` документа.
18. **`genericListener.listeners.addFrameId(message, sender)`:**
    - Добавляет новый пункт в список выбора фреймов (`frameIdList`) с ID фрейма, полученного из сообщения.
19. **Обработчики событий DOM (при загрузке страницы):**
    - Получают ссылки на элементы DOM.
    - Назначают обработчики событий для элементов управления (кнопки, текстовые поля, заголовки).
    - Обработчики событий включают:
       -  `sendExecute`: отправляет запрос на выполнение XPath-запроса.
       - `handleExprEnter`: отправляет запрос при нажатии Enter.
       -  `changeContextVisible`, `changeResolverVisible`, `changeFrameIdVisible`, `changeFrameDesignationVisible` : управляют видимостью соответствующих разделов.
       -  Обработчики для кнопок "previous-details-page", "move-details-page", "next-details-page": управляют переключением страниц с результатами.
       -  Обработчики для кнопок фокуса, стилей, получения фреймов.
       - Обработчик для `resultsTbody`: обрабатывает нажатие на кнопки детальной информации по элементу.
       -  Обработчик для `contextTbody`: обрабатывает нажатие на кнопки детальной информации по контекстному элементу.
    -  Добавляют слушатель события `unload` для сохранения состояния панели.
    -  Вызывают `fu.createDetailTableHeader()` для создания заголовков таблиц.
    - Отправляют запросы на вставку стилей и восстановление состояния.

## <mermaid>

```mermaid
flowchart TD
    Start[Загрузка страницы popup.html] --> Init[Инициализация переменных и элементов DOM]
    Init --> EventListeners[Установка обработчиков событий DOM]
    EventListeners --> SendExecuteClick[Клик на кнопке "Выполнить"]
    EventListeners --> EnterInExpr[Нажатие Enter в поле ввода]
    EventListeners --> ChangeVisibilityClick[Клик на заголовках для переключения видимости разделов]
    EventListeners --> PageNavigationClick[Клик на кнопках для навигации по страницам]
    EventListeners --> FocusFrameButtonClick[Клик на кнопках фокуса фрейма]
    EventListeners --> StyleButtonsClick[Клик на кнопках установки и сброса стилей]
    EventListeners --> GetFrameIdClick[Клик на кнопке получения frameId]
     EventListeners --> Unload[Событие unload]
    
     Unload --> CollectState[Сбор состояния элементов управления]
    CollectState --> SendStoreState[Отправка сообщения storePopupState]
    
    GetFrameIdClick --> SendAddFrameId[Отправка сообщения для получения всех frameId]

    SendAddFrameId --> genericListenerAddFrameId[Обработка сообщения addFrameId]
    genericListenerAddFrameId --> AddFrameIdToSelect[Добавление FrameId в список выбора]


    SendExecuteClick --> MakeExecuteMessage[Создание сообщения для выполнения]
    EnterInExpr --> MakeExecuteMessage
    MakeExecuteMessage --> SendToSpecifiedFrame[Отправка сообщения в указанный фрейм]
    FocusFrameButtonClick --> SendToSpecifiedFrame
    StyleButtonsClick --> SendToSpecifiedFrame
    

    ChangeVisibilityClick --> ChangeVisibility[Изменение видимости разделов (context, resolver, frameId)]
    
    SendToSpecifiedFrame --> CheckFrame[Проверка инициализации фрейма]
    CheckFrame -- init not complete --> ExecContentScripts[Выполнение контент-скриптов]
    CheckFrame -- init complete --> SendExecuteMessageToFrame[Отправка сообщения в фрейм]
    ExecContentScripts --> SendExecuteMessageToFrame
    SendExecuteMessageToFrame -->  genericListenerShowResults[Обработка сообщений showResultsInPopup в popup.js]
    
    PageNavigationClick --> ShowDetails[Обновление таблицы результатов для заданной страницы]

     genericListenerShowResults --> UpdatePopupUI[Обновление UI попапа]
    UpdatePopupUI --> ShowDetails
    
    genericListener[genericListener(message, sender, sendResponse)] --> genericListenerShowResults
    genericListener --> genericListenerRestoreState[Обработка сообщения restorePopupState в popup.js]
     genericListener --> genericListenerInsertStyleToPopup[Обработка сообщения insertStyleToPopup в popup.js]
     
     genericListenerRestoreState --> RestoreState[Восстановление состояния элементов управления]
    RestoreState --> ChangeVisibility
    
    
    genericListenerInsertStyleToPopup --> InsertStyle[Вставка стилей в попап]

```
### Зависимости Mermaid:

-   `Start` - начало работы скрипта, инициированное загрузкой `popup.html`.
-   `Init` - переменные, необходимые для работы, и ссылки на DOM-элементы.
-   `EventListeners` - привязывает функции к событиям DOM, инициированным пользователем.
-   `SendExecuteClick` - событие клика на кнопке "Выполнить", которое запускает поиск элементов.
-  `EnterInExpr` - событие нажатия клавиши Enter в текстовых полях.
-   `ChangeVisibilityClick` - событие клика по заголовкам, управляет видимостью секций.
-   `PageNavigationClick` - событие клика на кнопках пагинации, для просмотра страниц с результатами.
-   `FocusFrameButtonClick` - событие клика на кнопках для фокуса элементов во фреймах.
- `StyleButtonsClick` - событие клика на кнопках, связанных с установкой или сбросом стилей.
-   `GetFrameIdClick` - событие клика по кнопке для получения всех фреймов на странице.
-   `Unload` - событие выгрузки страницы, используется для сохранения состояния.
-   `CollectState` -  функция сбора состояния элементов для последующего восстановления.
-   `SendStoreState` - отправка сообщения `storePopupState` для сохранения состояния.
-   `SendAddFrameId` - отправка сообщения `addFrameId` для получения всех id фреймов на странице.
-   `genericListenerAddFrameId` - Обработчик сообщения для добавления frameId в select.
-   `AddFrameIdToSelect` - Добавление frameId в список выбора.
-   `MakeExecuteMessage` - создает объект сообщения для отправки с данными о запросе.
-   `SendToSpecifiedFrame` - функция отправки сообщения в конкретный фрейм.
-   `CheckFrame` - проверка инициализации скриптов во фрейме.
-   `ExecContentScripts` - выполнение контент скриптов в целевой вкладке.
-  `SendExecuteMessageToFrame` - отправка сформированного сообщения на конкретный фрейм.
-   `ChangeVisibility` -  функция переключения видимости разделов попапа.
-   `ShowDetails` - функция для отображения данных на конкретной странице.
-   `genericListener` - обработчик для сообщений, полученных из контент скриптов.
-   `genericListenerShowResults` - обработчик сообщений с результатами поиска в попапе.
-   `UpdatePopupUI` - функция обновления UI попапа
- `genericListenerRestoreState` - обработчик сообщения для восстановления состояния попапа.
- `genericListenerInsertStyleToPopup` - обработчик сообщения для вставки стилей.
- `RestoreState` -  функция для восстановления состояния попапа.
- `InsertStyle` - функция для вставки стилей в head.

## <объяснение>

### Импорты
В данном коде импорты как таковые отсутствуют, так как это standalone скрипт, работающий в контексте расширения браузера. Он использует глобальные объекты, предоставляемые браузером, такие как `browser`, `window`, `document`.  Также используется переменная `tryxpath`, предполагается, что она определена в контексте выполнения.

### Функции:

*   **`sendToActiveTab(msg, opts)`**:
    *   **Назначение**: Отправляет сообщение `msg` на активную вкладку текущего окна.
    *   **Аргументы**:
        *   `msg`: Объект, представляющий сообщение для отправки.
        *   `opts`: Необязательный объект с опциями для `browser.tabs.sendMessage`.
    *   **Возвращаемое значение**: `Promise`, который разрешается после отправки сообщения.
    *   **Пример**: `sendToActiveTab({event: 'execute', xpath: '//div'}, {frameId: 0})` - отправит сообщение `{'event': 'execute', 'xpath': '//div'}` в активную вкладку в фрейм 0.

*   **`sendToSpecifiedFrame(msg)`**:
    *   **Назначение**: Отправляет сообщение `msg` в конкретный фрейм, определенный функцией `getSpecifiedFrameId()`.
    *   **Аргументы**:
        *   `msg`: Объект, представляющий сообщение для отправки.
    *   **Возвращаемое значение**: `Promise`, который разрешается после отправки сообщения.
    *   **Пример**: `sendToSpecifiedFrame({event: 'focus', index: 2})` - отправит сообщение на фокусировку 2-го элемента.

*   **`collectPopupState()`**:
    *   **Назначение**: Собирает текущее состояние всех элементов управления на панели (чекбоксы, выпадающие списки, текстовые поля).
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Объект, содержащий состояние элементов управления.
    *   **Пример**: `{helpCheckboxChecked: false, mainWayIndex: 1, mainExpressionValue: '//a', ...}`.

*   **`changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`**:
    *   **Назначение**: Управляют видимостью соответствующих разделов на панели в зависимости от состояния чекбоксов.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Пример**: Если чекбокс `contextCheckbox` установлен, то `contextBody` будет показан.

*   **`changeHelpVisible()`**:
    *   **Назначение**: Управляет видимостью элементов с классом `help` в зависимости от состояния чекбокса `helpCheckbox`.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.

*   **`makeExecuteMessage()`**:
    *   **Назначение**: Создает объект сообщения для отправки в контентный скрипт с данными для выполнения XPath-запроса.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Объект сообщения.
    *   **Пример**: `{event: 'execute', main: {expression: '//div', method: 'evaluate', resultType: 'ANY_TYPE', resolver: null}, context: null}`.

*   **`getSpecifiedFrameId()`**:
    *   **Назначение**: Возвращает ID фрейма, на который будет отправлен запрос.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: ID фрейма в виде числа. Может вернуть `0`, если фрейм не выбран.
    *   **Пример**: Возвращает `0` если не выбран фрейм, `1` если выбран фрейм с id 1 или `25` если выбран ручной ввод и значение равно 25.

*   **`execContentScript()`**:
    *   **Назначение**: Выполняет скрипты `try_xpath_functions.js` и `try_xpath_content.js` во всех фреймах текущей вкладки.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: `Promise`, который разрешается после выполнения скриптов.

*   **`sendExecute()`**:
    *   **Назначение**: Отправляет запрос на выполнение XPath-запроса, вызывая `sendToSpecifiedFrame()` с сообщением, созданным `makeExecuteMessage()`.
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.

*    **`handleExprEnter(event)`**:
     *    **Назначение**: Обрабатывает нажатие клавиши Enter в полях ввода.
     *    **Аргументы**: `event` - объект события.
     *    **Возвращаемое значение**: Нет.

*   **`showDetailsPage(index)`**:
    *   **Назначение**: Обновляет таблицу результатов на странице, отображая конкретную страницу данных.
    *   **Аргументы**: `index` - индекс страницы.
    *   **Возвращаемое значение**: Нет.

*  **`showError(message, frameId)`**:
     *   **Назначение**: Выводит сообщение об ошибке и сбрасывает состояние панели.
     *    **Аргументы**:
         *   `message` - текст сообщения об ошибке.
         *   `frameId` - id фрейма, в котором произошла ошибка.
     *   **Возвращаемое значение**: Нет.

*   **`genericListener(message, sender, sendResponse)`**:
    *   **Назначение**: Общий обработчик сообщений, полученных из контентных скриптов.
    *   **Аргументы**:
        *   `message`: Объект сообщения.
        *   `sender`: Объект с информацией об отправителе сообщения.
        *   `sendResponse`: Функция для отправки ответа.
    *   **Возвращаемое значение**: Результат выполнения обработчика, соответствующего событию.

*   **`genericListener.listeners.showResultsInPopup(message, sender)`**:
    *   **Назначение**: Обрабатывает сообщения с результатами выполнения XPath-запроса, полученными от контентного скрипта.
    *   **Аргументы**:
        *   `message`: Объект сообщения с результатами.
        *   `sender`: Объект с информацией об отправителе.
    *   **Возвращаемое значение**: Нет.

*   **`genericListener.listeners.restorePopupState(message)`**:
    *   **Назначение**: Обрабатывает сообщение, которое восстанавливает состояние элементов управления.
    *   **Аргументы**:
        *   `message`: Объект сообщения с сохраненным состоянием.
    *   **Возвращаемое значение**: Нет.

*   **`genericListener.listeners.insertStyleToPopup(message)`**:
   *   **Назначение**: Обрабатывает сообщение, вставляет стили в popup.
   *   **Аргументы**:
       *   `message`: Объект сообщения с css стилями.
    *   **Возвращаемое значение**: Нет.

*   **`genericListener.listeners.addFrameId(message, sender)`**:
    *    **Назначение**: Добавляет ID фрейма в список выбора фреймов.
    *    **Аргументы**:
        *    `message`: Объект сообщения.
        *    `sender`: Объект с информацией об отправителе сообщения.
    *    **Возвращаемое значение**: Нет.

### Переменные:

*   `tx`, `fu`: Алиасы для `tryxpath` и `tryxpath.functions`.
*   `document`: Ссылка на объект `document` текущей панели.
*   `noneClass`, `helpClass`: Строковые константы для CSS классов.
*   `invalidTabId`, `invalidExecutionId`, `invalidFrameId`: Константы для обозначения неверных идентификаторов.
*   `mainWay`, `mainExpression` и т.д.: Ссылки на DOM элементы управления.
*   `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения информации о текущем запросе.
*   `resultedDetails`: Массив для хранения детальной информации о результатах.
*   `detailsPageSize`, `detailsPageIndex`: Переменные для управления постраничным выводом результатов.

### Потенциальные ошибки и области для улучшения:

*   **Обработка ошибок**: Ошибки обрабатываются в основном с помощью `catch(fu.onError)`. Желательно добавить более подробную обработку ошибок, с выводом пользовательских сообщений.
*   **Асинхронность**: Код активно использует промисы, что в целом хорошо. Однако, следует убедиться, что все асинхронные операции обрабатываются корректно, чтобы избежать race conditions.
*   **Управление состоянием**: Переменные состояния (например, `relatedTabId`, `executionId`) хранятся в глобальной области видимости. Использование более структурированного подхода, например, через объект или класс, может улучшить читаемость и поддерживаемость кода.
*   **Безопасность**: Следует обратить внимание на безопасность при выполнении `executeScript`. Передаваемые значения должны быть экранированы.
*   **Интернационализация**: Текстовые сообщения в UI панели не интернационализированы.

### Взаимосвязи с другими частями проекта:

*   **`try_xpath_functions.js` и `try_xpath_content.js`**: Эти скрипты выполняются в контексте контентной страницы и содержат логику для выполнения XPath запросов и взаимодействия с DOM.
*   **`browser.runtime.sendMessage`**: Используется для обмена сообщениями между popup.js, фоновым скриптом, и контентными скриптами.
*   **`browser.tabs.executeScript`**: Используется для внедрения скриптов в веб-страницы.
*   **Фоновый скрипт**: Скорее всего, присутствует фоновый скрипт, который управляет состоянием и взаимодействием между панелью и контентным скриптом.

Этот скрипт является центральной частью панели инструментов для работы с XPath, позволяя пользователю настраивать запросы и отображать результаты. Он взаимодействует с контентными скриптами, чтобы выполнить запросы и обрабатывать результаты.