# Модуль try_xpath_functions.js

## Обзор

Этот модуль содержит набор функций для работы с XPath, включая оценку выражений XPath, выбор элементов с помощью `querySelector` и `querySelectorAll`, обработку результатов и работу с атрибутами элементов.  Модуль предоставляет методы для работы с узлами DOM, такими как получение детальной информации об элементах, сохранение и восстановление атрибутов, создание таблиц и строк.

## Функции

### `execExpr`

**Описание**: Выполняет заданный XPath запрос или метод `querySelector` / `querySelectorAll` на предоставленном контексте.

**Параметры**:
- `expr` (str): XPath выражение или CSS селектор.
- `method` (str): Метод для выполнения запроса ("evaluate", "querySelector", "querySelectorAll").
- `opts` (dict, optional): Опции для выполнения запроса.

    - `context` (объект DOM, optional): Контекст для выполнения запроса (по умолчанию `document`).
    - `resolver` (функция или строка JSON, optional): Функция для обработки значений или JSON строка, содержащая словарь.
    - `document` (объект DOM, optional): Документ, используемый для обработки запроса.

**Возвращает**:
- `dict`: Словарь, содержащий результаты выполнения запроса:
    - `items` (list): Список результатов (узлов, чисел или строк).
    - `method` (str): Используемый метод (evaluate, querySelector, querySelectorAll).
    - `resultType` (число xpathResult, optional): Тип результата (если метод - evaluate).

**Вызывает исключения**:
- `Error`: Возникает при недопустимом контексте для запроса.


### `resToArr`

**Описание**: Преобразует результат XPath в массив.

**Параметры**:
- `res` (объект XPathResult): Результат выполнения XPath запроса.
- `type` (число xpathResult, optional): Тип результата.

**Возвращает**:
- `array`: Массив результатов.

**Вызывает исключения**:
- `Error`: Возникает при недопустимом типе результата.


### `makeResolver`

**Описание**: Создает функцию-разрешитель для обработки значений в XPath.

**Параметры**:
- `obj` (функция или строка JSON, optional): Функция или JSON строка с разрешением.

**Возвращает**:
- `function`: Функция-разрешитель.

**Вызывает исключения**:
- `Error`: Возникает при некорректном формате JSON разрешения.


### `isValidDict`

**Описание**: Проверяет, является ли переданный объект корректным словарем.

**Параметры**:
- `obj` (object, optional): Объект для проверки.

**Возвращает**:
- `bool`: `True`, если объект является корректным словарем, иначе `False`.


### `objToMap`

**Описание**: Преобразует словарь в объект `Map`.

**Параметры**:
- `obj` (object): Словарь.

**Возвращает**:
- `Map`: Объект `Map`.


### `isDocOrElem`

**Описание**: Проверяет, является ли объект элементом (`Element`) или документом (`Document`).

**Параметры**:
- `obj` (object): Объект для проверки.

**Возвращает**:
- `bool`: `True`, если объект является элементом или документом, иначе `False`.


### `listToArr`

**Описание**: Преобразует список в массив.

**Параметры**:
- `list` (list): Список.

**Возвращает**:
- `array`: Массив.


### `getItemDetail`

**Описание**: Возвращает подробную информацию об элементе.

**Параметры**:
- `item` (object): Элемент.

**Возвращает**:
- `dict`: Словарь с информацией об элементе.


### `getItemDetails`

**Описание**: Возвращает подробную информацию о списке элементов.

**Параметры**:
- `items` (list): Список элементов.

**Возвращает**:
- `array`: Массив словарей с информацией об элементах.


### `getNodeTypeStr`

**Описание**: Преобразует числовой тип узла в строковое представление.

**Параметры**:
- `nodeType` (число): Тип узла.

**Возвращает**:
- `str`: Строковое представление типа узла.


### `getxpathResultStr`, `getxpathResultNum`

**Описание**: Преобразует числовой тип результата XPath в строковое представление и наоборот.

**Параметры**:
- `resultType` (число xpathResult, optional): Тип результата.

**Возвращает**:
- `str`: Строковое представление типа результата.


### `isAttrItem`, `isNodeItem`, `isElementItem`

**Описание**: Проверяет, является ли объект узлом, атрибутом, элементом.

**Параметры**:
- `item` (object): Объект для проверки.

**Возвращает**:
- `bool`: `True` или `False`.


### ... (и так далее для остальных функций)