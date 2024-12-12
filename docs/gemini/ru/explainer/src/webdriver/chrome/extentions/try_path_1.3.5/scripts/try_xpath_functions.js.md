## АНАЛИЗ КОДА

### 1. <алгоритм>

**Общая идея:** Код предоставляет набор функций для работы с DOM (Document Object Model) и выполнения XPath-запросов в веб-браузере.

**Пошаговая блок-схема:**

1. **Инициализация:**
   - Проверяет существование пространства имен `tryxpath`. Если его нет, то создается.
   - Проверяет существование пространства имен `tryxpath.functions`. Если его нет, то создается.
   - Определяет псевдонимы `tx` и `fu` для `tryxpath` и `tryxpath.functions` соответственно.
   - Проверяет, не был ли код выполнен ранее (через `fu.done`). Если да, то выход.
   - Устанавливает `fu.done` в `true`, чтобы избежать повторного выполнения.

2. **`fu.execExpr(expr, method, opts)`:**
   - **Входные данные:** XPath-выражение (`expr`), метод выполнения (`method`), и объект опций (`opts`).
   - **Опции:**  контекстный узел (`context`), пользовательский резолвер (`resolver`), документ (`document`), тип результата (`resultType`).
   - **Логика:**
        -   Определяет контекст, резолвер и документ на основе входных `opts`.
        -   В зависимости от `method`:
            -   **`evaluate`**:
                -   Проверяет тип контекста (должен быть `Node` или `Attr`).
                -   Создает резолвер при помощи `fu.makeResolver(resolver)`.
                -   Выполняет XPath-выражение с помощью `doc.evaluate()`.
                -   Конвертирует результат в массив при помощи `fu.resToArr()`.
            -   **`querySelector`**:
                -   Проверяет тип контекста (должен быть `Document` или `Element`).
                -   Выполняет CSS-селектор при помощи `context.querySelector()`.
                -   Преобразует результат в массив.
            -   **`querySelectorAll` (default)**:
                -   Проверяет тип контекста (должен быть `Document` или `Element`).
                -   Выполняет CSS-селектор при помощи `context.querySelectorAll()`.
                -   Преобразует результат в массив с помощью `fu.listToArr()`.
        -   Возвращает объект с массивом найденных элементов `items`, методом выполнения `method` и типом результата `resultType`.
   - **Примеры:**
       - `fu.execExpr("//div[@id='test']", "evaluate", {context: document.body})`
       - `fu.execExpr(".my-class", "querySelector", {context: document})`
       - `fu.execExpr("div", "querySelectorAll", {context: document})`

3. **`fu.resToArr(res, type)`:**
   - **Входные данные:** результат XPath-запроса (`res`), тип результата (`type`).
   - **Логика:**
        -   Определяет `type`, если тип не указан, использует `res.resultType`.
        -   Конвертирует `res` в массив `arr` в зависимости от `type`:
            -   `NUMBER_TYPE`: Добавляет `res.numberValue` в массив.
            -   `STRING_TYPE`: Добавляет `res.stringValue` в массив.
            -   `BOOLEAN_TYPE`: Добавляет `res.booleanValue` в массив.
            -   `ORDERED_NODE_ITERATOR_TYPE` или `UNORDERED_NODE_ITERATOR_TYPE`: Итерирует по узлам с помощью `res.iterateNext()` и добавляет их в массив.
            -   `ORDERED_NODE_SNAPSHOT_TYPE` или `UNORDERED_NODE_SNAPSHOT_TYPE`: Итерирует по узлам с помощью `res.snapshotItem(i)` и добавляет их в массив.
            -   `ANY_UNORDERED_NODE_TYPE` или `FIRST_ORDERED_NODE_TYPE`: Добавляет `res.singleNodeValue` в массив.
   - **Примеры:**
       - `fu.resToArr(result, xpathResult.NUMBER_TYPE)`

4. **`fu.makeResolver(obj)`:**
    -   **Входные данные:** `obj`, который может быть `null`, функцией, строкой JSON или словарем.
    -   **Логика:**
        -   Если `obj` это `null`, возвращается `null`.
        -   Если `obj` это функция, она возвращается как есть.
        -   Если `obj` это строка, то она парсится как JSON.
        -   Если `obj` это объект, то проверяется `fu.isValidDict(dict)`, если валидный, то преобразуется `obj` к `Map` при помощи `fu.objToMap()`. Возвращает функцию, которая ищет namespace для XPath.
    -   **Примеры:**
        -   `fu.makeResolver(null)`
        -   `fu.makeResolver(myResolverFunction)`
        -   `fu.makeResolver('{"ns":"http://example.com"}')`
        -   `fu.makeResolver({"ns": "http://example.com"})`
