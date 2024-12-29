## Анализ кода `try_xpath_content.js`

### 1. <алгоритм>

1. **Инициализация**:
   - При запуске скрипт проверяет, был ли он уже загружен (`tx.isContentLoaded`). Если да, то выполнение прекращается.
   - Инициализируются константы, переменные для хранения состояния, атрибутов и стилей.
   - Создаются пустые коллекции и переменные для хранения элементов, фокуса, стилей и атрибутов.
   
   _Пример_:
   ```javascript
    const dummyItem = "";
    const dummyItems = [];
    var executionCount = 0;
    var currentCss = null;
    var insertedStyleElements = new Map();
    var originalAttributes = new Map();
   ```
   
2. **Функции для работы с атрибутами**:
    - `setAttr(attr, value, item)`: Сохраняет исходный атрибут элемента и устанавливает новый атрибут `value`.
    - `setIndex(attr, items)`: Сохраняет исходные атрибуты элементов и устанавливает им порядковые номера.
    
    _Пример_:
    ```javascript
    // Вызов
    setAttr("data-test", "test_value", element);
    setIndex("data-index", [element1, element2]);
    //Результат
    //element.getAttribute("data-test") == "test_value";
    //element1.getAttribute("data-index") == "0";
    //element2.getAttribute("data-index") == "1";
    ```

3. **Функции для работы с фокусом**:
    - `isFocusable(item)`: Проверяет, может ли элемент получить фокус.
    - `focusItem(item)`: Устанавливает фокус на элемент, добавляя соответствующие атрибуты для подсветки, и скролит к нему.
    
   _Пример_:
   ```javascript
   // Вызов
   focusItem(element);
   // Результат:
   // Элемент element получает фокус, добавляется атрибут data-tryxpath-focused и подсвечивается.
   ```

4. **Управление стилями**:
    - `updateCss()`: Отправляет запрос на обновление CSS, если он изменился.
    - `updateStyleElement(doc)`: Обновляет (или создаёт) тег `<style>` в документе, устанавливая туда текущие стили.
    - `updateAllStyleElements()`: Обновляет стили во всех отслеживаемых документах.
    - `removeStyleElement(doc)`: Удаляет тег `<style>` из документа.
    - `removeAllStyleElements()`: Удаляет все теги `<style>`.
    - `handleCssChange(newCss)`: Обрабатывает изменение CSS, запоминая предыдущий CSS.
    
    _Пример_:
    ```javascript
     // Вызов
      handleCssChange(".test { color: red; }");
      updateStyleElement(document);
     //Результат
     // В document будет добавлен style тег с контентом:
     /* This style element was inserted by browser add-on, Try xpath. If you want to remove this element, please click the reset style button in the popup. */
     // .test { color: red; }
    ```

5. **Работа с окнами и фреймами**:
    - `getFrames(spec)`: Получает фреймы на основе JSON-спецификации.
    - `parseFrameDesignation(frameDesi)`: Извлекает массив индексов фреймов из JSON-спецификации.
    - `traceBlankWindows(desi, win)`: Проверяет, являются ли фреймы пустыми окнами.
    - `findFrameByMessage(event, win)`: Определяет фрейм на основе сообщения.
    - `setFocusFrameListener(win, isBlankWindow)`: Настраивает слушателя сообщений для фреймов.
    - `initBlankWindow(win)`: Инициализирует пустые окна.
    
   _Пример_:
   ```javascript
   //вызов
    traceBlankWindows([0, 1], window);
    //результат
    // {success: true, windows: [window.frames[0], window.frames[0].frames[1]]}
   ```

6. **Обработка сообщений**:
    - `genericListener(message, sender, sendResponse)`: Главный слушатель сообщений от расширения.
    -  `genericListener.listeners.setContentInfo`: Устанавливает атрибуты.
    - `genericListener.listeners.execute`: Выполняет XPath, устанавливает контекст, и отправляет результаты.
    -  `genericListener.listeners.focusItem`: Устанавливает фокус на элемент из результатов.
    - `genericListener.listeners.focusContextItem`: Устанавливает фокус на контекстный элемент.
    - `genericListener.listeners.focusFrame`: Переключает фокус на фрейм.
    -  `genericListener.listeners.requestShowResultsInPopup`: Отправляет сообщение с последними результатами.
    - `genericListener.listeners.requestShowAllResults`: Отправляет сообщение с последними результатами, для показа в popup.
    - `genericListener.listeners.resetStyle`: Сбрасывает стили и атрибуты.
    - `genericListener.listeners.setStyle`: Обновляет стили, сохраняя атрибуты.
    -  `genericListener.listeners.finishInsertCss`: Завершает вставку CSS.
    - `genericListener.listeners.finishRemoveCss`: Завершает удаление CSS.
    
    _Пример_:
    ```javascript
     //Вызов из popup
     browser.runtime.sendMessage({
      "event": "execute",
      "main": {
          "method": "evaluate",
          "expression": "//body",
          "resultType": 4
      }
    })
     //Результат:
     // Скрипт выполнит xpath, подсветит результат.
    ```

7. **Слушатели**:
    - `browser.storage.onChanged.addListener`: Отслеживает изменения в хранилище для обновления настроек.
    - `window.addEventListener("message")`: Обрабатывает сообщения от фреймов.

8. **Инициализация**:
   - Запрашивает начальные настройки из background скрипта.
   - Устанавливает слушателя для фреймов.
   
   _Пример_:
   ```javascript
    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });
    setFocusFrameListener(window, false);
   ```

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Start] --> CheckContentLoaded{Check if Content Loaded}
    CheckContentLoaded -- Yes --> Stop[Stop]
    CheckContentLoaded -- No --> InitVariables[Initialize Variables]
    InitVariables --> SetFunctions[Set Attribute Functions]
    SetFunctions --> SetFocusFunctions[Set Focus Functions]
    SetFocusFunctions --> SetStyleFunctions[Set Style Functions]
    SetStyleFunctions --> SetFrameFunctions[Set Frame Functions]
    SetFrameFunctions --> SetMessageFunctions[Set Message Listener Functions]
    SetMessageFunctions --> SetListeners[Set Event Listeners]
    SetListeners --> RequestContentInfo[Request Content Info from Background]
     RequestContentInfo --> End[End]
    
    subgraph Attribute Functions
    SetFunctions --> setAttr[<code>setAttr(attr, value, item)</code><br>Save attr and Set attr]
     SetFunctions --> setIndex[<code>setIndex(attr, items)</code><br>Save attr and Set index]
    end
     
    subgraph Focus Functions
    SetFocusFunctions --> isFocusable[<code>isFocusable(item)</code><br>Check item focusable]
      SetFocusFunctions --> focusItem[<code>focusItem(item)</code><br>Set focus to item]
    end

    subgraph Style Functions
     SetStyleFunctions --> updateCss[<code>updateCss()</code><br>Send request to update css]
    SetStyleFunctions --> updateStyleElement[<code>updateStyleElement(doc)</code><br>Update or create style tag]
    SetStyleFunctions --> updateAllStyleElements[<code>updateAllStyleElements()</code><br>Update all style tags]
    SetStyleFunctions --> removeStyleElement[<code>removeStyleElement(doc)</code><br>Remove style tag]
    SetStyleFunctions --> removeAllStyleElements[<code>removeAllStyleElements()</code><br>Remove all style tags]
      SetStyleFunctions --> handleCssChange[<code>handleCssChange(newCss)</code><br>Handle css change]
    end

    subgraph Frame Functions
      SetFrameFunctions --> getFrames[<code>getFrames(spec)</code><br>Get frames by spec]
    SetFrameFunctions --> parseFrameDesignation[<code>parseFrameDesignation(frameDesi)</code><br>Parse frame designation]
     SetFrameFunctions --> traceBlankWindows[<code>traceBlankWindows(desi, win)</code><br>Check if frames are blank windows]
    SetFrameFunctions --> findFrameByMessage[<code>findFrameByMessage(event, win)</code><br>Find frame by message]
     SetFrameFunctions --> setFocusFrameListener[<code>setFocusFrameListener(win, isBlankWindow)</code><br>Set listener for frame]
     SetFrameFunctions --> initBlankWindow[<code>initBlankWindow(win)</code><br>Init blank window]
    end
    
    subgraph Message Listener Functions
        SetMessageFunctions --> genericListener[<code>genericListener(message, sender, sendResponse)</code><br>Message listener]
        genericListener --> setContentInfo[<code>setContentInfo(message)</code><br>Set attributes]
        genericListener --> execute[<code>execute(message, sender)</code><br>Execute xpath, set context and send results]
        genericListener --> focusItemListener[<code>focusItem(message)</code><br>Set focus to item]
         genericListener --> focusContextItemListener[<code>focusContextItem(message)</code><br>Set focus to context item]
        genericListener --> focusFrameListener[<code>focusFrame(message)</code><br>Switch focus to frame]
        genericListener --> requestShowResultsInPopup[<code>requestShowResultsInPopup()</code><br>Send last results]
          genericListener --> requestShowAllResults[<code>requestShowAllResults()</code><br>Send last results for popup]
         genericListener --> resetStyle[<code>resetStyle()</code><br>Reset styles and attributes]
        genericListener --> setStyle[<code>setStyle()</code><br>Update styles, keep attributes]
        genericListener --> finishInsertCss[<code>finishInsertCss(message)</code><br>Finish insert css]
        genericListener --> finishRemoveCss[<code>finishRemoveCss(message)</code><br>Finish remove css]
        
    end
  
  subgraph Event Listeners
      SetListeners --> storageChangeListener[<code>browser.storage.onChanged.addListener</code><br>Storage change listener]
       SetListeners --> windowMessageListener[<code>window.addEventListener("message")</code><br>Frame message listener]
  end
  
```

**Зависимости:**

- **`browser.runtime`**: Используется для отправки и получения сообщений от расширения.
- **`window`**: Используется для доступа к текущему окну и его свойствам, а также для добавления слушателей событий.
- **`document`**: Используется для доступа к текущему документу и манипулирования DOM.
- **`tryxpath`**: Объект, содержащий основные функции и состояния скрипта.
-  **`tryxpath.functions`**: Объект, содержащий функции для работы с элементами и XPath.
-  **`browser.storage`**: Используется для отслеживания изменений в хранилище.

### 3. <объяснение>

**Импорты**:

-   В коде нет явных импортов с использованием `import` или `require`. Код предполагает, что `tryxpath` и `tryxpath.functions` уже существуют в области видимости (например, определены в другом скрипте, который выполняется раньше,  или через  заранее добавленный тег `script`).

**Классы**:

-   В коде нет классов. Вся функциональность реализована через функции и объекты.
    
**Функции**:

-   `setAttr(attr, value, item)`:
    -   **Аргументы**: `attr` (строка, имя атрибута), `value` (строка, значение атрибута), `item` (элемент DOM или объект).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Сохраняет старое значение атрибута и устанавливает новое значение на элемент.
    -   **Пример**: `setAttr("data-test", "test_value", element);`
-   `setIndex(attr, items)`:
    -   **Аргументы**: `attr` (строка, имя атрибута), `items` (массив элементов DOM).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Сохраняет старые значения атрибутов и устанавливает порядковый номер для каждого элемента.
    -   **Пример**: `setIndex("data-index", [element1, element2]);`
-   `isFocusable(item)`:
    -   **Аргументы**: `item` (элемент DOM или объект).
    -   **Возвращаемое значение**: `true` если элемент может получить фокус, `false` в противном случае.
    -   **Назначение**: Проверяет, может ли элемент получить фокус.
    -   **Пример**: `isFocusable(element);`
-   `focusItem(item)`:
    -   **Аргументы**: `item` (элемент DOM или объект).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Устанавливает фокус на элемент, подсвечивая его и его предков.
    -   **Пример**: `focusItem(element);`
-   `setMainAttrs()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Устанавливает атрибуты для контекстного элемента и текущих элементов.
    -   **Пример**: `setMainAttrs();`
-   `restoreAttrs()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Восстанавливает исходные атрибуты элементов.
    -   **Пример**: `restoreAttrs();`
-   `resetPrev()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Сбрасывает переменные состояния и увеличивает счетчик выполнения.
    -   **Пример**: `resetPrev();`
-    `makeTypeStr(resultType)`:
    -   **Аргументы**: `resultType` (число или любой тип).
    -   **Возвращаемое значение**: Строка.
    -   **Назначение**: Создает строку с типом результата XPath.
    -   **Пример**: `makeTypeStr(4);`
-    `updateCss()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Отправляет сообщение для обновления CSS.
    -   **Пример**: `updateCss();`
-   `getFrames(spec)`:
    -   **Аргументы**: `spec` (строка, JSON-представление массива индексов фреймов).
    -   **Возвращаемое значение**: Массив фреймов.
    -   **Назначение**: Получает массив фреймов на основе JSON-спецификации.
    -   **Пример**: `getFrames("[0,1]");`
-   `parseFrameDesignation(frameDesi)`:
    -   **Аргументы**: `frameDesi` (строка, JSON-представление массива индексов фреймов).
    -   **Возвращаемое значение**: Массив индексов фреймов.
    -   **Назначение**: Извлекает массив индексов фреймов из JSON-спецификации.
    -   **Пример**: `parseFrameDesignation("[0,1]");`
-   `traceBlankWindows(desi, win)`:
    -   **Аргументы**: `desi` (массив индексов фреймов), `win` (окно).
    -   **Возвращаемое значение**: Объект с информацией об успехе и окнах.
    -   **Назначение**: Проверяет, являются ли фреймы пустыми окнами.
    -   **Пример**: `traceBlankWindows([0, 1], window);`
-   `handleCssChange(newCss)`:
    -   **Аргументы**: `newCss` (строка, новый CSS).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Обрабатывает изменения в CSS, управляет `currentCss` и `expiredCssSet`.
    -   **Пример**: `handleCssChange(".test { color: red; }");`
-   `findFrameByMessage(event, win)`:
    -   **Аргументы**: `event` (событие сообщения), `win` (окно).
    -   **Возвращаемое значение**: Фрейм или `null`.
    -   **Назначение**: Определяет фрейм на основе сообщения.
    -   **Пример**: `findFrameByMessage(event, window);`
-   `setFocusFrameListener(win, isBlankWindow)`:
    -   **Аргументы**: `win` (окно), `isBlankWindow` (логическое значение).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Устанавливает слушатель сообщений для фокуса на фрейм.
    -   **Пример**: `setFocusFrameListener(window, false);`
-   `initBlankWindow(win)`:
    -   **Аргументы**: `win` (окно).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Инициализирует пустое окно.
    -   **Пример**: `initBlankWindow(window.frames[0]);`
-   `findStyleParent(doc)`:
    -   **Аргументы**: `doc` (документ).
    -   **Возвращаемое значение**: Элемент `head` или `body`, или `null`.
    -   **Назначение**: Определяет родительский элемент для вставки тега `<style>`.
    -   **Пример**: `findStyleParent(document);`
-   `updateStyleElement(doc)`:
    -   **Аргументы**: `doc` (документ).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Обновляет или создает тег `<style>` с текущим CSS.
    -   **Пример**: `updateStyleElement(document);`
-   `updateAllStyleElements()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Обновляет стили во всех отслеживаемых документах.
    -   **Пример**: `updateAllStyleElements();`
-   `removeStyleElement(doc)`:
    -   **Аргументы**: `doc` (документ).
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Удаляет тег `<style>` из документа.
    -   **Пример**: `removeStyleElement(document);`
-   `removeAllStyleElements()`:
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Назначение**: Удаляет все теги `<style>`.
    -   **Пример**: `removeAllStyleElements();`
-    `createResultMessage()`:
     -   **Аргументы**: Нет.
     -   **Возвращаемое значение**: Объект сообщения.
     -   **Назначение**: Создает объект сообщения с дефолтными значениями.
     -   **Пример**: `createResultMessage();`
-   `genericListener(message, sender, sendResponse)`:
    -   **Аргументы**: `message` (сообщение от расширения), `sender` (информация об отправителе), `sendResponse` (функция для ответа).
    -   **Возвращаемое значение**: Результат обработки сообщения (может быть `undefined`, `true`, или любой другой тип).
    -   **Назначение**: Главный слушатель сообщений от расширения, делегирует обработку соответствующим функциям.
    -   **Пример**: `genericListener(message, sender, sendResponse);`

**Переменные**:

-   `tx`: Псевдоним для `tryxpath`.
-   `fu`: Псевдоним для `tryxpath.functions`.
-   `isContentLoaded`: Флаг, указывающий, загружен ли скрипт.
-   `dummyItem`: Пустая строка, используемая как значение по умолчанию.
-   `dummyItems`: Пустой массив, используемый как значение по умолчанию.
-   `invalidExecutionId`: Специальное значение `NaN` для некорректного id выполнения.
-   `styleElementHeader`: Заголовок для тегов `<style>`.
-    `attributes`: Объект, который содержит имена атрибутов.
-   `prevMsg`: Сообщение, отправленное в popup последним.
-   `executionCount`: Счетчик выполнения XPath.
-   `inBlankWindow`: Флаг, указывающий, выполняется ли скрипт в пустом окне.
-   `currentDocument`: Ссылка на текущий документ.
-   `contextItem`: Контекстный элемент для XPath.
-   `currentItems`: Массив элементов, полученных в результате XPath.
-   `focusedItem`: Элемент, на котором установлен фокус.
-   `focusedAncestorItems`: Массив предков элемента, на котором установлен фокус.
-   `currentCss`: Текущий CSS.
-   `insertedStyleElements`: Коллекция тегов `<style>`.
-   `expiredCssSet`: Набор устаревших CSS.
-   `originalAttributes`: Коллекция сохраненных исходных атрибутов.

**Потенциальные ошибки и области для улучшения**:

-   **Зависимость от `tryxpath`**: Код не обрабатывает ситуацию, когда `tryxpath` или `tryxpath.functions` не определены.
-   **Глобальные переменные**: Использование глобальных переменных может привести к конфликтам.
-   **Обработка ошибок**: Не все возможные ошибки обрабатываются явно.
-   **Производительность**:  Возможно, есть области, где можно оптимизировать работу с DOM.
-  **Расширение `tryxpath.functions`**:  Код зависит от наличия `tryxpath.functions` и конкретных методов в нем, которые не определены явно в данном файле, это создает риск несовместимости.

**Взаимосвязь с другими частями проекта**:

-   **`background.js`**:
    -   Отправляет сообщения для управления стилями и выполнением XPath.
    -   Отслеживает изменения в хранилище и отправляет обновления в `content.js`.
-   **`popup.js`**:
    -   Отправляет сообщения для выполнения XPath и управления стилями.
    -   Получает результаты и отображает их.
-  **`tryxpath.functions`**:
    -   Предоставляет функции для выполнения XPath, манипулирования элементами.
    -    Обеспечивает основную логику для нахождения, выделения, работы с атрибутами и стилями.

Этот скрипт является связующим звеном между расширением и веб-страницей. Он обрабатывает команды от расширения, взаимодействует с DOM, и возвращает результаты для отображения.