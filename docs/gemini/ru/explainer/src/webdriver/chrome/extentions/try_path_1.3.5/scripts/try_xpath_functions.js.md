## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    -   **Переменные**: Их типы и использование.
    -   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. Инициализация и Проверка Выполнения**

   -   Код начинается с проверки существования пространств имен `tryxpath` и `tryxpath.functions`. Если они не существуют, они создаются. Это гарантирует, что код не будет перезаписывать существующие пространства имен.
   -   Затем создаются алиасы `tx` для `tryxpath` и `fu` для `tryxpath.functions`.
   -   Проверяется, был ли код уже выполнен (`fu.done`). Если да, выполнение прекращается, чтобы избежать повторной инициализации. В противном случае устанавливается `fu.done = true`.

**2. Функция `execExpr` (Выполнение XPath/CSS выражений)**

   -   Функция принимает XPath или CSS выражение (`expr`), метод (`method` - 'evaluate', 'querySelector', или 'querySelectorAll') и опциональный объект `opts`.
   -   Определяет контекст (`context`) для поиска (по умолчанию `document`).
   -   Определяет резолвер пространства имен (`resolver`) из `opts`, если он есть.
   -   Получает документ (`doc`) из контекста.
   -   В зависимости от `method`:
      -   **`evaluate`**:
         -   Проверяет, является ли контекст узлом или атрибутом.
         -   Создает резолвер пространства имен.
         -   Выполняет `doc.evaluate(expr, context, resolver, resultType, null)` и преобразует результат в массив (`items`).
         -   Определяет `resultType`, если он был `xpathResult.ANY_TYPE`.
         -   **Пример:** `fu.execExpr("//div[@id='test']", "evaluate", {context: document.body, resultType: xpathResult.ORDERED_NODE_ITERATOR_TYPE})`
      -   **`querySelector`**:
         -   Проверяет, является ли контекст документом или элементом.
         -   Выполняет `context.querySelector(expr)` и возвращает массив из найденного элемента.
         -   **Пример:** `fu.execExpr(".my-class", "querySelector", {context: document.body})`
      -   **`querySelectorAll`**:
          -   Проверяет, является ли контекст документом или элементом.
         -  Выполняет `context.querySelectorAll(expr)` и преобразует результат в массив.
         -  **Пример:** `fu.execExpr(".my-class", "querySelectorAll", {context: document.body})`
   -   Возвращает объект с найденными элементами (`items`), использованным методом (`method`) и типом результата (`resultType`).

**3. Функция `resToArr` (Преобразование результата XPath в массив)**

   -   Принимает результат XPath (`res`) и его тип (`type`).
   -   Если тип не определен или `ANY_TYPE`, используется `res.resultType`.
   -   Создает массив (`arr`) и заполняет его в зависимости от типа:
      -   **NUMBER_TYPE, STRING_TYPE, BOOLEAN_TYPE**: Пушит в массив значения.
      -   **ITERATOR_TYPE**: Итерируется через узлы.
      -   **SNAPSHOT_TYPE**: Итерируется через снапшот.
      -   **ANY_UNORDERED_NODE_TYPE, FIRST_ORDERED_NODE_TYPE**: Пушит один узел.
   -   Возвращает массив результатов.

**4. Функция `makeResolver` (Создание Резолвера Пространства Имен)**

   -   Принимает объект резолвера (`obj`).
   -   Если `obj` `null`, возвращает `null`.
   -   Если `obj` функция, возвращает её.
   -   Если `obj` строка, пытается распарсить её как JSON.
   -   Если `obj` это валидный объект, конвертирует его в Map, и возвращает функцию, которая использует Map для резолвинга.
   -   **Пример:** `fu.makeResolver('{"prefix": "http://example.com"}')`, `fu.makeResolver(function(prefix){ if (prefix === "pre") return "http://example.com"; return ""})`
  -  Если `obj` не валиден, выбрасывает исключение

**5. Функции `isValidDict`, `objToMap` (Работа с Резолвером)**

   -   `isValidDict` проверяет, является ли объект валидным словарем (все значения - строки).
   -   `objToMap` конвертирует объект в `Map`.

