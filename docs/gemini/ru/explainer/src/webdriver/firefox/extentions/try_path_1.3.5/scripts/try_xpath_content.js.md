## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,  
    которые импортируются при создании диаграммы.  
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,  
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:  
    - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
    - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
    - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
    - **Переменные**: Их типы и использование.  
    - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
### <алгоритм>

1.  **Инициализация**:
    *   Проверка `tx.isContentLoaded` для предотвращения многократного выполнения скрипта. Если скрипт уже загружен, выполнение прекращается.
    *   Инициализация переменных:
        *   `dummyItem`, `dummyItems`, `invalidExecutionId`, `styleElementHeader` - константы для значений по умолчанию и заголовка стилей.
        *   `attributes` - объект с атрибутами данных для элементов.
        *   `prevMsg`, `executionCount`, `inBlankWindow`, `currentDocument`, `contextItem`, `currentItems`, `focusedItem`, `focusedAncestorItems`, `currentCss`, `insertedStyleElements`, `expiredCssSet`, `originalAttributes` - переменные для отслеживания состояния, хранения данных и элементов.

2.  **Функции управления атрибутами**:
    *   `setAttr(attr, value, item)`: Сохраняет старый атрибут элемента и устанавливает новый атрибут.
    *   `setIndex(attr, items)`: Сохраняет старые атрибуты элементов и устанавливает индексы для переданных элементов.

3.  **Управление фокусом**:
    *   `isFocusable(item)`: Проверяет, является ли элемент фокусируемым (элемент или атрибут).
    *   `focusItem(item)`:
        *   Удаляет фокус с ранее сфокусированного элемента и его предков.
        *   Определяет элемент для фокуса (сам элемент или его родительский элемент, если это атрибут).
        *   Устанавливает атрибуты фокуса на элемент и его предков.
        *   Фокусирует элемент и прокручивает его в поле видимости.
        *   *Пример*: Пользователь кликает на элемент, функция `focusItem` устанавливает на него атрибут `data-tryxpath-focused` и прокручивает элемент, чтобы он стал видимым.

4.  **Функции настройки и сброса состояния**:
    *   `setMainAttrs()`: Устанавливает основные атрибуты `data-tryxpath-context` и `data-tryxpath-element` для контекстного и текущих элементов.
        *   *Пример*: После выполнения запроса XPath устанавливаются атрибуты на найденные элементы, чтобы их можно было идентифицировать в DOM.
    *   `restoreAttrs()`: Восстанавливает оригинальные атрибуты элементов, удаляя добавленные атрибуты.
    *   `resetPrev()`: Сбрасывает все переменные состояния, подготавливая к новому запросу.
    *   `makeTypeStr(resultType)`: Преобразует числовой тип результата XPath в строку.
        *   *Пример*: `makeTypeStr(4)` вернёт строку `"UNORDERED_NODE_ITERATOR_TYPE(4)"`.

5.  **Функции CSS**:
    *   `updateCss()`: Отправляет сообщение для обновления стилей CSS, если есть новые или устаревшие стили.
    *   `handleCssChange(newCss)`: Обрабатывает изменение CSS, отслеживая текущий CSS и устаревшие стили.
        *   *Пример*: Когда пользователь изменяет CSS в настройках, эта функция определяет, нужно ли обновлять стили на странице.

6.  **Функции управления окнами и фреймами**:
    *   `getFrames(spec)`: Получает фреймы на основе спецификации.
        *   *Пример*: `getFrames("[0,1]")` вернёт массив из двух фреймов, где первый фрейм является `window.frames[0]`, а второй `window.frames[1]`.
    *   `parseFrameDesignation(frameDesi)`: Преобразует строку спецификации фрейма в массив индексов.
    *   `traceBlankWindows(desi, win)`: Проверяет цепочку фреймов и возвращает информацию о том, есть ли в этой цепочке пустые фреймы.
    *   `findFrameByMessage(event, win)`: Находит фрейм по сообщению от другого фрейма.
    *   `setFocusFrameListener(win, isBlankWindow)`: Устанавливает обработчик сообщений для фокусировки на фрейме.
    *   `initBlankWindow(win)`: Инициализирует пустые окна для обработки запросов xpath.

