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

Этот код JavaScript управляет настройками расширения, вероятно, для веб-драйвера Edge. Алгоритм:

1. **Инициализация:** Определяет переменные, связанные с элементами HTML, а также `defaultAttributes` и `defaultPopupBodyStyles`.
2. **Проверка валидности атрибутов:** Функции `isValidAttrName` и `isValidAttrNames` проверяют, поддерживает ли текущий браузер заданные атрибуты.
3. **Загрузка CSS:** `loadDefaultCss` загружает CSS файл `/css/try_xpath_insert.css` из расширения.
4. **Извлечение стилей:** `extractBodyStyles` анализирует CSS и извлекает значения ширины и высоты для элемента `body`.
5. **Создание CSS:** `createPopupCss` генерирует CSS-строку для элемента `body` на основе извлеченных стилей.
6. **Обработка события загрузки:** Функция `addEventListener("load", ...)` обрабатывает событие загрузки страницы:
   - Получает значения атрибутов и CSS из браузерного хранилища.
   - Заполняет поля формы значениями из `res`.
   - Извлекает стили из `res.popupCss` и устанавливает их в поля формы.
   - Обрабатывает событие клика на кнопку "Сохранить":
     - Получает значения из полей формы.
     - Проверяет валидность атрибутов и стилей.
     - Если валидны, сохраняет значения в хранилище браузера.
     - Обновляет сообщение об успехе/неудачи.
   - Обрабатывает событие клика на кнопку "По умолчанию":
     - Заполняет поля формы значениями из `defaultAttributes` и `defaultPopupBodyStyles`.
     - Загружает и устанавливает CSS из файла `/css/try_xpath_insert.css`
   - Создает тестовый элемент (`div`) для проверки валидности атрибутов.

Пример: Пользователь меняет значение атрибута `element` и нажимает "Сохранить". Код проверяет `isValidAttrName` для нового значения. Если все корректно, значения сохраняются в хранилище.

## <mermaid>

```mermaid
graph TD
    A[window.addEventListener("load")] --> B{Получение значений из хранилища};
    B --> C[Заполнение полей формы];
    C --> D[Извлечение стилей];
    D --> E[Заполнение полей стилей];
    E --> F[Проверка валидности атрибутов и стилей];
    F -- Валидно --> G[Сохранение значений в хранилище];
    F -- Невалидно --> H[Вывод сообщения об ошибке];
    G --> I[Вывод сообщения об успехе];
    E --> J[Обработка клика на "По умолчанию"];
    J --> K[Установка значений по умолчанию];
    K --> L[Загрузка default CSS];
    J --> M[Вывод default CSS];
    style
    subgraph Загрузка default CSS
        L --> N[XMLHttpRequest];
        N --> O[Обработка ответа];
        O --> L
    end
    subgraph Обработка ответа
        O --> P[Установка значений в style];
    end
    subgraph Проверка валидности
        F --> Q[isValidAttrName];
        F --> R[isValidStyleLength];
    end
```

## <explanation>

**Импорты:**

- Нет прямых импортов из `src.`, но есть `tryxpath` и `tryxpath.functions`. Это скорее всего внутренние для этого расширения переменные или функции, которые предоставляют функциональность для работы с XPath и другими вещами, специфичными для расширения.

**Классы:**

- Нет явно объявленных классов.

**Функции:**

- `isValidAttrName`: Проверяет, является ли имя атрибута допустимым для установки. Использует `setAttribute`, чтобы проверить, возможно ли его установить.  Возвращает `true` или `false`.
- `isValidAttrNames`: Проверяет валидность всех имен атрибутов в объекте.
- `isValidStyleLength`: Проверяет, является ли строка длины стилей допустимой (например, "300px", "auto").  Возвращает `true` или `false`.
- `loadDefaultCss`: Загружает CSS файл из расширения. Использует `Promise` для асинхронной загрузки.
- `extractBodyStyles`: Парсит CSS-строку и извлекает ширину и высоту тела.
- `createPopupCss`: Формирует CSS-строку для тела, используя полученные ширину и высоту.
- `loadDefaultCss`:  Загружает дефолтный CSS файл с использованием XMLHttpRequest и промисов.

**Переменные:**

- `defaultAttributes`, `defaultPopupBodyStyles`: Константы, содержащие значения по умолчанию для атрибутов и стилей.
- `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`, `style`, `popupBodyWidth`, `popupBodyHeight`, `message`: Переменные, хранящие ссылки на HTML-элементы.
- `testElement`: Временный элемент для проверки атрибутов.


**Возможные ошибки/улучшения:**

- **Обработка ошибок при загрузке CSS:**  Обработка ошибок в `loadDefaultCss` (например,  `req.onerror`) была бы полезной для более надежной работы.
- **Проверка `browser`:** Код использует `browser`, что предполагает, что он находится в контексте Chrome Extension или подобного окружения. Необходимо убедиться, что `browser` корректно определен.
- **Проверка входных данных:** Проверка входных данных для функций, которые принимают строки (например, `extractBodyStyles`) может предотвратить нежелательные поведения или исключения.
- **Локализация сообщений:**  Если сообщение об ошибке или успехе предназначено для пользователя, рекомендуется использовать методы локализации.

**Цепочка взаимосвязей:**

Код взаимодействует с хранилищем браузера (`browser.storage.sync`) для сохранения и загрузки настроек, а также с расширением, вероятно, для загрузки CSS (`/css/try_xpath_insert.css`). Вероятно, есть другие части расширения, которые используют эти сохраненные настройки для определения свойств элементов, которые затем могут быть использованы веб-драйвером.