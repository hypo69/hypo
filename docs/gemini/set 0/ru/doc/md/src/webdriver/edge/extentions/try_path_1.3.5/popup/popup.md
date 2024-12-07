# Модуль popup.js

## Обзор

Этот файл JavaScript содержит код для всплывающего окна расширения. Он обрабатывает пользовательский ввод, отправляет запросы в активную вкладку, отображает результаты, и управляет состоянием всплывающего окна.


## Переменные

### `noneClass`

**Описание:** Константа, представляющая имя класса, который скрывает элемент. Значение: `"none"`.

### `helpClass`

**Описание:** Константа, представляющая имя класса, который содержит вспомогательную информацию. Значение: `"help"`.

### `invalidTabId`, `invalidExecutionId`, `invalidFrameId`

**Описание:** Константы, представляющие недействительные значения для идентификаторов вкладок, ID выполнения и ID фреймов.

## Функции

### `sendToActiveTab`

**Описание:** Отправляет сообщение активной вкладке.

**Параметры:**

- `msg` (объект): Сообщение для отправки.
- `opts` (объект, опционально): Дополнительные параметры для сообщения. По умолчанию `{}`.

**Возвращает:**

- `Promise`: Обещание, которое разрешается после отправки сообщения.

### `sendToSpecifiedFrame`

**Описание:** Отправляет сообщение указанному фрейму.

**Параметры:**

- `msg` (объект): Сообщение для отправки.

**Возвращает:**

- `Promise`: Обещание, которое разрешается после отправки сообщения.

**Обрабатывает исключения:**

- `e`: Ошибки при взаимодействии с фреймом. Выводит ошибку пользователю и отображает сообщение об ошибке.

### `collectPopupState`

**Описание:** Собрать текущее состояние всплывающего окна.

**Возвращает:**

- `объект`: Объект, содержащий состояние всплывающего окна.

### `changeContextVisible`, `changeResolverVisible`, `changeFrameIdVisible`, `changeFrameDesignationVisible`

**Описание:** Функции для изменения видимости элементов связанных с контекстом, разрешением, идентификатором фрейма и описанием фрейма соответственно.


### `changeHelpVisible`

**Описание:** Функция для изменения видимости элементов с классом `helpClass`.


### `makeExecuteMessage`

**Описание:** Создает сообщение для выполнения запроса.

**Возвращает:**

- `объект`: Объект, содержащий данные для выполнения запроса.


### `getSpecifiedFrameId`

**Описание:** Возвращает ID указанного фрейма.

**Возвращает:**

- `число`: ID фрейма или 0, если не указано.

### `execContentScript`

**Описание:** Выполняет скрипты в текущей вкладке.


**Возвращает:**

- `Promise`: Обещание, которое разрешается после выполнения скриптов.

### `sendExecute`

**Описание:** Отправляет запрос на выполнение XPath в активной вкладке.

### `handleExprEnter`

**Описание:** Обрабатывает нажатие клавиши Enter для отправки запроса.

**Параметры:**

- `event` (событие): Событие нажатия клавиши.

**Обрабатывает исключения:**

- `Предотвращает` стандартное поведение нажатия Enter.

### `showDetailsPage`

**Описание:** Отображает страницу с результатами.

**Параметры:**

- `index` (число): Номер страницы с результатами.

**Обрабатывает исключения:**

- `Предотвращает` неверные индексы.

### `showError`

**Описание:** Отображает сообщение об ошибке в всплывающем окне.

**Параметры:**

- `message` (строка): Текст сообщения об ошибке.
- `frameId` (число): ID фрейма, в котором произошла ошибка (опционально).


### `genericListener`

**Описание:** Общий обработчик сообщений для расширения.

**Параметры:**

- `message`, `sender`, `sendResponse` (объекты): Данные сообщения и отправителя.

**Обрабатывает исключения:**

- Обрабатывает ненайденные обработчики сообщений.


## Обработчики событий


### `showResultsInPopup`, `restorePopupState`, `insertStyleToPopup`, `addFrameId`

**Описание:** Обработчики сообщений для различных событий.