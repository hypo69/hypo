# Модуль try_xpath_content.js

## Обзор

Этот модуль содержит JavaScript-код, реализующий функциональность для работы с XPath-выражениями в браузере. Он отвечает за выполнение запросов, фокусирование элементов, обновление стилей и взаимодействие с расширением.

## Переменные

### `tx`

**Описание**: псевдоним для объекта `tryxpath`.

### `fu`

**Описание**: псевдоним для объекта `tryxpath.functions`.

### `tx.isContentLoaded`

**Описание**: флаг, указывающий, был ли код загружен в контент страницы. Используется для предотвращения повторной инициализации.

### `dummyItem`, `dummyItems`

**Описание**: Пустые значения, используемые в качестве начальных значений для переменных, хранящих данные об элементах.

### `invalidExecutionId`

**Описание**: Специальное значение `NaN`, используемое для обозначения недействительного идентификатора выполнения.

### `styleElementHeader`

**Описание**: Строка, которая добавляется в начало CSS, вставляемого в стилевой элемент.

### `attributes`

**Описание**: Объект, содержащий имена атрибутов, используемых для хранения информации об элементах.

### `prevMsg`

**Описание**: Содержит последнюю отправленное сообщение.

### `executionCount`

**Описание**: Счетчик ID выполнения запросов.

### `inBlankWindow`

**Описание**: Флаг, показывающий, выполняются ли действия в фрейме или окне.

### `currentDocument`

**Описание**: Текущий документ, на котором выполняются операции.

### `contextItem`

**Описание**: Текущий элемент контекста для XPath-выражения.

### `currentItems`

**Описание**: Список элементов, полученных в результате выполнения XPath-выражения.

### `focusedItem`

**Описание**: Выбранный элемент.

### `focusedAncestorItems`

**Описание**: Список предковых элементов выбранного элемента.

### `currentCss`

**Описание**: Текущий CSS-код.

### `insertedStyleElements`

**Описание**: Хранит карту для связи между документами и вставленными стилевыми элементами.

### `expiredCssSet`

**Описание**: Объект, хранящий информацию о просроченных CSS-стилях.

### `originalAttributes`

**Описание**: Хранит оригинальные атрибуты элементов для их восстановления.


## Функции

### `setAttr(attr, value, item)`

**Описание**: Устанавливает атрибут для элемента.

**Параметры**:
- `attr` (str): Имя атрибута.
- `value` (str): Значение атрибута.
- `item` (object): Элемент, для которого устанавливается атрибут.

### `setIndex(attr, items)`

**Описание**: Устанавливает атрибут для списка элементов.

**Параметры**:
- `attr` (str): Имя атрибута.
- `items` (array): Список элементов.


### `isFocusable(item)`

**Описание**: Проверяет, можно ли фокусировать элемент.

**Параметры**:
- `item` (object): Элемент.

**Возвращает**:
- `boolean`: `true`, если элемент можно фокусировать; `false` иначе.

### `focusItem(item)`

**Описание**: Фокусирует указанный элемент.

**Параметры**:
- `item` (object): Элемент, который нужно фокусировать.


### `setMainAttrs()`

**Описание**: Устанавливает основные атрибуты для элементов контекста.

### `restoreAttrs()`

**Описание**: Восстанавливает первоначальные атрибуты элементов.

### `resetPrev()`

**Описание**: Сбрасывает значения переменных, связанных с предыдущим выполнением.


### `makeTypeStr(resultType)`

**Описание**: Преобразует тип результата в строку.

**Параметры**:
- `resultType` (number): Тип результата.

**Возвращает**:
- `str`: Строковое представление типа результата.


### `updateCss()`

**Описание**: Отправляет сообщение о необходимости обновления CSS в контекстную страницу.

### `getFrames(spec)`

**Описание**: Получает список фреймов по указанному спецификации.

**Параметры**:
- `spec` (string): Спецификация фреймов в формате JSON.

**Возвращает**:
- `array` Список фреймов.


### `parseFrameDesignation(frameDesi)`

**Описание**: Парсит строку обозначения фреймов.

**Параметры**:
- `frameDesi` (string): Обозначение фреймов в формате JSON.

**Возвращает**:
- `array` Список индексов фреймов.


### `traceBlankWindows(desi, win)`

