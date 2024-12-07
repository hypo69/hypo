Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код JavaScript отвечает за загрузку и сохранение настроек расширения, связанного с обработкой XPath. Он получает значения атрибутов, стилей, загружает CSS и сохраняет их в хранилище браузера.  Код также проверяет валидность введенных данных. Если данные некорректны, выводит сообщение об ошибке. При нажатии кнопки "Показать значения по умолчанию" восстанавливаются значения по умолчанию.

Шаги выполнения
-------------------------
1. **Инициализация переменных:** Код инициализирует переменные, представляющие элементы DOM (элементы формы, поле сообщения и т.д.).
2. **Запрос настроек:** Код отправляет запрос в хранилище браузера (`browser.runtime.sendMessage`) для получения текущих настроек расширения.
3. **Установка значений в поля:** Полученные из хранилища значения устанавливаются в соответствующие поля формы.
4. **Обработка события "сохранить":** При нажатии кнопки "Сохранить" выполняется функция, которая:
    - Читает значения из полей формы.
    - Проверяет валидность атрибутов и стилей.
    - Если значения валидны, сохраняет настройки в браузерное хранилище (`browser.storage.sync.set`).
    - Если значения невалидны, выводит сообщение об ошибке.
5. **Обработка события "показать значения по умолчанию":** При нажатии этой кнопки:
    - Заполняются поля формы значениями по умолчанию.
    - Выполняется загрузка CSS по умолчанию (`loadDefaultCss`).
6. **Загрузка CSS:** Функция `loadDefaultCss` загружает CSS-файл `/css/try_xpath_insert.css` с помощью `XMLHttpRequest`.
7. **Извлечение стилей:** Функция `extractBodyStyles` извлекает значения ширины и высоты из CSS-текста.
8. **Создание CSS для всплывающего окна:** Функция `createPopupCss` создает CSS-правила для стилей всплывающего окна.
9. **Обработка ошибок:** При неудачных запросах или операциях сохранения, код обрабатывает ошибки и выводит соответствующее сообщение пользователю.


Пример использования
-------------------------
.. code-block:: javascript
    // Предполагаем, что у нас есть форма с элементами:
    // element-attribute, context-attribute, ...
    // popup-body-width, popup-body-height, style, save, show-default

    // ... (вставка кода для инициализации) ...

    // Пример сохранения
    document.getElementById("save").addEventListener("click", function() {
        // ... (код проверки валидности) ...
        browser.storage.sync.set({
            "attributes": {
                "element": "data-tryxpath-element",
                "context": "data-tryxpath-context"
            },
            "css": "#element-css { width: 100px; }",
            "popupCss": "body{width:367px;height:auto;}"
        })
        .then(() => {
            // Успешно сохранено
        })
        .catch(err => {
            // Обработка ошибок
            console.error("Ошибка сохранения", err);
        });
    });