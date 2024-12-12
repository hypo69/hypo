## <алгоритм>

1. **Инициализация**:
   - Проверяется наличие глобального объекта `tryxpath` и его свойства `functions`. Если их нет, они создаются. Это обеспечивает изоляцию кода и предотвращает конфликты имен.
   - Создаются псевдонимы `tx` и `fu` для `tryxpath` и `tryxpath.functions` соответственно для удобства работы.
   - Проверяется, не была ли функция `tryxpath.functions` уже выполнена (свойство `done`). Если да, то функция завершается. Это предотвращает многократное выполнение кода.

2. **`fu.execExpr(expr, method, opts)`**:
   - Принимает XPath-выражение (`expr`), метод выполнения (`method`: "evaluate", "querySelector", "querySelectorAll") и опции (`opts`).
   - Извлекает контекст (`context`), резолвер пространства имен (`resolver`), и документ (`doc`) из `opts` или использует значения по умолчанию.
   - В зависимости от метода (`method`):
     - **"evaluate"**:
       - Проверяет, что контекст - узел (`Node`) или атрибут (`Attr`).
       - Создает резолвер имен с помощью `fu.makeResolver`.
       - Выполняет XPath-выражение с помощью `doc.evaluate()`.
       - Преобразует результат в массив с помощью `fu.resToArr()`.
       - Пример: `fu.execExpr("//div", "evaluate", {context: document.body});`
     - **"querySelector"**:
       - Проверяет, что контекст - документ (`Document`) или элемент (`Element`).
       - Использует `context.querySelector()` для поиска первого совпадения.
       - Преобразует результат в массив.
       - Пример: `fu.execExpr("div.myclass", "querySelector", {context: document});`
     - **"querySelectorAll" (default)**:
       - Проверяет, что контекст - документ (`Document`) или элемент (`Element`).
       - Использует `context.querySelectorAll()` для поиска всех совпадений.
       - Преобразует результат в массив с помощью `fu.listToArr()`.
       - Пример: `fu.execExpr("div", "querySelectorAll", {context: document});`
   - Возвращает объект с массивом результатов `items`, методом `method`, и типом результата `resultType`.

3. **`fu.resToArr(res, type)`**:
   - Принимает результат XPath (`res`) и тип результата (`type`).
   - Если `type` не указан, то берется `res.resultType`.
   - В зависимости от `type` результат преобразуется в массив:
     - `NUMBER_TYPE`, `STRING_TYPE`, `BOOLEAN_TYPE`: Значение помещается в массив.
       Пример: `[123]`, `["text"]`, `[true]`
     - `ORDERED_NODE_ITERATOR_TYPE`, `UNORDERED_NODE_ITERATOR_TYPE`: Перебираются все узлы с помощью `res.iterateNext()` и добавляются в массив.
     - `ORDERED_NODE_SNAPSHOT_TYPE`, `UNORDERED_NODE_SNAPSHOT_TYPE`: Перебираются все узлы с помощью `res.snapshotItem(i)` и добавляются в массив.
     - `ANY_UNORDERED_NODE_TYPE`, `FIRST_ORDERED_NODE_TYPE`: Первый узел помещается в массив.
   - Возвращает массив результатов.

4. **`fu.makeResolver(obj)`**:
   - Принимает объект резолвера (`obj`).
   - Если `obj` равен `null`, то возвращает `null`.
   - Если `obj` - функция, то возвращает ее.
   - Если `obj` - строка, то пытается распарсить JSON и создать словарь. Если парсинг не удается, то выбрасывается ошибка.
   - Если `obj` - словарь, то проверяется его валидность с помощью `fu.isValidDict`. Если не валидный, выбрасывается ошибка.
   - Преобразует словарь в `Map` с помощью `fu.objToMap` и возвращает функцию-резолвер, которая ищет значения в `Map`.

