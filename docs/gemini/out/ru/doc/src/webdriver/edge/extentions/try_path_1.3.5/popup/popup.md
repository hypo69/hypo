# Модуль popup.js

## Обзор

Этот JavaScript-модуль отвечает за создание и обработку пользовательского интерфейса всплывающего окна расширения `try_path`. Он предоставляет инструменты для настройки запросов XPath, выбора целевого фрейма, выполнения запросов и отображения результатов. Модуль использует API расширений браузера для коммуникации с активной вкладкой.


## Переменные

### `noneClass`

**Описание**: Константа, содержащая значение класса `none`, используемого для скрытия элементов.

### `helpClass`

**Описание**: Константа, содержащая значение класса `help`, используемого для элементов справки.

### `invalidTabId`, `invalidExecutionId`, `invalidFrameId`

**Описание**: Константы, представляющие недопустимые значения для идентификаторов вкладок, ID выполнения и ID фрейма соответственно.

### `mainWay`, `mainExpression`, `contextCheckbox`, `contextHeader`, ...

**Описание**: Переменные, хранящие ссылки на HTML-элементы, соответствующие элементам управления интерфейса (пути, выражения, флажки и т.д.).


## Функции

### `sendToActiveTab`

**Описание**: Отправляет сообщение активной вкладке.

**Параметры**:
- `msg` (объект): Объект, содержащий сообщение для отправки.
- `opts` (опциональный объект): Опции для отправки сообщения (например, `frameId`).

**Возвращает**:
- `Promise`: Обещание, которое разрешается после отправки сообщения.

**Вызывает исключения**:
- `Ошибка`: Возникает в случае возникновения ошибки при отправке сообщения вкладке.


### `sendToSpecifiedFrame`

**Описание**: Отправляет сообщение в указанный фрейм.

**Параметры**:
- `msg` (объект): Объект, содержащий сообщение для отправки.


**Возвращает**:
- `Promise`: Обещание, которое разрешается после отправки сообщения в указанный фрейм.

**Вызывает исключения**:
- `Ошибка`: Возникает в случае ошибки при взаимодействии с фреймом.


### `collectPopupState`

**Описание**: Собрать состояние всплывающего окна.

**Возвращает**:
- `объект`: Объект, содержащий собранное состояние.


### `changeContextVisible`

**Описание**: Изменяет видимость блока `context`.

**Параметры**:
- `нет параметров`.

**Возвращает**:
- `нет значения`


### `changeResolverVisible`, `changeFrameIdVisible`, `changeFrameDesignationVisible`, `changeHelpVisible`

**Описание**: Аналогичные функции для управления видимостью других блоков интерфейса.


### `makeExecuteMessage`

**Описание**: Формирует сообщение для отправки в контент-скрипт для выполнения XPath-запросов.

**Возвращает**:
- `объект`: Объект, содержащий данные запроса XPath.


### `getSpecifiedFrameId`

**Описание**: Возвращает ID указанного фрейма.

**Возвращает**:
- `число`: ID фрейма.

**Вызывает исключения**:
- `Ошибка`: Возникает, если указанное значение `frameId` некорректно.


### `execContentScript`

**Описание**: Выполняет скрипты в контенте страницы.

**Возвращает**:
- `Promise`: Обещание, которое разрешается после выполнения скриптов.

**Вызывает исключения**:
- `Ошибка`: Возникает в случае ошибки при выполнении скриптов.


### `sendExecute`

**Описание**: Отправляет запрос на выполнение XPath-запросов в контент-скрипт.


### `handleExprEnter`

**Описание**: Обрабатывает событие нажатия Enter в поле ввода выражения XPath.

**Параметры**:
- `event` (объект): Объект события.


### `showDetailsPage`

**Описание**: Отображает детали результатов запроса XPath.

**Параметры**:
- `index` (число): Индекс страницы результатов.


**Возвращает**:
- `нет значения`.

**Вызывает исключения**:
- `Ошибка`: Возникает в случае ошибки при обновлении таблицы.


### `showError`

**Описание**: Отображает сообщение об ошибке.

**Параметры**:
- `message` (строка): Сообщение об ошибке.
- `frameId` (строка): ID фрейма, связанный с ошибкой.


**Возвращает**:
- `нет значения`


### `genericListener`

**Описание**: Общий обработчик сообщений от контент-скрипта.

**Параметры**:
- `message`, `sender`, `sendResponse` (объекты): Данные сообщения, отправителя и функции ответа.

**Возвращает**:
- `boolean`: `true`, если обработка прошла успешно, иначе `false`.

**Вызывает исключения**:
- `Ошибка`: Возникает в случае возникновения ошибки при обработке сообщения.


## События

### `browser.runtime.onMessage`

**Описание**: Обрабатывает сообщения, отправленные в расширение.


##  Дополнительные пояснения

Функции, использующие `browser.tabs.sendMessage`, `browser.runtime.sendMessage`, и `browser.tabs.executeScript`, взаимодействуют с API браузера, что требует согласованности между сообщением и ожидаемыми результатами.


```