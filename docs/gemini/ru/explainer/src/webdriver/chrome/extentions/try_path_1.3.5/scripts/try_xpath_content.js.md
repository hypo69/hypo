## <алгоритм>
### Общая схема работы скрипта `try_xpath_content.js`

1.  **Инициализация**:
    *   Проверка на множественный запуск скрипта `tx.isContentLoaded`.
    *   Определение констант, переменных (пустые массивы и строки, id для ошибок, стили для элементов, атрибуты `data-tryxpath-*`, переменные для текущих элементов, css и т.д.).
    *   Инициализация `originalAttributes` для сохранения атрибутов перед изменениями.
2.  **Функции-утилиты**:
    *   `setAttr(attr, value, item)`: Сохраняет оригинальный атрибут и устанавливает новый.
        *   Пример: `setAttr("data-tryxpath-focused", "true", element)`
    *   `setIndex(attr, items)`: Сохраняет оригинальные атрибуты и устанавливает индексы для списка элементов.
        *   Пример: `setIndex("data-tryxpath-element", [element1, element2])`
    *   `isFocusable(item)`: Проверяет, может ли элемент получить фокус.
        *   Пример: `isFocusable(element)` // true или false
    *   `focusItem(item)`: Устанавливает фокус на элемент, добавляет атрибуты, прокручивает в видимую область.
        *   Пример: `focusItem(element)`
    *   `setMainAttrs()`: Устанавливает атрибуты для текущего контекста и элементов.
        *   Пример: `setMainAttrs()`
    *   `restoreAttrs()`: Восстанавливает оригинальные атрибуты элементов.
        *   Пример: `restoreAttrs()`
    *   `resetPrev()`: Сбрасывает переменные для нового выполнения, готовит сообщение для попапа.
        *   Пример: `resetPrev()`
    *   `makeTypeStr(resultType)`: Формирует строку с типом результата XPath.
        *   Пример: `makeTypeStr(7)` // "NUMBER_TYPE(7)"
    *   `updateCss()`: Отправляет сообщение на обновление CSS, если необходимо.
    *   `getFrames(spec)`: Возвращает массив элементов frame из строки.
    *   `parseFrameDesignation(frameDesi)`: Парсит строку с индексами фреймов.
    *  `traceBlankWindows(desi, win)`: Проверяет, являются ли фреймы пустыми окнами.
    *   `handleCssChange(newCss)`: Обрабатывает изменения CSS.
    *   `findFrameByMessage(event, win)`: Находит фрейм по сообщению.
    *   `setFocusFrameListener(win, isBlankWindow)`: Устанавливает слушателя для фреймов.
    *   `initBlankWindow(win)`: Инициализирует пустые окна.
    *   `findStyleParent(doc)`: Возвращает родительский элемент для вставки стилей.
    *   `updateStyleElement(doc)`: Обновляет/вставляет стили в документ.
    *   `updateAllStyleElements()`: Обновляет стили во всех документах.
    *   `removeStyleElement(doc)`: Удаляет стили из документа.
    *   `removeAllStyleElements()`: Удаляет стили из всех документов.
    *   `createResultMessage()`: Создает шаблон сообщения для результатов.
3.  **Обработчик сообщений**:
    *   `genericListener(message, sender, sendResponse)`:
        *   Получает сообщения от расширения и обрабатывает их.
        *   Вызывает соответствующий обработчик на основе `message.event`.
    *   `genericListener.listeners` — объект с обработчиками событий.
        *   `setContentInfo(message)`: Принимает информацию об атрибутах.
        *   `execute(message, sender)`:
            *   Сбрасывает состояние.
            *   Подготавливает сообщение для попапа,  извлекает параметры из сообщения, вычисляет контекст (если есть) и элементы по xpath, и  отправляет обратно в попап, помечает элементы атрибутами.
            *   Обработка фреймов.
            *   Обновление стилей.
        *   `focusItem(message)`: Устанавливает фокус на элемент.
        *   `focusContextItem(message)`: Устанавливает фокус на контекстный элемент.
        *   `focusFrame(message)`: Передает сообщение фрейму для фокуса.
        *   `requestShowResultsInPopup()`: Отправляет последнее сообщение для отображения результатов в попапе.
        *    `requestShowAllResults()`:  Отправляет последнее сообщение для отображения всех результатов.
        *   `resetStyle()`: Восстанавливает атрибуты и удаляет стили.
        *   `setStyle()`: Применяет стили для отображения элементов.
        *   `finishInsertCss(message)`: Завершает вставку CSS.
        *   `finishRemoveCss(message)`: Завершает удаление CSS.
