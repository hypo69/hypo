## <алгоритм>

1.  **Инициализация:**
    *   Проверяется наличие глобального объекта `tryxpath`. Если его нет, он создается.
    *   Проверяется наличие пространства имен `tryxpath.functions`. Если его нет, оно создается.
    *   Создаются алиасы `tx` для `tryxpath` и `fu` для `tryxpath.functions`.
    *   Проверяется, была ли функция `tryxpath.functions` уже выполнена. Если да, выполнение прекращается.

2.  **`fu.execExpr(expr, method, opts)`:**
    *   **Вход:** XPath выражение `expr`, метод `method` (`evaluate`, `querySelector`, `querySelectorAll`) и объект опций `opts`.
    *   Устанавливается контекст поиска:
        *   Если в `opts` есть `context`, используется он. Иначе используется `document`.
        *   Извлекается `resolver` из `opts` или устанавливается в `null`.
        *   Определяется `doc` (документ) на основе `context`.
    *   **Выбор метода:**
        *   **`evaluate`**:
            *   Проверяется, является ли `context` узлом или атрибутом. Если нет, выбрасывается ошибка.
            *   Создается `resolver` с помощью `fu.makeResolver(resolver)`.
            *   Определяется тип результата (`resultType`) из `opts` или устанавливается в `xpathResult.ANY_TYPE`.
            *   Выполняется XPath запрос с помощью `doc.evaluate(expr, context, resolver, resultType, null)`.
            *   Результат конвертируется в массив с помощью `fu.resToArr(result, resultType)`.
            *   Если `resultType` был `xpathResult.ANY_TYPE`, он обновляется на фактический тип результата.
        *   **`querySelector`**:
            *   Проверяется, является ли `context` документом или элементом. Если нет, выбрасывается ошибка.
            *   Выполняется запрос с помощью `context.querySelector(expr)`.
            *   Результат (один элемент или `null`) конвертируется в массив.
            *   `resultType` устанавливается в `null`.
        *   **`querySelectorAll`** (или `default`):
            *   Проверяется, является ли `context` документом или элементом. Если нет, выбрасывается ошибка.
            *   Выполняется запрос с помощью `context.querySelectorAll(expr)`.
            *   Результат (NodeList) конвертируется в массив с помощью `fu.listToArr(elems)`.
            *   `resultType` устанавливается в `null`.
    *   **Возврат:** Объект с результатами: `{"items": items, "method": method, "resultType": resultType}`.

3.  **`fu.resToArr(res, type)`:**
    *   **Вход:** Результат XPath запроса `res` и тип результата `type`.
    *   Если `type` не определен или равен `xpathResult.ANY_TYPE`, он берется из `res.resultType`.
    *   Создается пустой массив `arr`.
    *   **Обработка результатов в зависимости от типа:**
        *   `NUMBER_TYPE`, `STRING_TYPE`, `BOOLEAN_TYPE`: Значение добавляется в `arr`.
        *   `ORDERED_NODE_ITERATOR_TYPE`, `UNORDERED_NODE_ITERATOR_TYPE`: Итерация по узлам, добавляя каждый в `arr`.
        *   `ORDERED_NODE_SNAPSHOT_TYPE`, `UNORDERED_NODE_SNAPSHOT_TYPE`: Итерация по snapshot узлам, добавляя каждый в `arr`.
        *   `ANY_UNORDERED_NODE_TYPE`, `FIRST_ORDERED_NODE_TYPE`: Первый узел добавляется в `arr`.
        *   Если тип не распознан, выбрасывается ошибка.
    *   **Возврат:** Массив с результатами `arr`.

4.  **`fu.makeResolver(obj)`:**
    *   **Вход:** Объект резолвера `obj`.
    *   Если `obj` равен `null`, возвращается `null`.
    *   Если `obj` является функцией, возвращается эта функция.
    *   Если `obj` является строкой, пытаемся преобразовать ее в JSON. Если не удается, выбрасывается ошибка.
    *   Если `obj` является объектом, используется напрямую.
    *   Проверяется валидность словаря с помощью `fu.isValidDict(dict)`.
    *   Преобразуем объект в `Map` с помощью `fu.objToMap(dict)`.
    *   Возвращается функция, которая проверяет наличие namespace в `Map`.
    *   Если резолвер не валиден, выбрасывается ошибка.

