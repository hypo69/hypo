# Анализ кода try_path_1.3.5/pages/options.js

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

    // ... (rest of the code)
```

## <algorithm>

(Блок-схема не приводится из-за сложности визуализации)

Код реализует загрузку и сохранение настроек расширения `tryxpath`.  Алгоритм можно разделить на следующие этапы:

1. **Инициализация:** Определяются переменные, связанные с элементами страницы (атрибуты, стили, сообщение об ошибках), а также `defaultAttributes` и `defaultPopupBodyStyles`.
2. **Загрузка данных:** При загрузке страницы происходит запрос настроек к `browser.runtime` с событием `loadOptions`.  Полученные данные (атрибуты, CSS, стили всплывающего окна) сохраняются в соответствующие поля формы.
3. **Вадидация:** Проверка корректности введённых атрибутов (isValidAttrName, isValidAttrNames) и CSS/стилей (isValidStyleLength)
4. **Сохранение:** При нажатии на кнопку "Сохранить" данные из полей формы сохраняются в хранилище `browser.storage.sync` (в объекте `attributes`, `css`, `popupCss`).
5. **Обработка ошибок:** Обработка ошибок во время запроса и сохранения.
6. **Загрузка по умолчанию:** При нажатии на кнопку "Показать по умолчанию" все поля формы устанавливаются на значения из `defaultAttributes` и `defaultPopupBodyStyles`.  В этот момент происходит загрузка `try_xpath_insert.css`.

## <mermaid>

```mermaid
graph TD
    A[window.addEventListener("load")] --> B{Загрузка настроек};
    B --> C[Запрос настроек к browser.runtime];
    C --> D[Обработка ответа];
    D --> E[Установка значений в поля формы];
    E --> F[Проверка корректности данных];
    F -- Корректно --> G[Сохранение в браузер.storage.sync];
    F -- Некорректно --> H[Вывод сообщения об ошибке];
    G --> I[Успешное сохранение];
    H --> I;
    I --> J[Кнопка "Показать по умолчанию"];
    J --> K[Установка значений по умолчанию];
    K --> L[Загрузка try_xpath_insert.css];
    L --> E;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style H fill:#fcc,stroke:#990,stroke-width:2px;

```

## <explanation>

**Импорты:**

Код не использует импорты в привычном для современных языков программирования стиле (`import`).  Вместо этого используется синтаксис, характерный для более старых подходов к JavaScript.

**Классы:**

Нет явных классов. Всё реализовано с помощью функций.

**Функции:**

* `isValidAttrName(name)`: Проверяет, является ли имя атрибута допустимым. Попытка установить атрибут с недопустимым именем вызывает исключение.
* `isValidAttrNames(names)`: Проверяет, являются ли все имена атрибутов допустимыми.
* `isValidStyleLength(len)`: Проверяет, является ли строка со стилем ширины или высоты валидной.
* `loadDefaultCss()`: Загружает CSS из файла `/css/try_xpath_insert.css` с помощью `XMLHttpRequest` и `browser.runtime.getURL`. Возвращает промис, содержащий текст CSS.
* `extractBodyStyles(css)`: Извлекает ширину и высоту из CSS текста.
* `createPopupCss(bodyStyles)`: Создает строку CSS для стилей всплывающего окна.


**Переменные:**

* `defaultAttributes`, `defaultPopupBodyStyles`:  Константы, содержащие значения по умолчанию для атрибутов и стилей всплывающего окна.
* `elementAttr`, `contextAttr`, ...: Переменные, содержащие ссылки на элементы DOM.

**Возможные ошибки и улучшения:**

* **Обработка ошибок `loadDefaultCss`**: Обработка ошибок в промисе `loadDefaultCss` улучшена бы использованием `catch`.
* **Добавление валидации типов данных**: Проверка типов данных в переменных, принимаемых функциями, могла бы улучшить устойчивость к ошибкам.
* **Использование fetch API**: Загрузка ресурсов с помощью `fetch` API была бы более современным и гибким подходом, по сравнению с `XMLHttpRequest`.

**Взаимосвязь с другими частями проекта:**

Функция `browser.runtime.sendMessage` указывает на связь с другими частями расширения, которые отвечают на запросы и передают данные. Функция `browser.storage.sync.set` взаимодействует с хранилищем настроек расширения. Файл `/css/try_xpath_insert.css` — это внешний ресурс, используемый для настройки элементов пользовательского интерфейса расширения.  Функции `fu.onError` и `tryxpath` намекают на существование модуля или функции, обрабатывающей ошибки.