5.  **`fu.isValidDict(obj)`**:
    - Проверяет, является ли `obj` валидным словарем (объект, у которого все значения - строки).
    - Возвращает `true` если все значения объекта являются строками.
    - Возвращает `false` если `obj` не является объектом или если хоть одно из значений не является строкой.

6. **`fu.objToMap(obj)`**:
   - Принимает объект (`obj`).
   - Создает `Map` и для каждой пары ключ-значение в `obj` добавляет ее в `Map`.
   - Возвращает `Map`.

7. **`fu.isDocOrElem(obj)`**:
   - Проверяет, является ли `obj` узлом типа Document (9) или Element (1).
   - Возвращает `true` если `obj` является Document или Element.
   - Возвращает `false` если `obj` не является Document или Element.

8. **`fu.listToArr(list)`**:
   - Преобразует псевдомассив (NodeList) в массив.
   - Перебирает `list` и добавляет каждый элемент в массив.
   - Возвращает массив.

9. **`fu.getItemDetail(item)`**:
    - Определяет тип элемента (`item`) и возвращает объект с информацией о типе, имени, значении и текстовом содержимом.
    - Для строк, чисел и булевых значений возвращает объект с соответствующей информацией.
    - Для элементов (`Element`) возвращает объект с типом узла, именем тега, и текстом.
    - Для атрибутов (`Attr`) возвращает объект с типом "Attr", именем атрибута и его значением.
    - Для остальных типов узлов возвращает объект с типом, именем узла, значением узла и текстовым содержимым.

10. **`fu.getItemDetails(items)`**:
    - Принимает массив элементов (`items`) и возвращает массив объектов с детальной информацией о каждом элементе.
    - Использует `fu.getItemDetail` для получения информации о каждом элементе.

11. **`fu.getNodeTypeStr(nodeType)`**:
    - Принимает числовой код типа узла (`nodeType`) и возвращает его строковое представление.
    - Использует `nodeTypeMap` для поиска строкового представления.
    - Возвращает строку "Unknown", если код типа узла не найден.

12. **`fu.getxpathResultStr(resultType)`**:
    - Принимает числовой код типа результата XPath (`resultType`) и возвращает его строковое представление.
    - Использует `xpathResultMaps.numToStr` для поиска строкового представления.
    - Возвращает строку "Unknown", если код не найден.

13. **`fu.getxpathResultNum(resultTypeStr)`**:
    - Принимает строковое представление типа результата XPath (`resultTypeStr`) и возвращает его числовой код.
    - Использует `xpathResultMaps.strToNum` для поиска числового кода.
    - Возвращает `NaN`, если строка не найдена.

14. **`fu.isAttrItem(item)`**:
   - Проверяет, является ли `item` атрибутом `Attr`.
   - Возвращает `true`, если `item` является атрибутом.

15. **`fu.isNodeItem(item)`**:
   - Проверяет, является ли `item` узлом (не строкой, не числом).
   - Возвращает `true` если `item` является узлом.

16. **`fu.isElementItem(item)`**:
    - Проверяет, является ли `item` элементом (`Element`).
    - Проверяет, что `item` является узлом и его `nodeType` равен `Node.ELEMENT_NODE`.
    - Возвращает `true` если `item` является элементом.

17. **`fu.addClassToItem(clas, item)`**:
    - Добавляет класс (`clas`) к элементу (`item`), если `item` является элементом.

18. **`fu.addClassToItems(clas, items)`**:
    - Добавляет класс (`clas`) ко всем элементам в массиве `items`.
    - Использует `fu.addClassToItem` для добавления класса к каждому элементу.

19. **`fu.saveItemClass(item)`**:
    - Сохраняет класс элемента (`item`).
    - Возвращает объект с элементом и его оригинальным классом или `null`, если `item` не является элементом.

20. **`fu.restoreItemClass(savedClass)`**:
   - Восстанавливает сохраненный класс элемента.
   - Удаляет класс, если `origClass` равен `null`.
   - Если `savedClass` равен `null`, то возвращает `null`.
   - Устанавливает сохраненный класс, если `origClass` не равен `null`.

