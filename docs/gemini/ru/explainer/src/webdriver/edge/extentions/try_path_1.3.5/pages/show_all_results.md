```MD
# Анализ кода show_all_results.js

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

    var detailKeys = ["type", "name", "value", "textContent"];
    var headerValues = ["Type", "Name", "Value", "textContent"];
    var relatedTabId;
    var relatedFrameId;
    var executionId;

    // ... (остальной код)
});
```

## <algorithm>

Код отображает результаты XPath запроса, полученные из расширения браузера.  Алгоритм работы можно представить в виде следующих шагов:

1. **Инициализация:**  При загрузке страницы устанавливаются `relatedTabId`, `relatedFrameId`, `executionId` и выполняются функции обработки кликов.
2. **Получение результатов:**  Через `browser.runtime.sendMessage` ожидает результаты выполнения запроса.
3. **Обработка результатов:**
    *  Если результаты получены, заполняет элементы HTML (`message`, `title`, `url`, `frame-id`, ...), отображающие информацию о запросе.
    *  Обрабатывает результаты `context` и `main`:
        *  Если `context` есть, заполняет элементы HTML для контекстных данных, и вызывает `fu.updateDetailsTable` для отображения таблицы `context-detail`.
        *  Если `context` отсутствует, удаляет область `context-area`.
        *  Заполняет элементы HTML для основных данных (`main`), вызывает `fu.updateDetailsTable` для отображения таблицы `main-details`.
4. **Создание URL для скачивания:**  Генерирует URL для скачивания текстовых файлов с информацией о результатах (в обычном и преобразованном форматах).
5. **Обработка кликов:**  Обрабатывает клики по кнопкам в таблицах (`context-detail`, `main-details`), отправляя сообщения в активную вкладку браузера для навигации.

**Пример:** Если результаты содержат контекстные данные, функция `showAllResults` заполняет соответствующие поля, а `fu.updateDetailsTable` обновляет таблицу. В противном случае удаляется ненужная область.


## <mermaid>

```mermaid
graph LR
    A[Загрузка страницы] --> B{Получение результатов (browser.runtime.sendMessage)};
    B -- Результаты есть --> C[Обработка результатов];
    B -- Результатов нет --> D[Обработка отсутствия результатов];
    C --> E[Заполнение элементов HTML];
    C --> F[Обработка context];
    C --> G[Обработка main];
    F -- context есть --> H[fu.updateDetailsTable (context-detail)];
    F -- context нет --> I[Удаление context-area];
    G --> J[fu.updateDetailsTable (main-details)];
    C --> K[Генерация URL для скачивания];
    C --> L[Обработка кликов];
    L --> M[Отправка сообщений в активную вкладку браузера];
    D --> N[Нет действий];
```

**Объяснение зависимостей:**

* `browser`: Подключает к расширению браузера для взаимодействия с вкладками и другими функциями.
* `tryxpath`: Основной модуль, предоставляющий функции для работы с XPath, `tryxpath.functions` – подмодуль, предоставляющий вспомогательные функции.  Связь через `tx` и `fu`.
* `window`, `document`:  Стандартные объекты браузера.
* `URL`, `Blob`: Стандартные функции JavaScript для работы с URL и объектами Blob.
* `JSON.stringify`:  Функция для сериализации JavaScript объектов в JSON.

## <explanation>

**Импорты:**

* `tryxpath` и `tryxpath.functions` - предполагаются как объекты, содержащие функции, вероятно, относящиеся к обработке XPath-запросов и связанных задач. Они импортируются как `tx` и `fu` соответственно.  Это компоненты из другого файла проекта, связанного с `src`.


**Классы:**

Нет явных определений классов.  Функции и переменные работают с данными и DOM-элементами.

**Функции:**

* `showAllResults(results)`:  Основная функция для обработки и отображения результатов. Принимает объект `results` с данными и обновляет HTML элементы, отображающие данные запроса. Возвращаемого значения нет.
* `makeTextDownloadUrl(text)`: Создаёт URL для скачивания текстового контента. Принимает строку `text`, создаёт объект `Blob` и возвращает URL для скачивания.
* `makeInfoText(results)` и `makeConvertedInfoText(results)`: Форматируют результаты в текстовый формат для скачивания,  различая форматирование в зависимости от нужд.
* `fu.updateDetailsTable(tableBody, details, options)`:  Функция, вероятно, из `tryxpath.functions`, обновляет таблицу `tableBody` данными `details`.


**Переменные:**

* `detailKeys`, `headerValues`: Массивы строк, используемые для определения и заголовков столбцов таблицы.
* `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для сохранения информации о контексте выполнения.
* `document`: Объект `document` текущей HTML страницы.

**Возможные ошибки/улучшения:**

* **Обработка ошибок:** Обработка ошибок `catch(fu.onError)` используется, но стоит проверить, чтобы `fu.onError` тоже корректно обрабатывала ошибки.
* **Валидация данных:** Не хватает валидации данных, например проверки на null или undefined для `results` или `cont`.
* **`fu.updateDetailsTable`:** Нужно понимать, как `fu.updateDetailsTable` работает, есть ли внутри обработка ошибок, и как это влияет на работу функции `showAllResults`.
* **Использование `JSON.stringify`:**  Применение `JSON.stringify` для отображения  `expression` может привести к проблеме отображения в случае не-строк.  Стоит проверить `expression`, прежде чем отображать в JSON формате.

**Взаимосвязи с другими частями проекта:**

Расширение браузера (`browser`) взаимодействует с расширением для получения данных.  `tryxpath` и `tryxpath.functions` – очевидно, это другие модули, относящиеся к XPath обработке, расположенные вероятно в другом месте проекта `src`.  На основе кода можно предположить, что это часть проекта, занимающегося поддержкой XPath запросов.