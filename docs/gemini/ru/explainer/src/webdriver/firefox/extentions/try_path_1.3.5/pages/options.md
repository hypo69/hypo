# Анализ кода options.js

## <input code>

```javascript
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };

    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    function isValidAttrName(name) {
        try {
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            return false;
        }
        return true;
    };

    function isValidAttrNames(names) {
        for (var p in names) {
            if (!isValidAttrName(names[p])) {
                return false;
            }
        }
        return true;
    };

    function isValidStyleLength(len) {
        return /^auto$|^[1-9]\d*px$/.test(len);
    };

    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            var req = new XMLHttpRequest();
            req.open("GET",
                     browser.runtime.getURL("/css/try_xpath_insert.css"));
            req.responseType = "text";
            req.onreadystatechange = function () {
                if (req.readyState === XMLHttpRequest.DONE) {
                    resolve(req.responseText);
                }
            };
            req.send();
        });
    };

    function extractBodyStyles(css) {
        var styles = {};

        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            styles.width = res[1];
            styles.height = res[2];
        } else {
            styles.width = "";
            styles.height = "";
        }

        return styles;
    };

    function createPopupCss(bodyStyles) {
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

    window.addEventListener("load", () => {
        // ... (rest of the code)
    });

    testElement = document.createElement("div");
})(window);
```

## <algorithm>

(Блок-схема – сложно представить в текстовом формате.  Представлены ключевые этапы.)

1. **Инициализация:**
   - Объявляются переменные для хранения ссылок на элементы DOM.
   - Задаются значения по умолчанию для атрибутов и стилей.
   - Создается `testElement` для проверки валидности атрибутов.

2. **Проверка валидности:**
   - `isValidAttrName`: Проверяет, допустимо ли имя атрибута.
   - `isValidAttrNames`: Проверяет все имена атрибутов.
   - `isValidStyleLength`: Проверяет корректность значения стилей (ширина и высота).

3. **Загрузка стилей:**
   - `loadDefaultCss`: Загружает CSS из файла `try_xpath_insert.css` используя `browser.runtime.getURL`.
   - `extractBodyStyles`: Извлекает значения ширины и высоты из CSS.
   - `createPopupCss`: Формирует CSS-стили для всплывающего окна.

4. **Обработка события загрузки страницы:**
   - Считывает значения атрибутов и CSS из `browser.storage.sync`.
   - Заполняет соответствующие поля формы.
   - Обрабатывает клик на кнопку "Сохранить".
   - Обрабатывает клик на кнопку "Показать значения по умолчанию".

5. **Обработка клика на кнопку "Сохранить":**
   - Считывает значения из полей формы.
   - Проверяет валидность атрибутов и стилей.
   - Если валидность не соблюдена, выводит сообщение об ошибке.
   - Если валидность соблюдена, записывает значения в `browser.storage.sync`.
   - Выводит сообщение об успехе или об ошибке при записи.

6. **Обработка клика на кнопку "Показать значения по умолчанию":**
   - Устанавливает значения атрибутов и стилей на значения по умолчанию.
   - Загружает стили из файла по умолчанию.


## <mermaid>

```mermaid
graph TD
    A[window.addEventListener("load")] --> B{Обработка события загрузки};
    B --> C[Считывание значений из storage];
    C --> D[Заполнение полей формы];
    D --> E[Обработка клика "Сохранить"];
    E --> F[Проверка валидности];
    F -- Валидно --> G[Запись в storage];
    F -- Невалидно --> H[Вывод сообщения об ошибке];
    G --> I[Вывод сообщения об успехе];
    E --> J[Обработка клика "Показать значения по умолчанию"];
    J --> K[Установка значений по умолчанию];
    K --> L[Загрузка стилей по умолчанию];
    C --> M[Выполнение loadDefaultCss];
    M --> N[Обработка запроса];
    N --> O[Возврат CSS];
    O --> D;


    subgraph Загрузка стилей по умолчанию
        M --> P[Запрос к файлу /css/try_xpath_insert.css];
        P --> Q[Обработка запроса];
        Q --> R[Возврат CSS];
        R --> L;
    end


    subgraph Проверка валидности
        F --> S[isValidAttrName];
        F --> T[isValidAttrNames];
        F --> U[isValidStyleLength];
    end
```


## <explanation>

**Импорты:**

- Код не содержит импортов в привычном формате `import`, но использует алиасы `tx` и `fu` для `tryxpath` и `tryxpath.functions` соответственно. Это указывает на использование какого-то внутреннего модуля/пакета (вероятно, части расширения для браузера) с именем `tryxpath`.  `browser` - это объект, предоставляемый браузерной платформой (например, Chrome). Он используется для взаимодействия с браузером, в частности для доступа к локальным ресурсам (css) и к хранилищу.

**Классы:**

- Нет явных определений классов.


**Функции:**

- `isValidAttrName(name)`: Проверяет, можно ли у элемента установить атрибут с указанным именем. Возвращает `true`, если атрибут допустим, `false` — в противном случае. Используется для проверки валидности имен атрибутов.
- `isValidAttrNames(names)`: Проверяет, можно ли установить набор атрибутов. Возвращает `true`, если все атрибуты валидны, `false` — в противном случае.
- `isValidStyleLength(len)`: Проверяет корректность введённой длины стиля, например, "300px".
- `loadDefaultCss()`: Асинхронная функция, загружающая CSS из файла `/css/try_xpath_insert.css` с помощью `XMLHttpRequest`. Возвращает промис, содержащий загруженный текст CSS.
- `extractBodyStyles(css)`: Извлекает ширину и высоту из CSS-строки.
- `createPopupCss(bodyStyles)`: Создает CSS-правило для тела всплывающего окна.


**Переменные:**

- `defaultAttributes`, `defaultPopupBodyStyles`:  Константы, хранящие значения по умолчанию.
- `elementAttr`, `contextAttr`,  `focusedAttr`,  `ancestorAttr`, `frameAttr`,  `frameAncestorAttr`, `style`, `popupBodyWidth`, `popupBodyHeight`, `message`, `testElement`: Переменные-ссылки на элементы DOM.

**Возможные ошибки и улучшения:**

- **Обработка ошибок `XMLHttpRequest`**:  Функция `loadDefaultCss` не обрабатывает ошибки при загрузке CSS.  Необходимо добавить `reject` в `Promise`, чтобы обработать ошибки.
- **Более точная валидация стилей**: Регулярное выражение для `isValidStyleLength` могло бы быть более строгим. Например, оно не проверяет на наличие нечисловых значений.
- **Обработка пустых значений:**  В функции `extractBodyStyles` не проверяется, что `res` не равен null.


**Взаимосвязи с другими частями проекта:**

- Функция `browser.runtime.sendMessage` показывает взаимодействие с другим кодом расширения (вероятно, содержащим логику для получения данных).
- `browser.storage.sync.set` демонстрирует сохранение данных в хранилище, которое может использоваться другими частями расширения.


**Заключение:**

Код отвечает за загрузку настроек, проверку валидности атрибутов и стилей, и сохранение данных в хранилище расширения.  Он использует асинхронные операции и промисы, что позволяет обрабатывать данные, не блокируя выполнение остальных операций.