7.  **Функции стилизации элементов**:
    *    `findStyleParent(doc)`: Находит родительский элемент для вставки элемента style.
    *   `updateStyleElement(doc)`: Обновляет или вставляет CSS стили в документ.
    *   `updateAllStyleElements()`: Обновляет CSS стили во всех добавленных элементах style.
    *   `removeStyleElement(doc)`: Удаляет элемент style из документа.
    *   `removeAllStyleElements()`: Удаляет все элементы style.

8.  **Создание сообщения результата**:
    *   `createResultMessage()`: Создает объект сообщения с информацией о результате выполнения запроса XPath.

9.  **Обработчики сообщений**:
    *   `genericListener(message, sender, sendResponse)`: Главный обработчик сообщений.
    *   `genericListener.listeners.setContentInfo(message)`: Устанавливает атрибуты из сообщения.
    *   `genericListener.listeners.execute(message, sender)`: Выполняет XPath запрос, обрабатывает контекст, фреймы и результаты.
        *   *Пример*: Пользователь вводит XPath запрос в расширении, сообщение отправляется в этот скрипт, функция `execute` выполняет запрос и возвращает результат.
    *   `genericListener.listeners.focusItem(message)`: Фокусирует выбранный элемент.
    *   `genericListener.listeners.focusContextItem(message)`: Фокусирует контекстный элемент.
    *   `genericListener.listeners.focusFrame(message)`: Фокусирует фрейм.
    *   `genericListener.listeners.requestShowResultsInPopup()`: Отправляет предыдущий результат в popup.
    *   `genericListener.listeners.requestShowAllResults()`: Запрашивает отображение всех результатов.
    *   `genericListener.listeners.resetStyle()`: Сбрасывает все добавленные стили.
    *   `genericListener.listeners.setStyle()`: Устанавливает стили на элементы.
    *   `genericListener.listeners.finishInsertCss(message)`: Завершает вставку CSS, обновляя стили на странице.
    *   `genericListener.listeners.finishRemoveCss(message)`: Завершает удаление CSS.

10. **Обработчики событий**:
    *   `browser.storage.onChanged.addListener(...)`: Обрабатывает изменения в хранилище расширения (атрибуты, CSS).
    *   `window.addEventListener("message", ...)`: Обрабатывает сообщения из других фреймов, например, об ошибках.

11. **Инициализация и отправка первого сообщения**:
    *   Инициализируется `prevMsg`.
    *   Устанавливается обработчик сообщений для главного окна.
    *   Отправляется сообщение `requestSetContentInfo` для запроса информации о содержимом.

### <mermaid>

```mermaid
flowchart TD
    Start[Start: Script Execution] --> CheckContentLoaded{Is content loaded?}
    CheckContentLoaded -- Yes --> Stop[Stop]
    CheckContentLoaded -- No --> InitializeVariables[Initialize variables]
    
    InitializeVariables --> SetAttrFunc[setAttr(attr, value, item)]
    InitializeVariables --> SetIndexFunc[setIndex(attr, items)]
    InitializeVariables --> IsFocusableFunc[isFocusable(item)]
    InitializeVariables --> FocusItemFunc[focusItem(item)]
    InitializeVariables --> SetMainAttrsFunc[setMainAttrs()]
    InitializeVariables --> RestoreAttrsFunc[restoreAttrs()]
    InitializeVariables --> ResetPrevFunc[resetPrev()]
    InitializeVariables --> MakeTypeStrFunc[makeTypeStr(resultType)]
    InitializeVariables --> UpdateCssFunc[updateCss()]
    InitializeVariables --> HandleCssChangeFunc[handleCssChange(newCss)]
    InitializeVariables --> GetFramesFunc[getFrames(spec)]
    InitializeVariables --> ParseFrameDesignationFunc[parseFrameDesignation(frameDesi)]
    InitializeVariables --> TraceBlankWindowsFunc[traceBlankWindows(desi, win)]
    InitializeVariables --> FindFrameByMessageFunc[findFrameByMessage(event, win)]
     InitializeVariables --> SetFocusFrameListenerFunc[setFocusFrameListener(win, isBlankWindow)]
    InitializeVariables --> InitBlankWindowFunc[initBlankWindow(win)]
    InitializeVariables --> FindStyleParentFunc[findStyleParent(doc)]
    InitializeVariables --> UpdateStyleElementFunc[updateStyleElement(doc)]
    InitializeVariables --> UpdateAllStyleElementsFunc[updateAllStyleElements()]
    InitializeVariables --> RemoveStyleElementFunc[removeStyleElement(doc)]
    InitializeVariables --> RemoveAllStyleElementsFunc[removeAllStyleElements()]
    InitializeVariables --> CreateResultMessageFunc[createResultMessage()]
   InitializeVariables --> GenericListenerFunc[genericListener(message, sender, sendResponse)]
    
    GenericListenerFunc --> SetContentInfoListener[genericListener.listeners.setContentInfo(message)]
    GenericListenerFunc --> ExecuteListener[genericListener.listeners.execute(message, sender)]
    GenericListenerFunc --> FocusItemListener[genericListener.listeners.focusItem(message)]
    GenericListenerFunc --> FocusContextItemListener[genericListener.listeners.focusContextItem(message)]
    GenericListenerFunc --> FocusFrameListener[genericListener.listeners.focusFrame(message)]
    GenericListenerFunc --> RequestShowResultsInPopupListener[genericListener.listeners.requestShowResultsInPopup()]
   GenericListenerFunc --> RequestShowAllResultsListener[genericListener.listeners.requestShowAllResults()]
     GenericListenerFunc --> ResetStyleListener[genericListener.listeners.resetStyle()]
     GenericListenerFunc --> SetStyleListener[genericListener.listeners.setStyle()]
    GenericListenerFunc --> FinishInsertCssListener[genericListener.listeners.finishInsertCss(message)]
    GenericListenerFunc --> FinishRemoveCssListener[genericListener.listeners.finishRemoveCss(message)]
   

   ExecuteListener --> ResetPrevFunc
   ExecuteListener --> UpdateCssFunc
   ExecuteListener --> GetFramesFunc
   ExecuteListener --> ParseFrameDesignationFunc
   ExecuteListener --> TraceBlankWindowsFunc

   FocusItemListener --> UpdateStyleElementFunc
    FocusContextItemListener --> UpdateStyleElementFunc
   
   
   SetStyleListener --> RestoreAttrsFunc
     SetStyleListener --> UpdateCssFunc
    SetStyleListener --> UpdateStyleElementFunc
     SetStyleListener --> SetMainAttrsFunc

    InitializeVariables --> StorageOnChangedListener[browser.storage.onChanged.addListener(changes => {...})]
   InitializeVariables --> WindowMessageListener[window.addEventListener("message", event => {...})]

   InitializeVariables --> SetFocusFrameListenerMain[setFocusFrameListener(window, false)]
    InitializeVariables --> SendRequestSetContentInfo[browser.runtime.sendMessage({"event": "requestSetContentInfo"})]

    StorageOnChangedListener --> HandleCssChangeFunc
    
    WindowMessageListener --> CreateResultMessageFunc
  
     SetAttrFunc --> fu_saveAttrForItem[fu.saveAttrForItem()]
    SetAttrFunc --> fu_setAttrToItem[fu.setAttrToItem()]
    SetIndexFunc --> fu_saveAttrForItems[fu.saveAttrForItems()]
     SetIndexFunc --> fu_setIndexToItems[fu.setIndexToItems()]
    IsFocusableFunc --> fu_isNodeItem[fu.isNodeItem()]
    IsFocusableFunc --> fu_isAttrItem[fu.isAttrItem()]
    FocusItemFunc --> fu_removeAttrFromItem[fu.removeAttrFromItem()]
    FocusItemFunc --> fu_removeAttrFromItems[fu.removeAttrFromItems()]
     FocusItemFunc --> fu_isElementItem[fu.isElementItem()]
      FocusItemFunc --> fu_getParentElement[fu.getParentElement()]
      FocusItemFunc --> fu_getAncestorElements[fu.getAncestorElements()]
      FocusItemFunc --> setAttr
      FocusItemFunc --> setIndex
   GetFramesFunc --> fu_getFrameAncestry[fu.getFrameAncestry()]
   FindFrameByMessageFunc --> fu_findFrameElement[fu.findFrameElement()]
   
     
   ExecuteListener --> fu_getxpathResultNum[fu.getxpathResultNum()]
   ExecuteListener --> makeTypeStr
   ExecuteListener --> fu_execExpr[fu.execExpr()]
   ExecuteListener --> fu_getItemDetail[fu.getItemDetail()]
  ExecuteListener --> fu_getItemDetails[fu.getItemDetails()]
  
  FocusFrameListener -->  ParseFrameDesignationFunc
   FocusFrameListener --> TraceBlankWindowsFunc
     FocusFrameListener --> fu_findFrameIndex[fu.findFrameIndex()]
  
   
    classDef function fill:#f9f,stroke:#333,stroke-width:2px
    class  SetAttrFunc,SetIndexFunc,IsFocusableFunc,FocusItemFunc,SetMainAttrsFunc,RestoreAttrsFunc,ResetPrevFunc,MakeTypeStrFunc,UpdateCssFunc,HandleCssChangeFunc,GetFramesFunc,ParseFrameDesignationFunc,TraceBlankWindowsFunc,FindFrameByMessageFunc,SetFocusFrameListenerFunc,InitBlankWindowFunc,FindStyleParentFunc,UpdateStyleElementFunc,UpdateAllStyleElementsFunc,RemoveStyleElementFunc,RemoveAllStyleElementsFunc,CreateResultMessageFunc,GenericListenerFunc, fu_saveAttrForItem, fu_setAttrToItem, fu_saveAttrForItems,fu_setIndexToItems,fu_isNodeItem, fu_isAttrItem, fu_removeAttrFromItem, fu_removeAttrFromItems, fu_isElementItem,fu_getParentElement,fu_getAncestorElements,fu_getFrameAncestry,fu_findFrameElement,fu_getxpathResultNum,fu_execExpr,fu_getItemDetail,fu_getItemDetails,fu_findFrameIndex, StorageOnChangedListener,WindowMessageListener,SetFocusFrameListenerMain,SendRequestSetContentInfo function
    
    classDef listener fill:#ccf,stroke:#333,stroke-width:2px
    class  SetContentInfoListener, ExecuteListener, FocusItemListener, FocusContextItemListener,FocusFrameListener,RequestShowResultsInPopupListener,RequestShowAllResultsListener,ResetStyleListener,SetStyleListener,FinishInsertCssListener,FinishRemoveCssListener listener
    
```

