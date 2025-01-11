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

**1. Инициализация и Настройка:**
   -   При загрузке страницы (событие `window.addEventListener("load", ...)`):
        -   Получаем ссылки на DOM элементы input для атрибутов (`element-attribute`, `context-attribute` и т.д.) и стилей (`style`, `popup-body-width`, `popup-body-height`).
        -   Получаем ссылку на элемент для отображения сообщений (`message`).
        -   Отправляем сообщение в фоновый скрипт (`browser.runtime.sendMessage`) для запроса текущих настроек.
   -  **Пример**: DOM элементы (inputs) со значениями: `element-attribute = "data-tryxpath-element"`, `style = "body {color: red;}"`

**2. Получение и отображение сохраненных настроек:**
   -   Когда приходит ответ от фонового скрипта:
        -   Заполняем поля ввода значениями из ответа (атрибуты, CSS, стили popup).
        -   Вызываем `extractBodyStyles` для извлечения ширины и высоты popup из CSS.
   -   **Пример**: response от `browser.runtime.sendMessage` `{attributes: {element: "data-element", ...}, css: "body{color:black}", popupCss: "body{width:300px; height:auto;}"}`. В итоге поля input  заполняются этими значениями, а  `popupBodyWidth` = "300px", `popupBodyHeight` = "auto".

**3. Сохранение настроек:**
   -   При клике на кнопку "Save" (событие `document.getElementById("save").addEventListener("click", ...)`):
        -   Считываем значения полей ввода (атрибуты, стили, ширина и высота popup).
        -   Создаем объект `attrs` со значениями атрибутов.
        -   Создаем объект `bodyStyles` со значениями ширины и высоты.
        -   Проверяем валидность имен атрибутов с помощью `isValidAttrNames`.
        -   Проверяем валидность стилей ширины и высоты с помощью `isValidStyleLength`.
        -   Если все валидно:
            -   Создаем CSS строку для popup с помощью `createPopupCss`.
            -   Сохраняем настройки в хранилище (`browser.storage.sync.set`).
            -   Выводим сообщение об успешном сохранении.
        -   Если есть ошибки, выводим сообщение об ошибке.
   -   **Пример**: Пользователь меняет `element-attribute` на "my-element"  и нажимает "save". Происходит проверка валидности,  и если валидно, `browser.storage.sync.set` сохраняет обновленный `attrs` и CSS.

**4. Сброс настроек к умолчанию:**
   -   При клике на кнопку "Show Default" (событие `document.getElementById("show-default").addEventListener("click", ...)`):
        -   Устанавливаем значения полей ввода в значения по умолчанию (атрибуты).
        -   Загружаем CSS по умолчанию с помощью `loadDefaultCss` и устанавливаем его в поле `style`.
        -   Устанавливаем значения ширины и высоты popup в значения по умолчанию.
   -   **Пример**: Пользователь нажимает "Show Default". Значения атрибутов  сбрасываются в дефолтные (`data-tryxpath-element` и т.д.), `style`  обновляется, `popupBodyWidth` = "367px", `popupBodyHeight` = "auto".