21. **`fu.saveItemClasses(items)`**:
    - Сохраняет классы для всех элементов в массиве `items`.
    - Возвращает массив объектов с сохраненными классами.
    - Использует `fu.saveItemClass` для сохранения класса каждого элемента.

22. **`fu.restoreItemClasses(savedClasses)`**:
    - Восстанавливает сохраненные классы для всех элементов в массиве `savedClasses`.
    - Использует `fu.restoreItemClass` для восстановления класса каждого элемента.

23. **`fu.setAttrToItem(name, value, item)`**:
   - Устанавливает атрибут `name` со значением `value` для элемента `item`.

24. **`fu.removeAttrFromItem(name, item)`**:
   - Удаляет атрибут `name` из элемента `item`.

25. **`fu.removeAttrFromItems(name, items)`**:
    - Удаляет атрибут `name` у всех элементов в массиве `items`.
    - Использует `fu.removeAttrFromItem` для удаления атрибута у каждого элемента.

26. **`fu.setIndexToItems(name, items)`**:
    - Устанавливает атрибут `name` с индексом элемента в массиве `items` для каждого элемента.
    - Использует `fu.setAttrToItem` для установки атрибута.

27. **`fu.getParentElement(item)`**:
   - Возвращает родительский элемент для `item`.
   - Для атрибутов используется `ownerElement`.
   - Для узлов используется `parentElement`, если он существует. Если нет, то используется `parentNode`, если он является элементом.

28. **`fu.getAncestorElements(elem)`**:
   - Возвращает массив всех родительских элементов для элемента `elem`.
   - Перебирает элементы вверх по дереву, пока не дойдет до корня.

29. **`fu.getOwnerDocument(item)`**:
    - Возвращает документ, которому принадлежит узел `item`.
    - Для атрибутов используется `ownerElement.ownerDocument`.
    - Для узлов используется `ownerDocument`.

30. **`fu.createHeaderRow(values, opts)`**:
    - Создает строку заголовка таблицы (`<tr>`) с ячейками заголовков (`<th>`) для каждого значения в массиве `values`.
    - Используется для создания заголовка таблицы.

31. **`fu.createDetailTableHeader(opts)`**:
   - Создает заголовок таблицы с колонками: "Index", "Type", "Name", "Value", "Focus".
   - Используется для создания заголовка таблицы с деталями элемента.

32. **`fu.createDetailRow(index, detail, opts)`**:
    - Создает строку таблицы (`<tr>`) с данными об элементе (`detail`).
    - Создает ячейки таблицы (`<td>`) для индекса, типа, имени и значения элемента.
    - Добавляет кнопку "Focus" с индексом элемента.
    - Используется для создания строки таблицы с деталями элемента.

33. **`fu.appendDetailRows(parent, details, opts)`**:
    - Добавляет строки с деталями элемента в родительский элемент (`parent`).
    - Использует рекурсию для обработки большого количества деталей (`details`) чанками.
    - Вызывает `fu.createDetailRow` для создания каждой строки таблицы и добавляет её в `DocumentFragment`.
    - Добавляет фрагмент в `parent`.

34. **`fu.updateDetailsTable(parent, details, opts)`**:
    - Обновляет таблицу с деталями элемента.
    - Очищает родительский элемент `parent`, добавляет заголовок и строки с деталями.
    - Использует `fu.emptyChildNodes`, `fu.createHeaderRow`, `fu.appendDetailRows`.

35. **`fu.emptyChildNodes(elem)`**:
    - Удаляет все дочерние узлы из элемента `elem`.

36. **`fu.saveAttrForItem(item, attr, storage, overwrite)`**:
    - Сохраняет атрибут `attr` элемента `item` в `storage`.
    - Если `overwrite` равен true, то значение атрибута перезаписывается.

