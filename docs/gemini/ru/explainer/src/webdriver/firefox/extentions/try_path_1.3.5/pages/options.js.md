## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

1. **Инициализация переменных и констант:**
   - Определяются константы `defaultAttributes` и `defaultPopupBodyStyles`, содержащие значения по умолчанию для атрибутов элементов и стилей всплывающего окна.
   - Объявляются переменные для хранения элементов DOM, таких как атрибуты, стили, сообщения и тестовый элемент.
   - Примеры:
     - `defaultAttributes = {"element": "data-tryxpath-element", ...}`
     - `popupBodyWidth` - элемент ввода для ширины всплывающего окна
     - `message` - элемент для отображения сообщений об ошибках и успехе
2. **Функция `isValidAttrName(name)`:**
   - Проверяет, является ли переданное имя допустимым именем атрибута HTML-элемента.
   - Пытается установить атрибут с указанным именем тестовому элементу.
   - Возвращает `true`, если атрибут можно установить, иначе `false`.
   - Пример:
     - Вызов `isValidAttrName("data-custom-attr")` вернёт `true`
     - Вызов `isValidAttrName("invalid-attr-name")` вернёт `false` (если такое имя атрибута недопустимо)
3. **Функция `isValidAttrNames(names)`:**
   - Проверяет все имена атрибутов, переданные в объекте, на допустимость, используя `isValidAttrName`.
   - Возвращает `true`, если все имена атрибутов допустимы, иначе `false`.
   - Пример:
     - Вызов `isValidAttrNames({element: "data-tryxpath-element", context: "data-tryxpath-context"})` вернёт `true`
     - Вызов `isValidAttrNames({element: "data-tryxpath-element", context: "invalid-attr-name"})` вернёт `false`
4. **Функция `isValidStyleLength(len)`:**
   - Проверяет, является ли переданная строка допустимой длиной CSS (например, "auto" или "100px").
   - Использует регулярное выражение для проверки формата.
   - Возвращает `true`, если длина допустима, иначе `false`.
   - Пример:
     - Вызов `isValidStyleLength("150px")` вернёт `true`
     - Вызов `isValidStyleLength("auto")` вернёт `true`
     - Вызов `isValidStyleLength("150")` вернёт `false`
5. **Функция `loadDefaultCss()`:**
   - Загружает содержимое CSS-файла по умолчанию, используя `XMLHttpRequest`.
   - Создает `Promise`, который разрешается с содержимым CSS при успешной загрузке.
   - Возвращает `Promise` с текстом css.
   - Пример:
     - Promise возвращает строку с css стилями `body { ... }`
6. **Функция `extractBodyStyles(css)`:**
   - Извлекает стили `width` и `height` из переданной строки CSS.
   - Использует регулярное выражение для поиска значений.
   - Возвращает объект со свойствами `width` и `height` или пустые значения, если не найдены.
   - Пример:
     - Вызов `extractBodyStyles("body{width:300px;height:auto;}")` вернет `{width: "300px", height: "auto"}`
     - Вызов `extractBodyStyles("body{color:red;}")` вернет `{width: "", height: ""}`
7. **Функция `createPopupCss(bodyStyles)`:**
   - Создает строку CSS для всплывающего окна на основе переданных стилей.
   - Использует значения `width` и `height` из объекта `bodyStyles`.
   - Возвращает строку CSS.
   - Пример:
     - Вызов `createPopupCss({width: "300px", height: "auto"})` вернёт `"body{width:300px;height:auto;}"`
8. **Обработчик события `window.onload`:**
   - Выполняется после загрузки страницы.
   - Получает ссылки на DOM-элементы (input поля и сообщение).
   - Отправляет сообщение `loadOptions` в фоновый скрипт, получая текущие настройки и заполняя ими значения input полей.
   - Добавляет обработчик события `click` для кнопки "save":
      - Собирает значения атрибутов и стилей из input-полей.
      - Проверяет валидность атрибутов и длин стилей.
      - Сохраняет настройки в `browser.storage.sync`.
      - Выводит сообщение об успехе или неудаче.
   - Добавляет обработчик события `click` для кнопки "show-default":
      - Устанавливает значения атрибутов по умолчанию.
      - Загружает CSS по умолчанию и устанавливает его.
      - Устанавливает значения ширины и высоты popup по умолчанию.
9. **Создание тестового элемента:**
   - Создается `div` элемент для тестирования атрибутов.

## <mermaid>

```mermaid
flowchart TD
    subgraph OptionsPage
        Start[Начало] --> LoadElements[Получение DOM элементов]
        LoadElements --> SendLoadOptionsMessage[Отправка сообщения "loadOptions" в фоновый скрипт]
        SendLoadOptionsMessage --> ReceiveOptions[Получение настроек]
        ReceiveOptions --> FillInputFields[Заполнение полей ввода полученными данными]
        FillInputFields --> SaveButton[Обработчик клика на кнопку "save"]
        SaveButton --> CollectInputValues[Сбор данных из полей ввода]
        CollectInputValues --> ValidateAttributes[Проверка валидности атрибутов: isValidAttrNames()]
         ValidateAttributes -- Атрибуты не валидны --> DisplayError[Отображение ошибки]
        ValidateAttributes -- Атрибуты валидны --> ValidateStyles[Проверка валидности стилей: isValidStyleLength()]
         ValidateStyles -- Стили не валидны --> DisplayError
        ValidateStyles -- Стили валидны --> SaveSettings[Сохранение настроек в browser.storage.sync]
        SaveSettings --> DisplaySuccess[Отображение сообщения об успехе]
        SaveSettings -- Ошибка при сохранении --> DisplayError
        FillInputFields --> ShowDefaultButton[Обработчик клика на кнопку "show-default"]
        ShowDefaultButton --> SetDefaultAttributeValues[Установка значений атрибутов по умолчанию]
        SetDefaultAttributeValues --> LoadDefaultCss[Загрузка CSS по умолчанию: loadDefaultCss()]
        LoadDefaultCss --> SetDefaultCss[Установка CSS]
         SetDefaultAttributeValues --> SetDefaultPopupStyles[Установка ширины и высоты popup по умолчанию]
         SetDefaultPopupStyles --> End[Конец]
         DisplayError --> End
    end
    subgraph Functions
        isValidAttrName(attributeName) -->|true| ValidateAttributes
        isValidAttrName(attributeName) -->|false| ValidateAttributes
        isValidAttrNames(attributeNames) -->|true| ValidateAttributes
        isValidAttrNames(attributeNames) -->|false| ValidateAttributes
       isValidStyleLength(styleLength) -->|true| ValidateStyles
        isValidStyleLength(styleLength) -->|false| ValidateStyles
        loadDefaultCss() --> LoadDefaultCss
       extractBodyStyles(css) --> ReceiveOptions
       createPopupCss(bodyStyles) --> SaveSettings
    end
    
    
    linkStyle default stroke:#000,stroke-width:2px
    
```

### Зависимости Mermaid

*   **`OptionsPage`**: Описывает основной блок кода, работающий на странице опций расширения.
    *   `Start`: Начало выполнения скрипта на странице.
    *   `LoadElements`: Загружает все необходимые элементы DOM, такие как input-поля и текстовые сообщения для дальнейшей работы с ними.
    *   `SendLoadOptionsMessage`: Отправляет сообщение с запросом текущих настроек в фоновый скрипт расширения.
    *   `ReceiveOptions`: Получает объект с настройками из фонового скрипта.
    *   `FillInputFields`: Заполняет поля input значениями полученных настроек.
    *   `SaveButton`: Обработчик события клика по кнопке сохранения настроек.
    *   `CollectInputValues`: Собирает значения из input-полей для сохранения.
    *   `ValidateAttributes`: Проверяет валидность имен атрибутов с помощью функции `isValidAttrNames()`.
    *   `ValidateStyles`: Проверяет валидность CSS-свойств с помощью функции `isValidStyleLength()`.
    *   `DisplayError`: Выводит сообщение об ошибке на странице.
    *   `SaveSettings`: Сохраняет данные в `browser.storage.sync`.
    *   `DisplaySuccess`: Выводит сообщение об успешном сохранении настроек.
     *   `ShowDefaultButton`: Обработчик события клика по кнопке "Показать по умолчанию".
      *   `SetDefaultAttributeValues`: Устанавливает дефолтные значения атрибутов.
       *   `LoadDefaultCss`: Загружает дефолтные стили CSS с помощью функции `loadDefaultCss()`.
        *   `SetDefaultCss`: Устанавливает дефолтные стили в input.
        *   `SetDefaultPopupStyles`: Устанавливает дефолтные стили для popup.
    *   `End`: Конец работы скрипта.

*   **`Functions`**: Описывает группу функций, которые используются в коде.
    *   `isValidAttrName(attributeName)`: Функция проверяет, является ли имя атрибута валидным для HTML элемента. Возвращает true или false.
    *  `isValidAttrNames(attributeNames)`: Функция проверяет валидность всех имен атрибутов в переданом объекте, использует `isValidAttrName()`. Возвращает true или false.
    *   `isValidStyleLength(styleLength)`: Функция проверяет валидность длины CSS-свойства, возвращает true или false.
    *   `loadDefaultCss()`: Функция асинхронно загружает CSS из файла.
    *  `extractBodyStyles(css)`: Функция парсит CSS и извлекает ширину и высоту.
    * `createPopupCss(bodyStyles)`: Функция формирует строку css для body на основе переданных стилей ширины и высоты.

## <объяснение>

**Импорты:**
- В данном коде нет явных импортов из других пакетов `src`. Он работает в контексте веб-страницы расширения браузера и использует API браузера (`browser.runtime`, `browser.storage`).

**Классы:**

- В коде нет классов.

**Функции:**
*   `isValidAttrName(name)`:
    *   **Аргументы**: `name` (строка) - имя атрибута для проверки.
    *   **Возвращаемое значение**: `true`, если имя допустимо; `false` в противном случае.
    *   **Назначение**: Проверяет, является ли переданное имя допустимым для HTML-атрибута, пытаясь установить его на тестовом элементе.
    *   **Пример**: `isValidAttrName('data-my-attribute')` вернет `true`, если такой атрибут можно установить.
*   `isValidAttrNames(names)`:
    *   **Аргументы**: `names` (объект) - объект с именами атрибутов в виде `key:value`.
    *   **Возвращаемое значение**: `true`, если все имена допустимы; `false` в противном случае.
    *   **Назначение**: Проверяет все имена атрибутов в переданном объекте, используя `isValidAttrName`.
    *   **Пример**: `isValidAttrNames({ element: 'data-element', context: 'data-context' })` вернет `true` если оба имени корректны.
*   `isValidStyleLength(len)`:
    *   **Аргументы**: `len` (строка) - строка для проверки на длину CSS.
    *   **Возвращаемое значение**: `true`, если строка соответствует допустимой длине CSS; `false` в противном случае.
    *   **Назначение**: Проверяет строку на соответствие формату длины CSS (например, "auto", "100px").
    *   **Пример**: `isValidStyleLength('200px')` вернет `true`; `isValidStyleLength('200')` вернет `false`.
*   `loadDefaultCss()`:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: `Promise`, разрешающийся со строкой, содержащей CSS-стили.
    *   **Назначение**: Загружает CSS из внешнего файла и возвращает промис.
    *   **Пример**: `loadDefaultCss().then(css => console.log(css))`
*   `extractBodyStyles(css)`:
    *   **Аргументы**: `css` (строка) - строка, содержащая CSS.
    *   **Возвращаемое значение**: Объект с ключами `width` и `height`, содержащими извлеченные значения стилей или пустые строки.
    *   **Назначение**: Извлекает значения ширины и высоты из переданной CSS-строки, используя регулярное выражение.
    *    **Пример**: `extractBodyStyles("body{width:300px;height:auto;}")` вернет `{width: "300px", height: "auto"}`.
*   `createPopupCss(bodyStyles)`:
    *   **Аргументы**: `bodyStyles` (объект) - объект со стилями `width` и `height`.
    *   **Возвращаемое значение**: Строка, содержащая CSS-стили для всплывающего окна.
    *   **Назначение**: Создает CSS-строку для стилизации всплывающего окна на основе переданных стилей.
    *   **Пример**: `createPopupCss({width: '200px', height: 'auto'})` вернет `"body{width:200px;height:auto;}"`.

**Переменные:**

*   `tx`: Алиас для объекта `tryxpath`.
*   `fu`: Алиас для объекта `tryxpath.functions`.
*   `document`: Ссылка на объект `document` веб-страницы.
*   `defaultAttributes`: Объект, содержащий атрибуты по умолчанию.
*   `defaultPopupBodyStyles`: Объект, содержащий стили по умолчанию для всплывающего окна.
*   `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`: DOM-элементы `<input>`, представляющие поля для ввода атрибутов.
*   `style`: DOM-элемент `<input>`, представляющий поле для ввода CSS.
*   `popupBodyWidth`, `popupBodyHeight`: DOM-элементы `<input>`, представляющие поля для ввода ширины и высоты всплывающего окна.
*   `message`: DOM-элемент, представляющий область для вывода сообщений.
*   `testElement`: Созданный `div`-элемент, используемый для проверки имен атрибутов.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок**: В некоторых местах используется `catch(fu.onError)`. Желательно добавить более детальную обработку ошибок с выводом сообщений пользователю.
2.  **Валидация стилей**: Проверка `isValidStyleLength` достаточно простая, она не проверяет, что в строке содержатся только цифры и `px`.
3.  **Код дублируется**: Код для получения элементов по id вынесен в отдельный блок, было бы лучше сделать функцию для этого.

**Взаимосвязи с другими частями проекта:**

- Этот код работает в контексте страницы опций расширения (extension options). Он взаимодействует с фоновым скриптом через `browser.runtime.sendMessage` для получения и сохранения настроек.
- Использует API `browser.storage.sync` для сохранения настроек, которые будут доступны в других частях расширения.
-  Используется библиотека `tryxpath` через алиасы `tx` и `fu`.

Этот скрипт обеспечивает пользовательский интерфейс для настройки атрибутов и стилей, используемых расширением, и сохраняет эти настройки для дальнейшего использования.