5.  **`fu.isValidDict(obj)`:**
    *   **Вход:** Объект `obj`.
    *   Проверяется, является ли `obj` объектом, и не `null`.
    *   Проверяется, являются ли все значения в объекте строками.
    *   **Возврат:** `true` если словарь валиден, иначе `false`.

6.  **`fu.objToMap(obj)`:**
    *   **Вход:** Объект `obj`.
    *   Создается `Map`.
    *   Итерируется по ключам `obj`, добавляя пары ключ-значение в `Map`.
    *   **Возврат:** `Map` с данными из `obj`.

7. **`fu.isDocOrElem(obj)`:**
    *   **Вход:** Объект `obj`.
    *   Проверяется, является ли `obj` элементом (nodeType === 1) или документом (nodeType === 9).
    *   **Возврат:** `true`, если является документом или элементом, иначе `false`.

8. **`fu.listToArr(list)`:**
    *   **Вход:** NodeList `list`.
    *   Создается пустой массив `elems`.
    *   Перебираются элементы из `list`, добавляя каждый в `elems`.
    *   **Возврат:** Массив `elems` с элементами из `list`.

9.  **`fu.getItemDetail(item)`:**
    *   **Вход:** Любой элемент `item` (строка, число, булево, узел, атрибут).
    *   Определяется тип `item`.
    *   **Обработка типа:**
        *   `string`, `number`, `boolean`: Возвращается объект с типом, значением (приведенным к строке) и пустыми `name` и `textContent`.
        *   **Если `item` - Element:** Возвращается объект с типом "Node", именем, пустым значением и `textContent` элемента.
        *   **Если `item` - Attr:** Возвращается объект с типом "Attr", именем атрибута, значением атрибута и пустым `textContent`.
        *   **Если `item` - Node:** Возвращается объект с типом "Node", именем узла, значением узла и `textContent` узла.
    *   **Возврат:** Объект с информацией о элементе.

10. **`fu.getItemDetails(items)`:**
    *   **Вход:** Массив элементов `items`.
    *   Создается пустой массив `details`.
    *   Перебираются элементы из `items`, добавляя результат `fu.getItemDetail()` для каждого элемента в `details`.
    *   **Возврат:** Массив объектов с детальной информацией `details`.

11. **`fu.getNodeTypeStr(nodeType)`:**
    *   **Вход:** Тип узла `nodeType`.
    *   Проверяет, есть ли `nodeType` в `nodeTypeMap`.
    *   **Возврат:** Строковое представление типа узла или "Unknown".

12. **`fu.getxpathResultStr(resultType)`:**
    *   **Вход:** Числовой тип результата XPath `resultType`.
    *   Проверяет, есть ли `resultType` в `xpathResultMaps.numToStr`.
    *   **Возврат:** Строковое представление типа результата или "Unknown".

13. **`fu.getxpathResultNum(resultTypeStr)`:**
    *   **Вход:** Строковое представление типа результата XPath `resultTypeStr`.
    *   Проверяет, есть ли `resultTypeStr` в `xpathResultMaps.strToNum`.
    *   **Возврат:** Числовой тип результата или `NaN`.

14. **`fu.isAttrItem(item)`:**
    *   **Вход:** Любой элемент `item`.
    *   Проверяется, является ли `item` атрибутом.
    *   **Возврат:** `true`, если является атрибутом, иначе `false`.

15. **`fu.isNodeItem(item)`:**
    *   **Вход:** Любой элемент `item`.
    *   Проверяется, не является ли `item` атрибутом.
    *   Проверяется, не является ли `item` строкой или числом.
    *   **Возврат:** `true`, если `item` является узлом, иначе `false`.

16. **`fu.isElementItem(item)`:**
     *   **Вход:** Любой элемент `item`.
     *   Проверяется, является ли `item` узлом и элементом.
     *   **Возврат:** `true` если является элементом, иначе `false`.