37. **`fu.saveAttrForItems(items, attr, storage, overwrite)`**:
   - Сохраняет атрибут `attr` для всех элементов в массиве `items`.
   - Использует `fu.saveAttrForItem` для сохранения атрибута каждого элемента.

38. **`fu.restoreItemAttrs(storage)`**:
    - Восстанавливает сохраненные атрибуты для всех элементов в `storage`.

39. **`fu.getFrameAncestry(inds, win)`**:
   - Получает массив фреймов по индексам `inds`, начиная с окна `win`.
   - Если фрейм не найден, выбрасывается ошибка.

40. **`fu.isNumberArray(arr)`**:
   - Проверяет, является ли `arr` массивом чисел.
   - Если `arr` пустой, то возвращает `true`.

41. **`fu.onError(err)`**:
   - Функция-заглушка для обработки ошибок.

42. **`fu.isBlankWindow(win)`**:
    - Проверяет, является ли окно (`win`) пустым (содержит "about:blank").

43. **`fu.collectBlankWindows(top)`**:
   - Собирает все пустые окна (`about:blank`) в иерархии фреймов, начиная с `top`.
   - Рекурсивно проходит по всем фреймам.

44. **`fu.findFrameElement(win, parent)`**:
   - Находит элемент фрейма `iframe` для окна `win` в родительском элементе `parent`.

45. **`fu.findFrameIndex(win, parent)`**:
    - Находит индекс окна `win` в массиве фреймов `parent`.

46. **`fu.makeDetailText(detail, keys, separator, replacers)`**:
    - Создает текстовое представление данных из объекта `detail`, используя ключи `keys`.
    - Использует разделитель `separator` и функции замены из `replacers`.

## <mermaid>

