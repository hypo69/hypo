# Документация для файла popup.js

## Обзор

Файл `popup.js` содержит код для всплывающего окна расширения, управляющего взаимодействием с активной вкладкой и выполнением XPath-запросов. Он обрабатывает ввод пользователя, отправляет запросы в активную вкладку, отображает результаты, а также управляет состоянием всплывающего окна.


## Переменные

В этом разделе описаны глобальные переменные, используемые в коде.

### `noneClass`, `helpClass`

Строковые константы, используемые для добавления/удаления классов `none` и `help` к элементам страницы, контролируя их видимость.

### `invalidTabId`, `invalidExecutionId`, `invalidFrameId`

Константы, представляющие значения, указывающие на отсутствие валидного значения для идентификатора вкладки, выполнения и фрейма соответственно.

### `mainWay`, `mainExpression`, `contextCheckbox`, `contextHeader`, `contextBody`, `contextWay`, `contextExpression`, `resolverHeader`, `resolverBody`, `resolverCheckbox`, `resolverExpression`, `frameDesignationHeader`, `frameDesignationCheckbox`, `frameDesignationBody`, `frameDesignationExpression`, `frameIdHeader`, `frameIdCheckbox`, `frameIdBody`, `frameIdList`, `frameIdExpression`, `resultsMessage`, `resultsTbody`, `contextTbody`, `resultsCount`, `resultsFrameId`, `detailsPageCount`, `helpBody`, `helpCheckbox`

Переменные, ссылающиеся на DOM-элементы всплывающего окна, используемые для отображения, ввода и управления взаимодействием с пользователем.

### `relatedTabId`, `relatedFrameId`, `executionId`, `resultedDetails`, `detailsPageSize`, `detailsPageIndex`

Переменные, хранящие текущие данные о связанной вкладке, фрейме, выполнении, результатах поиска, размере страницы с результатами, текущей странице с результатами.


## Функции

### `sendToActiveTab(msg, opts)`

**Описание**: Отправляет сообщение `msg` в активную вкладку.

**Параметры**:
- `msg` (object): Сообщение, которое необходимо отправить.
- `opts` (object, необязательно): Дополнительные параметры. По умолчанию `{}`.

**Возвращает**:
- `Promise`: Обещание, возвращающее результат выполнения `browser.tabs.sendMessage`.


### `sendToSpecifiedFrame(msg)`

**Описание**: Отправляет сообщение `msg` в указанный фрейм активной вкладки.

**Параметры**:
- `msg` (object): Сообщение, которое необходимо отправить.

**Возвращает**:
- `Promise`: Обещание, возвращающее результат выполнения.

**Обрабатывает исключения**:
- `e`: Обработка ошибки при выполнении `browser.tabs.executeScript`.


### `collectPopupState()`

**Описание**: Считывает текущее состояние всплывающего окна и возвращает его в виде объекта.

**Возвращает**:
- `object`: Объект, содержащий значения элементов ввода и состояние флагов.


### `changeContextVisible()`

**Описание**: Управляет отображением блока `context-body` в зависимости от состояния `contextCheckbox`.

### `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`

**Описание**: Аналогичные функции для управления отображением других блоков (resolver, frameId, frameDesignation, help).


### `makeExecuteMessage()`

**Описание**: Формирует сообщение, содержащее данные для выполнения XPath-запроса.

**Возвращает**:
- `object`: Сообщение для выполнения XPath.

**Обрабатывает исключения**:
- `e`: Обработка ошибки при формировании сообщения.


### `getSpecifiedFrameId()`

**Описание**: Получает идентификатор фрейма, указанный в поле frameId.

**Возвращает**:
- `number`: ID указанного фрейма.

### `execContentScript()`

**Описание**: Выполняет скрипты в содержимом активной вкладки.

**Возвращает**:
- `Promise`: Обещание, завершающееся после выполнения скриптов.


### `sendExecute()`

**Описание**: Отправляет сформированное сообщение для выполнения XPath-запроса в активный фрейм.


### `handleExprEnter(event)`

**Описание**: Обрабатывает нажатие клавиши Enter в поле ввода выражения.

**Параметры**:
- `event` (object): Объект события нажатия клавиши.


### `showDetailsPage(index)`

**Описание**: Отображает результаты XPath-запроса на заданной странице.

**Параметры**:
- `index` (number): Номер страницы результатов (индекс).


### `showError(message, frameId)`

**Описание**: Отображает сообщение об ошибке.

**Параметры**:
- `message` (string): Текст сообщения об ошибке.
- `frameId` (string): ID фрейма, к которому относится ошибка.

**Обрабатывает исключения**:
- `fu.onError`:  Обработка ошибок при обновлении таблиц.


### `genericListener(message, sender, sendResponse)`

**Описание**: Обработчик сообщений из других частей расширения.


## Обработчики событий

В этом разделе описаны обработчики событий, привязанные к элементам DOM.

Обработчики событий для элементов ввода (`mainExpression`, `contextExpression`, `resolverExpression`, `frameDesignationExpression`, `frameIdExpression`) настраивают выполнение запроса при нажатии Enter.

Обработчики для кнопок (`execute`, `get-all-frame-id`, `show-previous-results`, `focus-frame`, `show-all-results`, `open-options`, `set-style`, `reset-style`, `set-all-style`, `reset-all-style`) обрабатывают различные действия пользователя, такие как отправка запросов, загрузка фреймов и т.д.


```