17. **`fu.addClassToItem(clas, item)`:**
    *   **Вход:** Имя класса `clas` и элемент `item`.
    *   Если `item` является элементом, добавляет класс `clas` к `item`.

18. **`fu.addClassToItems(clas, items)`:**
    *   **Вход:** Имя класса `clas` и массив элементов `items`.
    *   Перебираются элементы из `items`, добавляя класс `clas` к каждому.

19. **`fu.saveItemClass(item)`:**
    *   **Вход:** Элемент `item`.
    *   Если `item` не является элементом, возвращает `null`.
    *   Сохраняет класс `item`, если он есть, и возвращает объект с элементом и сохраненным классом.

20. **`fu.restoreItemClass(savedClass)`:**
    *   **Вход:** Объект с сохраненным классом `savedClass`.
    *   Если `savedClass` равен `null`, возвращает `null`.
    *   Восстанавливает класс у элемента. Если сохраненного класса нет, удаляет атрибут `class`.

21. **`fu.saveItemClasses(items)`:**
    *   **Вход:** Массив элементов `items`.
    *   Перебирает элементы из `items`, сохраняя класс каждого элемента, добавляя их в массив.
    *   **Возврат:** Массив объектов с сохраненными классами.

22. **`fu.restoreItemClasses(savedClasses)`:**
    *   **Вход:** Массив объектов с сохраненными классами `savedClasses`.
    *   Перебираются объекты из `savedClasses`, восстанавливая класс у каждого элемента.

23. **`fu.setAttrToItem(name, value, item)`:**
    *   **Вход:** Имя атрибута `name`, значение атрибута `value` и элемент `item`.
    *   Если `item` является элементом, устанавливает атрибут `name` со значением `value` к `item`.

24. **`fu.removeAttrFromItem(name, item)`:**
    *   **Вход:** Имя атрибута `name` и элемент `item`.
    *   Если `item` является элементом, удаляет атрибут `name` у `item`.

25. **`fu.removeAttrFromItems(name, items)`:**
     *   **Вход:** Имя атрибута `name` и массив элементов `items`.
     *   Перебирает элементы `items`, удаляя атрибут `name` у каждого.

26. **`fu.setIndexToItems(name, items)`:**
    *   **Вход:** Имя атрибута `name` и массив элементов `items`.
    *   Перебирает элементы из `items`, устанавливая для каждого атрибут `name` со значением его индекса.

27. **`fu.getParentElement(item)`:**
    *   **Вход:** Любой элемент `item`.
    *   Если `item` является атрибутом, возвращает его родительский элемент.
    *   Если `item` является узлом, возвращает его родительский элемент или узел.
    *   **Возврат:** Родительский элемент, если он есть, иначе `null`.

28. **`fu.getAncestorElements(elem)`:**
    *   **Вход:** Элемент `elem`.
    *   Собирает массив родительских элементов `elem` и возвращает его.

29. **`fu.getOwnerDocument(item)`:**
    *   **Вход:** Любой элемент `item`.
    *   Если `item` является атрибутом, возвращает `ownerDocument` его родительского элемента или `item`.
    *   Если `item` является узлом, возвращает его `ownerDocument`.
    *   **Возврат:** `ownerDocument` или `null`.

30. **`fu.createHeaderRow(values, opts)`:**
    *   **Вход:** Массив значений `values` для заголовка и объект опций `opts`.
    *   Создает строку таблицы (`<tr>`) и заполняет ее заголовками (`<th>`) на основе `values`.
    *   **Возврат:** Строка таблицы (`<tr>`).

31. **`fu.createDetailTableHeader(opts)`:**
    *   **Вход:** Объект опций `opts`.
    *   Создает строку таблицы (`<tr>`) с заголовками столбцов для детальной информации.
    *   **Возврат:** Строка таблицы (`<tr>`).

32. **`fu.createDetailRow(index, detail, opts)`:**
    *   **Вход:** Индекс `index`, объект с деталями `detail`, и объект опций `opts`.
    *   Создает строку таблицы (`<tr>`) с информацией из `detail`, включая кнопку "Focus".
    *   **Возврат:** Строка таблицы (`<tr>`).