```mermaid
graph TD
    A[Start] --> B{fu.done?};
    B -- Yes --> C[Return];
    B -- No --> D[fu.done = true];
    D --> E[fu.execExpr];
    E --> F[fu.resToArr];
    E --> G[context.querySelector];
    E --> H[context.querySelectorAll];
    F --> I[switch(type)];
    I --> J[push(res.numberValue)];
    I --> K[push(res.stringValue)];
     I --> L[push(res.booleanValue)];
     I --> M[res.iterateNext()];
     I --> N[res.snapshotItem(i)];
     I --> O[push(res.singleNodeValue)];
     M --> P[arr.push(node)];
     N --> Q[arr.push(item)];
    E --> R[Return {items, method, resultType}];
    D --> S[fu.makeResolver];
    S --> T{obj is null?};
    T -- Yes --> U[return null];
    T -- No --> V{obj is function?};
    V -- Yes --> W[return obj];
    V -- No --> X{obj is string?};
    X -- Yes --> Y[JSON.parse(obj)];
     Y --> Z{isValidDict};
      Z -- No --> AA[throw Error];
      Z --> AB[objToMap];
     AB --> AC[return function(str)];
      AC --> AD{map.has(str)?};
      AD -- Yes --> AE[return map.get(str)];
      AD -- No --> AF[return ""];
    X -- No --> AG[dict = obj];
      AG --> Z;
    D --> AH[fu.isValidDict];
    AH --> AI{obj is null or not obj?};
      AI -- Yes --> AJ[return false];
      AI -- No --> AK[for key of obj.keys];
      AK --> AL{typeof(obj[key]) is not string};
      AL -- Yes --> AM[return false];
      AL -- No --> AN[return true];
    D --> AO[fu.objToMap];
     AO --> AP[create map];
      AP --> AQ[Object.keys(obj).forEach()];
      AQ --> AR[map.set(item, obj[item])];
      AR --> AS[return map];
    D --> AT[fu.isDocOrElem];
     AT --> AU{obj.nodeType is 1 or 9};
     AU -- Yes --> AV[return true];
     AU -- No --> AW[return false];
     D --> AX[fu.listToArr];
     AX --> AY[create elems];
       AY --> AZ[for i < list.length];
       AZ --> BA[elems.push(list[i])];
     BA --> BB[return elems];
    D --> BC[fu.getItemDetail];
    BC --> BD{typeof(item)};
     BD --> BE[return String detail];
     BD --> BF[return Number detail];
    BD --> BG[return Boolean detail];
     BG --> BH{isElementItem};
     BH -- Yes --> BI[return Element detail];
     BH -- No --> BJ{isAttrItem};
     BJ -- Yes --> BK[return Attr detail];
      BJ -- No --> BL[return Node detail];
    D --> BM[fu.getItemDetails];
     BM --> BN[create details];
      BN --> BO[for i < items.length];
      BO --> BP[push(fu.getItemDetail)];
      BP --> BQ[return details];
   D --> BR[fu.getNodeTypeStr];
      BR --> BS{nodeTypeMap.has(nodeType)};
      BS -- Yes --> BT[return nodeTypeMap.get(nodeType)];
      BS -- No --> BU[return "Unknown"];
   D --> BV[fu.getxpathResultStr];
      BV --> BW{xpathResultMaps.numToStr.has(resultType)};
      BW -- Yes --> BX[return xpathResultMaps.numToStr.get(resultType)];
      BW -- No --> BY[return "Unknown"];
   D --> BZ[fu.getxpathResultNum];
      BZ --> CA{xpathResultMaps.strToNum.has(resultTypeStr)};
      CA -- Yes --> CB[return xpathResultMaps.strToNum.get(resultTypeStr)];
      CA -- No --> CC[return NaN];
   D --> CD[fu.isAttrItem];
       CD --> CE[return Object.prototype.toString.call(item) === "[object Attr]"];
  D --> CF[fu.isNodeItem];
      CF --> CG{isAttrItem};
      CG -- Yes --> CH[return false];
      CG -- No --> CI{typeof(item)};
      CI --> CJ[return false];
      CI --> CK[return true];
   D --> CL[fu.isElementItem];
       CL --> CM{isNodeItem and nodeType is ELEMENT_NODE};
       CM -- Yes --> CN[return true];
       CM -- No --> CO[return false];
   D --> CP[fu.addClassToItem];
        CP --> CQ{isElementItem};
        CQ -- Yes --> CR[item.classList.add(clas)];
   D --> CS[fu.addClassToItems];
        CS --> CT[for item of items];
        CT --> CU[fu.addClassToItem];
   D --> CV[fu.saveItemClass];
       CV --> CW{isElementItem};
       CW -- No --> CX[return null];
       CW -- Yes --> CY{item.hasAttribute("class")};
       CY -- Yes --> CZ[clas = item.getAttribute("class")];
       CY -- No --> DA[clas = null];
       DA --> DB[return {elem, origClass}];
   D --> DC[fu.restoreItemClass];
        DC --> DD{savedClass is null};
         DD -- Yes --> DE[return null];
         DD -- No --> DF{savedClass.origClass is null};
         DF -- Yes --> DG[savedClass.elem.removeAttribute("class")];
         DF -- No --> DH[savedClass.elem.setAttribute("class", savedClass.origClass)];
    D --> DI[fu.saveItemClasses];
    DI --> DJ[create savedClasses];
    DJ --> DK[for item of items];
    DK --> DL[push(fu.saveItemClass)];
    DL --> DM[return savedClasses];
    D --> DN[fu.restoreItemClasses];
      DN --> DO[for savedClass of savedClasses];
      DO --> DP[fu.restoreItemClass];
   D --> DQ[fu.setAttrToItem];
   DQ --> DR{isElementItem};
     DR -- Yes --> DS[item.setAttribute(name, value)];
   D --> DT[fu.removeAttrFromItem];
     DT --> DU{isElementItem};
     DU -- Yes --> DV[item.removeAttribute(name)];
   D --> DW[fu.removeAttrFromItems];
   DW --> DX[items.forEach()];
   DX --> DY[fu.removeAttrFromItem];
    D --> DZ[fu.setIndexToItems];
    DZ --> EA[for i < items.length];
    EA --> EB[fu.setAttrToItem];
   D --> EC[fu.getParentElement];
    EC --> ED{isAttrItem};
    ED -- Yes --> EE[return item.ownerElement];
    ED -- No --> EF{isNodeItem};
    EF -- Yes --> EG[return item.parentElement];
      EG --> EH{parent exists?};
      EH -- Yes --> EI[return parent];
      EH -- No --> EJ[parent = item.parentNode];
      EJ --> EK{parent is ELEMENT_NODE};
      EK -- Yes --> EL[return parent];
      EK -- No --> EM[return null];
   D --> EN[fu.getAncestorElements];
    EN --> EO[create ancs];
    EO --> EP[cur = elem];
    EP --> EQ[parent = cur.parentElement];
    EQ --> ER{parent exists};
    ER -- Yes --> ES[push(parent) ancs];
     ES --> ET[cur = parent];
     ET --> EU[parent = cur.parentElement];
      EU --> ER;
    ER -- No --> EV[parent = cur.parentNode];
      EV --> EW{parent is ELEMENT_NODE};
    EW -- Yes --> EX[push(cur)];
     EX --> EY[cur = parent];
      EY --> EZ[parent = cur.parentNode];
      EZ --> EW;
    EW -- No --> FA[return ancs];
   D --> FB[fu.getOwnerDocument];
    FB --> FC{isAttrItem};
     FC -- Yes --> FD[elem = item.ownerElement];
    FD --> FE{elem exists};
     FE -- Yes --> FF[return elem.ownerDocument];
     FE -- No --> FG[return item.ownerDocument];
    FC -- No --> FH{isNodeItem};
    FH -- Yes --> FI[return item.ownerDocument];
    FH -- No --> FJ[return null];
   D --> FK[fu.createHeaderRow];
    FK --> FL[create tr];
    FL --> FM[for value of values];
    FM --> FN[create th];
    FN --> FO[th.textContent = value];
    FO --> FP[tr.appendChild(th)];
    FP --> FQ[return tr];
    D --> FR[fu.createDetailTableHeader];
    FR --> FS[create tr];
    FS --> FT[create th for Index];
    FT --> FU[create th for Type];
    FU --> FV[create th for Name];
    FV --> FW[create th for Value];
    FW --> FX[create th for Focus];
    FX --> FY[return tr];
    D --> FZ[fu.createDetailRow];
    FZ --> GA[create tr];
    GA --> GB[create td for index];
    GB --> GC[create td for keys];
    GC --> GD[create td for focus button];
    GD --> GE[return tr];
    D --> GF[fu.appendDetailRows];
     GF --> GG[Promise.resolve().then()];
     GG --> GH[opts = opts || {}];
      GH --> GI[chunkSize, begin, end, createRow];
      GI --> GJ[doc = parent.ownerDocument];
      GJ --> GK[create DocumentFragment];
      GK --> GL[index = Math.max(begin, 0)];
      GL --> GM[chunkEnd = Math.min(index+chunkSize, details.length, end)];
      GM --> GN[for index < chunkEnd];
      GN --> GO[frag.appendChild(createRow)];
      GO --> GP[parent.appendChild(frag)];
      GP --> GQ{index < end and index < details.length};
       GQ -- Yes --> GR[Recursive fu.appendDetailRows];
       GQ -- No --> GS[return];
    D --> GT[fu.updateDetailsTable];
     GT --> GU[opts = opts || {}];
      GU --> GV[chunkSize, begin, end];
       GV --> GW{opts.headerValues exists};
      GW -- Yes --> GX[headerValues = ["Index"].concat(...)];
      GW -- No --> GY[headerValues = ["Index", "Type", "Name", "Value", "Focus"]];
      GY --> GZ[doc = parent.ownerDocument];
       GZ --> HA[fu.emptyChildNodes(parent)];
       HA --> HB[parent.appendChild(fu.createHeaderRow(...))];
       HB --> HC[fu.appendDetailRows(parent, details, ...)];
   D --> HD[fu.emptyChildNodes];
      HD --> HE[while(elem.firstChild)];
       HE --> HF[elem.removeChild(elem.firstChild)];
   D --> HG[fu.saveAttrForItem];
    HG --> HH[storage = storage || new Map()];
       HH --> HI{isElementItem};
       HI -- No --> HJ[return storage];
       HI -- Yes --> HK{storage.has(item)};
        HK -- Yes --> HL[elemStor = storage.get(item)];
        HK -- No --> HM[elemStor = new Map(); storage.set(item, elemStor)];
        HM --> HN[val = item.hasAttribute(attr) ? item.getAttribute(attr) : null;];
        HN --> HO{overwrite or !elemStor.has(attr)};
        HO -- Yes --> HP[elemStor.set(attr, val)];
        HP --> HQ[return storage];
    D --> HR[fu.saveAttrForItems];
      HR --> HS[storage = storage || new Map()];
       HS --> HT[for item of items];
        HT --> HU[fu.saveAttrForItem()];
       HU --> HV[return storage];
     D --> HW[fu.restoreItemAttrs];
       HW --> HX[for [elem, elemStor] of storage];
        HX --> HY[for [attr, value] of elemStor];
        HY --> HZ{value is null};
         HZ -- Yes --> IA[elem.removeAttribute(attr)];
         HZ -- No --> IB[elem.setAttribute(attr, value)];
    D --> IC[fu.getFrameAncestry];
     IC --> ID[win = win || window];
     ID --> IE[create frames];
       IE --> IF[for i < inds.length];
        IF --> IG[win = win.frames[inds[i]]];
          IG --> IH{win exists};
          IH -- No --> II[throw Error];
          IH -- Yes --> IJ[frame = win.frameElement];
           IJ --> IK{frameElement exists};
            IK -- Yes --> IL[frames.push(frame)];
          IK -- No --> IM[throw Error];
        IM --> IN[return frames];
    D --> IO[fu.isNumberArray];
      IO --> IP[!Array.isArray(arr)];
      IP -- Yes --> IQ[return false];
      IP -- No --> IR[for item of arr];
      IR --> IS{typeof(item) !== "number"};
      IS -- Yes --> IT[return false];
       IS -- No --> IU[return true];
    D --> IV[fu.onError];
    D --> IW[fu.isBlankWindow];
      IW --> IX[return win.location.href === "about:blank"];
    D --> IY[fu.collectBlankWindows];
      IY --> IZ[create wins];
       IZ --> JA[for i < frames.length];
        JA --> JB[win = frames[i]];
        JB --> JC{fu.isBlankWindow(win)};
          JC -- Yes --> JD[wins.push(win)];
          JD --> JE[wins = wins.concat(fu.collectBlankWindows(win))];
           JE --> JF[return wins];
       JC -- No --> JF;
    D --> JG[fu.findFrameElement];
    JG --> JH[frames = parent.document.getElementsByTagName("iframe")];
       JH --> JI[for i < frames.length];
        JI --> JJ{win === frames[i].contentWindow};
        JJ -- Yes --> JK[return frames[i]];
    JK --> JL[return null];
   D --> JM[fu.findFrameIndex];
    JM --> JN[wins = parent.frames];
    JN --> JO[for i < wins.length];
    JO --> JP{win === wins[i]};
     JP -- Yes --> JQ[return i];
      JQ --> JR[return -1];
    D --> JS[fu.makeDetailText];
     JS --> JT[create texts];
     JT --> JU[keys.forEach(key)];
      JU --> JV[val = detail[key]];
      JV --> JW{replacers[key]};
        JW -- Yes --> JX[val = replacers[key](val)];
         JX --> JY[texts.push(val)];
       JW -- No --> JY;
      JY --> JZ[return texts.join(separator)];
```

