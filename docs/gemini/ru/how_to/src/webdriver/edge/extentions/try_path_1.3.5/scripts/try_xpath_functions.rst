Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код JavaScript содержит набор функций для работы с узлами DOM (Document Object Model) и XPath выражениями.  Он предоставляет методы для выполнения XPath запросов, выбора элементов с помощью `querySelector` и `querySelectorAll`, обработки результатов запроса, получения и работы с деталями узлов (типы, имена, значения, текст).  Кроме того, функции позволяют сохранять и восстанавливать атрибуты элементов, работать со строками, числами, булевыми значениями, и выполнять дополнительные операции, такие как нахождение родительских элементов, предков, фреймов, и т.д. Код предназначен для использования в браузерной среде и взаимодействует с объектами DOM.


Шаги выполнения
-------------------------
1. **Инициализация пространства имен:** Код определяет пространство имен `tryxpath` и `tryxpath.functions`. Если пространство имен уже существует, выполнение функции прекращается, что предотвращает повторное выполнение кода.
2. **Функция `execExpr`:**
    * Принимает XPath выражение, метод (`evaluate`, `querySelector`, или `querySelectorAll`), и опции.
    * Выбирает контекст выполнения (по умолчанию - текущий документ).
    * Использует `doc.evaluate()` для выполнения XPath запроса, если метод `evaluate`.  Обрабатывает исключение, если контекст не узел или атрибут.
    * Использует `context.querySelector()` или `context.querySelectorAll()` для выбора элементов, если метод `querySelector` или `querySelectorAll` соответственно.  Обрабатывает исключения, если контекст не документ или элемент.
    * Возвращает результат запроса в формате объекта с полями `items` (массив результатов), `method` (используемый метод) и `resultType` (тип результата).
3. **Функция `resToArr`:** преобразует результат выполнения XPath в массив, обрабатывая различные типы результатов (числа, строки, булевые значения, узлы).
4. **Функция `makeResolver`:** Создает функцию-резолвер, которая обрабатывает заданный резолвер.  Может принимать строку JSON или объект. Возвращает функцию, которая для заданной строки ищет соответствующее значение из объекта (резолвера). Проверяет корректность резолвера.
5. **Функции работы с узлами DOM:**  `isDocOrElem`, `listToArr`, `getItemDetail`, `getItemDetails`, `addClassToItem`, `addClassToItems`, `saveItemClass`, `restoreItemClass`, `saveItemClasses`, `restoreItemClasses`, `setAttrToItem`, `removeAttrFromItem`, `removeAttrFromItems`, `setIndexToItems`, `getParentElement`, `getAncestorElements`, `getOwnerDocument`, `createHeaderRow`, `createDetailTableHeader`, `createDetailRow`, `appendDetailRows`, `updateDetailsTable`, `emptyChildNodes`,  и другие. Каждая функция выполняет определенную операцию с элементами DOM, например, проверка типов узлов, получение атрибутов, добавление или удаление классов, создание таблиц и строк для отображения результатов.
6. **Функции проверки типов:** `isNumberArray`, `isAttrItem`, `isNodeItem`, `isElementItem`, `isBlankWindow`, `collectBlankWindows`, `findFrameElement`, `findFrameIndex`. Выполняют проверки типов данных и элементов DOM.
7. **Функция `onError`:** Обрабатывает возможные ошибки во время выполнения.
8. **Функция `makeDetailText`:**  Создаёт строку из деталей элемента, с возможностью пользовательской замены частей.


Пример использования
-------------------------
.. code-block:: javascript

    // Выполнить XPath запрос
    let result = tryxpath.functions.execExpr(
        '//div[@class="myClass"]',
        'evaluate',
        { context: document }
    );

    // Обработка результатов
    let items = result.items;
    for (let item of items) {
        let details = tryxpath.functions.getItemDetail(item);
        console.log(details);
    }


    // Добавление класса к элементу
    let elem = document.querySelector('p');
    tryxpath.functions.addClassToItem('highlight', elem);


    // Извлечение атрибутов элемента и сохранение
    let item = document.getElementById('myElement');
    let savedAttrs = tryxpath.functions.saveAttrForItem(item, "data-id", null, false);
    // После использования можно восстановить:
    // tryxpath.functions.restoreItemAttrs(savedAttrs)