В данном коде `mermaid` описывает блок схему работы скрипта. 
- Начинается с проверки загруженности скрипта `CheckContentLoaded` . 
- Если скрипт не загружен, выполняется блок `InitializeVariables`, который содержит инициализации всех переменных и функций.
-   Функции, начинающиеся с `fu_`, обозначают функции из `tryxpath.functions`, т.е. `var fu = tryxpath.functions;`
-   `genericListener` - обработчик всех сообщений, который перенаправляет вызовы к соответствующим лисенерам. 
-   Остальные блоки  (`StorageOnChangedListener`, `WindowMessageListener`) - слушатели событий, срабатывающие при наступлении определенных условий.
-   В самом конце диаграммы показана инициализация и отправка стартового сообщения.

### <объяснение>

**Импорты**:

*   В начале кода объявляются алиасы:
    *   `var tx = tryxpath;` - создает алиас `tx` для объекта `tryxpath`, который, предположительно, является глобальным объектом или объектом, доступным в текущей области видимости, и который содержит общую функциональность расширения.
    *   `var fu = tryxpath.functions;` - создает алиас `fu` для объекта `tryxpath.functions`, который содержит набор функций для работы с XPath и DOM.

**Классы**:

*   В коде нет явных объявлений классов, используется функциональное программирование и объекты.

**Функции**:

