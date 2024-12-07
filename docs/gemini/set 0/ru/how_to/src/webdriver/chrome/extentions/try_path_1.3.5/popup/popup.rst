Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код JavaScript отвечает за взаимодействие с расширением браузера, реализующим поиск по XPath. Он обрабатывает пользовательские вводы, отправляет запросы в активную вкладку браузера, получает и отображает результаты поиска.  Код включает функции для управления отображением различных элементов интерфейса, отправки сообщений в активную вкладку и обработку ответов от контентного скрипта.

Шаги выполнения
-------------------------
1. **Инициализация элементов:** Код получает ссылки на все элементы интерфейса (кнопки, текстовые поля, таблицы), необходимые для работы с расширением.

2. **Обработка событий кликов:** При нажатии определенных кнопок (например, "execute", "previous-details-page", "next-details-page") вызываются соответствующие функции для выполнения заданных действий.

3. **Создание сообщений для отправки:**  Функция `makeExecuteMessage()` собирает данные из полей ввода (XPath, параметры контекста и т.д.) в структурированное сообщение `msg` для отправки в активную вкладку.

4. **Отправка сообщений в активную вкладку:**  Функция `sendToActiveTab()` отправляет сформированное сообщение в активную вкладку браузера. Функция `sendToSpecifiedFrame()` модифицирует отправку сообщений, добавляя обработку выбранного кадра.

5. **Обработка ответов от контентного скрипта:**  В функции `genericListener` обрабатываются сообщения, возвращаемые контентным скриптом. Принимая данные (результаты поиска), код заполняет таблицы результатами.  Функция `showError` используется для отображения сообщений об ошибках.

6. **Обновление отображения:** Код обновляет отображаемые данные в таблице результатов и обновляет отображаемые поля. Функции `showDetailsPage` управляет отображением страниц результатов, а `showError` отвечает за вывод сообщений об ошибках.

7. **Обработка пользовательского ввода:** Функция `handleExprEnter` реагирует на нажатие Enter в полях ввода XPath.

8. **Сохранение состояния:**  Перед закрытием вкладки функция `window.addEventListener("unload", ...)` собирает текущее состояние (состояние элементов, параметры поиска, т.д.) и отправляет его в хранилище расширения.

9. **Загрузка стилей:**  `browser.runtime.sendMessage({ "event": "requestInsertStyleToPopup"})` запрашивает и применяет стили, необходимые для отображения элементов.


Пример использования
-------------------------
.. code-block:: javascript

    // Предположим, что у вас есть элементы с id "main-expression" и "execute".
    // В этом случае, для запуска поиска по XPath:
    document.getElementById("main-expression").value = "//a[@href]"; // Ваш XPath
    document.getElementById("execute").click();