**6. Функции `isDocOrElem`, `listToArr` (Проверка Типов и Конвертация)**

   -   `isDocOrElem` проверяет, является ли объект документом или элементом.
   -   `listToArr` конвертирует NodeList в массив.

**7. Функции `getItemDetail`, `getItemDetails` (Получение Информации об Элементе)**

   -   `getItemDetail` возвращает объект с подробной информацией об элементе (тип, имя, значение, текст).
   -  `getItemDetails` возвращает массив объектов с информацией по всем элементам.
   -  **Пример:** `fu.getItemDetail(document.getElementById("test"))`, `fu.getItemDetail("test")`, `fu.getItemDetails([document.getElementById("test"), document.body])`

**8. Функции `getNodeTypeStr`, `getxpathResultStr`, `getxpathResultNum` (Работа с Типами)**

   -  `getNodeTypeStr` возвращает строковое представление типа узла.
   -  `getxpathResultStr` возвращает строковое представление типа результата XPath.
   -  `getxpathResultNum` возвращает числовое представление типа результата XPath.

**9. Функции `isAttrItem`, `isNodeItem`, `isElementItem` (Проверка Типа Элемента)**

   -   `isAttrItem` проверяет, является ли элемент атрибутом.
   -   `isNodeItem` проверяет, является ли элемент узлом.
   -   `isElementItem` проверяет, является ли элемент элементом.

**10. Функции `addClassToItem`, `addClassToItems` (Работа с Классами)**

   -   `addClassToItem` добавляет класс к элементу.
   -   `addClassToItems` добавляет класс к массиву элементов.

**11. Функции `saveItemClass`, `restoreItemClass`, `saveItemClasses`, `restoreItemClasses` (Сохранение и Восстановление Классов)**

   -   Сохраняют и восстанавливают классы элементов.

**12. Функции `setAttrToItem`, `removeAttrFromItem`, `removeAttrFromItems`, `setIndexToItems` (Работа с Атрибутами)**

    - `setAttrToItem` устанавливает атрибут на элемент.
    - `removeAttrFromItem` удаляет атрибут с элемента.
    - `removeAttrFromItems` удаляет атрибут с массива элементов.
    - `setIndexToItems` устанавливает индекс как атрибут на массив элементов.

**13. Функции `getParentElement`, `getAncestorElements` (Работа с Родительскими Элементами)**

   -   `getParentElement` возвращает родительский элемент.
   -  `getAncestorElements` возвращает массив родительских элементов.

**14. Функция `getOwnerDocument` (Получение Документа)**

   -  Возвращает документ, которому принадлежит элемент.

**15. Функции `createHeaderRow`, `createDetailTableHeader`, `createDetailRow` (Создание HTML)**

   -   Создают HTML элементы для таблиц.

**16. Функции `appendDetailRows`, `updateDetailsTable` (Работа с Таблицами)**

   -   `appendDetailRows` добавляет строки в таблицу.
   -   `updateDetailsTable` обновляет таблицу детальной информацией.

**17. Функция `emptyChildNodes` (Удаление дочерних элементов)**

    - Удаляет все дочерние элементы из заданного элемента.

**18. Функции `saveAttrForItem`, `saveAttrForItems`, `restoreItemAttrs` (Сохранение и Восстановление Атрибутов)**

   -  Сохраняют и восстанавливают атрибуты элементов.

**19. Функция `getFrameAncestry` (Получение Предков Фрейма)**

   -  Возвращает массив элементов iframe на основе массива индексов и текущего window.

**20. Функции `isNumberArray`, `onError`, `isBlankWindow`, `collectBlankWindows`, `findFrameElement`, `findFrameIndex` (Работа с Фреймами)**

   -   `isNumberArray` проверяет, является ли массив массивом чисел.
   -  `onError` для обработки ошибок.
   -   `isBlankWindow` проверяет, является ли окно пустым (`about:blank`).
   -   `collectBlankWindows` собирает пустые окна.
    - `findFrameElement` находит элемент iframe по window.
   -   `findFrameIndex` находит индекс фрейма в родительском окне.

**21. Функция `makeDetailText` (Формирование текста из деталей)**

   -  Создает строку из деталей с заданным разделителем.