*   **`setAttr(attr, value, item)`**:
    *   **Аргументы**:
        *   `attr` (строка): Имя атрибута, который нужно установить.
        *   `value` (строка): Значение атрибута.
        *   `item` (DOM-элемент или объект): Элемент, которому нужно установить атрибут.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Сохраняет старое значение атрибута элемента и устанавливает новое. Используется для добавления атрибутов, чтобы выделять элементы, соответствующие xpath выражению.
    *   **Пример**: `setAttr("data-tryxpath-element", "true", document.querySelector("div"));`
*   **`setIndex(attr, items)`**:
    *   **Аргументы**:
        *   `attr` (строка): Имя атрибута для установки.
        *   `items` (массив): Массив DOM-элементов, которым нужно установить атрибут.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Сохраняет старые значения атрибутов для элементов и устанавливает индекс элемента. Используется, например, для добавления атрибута, указывающего порядковый номер элемента, соответствующего xpath выражению.
    *   **Пример**: `setIndex("data-tryxpath-index", document.querySelectorAll("li"));`
*   **`isFocusable(item)`**:
    *   **Аргументы**:
        *   `item` (DOM-элемент или объект): Элемент для проверки.
    *   **Возвращаемое значение**: `true`, если элемент можно сфокусировать; `false` в противном случае.
    *   **Назначение**: Проверяет, может ли элемент быть сфокусирован (элемент или атрибут).
    *   **Пример**: `isFocusable(document.querySelector("button"));`
*   **`focusItem(item)`**:
    *   **Аргументы**:
        *   `item` (DOM-элемент или объект): Элемент, который нужно сфокусировать.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Устанавливает фокус на указанный элемент, прокручивает его в поле видимости и устанавливает атрибуты для отслеживания.
    *   **Пример**: `focusItem(document.querySelector("a"));`
*   **`setMainAttrs()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Устанавливает атрибуты контекста и индекса элемента.
    *   **Пример**: `setMainAttrs();`
*   **`restoreAttrs()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Восстанавливает оригинальные атрибуты элементов.
    *   **Пример**: `restoreAttrs();`
*   **`resetPrev()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Сбрасывает состояние для подготовки к новому запросу.
    *   **Пример**: `resetPrev();`
*   **`makeTypeStr(resultType)`**:
    *   **Аргументы**:
        *   `resultType` (число): Код типа результата XPath.
    *   **Возвращаемое значение**: Строка, представляющая тип результата.
    *   **Назначение**: Преобразует числовой тип результата XPath в строку.
    *   **Пример**: `makeTypeStr(4);` вернет строку `"UNORDERED_NODE_ITERATOR_TYPE(4)"`
*   **`updateCss()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Отправляет сообщение для обновления стилей CSS.
    *   **Пример**: `updateCss();`
*   **`handleCssChange(newCss)`**:
    *   **Аргументы**:
        *   `newCss` (строка): Новый CSS.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Обрабатывает изменения CSS, управляет флагом устаревших стилей и текущим стилем.
    *   **Пример**: `handleCssChange("body { color: red; }");`
*   **`getFrames(spec)`**:
    *   **Аргументы**:
        *   `spec` (строка): Спецификация фреймов в формате JSON массива.
    *   **Возвращаемое значение**: Массив фреймов.
    *   **Назначение**: Получает фреймы по спецификации.
    *   **Пример**: `getFrames("[0,1]");`
*   **`parseFrameDesignation(frameDesi)`**:
    *   **Аргументы**:
        *   `frameDesi` (строка): Спецификация фрейма в формате JSON массива.
    *   **Возвращаемое значение**: Массив индексов фреймов.
    *   **Назначение**: Парсит строку спецификации фрейма.
    *   **Пример**: `parseFrameDesignation("[0,1]");`
*   **`traceBlankWindows(desi, win)`**:
    *   **Аргументы**:
        *   `desi` (массив): Массив индексов фреймов.
        *   `win` (window): Начальное окно.
    *   **Возвращаемое значение**: Объект с информацией о фреймах, является ли фрейм пустым или нет.
    *   **Назначение**: Проверяет цепочку фреймов на наличие пустых фреймов.
    *   **Пример**: `traceBlankWindows([0, 1], window);`