33. **`fu.appendDetailRows(parent, details, opts)`:**
    *   **Вход:** Родительский элемент `parent`, массив деталей `details` и объект опций `opts`.
    *   Асинхронно добавляет строки в `parent` с использованием DocumentFragment, разбивая на чанки.
    *   Использует рекурсивный подход, для обработки большого массива данных.
    *   **Возврат:** `Promise`, который разрешается по завершению.

34. **`fu.updateDetailsTable(parent, details, opts)`:**
    *   **Вход:** Родительский элемент `parent`, массив деталей `details` и объект опций `opts`.
    *   Обновляет таблицу в `parent`, добавляя заголовок и детальные строки.
    *   **Возврат:** `Promise`, который разрешается по завершению.

35. **`fu.emptyChildNodes(elem)`:**
    *   **Вход:** Элемент `elem`.
    *   Удаляет все дочерние узлы элемента `elem`.

36. **`fu.saveAttrForItem(item, attr, storage, overwrite)`:**
    *   **Вход:** Элемент `item`, имя атрибута `attr`, `Map` для хранения `storage`, флаг для перезаписи `overwrite`.
    *   Сохраняет значение атрибута `attr` у элемента `item` в хранилище `storage`.
    *   **Возврат:** `storage` с сохраненным значением.

37. **`fu.saveAttrForItems(items, attr, storage, overwrite)`:**
     *   **Вход:** Массив элементов `items`, имя атрибута `attr`, `Map` для хранения `storage`, флаг для перезаписи `overwrite`.
     *   Итерирует по `items` и сохраняет значение атрибута `attr` каждого элемента в `storage` с помощью `fu.saveAttrForItem`.
     *   **Возврат:** `storage` с сохраненными значениями.

38. **`fu.restoreItemAttrs(storage)`:**
    *   **Вход:** Хранилище атрибутов `storage`.
    *   Восстанавливает сохраненные атрибуты элементов из хранилища `storage`.

39. **`fu.getFrameAncestry(inds, win)`:**
    *   **Вход:** Массив индексов фреймов `inds` и window `win`.
    *   Возвращает массив элементов frame на основе переданных индексов.
    *   Если фрейма не существует или доступ запрещен, выбрасывается ошибка.

40. **`fu.isNumberArray(arr)`:**
    *   **Вход:** Массив `arr`.
    *   Проверяет, является ли `arr` массивом чисел.
    *   **Возврат:** `true`, если `arr` - массив чисел, иначе `false`.

41. **`fu.onError(err)`:**
    *   **Вход:** Ошибка `err`.
    *   Функция для обработки ошибок (в текущей реализации она закомментирована).

42. **`fu.isBlankWindow(win)`:**
    *   **Вход:** window `win`.
    *   Проверяет, является ли window `win` пустым окном (about:blank).
    *   **Возврат:** `true`, если окно пустое, иначе `false`.

43. **`fu.collectBlankWindows(top)`:**
    *   **Вход:** Верхнее окно `top`.
    *   Собирает все пустые окна во всех дочерних фреймах.
    *   **Возврат:** Массив пустых окон.

44. **`fu.findFrameElement(win, parent)`:**
    *   **Вход:** window `win` и родительский элемент `parent`.
    *   Ищет iframe, содержащий window `win` внутри `parent`.
    *   **Возврат:** Iframe или `null`.

45. **`fu.findFrameIndex(win, parent)`:**
    *   **Вход:** window `win` и родительский элемент `parent`.
    *   Ищет индекс фрейма с окном `win` внутри `parent`.
    *   **Возврат:** Индекс фрейма или `-1`.

46. **`fu.makeDetailText(detail, keys, separator, replacers)`:**
    *  **Вход:** Объект с деталями `detail`, массив ключей `keys`, разделитель `separator` и объект `replacers`.
    *  Создает строку из значений `detail` для ключей `keys`, разделенных `separator`, применяя `replacers` к значениям.
    *  **Возврат:** Текст.