5. **`fu.isValidDict(obj)`:**
    -   **Входные данные:** `obj`.
    -   **Логика:**
        -   Проверяет, является ли `obj` не `null`, и объектом.
        -   Проверяет, являются ли все значения `obj` строками.
    -   **Примеры:**
        -   `fu.isValidDict(null)` => `false`
        -   `fu.isValidDict({a: 1})` => `false`
        -   `fu.isValidDict({a: "1"})` => `true`

6. **`fu.objToMap(obj)`:**
   - **Входные данные:** объект `obj`.
   - **Логика:**
        -   Преобразует объект в `Map`.
   - **Примеры:**
       - `fu.objToMap({a: 1, b: 2})`

7.  **`fu.isDocOrElem(obj)`:**
    - **Входные данные:** `obj`.
    - **Логика:**
        -   Проверяет, является ли `obj` документом (`nodeType === 9`) или элементом (`nodeType === 1`).
    - **Примеры:**
        - `fu.isDocOrElem(document)` => `true`
        - `fu.isDocOrElem(document.body)` => `true`
        - `fu.isDocOrElem(null)` => `false`
8.  **`fu.listToArr(list)`:**
    - **Входные данные:** `list`.
    - **Логика:**
        -   Преобразует `list` в массив.
    - **Примеры:**
        - `fu.listToArr(document.querySelectorAll("div"))`