*   **`findFrameByMessage(event, win)`**:
    *   **Аргументы**:
        *   `event` (объект): Событие сообщения.
        *   `win` (window): Окно.
    *   **Возвращаемое значение**: DOM элемент фрейма.
    *   **Назначение**: Находит фрейм по сообщению.
    *   **Пример**: `findFrameByMessage(event, window);`
*   **`setFocusFrameListener(win, isBlankWindow)`**:
    *   **Аргументы**:
        *   `win` (window): Окно, для которого устанавливается листенер.
        *   `isBlankWindow` (boolean): Является ли окно пустым.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Устанавливает обработчик сообщений для фокуса на фрейме.
    *   **Пример**: `setFocusFrameListener(window, false);`
*   **`initBlankWindow(win)`**:
    *   **Аргументы**:
        *   `win` (window): Окно для инициализации.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Инициализирует пустые окна.
    *   **Пример**: `initBlankWindow(window.frames[0]);`
*    **`findStyleParent(doc)`**:
    *   **Аргументы**:
        *   `doc` (Document): DOM document.
    *   **Возвращаемое значение**: DOM элемент head или body.
    *   **Назначение**: Находит родительский элемент для вставки элемента style.
    *   **Пример**: `findStyleParent(document);`
*   **`updateStyleElement(doc)`**:
    *   **Аргументы**:
        *   `doc` (Document): DOM document.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Обновляет или вставляет CSS стили в документ.
    *   **Пример**: `updateStyleElement(document);`
*   **`updateAllStyleElements()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Обновляет CSS стили во всех элементах style.
    *   **Пример**: `updateAllStyleElements();`
*   **`removeStyleElement(doc)`**:
    *   **Аргументы**:
        *   `doc` (Document): DOM document.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Удаляет элемент style из документа.
    *   **Пример**: `removeStyleElement(document);`
*    **`removeAllStyleElements()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Удаляет все элементы style.
    *   **Пример**: `removeAllStyleElements();`
*   **`createResultMessage()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Объект сообщения результата.
    *   **Назначение**: Создает объект сообщения с информацией о результате выполнения запроса XPath.
    *   **Пример**: `createResultMessage();`
*   **`genericListener(message, sender, sendResponse)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение от расширения.
        *   `sender` (объект): Отправитель сообщения.
        *   `sendResponse` (функция): Функция обратного вызова для отправки ответа.
    *   **Возвращаемое значение**: Зависит от вызванного лисенера.
    *   **Назначение**: Обрабатывает сообщения от расширения, перенаправляя вызовы к соответствующим обработчикам.
    *   **Пример**: Вызывается автоматически при получении сообщения от расширения.
*   **`genericListener.listeners.setContentInfo(message)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение с атрибутами.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Устанавливает атрибуты из сообщения.
    *   **Пример**: Вызывается при получении сообщения с событием "setContentInfo".
*   **`genericListener.listeners.execute(message, sender)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение с параметрами запроса XPath.
        *   `sender` (объект): Отправитель сообщения.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Выполняет XPath запрос, обрабатывает контекст, фреймы и результаты.
    *   **Пример**: Вызывается при получении сообщения с событием "execute".
*   **`genericListener.listeners.focusItem(message)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение с индексом элемента для фокуса.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Фокусирует выбранный элемент.
    *   **Пример**: Вызывается при получении сообщения с событием "focusItem".
*   **`genericListener.listeners.focusContextItem(message)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение для фокуса контекста.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Фокусирует контекстный элемент.
    *   **Пример**: Вызывается при получении сообщения с событием "focusContextItem".
*   **`genericListener.listeners.focusFrame(message)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение с спецификацией фрейма.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Фокусирует фрейм.
    *   **Пример**: Вызывается при получении сообщения с событием "focusFrame".
*    **`genericListener.listeners.requestShowResultsInPopup()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Отправляет предыдущий результат в popup.
    *    **Пример**: Вызывается при получении сообщения с событием "requestShowResultsInPopup".
*   **`genericListener.listeners.requestShowAllResults()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Запрашивает отображение всех результатов.
    *   **Пример**: Вызывается при получении сообщения с событием "requestShowAllResults".
*   **`genericListener.listeners.resetStyle()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Сбрасывает все добавленные стили.
    *   **Пример**: Вызывается при получении сообщения с событием "resetStyle".