## <mermaid>
```mermaid
flowchart TD
    subgraph tryxpath.functions
        Start(Start) --> CheckDone{fu.done?};
        CheckDone -- Yes --> End(End);
        CheckDone -- No --> SetDone(fu.done = true);
        SetDone --> ExecExpr(fu.execExpr);
        ExecExpr --> ResToArr(fu.resToArr);
        ExecExpr --> MakeResolver(fu.makeResolver);
        ExecExpr --> QuerySelector(context.querySelector);
        ExecExpr --> QuerySelectorAll(context.querySelectorAll);
        ExecExpr --> ListToArr(fu.listToArr);
        ExecExpr --> IsDocOrElem(fu.isDocOrElem);
        ExecExpr --> IsNodeItem(fu.isNodeItem);
        ExecExpr --> IsAttrItem(fu.isAttrItem);

        MakeResolver --> IsValidDict(fu.isValidDict);
        MakeResolver --> ObjToMap(fu.objToMap);
        MakeResolver --> ResolveNamespace(Resolver Function);

        ResToArr --> GetResultType{res.resultType};
        GetResultType --> NumberType{NUMBER_TYPE};
        GetResultType --> StringType{STRING_TYPE};
        GetResultType --> BooleanType{BOOLEAN_TYPE};
        GetResultType --> IteratorType{ORDERED_NODE_ITERATOR_TYPE/UNORDERED_NODE_ITERATOR_TYPE};
        GetResultType --> SnapshotType{ORDERED_NODE_SNAPSHOT_TYPE/UNORDERED_NODE_SNAPSHOT_TYPE};
        GetResultType --> NodeType{ANY_UNORDERED_NODE_TYPE/FIRST_ORDERED_NODE_TYPE};
        GetResultType --> ErrorType{Invalid resultType};

        IteratorType --> IterateNext(res.iterateNext);
        SnapshotType --> SnapshotItem(res.snapshotItem);
        NodeType --> GetSingleNodeValue(res.singleNodeValue);

        ListToArr --> LoopList(for loop);
    
        ExecExpr --> ReturnResult{return result};

        SetDone --> GetItemDetail(fu.getItemDetail);
        GetItemDetail --> IsElementItem(fu.isElementItem);
        GetItemDetail --> IsAttrItemDetail(fu.isAttrItem);
        GetItemDetail --> GetNodeTypeStr(fu.getNodeTypeStr);

        SetDone --> GetItemDetails(fu.getItemDetails);
        GetItemDetails --> LoopItems(for loop);

        SetDone --> GetXPathResultStr(fu.getxpathResultStr);
        SetDone --> GetXPathResultNum(fu.getxpathResultNum);
        
        SetDone --> IsAttrItemCheck(fu.isAttrItem);
        SetDone --> IsNodeItemCheck(fu.isNodeItem);
        SetDone --> IsElementItemCheck(fu.isElementItem);
        
        SetDone --> AddClassToItem(fu.addClassToItem);
        SetDone --> AddClassToItems(fu.addClassToItems);
        AddClassToItems --> LoopItemsAddClass(for loop);

        SetDone --> SaveItemClass(fu.saveItemClass);
        SaveItemClass --> HasAttribute(item.hasAttribute);

        SetDone --> RestoreItemClass(fu.restoreItemClass);
        RestoreItemClass --> RemoveAttribute(elem.removeAttribute);
        RestoreItemClass --> SetAttribute(elem.setAttribute);

        SetDone --> SaveItemClasses(fu.saveItemClasses);
        SaveItemClasses --> LoopSaveItem(for loop);

        SetDone --> RestoreItemClasses(fu.restoreItemClasses);
        RestoreItemClasses --> LoopRestoreItem(for loop);
    
        SetDone --> SetAttrToItem(fu.setAttrToItem);
        SetDone --> RemoveAttrFromItem(fu.removeAttrFromItem);
         SetDone --> RemoveAttrFromItems(fu.removeAttrFromItems);
        RemoveAttrFromItems --> LoopRemoveAttr(forEach loop);

        SetDone --> SetIndexToItems(fu.setIndexToItems);
        SetIndexToItems --> LoopSetIndex(for loop);

        SetDone --> GetParentElement(fu.getParentElement);
        GetParentElement --> GetOwnerElement(item.ownerElement);
        GetParentElement --> GetParentNode(item.parentNode);

        SetDone --> GetAncestorElements(fu.getAncestorElements);
        GetAncestorElements --> LoopAncestors(while loop);
       
       SetDone --> GetOwnerDocumentFunc(fu.getOwnerDocument);
        GetOwnerDocumentFunc --> GetOwnerElementDoc(item.ownerElement);

        SetDone --> CreateHeaderRow(fu.createHeaderRow);
        CreateHeaderRow --> CreateElementTH(doc.createElement("th"));
        CreateHeaderRow --> AppendChildTH(tr.appendChild(th));

        SetDone --> CreateDetailTableHeader(fu.createDetailTableHeader);
        CreateDetailTableHeader --> CreateElementTHDetail(doc.createElement("th"));
        CreateDetailTableHeader --> AppendChildTHDetail(tr.appendChild(th));
    
        SetDone --> CreateDetailRow(fu.createDetailRow);
        CreateDetailRow --> CreateElementTD(doc.createElement("td"));
        CreateDetailRow --> CreateElementButton(doc.createElement("button"));
        CreateDetailRow --> AppendChildTD(tr.appendChild(td));

        SetDone --> AppendDetailRows(fu.appendDetailRows);
        AppendDetailRows --> CreateDocumentFragment(doc.createDocumentFragment);
        AppendDetailRows --> LoopAppendDetailRows(for loop);
        AppendDetailRows --> AppendChildAppend(parent.appendChild(frag));
        AppendDetailRows --> RecursiveAppend(fu.appendDetailRows);

        SetDone --> UpdateDetailsTable(fu.updateDetailsTable);
        UpdateDetailsTable --> EmptyChildNodes(fu.emptyChildNodes);
         UpdateDetailsTable --> AppendHeaderRow(parent.appendChild(fu.createHeaderRow));
          UpdateDetailsTable --> AppendDetailRowsCall(fu.appendDetailRows);

        SetDone --> EmptyChildNodesFunc(fu.emptyChildNodes);
        EmptyChildNodesFunc --> RemoveFirstChild(elem.removeChild(elem.firstChild));

       SetDone --> SaveAttrForItem(fu.saveAttrForItem);
       SaveAttrForItem --> CheckStorage(storage.has(item));
       SaveAttrForItem --> GetItemStorage(storage.get(item));
       SaveAttrForItem --> HasAttr(item.hasAttribute);
       SaveAttrForItem --> SaveStorage(elemStor.set(attr, val));

       SetDone --> SaveAttrForItems(fu.saveAttrForItems);
        SaveAttrForItems --> LoopSaveAttr(for loop);

        SetDone --> RestoreItemAttrs(fu.restoreItemAttrs);
        RestoreItemAttrs --> LoopStorage(for loop);
        RestoreItemAttrs --> CheckValueAttr(value === null);
        RestoreItemAttrs --> RestoreRemoveAttr(elem.removeAttribute(attr));
         RestoreItemAttrs --> RestoreSetAttr(elem.setAttribute(attr,value));

        SetDone --> GetFrameAncestry(fu.getFrameAncestry);
       GetFrameAncestry --> LoopFrameAncestry(for loop);
      
        SetDone --> IsNumberArray(fu.isNumberArray);
        IsNumberArray --> LoopNumberArray(for loop);

        SetDone --> OnError(fu.onError);
    
         SetDone --> IsBlankWindow(fu.isBlankWindow);
         IsBlankWindow --> IsAboutBlank(win.location.href === "about:blank");
         
        SetDone --> CollectBlankWindows(fu.collectBlankWindows);
        CollectBlankWindows --> LoopFrames(for loop);
          CollectBlankWindows --> RecursiveCollect(fu.collectBlankWindows);
        
          SetDone --> FindFrameElement(fu.findFrameElement);
          FindFrameElement --> LoopIframes(for loop);
         
         SetDone --> FindFrameIndex(fu.findFrameIndex);
           FindFrameIndex --> LoopWins(for loop);

         SetDone --> MakeDetailText(fu.makeDetailText);
           MakeDetailText --> LoopDetailText(forEach loop);
    
     End(End)
    end
```

