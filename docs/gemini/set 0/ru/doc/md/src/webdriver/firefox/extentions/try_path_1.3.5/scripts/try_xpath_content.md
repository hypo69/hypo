# Модуль try_xpath_content.js

## Обзор

Этот JavaScript-модуль реализует функциональность обработки запросов и управления отображением результатов для дополнения браузера Try XPath. Он отвечает за взаимодействие с расширением, получение данных из DOM, установку атрибутов элементов и обработку событий сообщений.  Модуль использует API браузера для коммуникации и управления стилями.


## Переменные

### `tx`

**Описание**: Псевдоним для глобальной переменной `tryxpath`.


### `fu`

**Описание**: Псевдоним для глобальной переменной `tryxpath.functions`.


### `tx.isContentLoaded`

**Описание**: Логическая переменная, используемая для предотвращения многократного выполнения кода.


### `dummyItem`, `dummyItems`

**Описание**: Пустые значения, используемые в качестве начальных значений для переменных, хранящих элементы.


### `invalidExecutionId`

**Описание**: Специальное значение `NaN`, используемое для идентификации ошибок при выполнении запросов.


### `styleElementHeader`

**Описание**: Строка, содержащая комментарий для элемента стиля, вставляемого дополнением.


### `attributes`

**Описание**: Объект, содержащий имена атрибутов, используемых для маркировки элементов.


### `prevMsg`

**Описание**:  Переменная, хранящая последнее отправленное сообщение.


### `executionCount`

**Описание**: Счётчик идентификаторов выполнения.


### `inBlankWindow`

**Описание**: Логическая переменная, указывающая, находится ли код в контексте фрейма.


### `currentDocument`

**Описание**: Текущий документ, с которым работает код.


### `contextItem`, `currentItems`, `focusedItem`, `focusedAncestorItems`

**Описание**: Переменные, хранящие контекстные элементы и фокусированные узлы.


### `currentCss`, `insertedStyleElements`, `expiredCssSet`, `originalAttributes`

**Описание**: Переменные, используемые для управления стилями, запоминания первоначальных атрибутов и других служебных данных.


## Функции

### `setAttr`

**Описание**: Устанавливает атрибут элемента.

**Параметры**:

- `attr` (строка): Имя атрибута.
- `value` (строка): Значение атрибута.
- `item` (элемент): Элемент, которому нужно установить атрибут.

**Возвращает**:
- `void`


### `setIndex`

**Описание**: Устанавливает индекс элементов.

**Параметры**:

- `attr` (строка): Имя атрибута.
- `items` (массив элементов): Массив элементов, которым нужно установить индекс.

**Возвращает**:
- `void`


### `isFocusable`

**Описание**: Проверяет, может ли элемент быть фокусирован.

**Параметры**:

- `item` (элемент): Проверяемый элемент.

**Возвращает**:
- `boolean`: `true`, если элемент может быть фокусирован, `false` иначе.


### `focusItem`

**Описание**: Устанавливает фокус на элемент.

**Параметры**:

- `item` (элемент): Элемент, на который нужно установить фокус.

**Возвращает**:
- `void`

**Возможные исключения**:
- `Error`: Если `item` не может быть фокусирован.


### `setMainAttrs`

**Описание**: Устанавливает основные атрибуты элементов.

**Возвращает**:
- `void`


### `restoreAttrs`

**Описание**: Восстанавливает первоначальные атрибуты элементов.

**Возвращает**:
- `void`


### `resetPrev`

**Описание**: Сбрасывает предыдущие данные.

**Возвращает**:
- `void`


### `makeTypeStr`

**Описание**: Преобразует результат в строку.

**Параметры**:

- `resultType` (число): Результат выполнения.

**Возвращает**:
- `строка`: Строковое представление результата.



### `updateCss`

**Описание**: Обновляет CSS стили.

**Возвращает**:
- `void`



### `getFrames`

**Описание**: Возвращает массив фреймов по заданному списку индексов.

**Параметры**:

- `spec` (строка): JSON-представление спика индексов.

**Возвращает**:
- `массив фреймов`: Массив фреймов.

**Возможные исключения**:
- `Error`: Если спецификация некорректна.


### `parseFrameDesignation`

**Описание**: Парсит строку, содержащую индексы фреймов.

**Параметры**:

- `frameDesi` (строка): JSON-представление списка индексов фреймов.

**Возвращает**:
- `массив чисел`: Массив индексов фреймов.

**Возможные исключения**:
- `Error`: Если спецификация некорректна.



### `traceBlankWindows`

**Описание**: Проверяет, что все фреймы в указанном списке являются пустыми.

**Параметры**:

- `desi` (массив чисел): Список индексов фреймов.
- `win` (объект Window, необязательно): Текущее окно.

**Возвращает**:
- `объект`: Объект, содержащий массив фреймов, или ошибку.

**Возможные исключения**:
- `Error`: Возникает, если фрейм не найден.



### `handleCssChange`

**Описание**: Обрабатывает изменения CSS.

**Параметры**:

- `newCss` (строка): Новые CSS стили.

**Возвращает**:
- `void`


### `findFrameByMessage`

**Описание**: Находит фрейм по сообщению.

**Параметры**:

- `event` (объект события): Объект события.
- `win` (объект Window): Текущее окно.

**Возвращает**:
- `элемент фрейма`: Элемент фрейма.


### `setFocusFrameListener`

**Описание**: Добавляет слушатель событий для фреймов.

**Параметры**:

- `win` (объект Window): Текущее окно.
- `isBlankWindow` (boolean):  Флаг, показывающий, что это пустое окно.


### `initBlankWindow`

**Описание**: Инициализирует пустое окно.

**Параметры**:

- `win` (объект Window): Текущее окно.

**Возвращает**:
- `void`


### `findStyleParent`

**Описание**: Находит родительский элемент для вставки элемента стиля.

**Параметры**:

- `doc` (объект документа): Объект документа.

**Возвращает**:
- `элемент`: Родительский элемент или `null`.


### `updateStyleElement`

**Описание**: Обновляет элемент стиля.

**Параметры**:

- `doc` (объект документа): Объект документа.


### `updateAllStyleElements`

**Описание**: Обновляет все элементы стиля.

### `removeStyleElement`

**Описание**: Удаляет элемент стиля.

**Параметры**:

- `doc` (объект документа): Объект документа.

**Возвращает**:
- `void`

### `removeAllStyleElements`

**Описание**: Удаляет все элементы стиля.

**Возвращает**:
- `void`



### `createResultMessage`

**Описание**: Создает объект сообщения для отправки результата.


### `genericListener`

**Описание**: Общий слушатель сообщений.


### `setContentInfo`

**Описание**: Обрабатывает сообщения, связанные с атрибутами.

**Параметры**:

- `message` (объект): Сообщение с информацией об атрибутах.


### `execute`

**Описание**: Обрабатывает запрос на выполнение XPath выражения.

**Параметры**:

- `message` (объект): Сообщение с запросом.


**Возможные исключения**:
- `Error`: Возникает при ошибках в процессе получения фрейма или контекста.



### `focusItem`, `focusContextItem`, `focusFrame`

**Описание**: Обработчики событий для установки фокуса.


### `requestShowResultsInPopup`, `requestShowAllResults`

**Описание**: Обработчики запросов на отображение результатов.


### `resetStyle`, `setStyle`


**Описание**: Обработчики запросов на сброс и обновление стилей.



### `finishInsertCss`, `finishRemoveCss`

**Описание**: Обработчики событий, связанные с изменением CSS.


###  Обработчик событий `storage.onChanged`

**Описание**: Обрабатывает изменения в хранилище браузера, особенно изменения настроек атрибутов и CSS стилей.

## API (общие методы)

* `tx` (объект) - доступ к основным функциям Try XPath.
* `fu` (объект) - доступ к внутренним функциям.
* `browser` (объект) - доступ к API браузера.


## Замечания

Этот модуль использует сложную логику для обработки различных сценариев, включая работу с фреймами, контекстами и управлением стилями.  Описания некоторых функций содержат упрощенные версии.  Более полное понимание requires детальный анализ соответствующего кода.