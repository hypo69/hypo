# Анализ кода try_xpath_background.js

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

    var popupState = null;
    var popupCss = "body{width:367px;height:auto;}";
    var results = {};
    var css = "";
    var attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
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
    }

    // ... (остальной код)
```

## <algorithm>

**Алгоритм:**

Код устанавливает обработчики событий для сообщений, получаемых от вкладок.
1. **Инициализация:**
   - `tx`, `fu`: алиасы для `tryxpath` и `tryxpath.functions` (для краткости).
   - `popupState`, `popupCss`, `results`, `css`, `attributes`: инициализация переменных, хранящих состояние всплывающего окна, CSS стили, результаты поиска и атрибуты.
2. **Загрузка стилей:**
   - `loadDefaultCss()`: загружает стили из `/css/try_xpath_insert.css` с помощью `XMLHttpRequest` и `Promise`.
   - **Пример:** Запрос на сервер `/css/try_xpath_insert.css` возвращает ответ в виде строки CSS.
3. **Обработка сообщений:**
   - `genericListener`: обработчик сообщений, который определяет тип сообщения и вызывает соответствующую функцию.
   - **Пример:** Если сообщение `storePopupState`, вызывается функция `genericListener.listeners.storePopupState`.
   - **Внутри `genericListener.listeners`**: набор функций для обработки разных типов сообщений, таких как:
    - `storePopupState`: сохраняет состояние всплывающего окна.
    - `requestRestorePopupState`: востанавливает состояние всплывающего окна.
    - `requestInsertStyleToPopup`: отправляет стили в всплывающее окно.
    - `showAllResults`: обрабатывает результаты поиска и создает новую вкладку для их отображения.
    - `loadResults`: возвращает результаты поиска.
    - `updateCss`: загружает и удаляет CSS стили.
    - `loadOptions`: возвращает атрибуты, css и popupCss.
    - `requestSetContentInfo`: отправляет атрибуты во вкладку.
4. **Синхронизация данных:**
   - `browser.storage.onChanged.addListener`: следит за изменениями в хранилище браузера (`attributes`, `css`, `popupCss`).
   - **Пример:** Если изменились `attributes`, то они обновляются.
5. **Загрузка настроек:**
   - `browser.storage.sync.get`: загружает настройки из браузерного хранилища (`attributes`, `css`, `popupCss`).
   - `loadDefaultCss()`: если `css` не загружено, то загружается по умолчанию.
   - **Пример:** `attributes` обновляются из хранилища, а если `css` нет, то загружается из файла по умолчанию.


## <mermaid>

```mermaid
graph LR
    A[try_xpath_background.js] --> B(Инициализация);
    B --> C{Загрузка стилей};
    C --> D[loadDefaultCss];
    D --> E{Обработка сообщений};
    E --> F[genericListener];
    F --> G[storePopupState];
    F --> H[requestRestorePopupState];
    F --> I[requestInsertStyleToPopup];
    F --> J[showAllResults];
    F --> K[loadResults];
    F --> L[updateCss];
    F --> M[loadOptions];
    F --> N[requestSetContentInfo];
    F --> O{Синхронизация данных};
    O --> P[browser.storage.onChanged.addListener];
    E --> Q{Загрузка настроек};
    Q --> R[browser.storage.sync.get];
    R --> S[loadDefaultCss (если css не задано)];
    S --> T[Загрузка CSS];
    T --> U[css = loadedCss];
    U --> E;
    
    subgraph Хранилище браузера
        P --> V[attributes, css, popupCss];
    end
    subgraph Вкладки браузера
        G --> W[Всплывающее окно];
        H --> X[Всплывающее окно];
        I --> Y[Всплывающее окно];
        J --> Z[Новая вкладка];
        K --> AA[Вкладка];
        L --> AB[Вкладка];
        M --> AC[Вкладка];
        N --> AD[Вкладка];
    end
```

## <explanation>

**Импорты:**

- `tryxpath` и `tryxpath.functions`:  Предполагается, что эти модули определены в другом месте проекта (`src.`) и содержат функции, необходимые для работы расширения, например, функции обработки ошибок (`fu.onError`).

**Классы:**

- Нет явных классов. Код использует функции и переменные.

**Функции:**

- `loadDefaultCss()`: Загружает CSS из файла `/css/try_xpath_insert.css`  и возвращает его текст как промис.  Возвращаемое значение - `Promise`, содержащий результат загрузки.
- `genericListener()`: Обработчик сообщений. Находит слушатель `message.event` и вызывает соответствующую функцию `genericListener.listeners`.
- Все функции в `genericListener.listeners`: обрабатывают различные типы сообщений. Пример: `updateCss` обновляет CSS стили во вкладках, используя `browser.tabs.insertCSS` и `browser.tabs.removeCSS`.

**Переменные:**

- `popupState`, `popupCss`, `results`, `css`, `attributes`:  Хранят различные состояния и данные, связанные с расширением.
- `attributes`:  Словарь, содержащий атрибуты элементов, используемые в `tryxpath`.

**Возможные ошибки и улучшения:**

- Отсутствие обработки ошибок в `loadDefaultCss`: Необходимо добавить `reject` в `Promise` для обработки случаев, когда загрузка CSS не удалась.
- Отсутствие явного `try...catch` вокруг `browser.storage.sync.get`:  Хотя `.then`/`.catch` в коде используются, рекомендуется обернуть в `try...catch` для предотвращения падения всего скрипта при ошибках.
- Недостаточная проверка типов данных, передаваемых в функции (`message`, `sender`).

**Взаимосвязь с другими частями проекта:**

- `browser.runtime.getURL()`: Подключается к механизму runtime браузера для получения абсолютного URL ресурса.
- `browser.runtime.onMessage`: Подключается к системе коммуникации браузера, что подразумевает взаимодействие с другими частями проекта.
- `browser.tabs.insertCSS`, `browser.tabs.removeCSS`, `browser.tabs.sendMessage`:  Работают с API вкладок браузера, что предполагает использование в других частях проекта (например, в popup-странице или содержимом вкладок).
- `tryxpath` и `tryxpath.functions`:  Указывают на наличие взаимосвязей с другими частями проекта, где эти функции используются.
- `/css/try_xpath_insert.css`: указывает на использование внешних ресурсов для стилизации расширения.
- `/pages/show_all_results.html`:  указывает на наличие html файла для отображения результатов.