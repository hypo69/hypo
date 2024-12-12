## <алгоритм>

1.  **Инициализация:**
    *   Определение алиасов `tx` для `tryxpath` и `fu` для `tryxpath.functions`.
    *   Получение объекта `document` из `window`.
    *   Определение констант `defaultAttributes` (атрибуты для элементов) и `defaultPopupBodyStyles` (стили для всплывающего окна).
    *   Объявление переменных для атрибутов элементов (`elementAttr`, `contextAttr` и т.д.), стилей (`style`), размеров всплывающего окна (`popupBodyWidth`, `popupBodyHeight`), сообщения (`message`) и тестового элемента (`testElement`).
    *   Создание элемента `div` для проверки атрибутов: `testElement = document.createElement("div");`.

2.  **Функция `isValidAttrName(name)`:**
    *   Принимает имя атрибута (`name`).
    *   Пытается установить атрибут с этим именем на `testElement` со значением `"testValue"`.
    *   Если операция успешна, возвращает `true`; если возникает ошибка (например, недопустимое имя атрибута), возвращает `false`.

    *   *Пример:* `isValidAttrName("data-test")` вернет `true`, `isValidAttrName("invalid-attr-name")` может вернуть `false`.

3.  **Функция `isValidAttrNames(names)`:**
    *   Принимает объект с именами атрибутов (`names`).
    *   Итерируется по всем именам в `names`.
    *   Для каждого имени вызывает `isValidAttrName`. Если хотя бы одно имя недопустимо, возвращает `false`.
    *   Если все имена допустимы, возвращает `true`.
    
    *   *Пример:* `isValidAttrNames({ "element": "data-tryxpath-element", "context": "data-tryxpath-context" })` вернет `true`, если оба атрибута допустимы. `isValidAttrNames({ "element": "invalid-attr-name", "context": "data-tryxpath-context" })` вернет `false`, если `invalid-attr-name` не допустим.

4.  **Функция `isValidStyleLength(len)`:**
    *   Принимает строку с длиной стиля (`len`).
    *   Проверяет, соответствует ли строка формату `"auto"` или формату `"числоpx"` (где число - целое положительное).
    *   Возвращает `true`, если строка соответствует формату; `false` в противном случае.
    
    *   *Пример:* `isValidStyleLength("auto")` вернет `true`, `isValidStyleLength("100px")` вернет `true`, `isValidStyleLength("100")` вернет `false`, `isValidStyleLength("100px ")` вернет `false`.

5.  **Функция `loadDefaultCss()`:**
    *   Создает `Promise`, который разрешается со значением `req.responseText` или отклоняется с ошибкой.
    *   Создает `XMLHttpRequest` для загрузки CSS файла `try_xpath_insert.css`.
    *   Устанавливает тип ответа `text` и устанавливает callback функцию `onreadystatechange`
    *   `onreadystatechange` проверяет, если `readyState` равен `XMLHttpRequest.DONE`, то `Promise` разрешается с помощью `resolve` и значением `req.responseText`.
    *   Отправляет запрос `req.send()`.
    
    *   *Пример:* загрузка содержимого CSS файла в виде строки.

6.  **Функция `extractBodyStyles(css)`:**
    *   Принимает строку CSS (`css`).
    *   Ищет в строке `width:` и `height:`, используя регулярное выражение `/width:(.+?);.*height:(.+?);/`.
    *   Если находит, то извлекает значения `width` и `height` и возвращает их в виде объекта.
    *   Если не находит, то возвращает объект с пустыми значениями для `width` и `height`.
    
    *   *Пример:* `extractBodyStyles("width:367px;height:auto;")` вернет `{ width: "367px", height: "auto" }`. `extractBodyStyles("font-size:12px;")` вернет `{ width: "", height: "" }`.

7.  **Функция `createPopupCss(bodyStyles)`:**
    *   Принимает объект `bodyStyles` с `width` и `height`.
    *   Возвращает строку CSS, которая устанавливает ширину и высоту тела (`body`).
    
    *   *Пример:* `createPopupCss({ width: "367px", height: "auto" })` вернет `"body{width:367px;height:auto;}"`.

