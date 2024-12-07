# Анализ кода show_all_results.js

```
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;

    function showAllResults(results) {
        // ... (код функции)
    };

    // ... (остальной код)
})(window);
```

## <algorithm>

**Пошаговая блок-схема:**

1. **Инициализация:**
   - Alias для `tryxpath` и `tryxpath.functions`.
   - Получение `document` из `window`.
   - Определение массивов `detailKeys` и `headerValues` для структуры данных.
   - Инициализация переменных `relatedTabId`, `relatedFrameId`, `executionId` (null или undefined).

2. **Функция `showAllResults(results)`:**
   - Заполнение элементов HTML (`message`, `title`, `url`, `frame-id`) данными из `results`.
   - **Ветвление:**
     - Если `results.context` существует:
       - Заполнение элементов HTML (`context-method`, `context-expression`, `context-specified-result-type`, `context-result-type`, `context-resolver`) данными из `results.context`.
       - Вызов `fu.updateDetailsTable` для заполнения таблицы `context-detail` данными из `cont.itemDetail`. Обработка ошибки с помощью `.catch(fu.onError)`.
     - Если `results.context` не существует:
       - Удаление элемента `context-area`.
   - Заполнение элементов HTML (`main-method`, `main-expression`, `main-specified-result-type`, `main-result-type`, `main-resolver`, `main-count`) данными из `results.main`.
   - Вызов `fu.updateDetailsTable` для заполнения таблицы `main-details` данными из `main.itemDetails`. Обработка ошибки с помощью `.catch(fu.onError)`.

3. **Функции `makeTextDownloadUrl`, `makeInfoText`, `makeConvertedInfoText`:**
   - Генерируют текстовые данные для загрузки файла (формат).

4. **Event Listener `window.addEventListener("load")`:**
   - Отправляет сообщение `browser.runtime.sendMessage({"event":"loadResults"})` в контекст расширения.
   - Обрабатывает `results` при получении ответа:
     - Присваивает значения переменным `relatedTabId`, `relatedFrameId`, `executionId`.
     - Устанавливает атрибуты `href` и `download` для элементов `export-text` и `export-partly-converted` с использованием `makeTextDownloadUrl` и `makeInfoText`, `makeConvertedInfoText`.
     - Вызывает `showAllResults(results)`.
     - Обрабатывает ошибки с помощью `.catch(fu.onError)`.
   - Добавляет Event Listener на `context-detail` для обработки нажатия на кнопки (переход по элементам контекста).
   - Добавляет Event Listener на `main-details` для обработки нажатия на кнопки (переход по элементам результата).


**Примеры данных:**

`results`:
```javascript
{
  "message": "Message",
  "title": "Title",
  "href": "URL",
  "frameId": 123,
  "context": { /* ... */ },
  "main": { /* ... */ }
}
```

`results.context.itemDetail`: массив объектов с деталями.


## <mermaid>

```mermaid
graph TD
    A[window.addEventListener("load")] --> B{Получить данные из расширения};
    B --> C[showAllResults(results)];
    C --> D{Заполнение HTML элементов};
    D -- results.context существует --> E[Заполнение context-деталей];
    D -- results.context не существует --> F[Удаление context-area];
    E --> G[fu.updateDetailsTable (context)];
    F --> C;
    G --> H{Заполнение main-деталей};
    H --> I[fu.updateDetailsTable (main)];
    C --> J[Экспорт текста];
    J --> K[Загрузка файлов];
    C --> L[Обработка событий кликов];
    L -- context-detail --> M[browser.tabs.sendMessage (focusContextItem)];
    L -- main-details --> N[browser.tabs.sendMessage (focusItem)];

    subgraph Функции
        C --> O[makeTextDownloadUrl];
        O --> K;
        C --> P[makeInfoText];
        C --> Q[makeConvertedInfoText];
    end
```

## <explanation>

**Импорты:**

- `tryxpath` и `tryxpath.functions`:  Предполагается, что `tryxpath` - это модуль, который содержит функции для работы с XPath, а `tryxpath.functions` - объект, содержащий вспомогательные функции (например, `updateDetailsTable`, `onError`). Эти импорты призваны упростить работу с XPath-выражениями.  `src` - это корневая папка проекта.

**Классы:**

Нет явных классов. Функции являются основными структурными элементами.

**Функции:**

- `showAllResults(results)`:  Получает результаты поиска и обновляет соответствующие элементы на странице. Принимает объект `results` с результатами.
- `makeTextDownloadUrl(text)`: Создает URL для загрузки текста. Принимает строку `text` и возвращает строку URL.
- `makeInfoText(results)`: Создаёт текст для экспорта (с данными). Принимает объект `results` и возвращает строку.
- `makeConvertedInfoText(results)`: Аналогично `makeInfoText`, но с JSON-конвертацией.
- Внутренние функции из `tryxpath.functions`:
    - `updateDetailsTable`: Заполняет таблицу данными из массива.
    - `onError`: Обрабатывает ошибки.

**Переменные:**

- `detailKeys`, `headerValues`: Массивы строк, используемые для определения столбцов в таблицах.
- `relatedTabId`, `relatedFrameId`, `executionId`: Хранят ID для связи с табом и фреймом.

**Возможные ошибки и улучшения:**

- **Обработка ошибок:** В коде присутствует `catch(fu.onError)`, что улучшает устойчивость. Но  важно добавить логирование ошибок для отладки.
- **Универсальность `fu.updateDetailsTable`:**  Непонятно, как обрабатываются ошибки в `fu.updateDetailsTable`. Лучше сделать обработку ошибок более явной и использовать подходящие исключения.
- **Проверка ввода:** Можно добавить проверку типов и валидацию данных `results` для предотвращения ошибок.
- **Использование констант:**  Использование констант (например, для имен элементов) может сделать код более читаемым и поддерживаемым.

**Взаимосвязи с другими частями проекта:**

Функция `browser.runtime.sendMessage` указывает на взаимодействие с контекстом расширения браузера. Функции `browser.tabs.sendMessage` показывают, что код связан с управлением вкладками и фреймами.  Код в данном файле `show_all_results.js` получает данные от `tryxpath` (возможно, другая часть расширения или приложение), отображает их и предоставляет механизмы для взаимодействия с результатами. Необходимы данные о реализации `tryxpath`, чтобы полностью понять эту связь.


**Вывод:**

Код реализует отображение результатов поиска,  полученных от другого компонента расширения.  Он имеет хорошо структурированный дизайн, включая разделение на функции для обработки разных частей. Важно понимать функциональность `tryxpath` и `fu` для более полного анализа.