# popup.js

## Обзор

Данный файл `popup.js` является скриптом для расширения браузера, который предоставляет пользовательский интерфейс для выполнения XPath-запросов на веб-страницах. Он позволяет пользователю задавать XPath-выражения, контексты и параметры для их выполнения, а также отображает результаты в виде таблицы.

## Оглавление

- [Константы](#константы)
- [Переменные](#переменные)
- [Функции](#функции)
  - [`sendToActiveTab`](#sendtoactivetab)
  - [`sendToSpecifiedFrame`](#sendtospecifiedframe)
  - [`collectPopupState`](#collectpopupstate)
  - [`changeContextVisible`](#changecontextvisible)
  - [`changeResolverVisible`](#changeresolvervisible)
  - [`changeFrameIdVisible`](#changeframeidvisible)
  - [`changeFrameDesignationVisible`](#changeframedesignationvisible)
  - [`changeHelpVisible`](#changehelpvisible)
  - [`makeExecuteMessage`](#makeexecutemessage)
  - [`getSpecifiedFrameId`](#getspecifiedframeid)
  - [`execContentScript`](#execcontentscript)
  - [`sendExecute`](#sendexecute)
  - [`handleExprEnter`](#handleexprenter)
  - [`showDetailsPage`](#showdetailspage)
  - [`showError`](#showerror)
  - [`genericListener`](#genericlistener)
- [События](#события)

## Константы

- `noneClass`: Строка "none", используется для скрытия элементов.
- `helpClass`: Строка "help", используется для элементов справки.
- `invalidTabId`: Значение `browser.tabs.TAB_ID_NONE`, представляющее недопустимый ID вкладки.
- `invalidExecutionId`: Значение `NaN`, представляющее недопустимый ID выполнения.
- `invalidFrameId`: Значение `-1`, представляющее недопустимый ID фрейма.
- `detailsPageSize`: Размер страницы для отображения деталей результатов.

## Переменные

- `tx`: Псевдоним для объекта `tryxpath`.
- `fu`: Псевдоним для объекта `tryxpath.functions`.
- `document`: Ссылка на объект `document` текущего окна.
- `mainWay`, `mainExpression`, `contextCheckbox`, `contextHeader`, `contextBody`, `contextWay`, `contextExpression`, `resolverHeader`, `resolverBody`, `resolverCheckbox`, `resolverExpression`, `frameDesignationHeader`, `frameDesignationCheckbox`, `frameDesignationBody`, `frameDesignationExpression`, `frameIdHeader`, `frameIdCheckbox`, `frameIdBody`, `frameIdList`, `frameIdExpression`, `resultsMessage`, `resultsTbody`, `contextTbody`, `resultsCount`, `resultsFrameId`, `detailsPageCount`, `helpBody`, `helpCheckbox`: Переменные для хранения ссылок на элементы DOM.
- `relatedTabId`: ID связанной вкладки, по умолчанию `invalidTabId`.
- `relatedFrameId`: ID связанного фрейма, по умолчанию `invalidFrameId`.
- `executionId`: ID выполнения, по умолчанию `invalidExecutionId`.
- `resultedDetails`: Массив деталей результатов.
- `detailsPageIndex`: Индекс текущей страницы деталей.

## Функции

### `sendToActiveTab`

```javascript
function sendToActiveTab(msg, opts)
```

**Описание**:
Отправляет сообщение активной вкладке.

**Параметры**:
- `msg` (Object): Сообщение для отправки.
- `opts` (Object, optional): Дополнительные опции для отправки сообщения. По умолчанию `{}`.

**Возвращает**:
- `Promise`: Промис, который разрешается после отправки сообщения.

**Вызывает исключения**:
- Нет.

### `sendToSpecifiedFrame`

```javascript
function sendToSpecifiedFrame(msg)
```

**Описание**:
Отправляет сообщение в указанный фрейм.

**Параметры**:
- `msg` (Object): Сообщение для отправки.

**Возвращает**:
- `Promise`: Промис, который разрешается после отправки сообщения.

**Вызывает исключения**:
- Нет.

### `collectPopupState`

```javascript
function collectPopupState()
```

**Описание**:
Собирает состояние элементов popup.

**Параметры**:
- Нет.

**Возвращает**:
- `Object`: Объект, содержащий состояние элементов popup.

**Вызывает исключения**:
- Нет.

### `changeContextVisible`

```javascript
function changeContextVisible()
```

**Описание**:
Изменяет видимость контекстной области.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `changeResolverVisible`

```javascript
function changeResolverVisible()
```

**Описание**:
Изменяет видимость области резолвера.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `changeFrameIdVisible`

```javascript
function changeFrameIdVisible()
```

**Описание**:
Изменяет видимость области ввода ID фрейма.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `changeFrameDesignationVisible`

```javascript
function changeFrameDesignationVisible()
```

**Описание**:
Изменяет видимость области определения фрейма.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `changeHelpVisible`

```javascript
function changeHelpVisible()
```

**Описание**:
Изменяет видимость элементов справки.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `makeExecuteMessage`

```javascript
function makeExecuteMessage()
```

**Описание**:
Создает сообщение для выполнения XPath запроса.

**Параметры**:
- Нет.

**Возвращает**:
- `Object`: Объект сообщения для выполнения XPath.

**Вызывает исключения**:
- Нет.

### `getSpecifiedFrameId`

```javascript
function getSpecifiedFrameId()
```

**Описание**:
Получает ID указанного фрейма.

**Параметры**:
- Нет.

**Возвращает**:
- `number`: ID фрейма или 0, если не указан.

**Вызывает исключения**:
- Нет.

### `execContentScript`

```javascript
function execContentScript()
```

**Описание**:
Выполняет контент скрипты на странице.

**Параметры**:
- Нет.

**Возвращает**:
- `Promise`: Промис, который разрешается после выполнения скриптов.

**Вызывает исключения**:
- Нет.

### `sendExecute`

```javascript
function sendExecute()
```

**Описание**:
Отправляет сообщение для выполнения XPath запроса.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `handleExprEnter`

```javascript
function handleExprEnter(event)
```

**Описание**:
Обрабатывает нажатие клавиши Enter для отправки запроса.

**Параметры**:
- `event` (Event): Событие нажатия клавиши.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `showDetailsPage`

```javascript
function showDetailsPage(index)
```

**Описание**:
Показывает страницу с деталями результатов.

**Параметры**:
- `index` (number): Индекс страницы.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `showError`

```javascript
function showError(message, frameId)
```

**Описание**:
Показывает сообщение об ошибке.

**Параметры**:
- `message` (string): Сообщение об ошибке.
- `frameId` (number): ID фрейма, где произошла ошибка.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

### `genericListener`

```javascript
function genericListener(message, sender, sendResponse)
```

**Описание**:
Общий обработчик сообщений.

**Параметры**:
- `message` (Object): Сообщение.
- `sender` (Object): Отправитель сообщения.
- `sendResponse` (Function): Функция для отправки ответа.

**Возвращает**:
- `any`: Результат обработки сообщения.

**Вызывает исключения**:
- Нет.

## События

- `window.addEventListener("load", ...)`: Выполняется при загрузке окна. Инициализирует элементы DOM, устанавливает обработчики событий и отправляет начальные сообщения.
- `resultsTbody.addEventListener("click", ...)`: Обрабатывает клики по строкам результатов, вызывая фокус на элементе.
- `window.addEventListener("unload", ...)`: Выполняется при выгрузке окна. Сохраняет состояние popup.