**Описание**: Трассирует все окна, переданные в функции.

**Параметры**:
- `desi` (array): Массив индексов фреймов.
- `win` (Window, optional): Окно.

**Возвращает**:
- `object`: Объект с результатами.


### `handleCssChange(newCss)`

**Описание**: Обрабатывает изменение CSS.

**Параметры**:
- `newCss` (string): Новый CSS-код.

### `findFrameByMessage(event, win)`

**Описание**: Находит фрейм по сообщению.

**Параметры**:
- `event` (object): Объект события.
- `win` (Window): Текущее окно.

**Возвращает**:
- `Window`: Найденный фрейм или `null`.


### `setFocusFrameListener(win, isBlankWindow)`

**Описание**: Устанавливает слушатель для сообщений о фокусировании фреймов.

**Параметры**:
- `win` (Window): Текущее окно.
- `isBlankWindow` (boolean): Флаг, указывающий, является ли окно пустым.



### `initBlankWindow(win)`

**Описание**: Инициализирует окно, если оно еще не инициализировано.

**Параметры**:
- `win` (Window): Окно.


### `findStyleParent(doc)`

**Описание**: Находит родительский элемент для вставки стилевого элемента.

**Параметры**:
- `doc` (Document): Документ.

**Возвращает**:
- `Element`: Родительский элемент, или `null` если не найден.


### `updateStyleElement(doc)`

**Описание**: Обновляет стилевой элемент в документе.

**Параметры**:
- `doc` (Document): Документ.

### `updateAllStyleElements()`

**Описание**: Обновляет все стилевые элементы.

### `removeStyleElement(doc)`

**Описание**: Удаляет стилевой элемент из документа.

**Параметры**:
- `doc` (Document): Документ.


### `removeAllStyleElements()`

**Описание**: Удаляет все стилевые элементы.

### `createResultMessage()`

**Описание**: Создает сообщение для отправки результата в поп-ап окно.

**Возвращает**:
- `object`: Объект с информацией о результате.


### `genericListener(message, sender, sendResponse)`

**Описание**: Общий слушатель сообщений.

**Параметры**:
- `message` (object): Сообщение.
- `sender` (object): Отправитель сообщения.
- `sendResponse` (function): Функция для отправки ответа.

### `genericListener.listeners`

**Описание**: Хранилище слушателей для конкретных событий.


### `genericListener.listeners.setContentInfo`

**Описание**: Слушатель для обновления атрибутов.

**Параметры**:
- `message` (object): Сообщение.

### `genericListener.listeners.execute`

**Описание**: Обрабатывает запрос на выполнение XPath-выражения.

**Параметры**:
- `message` (object): Запрос.
- `sender` (object): Отправитель.

### `genericListener.listeners.focusItem`

**Описание**: Фокусирует элемент по индексу.

**Параметры**:
- `message` (object): Сообщение.

### `genericListener.listeners.focusContextItem`

**Описание**: Фокусирует контекстный элемент.

**Параметры**:
- `message` (object): Сообщение.

### `genericListener.listeners.focusFrame`

**Описание**: Фокусирует фрейм.

**Параметры**:
- `message` (object): Сообщение.

### `genericListener.listeners.requestShowResultsInPopup`

**Описание**: Запрашивает отображение результатов в поп-ап окне.

### `genericListener.listeners.requestShowAllResults`

**Описание**: Запрашивает отображение всех результатов.

### `genericListener.listeners.resetStyle`

**Описание**: Сбрасывает CSS стили.

### `genericListener.listeners.setStyle`

**Описание**: Устанавливает CSS стили.

### `genericListener.listeners.finishInsertCss`

**Описание**: Обрабатывает завершение вставки CSS кода.

**Параметры**:
- `message` (object): Сообщение.

### `genericListener.listeners.finishRemoveCss`

**Описание**: Обрабатывает завершение удаления CSS кода.

**Параметры**:
- `message` (object): Сообщение.


## Обработчики событий

### `browser.storage.onChanged`

**Описание**: Обработчик изменений в хранилище браузера.


### `window.addEventListener("message")`

**Описание**: Слушатель сообщений из других окон и фреймов.


## Замечания

Код использует псевдонимы `tx` и `fu` для доступа к объектам `tryxpath` и `tryxpath.functions`.