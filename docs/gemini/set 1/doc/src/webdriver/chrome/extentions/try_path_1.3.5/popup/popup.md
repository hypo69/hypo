# Документация модуля popup.js

## Обзор

Этот JavaScript-модуль отвечает за работу всплывающего окна расширения. Он обрабатывает пользовательский ввод, отправляет запросы в активную вкладку браузера, и отображает результаты выполнения XPath-запросов. Модуль использует API браузера для взаимодействия с активной вкладкой и её фреймами. Он также отвечает за сохранение и восстановление состояния всплывающего окна.

## Переменные

### `noneClass`

Строковая константа, используемая для класса, скрывающего элементы.

### `helpClass`

Строковая константа, используемая для класса, содержащего элементы справки.

### `invalidTabId`, `invalidExecutionId`, `invalidFrameId`

Константы, представляющие недействительные значения идентификаторов вкладок, выполнения и фреймов.

### `mainWay`, `mainExpression`, ...

Переменные, хранящие ссылки на HTML-элементы, представляющие входные поля для XPath-запросов.

### `relatedTabId`, `relatedFrameId`, `executionId`, `resultedDetails`, `detailsPageSize`, `detailsPageIndex`

Переменные, хранящие данные о текущем запросе, результатах и страницировании.

## Функции

### `sendToActiveTab(msg, opts)`

**Описание**: Отправляет сообщение в активную вкладку.

**Параметры**:
- `msg` (объект): Сообщение, которое необходимо отправить.
- `opts` (объект, необязательно): Дополнительные параметры. По умолчанию пусто.

**Возвращает**:
- `Promise`: Обещание, которое выполняется после отправки сообщения.

**Вызывает исключения**:
- `Error`: Любые исключения, которые могут возникнуть при использовании API браузера.

### `sendToSpecifiedFrame(msg)`

**Описание**: Отправляет сообщение в указанный фрейм активной вкладки.

**Параметры**:
- `msg` (объект): Сообщение, которое необходимо отправить.

**Возвращает**:
- `Promise`: Обещание, которое выполняется после отправки сообщения в указанный фрейм.

**Вызывает исключения**:
- `Error`: Возникает при ошибке взаимодействия с фреймом.

### `collectPopupState()`

**Описание**: Сбор текущего состояния всплывающего окна.

**Возвращает**:
- `объект`: Объект, содержащий текущее состояние.

### `changeContextVisible()`, `changeResolverVisible()`, `changeFrameIdVisible()`, `changeFrameDesignationVisible()`, `changeHelpVisible()`

**Описание**: Изменяют видимость блоков контекста, решателя, фреймов и справки в зависимости от состояния чекбоксов.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

### `makeExecuteMessage()`

**Описание**: Собирает и формирует сообщение для отправки в активную вкладку для выполнения запроса.

**Возвращает**:
- `объект`: Объект с параметрами запроса.

### `getSpecifiedFrameId()`

**Описание**: Возвращает идентификатор указанного фрейма.

**Возвращает**:
- `целое число`: Идентификатор фрейма.

### `execContentScript()`

**Описание**: Выполняет скрипты в активной вкладке.

**Возвращает**:
- `Promise`: Обещание, которое выполняется после выполнения скриптов.

**Вызывает исключения**:
- `Error`: Возникает при ошибке выполнения скриптов.


### `sendExecute()`, `handleExprEnter()`, `showDetailsPage()`, `showError()`, `genericListener()`

**Описание**:  Функции для обработки отправки запроса, обработки нажатия Enter, отображения результатов, обработки ошибок, и обработки сообщений от контентного скрипта.

**Параметры**:  Зависит от функции.

**Возвращает**:  Зависит от функции.

**Вызывает исключения**: Зависит от функции.


## Обработчики событий

Подробные описания обработчиков событий для каждого элемента интерфейса.

##  Заключение

Модуль `popup.js` обеспечивает взаимодействие пользователя с расширением и отображение результатов XPath-запросов, предоставляя пользователю удобный интерфейс.  Поддерживается сложная логика для обработки ошибок и запросов к активной вкладке и фреймам.