4.  **Слушатели событий**:
    *   `browser.storage.onChanged`: Отслеживает изменения в хранилище расширения (атрибуты, css) и обновляет соответствующие переменные.
        *   Пример: Пользователь изменил цвет подсветки элементов, это изменение применяется скриптом.
    *   `window.addEventListener("message")`: Отслеживает сообщения, отправленные из фреймов.
        *   Пример: Получено сообщение о запросе сообщения в попап при ошибке на фрейме.
5.  **Инициализация**:
    *   Создание начального сообщения для попапа `prevMsg`.
    *   Установка слушателя для фреймов `setFocusFrameListener`.
    *   Запрос начальной информации `browser.runtime.sendMessage` (например, получить `attributes`).

## <mermaid>

```mermaid
flowchart TD
    Start(Start: Initialize) --> checkContentLoaded{Is content loaded?}
    checkContentLoaded -- Yes --> End(End: Exit)
    checkContentLoaded -- No --> initVars(Initialize variables: <br> attributes, style, messages)
    initVars --> setListeners(Set up event listeners: <br>browser.runtime.onMessage, <br>browser.storage.onChanged, <br>window.addEventListener("message"))
    setListeners --> genericListener(Generic Message Listener: <br>Handle incoming messages from popup)
    genericListener -- setContentInfo --> setAttributes(Set Attributes from message)
     genericListener -- execute --> reset(Reset variables: <br>contextItem, currentItems, <br>focusedItem, etc.)
     reset --> updateCssCall(Update CSS if needed)
      updateCssCall --> prepareMessage(Prepare result message: <br>executionId, href, title)
      prepareMessage --> processFrames{Is FrameDesignation present?}
     processFrames -- Yes --> parseFrames(Parse frame designation)
     parseFrames --> traceFrames(Trace blank frames)
     traceFrames -- Success --> setContextFromFrame(Set context from frame)
     traceFrames -- Fail --> sendErrorMsg(Send error message to popup)
       setContextFromFrame --> checkContext(Check if context provided)
     processFrames -- No --> checkContext
    checkContext -- Yes --> executeContextExpr(Execute context expression)
    executionContextExpr --> handleContextResult(Handle context result)
       handleContextResult -- ContextFound --> executeMainExpr(Execute main expression)
    handleContextResult -- ContextNotFound --> sendErrorMsg
    checkContext -- No --> executeMainExpr
      executeMainExpr --> handleMainResult(Handle main result and send to popup)
    handleMainResult --> setMainAttrCall(Set attributes to items)
    setMainAttrCall --> updateStyleElementCall(Update style element)
    
    genericListener -- focusItem --> focusItemCall(Focus on item)
    genericListener -- focusContextItem --> focusContextItemCall(Focus on context item)
     genericListener -- focusFrame --> processFrameFocus(Process frame focus)
     genericListener -- requestShowResultsInPopup --> sendPrevMessage(Send previous message to popup)
     genericListener -- requestShowAllResults --> sendPrevMessageAll(Send previous message to popup all result)
     genericListener -- resetStyle --> resetStyleCall(Reset style and attributes)
     genericListener -- setStyle --> setStyleCall(Set style)
     genericListener -- finishInsertCss --> finishInsertCssCall(Finish insert css)
     genericListener -- finishRemoveCss --> finishRemoveCssCall(Finish remove css)

    sendErrorMsg --> End
    focusItemCall --> End
    focusContextItemCall --> End
    processFrameFocus --> End
    sendPrevMessage --> End
    sendPrevMessageAll --> End
    resetStyleCall --> End
     setStyleCall --> End
    finishInsertCssCall --> End
    finishRemoveCssCall --> End
    updateStyleElementCall --> End
    setAttributes --> End
   
    browser.storage.onChanged --> handleStorageChange(Handle storage change)
    handleStorageChange --> End
    window.addEventListener("message") --> handleWindowMessage(Handle window message)
    handleWindowMessage --> End
     
```

### Зависимости `mermaid`

*   **flowchart TD**:  Определяет тип диаграммы как блок-схему (flowchart) и направление сверху вниз (TD - top-down).
*   **Start(Start: Initialize)**:  Начальная точка диаграммы с именем "Start" и описанием "Initialize".
*   **checkContentLoaded{Is content loaded?}**: Логический блок (ромб) для проверки загрузки контента.
*   **initVars(Initialize variables: ...)**: Блок с описанием инициализации переменных.
*   **setListeners(Set up event listeners: ...)**: Блок с описанием установки слушателей событий.
*   **genericListener(Generic Message Listener: ...)**: Блок с описанием обработки входящих сообщений.
*   **setAttributes(Set Attributes from message)**: Блок для обработки события `setContentInfo`.
*    **reset(Reset variables: ...)**: Сбрасывает переменные для нового выполнения.
*   **updateCssCall(Update CSS if needed)**: Вызов функции для обновления CSS.
*   **prepareMessage(Prepare result message: ...)**: Подготовка сообщения с результатами.
*   **processFrames{Is FrameDesignation present?}**: Проверка на наличие информации о фреймах в сообщении.
*   **parseFrames(Parse frame designation)**: Парсинг строки с индексами фреймов.
*   **traceFrames(Trace blank frames)**: Проверка на пустые фреймы.
*   **setContextFromFrame(Set context from frame)**: Установка контекста из фрейма.
*   **sendErrorMsg(Send error message to popup)**: Отправка сообщения об ошибке в попап.
*   **checkContext(Check if context provided)**: Проверка наличия контекста.
*   **executionContextExpr(Execute context expression)**: Выполнение выражения для получения контекста.
*   **handleContextResult(Handle context result)**: Обработка результата выполнения контекстного выражения.
*    **executeMainExpr(Execute main expression)**: Выполнение основного выражения.
*    **handleMainResult(Handle main result and send to popup)**: Обработка результата выполнения основного выражения и отправка сообщения.
*   **setMainAttrCall(Set attributes to items)**: Установка атрибутов к элементам.
*   **updateStyleElementCall(Update style element)**: Обновление стилей.
*   **focusItemCall(Focus on item)**: Вызов функции для фокусировки на элементе.
*   **focusContextItemCall(Focus on context item)**: Вызов функции для фокусировки на контекстном элементе.
*    **processFrameFocus(Process frame focus)**: Обработка фокусировки на фрейме.
*   **sendPrevMessage(Send previous message to popup)**: Отправка предыдущего сообщения в попап.
*    **sendPrevMessageAll(Send previous message to popup all result)**: Отправка предыдущего сообщения в попап со всеми результатами.
*   **resetStyleCall(Reset style and attributes)**: Сброс стилей и атрибутов.
*    **setStyleCall(Set style)**: Установка стилей.
*   **finishInsertCssCall(Finish insert css)**: Завершение вставки стилей.
*    **finishRemoveCssCall(Finish remove css)**: Завершение удаления стилей.
*   **handleStorageChange(Handle storage change)**: Обработчик изменений хранилища.
*    **handleWindowMessage(Handle window message)**: Обработчик сообщений окна.
*    **End(End: Exit)**: Конечная точка диаграммы с именем "End" и описанием "Exit".
*   **-->**: Обозначает поток управления.
*   **-- Yes -->**: Поток управления при условии "да".
*   **-- No -->**: Поток управления при условии "нет".

## <объяснение>

### Импорты

В данном коде нет явных операторов `import`. Однако, есть неявные импорты, использующие глобальный объект `tryxpath`:
-   `tryxpath`: Глобальный объект, который содержит функции и свойства расширения.
-   `tryxpath.functions`: Содержит набор вспомогательных функций, используемых для манипуляции DOM, выполнения XPath выражений, работы с атрибутами элементов.

### Классы

В предоставленном коде нет явного определения классов. Однако можно выделить структуры и объекты, которые играют роль классов:

-   `originalAttributes`: `Map`, используется для хранения оригинальных атрибутов элементов перед их изменением. Позволяет восстановить исходное состояние.
-   `insertedStyleElements`: `Map`, хранит `<style>` элементы, которые вставлены в документы. Ключ - документ, значение - элемент `<style>`.
-   `expiredCssSet`: Объект, используется для отслеживания устаревших CSS стилей.
-   `genericListener.listeners`: Объект, который хранит обработчики сообщений. Можно рассматривать его как неявный класс для управления и обработки сообщений от расширения.
-   `attributes`: Объект, содержащий пары ключ-значение для атрибутов.

### Функции

-   `setAttr(attr, value, item)`:
    -   **Аргументы**:
        -   `attr` (string): Атрибут для установки.
        -   `value` (string): Значение атрибута.
        -   `item` (HTMLElement|Attr): DOM элемент или атрибут.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает атрибут на элементе, предварительно сохранив его оригинальное значение в `originalAttributes`.
    -   **Пример**: `setAttr("data-tryxpath-focused", "true", element)`.
-   `setIndex(attr, items)`:
    -   **Аргументы**:
        -   `attr` (string): Атрибут для установки.
        -   `items` (Array): Массив элементов.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает атрибут `attr` с порядковым номером для каждого элемента в массиве, сохраняя оригинальные значения.
    -   **Пример**: `setIndex("data-tryxpath-element", [element1, element2])`.
-   `isFocusable(item)`:
    -   **Аргументы**:
        -   `item` (HTMLElement|Attr|null): DOM элемент или атрибут.
    -   **Возвращаемое значение**: `boolean`.
    -   **Назначение**: Проверяет, является ли элемент фокусным.
    -   **Пример**: `isFocusable(element)` // true or false
-   `focusItem(item)`:
    -   **Аргументы**:
        -   `item` (HTMLElement|Attr): DOM элемент или атрибут.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает фокус на элемент, добавляет атрибуты и прокручивает элемент в видимую область.
    -   **Пример**: `focusItem(element)`.
-   `setMainAttrs()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает атрибуты `data-tryxpath-context` и `data-tryxpath-element` для текущих элементов.
    -   **Пример**: `setMainAttrs()`.
-   `restoreAttrs()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Восстанавливает оригинальные атрибуты элементов, используя `originalAttributes`.
    -   **Пример**: `restoreAttrs()`.
-   `resetPrev()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Сбрасывает переменные для новой итерации.
    -   **Пример**: `resetPrev()`.
-   `makeTypeStr(resultType)`:
    -   **Аргументы**:
        -   `resultType` (number): Тип результата XPath выражения.
    -   **Возвращаемое значение**: `string`.
    -   **Назначение**: Формирует строку, описывающую тип результата.
    -   **Пример**: `makeTypeStr(7)` // "NUMBER_TYPE(7)".
-    `updateCss()`:
    -    **Аргументы**: Нет.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**:  Отправляет сообщение на обновление CSS, если есть устаревшие стили.
-   `getFrames(spec)`:
    -    **Аргументы**:
        -   `spec` (string): JSON строка с индексами фреймов.
    -    **Возвращаемое значение**: `Array<HTMLFrameElement>`: Массив элементов frame.
    -    **Назначение**: Преобразует строку с индексами во фреймы.
-   `parseFrameDesignation(frameDesi)`:
    -    **Аргументы**:
        -    `frameDesi` (string):  JSON строка с индексами фреймов.
    -    **Возвращаемое значение**: `Array<number>`: Массив индексов.
    -    **Назначение**: Преобразует строку с индексами в массив чисел.
-   `traceBlankWindows(desi, win)`:
     -   **Аргументы**:
          -   `desi` (Array<number>): Массив индексов фреймов.
         -   `win` (Window): Объект окна, в котором искать фреймы.
     -   **Возвращаемое значение**: `Object`: Объект с информацией об успешности поиска и найденных окнах.
    -   **Назначение**: Проверяет, являются ли фреймы с указанными индексами пустыми окнами.
-   `handleCssChange(newCss)`:
    -   **Аргументы**:
        -   `newCss` (string): Новый CSS.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Обрабатывает изменения CSS, отслеживая устаревшие стили.
-   `findFrameByMessage(event, win)`:
    -   **Аргументы**:
        -   `event` (MessageEvent): Событие сообщения.
        -   `win` (Window): Объект окна.
    -   **Возвращаемое значение**: `HTMLFrameElement|null`.
    -   **Назначение**: Находит элемент фрейма, отправившего сообщение.
-   `setFocusFrameListener(win, isBlankWindow)`:
    -   **Аргументы**:
        -   `win` (Window): Объект окна.
        -   `isBlankWindow` (boolean): Является ли окно пустым.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает слушателя для сообщений фокуса фрейма.
-   `initBlankWindow(win)`:
    -   **Аргументы**:
        -   `win` (Window): Объект окна.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Инициализирует пустые окна.
-  `findStyleParent(doc)`:
    -  **Аргументы**:
        -   `doc` (Document): Объект документа.
    - **Возвращаемое значение**: `HTMLElement|null`.
    -   **Назначение**: Определяет родительский элемент, в который будут вставлены стили (head или body).
-   `updateStyleElement(doc)`:
    -   **Аргументы**:
        -   `doc` (Document): Объект документа.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Обновляет или вставляет стили в документ.
-   `updateAllStyleElements()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Обновляет стили во всех документах.
-   `removeStyleElement(doc)`:
    -   **Аргументы**:
        -   `doc` (Document): Объект документа.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Удаляет элемент стиля из документа.
-    `removeAllStyleElements()`:
    -    **Аргументы**: Нет.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Удаляет все элементы стилей из всех документов.
-   `createResultMessage()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `object`
    -   **Назначение**: Создает шаблон сообщения для результатов.
-   `genericListener(message, sender, sendResponse)`:
    -   **Аргументы**:
        -   `message` (object): Сообщение от расширения.
        -   `sender` (object): Информация об отправителе сообщения.
        -   `sendResponse` (function): Функция для отправки ответа.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Основной обработчик сообщений от расширения, вызывает соответствующий обработчик в `genericListener.listeners`.
-  `genericListener.listeners.setContentInfo(message)`:
    -   **Аргументы**:
        -   `message` (object): Сообщение от расширения.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Принимает информацию об атрибутах, которые необходимо установить.
-   `genericListener.listeners.execute(message, sender)`:
    -   **Аргументы**:
        -   `message` (object): Сообщение от расширения с параметрами выполнения.
        -   `sender` (object): Информация об отправителе сообщения.
    -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Выполняет XPath запрос и отправляет результаты в попап.
-  `genericListener.listeners.focusItem(message)`:
     -   **Аргументы**:
         -   `message` (object): Сообщение от расширения.
     -   **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает фокус на элемент.
-   `genericListener.listeners.focusContextItem(message)`:
     -   **Аргументы**:
         -   `message` (object): Сообщение от расширения.
    -    **Возвращаемое значение**: `undefined`.
    -   **Назначение**: Устанавливает фокус на контекстный элемент.
-  `genericListener.listeners.focusFrame(message)`:
    -    **Аргументы**:
        -   `message` (object): Сообщение от расширения.
    -   **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Фокусируется на фрейме.
-  `genericListener.listeners.requestShowResultsInPopup()`:
    -    **Аргументы**: Нет.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Отправляет предыдущее сообщение в попап для отображения результатов.
-   `genericListener.listeners.requestShowAllResults()`:
    -    **Аргументы**: Нет.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Отправляет предыдущее сообщение в попап для отображения всех результатов.
-   `genericListener.listeners.resetStyle()`:
     -   **Аргументы**: Нет.
     -   **Возвращаемое значение**: `undefined`.
     -   **Назначение**: Сбрасывает стили и атрибуты, восстанавливая исходное состояние.
-   `genericListener.listeners.setStyle()`:
    -    **Аргументы**: Нет.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Устанавливает стили для отображения элементов.
-   `genericListener.listeners.finishInsertCss(message)`:
    -    **Аргументы**:
        -    `message` (object): Сообщение от расширения с CSS.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Завершает вставку CSS, обновляя стили.
-  `genericListener.listeners.finishRemoveCss(message)`:
    -    **Аргументы**:
        -    `message` (object): Сообщение от расширения с CSS.
    -    **Возвращаемое значение**: `undefined`.
    -    **Назначение**: Завершает удаление CSS, убирая устаревший CSS.

### Переменные

*   `tx`: Ссылка на `tryxpath`.
*    `fu`: Ссылка на `tryxpath.functions`.
*   `isContentLoaded`: Флаг, который предотвращает многократное выполнение скрипта.
*   `dummyItem`: Пустая строка, используется как значение по умолчанию.
*   `dummyItems`: Пустой массив, используется как значение по умолчанию.
*   `invalidExecutionId`: `NaN`, используется для идентификации некорректных запросов.
*   `styleElementHeader`: Строка,  содержит комментарий, который вставляется в начало CSS.
*   `attributes`: Объект, содержит атрибуты для элементов.
*   `prevMsg`: Последнее сообщение от скрипта в попап.
*   `executionCount`: Счетчик выполненных запросов.
*   `inBlankWindow`: Флаг, определяющий, находится ли скрипт в пустом окне.
*   `currentDocument`: Текущий документ (в контексте фрейма).
*    `contextItem`: Текущий контекстный элемент.
*    `currentItems`: Текущий массив элементов.
*    `focusedItem`: Элемент, на котором установлен фокус.
*   `focusedAncestorItems`:  Массив родительских элементов `focusedItem`.
*   `currentCss`: Текущий CSS, применяемый к элементам.
*    `insertedStyleElements`:  Карта, которая хранит все добавленные `<style>` элементы.
*   `expiredCssSet`: Объект,  хранит устаревшие css.
*   `originalAttributes`: Карта,  хранит оригинальные атрибуты элементов.

### Потенциальные ошибки и области для улучшения

1.  **Обработка ошибок фреймов**:  Код обрабатывает ошибки при работе с фреймами, отправляя сообщения в попап, но можно сделать обработку ошибок более гранулированной.
2.  **Сообщения об ошибках**: Текст ошибок часто передаётся непосредственно в `sendMsg.message`. Для улучшения читаемости и поддержки можно вынести эти сообщения в отдельный объект или константы.
3.  **Работа со стилями**:  Работа со стилями выполняется с помощью прямого манипулирования `textContent`. Можно использовать `CSSStyleSheet` API для более эффективной и безопасной работы со стилями.
4.  **Управление памятью**:   Управление `originalAttributes` и `insertedStyleElements` с помощью `Map` эффективно, но стоит дополнительно рассмотреть возможность очистки, когда это необходимо.
5.  **Использование `Object.create(null)`**:  Использование `Object.create(null)` уместно, но нужно помнить, что это создает объекты без прототипов, и поэтому некоторые методы (вроде `hasOwnProperty`) могут быть недоступны.

### Цепочка взаимосвязей с другими частями проекта

1.  **`tryxpath.functions`**: Скрипт зависит от функций, определенных в `tryxpath.functions`, для DOM манипуляций, XPath выражений и работы с атрибутами.
2.  **Расширение браузера**: Скрипт взаимодействует с расширением через `browser.runtime.onMessage` и `browser.runtime.sendMessage`. Это позволяет расширению запускать скрипт, передавать параметры и получать результаты.
3.  **Хранилище расширения**: Скрипт отслеживает изменения в хранилище расширения через `browser.storage.onChanged` для обновления атрибутов и CSS.
4.  **HTML-страница**: Скрипт непосредственно манипулирует DOM HTML-страницы.
5.  **Фреймы**: Скрипт поддерживает взаимодействие со фреймами, обрабатывая сообщения и передавая управление.

В целом, этот скрипт является ключевым компонентом расширения, который позволяет пользователю взаимодействовать со страницей, используя XPath, и отображать результаты в удобном виде.