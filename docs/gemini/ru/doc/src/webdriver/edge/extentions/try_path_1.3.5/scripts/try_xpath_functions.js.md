# tryxpath.functions

## Обзор

Данный модуль `tryxpath.functions.js` предоставляет набор функций для работы с XPath и DOM в JavaScript. Он включает в себя функции для выполнения XPath-выражений, обработки результатов, преобразования типов, работы с элементами и их атрибутами, а также для работы с фреймами.

## Оглавление
- [Обзор](#обзор)
- [Функции](#функции)
    - [`execExpr`](#execExpr)
    - [`resToArr`](#resToArr)
    - [`makeResolver`](#makeResolver)
    - [`isValidDict`](#isValidDict)
    - [`objToMap`](#objToMap)
    - [`isDocOrElem`](#isDocOrElem)
    - [`listToArr`](#listToArr)
    - [`getItemDetail`](#getItemDetail)
    - [`getItemDetails`](#getItemDetails)
    - [`getNodeTypeStr`](#getNodeTypeStr)
    - [`getxpathResultStr`](#getxpathResultStr)
    - [`getxpathResultNum`](#getxpathResultNum)
    - [`isAttrItem`](#isAttrItem)
    - [`isNodeItem`](#isNodeItem)
    - [`isElementItem`](#isElementItem)
    - [`addClassToItem`](#addClassToItem)
    - [`addClassToItems`](#addClassToItems)
    - [`saveItemClass`](#saveItemClass)
    - [`restoreItemClass`](#restoreItemClass)
    - [`saveItemClasses`](#saveItemClasses)
    - [`restoreItemClasses`](#restoreItemClasses)
    - [`setAttrToItem`](#setAttrToItem)
    - [`removeAttrFromItem`](#removeAttrFromItem)
    - [`removeAttrFromItems`](#removeAttrFromItems)
    - [`setIndexToItems`](#setIndexToItems)
    - [`getParentElement`](#getParentElement)
    - [`getAncestorElements`](#getAncestorElements)
    - [`getOwnerDocument`](#getOwnerDocument)
    - [`createHeaderRow`](#createHeaderRow)
    - [`createDetailTableHeader`](#createDetailTableHeader)
    - [`createDetailRow`](#createDetailRow)
    - [`appendDetailRows`](#appendDetailRows)
    - [`updateDetailsTable`](#updateDetailsTable)
    - [`emptyChildNodes`](#emptyChildNodes)
    - [`saveAttrForItem`](#saveAttrForItem)
    - [`saveAttrForItems`](#saveAttrForItems)
    - [`restoreItemAttrs`](#restoreItemAttrs)
    - [`getFrameAncestry`](#getFrameAncestry)
    - [`isNumberArray`](#isNumberArray)
    - [`onError`](#onError)
    - [`isBlankWindow`](#isBlankWindow)
    - [`collectBlankWindows`](#collectBlankWindows)
    - [`findFrameElement`](#findFrameElement)
    - [`findFrameIndex`](#findFrameIndex)
    - [`makeDetailText`](#makeDetailText)

## Функции

### `execExpr`

**Описание**: Выполняет XPath выражение или CSS селектор в заданном контексте.

**Параметры**:
- `expr` (string): XPath выражение или CSS селектор.
- `method` (string): Метод выполнения ("evaluate", "querySelector", "querySelectorAll").
- `opts` (object, optional): Опции выполнения. Может включать:
    - `context` (Node, optional): Контекстный узел для выполнения запроса. По умолчанию `document`.
    - `resolver` (object | string | function, optional): Пользовательский преобразователь пространства имен.
    - `document` (Document, optional): Документ, в котором выполняется запрос.
    - `resultType` (number, optional): Тип результата XPath.

**Возвращает**:
- `object`: Объект, содержащий:
    - `items` (array): Массив элементов, соответствующих запросу.
    - `method` (string): Использованный метод.
    - `resultType` (number): Тип результата XPath.

**Вызывает исключения**:
- `Error`: Если контекст не является корректным узлом или атрибутом для XPath.
- `Error`: Если контекст не является `Document` или `Element` для `querySelector` и `querySelectorAll`.

### `resToArr`

**Описание**: Преобразует результат XPath в массив.

**Параметры**:
- `res` (XPathResult): Результат XPath.
- `type` (number, optional): Тип результата XPath.

**Возвращает**:
- `array`: Массив, содержащий результаты XPath.

**Вызывает исключения**:
- `Error`: Если `resultType` недействительный.

### `makeResolver`

**Описание**: Создает преобразователь пространства имен из объекта, строки JSON или функции.

**Параметры**:
- `obj` (object | string | function): Преобразователь пространства имен.

**Возвращает**:
- `function | null`: Функция преобразователя или `null`.

**Вызывает исключения**:
- `Error`: Если входные данные не являются корректным объектом, JSON или функцией.
- `Error`: Если JSON не парсится.
- `Error`: Если преобразователь не является допустимым словарем.

### `isValidDict`

**Описание**: Проверяет, является ли объект допустимым словарем (все значения являются строками).

**Параметры**:
- `obj` (object): Объект для проверки.

**Возвращает**:
- `boolean`: `true`, если объект является допустимым словарем, `false` в противном случае.

### `objToMap`

**Описание**: Преобразует объект в Map.

**Параметры**:
- `obj` (object): Объект для преобразования.

**Возвращает**:
- `Map`: Map, созданный из объекта.

### `isDocOrElem`

**Описание**: Проверяет, является ли объект `Document` или `Element`.

**Параметры**:
- `obj` (object): Объект для проверки.

**Возвращает**:
- `boolean`: `true`, если объект является `Document` или `Element`, `false` в противном случае.

### `listToArr`

**Описание**: Преобразует `NodeList` в массив.

**Параметры**:
- `list` (NodeList): `NodeList` для преобразования.

**Возвращает**:
- `array`: Массив элементов из `NodeList`.

### `getItemDetail`

**Описание**: Возвращает детали элемента в виде объекта.

**Параметры**:
- `item` (any): Элемент для получения деталей.

**Возвращает**:
- `object`: Объект, содержащий детали элемента, включая тип, имя, значение и `textContent`.

### `getItemDetails`

**Описание**: Возвращает массив деталей для списка элементов.

**Параметры**:
- `items` (array): Массив элементов.

**Возвращает**:
- `array`: Массив объектов деталей элементов.

### `getNodeTypeStr`

**Описание**: Возвращает строковое представление типа узла.

**Параметры**:
- `nodeType` (number): Тип узла.

**Возвращает**:
- `string`: Строковое представление типа узла.

### `getxpathResultStr`

**Описание**: Возвращает строковое представление типа результата XPath.

**Параметры**:
- `resultType` (number): Тип результата XPath.

**Возвращает**:
- `string`: Строковое представление типа результата XPath.

### `getxpathResultNum`

**Описание**: Возвращает числовое представление типа результата XPath.

**Параметры**:
- `resultTypeStr` (string): Строковое представление типа результата XPath.

**Возвращает**:
- `number`: Числовое представление типа результата XPath или `NaN`.

### `isAttrItem`

**Описание**: Проверяет, является ли объект атрибутом (Attr).

**Параметры**:
- `item` (any): Объект для проверки.

**Возвращает**:
- `boolean`: `true`, если объект является атрибутом, `false` в противном случае.

### `isNodeItem`

**Описание**: Проверяет, является ли объект узлом (не атрибутом, строкой или числом).

**Параметры**:
- `item` (any): Объект для проверки.

**Возвращает**:
- `boolean`: `true`, если объект является узлом, `false` в противном случае.

### `isElementItem`

**Описание**: Проверяет, является ли объект элементом.

**Параметры**:
- `item` (any): Объект для проверки.

**Возвращает**:
- `boolean`: `true`, если объект является элементом, `false` в противном случае.

### `addClassToItem`

**Описание**: Добавляет класс к элементу.

**Параметры**:
- `clas` (string): Имя класса.
- `item` (Node): Элемент, к которому нужно добавить класс.

**Возвращает**:
- `void`

### `addClassToItems`

**Описание**: Добавляет класс ко всем элементам массива.

**Параметры**:
- `clas` (string): Имя класса.
- `items` (array): Массив элементов.

**Возвращает**:
- `void`

### `saveItemClass`

**Описание**: Сохраняет текущее значение атрибута class элемента.

**Параметры**:
- `item` (Node): Элемент для сохранения класса.

**Возвращает**:
- `object | null`: Объект с элементом и исходным классом или `null`, если элемент не является элементом.

### `restoreItemClass`

**Описание**: Восстанавливает сохраненное значение атрибута class элемента.

**Параметры**:
- `savedClass` (object): Объект, возвращенный функцией `saveItemClass`.

**Возвращает**:
 -`null | void`: Возвращает null если savedClass null иначе void.

### `saveItemClasses`

**Описание**: Сохраняет классы для всех элементов массива.

**Параметры**:
- `items` (array): Массив элементов.

**Возвращает**:
- `array`: Массив сохраненных объектов классов.

### `restoreItemClasses`

**Описание**: Восстанавливает классы для всех сохраненных элементов.

**Параметры**:
- `savedClasses` (array): Массив сохраненных объектов классов.

**Возвращает**:
- `void`

### `setAttrToItem`

**Описание**: Устанавливает атрибут для элемента.

**Параметры**:
- `name` (string): Имя атрибута.
- `value` (string): Значение атрибута.
- `item` (Node): Элемент, которому нужно установить атрибут.

**Возвращает**:
- `void`

### `removeAttrFromItem`

**Описание**: Удаляет атрибут у элемента.

**Параметры**:
- `name` (string): Имя атрибута.
- `item` (Node): Элемент, у которого нужно удалить атрибут.

**Возвращает**:
- `void`

### `removeAttrFromItems`

**Описание**: Удаляет атрибут у всех элементов массива.

**Параметры**:
- `name` (string): Имя атрибута.
- `items` (array): Массив элементов.

**Возвращает**:
- `void`

### `setIndexToItems`

**Описание**: Устанавливает атрибут индекса для всех элементов массива.

**Параметры**:
- `name` (string): Имя атрибута.
- `items` (array): Массив элементов.

**Возвращает**:
- `void`

### `getParentElement`

**Описание**: Возвращает родительский элемент элемента или атрибута.

**Параметры**:
- `item` (any): Элемент или атрибут.

**Возвращает**:
- `Element | null`: Родительский элемент или `null`.

### `getAncestorElements`

**Описание**: Возвращает массив всех родительских элементов для заданного элемента.

**Параметры**:
- `elem` (Element): Элемент для получения предков.

**Возвращает**:
- `array`: Массив родительских элементов.

### `getOwnerDocument`

**Описание**: Возвращает документ, которому принадлежит элемент или атрибут.

**Параметры**:
- `item` (any): Элемент или атрибут.

**Возвращает**:
- `Document | null`: Документ или `null`.

### `createHeaderRow`

**Описание**: Создает строку заголовка таблицы.

**Параметры**:
- `values` (array): Массив значений для ячеек заголовка.
- `opts` (object, optional): Опции, такие как `document`.

**Возвращает**:
- `HTMLTableRowElement`: Строка заголовка.

### `createDetailTableHeader`

**Описание**: Создает строку заголовка таблицы деталей.

**Параметры**:
- `opts` (object, optional): Опции, такие как `document`.

**Возвращает**:
- `HTMLTableRowElement`: Строка заголовка таблицы деталей.

### `createDetailRow`

**Описание**: Создает строку с деталями элемента.

**Параметры**:
- `index` (number): Индекс элемента.
- `detail` (object): Объект с деталями элемента.
- `opts` (object, optional): Опции, такие как `document` и `keys`.

**Возвращает**:
- `HTMLTableRowElement`: Строка с деталями элемента.

### `appendDetailRows`

**Описание**: Добавляет строки деталей в таблицу частями.

**Параметры**:
- `parent` (HTMLElement): Родительский элемент таблицы.
- `details` (array): Массив деталей элементов.
- `opts` (object, optional): Опции, такие как `chunkSize`, `begin`, `end`, `createRow` и `detailKeys`.

**Возвращает**:
- `Promise<void>`: Промис, выполняющийся после добавления всех строк.

### `updateDetailsTable`

**Описание**: Обновляет таблицу деталей элементов.

**Параметры**:
- `parent` (HTMLElement): Родительский элемент таблицы.
- `details` (array): Массив деталей элементов.
- `opts` (object, optional): Опции, такие как `chunkSize`, `begin`, `end` и `headerValues`.

**Возвращает**:
- `Promise<void>`: Промис, выполняющийся после обновления таблицы.

### `emptyChildNodes`

**Описание**: Удаляет все дочерние узлы элемента.

**Параметры**:
- `elem` (HTMLElement): Элемент, дочерние узлы которого нужно удалить.

**Возвращает**:
- `void`

### `saveAttrForItem`

**Описание**: Сохраняет значение атрибута элемента в хранилище.

**Параметры**:
- `item` (Element): Элемент.
- `attr` (string): Имя атрибута.
- `storage` (Map, optional): Хранилище атрибутов.
- `overwrite` (boolean, optional): Флаг перезаписи существующего атрибута.

**Возвращает**:
- `Map`: Хранилище атрибутов.

### `saveAttrForItems`

**Описание**: Сохраняет значения атрибутов элементов в хранилище.

**Параметры**:
- `items` (array): Массив элементов.
- `attr` (string): Имя атрибута.
- `storage` (Map, optional): Хранилище атрибутов.
- `overwrite` (boolean, optional): Флаг перезаписи существующего атрибута.

**Возвращает**:
- `Map`: Хранилище атрибутов.

### `restoreItemAttrs`

**Описание**: Восстанавливает атрибуты элементов из хранилища.

**Параметры**:
- `storage` (Map): Хранилище атрибутов.

**Возвращает**:
- `void`

### `getFrameAncestry`

**Описание**: Возвращает массив фреймов-предков для заданных индексов.

**Параметры**:
- `inds` (array): Массив индексов фреймов.
- `win` (Window, optional): Начальное окно.

**Возвращает**:
- `array`: Массив фреймов-предков.

**Вызывает исключения**:
- `Error`: Если указанный фрейм не существует.
- `Error`: Если доступ к фрейму запрещен.

### `isNumberArray`

**Описание**: Проверяет, является ли массив массивом чисел.

**Параметры**:
- `arr` (array): Массив для проверки.

**Возвращает**:
- `boolean`: `true`, если массив является массивом чисел, `false` в противном случае.

### `onError`

**Описание**: Обработчик ошибок (в текущей реализации не делает ничего).

**Параметры**:
- `err` (any): Объект ошибки.

**Возвращает**:
- `void`

### `isBlankWindow`

**Описание**: Проверяет, является ли окно пустым окном (about:blank).

**Параметры**:
- `win` (Window): Окно для проверки.

**Возвращает**:
- `boolean`: `true`, если окно пустое, `false` в противном случае.

### `collectBlankWindows`

**Описание**: Собирает пустые окна (about:blank) из всех фреймов.

**Параметры**:
- `top` (Window): Верхнее окно.

**Возвращает**:
- `array`: Массив пустых окон.

### `findFrameElement`

**Описание**: Находит элемент `iframe` для заданного окна.

**Параметры**:
- `win` (Window): Окно.
- `parent` (Window): Родительское окно.

**Возвращает**:
- `HTMLIFrameElement | null`: Элемент `iframe` или `null`.

### `findFrameIndex`

**Описание**: Находит индекс фрейма в родительском окне.

**Параметры**:
- `win` (Window): Окно.
- `parent` (Window): Родительское окно.

**Возвращает**:
- `number`: Индекс фрейма или `-1`.

### `makeDetailText`

**Описание**: Создает текстовую строку из объекта детали.

**Параметры**:
- `detail` (object): Объект детали.
- `keys` (array): Массив ключей для извлечения значений.
- `separator` (string, optional): Разделитель между значениями. По умолчанию `,`.
- `replacers` (object, optional): Объект с функциями для замены значений.

**Возвращает**:
- `string`: Текстовая строка, созданная из объекта детали.