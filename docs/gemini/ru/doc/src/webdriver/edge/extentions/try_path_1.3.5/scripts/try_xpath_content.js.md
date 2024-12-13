# Документация для `try_xpath_content.js`

## Обзор

Данный файл содержит скрипт, который обрабатывает запросы от расширения Try Xpath, взаимодействует со страницей для поиска и выделения элементов, а также управляет стилями и атрибутами элементов на странице.

## Оглавление

1. [Глобальные переменные](#глобальные-переменные)
2. [Функции](#функции)
    - [`setAttr`](#setattr)
    - [`setIndex`](#setindex)
    - [`isFocusable`](#isfocusable)
    - [`focusItem`](#focusitem)
    - [`setMainAttrs`](#setmainattrs)
    - [`restoreAttrs`](#restoreattrs)
    - [`resetPrev`](#resetprev)
    - [`makeTypeStr`](#maketypestr)
    - [`updateCss`](#updatecss)
    - [`getFrames`](#getframes)
    - [`parseFrameDesignation`](#parseframedesignation)
    - [`traceBlankWindows`](#traceblankwindows)
    - [`handleCssChange`](#handlecsschange)
    - [`findFrameByMessage`](#findframebymessage)
    - [`setFocusFrameListener`](#setfocusframelistener)
    - [`initBlankWindow`](#initblankwindow)
    - [`findStyleParent`](#findstyleparent)
    - [`updateStyleElement`](#updatestyleelement)
    - [`updateAllStyleElements`](#updateallstyleelements)
    - [`removeStyleElement`](#removestyleelement)
    - [`removeAllStyleElements`](#removeallstyleelements)
    - [`createResultMessage`](#createresultmessage)
    - [`genericListener`](#genericlistener)
    - [`genericListener.listeners.setContentInfo`](#genericlistenerlistenerssetcontentinfo)
    - [`genericListener.listeners.execute`](#genericlistenerlistenersexecute)
    - [`genericListener.listeners.focusItem`](#genericlistenerlistenersfocusitem)
    - [`genericListener.listeners.focusContextItem`](#genericlistenerlistenersfocuscontextitem)
    - [`genericListener.listeners.focusFrame`](#genericlistenerlistenersfocusframe)
    - [`genericListener.listeners.requestShowResultsInPopup`](#genericlistenerlistenersrequestshowresultsinpopup)
    - [`genericListener.listeners.requestShowAllResults`](#genericlistenerlistenersrequestshowallresults)
    - [`genericListener.listeners.resetStyle`](#genericlistenerlistenersresetstyle)
    - [`genericListener.listeners.setStyle`](#genericlistenerlistenerssetstyle)
    - [`genericListener.listeners.finishInsertCss`](#genericlistenerlistenersfinishinsertcss)
    - [`genericListener.listeners.finishRemoveCss`](#genericlistenerlistenersfinishremovecss)

## Глобальные переменные

- `tx`: Псевдоним для `tryxpath`.
- `fu`: Псевдоним для `tryxpath.functions`.
- `tx.isContentLoaded`: Флаг, указывающий, загружено ли содержимое.
- `dummyItem`: Пустая строка.
- `dummyItems`: Пустой массив.
- `invalidExecutionId`: Значение `NaN`, представляющее недействительный идентификатор выполнения.
- `styleElementHeader`: Заголовок для стилей, добавляемых скриптом.
- `attributes`: Объект с атрибутами для элементов.
- `prevMsg`: Предыдущее сообщение.
- `executionCount`: Счетчик выполнений.
- `inBlankWindow`: Флаг, указывающий, выполняется ли скрипт в пустом окне.
- `currentDocument`: Текущий документ.
- `contextItem`: Контекстный элемент.
- `currentItems`: Массив текущих элементов.
- `focusedItem`: Фокусируемый элемент.
- `focusedAncestorItems`: Массив предковых элементов фокусируемого элемента.
- `currentCss`: Текущий CSS.
- `insertedStyleElements`: `Map` для хранения вставленных элементов стилей.
- `expiredCssSet`: Набор CSS, которые нужно обновить.
- `originalAttributes`: `Map` для хранения исходных атрибутов элементов.

## Функции

### `setAttr`
```javascript
function setAttr(attr, value, item)
```
**Описание**: Сохраняет исходный атрибут элемента и устанавливает новый атрибут.

**Параметры**:
- `attr` (string): Имя атрибута.
- `value` (string): Значение атрибута.
- `item` (Element): Элемент.

**Возвращает**:
- `undefined`

### `setIndex`
```javascript
function setIndex(attr, items)
```
**Описание**: Сохраняет исходные атрибуты для массива элементов и устанавливает индекс в качестве атрибута.

**Параметры**:
- `attr` (string): Имя атрибута.
- `items` (Array<Element>): Массив элементов.

**Возвращает**:
- `undefined`

### `isFocusable`
```javascript
function isFocusable(item)
```
**Описание**: Проверяет, является ли элемент фокусируемым.

**Параметры**:
- `item` (Element): Проверяемый элемент.

**Возвращает**:
- `boolean`: `true`, если элемент фокусируемый, иначе `false`.

### `focusItem`
```javascript
function focusItem(item)
```
**Описание**: Устанавливает фокус на элементе и выделяет его предков.

**Параметры**:
- `item` (Element): Элемент для фокусировки.

**Возвращает**:
- `undefined`

### `setMainAttrs`
```javascript
function setMainAttrs()
```
**Описание**: Устанавливает атрибуты для контекстного элемента и текущих элементов.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `restoreAttrs`
```javascript
function restoreAttrs()
```
**Описание**: Восстанавливает оригинальные атрибуты элементов и очищает `originalAttributes`.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `resetPrev`
```javascript
function resetPrev()
```
**Описание**: Сбрасывает значения переменных и счетчика выполнения.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `makeTypeStr`
```javascript
function makeTypeStr(resultType)
```
**Описание**: Формирует строку для типа результата XPath.

**Параметры**:
- `resultType` (number): Числовое представление типа результата.

**Возвращает**:
- `string`: Строка с типом результата или пустая строка.

### `updateCss`
```javascript
function updateCss()
```
**Описание**: Отправляет сообщение расширению для обновления CSS.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `getFrames`
```javascript
function getFrames(spec)
```
**Описание**: Получает массив фреймов на основе спецификации.

**Параметры**:
- `spec` (string): JSON-строка с индексами фреймов.

**Возвращает**:
- `Array<Window>`: Массив фреймов.

**Вызывает исключения**:
- `Error`: Если спецификация недействительна.

### `parseFrameDesignation`
```javascript
function parseFrameDesignation(frameDesi)
```
**Описание**: Разбирает JSON-строку со спецификацией фреймов.

**Параметры**:
- `frameDesi` (string): JSON-строка со спецификацией фреймов.

**Возвращает**:
- `Array<number>`: Массив индексов фреймов.

**Вызывает исключения**:
- `Error`: Если спецификация недействительна.

### `traceBlankWindows`
```javascript
function traceBlankWindows(desi, win)
```
**Описание**: Проверяет и возвращает массив окон, соответствующих индексам, и проверяет, являются ли они пустыми окнами.

**Параметры**:
- `desi` (Array<number>): Массив индексов фреймов.
- `win` (Window): Стартовое окно.

**Возвращает**:
- `Object`: Объект со свойствами `success` (boolean), `failedWindow` (Window) и `windows` (Array<Window>).

### `handleCssChange`
```javascript
function handleCssChange(newCss)
```
**Описание**: Обрабатывает изменение CSS.

**Параметры**:
- `newCss` (string): Новый CSS.

**Возвращает**:
- `undefined`

### `findFrameByMessage`
```javascript
function findFrameByMessage(event, win)
```
**Описание**: Находит фрейм по сообщению.

**Параметры**:
- `event` (MessageEvent): Событие сообщения.
- `win` (Window): Окно, в котором произошло событие.

**Возвращает**:
- `HTMLElement | null`: Элемент фрейма или `null`, если не найден.

### `setFocusFrameListener`
```javascript
function setFocusFrameListener(win, isBlankWindow)
```
**Описание**: Устанавливает слушателя событий для фокусировки фрейма.

**Параметры**:
- `win` (Window): Окно, на которое устанавливается слушатель.
- `isBlankWindow` (boolean): Флаг, указывающий, является ли окно пустым.

**Возвращает**:
- `undefined`

### `initBlankWindow`
```javascript
function initBlankWindow(win)
```
**Описание**: Инициализирует пустое окно для взаимодействия с расширением.

**Параметры**:
- `win` (Window): Пустое окно.

**Возвращает**:
- `undefined`

### `findStyleParent`
```javascript
function findStyleParent(doc)
```
**Описание**: Находит родительский элемент для вставки стилей.

**Параметры**:
- `doc` (Document): Документ, в котором ищется родительский элемент.

**Возвращает**:
- `HTMLElement | null`: Родительский элемент (head или body) или `null`.

### `updateStyleElement`
```javascript
function updateStyleElement(doc)
```
**Описание**: Обновляет или создает элемент style в документе.

**Параметры**:
- `doc` (Document): Документ, в котором нужно обновить стили.

**Возвращает**:
- `undefined`

### `updateAllStyleElements`
```javascript
function updateAllStyleElements()
```
**Описание**: Обновляет все элементы style во всех документах.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `removeStyleElement`
```javascript
function removeStyleElement(doc)
```
**Описание**: Удаляет элемент style из документа.

**Параметры**:
- `doc` (Document): Документ, из которого нужно удалить стиль.

**Возвращает**:
- `undefined`

### `removeAllStyleElements`
```javascript
function removeAllStyleElements()
```
**Описание**: Удаляет все элементы style из всех документов.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `createResultMessage`
```javascript
function createResultMessage()
```
**Описание**: Создает объект сообщения с дефолтными значениями для показа результатов.

**Параметры**:
- `undefined`

**Возвращает**:
- `Object`: Объект сообщения.

### `genericListener`
```javascript
function genericListener(message, sender, sendResponse)
```
**Описание**: Обработчик сообщений, перенаправляющий их соответствующим функциям.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя.
- `sendResponse` (function): Функция для отправки ответа.

**Возвращает**:
- `undefined`

### `genericListener.listeners.setContentInfo`
```javascript
genericListener.listeners.setContentInfo = function (message)
```
**Описание**: Устанавливает информацию о контенте (атрибуты).

**Параметры**:
- `message` (object): Объект сообщения, содержащий атрибуты.

**Возвращает**:
- `undefined`

### `genericListener.listeners.execute`
```javascript
genericListener.listeners.execute = function(message, sender)
```
**Описание**: Выполняет запрос на выполнение XPath и отправляет результаты.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя.

**Возвращает**:
- `undefined`

### `genericListener.listeners.focusItem`
```javascript
genericListener.listeners.focusItem = function(message)
```
**Описание**: Фокусирует элемент по индексу.

**Параметры**:
- `message` (object): Объект сообщения, содержащий индекс элемента.

**Возвращает**:
- `undefined`

### `genericListener.listeners.focusContextItem`
```javascript
genericListener.listeners.focusContextItem = function(message)
```
**Описание**: Фокусирует контекстный элемент.

**Параметры**:
- `message` (object): Объект сообщения.

**Возвращает**:
- `undefined`

### `genericListener.listeners.focusFrame`
```javascript
genericListener.listeners.focusFrame = function(message)
```
**Описание**: Фокусирует фрейм.

**Параметры**:
- `message` (object): Объект сообщения.

**Возвращает**:
- `undefined`

### `genericListener.listeners.requestShowResultsInPopup`
```javascript
genericListener.listeners.requestShowResultsInPopup = function ()
```
**Описание**: Отправляет предыдущие результаты во всплывающее окно.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `genericListener.listeners.requestShowAllResults`
```javascript
genericListener.listeners.requestShowAllResults = function ()
```
**Описание**: Отправляет все результаты во всплывающее окно.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `genericListener.listeners.resetStyle`
```javascript
genericListener.listeners.resetStyle = function ()
```
**Описание**: Сбрасывает стили и атрибуты.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `genericListener.listeners.setStyle`
```javascript
genericListener.listeners.setStyle = function ()
```
**Описание**: Применяет текущий стиль к элементам.

**Параметры**:
- `undefined`

**Возвращает**:
- `undefined`

### `genericListener.listeners.finishInsertCss`
```javascript
genericListener.listeners.finishInsertCss = function (message)
```
**Описание**: Обрабатывает завершение вставки CSS.

**Параметры**:
- `message` (object): Объект сообщения, содержащий CSS.

**Возвращает**:
- `undefined`

### `genericListener.listeners.finishRemoveCss`
```javascript
genericListener.listeners.finishRemoveCss = function (message)
```
**Описание**: Обрабатывает завершение удаления CSS.

**Параметры**:
- `message` (object): Объект сообщения, содержащий CSS.

**Возвращает**:
- `undefined`