9.  **`fu.getItemDetail(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Возвращает объект с детальной информацией об `item`: `type`, `name`, `value`, `textContent`.
        -   Определяет тип: string, number, boolean, node, attr.
        -   Если `item` является строкой, числом или булевым значением, создает соответствующий объект.
        -   Если `item` является элементом, создает объект с деталями элемента.
        -   Если `item` является атрибутом, создает объект с деталями атрибута.
        -   Если `item` является узлом, создает объект с деталями узла.
    - **Примеры:**
        - `fu.getItemDetail("test")`
        - `fu.getItemDetail(123)`
        - `fu.getItemDetail(true)`
        - `fu.getItemDetail(document.body)`
        - `fu.getItemDetail(document.body.attributes[0])`
10. **`fu.getItemDetails(items)`:**
    - **Входные данные:** массив `items`.
    - **Логика:**
        -   Создает массив `details`, и для каждого элемента `items` получает детали при помощи `fu.getItemDetail()` и добавляет в массив.
    - **Примеры:**
        - `fu.getItemDetails([document.body, document.body.firstChild])`
11. **`fu.getNodeTypeStr(nodeType)`:**
    - **Входные данные:** `nodeType`.
    - **Логика:**
        -   Возвращает строковое представление типа узла на основе `nodeType`.
        -   Использует `nodeTypeMap` для поиска.
    - **Примеры:**
        - `fu.getNodeTypeStr(Node.ELEMENT_NODE)`
12. **`fu.getxpathResultStr(resultType)`:**
    - **Входные данные:** `resultType`.
    - **Логика:**
        -   Возвращает строковое представление XPath result type.
        -   Использует `xpathResultMaps.numToStr` для поиска.
    - **Примеры:**
        - `fu.getxpathResultStr(xpathResult.NUMBER_TYPE)`
13. **`fu.getxpathResultNum(resultTypeStr)`:**
    - **Входные данные:** `resultTypeStr`.
    - **Логика:**
        -   Возвращает числовое представление XPath result type.
        -   Использует `xpathResultMaps.strToNum` для поиска.
    - **Примеры:**
        - `fu.getxpathResultNum("NUMBER_TYPE")`
14. **`fu.isAttrItem(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Проверяет, является ли `item` атрибутом.
        -   Использует `Object.prototype.toString.call(item)`.
    - **Примеры:**
        - `fu.isAttrItem(document.body.attributes[0])`
15. **`fu.isNodeItem(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Проверяет, является ли `item` узлом (не атрибутом, не строкой, не числом).
    - **Примеры:**
        - `fu.isNodeItem(document.body)`
        - `fu.isNodeItem("test")`
16. **`fu.isElementItem(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Проверяет, является ли `item` элементом (узел с `nodeType === Node.ELEMENT_NODE`).
    - **Примеры:**
        - `fu.isElementItem(document.body)`
17. **`fu.addClassToItem(clas, item)`:**
    - **Входные данные:** `clas` и `item`.
    - **Логика:**
        -   Добавляет класс `clas` к элементу `item` (если `item` является элементом).
    - **Примеры:**
        - `fu.addClassToItem("test-class", document.body)`
18. **`fu.addClassToItems(clas, items)`:**
    - **Входные данные:** `clas` и массив `items`.
    - **Логика:**
        -   Добавляет класс `clas` ко всем элементам в массиве `items`.
    - **Примеры:**
        - `fu.addClassToItems("test-class", [document.body, document.body.firstChild])`
19. **`fu.saveItemClass(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Сохраняет оригинальный класс элемента `item`.
        -   Возвращает объект с элементом и оригинальным классом.
    - **Примеры:**
        - `fu.saveItemClass(document.body)`
20. **`fu.restoreItemClass(savedClass)`:**
    - **Входные данные:** `savedClass`.
    - **Логика:**
        -   Восстанавливает оригинальный класс элемента.
    - **Примеры:**
        - `fu.restoreItemClass(fu.saveItemClass(document.body))`
21. **`fu.saveItemClasses(items)`:**
    - **Входные данные:** массив `items`.
    - **Логика:**
        -   Сохраняет оригинальные классы всех элементов в `items`.
    - **Примеры:**
        - `fu.saveItemClasses([document.body, document.body.firstChild])`
22. **`fu.restoreItemClasses(savedClasses)`:**
    - **Входные данные:** массив `savedClasses`.
    - **Логика:**
        -   Восстанавливает оригинальные классы для всех сохраненных элементов.
    - **Примеры:**
        - `fu.restoreItemClasses(fu.saveItemClasses([document.body, document.body.firstChild]))`
23. **`fu.setAttrToItem(name, value, item)`:**
    - **Входные данные:** имя атрибута `name`, значение атрибута `value` и элемент `item`.
    - **Логика:**
        -   Устанавливает атрибут `name` со значением `value` для элемента `item`.
    - **Примеры:**
        - `fu.setAttrToItem("data-test", "123", document.body)`
24. **`fu.removeAttrFromItem(name, item)`:**
    - **Входные данные:** имя атрибута `name` и элемент `item`.
    - **Логика:**
        -   Удаляет атрибут `name` из элемента `item`.
    - **Примеры:**
        - `fu.removeAttrFromItem("data-test", document.body)`
25. **`fu.removeAttrFromItems(name, items)`:**
    - **Входные данные:** имя атрибута `name` и массив элементов `items`.
    - **Логика:**
        -   Удаляет атрибут `name` из каждого элемента в `items`.
    - **Примеры:**
        - `fu.removeAttrFromItems("data-test", [document.body, document.body.firstChild])`
26. **`fu.setIndexToItems(name, items)`:**
    - **Входные данные:** имя атрибута `name` и массив элементов `items`.
    - **Логика:**
        -   Устанавливает атрибут `name` со значением индекса для каждого элемента в `items`.
    - **Примеры:**
        - `fu.setIndexToItems("data-index", [document.body, document.body.firstChild])`
27. **`fu.getParentElement(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Возвращает родительский элемент для `item` (если `item` является атрибутом или узлом).
        -   Для атрибутов возвращает `item.ownerElement`.
        -   Для узлов возвращает `item.parentElement` или `item.parentNode` (если это элемент).
    - **Примеры:**
        - `fu.getParentElement(document.body.firstChild)`
        - `fu.getParentElement(document.body.attributes[0])`
28. **`fu.getAncestorElements(elem)`:**
    - **Входные данные:** элемент `elem`.
    - **Логика:**
        -   Возвращает массив всех родительских элементов `elem` до `document`.
        -   Итерирует по `parentElement`, а потом `parentNode`.
    - **Примеры:**
        - `fu.getAncestorElements(document.body.firstChild)`
29. **`fu.getOwnerDocument(item)`:**
    - **Входные данные:** `item`.
    - **Логика:**
        -   Возвращает документ, которому принадлежит `item`.
        -   Для атрибутов возвращает `item.ownerElement.ownerDocument` или `item.ownerDocument`.
        -   Для узлов возвращает `item.ownerDocument`.
    - **Примеры:**
        - `fu.getOwnerDocument(document.body.firstChild)`
        - `fu.getOwnerDocument(document.body.attributes[0])`
30. **`fu.createHeaderRow(values, opts)`:**
    - **Входные данные:** массив значений `values`, опции `opts`.
    - **Логика:**
        -   Создает `<tr>` с заголовками `<th>` из массива `values`.
        -   Использует документ из `opts.document` или `document` по умолчанию.
    - **Примеры:**
        - `fu.createHeaderRow(["Name", "Value"])`
31. **`fu.createDetailTableHeader(opts)`:**
    - **Входные данные:** опции `opts`.
    - **Логика:**
        -   Создает `<tr>` с предопределенными заголовками для таблицы деталей.
        -   Использует документ из `opts.document` или `document` по умолчанию.
    - **Примеры:**
        - `fu.createDetailTableHeader()`
32. **`fu.createDetailRow(index, detail, opts)`:**
    - **Входные данные:** `index`, объект с деталями `detail`, опции `opts`.
    - **Логика:**
        -   Создает `<tr>` с данными детализации.
        -   Добавляет индекс, значения из `detail` по ключам из `opts.keys`, и кнопку "Focus".
        -   Использует документ из `opts.document` или `document` по умолчанию.
    - **Примеры:**
        - `fu.createDetailRow(0, {type: "String", name: "test", value: "test-value"})`
33. **`fu.appendDetailRows(parent, details, opts)`:**
    - **Входные данные:** родительский элемент `parent`, массив деталей `details`, опции `opts`.
    - **Логика:**
        -   Добавляет строки детализации в `parent` с использованием document fragment.
        -   Разбивает добавление на чанки (с использованием `chunkSize` из `opts`), чтобы избежать блокировки UI.
        -   Использует рекурсию для обработки всех деталей.
        -   Использует `opts.createRow` для создания строки.
    - **Примеры:**
        - `fu.appendDetailRows(tableBody, [{}, {}])`
34. **`fu.updateDetailsTable(parent, details, opts)`:**
    - **Входные данные:** родительский элемент `parent`, массив деталей `details`, опции `opts`.
    - **Логика:**
        -   Очищает `parent`, добавляет строку заголовков, и добавляет строки деталей.
        -   Использует `fu.createHeaderRow`, `fu.appendDetailRows`, `fu.emptyChildNodes`.
    - **Примеры:**
        - `fu.updateDetailsTable(tableBody, [{}, {}])`
35. **`fu.emptyChildNodes(elem)`:**
    - **Входные данные:** элемент `elem`.
    - **Логика:**
        -   Удаляет все дочерние узлы элемента `elem`.
    - **Примеры:**
        - `fu.emptyChildNodes(document.body)`
36. **`fu.saveAttrForItem(item, attr, storage, overwrite)`:**
    - **Входные данные:** элемент `item`, имя атрибута `attr`, хранилище `storage`, флаг перезаписи `overwrite`.
    - **Логика:**
        -   Сохраняет значение атрибута `attr` элемента `item` в `storage`.
    - **Примеры:**
        - `fu.saveAttrForItem(document.body, "data-test", new Map())`
37. **`fu.saveAttrForItems(items, attr, storage, overwrite)`:**
    - **Входные данные:** массив элементов `items`, имя атрибута `attr`, хранилище `storage`, флаг перезаписи `overwrite`.
    - **Логика:**
        -   Сохраняет значения атрибута `attr` всех элементов из `items` в `storage`.
    - **Примеры:**
        - `fu.saveAttrForItems([document.body, document.body.firstChild], "data-test", new Map())`
38. **`fu.restoreItemAttrs(storage)`:**
    - **Входные данные:** хранилище `storage`.
    - **Логика:**
        -   Восстанавливает значения атрибутов элементов из `storage`.
    - **Примеры:**
        - `fu.restoreItemAttrs(fu.saveAttrForItems([document.body], "data-test", new Map()))`
39. **`fu.getFrameAncestry(inds, win)`:**
    - **Входные данные:** массив индексов фреймов `inds`, окно `win`.
    - **Логика:**
        -   Возвращает массив фреймов-предков на основе массива индексов `inds` из окна `win`.
    - **Примеры:**
        - `fu.getFrameAncestry([0, 1])`
40. **`fu.isNumberArray(arr)`:**
    - **Входные данные:** массив `arr`.
    - **Логика:**
        -   Проверяет, является ли `arr` массивом чисел.
    - **Примеры:**
        - `fu.isNumberArray([1, 2, 3])`
41. **`fu.onError(err)`:**
    - **Входные данные:** ошибка `err`.
    - **Логика:**
        -   Обработчик ошибок.
    - **Примеры:**
        - `fu.onError(new Error("test"))`
42. **`fu.isBlankWindow(win)`:**
    - **Входные данные:** окно `win`.
    - **Логика:**
        -   Проверяет, является ли окно `win` пустым (about:blank).
    - **Примеры:**
        - `fu.isBlankWindow(window.open("about:blank"))`
43. **`fu.collectBlankWindows(top)`:**
    - **Входные данные:** окно `top`.
    - **Логика:**
        -   Собирает все пустые окна из окна `top` (рекурсивно).
    - **Примеры:**
        - `fu.collectBlankWindows(window)`
44. **`fu.findFrameElement(win, parent)`:**
    - **Входные данные:** окно `win`, родительский элемент `parent`.
    - **Логика:**
        -   Ищет фрейм-элемент по окну `win` в `parent`.
    - **Примеры:**
        - `fu.findFrameElement(window.frames[0], document.body)`
45. **`fu.findFrameIndex(win, parent)`:**
    - **Входные данные:** окно `win`, родительский элемент `parent`.
    - **Логика:**
        -   Ищет индекс фрейма по окну `win` в `parent`.
    - **Примеры:**
        - `fu.findFrameIndex(window.frames[0], window)`
46. **`fu.makeDetailText(detail, keys, separator, replacers)`:**
    - **Входные данные:** объект `detail`, массив ключей `keys`, разделитель `separator`, объект замены `replacers`.
    - **Логика:**
        -   Создает строку из значений объекта `detail` по ключам из массива `keys` с разделителем `separator`.
        -   Использует объект `replacers` для замены значений.
    - **Примеры:**
        - `fu.makeDetailText({a: 1, b: 2}, ["a", "b"], "-")`
        - `fu.makeDetailText({a: "test", b: 2}, ["a", "b"], "-", {a: function(val) { return val.toUpperCase(); }})`

### 2. <mermaid>
```mermaid
graph TD
    subgraph tryxpath
        Start(Start) --> InitNamespace[Initialize tryxpath and tryxpath.functions Namespaces]
        InitNamespace --> CheckDone{fu.done?}
        CheckDone -- Yes --> End(End)
        CheckDone -- No --> SetDone[fu.done = true]
        SetDone --> execExprCall[Call fu.execExpr()]
        execExprCall --> execExpr(fu.execExpr)
        execExpr --> DetermineMethod{method}
        DetermineMethod -- "evaluate" --> EvaluateMethod[XPath Evaluation]
        EvaluateMethod --> CheckContextType1{isNodeItem or isAttrItem?}
        CheckContextType1 -- No --> ErrorContext1[Throw Error: Context should be Node or Attr]
        CheckContextType1 -- Yes --> MakeResolver[fu.makeResolver(resolver)]
        MakeResolver -->  Evaluate[doc.evaluate(expr, context, resolver, resultType, null)]
        Evaluate --> ResToArr[fu.resToArr(result, resultType)]
        DetermineMethod -- "querySelector" --> QuerySelectorMethod[CSS querySelector]
        QuerySelectorMethod --> CheckContextType2{isDocOrElem?}
        CheckContextType2 -- No --> ErrorContext2[Throw Error: Context should be Document or Element]
        CheckContextType2 -- Yes --> QuerySelector[context.querySelector(expr)]
        QuerySelector --> ResultToArray1[elem ? [elem] : []]
        DetermineMethod -- "querySelectorAll" --> QuerySelectorAllMethod[CSS querySelectorAll]
        QuerySelectorAllMethod --> CheckContextType3{isDocOrElem?}
        CheckContextType3 -- No --> ErrorContext3[Throw Error: Context should be Document or Element]
        CheckContextType3 -- Yes --> QuerySelectorAll[context.querySelectorAll(expr)]
         QuerySelectorAll --> ListToArr[fu.listToArr(elems)]
        ResToArr --> ReturnResult[Return {"items", "method", "resultType"}]
        ResultToArray1 --> ReturnResult
        ListToArr --> ReturnResult
        ReturnResult --> End
        
        execExpr --> ReturnResult
        
        MakeResolver -->  makeResolver(fu.makeResolver)
       makeResolver --> CheckResolverType{typeof(obj)?}
       CheckResolverType -- "null" --> ReturnNull[return null]
       CheckResolverType -- "function" --> ReturnFunction[return obj]
       CheckResolverType -- "string" --> ParseJSON[JSON.parse(obj)]
       ParseJSON -- success --> ValidDict{isValidDict(dict)?}
       ParseJSON -- error --> ErrorResolver[Throw Error: Invalid resolver]
       CheckResolverType -- "object" --> ValidDict
       ValidDict -- Yes --> ObjToMapCall[Call fu.objToMap(dict)]
       ObjToMapCall --> objToMap(fu.objToMap)
        objToMap --> CreateMap[Create new Map]
        CreateMap --> IterateKeys[Iterate over obj keys]
        IterateKeys --> SetMap[map.set(item, obj[item])]
        SetMap --> CheckNextKey[Check next key]
        CheckNextKey -- Yes --> IterateKeys
         CheckNextKey -- No --> ReturnMap[Return map]
        ReturnMap -->  makeResolverReturnFunction[Return function(str){}]
       ValidDict -- No --> ErrorResolver2[Throw Error: Invalid resolver]
       ReturnFunction --> makeResolverReturnFunction
        ReturnNull --> makeResolverReturnFunction
       makeResolverReturnFunction --> End
        
        ResToArr --> resToArr(fu.resToArr)
        resToArr --> DetermineResultType{type}
        DetermineResultType --> NumberTypeCase[xpathResult.NUMBER_TYPE]
        NumberTypeCase --> AddNumberValueToArray[arr.push(res.numberValue)]
        DetermineResultType --> StringTypeCase[xpathResult.STRING_TYPE]
         StringTypeCase --> AddStringValueToArray[arr.push(res.stringValue)]
        DetermineResultType --> BooleanTypeCase[xpathResult.BOOLEAN_TYPE]
         BooleanTypeCase --> AddBooleanValueToArray[arr.push(res.booleanValue)]
        DetermineResultType --> IteratorTypeCase1[xpathResult.ORDERED_NODE_ITERATOR_TYPE]
        DetermineResultType --> IteratorTypeCase2[xpathResult.UNORDERED_NODE_ITERATOR_TYPE]
         IteratorTypeCase1 --> IteratorLoopStart[node = res.iterateNext()]
          IteratorTypeCase2 --> IteratorLoopStart
        IteratorLoopStart --> CheckNodeNull{node !== null?}
        CheckNodeNull -- No --> ReturnArray1[Return arr]
        CheckNodeNull -- Yes --> AddNodeToArray[arr.push(node)]
        AddNodeToArray --> IteratorLoopStart
        DetermineResultType --> SnapshotTypeCase1[xpathResult.ORDERED_NODE_SNAPSHOT_TYPE]
        DetermineResultType --> SnapshotTypeCase2[xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE]
         SnapshotTypeCase1 --> SnapshotLoopStart[for (i = 0; i < res.snapshotLength; i++)]
        SnapshotTypeCase2 --> SnapshotLoopStart
        SnapshotLoopStart --> AddSnapshotToArray[arr.push(res.snapshotItem(i))]
         AddSnapshotToArray --> CheckNextItem[Check next item]
         CheckNextItem -- Yes --> SnapshotLoopStart
        CheckNextItem -- No --> ReturnArray2[Return arr]
        DetermineResultType --> SingleNodeCase1[xpathResult.ANY_UNORDERED_NODE_TYPE]
         DetermineResultType --> SingleNodeCase2[xpathResult.FIRST_ORDERED_NODE_TYPE]
         SingleNodeCase1 --> AddSingleNodeToArray[arr.push(res.singleNodeValue)]
         SingleNodeCase2 --> AddSingleNodeToArray
        AddNumberValueToArray --> ReturnArray1
        AddStringValueToArray --> ReturnArray1
        AddBooleanValueToArray --> ReturnArray1
        AddSingleNodeToArray --> ReturnArray1
        ReturnArray1 --> End
        ReturnArray2 --> End
        
          
    end
    subgraph DOM
       
        ListToArr --> listToArr(fu.listToArr)
         listToArr --> CreateArray[var elems = []]
          CreateArray --> IterateList[for (i = 0; i < list.length; i++)]
          IterateList --> PushItemToArray[elems.push(list[i])]
          PushItemToArray --> CheckNextItem1[Check next item]
          CheckNextItem1 -- Yes --> IterateList
          CheckNextItem1 -- No --> ReturnArray3[return elems]
           ReturnArray3 --> End

    end
```
### 3. <объяснение>

**Импорты:**

-   В данном коде нет явных импортов, так как это код для браузерного окружения и использует глобальные объекты вроде `window`, `document`, `Node` и `xpathResult`.
-   Он работает в пространстве имен `tryxpath` и `tryxpath.functions`, определяя свои собственные функции и методы.

**Классы:**

-   В коде нет явных классов, но есть объект `fu` (псевдоним для `tryxpath.functions`), который фактически играет роль контейнера для функций, работающих как методы.
    - `fu`: Хранит все функции для работы с DOM и XPath. Функции, такие как `execExpr`, `resToArr`, `makeResolver`, `isDocOrElem`, и другие, предназначены для работы с DOM и выполнения XPath-запросов, а также манипуляции с элементами и их атрибутами.

**Функции:**

-   `fu.execExpr(expr, method, opts)`:
    -   **Аргументы**: `expr` (строка, XPath-выражение или CSS-селектор), `method` (строка, метод выполнения: `evaluate`, `querySelector`, `querySelectorAll`), `opts` (объект, опции).
    -   **Возвращаемое значение**: Объект с ключами `items` (массив найденных элементов), `method` и `resultType`.
    -   **Назначение**: Выполняет XPath-выражение или CSS-селектор и возвращает результат.
    -   **Пример**: `fu.execExpr("//div[@class='test']", "evaluate", { context: document.body });`.
-   `fu.resToArr(res, type)`:
    -   **Аргументы**: `res` (результат XPath-запроса), `type` (тип результата).
    -   **Возвращаемое значение**: Массив элементов/значений.
    -   **Назначение**: Преобразует результат XPath в массив.
    -   **Пример**: `fu.resToArr(xpathResult, xpathResult.NUMBER_TYPE)`.
-   `fu.makeResolver(obj)`:
    -   **Аргументы**: `obj` (объект резолвера или строка).
    -   **Возвращаемое значение**: Функция резолвера или `null`.
    -   **Назначение**: Создает функцию резолвера для XPath на основе переданного объекта.
    -   **Пример**: `fu.makeResolver({ 'ns': 'http://example.com' });`.
-   `fu.isValidDict(obj)`:
    -   **Аргументы**: `obj` (объект).
    -   **Возвращаемое значение**: Булево значение (является ли объект валидным словарем).
    -   **Назначение**: Проверяет, является ли объект валидным словарем для резолвера.
    -   **Пример**: `fu.isValidDict({ a: 'value' });`.
-   `fu.objToMap(obj)`:
    -   **Аргументы**: `obj` (объект).
    -   **Возвращаемое значение**: Объект `Map`.
    -   **Назначение**: Преобразует объект в `Map`.
    -   **Пример**: `fu.objToMap({ 'a': '1', 'b': '2' });`.
-  `fu.isDocOrElem(obj)`:
    -  **Аргументы**: `obj` (объект).
    -  **Возвращаемое значение**: Булево значение.
    -  **Назначение**: Проверяет, является ли `obj` документом или элементом.
    -  **Пример**: `fu.isDocOrElem(document.body)`
- `fu.listToArr(list)`:
    -  **Аргументы**: `list` (коллекция).
    -  **Возвращаемое значение**: Массив элементов.
    -  **Назначение**: Преобразует коллекцию в массив.
    -  **Пример**: `fu.listToArr(document.querySelectorAll("div"))`
-   `fu.getItemDetail(item)`:
    -   **Аргументы**: `item` (DOM-элемент или значение).
    -   **Возвращаемое значение**: Объект с деталями элемента.
    -   **Назначение**: Возвращает детальную информацию об элементе/значении (тип, имя, значение, текст).
    -   **Пример**: `fu.getItemDetail(document.body)`.
-   `fu.getItemDetails(items)`:
    -   **Аргументы**: `items`