## <объяснение>

**Импорты:**

В данном коде нет явных импортов. Код работает в глобальном пространстве `window` браузера. Все необходимые зависимости (например, `Node`, `xpathResult`)  предполагаются как встроенные или определенные в окружении браузера.

**Классы:**

В коде не определены классы. Он использует JavaScript-объекты в качестве контейнеров для функций и данных.

**Функции:**

- **`fu.execExpr(expr, method, opts)`**:
    - **Аргументы**:
        - `expr`: XPath-выражение в виде строки.
        - `method`: Метод выполнения выражения (строка): "evaluate", "querySelector", "querySelectorAll".
        - `opts`: Объект с опциями:
            - `context`: Контекстный узел для выполнения выражения (по умолчанию `document`).
            - `resolver`: Функция резолвера пространств имен или объект-словарь для резолвера.
            - `document`: Документ для выполнения выражения (по умолчанию документ контекста или `document`).
            - `resultType`: Тип результата XPath-выражения для `evaluate`.
    - **Возвращаемое значение**: Объект со свойствами:
        - `items`: Массив найденных элементов или значений.
        - `method`: Переданный метод.
        - `resultType`: Тип результата XPath-выражения.
    - **Назначение**: Выполняет XPath-выражение или CSS-селектор на основе заданного контекста и метода. Преобразует результат в массив.
    - **Пример**: `fu.execExpr("//div[@class='test']", "evaluate", {context: document.body, resolver: {"my": "http://example.com"}});` или `fu.execExpr("div.test", "querySelectorAll", {context: document.body});`.