8.  **Слушатель события `load`:**
    *   После полной загрузки страницы выполняются следующие действия:
        *   Получение элементов DOM по их ID и сохранение в соответствующие переменные.
        *   Отправка сообщения `loadOptions` в `browser.runtime` и ожидание ответа.
        *   В случае успеха:
            *   Заполнение полей ввода значениями атрибутов из полученного ответа.
            *   Извлечение стилей тела всплывающего окна из `popupCss` и установка значений в соответствующие поля ввода.
        *   В случае ошибки:
            *   Обработка ошибки с помощью `fu.onError`.
        *   Добавление обработчика события `click` на кнопку `"save"`:
            *   Получение введенных значений атрибутов и стилей.
            *   Проверка валидности имен атрибутов и стилей.
            *   Если значения не валидны, отображается сообщение об ошибке.
            *   Если значения валидны, сохранение новых значений в `browser.storage.sync`.
            *   В случае успеха отображается сообщение об успехе.
            *   В случае неудачи отображается сообщение об ошибке.
        *   Добавление обработчика события `click` на кнопку `"show-default"`:
            *   Заполнение полей ввода значениями атрибутов по умолчанию.
            *   Загрузка CSS по умолчанию и установка его в поле ввода.
            *   Установка размеров всплывающего окна по умолчанию.
    
    *   *Пример:* При загрузке страницы поля ввода заполняются ранее сохраненными значениями. При нажатии на кнопку `save`, данные сохраняются в `browser.storage.sync`, и отображается сообщение. При нажатии на кнопку `show-default`, поля ввода возвращаются к значениям по умолчанию.
    

## <mermaid>

```mermaid
flowchart TD
    Start[Start: Page Load] --> GetElements[Get DOM elements by ID];
    GetElements --> SendMessage[browser.runtime.sendMessage({event: "loadOptions"})];
    SendMessage --> HandleResponse{Response Received?};
    HandleResponse -- Yes --> ExtractAttributes[Extract attributes from response]
    ExtractAttributes --> SetAttributeValues[Set attribute input values]
    SetAttributeValues --> ExtractBodyStylesFromCss[Extract Body Styles from popupCss];
    ExtractBodyStylesFromCss --> SetStyleValues[Set popup body width and height values];
    HandleResponse -- No --> ErrorHandler[fu.onError];

    GetElements --> SaveButton[Get "save" button];
    SaveButton --> SaveButtonClick[Add click event listener to "save" button];
    SaveButtonClick --> GetInputValues[Get values from input fields]
    GetInputValues --> ValidateAttributes[isValidAttrNames(attributes)];
    ValidateAttributes -- No --> DisplayInvalidAttributeMessage[Display "Invalid attribute" message];
    ValidateAttributes -- Yes --> ValidateStyles[isValidStyleLength(popupBodyStyles.width) && isValidStyleLength(popupBodyStyles.height)];
    ValidateStyles -- No --> DisplayInvalidStyleMessage[Display "Invalid style" message];
    ValidateStyles -- Yes --> CreatePopupCss[createPopupCss(bodyStyles)];
    CreatePopupCss --> SaveToStorage[browser.storage.sync.set({attributes, css, popupCss})];
    SaveToStorage --> SuccessHandler{Success?};
    SuccessHandler -- Yes --> DisplaySuccessMessage[Display "Success" message];
    SuccessHandler -- No --> DisplayFailureMessage[Display "Failure" message];

    GetElements --> ShowDefaultButton[Get "show-default" button];
    ShowDefaultButton --> ShowDefaultClick[Add click event listener to "show-default" button];
    ShowDefaultClick --> SetDefaultAttributeValues[Set default attribute values];
    SetDefaultAttributeValues --> LoadDefaultCss[loadDefaultCss()];
    LoadDefaultCss --> SetDefaultCssValue[Set default CSS value];
     SetDefaultCssValue--> SetDefaultPopupBodyStyles[Set default popup body styles]

    classDef element fill:#f9f,stroke:#333,stroke-width:2px
    class GetElements, SendMessage,ExtractAttributes, SetAttributeValues,ExtractBodyStylesFromCss,SetStyleValues, SaveButton, SaveButtonClick, GetInputValues, ValidateAttributes, ValidateStyles,CreatePopupCss, SaveToStorage,SuccessHandler, ShowDefaultButton, ShowDefaultClick, SetDefaultAttributeValues, LoadDefaultCss,SetDefaultCssValue,SetDefaultPopupBodyStyles element
```

**Объяснение зависимостей:**

*   `Start`: Начало выполнения скрипта, когда страница загружается.
*   `GetElements`: Получение элементов DOM, таких как поля ввода и кнопки.
*   `SendMessage`: Отправка сообщения `loadOptions` в фоновый скрипт через `browser.runtime.sendMessage`.
*   `HandleResponse`: Проверка наличия ответа от фонового скрипта.
*    `ExtractAttributes`: Извлечение значений атрибутов из полученного ответа.
*   `SetAttributeValues`: Установка значений атрибутов в соответствующие поля ввода.
*   `ExtractBodyStylesFromCss`: Извлечение стилей `width` и `height` из CSS.
*   `SetStyleValues`: Установка значений ширины и высоты всплывающего окна в соответствующие поля ввода.
*    `ErrorHandler`: Обработка ошибки, в случае если не удалось получить данные.
*   `SaveButton`: Получение кнопки `save` по ее ID.
*   `SaveButtonClick`: Добавление слушателя события `click` на кнопку `save`.
*   `GetInputValues`: Получение значений из полей ввода для атрибутов и стилей.
*   `ValidateAttributes`: Проверка валидности введенных имен атрибутов.
*   `DisplayInvalidAttributeMessage`: Отображение сообщения об ошибке, если имена атрибутов невалидны.
*   `ValidateStyles`: Проверка валидности введенных значений стилей.
*   `DisplayInvalidStyleMessage`: Отображение сообщения об ошибке, если значения стилей невалидны.
*   `CreatePopupCss`: Создание CSS для всплывающего окна на основе введенных стилей.
*   `SaveToStorage`: Сохранение введенных значений в `browser.storage.sync`.
*   `SuccessHandler`: Проверка результата операции сохранения.
*   `DisplaySuccessMessage`: Отображение сообщения об успехе.
*    `DisplayFailureMessage`: Отображение сообщения об ошибке сохранения.
*   `ShowDefaultButton`: Получение кнопки `show-default` по ее ID.
*   `ShowDefaultClick`: Добавление слушателя события `click` на кнопку `show-default`.
*   `SetDefaultAttributeValues`: Установка значений атрибутов по умолчанию.
*  `LoadDefaultCss`: Загрузка CSS по умолчанию из файла.
*    `SetDefaultCssValue`: Установка значения CSS по умолчанию в поле ввода.
*   `SetDefaultPopupBodyStyles`: Установка размеров всплывающего окна по умолчанию.

## <объяснение>

### Импорты:

*   В коде нет явных импортов из других файлов или модулей с использованием ключевого слова `import`. Вместо этого используется объект `browser` для взаимодействия с API браузерных расширений (например, для отправки сообщений и работы с хранилищем).
*   Алиас `tx` ссылается на объект `tryxpath`, вероятно, определенный в другом файле этого же расширения.
*   Алиас `fu` ссылается на объект `tryxpath.functions`, который, предположительно, содержит общие функции, включая функцию обработки ошибок `onError`.
*   Зависимость от `browser.runtime` и `browser.storage.sync` указывает на тесную интеграцию с API браузера для обмена данными и сохранения настроек.

### Классы:

*   В коде нет явных объявлений классов. Весь код организован в виде функций и обработчиков событий.
*   Однако, можно считать, что объекты, такие как `XMLHttpRequest` и `Promise`, являются экземплярами классов, предоставленных средой выполнения JavaScript.
*   Объект `defaultAttributes` можно считать своего рода "конфигурационным" объектом.

### Функции:

*   **`isValidAttrName(name)`**:
    *   Аргумент: `name` (строка) - имя атрибута.
    *   Возвращаемое значение: `true`, если имя атрибута допустимо; `false` в противном случае.
    *   Назначение: Проверяет, является ли имя атрибута допустимым для установки в DOM-элемент.
    *   Пример: `isValidAttrName("data-test")` вернет `true`. `isValidAttrName("invalid-attr")` может вернуть `false`.
*   **`isValidAttrNames(names)`**:
    *   Аргумент: `names` (объект) - объект с именами атрибутов.
    *   Возвращаемое значение: `true`, если все имена атрибутов допустимы; `false` в противном случае.
    *   Назначение: Проверяет, являются ли все имена атрибутов в объекте допустимыми.
    *   Пример: `isValidAttrNames({"attr1": "data-test", "attr2": "data-test2"})` вернет `true`, если оба допустимы.
*   **`isValidStyleLength(len)`**:
    *   Аргумент: `len` (строка) - длина стиля.
    *   Возвращаемое значение: `true`, если длина стиля имеет допустимый формат; `false` в противном случае.
    *   Назначение: Проверяет, является ли длина стиля строкой в формате `"auto"` или `"числоpx"`.
    *   Пример: `isValidStyleLength("auto")` вернет `true`. `isValidStyleLength("100px")` вернет `true`. `isValidStyleLength("100")` вернет `false`.