## <mermaid>

```mermaid
flowchart TD
    subgraph tryxpath
        Start[Start] --> checkNamespace[Проверка/Создание пространств имен tryxpath и tryxpath.functions]
        checkNamespace --> alias[Создание алиасов tx и fu]
        alias --> checkDone[Проверка fu.done]
        checkDone -- fu.done is true --> End[End]
        checkDone -- fu.done is false --> setDone[fu.done = true]
        setDone --> execExpr[fu.execExpr(expr, method, opts)]
        execExpr --> resToArr[fu.resToArr(res, type)]
        execExpr --> querySelector[context.querySelector(expr)]
        execExpr --> querySelectorAll[context.querySelectorAll(expr)]
        resToArr --> getItemDetail[fu.getItemDetail(item)]
        getItemDetail --> getNodeTypeStr[fu.getNodeTypeStr(nodeType)]
        execExpr --> makeResolver[fu.makeResolver(obj)]
         makeResolver --> isValidDict[fu.isValidDict(dict)]
        makeResolver --> objToMap[fu.objToMap(obj)]
        objToMap --> map[new Map()]
         execExpr --> isDocOrElem[fu.isDocOrElem(obj)]
         execExpr --> listToArr[fu.listToArr(list)]
        listToArr --> listLength[list.length]
        execExpr --> getItemDetails[fu.getItemDetails(items)]
        getItemDetails --> getItemDetail
         getItemDetails --> saveItemClass[fu.saveItemClass(item)]
        saveItemClass --> isElementItem[fu.isElementItem(item)]
        saveItemClass --> hasAttribute[item.hasAttribute("class")]
        saveItemClass --> getAttribute[item.getAttribute("class")]
        saveItemClass --> End
        getItemDetails --> restoreItemClasses[fu.restoreItemClasses(savedClasses)]
        restoreItemClasses --> restoreItemClass[fu.restoreItemClass(savedClass)]
        restoreItemClass --> removeAttribute[savedClass.elem.removeAttribute("class")]
        restoreItemClass --> setAttribute[savedClass.elem.setAttribute("class", savedClass.origClass)]
        restoreItemClass --> End
        execExpr --> addClassToItem[fu.addClassToItem(clas, item)]
        addClassToItem --> classListAdd[item.classList.add(clas)]
        execExpr --> addClassToItems[fu.addClassToItems(clas, items)]
        addClassToItems --> addClassToItem
        execExpr --> setAttrToItem[fu.setAttrToItem(name, value, item)]
         setAttrToItem --> isElementItem
         setAttrToItem --> setAttribute_1[item.setAttribute(name, value)]
        execExpr --> removeAttrFromItem[fu.removeAttrFromItem(name, item)]
        removeAttrFromItem --> isElementItem_2[fu.isElementItem(item)]
        removeAttrFromItem --> removeAttribute_2[item.removeAttribute(name)]
        execExpr --> removeAttrFromItems[fu.removeAttrFromItems(name, items)]
        removeAttrFromItems --> removeAttrFromItem_3[fu.removeAttrFromItem(name, item)]
        execExpr --> setIndexToItems[fu.setIndexToItems(name, items)]
        setIndexToItems --> setAttrToItem_2[fu.setAttrToItem(name, i, items[i])]
        execExpr --> getParentElement[fu.getParentElement(item)]
        getParentElement --> isAttrItem[fu.isAttrItem(item)]
        getParentElement --> ownerElement[item.ownerElement]
        getParentElement --> isNodeItem_1[fu.isNodeItem(item)]
        getParentElement --> parentElement[item.parentElement]
        getParentElement --> parentNode[item.parentNode]
        execExpr --> getAncestorElements[fu.getAncestorElements(elem)]
        getAncestorElements --> parentElement_2[cur.parentElement]
        getAncestorElements --> parentNode_2[cur.parentNode]
        execExpr --> getOwnerDocument[fu.getOwnerDocument(item)]
        getOwnerDocument --> isAttrItem_2[fu.isAttrItem(item)]
        getOwnerDocument --> ownerElement_2[item.ownerElement]
        getOwnerDocument --> ownerDocument_2[item.ownerDocument]
        getOwnerDocument --> isNodeItem_2[fu.isNodeItem(item)]
        getOwnerDocument --> ownerDocument_3[item.ownerDocument]
        execExpr --> createHeaderRow[fu.createHeaderRow(values, opts)]
        createHeaderRow --> createElement_1[doc.createElement("tr")]
        createHeaderRow --> createElement_2[doc.createElement("th")]
        createHeaderRow --> appendChild_1[tr.appendChild(th)]
        createHeaderRow --> End_1
        execExpr --> createDetailTableHeader[fu.createDetailTableHeader(opts)]
         createDetailTableHeader --> createElement_3[doc.createElement("tr")]
        createDetailTableHeader --> createElement_4[doc.createElement("th")]
         createDetailTableHeader --> appendChild_2[tr.appendChild(th)]
        createDetailTableHeader --> End_2
        execExpr --> createDetailRow[fu.createDetailRow(index, detail, opts)]
        createDetailRow --> createElement_5[doc.createElement("tr")]
         createDetailRow --> createElement_6[doc.createElement("td")]
         createDetailRow --> appendChild_3[tr.appendChild(td)]
        createDetailRow --> createElement_7[doc.createElement("button")]
        createDetailRow --> setAttribute_3[button.setAttribute("data-index", index)]
        createDetailRow --> appendChild_4[td.appendChild(button)]
        createDetailRow --> End_3
        execExpr --> appendDetailRows[fu.appendDetailRows(parent, details, opts)]
        appendDetailRows --> createDocumentFragment[doc.createDocumentFragment()]
        appendDetailRows --> appendChild_5[frag.appendChild(createRow(index, details[index], ...))]
        appendDetailRows --> appendChild_6[parent.appendChild(frag)]
        appendDetailRows --> appendDetailRows_recur[fu.appendDetailRows(parent, details, ...)]
        execExpr --> updateDetailsTable[fu.updateDetailsTable(parent, details, opts)]
        updateDetailsTable --> emptyChildNodes[fu.emptyChildNodes(parent)]
         emptyChildNodes --> removeChild[elem.removeChild(elem.firstChild)]
        updateDetailsTable --> createHeaderRow_2[fu.createHeaderRow(headerValues, { "document": doc })]
        updateDetailsTable --> appendDetailRows_2[fu.appendDetailRows(parent, details, ...)]
        execExpr --> saveAttrForItem[fu.saveAttrForItem(item, attr, storage, overwrite)]
        saveAttrForItem --> isElementItem_3[fu.isElementItem(item)]
        saveAttrForItem --> hasAttribute_2[item.hasAttribute(attr)]
        saveAttrForItem --> getAttribute_2[item.getAttribute(attr)]
        saveAttrForItem -->  elemStorHas[elemStor.has(attr)]
        saveAttrForItem --> set_1[elemStor.set(attr, val)]
       execExpr --> saveAttrForItems[fu.saveAttrForItems(items, attr, storage, overwrite)]
        saveAttrForItems --> saveAttrForItem_2[fu.saveAttrForItem(item, attr, storage, overwrite)]
       execExpr --> restoreItemAttrs[fu.restoreItemAttrs(storage)]
        restoreItemAttrs --> removeAttribute_3[elem.removeAttribute(attr)]
        restoreItemAttrs --> setAttribute_4[elem.setAttribute(attr, value)]
        execExpr --> getFrameAncestry[fu.getFrameAncestry(inds, win)]
        getFrameAncestry --> frames_1[win.frames[inds[i]]]
         getFrameAncestry --> frameElement[win.frameElement]
        execExpr --> isNumberArray[fu.isNumberArray(arr)]
        execExpr --> onError[fu.onError(err)]
        execExpr --> isBlankWindow[fu.isBlankWindow(win)]
        execExpr --> collectBlankWindows[fu.collectBlankWindows(top)]
        collectBlankWindows --> isBlankWindow_2[fu.isBlankWindow(win)]
        collectBlankWindows --> collectBlankWindows_recur[fu.collectBlankWindows(win)]
        execExpr --> findFrameElement[fu.findFrameElement(win, parent)]
        findFrameElement --> getElementsByTagName[parent.document.getElementsByTagName("iframe")]
        findFrameElement --> contentWindow[frames[i].contentWindow]
        execExpr --> findFrameIndex[fu.findFrameIndex(win, parent)]
        findFrameIndex -->  parent_frames[parent.frames]
        execExpr --> makeDetailText[fu.makeDetailText(detail, keys, separator, replacers)]
    end
```

