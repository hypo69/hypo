# `popup.js`

## Обзор

Этот файл `popup.js` является скриптом всплывающего окна расширения для браузера, предназначенного для тестирования и отладки XPath-выражений на веб-страницах. Он управляет пользовательским интерфейсом всплывающего окна, взаимодействует с контент-скриптами на страницах и обрабатывает ответы, отображая результаты и детали.

## Содержание

1.  [Обзор](#обзор)
2.  [Переменные](#переменные)
3.  [Функции](#функции)
    *   [`sendToActiveTab`](#sendToActiveTab)
    *   [`sendToSpecifiedFrame`](#sendToSpecifiedFrame)
    *   [`collectPopupState`](#collectPopupState)
    *   [`changeContextVisible`](#changeContextVisible)
    *   [`changeResolverVisible`](#changeResolverVisible)
    *   [`changeFrameIdVisible`](#changeFrameIdVisible)
    *   [`changeFrameDesignationVisible`](#changeFrameDesignationVisible)
    *   [`changeHelpVisible`](#changeHelpVisible)
    *   [`makeExecuteMessage`](#makeExecuteMessage)
    *   [`getSpecifiedFrameId`](#getSpecifiedFrameId)
    *   [`execContentScript`](#execContentScript)
    *   [`sendExecute`](#sendExecute)
    *   [`handleExprEnter`](#handleExprEnter)
    *   [`showDetailsPage`](#showDetailsPage)
    *   [`showError`](#showError)
    *   [`genericListener`](#genericListener)
    *   [`showResultsInPopup`](#showResultsInPopup)
    *   [`restorePopupState`](#restorePopupState)
    *  [`insertStyleToPopup`](#insertStyleToPopup)
    *  [`addFrameId`](#addFrameId)
4.  [События](#события)
    *   [`window.addEventListener("load")`](#windowaddEventListenerload)

## Переменные

-   `tx`: Псевдоним для `tryxpath`.
-   `fu`: Псевдоним для `tryxpath.functions`.
-   `document`: Ссылка на объект `document` текущего окна.
-   `noneClass`: Строка `"none"`, используемая для скрытия элементов.
-   `helpClass`: Строка `"help"`, используемая для определения элементов справки.
-   `invalidTabId`: Значение `browser.tabs.TAB_ID_NONE`, представляющее недействительный идентификатор вкладки.
-   `invalidExecutionId`: Значение `NaN`, представляющее недействительный идентификатор выполнения.
-   `invalidFrameId`: Значение `-1`, представляющее недействительный идентификатор фрейма.
-   `mainWay`, `mainExpression`, `contextCheckbox`, `contextHeader`, `contextBody`, `contextWay`, `contextExpression`, `resolverHeader`, `resolverBody`, `resolverCheckbox`, `resolverExpression`, `frameDesignationHeader`, `frameDesignationCheckbox`, `frameDesignationBody`, `frameDesignationExpression`, `frameIdHeader`, `frameIdCheckbox`, `frameIdBody`, `frameIdList`, `frameIdExpression`, `resultsMessage`, `resultsTbody`, `contextTbody`, `resultsCount`, `resultsFrameId`, `detailsPageCount`, `helpBody`, `helpCheckbox`: HTML-элементы, используемые для управления пользовательским интерфейсом всплывающего окна.
-   `relatedTabId`: Идентификатор вкладки, к которой относятся результаты.
-   `relatedFrameId`: Идентификатор фрейма, к которому относятся результаты.
-   `executionId`: Идентификатор текущего выполнения.
-   `resultedDetails`: Массив, содержащий детали результатов.
-   `detailsPageSize`: Размер страницы деталей результатов.
-   `detailsPageIndex`: Индекс текущей страницы деталей результатов.

## Функции

### `sendToActiveTab`

```javascript
function sendToActiveTab(msg, opts)
```

**Описание**:
Отправляет сообщение на активную вкладку.

**Параметры**:
- `msg` (Object): Сообщение для отправки.
- `opts` (Object, optional): Дополнительные параметры для отправки сообщения. По умолчанию `{}`.

**Возвращает**:
- `Promise<any>`: Промис, который разрешается, когда сообщение успешно отправлено.

### `sendToSpecifiedFrame`

```javascript
function sendToSpecifiedFrame(msg)
```

**Описание**:
Отправляет сообщение на указанный фрейм.

**Параметры**:
- `msg` (Object): Сообщение для отправки.

**Возвращает**:
- `Promise<void>`: Промис, который разрешается, когда сообщение успешно отправлено.

**Вызывает исключения**:
- `Error`: Если возникает ошибка при отправке сообщения или frameId неверный

### `collectPopupState`

```javascript
function collectPopupState()
```

**Описание**:
Собирает текущее состояние всплывающего окна.

**Возвращает**:
- `Object`: Объект, содержащий текущее состояние всплывающего окна.

### `changeContextVisible`

```javascript
function changeContextVisible()
```

**Описание**:
Переключает видимость раздела контекста.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `changeResolverVisible`

```javascript
function changeResolverVisible()
```

**Описание**:
Переключает видимость раздела резолвера.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `changeFrameIdVisible`

```javascript
function changeFrameIdVisible()
```

**Описание**:
Переключает видимость раздела идентификатора фрейма.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `changeFrameDesignationVisible`

```javascript
function changeFrameDesignationVisible()
```

**Описание**:
Переключает видимость раздела обозначения фрейма.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `changeHelpVisible`

```javascript
function changeHelpVisible()
```

**Описание**:
Переключает видимость элементов справки.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `makeExecuteMessage`

```javascript
function makeExecuteMessage()
```

**Описание**:
Создает сообщение для выполнения XPath.

**Возвращает**:
- `Object`: Объект, содержащий данные для выполнения XPath.

### `getSpecifiedFrameId`

```javascript
function getSpecifiedFrameId()
```

**Описание**:
Получает идентификатор указанного фрейма.

**Возвращает**:
- `number`: Идентификатор фрейма.

### `execContentScript`

```javascript
function execContentScript()
```

**Описание**:
Выполняет контент-скрипты на всех фреймах.

**Возвращает**:
- `Promise<void>`: Промис, который разрешается после выполнения контент-скриптов.

### `sendExecute`

```javascript
function sendExecute()
```

**Описание**:
Отправляет сообщение для выполнения XPath.

**Параметры**:
- Нет

**Возвращает**:
- `void`

### `handleExprEnter`

```javascript
function handleExprEnter (event)
```

**Описание**:
Обрабатывает нажатие клавиши Enter в текстовых полях.

**Параметры**:
- `event` (KeyboardEvent): Событие нажатия клавиши.

**Возвращает**:
- `void`

### `showDetailsPage`

```javascript
function showDetailsPage(index)
```

**Описание**:
Отображает страницу с деталями результатов.

**Параметры**:
- `index` (number): Индекс страницы для отображения.

**Возвращает**:
- `void`

### `showError`

```javascript
function showError(message, frameId)
```

**Описание**:
Отображает сообщение об ошибке.

**Параметры**:
- `message` (string): Сообщение об ошибке.
- `frameId` (number): Идентификатор фрейма, где произошла ошибка.

**Возвращает**:
- `void`

### `genericListener`

```javascript
function genericListener(message, sender, sendResponse)
```

**Описание**:
Общий обработчик входящих сообщений.

**Параметры**:
- `message` (Object): Входящее сообщение.
- `sender` (Object): Отправитель сообщения.
- `sendResponse` (function): Функция для отправки ответа.

**Возвращает**:
- `any`: Возвращает результат выполнения обработчика.
- `void`

### `showResultsInPopup`

```javascript
genericListener.listeners.showResultsInPopup = function (message, sender)
```

**Описание**:
Обрабатывает сообщение для отображения результатов во всплывающем окне.

**Параметры**:
- `message` (Object): Сообщение с результатами.
- `sender` (Object): Отправитель сообщения.

**Возвращает**:
- `void`

### `restorePopupState`

```javascript
genericListener.listeners.restorePopupState = function (message)
```

**Описание**:
Восстанавливает состояние всплывающего окна из сохраненных данных.

**Параметры**:
- `message` (Object): Сообщение с состоянием.

**Возвращает**:
- `void`

### `insertStyleToPopup`

```javascript
genericListener.listeners.insertStyleToPopup = function(message)
```
**Описание**:
Вставляет стили в popup окно.

**Параметры**:
- `message` (Object): Сообщение содержащее стили.
**Возвращает**:
- `void`

### `addFrameId`

```javascript
genericListener.listeners.addFrameId = function (message, sender)
```
**Описание**:
Добавляет ID фрейма в выпадающий список.

**Параметры**:
- `message` (Object): Сообщение.
- `sender` (Object): Отправитель сообщения.
**Возвращает**:
- `void`

## События

### `window.addEventListener("load")`

```javascript
window.addEventListener("load", () => { ... });
```

**Описание**:
Обработчик события `load` окна.
Инициализирует элементы пользовательского интерфейса, добавляет слушатели событий и отправляет сообщения для восстановления состояния и стилей.

**Параметры**:
- Нет.

**Возвращает**:
- `void`