# Документация для файла popup.js

## Обзор

Файл `popup.js` отвечает за реализацию пользовательского интерфейса и взаимодействие с расширением TryXPath.  Он обрабатывает пользовательские запросы, отображает результаты, и сохраняет состояние поп-ап окна.

## Переменные

```javascript
const noneClass = "none";
const helpClass = "help";
const invalidTabId = browser.tabs.TAB_ID_NONE;
const invalidExecutionId = NaN;
const invalidFrameId = -1;
```

Переменные `noneClass`, `helpClass`, `invalidTabId`, `invalidExecutionId` и `invalidFrameId` хранят константы для удобства использования в коде и определяют специальные значения для недействительных значений.

```javascript
var mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
    contextWay, contextExpression, resolverHeader, resolverBody,
    resolverCheckbox, resolverExpression, frameDesignationHeader,
    frameDesignationCheckbox, frameDesignationBody,
    frameDesignationExpression, frameIdHeader, frameIdCheckbox,
    frameIdBody, frameIdList, frameIdExpression, resultsMessage,
    resultsTbody, contextTbody, resultsCount, resultsFrameId,
    detailsPageCount, helpBody, helpCheckbox;
```

Переменные `mainWay`, `mainExpression`, `contextCheckbox`, и другие – это ссылки на DOM-элементы страницы, используемые для взаимодействия с пользователем.

```javascript
var relatedTabId = invalidTabId;
var relatedFrameId = invalidFrameId;
var executionId = invalidExecutionId;
var resultedDetails = [];
const detailsPageSize = 50;
var detailsPageIndex = 0;
```

Переменные `relatedTabId`, `relatedFrameId`, `executionId`, `resultedDetails`, `detailsPageSize`, `detailsPageIndex` хранят состояние взаимодействия с активной вкладкой, результатами запроса и страницей детализации.

## Функции

### `sendToActiveTab`

**Описание**: Отправляет сообщение в активную вкладку.

**Параметры**:
- `msg` (Object): Сообщение для отправки.
- `opts` (Object, optional): Дополнительные опции для отправки сообщения. По умолчанию `{}`.

**Возвращает**:
- `Promise`: Обещание, которое выполняется, если сообщение успешно отправлено.

**Вызывает исключения**:
- Нет.

### `sendToSpecifiedFrame`

**Описание**: Отправляет сообщение в указанный iframe.

**Параметры**:
- `msg` (Object): Сообщение для отправки.

**Возвращает**:
- `Promise`: Обещание, которое выполняется, если сообщение успешно отправлено.

**Вызывает исключения**:
- `e`: Возникает при ошибке в работе с фреймом.

### `collectPopupState`

**Описание**: Собирает текущее состояние поп-ап окна.

**Параметры**:
- Нет.

**Возвращает**:
- `Object`: Словарь, содержащий состояние поп-ап окна.

**Вызывает исключения**:
- Нет.

### `changeContextVisible`

**Описание**: Изменяет видимость блока контекста.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

(Аналогичные описания для других функций `changeResolverVisible`, `changeFrameIdVisible`, `changeFrameDesignationVisible`, `changeHelpVisible`, `makeExecuteMessage`, `getSpecifiedFrameId`, `execContentScript`, `sendExecute`, `handleExprEnter`, `showDetailsPage`, `showError`, `genericListener`, и др.)

## Обработка событий

(Описание обработчиков событий `click`, `keypress`, `unload`, и других на элементах DOM, с указанием вызываемых функций)

## Взаимодействие с расширением

(Описание взаимодействия с другими частями расширения через `browser.runtime.onMessage` и `browser.tabs`)

## Замечания

Файл `popup.js` использует асинхронные операции (promises) для обработки событий и коммуникации с другими компонентами расширения.  Для успешной работы расширения необходимо, чтобы все скрипты (`try_xpath_check_frame.js`, `try_xpath_functions.js`, `try_xpath_content.js`) были правильно импортированы и взаимодействовали между собой.


```