**5. Вспомогательные функции:**
    -  `isValidAttrName(name)`: Проверяет, является ли `name` валидным именем атрибута, устанавливая его на тестовый элемент.
    - `isValidAttrNames(names)`: Проверяет, являются ли все имена атрибутов в `names` валидными.
    - `isValidStyleLength(len)`: Проверяет, является ли `len` валидной длиной стиля (например, "auto" или "100px").
    - `loadDefaultCss()`: Загружает CSS из файла `/css/try_xpath_insert.css`.
    - `extractBodyStyles(css)`: Извлекает значения ширины и высоты из CSS строки.
    - `createPopupCss(bodyStyles)`: Создает CSS строку для popup на основе объекта `bodyStyles`.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало: window.addEventListener("load")] --> GetElements[Получение DOM элементов (input, message)];
    GetElements --> SendMessage[Отправка сообщения в фоновый скрипт (loadOptions)];
    SendMessage --> Response[Получение ответа с настройками];
    Response --> FillInputs[Заполнение полей ввода значениями из ответа];
    Response --> ExtractStyles[Извлечение стилей popup из CSS];
    ExtractStyles --> FillPopupStyle[Заполнение полей ввода стилей popup (ширина, высота)];
    FillInputs --> WaitSaveClick[Ожидание клика на кнопку "Save"];
    WaitSaveClick --> SaveClick[Клик на кнопку "Save"];
    SaveClick --> GetInputValues[Считывание значений из полей ввода];
    GetInputValues --> ValidateAttrs[Проверка валидности атрибутов (isValidAttrNames)];
     ValidateAttrs -- invalid --> ShowInvalidAttrMessage[Вывод сообщения об ошибке с атрибутами];
     ValidateAttrs -- valid --> ValidateStyles[Проверка валидности стилей (isValidStyleLength)];
     ValidateStyles -- invalid --> ShowInvalidStyleMessage[Вывод сообщения об ошибке со стилями];
      ValidateStyles -- valid --> CreatePopupCss[Создание CSS для popup (createPopupCss)];
     CreatePopupCss --> SaveSettings[Сохранение настроек в хранилище (browser.storage.sync.set)];
    SaveSettings --> ShowSuccessMessage[Вывод сообщения об успехе];
    ShowSuccessMessage --> EndSave[Завершение: Сохранение настроек];
    ShowInvalidAttrMessage --> EndSave;
    ShowInvalidStyleMessage --> EndSave;
    Response --> WaitDefaultClick[Ожидание клика на кнопку "Show Default"];
    WaitDefaultClick --> DefaultClick[Клик на кнопку "Show Default"];
    DefaultClick --> SetDefaultValues[Установка значений по умолчанию для полей ввода];
    DefaultClick --> LoadDefaultCss[Загрузка CSS по умолчанию (loadDefaultCss)];
    LoadDefaultCss --> SetStyleValue[Установка значения CSS в поле style];
    SetDefaultValues -->  SetDefaultPopupStyle[Установка значений ширины и высоты popup по умолчанию];
     SetDefaultPopupStyle --> EndDefault[Завершение: Сброс настроек к умолчанию];
    EndSave --> End;
    EndDefault --> End;
    
    subgraph isValidAttrName
        direction LR
        isValidAttrNameStart[Начало: isValidAttrName] --> SetTestAttr[Установка тестового атрибута на testElement];
        SetTestAttr --> CatchError{Возникла ли ошибка?};
        CatchError -- Да --> isValidAttrNameFalse[Возврат false];
        CatchError -- Нет --> isValidAttrNameTrue[Возврат true];
        isValidAttrNameFalse --> isValidAttrNameEnd[Конец isValidAttrName]
        isValidAttrNameTrue --> isValidAttrNameEnd
    end

    subgraph isValidAttrNames
         direction LR
          isValidAttrNamesStart[Начало: isValidAttrNames] --> LoopAttrNames[Цикл по атрибутам];
          LoopAttrNames --> CallValidAttrName[Вызов isValidAttrName];
        CallValidAttrName -->  CheckValidResult{Результат isValidAttrName == false?};
         CheckValidResult -- Да --> isValidAttrNamesFalse[Возврат false];
          CheckValidResult -- Нет --> CheckNextAttr{Следующий атрибут?};
          CheckNextAttr -- Да --> LoopAttrNames;
          CheckNextAttr -- Нет --> isValidAttrNamesTrue[Возврат true];
        isValidAttrNamesFalse -->  isValidAttrNamesEnd[Конец isValidAttrNames];
         isValidAttrNamesTrue -->  isValidAttrNamesEnd;
    end
  
    subgraph isValidStyleLength
        direction LR
        isValidStyleLengthStart[Начало: isValidStyleLength] --> CheckStyleLength[Проверка длины стиля (регулярное выражение)];
          CheckStyleLength -- valid --> isValidStyleLengthTrue[Возврат true];
           CheckStyleLength -- invalid --> isValidStyleLengthFalse[Возврат false];
         isValidStyleLengthTrue -->  isValidStyleLengthEnd[Конец isValidStyleLength];
        isValidStyleLengthFalse -->  isValidStyleLengthEnd;
    end
    
    subgraph loadDefaultCss
        direction LR
        loadDefaultCssStart[Начало: loadDefaultCss] --> CreateRequest[Создание XMLHttpRequest];
        CreateRequest --> OpenRequest[Открытие запроса на css файл];
        OpenRequest --> SetResponseType[Установка типа ответа text];
        SetResponseType --> onReadyStateChange[Событие onreadystatechange];
        onReadyStateChange --> CheckReadyState{readyState === DONE?};
        CheckReadyState -- Да --> ResolveWithResponse[Разрешение промиса с текстом css];
        CheckReadyState -- Нет --> onReadyStateChange;
        ResolveWithResponse --> loadDefaultCssEnd[Конец loadDefaultCss];
    end
    
    subgraph extractBodyStyles
        direction LR
        extractBodyStylesStart[Начало: extractBodyStyles] -->  ExtractStyleFromCss[Извлечение ширины и высоты из CSS (регулярное выражение)];
        ExtractStyleFromCss --> checkResult{Результат найден?};
         checkResult -- Да --> SetWidthAndHeight[Установка width и height в styles];
         checkResult -- Нет --> SetEmptyStyles[Установка width и height в пустые строки];
          SetWidthAndHeight --> extractBodyStylesEnd[Конец extractBodyStyles];
          SetEmptyStyles --> extractBodyStylesEnd;
    end

    subgraph createPopupCss
       direction LR
         createPopupCssStart[Начало: createPopupCss] --> CreateCssString[Создание css строки с width и height];
        CreateCssString --> createPopupCssEnd[Конец createPopupCss];
     end
```

**Объяснение зависимостей `mermaid`:**
-   `Start` (window.addEventListener("load")):  Основная точка входа, откуда начинается выполнение скрипта после загрузки страницы.
-   `GetElements`: Получает ссылки на DOM-элементы input и message, необходимые для управления настройками.
-    `SendMessage`: Отправляет запрос к background скрипту для получения сохраненных ранее настроек
-   `Response`: Получает объект ответа с настройками из фонового скрипта.
-    `FillInputs`: Заполняет поля ввода значениями, полученными из ответа, что отображает текущие настройки.
-    `ExtractStyles`: Извлекает значения `width` и `height` из строки CSS, что позволяет использовать их для настройки popup.
-    `FillPopupStyle`: Заполняет поля для редактирования ширины и высоты popup.
-   `WaitSaveClick`: Ожидает клика на кнопке "Save" для сохранения новых настроек.
-   `SaveClick`: Запускает процесс сохранения настроек.
-   `GetInputValues`: Считывает значения, введенные пользователем, из полей ввода.
-   `ValidateAttrs`:  Проверяет имена атрибутов на валидность с помощью функции `isValidAttrNames`.
-    `ShowInvalidAttrMessage`: Выводит сообщение об ошибке при не валидных именах атрибутов.
-   `ValidateStyles`:  Проверяет длину стилей с помощью функции `isValidStyleLength` на валидность.
-  `ShowInvalidStyleMessage`: Выводит сообщение об ошибке при невалидных значениях стилей.
-   `CreatePopupCss`: Создает CSS строку для popup, используя ширину и высоту, что важно для правильного отображения popup.
-   `SaveSettings`: Сохраняет новые настройки в браузере, используя `browser.storage.sync.set`.
-   `ShowSuccessMessage`:  Отображает сообщение об успешном сохранении настроек, информируя пользователя о результатах.
-    `EndSave`: Конечная точка процесса сохранения настроек.
-  `WaitDefaultClick`: Ожидает клика на кнопке "Show Default".
-   `DefaultClick`: Начинает процесс сброса настроек к значениям по умолчанию.
-  `SetDefaultValues`: Сбрасывает значения полей ввода атрибутов к значениям по умолчанию.
-   `LoadDefaultCss`: Загружает CSS по умолчанию, используя функцию `loadDefaultCss`.
-   `SetStyleValue`: Заполняет поле `style` значением CSS по умолчанию.
-    `SetDefaultPopupStyle`:  Устанавливает значения ширины и высоты popup в значения по умолчанию.
-   `EndDefault`: Конечная точка процесса сброса настроек.
-   `End`: Конец работы всего скрипта.
 - `isValidAttrName`, `isValidAttrNames`, `isValidStyleLength`: Подграфы, которые описывают работу этих функций.
-    `loadDefaultCss`, `extractBodyStyles`, `createPopupCss`: Подграфы, которые описывают работу этих функций.

## <объяснение>

### Импорты
В коде нет явных импортов через `import ... from ...`. Вместо этого используются глобальные переменные `tryxpath` (alias `tx`) и его функции `tryxpath.functions` (alias `fu`), предполагается, что они определены в другом месте. `browser` предоставляет API для работы с расширениями браузера и является глобальным объектом, доступным в контексте расширения.

### Переменные
-   `tx` (alias `tryxpath`): Предполагается, что это объект, предоставляющий функционал для работы с XPath.
-   `fu` (alias `tryxpath.functions`): Объект, содержащий различные функции, используемые в расширении. В частности, в коде используется `fu.onError` для обработки ошибок.
-   `document` (из `window.document`): Объект, представляющий DOM текущей страницы опций.
-   `defaultAttributes`: Объект, содержащий дефолтные имена для HTML-атрибутов, которые используются расширением.
-   `defaultPopupBodyStyles`: Объект, содержащий дефолтные стили для ширины и высоты popup.
-   `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`: DOM-элементы `<input>`, связанные с редактированием соответствующих атрибутов.
-   `style`: DOM-элемент `<input>`, связанный с редактированием CSS стилей.
-   `popupBodyWidth`, `popupBodyHeight`: DOM-элементы `<input>`, связанные с редактированием ширины и высоты popup.
-    `message`: DOM-элемент, используемый для вывода сообщений пользователю.
-  `testElement`: Временный DOM-элемент `<div>` созданный для проверки валидности атрибутов.

### Функции

**1. `isValidAttrName(name)`**
   -   **Аргументы:**
        -   `name`: `String` - имя атрибута, которое нужно проверить.
   -   **Возвращаемое значение:**
        -   `Boolean`: `true`, если имя атрибута валидное, `false` в противном случае.
   -   **Назначение:** Проверяет, является ли `name` валидным именем атрибута. Это делается путем попытки установить атрибут с таким именем на тестовый элемент `testElement`. Если операция проходит успешно, возвращается `true`, иначе `false`.
   -   **Пример:**
        -   `isValidAttrName("data-test")` может вернуть `true`.
        -   `isValidAttrName("invalid-attr-!")` может вернуть `false`.

**2. `isValidAttrNames(names)`**
    -   **Аргументы:**
        -   `names`: `Object` - Объект, содержащий имена атрибутов для проверки.
    -   **Возвращаемое значение:**
        -   `Boolean`: `true`, если все имена атрибутов валидны, `false` в противном случае.
    -   **Назначение:** Проверяет все имена атрибутов в объекте `names` с помощью `isValidAttrName`.
    -   **Пример:**
         -   `isValidAttrNames({element: "data-element", context: "data-context"})` может вернуть `true`.
         -   `isValidAttrNames({element: "data-element", context: "invalid-attr-!"})` может вернуть `false`.

**3. `isValidStyleLength(len)`**
    -   **Аргументы:**
        -   `len`: `String` - длина стиля для проверки (например, "auto", "100px").
    -   **Возвращаемое значение:**
        -   `Boolean`: `true`, если длина стиля валидна, `false` в противном случае.
    -   **Назначение:** Проверяет, соответствует ли длина стиля одному из допустимых форматов: `"auto"` или число в пикселях (например, `"100px"`).
    -   **Пример:**
        -   `isValidStyleLength("auto")` вернет `true`.
        -   `isValidStyleLength("100px")` вернет `true`.
        -   `isValidStyleLength("100")` вернет `false`.

**4. `loadDefaultCss()`**
   -   **Аргументы:** нет
   -   **Возвращаемое значение:**
        -   `Promise`: промис, разрешающийся текстом CSS-файла по умолчанию.
   -   **Назначение:** Загружает содержимое CSS файла, расположенного по адресу `/css/try_xpath_insert.css`  с помощью `XMLHttpRequest`.
   -    **Пример:** Асинхронно загружает CSS файл и возвращает текст, используя Promise.

**5. `extractBodyStyles(css)`**
    -   **Аргументы:**
        -   `css`: `String` - CSS строка.
    -   **Возвращаемое значение:**
        -  `Object`: Объект, содержащий свойства `width` и `height` из CSS.
    -   **Назначение:** Извлекает из CSS строки ширину и высоту popup. Использует регулярное выражение для поиска `width` и `height`.
    -   **Пример:**
        -  `extractBodyStyles("body{width:300px;height:auto;}")` вернет `{ width: "300px", height: "auto" }`.
        -  `extractBodyStyles("body{color:red;}")` вернет `{ width: "", height: "" }`.

**6. `createPopupCss(bodyStyles)`**
   -   **Аргументы:**
        -  `bodyStyles`: `Object` - Объект, содержащий свойства `width` и `height`.
   -   **Возвращаемое значение:**
        -  `String`: CSS строка, включающая значения ширины и высоты из `bodyStyles`.
   -   **Назначение:** Создает CSS строку для задания стилей ширины и высоты для элемента `body`.
   -   **Пример:**
        -   `createPopupCss({ width: "300px", height: "auto" })` вернет `"body{width:300px;height:auto;}"`

###  Объяснения
-   Код управляет настройками расширения TryXPath через страницу опций. Пользователь может изменять имена атрибутов, CSS стили и размеры popup.
-   Используются асинхронные операции для загрузки данных и сохранения настроек, в частности `browser.runtime.sendMessage` для связи с фоновым скриптом и `browser.storage.sync.set` для сохранения настроек.
-   Валидация ввода обеспечивает, что значения атрибутов и стилей соответствуют ожидаемым форматам, предотвращая потенциальные ошибки.
-   Использование промисов для асинхронных операций упрощает обработку результатов и ошибок.
-   Логика работы разбита на несколько функций, что повышает читаемость и тестируемость кода.
-   **Связи с другими частями проекта**: Этот код взаимодействует с фоновым скриптом (background.js) для получения и сохранения настроек, а также с `tryxpath` для XPath функционала, предполагается, что `tryxpath` - это библиотека, подключаемая в других частях проекта. Взаимодействие с `browser.storage.sync` позволяет синхронизировать настройки между браузерами, если эта возможность включена пользователем.

### Потенциальные ошибки и области для улучшения
1. **Обработка ошибок:**
    -   Несмотря на использование `catch(fu.onError)`, в коде не прописана детальная обработка возможных ошибок.
    -   В `loadDefaultCss` не обрабатываются ошибки при запросе файла.
2. **Валидация стилей:**
    -   Валидация `style` ограничена проверкой ширины и высоты popup. Другие CSS стили не проверяются.
3. **Общая архитектура:**
    -   Код находится в одном файле, что может усложнить его поддержку при увеличении функционала. Можно рассмотреть разделение на более мелкие модули.
4. **Использование `tryxpath`:**
    -  `tryxpath` и `tryxpath.functions` используются как глобальные переменные, что может привести к проблемам, если `tryxpath` не инициализирован или определен неправильно. Лучше использовать явный импорт модуля.
5. **Улучшение сообщений:**
     -   Сообщения об ошибках можно сделать более информативными, например, указывая конкретное имя атрибута или тип стиля, который вызвал ошибку.

В целом, код хорошо структурирован и понятен, но есть возможности для улучшения в части обработки ошибок, валидации, разделении кода на модули и улучшении пользовательского опыта.