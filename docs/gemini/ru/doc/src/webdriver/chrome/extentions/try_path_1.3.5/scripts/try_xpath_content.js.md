# try_xpath_content.js

## Обзор

Данный скрипт является основным контентным скриптом для расширения Try xpath. Он обрабатывает сообщения от фонового скрипта, выполняет XPath-запросы, подсвечивает элементы на странице и управляет стилями.

## Оглавление
1. [Переменные](#Переменные)
2. [Функции](#Функции)
    - [setAttr](#setAttr)
    - [setIndex](#setIndex)
    - [isFocusable](#isFocusable)
    - [focusItem](#focusItem)
    - [setMainAttrs](#setMainAttrs)
    - [restoreAttrs](#restoreAttrs)
    - [resetPrev](#resetPrev)
    - [makeTypeStr](#makeTypeStr)
    - [updateCss](#updateCss)
    - [getFrames](#getFrames)
    - [parseFrameDesignation](#parseFrameDesignation)
    - [traceBlankWindows](#traceBlankWindows)
    - [handleCssChange](#handleCssChange)
    - [findFrameByMessage](#findFrameByMessage)
    - [setFocusFrameListener](#setFocusFrameListener)
    - [initBlankWindow](#initBlankWindow)
    - [findStyleParent](#findStyleParent)
    - [updateStyleElement](#updateStyleElement)
    - [updateAllStyleElements](#updateAllStyleElements)
    - [removeStyleElement](#removeStyleElement)
    - [removeAllStyleElements](#removeAllStyleElements)
    - [createResultMessage](#createResultMessage)
    - [genericListener](#genericListener)
3. [Слушатели сообщений](#Слушатели-сообщений)
    - [setContentInfo](#setContentInfo)
    - [execute](#execute)
    - [focusItem](#focusItem)
    - [focusContextItem](#focusContextItem)
    - [focusFrame](#focusFrame)
    - [requestShowResultsInPopup](#requestShowResultsInPopup)
    - [requestShowAllResults](#requestShowAllResults)
    - [resetStyle](#resetStyle)
    - [setStyle](#setStyle)
    - [finishInsertCss](#finishInsertCss)
    - [finishRemoveCss](#finishRemoveCss)
4. [Слушатели событий](#Слушатели-событий)
    - [browser.storage.onChanged](#browserstorageonChanged)
    - [window.addEventListener("message")](#windowaddEventListenermessage)
5. [Инициализация](#Инициализация)

## Переменные

### `tx`
- **Описание**: Псевдоним для `tryxpath`.
- **Тип**: `Object`

### `fu`
- **Описание**: Псевдоним для `tryxpath.functions`.
- **Тип**: `Object`

### `isContentLoaded`
- **Описание**: Флаг, предотвращающий множественный запуск скрипта.
- **Тип**: `Boolean`

### `dummyItem`
- **Описание**: Пустая строка, используемая в качестве значения по умолчанию.
- **Тип**: `String`

### `dummyItems`
- **Описание**: Пустой массив, используемый в качестве значения по умолчанию.
- **Тип**: `Array`

### `invalidExecutionId`
- **Описание**: Значение, представляющее неверный ID выполнения.
- **Тип**: `Number`

### `styleElementHeader`
- **Описание**: Заголовок для стилей, добавленных расширением.
- **Тип**: `String`

### `attributes`
- **Описание**: Объект, содержащий имена атрибутов для выделения элементов.
- **Тип**: `Object`

### `prevMsg`
- **Описание**: Предыдущее сообщение для показа результатов.
- **Тип**: `Object`

### `executionCount`
- **Описание**: Счетчик выполненных запросов.
- **Тип**: `Number`

### `inBlankWindow`
- **Описание**: Флаг, указывающий, выполняется ли код в пустом окне.
- **Тип**: `Boolean`

### `currentDocument`
- **Описание**: Текущий документ, с которым работает скрипт.
- **Тип**: `Document`

### `contextItem`
- **Описание**: Текущий контекстный элемент.
- **Тип**: `HTMLElement | Document`

### `currentItems`
- **Описание**: Массив текущих элементов, найденных XPath-запросом.
- **Тип**: `Array<HTMLElement>`

### `focusedItem`
- **Описание**: Текущий элемент, находящийся в фокусе.
- **Тип**: `HTMLElement`

### `focusedAncestorItems`
- **Описание**: Массив родительских элементов текущего элемента в фокусе.
- **Тип**: `Array<HTMLElement>`

### `currentCss`
- **Описание**: Текущий CSS, используемый для выделения элементов.
- **Тип**: `String`

### `insertedStyleElements`
- **Описание**: Карта, хранящая добавленные элементы style.
- **Тип**: `Map<Document, HTMLStyleElement>`

### `expiredCssSet`
- **Описание**: Набор устаревших CSS.
- **Тип**: `Object`

### `originalAttributes`
- **Описание**: Карта, хранящая оригинальные атрибуты элементов.
- **Тип**: `Map<HTMLElement, Object>`

## Функции

### `setAttr`

**Описание**: Устанавливает атрибут для элемента, сохраняя предыдущее значение.

**Параметры**:
- `attr` (string): Название атрибута.
- `value` (string): Значение атрибута.
- `item` (HTMLElement): Элемент, для которого устанавливается атрибут.

**Возвращает**:
- `void`

### `setIndex`

**Описание**: Устанавливает индексный атрибут для набора элементов, сохраняя предыдущие значения.

**Параметры**:
- `attr` (string): Название атрибута.
- `items` (Array<HTMLElement>): Массив элементов.

**Возвращает**:
- `void`

### `isFocusable`

**Описание**: Проверяет, может ли элемент получить фокус.

**Параметры**:
- `item` (HTMLElement): Элемент для проверки.

**Возвращает**:
- `boolean`: `true`, если элемент может получить фокус, `false` в противном случае.

### `focusItem`

**Описание**: Устанавливает фокус на элемент, выделяя его и его предков.

**Параметры**:
- `item` (HTMLElement): Элемент, на который нужно установить фокус.

**Возвращает**:
- `void`

### `setMainAttrs`

**Описание**: Устанавливает главные атрибуты для контекстного элемента и текущих элементов.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `restoreAttrs`

**Описание**: Восстанавливает оригинальные атрибуты элементов.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `resetPrev`

**Описание**: Сбрасывает состояние для нового выполнения запроса.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `makeTypeStr`

**Описание**: Преобразует числовой тип результата XPath в строковое представление.

**Параметры**:
- `resultType` (number): Числовой тип результата XPath.

**Возвращает**:
- `string`: Строковое представление типа результата.

### `updateCss`

**Описание**: Запрашивает обновление CSS у фонового скрипта, если CSS изменился или есть устаревшие стили.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `getFrames`

**Описание**: Получает массив фреймов на основе спецификации.

**Параметры**:
- `spec` (string): JSON-строка, представляющая массив индексов фреймов.

**Возвращает**:
- `Array<HTMLIFrameElement>`: Массив фреймов.

**Вызывает исключения**:
- `Error`: Если спецификация фрейма неверна.

### `parseFrameDesignation`

**Описание**: Парсит спецификацию фрейма.

**Параметры**:
- `frameDesi` (string): JSON-строка, представляющая массив индексов фреймов.

**Возвращает**:
- `Array<number>`: Массив индексов фреймов.

**Вызывает исключения**:
- `Error`: Если спецификация фрейма неверна.

### `traceBlankWindows`

**Описание**: Проверяет наличие пустых фреймов.

**Параметры**:
- `desi` (Array<number>): Массив индексов фреймов.
- `win` (Window): Начальное окно.

**Возвращает**:
- `Object`: Объект с информацией об успехе, неудавшемся окне и массивом окон.

### `handleCssChange`

**Описание**: Обрабатывает изменения CSS, полученные из хранилища.

**Параметры**:
- `newCss` (string): Новый CSS.

**Возвращает**:
- `void`

### `findFrameByMessage`

**Описание**: Находит элемент фрейма на основе сообщения.

**Параметры**:
- `event` (MessageEvent): Событие сообщения.
- `win` (Window): Окно, в котором ищем фрейм.

**Возвращает**:
- `HTMLIFrameElement`: Найденный элемент фрейма.

### `setFocusFrameListener`

**Описание**: Устанавливает слушатель сообщений для фреймов, для переключения фокуса.

**Параметры**:
- `win` (Window): Окно, для которого устанавливается слушатель.
- `isBlankWindow` (boolean): Флаг, указывающий, является ли окно пустым.

**Возвращает**:
- `void`

### `initBlankWindow`

**Описание**: Инициализирует пустые окна.

**Параметры**:
- `win` (Window): Окно для инициализации.

**Возвращает**:
- `void`

### `findStyleParent`

**Описание**: Находит родительский элемент для вставки элемента style.

**Параметры**:
- `doc` (Document): Документ, в котором ищем родительский элемент.

**Возвращает**:
- `HTMLElement`: Родительский элемент.

### `updateStyleElement`

**Описание**: Обновляет или вставляет элемент style.

**Параметры**:
- `doc` (Document): Документ, в котором нужно обновить или вставить элемент style.

**Возвращает**:
- `void`

### `updateAllStyleElements`

**Описание**: Обновляет все элементы style.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `removeStyleElement`

**Описание**: Удаляет элемент style из документа.

**Параметры**:
- `doc` (Document): Документ, из которого нужно удалить элемент style.

**Возвращает**:
- `void`

### `removeAllStyleElements`

**Описание**: Удаляет все элементы style.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `createResultMessage`

**Описание**: Создает объект сообщения с результатами по умолчанию.

**Параметры**:
- `void`

**Возвращает**:
- `Object`: Объект сообщения с результатами по умолчанию.

### `genericListener`

**Описание**: Слушатель общих сообщений.

**Параметры**:
- `message` (Object): Сообщение.
- `sender` (Object): Отправитель сообщения.
- `sendResponse` (Function): Функция для отправки ответа.

**Возвращает**:
- `Function`: Функция-слушатель.

## Слушатели сообщений

### `setContentInfo`

**Описание**: Устанавливает атрибуты из сообщения.

**Параметры**:
- `message` (Object): Сообщение с атрибутами.

**Возвращает**:
- `void`

### `execute`

**Описание**: Выполняет XPath-запрос и отправляет результаты.

**Параметры**:
- `message` (Object): Сообщение с параметрами запроса.
- `sender` (Object): Отправитель сообщения.

**Возвращает**:
- `void`

### `focusItem`

**Описание**: Фокусирует элемент.

**Параметры**:
- `message` (Object): Сообщение с ID выполнения и индексом элемента.

**Возвращает**:
- `void`

### `focusContextItem`

**Описание**: Фокусирует контекстный элемент.

**Параметры**:
- `message` (Object): Сообщение с ID выполнения.

**Возвращает**:
- `void`

### `focusFrame`

**Описание**: Фокусирует фрейм.

**Параметры**:
- `message` (Object): Сообщение с описанием фрейма.

**Возвращает**:
- `void`

### `requestShowResultsInPopup`

**Описание**: Запрашивает показ результатов во всплывающем окне.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `requestShowAllResults`

**Описание**: Запрашивает показ всех результатов.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `resetStyle`

**Описание**: Сбрасывает стили.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `setStyle`

**Описание**: Устанавливает стили.

**Параметры**:
- `void`

**Возвращает**:
- `void`

### `finishInsertCss`

**Описание**: Завершает вставку CSS.

**Параметры**:
- `message` (Object): Сообщение с CSS.

**Возвращает**:
- `void`

### `finishRemoveCss`

**Описание**: Завершает удаление CSS.

**Параметры**:
- `message` (Object): Сообщение с CSS.

**Возвращает**:
- `void`

## Слушатели событий

### `browser.storage.onChanged`

**Описание**: Слушатель изменений в хранилище браузера для атрибутов и CSS.

**Параметры**:
- `changes` (Object): Объект с изменениями в хранилище.

**Возвращает**:
- `void`

### `window.addEventListener("message")`

**Описание**: Слушатель сообщений от других скриптов.

**Параметры**:
- `event` (MessageEvent): Событие сообщения.

**Возвращает**:
- `void`

## Инициализация

- Устанавливается слушатель сообщений для текущего окна.
- Отправляется запрос на получение информации о контенте.
- Устанавливается слушатель для сообщений от фреймов.

Этот скрипт является ядром функциональности расширения, обрабатывая запросы от фонового скрипта и взаимодействуя со страницей для поиска и выделения элементов на основе XPath-запросов.