- **`fu.resToArr(res, type)`**:
    - **Аргументы**:
        - `res`: Результат выполнения XPath-выражения.
        - `type`: Тип результата XPath-выражения (числовая константа).
    - **Возвращаемое значение**: Массив с результатами.
    - **Назначение**: Преобразует результат XPath в массив, в зависимости от типа результата.
    - **Пример**: Если `res` - это `xpathResult.NUMBER_TYPE` со значением `123`, то функция вернет `[123]`.
- **`fu.makeResolver(obj)`**:
    - **Аргументы**: `obj`: Объект резолвера (функция, строка-JSON или словарь).
    - **Возвращаемое значение**: Функция-резолвер или `null`.
    - **Назначение**: Создает функцию-резолвер для пространств имен XPath, которая может быть передана в `doc.evaluate()`. Позволяет преобразовывать префиксы пространств имен в URI.
    - **Пример**: `fu.makeResolver({"my": "http://example.com"})` вернет функцию, которая будет возвращать `"http://example.com"` при вызове с аргументом `"my"`.
- **`fu.isValidDict(obj)`**:
    - **Аргументы**: `obj`: Объект для проверки.
    - **Возвращаемое значение**: `true` или `false`.
    - **Назначение**: Проверяет, является ли объект допустимым словарем (все значения - строки).
    - **Пример**: `fu.isValidDict({"a": "1", "b": "2"})` вернет `true`, а `fu.isValidDict({"a": 1, "b": "2"})` вернет `false`.
- **`fu.objToMap(obj)`**:
    - **Аргументы**: `obj`: Объект для преобразования.
    - **Возвращаемое значение**: `Map`.
    - **Назначение**: Преобразует объект в `Map`.
    - **Пример**: `fu.objToMap({"a": "1", "b": "2"})` вернет `Map {"a" => "1", "b" => "2"}`.
- **`fu.isDocOrElem(obj)`**:
    - **Аргументы**: `obj`: Объект для проверки.
    - **Возвращаемое значение**: `true` или `false`.
    - **Назначение**: Проверяет, является ли объект `Document` или `Element`.
- **`fu.listToArr(list)`**: