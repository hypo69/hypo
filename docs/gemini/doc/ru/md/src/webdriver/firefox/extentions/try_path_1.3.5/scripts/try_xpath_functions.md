# Модуль try_xpath_functions.js

## Обзор

Данный модуль предоставляет набор функций для работы с XPath выражениями и DOM-элементами в JavaScript.  Он позволяет выполнять XPath запросы, получать результаты в виде массивов, обрабатывать различные типы результатов (числа, строки, булевы значения, узлы), а также манипулировать классами и атрибутами элементов.

## Функции

### `execExpr`

**Описание**: Выполняет XPath выражение или JavaScript селектор в заданном контексте.

**Параметры**:

- `expr` (string): XPath выражение или селектор.
- `method` (string): Метод для выполнения выражения. Может быть `evaluate`, `querySelector` или `querySelectorAll`.
- `opts` (object, optional): Опциональный объект с параметрами:
    - `context` (object, optional): Контекст для выполнения выражения (документ, элемент или атрибут).
    - `resolver` (function|string|object, optional): Функция-резолвр для замены значений в XPath.
    - `resultType` (number, optional): Тип результата XPath выражения (xpathResult.ANY_TYPE по умолчанию).
    - `document` (Document, optional): Документ для выполнения выражения.

**Возвращает**:

- object: Объект с результатами выполнения:
    - `items` (array): Массив результатов (узлы, значения).
    - `method` (string): Метод, использованный для выполнения.
    - `resultType` (number): Тип возвращённого результата.


**Вызывает исключения**:

- `Error`: Возникает, если контекст не является допустимым типом (Node, Attr) для метода `evaluate`, или элементом документа для `querySelector`/`querySelectorAll`.
- `Error`: Возникает при невалидном `resolver` или при ошибке разбора JSON `resolver`.
- `Error`: Возникает при невалидном типе результата `resultType`.

### `resToArr`

**Описание**: Преобразует результат XPath выражения в массив.

**Параметры**:

- `res` (object): Результат выполнения XPath выражения (объект `XPathResult`).
- `type` (number, optional): Тип результата (если не указан, берется из `res`).

**Возвращает**:

- array: Массив результатов.

**Вызывает исключения**:

- `Error`: Возникает, если тип результата `type` не является допустимым.


### `makeResolver`

**Описание**: Создает функцию-резолвр для замены значений в XPath.

**Параметры**:

- `obj` (function|string|object): Функция или строка (JSON-представление объекта), определяющие правила замены.

**Возвращает**:

- function: Функция-резолвр.

**Вызывает исключения**:

- `Error`: Возникает, если `obj` не является допустимым типом для резолвера (null, функция или JSON-строка) или если переданный JSON невалиден.


### `isValidDict`

**Описание**: Проверяет, является ли переданный объект валидным словарем.

**Параметры**:

- `obj` (object): Объект для проверки.

**Возвращает**:

- boolean: `True`, если объект является валидным словарем, иначе `False`.


### `objToMap`

**Описание**: Преобразует объект в Map.

**Параметры**:

- `obj` (object): Объект для преобразования.

**Возвращает**:

- Map: Map, содержащий пары ключ-значение из входного объекта.



... (документация для остальных функций)