### Анализ зависимостей `mermaid`

*   **`tryxpath.functions`**: Это пространство имен, в котором определены все функции, представленные на диаграмме. Это центральный блок.

*   **Функции (узлы с `fu.`)**: Каждая функция на диаграмме представляет отдельную операцию, например:
    *   `fu.execExpr`:  Выполняет XPath выражение и управляет потоком выполнения.
    *   `fu.resToArr`: Преобразует результат XPath в массив.
    *   `fu.makeResolver`: Создает функцию для разрешения namespace XPath.
    *   `fu.isDocOrElem`, `fu.isNodeItem`, `fu.isAttrItem`, `fu.isElementItem`:  Проверки типов элементов.
    *   `fu.getItemDetail`, `fu.getItemDetails`:  Извлекают информацию о элементе.
    *   `fu.getNodeTypeStr`, `fu.getxpathResultStr`, `fu.getxpathResultNum`:  Преобразуют типы.
    *   `fu.addClassToItem`, `fu.addClassToItems`: Добавляют классы к элементам.
    *   `fu.saveItemClass`, `fu.restoreItemClass`, `fu.saveItemClasses`, `fu.restoreItemClasses`:  Сохраняют и восстанавливают классы.
    *   `fu.setAttrToItem`, `fu.removeAttrFromItem`, `fu.removeAttrFromItems`: Устанавливают и удаляют атрибуты.
    *   `fu.setIndexToItems`: Добавляет индекс к элементам.
    *   `fu.getParentElement`, `fu.getAncestorElements`:  Получают родительские элементы.
    *   `fu.getOwnerDocument`: Получает документ, которому принадлежит элемент.
    *   `fu.createHeaderRow`, `fu.createDetailTableHeader`, `fu.createDetailRow`, `fu.appendDetailRows`, `fu.updateDetailsTable`: Создают структуру таблицы.
    *   `fu.emptyChildNodes`: Удаляет все дочерние узлы.
    *  `fu.saveAttrForItem`, `fu.saveAttrForItems`, `fu.restoreItemAttrs`:  Сохраняют и восстанавливают атрибуты.
    *   `fu.getFrameAncestry`:  Получает предков фрейма.
    *   `fu.isNumberArray`: Проверяет массив на числовые значения.
    *   `fu.onError`: Обработчик ошибок (не реализован).
    *   `fu.isBlankWindow`, `fu.collectBlankWindows`: Работа с пустыми окнами.
    *   `fu.findFrameElement`, `fu.findFrameIndex`: Ищет фреймы.
     *   `fu.makeDetailText`:  Собирает данные об элементах в одну строку.