**Объяснение зависимостей:**

-   **`tryxpath`**: Это глобальный объект, представляющий собой пространство имен для всего кода.
-   **`tryxpath.functions`**: Вложенный объект, где хранятся все функции, предназначенные для работы с XPath и CSS.
-   **`window`**: Глобальный объект, представляющий окно браузера. Используется для доступа к `document` и `frame`.
-   **`document`**: Объект, представляющий HTML документ.
-   **`Node`**: Интерфейс, представляющий узел в DOM.
-   **`xpathResult`**: Объект с константами, представляющими различные типы результатов XPath.

## <объяснение>

### Импорты

В данном коде отсутствуют явные импорты из других файлов или пакетов `src`. Код является самодостаточным и работает с глобальным окружением браузера (объекты `window`, `document`, `Node`).

### Классы

В данном коде нет явного определения классов. Вместо этого, используется объект `tryxpath.functions` как контейнер для функций, что соответствует подходу функционального программирования.

### Функции

Код содержит множество функций, каждая из которых выполняет определенную задачу:

-   **`fu.execExpr(expr, method, opts)`**:
    -   **Аргументы:**
        -   `expr` (string): XPath или CSS выражение.
        -   `method` (string): Метод выполнения ('evaluate', 'querySelector', 'querySelectorAll').
        -   `opts` (object, optional): Объект с опциями.
    -   **Возвращаемое значение:** Объект с результатами (`items`, `method`, `resultType`).
    -   **Назначение:** Выполняет XPath или CSS выражения, возвращает результаты в массиве.
    -   **Пример:**
        ```javascript
        fu.execExpr("//div[@class='test']", "evaluate", { context: document.body });
        fu.execExpr(".test-class", "querySelectorAll", { context: document.body });
        ```
-   **`fu.resToArr(res, type)`**:
    -   **Аргументы:**
        -   `res` (object): Результат выполнения XPath.
        -   `type` (number, optional): Тип результата XPath.
    -   **Возвращаемое значение:** Массив значений или узлов.
    -   **Назначение:** Преобразует результат XPath в массив.
    -   **Пример:**
        ```javascript
        var xpathResult = document.evaluate("//div", document, null, xpathResult.ORDERED_NODE_ITERATOR_TYPE, null);
        var arr = fu.resToArr(xpathResult);
        ```

-   **`fu.makeResolver(obj)`**:
    -   **Аргументы:**
        -   `obj` (object/string/function): Объект резолвера.
    -   **Возвращаемое значение:** Функция резолвер или null
    -   **Назначение:** Создает функцию-резолвер пространства имен из объекта, строки JSON или функции.

-   **`fu.isValidDict(obj)`**:
    -   **Аргументы:**
        -   `obj` (object): Объект для проверки.
    -   **Возвращаемое значение:** Boolean, является ли переданный объект словарем (все значения строки).
    -   **Назначение:** Проверяет, является ли объект словарем.

-   **`fu.objToMap(obj)`**:
    -   **Аргументы:**
        -   `obj` (object): Объект для преобразования.
    -   **Возвращаемое значение:** `Map`.
    -   **Назначение:** Преобразует объект в `Map`.

-   **`fu.isDocOrElem(obj)`**:
    -   **Аргументы:**
        -   `obj` (object): Объект для проверки.
    -   **Возвращаемое значение:** `Boolean`, является ли объект document или element.
    -   **Назначение:** Проверяет, является ли объект документом или элементом.

-   **`fu.listToArr(list)`**:
    -   **Аргументы:**
        -   `list` (NodeList): NodeList для преобразования.
    -   **Возвращаемое значение:** `Array`.
    -   **Назначение:** Преобразует NodeList в массив.