*  **`genericListener.listeners.setStyle()`**:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Устанавливает стили на элементы.
    *   **Пример**: Вызывается при получении сообщения с событием "setStyle".
*   **`genericListener.listeners.finishInsertCss(message)`**:
    *   **Аргументы**:
        *   `message` (объект): Сообщение с CSS.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Завершает вставку CSS, обновляя стили на странице.
    *   **Пример**: Вызывается при получении сообщения с событием "finishInsertCss".
*   **`genericListener.listeners.finishRemoveCss(message)`**:
    *   **Аргументы**:
        *    `message` (объект): Сообщение с CSS.
    *   **Возвращаемое значение**: Нет.
    *   **Назначение**: Завершает удаление CSS.
    *   **Пример**: Вызывается при получении сообщения с событием "finishRemoveCss".

**Переменные**:

*   `tx`: Алиас для объекта `tryxpath`, используется для доступа к его свойствам и методам.
*   `fu`: Алиас для `tryxpath.functions`, используется для вызова функций работы с DOM и XPath.
*   `isContentLoaded`: Флаг, указывающий, загружен ли скрипт.
*   `dummyItem`: Пустая строка, используется как значение по умолчанию.
*   `dummyItems`: Пустой массив, используется как значение по умолчанию.
*   `invalidExecutionId`: `NaN`, используется как недействительный ID выполнения.
*   `styleElementHeader`: Строка, которая является заголовком для всех добавляемых CSS стилей.
*   `attributes`: Объект, содержащий атрибуты данных, которые добавляются к элементам.
*   `prevMsg`: Объект, содержащий последнее сообщение результата XPath.
*   `executionCount`: Счетчик выполненных XPath запросов.
*   `inBlankWindow`: Флаг, указывающий, выполняется ли скрипт в пустом фрейме.
*   `currentDocument`: Текущий документ, в котором выполняется скрипт (может быть фреймом).
*   `contextItem`: DOM элемент, используемый как контекст для XPath запроса.
*   `currentItems`: Массив DOM элементов, соответствующих результату XPath запроса.
*   `focusedItem`: DOM элемент, находящийся в фокусе.
*   `focusedAncestorItems`: Массив DOM элементов предков сфокусированного элемента.
*    `currentCss`: Текущий CSS, примененный к элементам.
*   `insertedStyleElements`: Map, содержащий все вставленные элементы style.
*   `expiredCssSet`: Объект, содержащий устаревшие CSS стили.
*   `originalAttributes`: Map, содержащий оригинальные атрибуты элементов, которые были изменены.

**Потенциальные ошибки и области для улучшения**:

*   **Обработка ошибок**: В коде присутствует множество блоков `try...catch`, что хорошо для надежности, но обработка ошибок довольно однообразна - сообщение отправляется в попап и текущий запрос завершается. Было бы неплохо, если бы ошибки логгировались или была какая-то более сложная обработка ошибок, нежели просто отправка сообщения.
*   **Читаемость кода**: Некоторые функции можно разбить на более мелкие, чтобы улучшить читаемость.
*   **Производительность**: Перебор всех `insertedStyleElements` для обновления стилей может быть неэффективным на больших страницах.
*   **Масштабируемость**: Код выглядит довольно сложным, можно было бы реорганизовать некоторые части, чтобы облегчить поддержку и расширение функциональности.

**Взаимосвязь с другими частями проекта**:

*   Данный скрипт является частью расширения для браузера, предположительно, `Try Xpath`.
*   Он взаимодействует с `tryxpath.functions`, предполагаемым набором функций для выполнения XPath и манипуляций с DOM.
*   Он обменивается сообщениями с popup через `browser.runtime.sendMessage`, передавая туда данные о результатах и ошибки.
*   Использует `browser.storage` для хранения атрибутов и CSS, которые влияют на поведение скрипта.
*   Взаимодействует с другими фреймами через `postMessage` для управления фокусом во фреймах.

Этот скрипт является ключевой частью расширения, поскольку он обрабатывает XPath запросы, выделяет элементы