*   **Встроенные функции и свойства**:
    *   `doc.evaluate`, `context.querySelector`, `context.querySelectorAll`, `item.ownerElement`, `item.parentElement`, `item.parentNode`, `item.nodeType`, `item.hasAttribute`, `elem.removeAttribute`, `elem.setAttribute`, `document.createElement`, `tr.appendChild`, `res.iterateNext`, `res.snapshotItem`, `res.singleNodeValue`, `storage.has`, `storage.get`, `elemStor.set`, `window.frames`, `win.location.href`: Это вызовы браузерных API, которые используются для работы с DOM.
    *   `Array.isArray`, `Object.keys`, `Object.prototype.toString`, `Map`, `forEach`.
*   **Потоки управления**:
    *   Условные ветвления (`CheckDone`, `GetResultType`, `HasAttribute`, `CheckStorage`, `CheckValueAttr`).
    *   Циклы (`LoopList`, `LoopItems`, `LoopItemsAddClass`, `LoopSaveItem`, `LoopRestoreItem`, `LoopRemoveAttr`,`LoopSetIndex`, `LoopAncestors`, `LoopAppendDetailRows`, `LoopStorage`,`LoopFrameAncestry`,`LoopNumberArray`,`LoopFrames`,`LoopIframes`,`LoopWins`,`LoopDetailText`).
    *   Рекурсивные вызовы (`RecursiveAppend`, `RecursiveCollect`).