-   **`fu.getItemDetail(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент для получения информации.
    -   **Возвращаемое значение:** Объект с детальной информацией о элементе.
    -   **Назначение:** Возвращает объект с информацией о элементе.

-   **`fu.getItemDetails(items)`**:
    -   **Аргументы:**
        -   `items` (array): Массив элементов.
    -   **Возвращаемое значение:** Массив объектов с детальной информацией о элементах.
    -   **Назначение:** Возвращает массив объектов с информацией о элементах.

-   **`fu.getNodeTypeStr(nodeType)`**:
    -   **Аргументы:**
        -   `nodeType` (number): Тип узла.
    -   **Возвращаемое значение:** Строковое представление типа узла.
    -   **Назначение:** Возвращает строковое представление типа узла.

-   **`fu.getxpathResultStr(resultType)`**:
    -   **Аргументы:**
        -   `resultType` (number): Тип результата XPath.
    -   **Возвращаемое значение:** Строковое представление типа результата XPath.
    -   **Назначение:** Возвращает строковое представление типа результата XPath.

-    **`fu.getxpathResultNum(resultTypeStr)`**:
    -   **Аргументы:**
        -   `resultTypeStr` (string): Строковое представление типа результата XPath.
    -   **Возвращаемое значение:** Числовое представление типа результата XPath.
    -   **Назначение:** Возвращает числовое представление типа результата XPath.

-    **`fu.isAttrItem(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент для проверки.
    -   **Возвращаемое значение:** `Boolean`
    -   **Назначение:** Проверяет, является ли элемент атрибутом.

-   **`fu.isNodeItem(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент для проверки.
    -   **Возвращаемое значение:** `Boolean`
    -   **Назначение:** Проверяет, является ли элемент узлом.

-   **`fu.isElementItem(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент для проверки.
    -   **Возвращаемое значение:** `Boolean`
    -   **Назначение:** Проверяет, является ли элемент элементом.

-   **`fu.addClassToItem(clas, item)`**:
    -   **Аргументы:**
        -   `clas` (string): Класс для добавления.
        -   `item` (Element): Элемент.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Добавляет класс к элементу.

-   **`fu.addClassToItems(clas, items)`**:
    -   **Аргументы:**
        -   `clas` (string): Класс для добавления.
        -   `items` (Array): Массив элементов.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Добавляет класс к массиву элементов.

-   **`fu.saveItemClass(item)`**:
    -   **Аргументы:**
        -   `item` (Element): Элемент.
    -   **Возвращаемое значение:** Объект с сохраненной информацией о классе или null
    -   **Назначение:** Сохраняет класс элемента.

-    **`fu.restoreItemClass(savedClass)`**:
    -   **Аргументы:**
        -   `savedClass` (object): Объект с сохраненной информацией о классе.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Восстанавливает класс элемента.

-    **`fu.saveItemClasses(items)`**:
    -   **Аргументы:**
        -   `items` (Array): Массив элементов.
    -   **Возвращаемое значение:** Массив объектов с сохраненной информацией о классах
    -   **Назначение:** Сохраняет классы массива элементов.

-    **`fu.restoreItemClasses(savedClasses)`**:
    -   **Аргументы:**
        -   `savedClasses` (Array): Массив объектов с сохраненной информацией о классах.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Восстанавливает классы массива элементов.

-   **`fu.setAttrToItem(name, value, item)`**:
    -   **Аргументы:**
        -   `name` (string): Имя атрибута.
        -   `value` (string): Значение атрибута.
        -   `item` (Element): Элемент.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Устанавливает атрибут на элемент.

-   **`fu.removeAttrFromItem(name, item)`**:
    -   **Аргументы:**
        -   `name` (string): Имя атрибута.
        -   `item` (Element): Элемент.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Удаляет атрибут с элемента.

-   **`fu.removeAttrFromItems(name, items)`**:
    -   **Аргументы:**
        -   `name` (string): Имя атрибута.
        -   `items` (Array): Массив элементов.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Удаляет атрибут с массива элементов.

-   **`fu.setIndexToItems(name, items)`**:
    -   **Аргументы:**
        -   `name` (string): Имя атрибута.
        -   `items` (Array): Массив элементов.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Устанавливает индекс в виде атрибута на массив элементов.

-   **`fu.getParentElement(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент.
    -   **Возвращаемое значение:** Родительский элемент или null.
    -   **Назначение:** Возвращает родительский элемент.

-   **`fu.getAncestorElements(elem)`**:
    -   **Аргументы:**
        -   `elem` (Element): Элемент.
    -   **Возвращаемое значение:** Массив родительских элементов.
    -   **Назначение:** Возвращает массив родительских элементов.

-    **`fu.getOwnerDocument(item)`**:
    -   **Аргументы:**
        -   `item` (any): Элемент
    -   **Возвращаемое значение:** `Document`.
    -   **Назначение:** Возвращает документ элемента.

-   **`fu.createHeaderRow(values, opts)`**:
    -   **Аргументы:**
        -   `values` (Array): Массив значений для заголовка.
        -   `opts` (object): Объект опций.
    -   **Возвращаемое значение:** HTML `tr` элемент
    -   **Назначение:** Создает строку HTML для заголовка таблицы.

-   **`fu.createDetailTableHeader(opts)`**:
    -   **Аргументы:**
        -   `opts` (object): Объект опций.
    -   **Возвращаемое значение:** HTML `tr` элемент
    -   **Назначение:** Создает строку HTML для заголовка таблицы с деталями.

-   **`fu.createDetailRow(index, detail, opts)`**:
    -   **Аргументы:**
        -   `index` (number): Индекс строки.
        -   `detail` (object): Объект с детальной информацией.
        -   `opts` (object): Объект опций.
    -   **Возвращаемое значение:** HTML `tr` элемент
    -   **Назначение:** Создает строку HTML для таблицы с деталями.

-   **`fu.appendDetailRows(parent, details, opts)`**:
    -   **Аргументы:**
        -   `parent` (Element): Родительский элемент для вставки строк.
        -   `details` (Array): Массив объектов с детальной информацией.
        -   `opts` (object): Объект опций.
    -   **Возвращаемое значение:** `Promise`, resolve когда добавлены все строки.
    -   **Назначение:** Добавляет строки в таблицу с использованием DocumentFragment и Promises для улучшения производительности.

-   **`fu.updateDetailsTable(parent, details, opts)`**:
    -   **Аргументы:**
        -   `parent` (Element): Родительский элемент для таблицы.
        -   `details` (Array): Массив объектов с детальной информацией.
        -   `opts` (object): Объект опций.
    -   **Возвращаемое значение:** `Promise`, resolve когда таблица обновлена.
    -   **Назначение:** Обновляет таблицу с детальной информацией.

-   **`fu.emptyChildNodes(elem)`**:
    -   **Аргументы:**
        -   `elem` (Element): Элемент для очистки.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Удаляет все дочерние узлы элемента.

-   **`fu.saveAttrForItem(item, attr, storage, overwrite)`**:
    -   **Аргументы:**
        -   `item` (Element): Элемент для сохранения атрибута.
        -   `attr` (string): Имя атрибута.
        -   `storage` (Map): Map для хранения атрибутов.
        -   `overwrite` (boolean, optional): Перезаписать ли атрибут если он уже сохранен.
    -   **Возвращаемое значение:** `Map`
    -   **Назначение:** Сохраняет атрибут элемента в Map.

-   **`fu.saveAttrForItems(items, attr, storage, overwrite)`**:
     -   **Аргументы:**
         -   `items` (Array): Массив элементов.
         -  `attr` (string): Имя атрибута.
         -   `storage` (Map): Map для хранения атрибутов.
         -   `overwrite` (boolean, optional): Перезаписать ли атрибут если он уже сохранен.
    -    **Возвращаемое значение:** `Map`
     -   **Назначение:** Сохраняет атрибуты массива элементов в Map.

-   **`fu.restoreItemAttrs(storage)`**:
    -   **Аргументы:**
        -   `storage` (Map): Map с сохраненными атрибутами.
    -   **Возвращаемое значение:** `void`
    -   **Назначение:** Восстанавливает атрибуты элементов из Map.

-    **`fu.getFrameAncestry(inds, win)`**:
    -   **Аргументы:**
        -   `