*  **`loadDefaultCss()`**:
    *   Аргументы: нет.
    *   Возвращаемое значение: `Promise` - промис, разрешающийся со строкой CSS или отклоняющийся с ошибкой.
    *   Назначение: Загружает CSS по умолчанию из файла.
    *   Пример: Загружает текст CSS файла по адресу `browser.runtime.getURL("/css/try_xpath_insert.css")`
*   **`extractBodyStyles(css)`**:
    *   Аргумент: `css` (строка) - строка CSS.
    *   Возвращаемое значение: Объект с атрибутами `width` и `height` (строки).
    *   Назначение: Извлекает значения `width` и `height` из строки CSS.
    *   Пример: `extractBodyStyles("width:100px;height:auto;")` вернет `{ width: "100px", height: "auto" }`.
*   **`createPopupCss(bodyStyles)`**:
    *   Аргумент: `bodyStyles` (объект) - объект со стилями (`width`, `height`).
    *   Возвращаемое значение: Строка CSS для установки стилей тела.
    *   Назначение: Создает строку CSS, устанавливающую `width` и `height` тела (`body`).
    *   Пример: `createPopupCss({ width: "100px", height: "auto" })` вернет `"body{width:100px;height:auto;}"`.

### Переменные:

*   `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`: Ссылки на DOM-элементы (поля ввода) для редактирования атрибутов.
*   `style`: Ссылка на DOM-элемент (поле ввода) для редактирования CSS.
*   `popupBodyWidth`, `popupBodyHeight`: Ссылки на DOM-элементы (поля ввода) для редактирования размеров всплывающего окна.
*   `message`: Ссылка на DOM-элемент (параграф) для отображения сообщений пользователю.
*    `testElement`: Элемент, используемый для валидации атрибутов
*  `defaultAttributes`: Объект содержащий значения атрибутов по умолчанию.
*  `defaultPopupBodyStyles`: Объект содержащий стили для всплывающего окна по умолчанию.

### Цепочка взаимосвязей:

1.  **Загрузка страницы:**
    *   Скрипт начинает выполняться после загрузки DOM (`window.addEventListener("load", ...)`).
    *   Получаются ссылки на все необходимые DOM-элементы по их ID.
2.  **Загрузка сохраненных опций:**
    *   Отправляется сообщение `loadOptions` в фоновый скрипт через `browser.runtime.sendMessage`.
    *   Полученный ответ содержит сохраненные атрибуты и стили.
    *   Значения атрибутов устанавливаются в соответствующие поля ввода.
    *   Извлекаются стили `width` и `height` из сохраненной CSS для всплывающего окна.
    *   Значения `width` и `height` устанавливаются в соответствующие поля ввода.
3.  **Сохранение опций:**
    *   Событие `click` на кнопке "save" запускает процесс сохранения.
    *   Получаются значения из полей ввода.
    *   Происходит валидация имен атрибутов и стилей.
    *   В случае ошибки отображается сообщение.
    *   В случае успеха создается CSS для всплывающего окна, и значения сохраняются в `browser.storage.sync`.
4.  **Установка значений по умолчанию:**
    *   Событие `click` на кнопке "show-default" запускает процесс установки значений по умолчанию.
    *   В поля ввода устанавливаются значения атрибутов по умолчанию.
    *    Загружается CSS по умолчанию и устанавливается в соответствующее поле ввода
    *    В поля ввода устанавливаются стили по умолчанию.

### Потенциальные ошибки и области для улучшения:

*   **Обработка ошибок:** Код использует `fu.onError` для обработки ошибок, но не предоставляет подробной информации о том, как именно обрабатываются ошибки.
*   **Валидация стилей:** Код проверяет только формат длин стилей (`auto` или `числоpx`). Можно добавить более строгую проверку значений.
*  **Регулярные выражения:** Регулярное выражение `/width:(.+?);.*height:(.+?);/`  не является надежным парсером CSS. Его поведение при нестандартном css может быть непредсказуемым. Желательно использовать более надежный метод парсинга CSS.
*   **Улучшение пользовательского интерфейса**: Можно добавить больше интерактивности и обратной связи для пользователя, например, валидацию ввода в режиме реального времени.
*   **Проверка наличия DOM элементов**: Код предполагает наличие элементов DOM с заданными ID, но не проверяет их наличие. Желательно добавить проверку наличия элементов перед обращением к ним.