## <объяснение>

### Импорты

В данном коде отсутствуют явные операторы `import`, так как это файл JavaScript, предназначенный для выполнения в контексте браузера. Вместо этого, код полагается на глобальные переменные и API браузера.
Однако, стоит отметить, что код использует ряд констант и переменных, связанных с XPath (например, `xpathResult.ANY_TYPE`) и Node (например, `Node.ELEMENT_NODE`). Эти константы доступны через встроенный в браузер объект `document`, `window` и конструкторы Node и xpathResult и не требуют импорта.

### Классы

В этом коде нет определения классов. Весь код построен на функциях и объектах JavaScript.

### Функции

*   `fu.execExpr(expr, method, opts)`:
    *   **Аргументы:**
        *   `expr` (String): XPath выражение для запроса.
        *   `method` (String): Метод выполнения запроса (`evaluate`, `querySelector`, `querySelectorAll`).
        *   `opts` (Object): Объект с опциями, такими как `context` (контекст поиска), `resolver` (функция разрешения namespace) и `resultType` (тип результата).
    *   **Возвращаемое значение:** Объект со структурой `{"items": items, "method": method, "resultType": resultType}`.
    *   **Назначение:** Главная функция для выполнения XPath запросов и запросов CSS селекторов. Она управляет контекстом, выбирает метод выполнения и преобразует результат.
    *   **Примеры:**
        *   `fu.execExpr('//div', 'evaluate', {context: document.body})`
        *   `fu.execExpr('.my-class', 'querySelector', {context: document.getElementById('container')})`
        *   `fu.execExpr('li', 'querySelectorAll', {context: document.querySelector('ul')})`
*   `fu.resToArr(res, type)`:
    *   **Аргументы:**
        *   `res` (XPathResult): Объект результата XPath запроса.
        *   `type` (Number): Тип результата XPath запроса.
    *   **Возвращаемое значение:** Массив элементов, соответствующих результату XPath запроса.
    *   **Назначение:** Преобразует результат XPath запроса в массив. Поддерживает разные типы результатов.
    *   **Примеры:**
        *   `fu.resToArr(result, xpathResult.ORDERED_NODE_ITERATOR_TYPE)`
        *   `fu.resToArr(result, xpathResult.NUMBER_TYPE)`
*   `fu.makeResolver(obj)`:
    *   **Аргументы:**
        *   `obj` (Object|String|Function): Функция-резолвер, словарь или JSON строка.
    *   **Возвращаемое значение:** Функция-резолвер, преобразующая namespace в uri, или `null`.
    *   **Назначение:** Создает функцию для разрешения namespace для XPath запросов. Поддерживает разные форматы входных данных.
    *    **Примеры:**
        *    `fu.makeResolver({prefix1: 'uri1', prefix2: 'uri2'})`
        *    `fu.makeResolver('{"prefix1": "uri1", "prefix2": "uri2"}')`
        *    `fu.makeResolver(function(prefix){ return "uri1"; })`
*   `fu.isValidDict(obj)`:
    *   **Аргументы:**
        *   `obj` (Object): Объект, который нужно проверить.
    *   **Возвращаемое значение:** `true` если объект валидный словарь, иначе `false`.
    *   **Назначение:** Проверяет, является ли объект валидным словарем для `makeResolver`.
    *   **Примеры:**
        *   `fu.isValidDict({prefix1: "uri1", prefix2: "uri2"})` // true
        *   `fu.isValidDict({prefix1: "uri1", prefix2: 123})` // false
        *   `fu.isValidDict("string")` // false
        *   `fu.isValidDict(null)` // false
*   `fu.objToMap(obj)`:
    *   **Аргументы:**
        *   `obj` (Object): Объект, который нужно преобразовать.
    *   **Возвращаемое значение:** `Map` с данными из `obj`.
    *   **Назначение:** Преобразует объект JavaScript в `Map`.
    *   **Примеры:**
         *   `fu.objToMap({key1: 'value1', key2: