Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот JavaScript-код содержит функции для работы с XPath, выборщиками CSS и элементами DOM. Он предоставляет методы для оценки XPath выражений, выбора элементов с помощью `querySelector` и `querySelectorAll`, получения информации об элементах (тип, имя, значение, текстовое содержимое), сохранения и восстановления атрибутов элементов, создания таблиц и обработки ошибок.  Функции предназначены для работы с различными типами элементов DOM, включая узлы, атрибуты, числа и строки.

Шаги выполнения
-------------------------
1. **Инициализация контекста:** Функции работают с объектом `document` (или указанным `context` в параметрах).  Код определяет `tryxpath.functions` как глобальный объект, что позволяет использовать функции в других скриптах.

2. **Выполнение выражений:** Функция `fu.execExpr` позволяет выполнять XPath выражения (`method = "evaluate"`), запрос CSS селекторов `querySelector`, `querySelectorAll` задав подходящий `method`.

3. **Обработка результатов:** `fu.execExpr` возвращает объект с результатами (`items` - массив элементов,  `method` - метод который был использован, `resultType` - тип результата). `fu.resToArr` преобразует результаты `evaluate` в массив. Обрабатываются различные типы результатов XPath (числа, строки, булевы значения, итераторы узлов и т.д.).

4. **Работа с DOM элементами:** Функции `fu.getItemDetail`, `fu.getItemDetails` и `fu.getFrameAncestry`  предоставляют средства для работы с элементами DOM, такие как получение информации об элементе, получение списка элементов, нахождения предков в иерархии фреймов.

5. **Сохранение и восстановление атрибутов:**  `fu.saveItemClass`, `fu.restoreItemClass`, `fu.saveItemClasses`, `fu.restoreItemAttrs` дают возможность сохранять и восстанавливать классы и атрибуты элементов для дальнейшего использования.

6. **Создание таблиц:** `fu.createHeaderRow`, `fu.createDetailTableHeader`, `fu.createDetailRow`, `fu.appendDetailRows`, `fu.updateDetailsTable`  реализуют функции для создания и заполнения таблиц в DOM.

7. **Управление ошибками:** Функции `fu.onError` обрабатывают и выдают информацию об ошибках.


Пример использования
-------------------------
.. code-block:: javascript

    // Получить все элементы с классом 'myClass'
    tryxpath.functions.execExpr("//div[@class='myClass']", "evaluate",
                                  {context: document}).then(result => {
        // Обработка результата
        const items = result.items;
        for (let item of items) {
          console.log(tryxpath.functions.getItemDetail(item));
        }
    });

    // Добавить класс к элементам
    tryxpath.functions.addClassToItems('highlight', document.querySelectorAll('p'));

    // Создать таблицу
    let details = [ /* ... данные для таблицы ... */];
    let tableContainer = document.getElementById('myTable');
    tryxpath.functions.updateDetailsTable(tableContainer, details);

    // Сохранение и восстановление атрибутов
    const storage = new Map();
    tryxpath.functions.saveAttrForItems(document.querySelectorAll('a'), 'target', storage);
    // ... работа с данными ...
    tryxpath.functions.restoreItemAttrs(storage);