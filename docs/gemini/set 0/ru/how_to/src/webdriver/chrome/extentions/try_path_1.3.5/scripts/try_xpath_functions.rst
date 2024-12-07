Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот JavaScript-код содержит набор функций, предназначенных для работы с узлами DOM (Document Object Model) и XPath выражениями.  Функции позволяют выполнять XPath запросы, получать элементы с помощью querySelector/querySelectorAll, обрабатывать результаты, сохранять и восстанавливать атрибуты элементов, создавать таблицы, и выполнять дополнительные операции, связанные с DOM.  Код организован в виде пространства имён `tryxpath.functions`.

Шаги выполнения
-------------------------
1. **Инициализация пространства имён:**  Код проверяет, существует ли пространство имён `tryxpath.functions`. Если нет, создаёт его. Это делается для предотвращения ошибок, если код используется многократно.

2. **Функция `execExpr`:** Основная функция для выполнения XPath выражений, `querySelector` и `querySelectorAll`. Она принимает XPath выражение, метод выполнения (`evaluate`, `querySelector`, `querySelectorAll`), и опционально `opts` - объект с параметрами (например, `context`, `resolver`, `document`).
   - **Выбор метода:**  В зависимости от заданного метода, выполняется соответствующая операция.
   - **Проверка контекста:** Функция проверяет, является ли контекст (`context`) элементом или документом, выбрасывая ошибку при несоответствии.
   - **Выполнение запроса:** Выполняет XPath запрос или выбор элементов с помощью `querySelector` или `querySelectorAll` в зависимости от указанного `method`.
   - **Обработка результатов:** Функция обрабатывает результат запроса и возвращает объект, содержащий массив найденных элементов (`items`), используемый метод (`method`), и тип результата (`resultType`). Если `resultType` равен `xpathResult.ANY_TYPE`, он обновляется до актуального типа из результата запроса.

3. **Функция `resToArr`:** Преобразует результат XPath запроса (объект `res`) в массив (`arr`).
   - **Определение типа результата:** При необходимости определяет тип результата `res.resultType` для корректной обработки.
   - **Обработка различных типов результатов:** Обрабатывает различные типы XPath результатов (число, строка, булево значение, итераторы узлов, снифснэпшоты узлов) и добавляет соответствующие значения в массив.

4. **Функция `makeResolver`:** Создаёт функцию-резолвер для XPath запроса.
   - **Обработка null:** Проверяет, если `resolver` равен `null`, то возвращает `null`.
   - **Обработка функции:** Если `resolver` - функция, возвращает её напрямую.
   - **Обработка строки:** Если `resolver` - строка, парсит её как JSON и возвращает функцию-резолвер.
   - **Обработка объекта:** Если `resolver` - объект, создаёт карту `Map` из его свойств и возвращает функцию-резолвер, которая возвращает значение из карты по ключу.
   - **Обработка ошибок:** Если входные данные некорректны, выводит ошибку.

5. **Дополнительные функции:**  Код содержит множество вспомогательных функций, таких как проверка типов узлов, преобразование списков в массивы, извлечение свойств узлов и др. Эти функции обеспечивают гибкость и расширяемость кода.

6. **Функция `updateDetailsTable`:**  Создаёт и обновляет таблицу, отображающую детали элементов DOM.  Принимает родительский элемент (`parent`), массив деталей (`details`), и опционально `opts` для настройки. Очищает существующее содержимое родительского элемента и добавляет заголовок таблицы, а затем добавляет строки с подробностями элементов.

7. **Функция `saveItemClass`, `restoreItemClass`:** Сохраняют/восстанавливают атрибут "class" элементов.


Пример использования
-------------------------
.. code-block:: javascript

    // Предполагается, что в документе есть элемент с id 'myElement'
    const myElement = document.getElementById('myElement');
    
    // Выполните XPath запрос
    tryxpath.functions.execExpr('//div[@id="someDiv"]/p', 'evaluate', {
        context: myElement,
        resultType: xpathResult.ORDERED_NODE_SNAPSHOT_TYPE
    }).then(result => {
        // Обработка результатов
        const items = result.items;
        for (let i = 0; i < items.length; i++) {
          console.log(items[i].textContent);
        }
    });