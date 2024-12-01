Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот JavaScript-код отображает результаты поиска, полученные из расширения браузера. Он получает данные о результатах поиска (results), извлекает информацию из объекта `results` и заполняет соответствующие HTML-элементы на странице.  Код также обрабатывает таблицу результатов и позволяет пользователю фокусироваться на определенных элементах.  Он использует функцию `updateDetailsTable`, чтобы добавить детализированную информацию в таблицу.  Ключевым элементом является обработка событий кликов на кнопки в таблицах для взаимодействия с браузером.

Шаги выполнения
-------------------------
1. **Получение результатов:** Код ожидает загрузку страницы и отправляет запрос `browser.runtime.sendMessage({"event":"loadResults"})` в браузерное расширение.
2. **Обработка результата запроса:** Если в результате есть данные (`if (results)`), то значения из объекта `results` устанавливаются в соответствующие HTML-элементы страницы (message, title, href, frameId, и т.д.).
3. **Обработка контекста (results.context):** Если `results.context` содержит данные, то функция заполняет HTML-элементы, относящиеся к контексту (method, expression, specifiedResultType, resultType, resolver, itemDetail).
4. **Обработка основной информации (results.main):** Функция заполняет HTML-элементы, относящиеся к основной части результатов (method, expression, specifiedResultType, resultType, resolver, itemDetails, count).
5. **Обновление таблиц:** Функция `fu.updateDetailsTable` использует данные `itemDetails` для обновления таблиц, отображающих детали результатов.
6. **Обработка событий кликов:** Обработчик событий `addEventListener` для `context-detail` и `main-details` реагирует на клики по кнопкам в таблицах. В зависимости от нажатой кнопки, отправляется сообщение `browser.tabs.sendMessage` в активную вкладку.
7. **Создание ссылок для скачивания:** Создаются ссылки для скачивания информации в текстовом формате (makeInfoText, makeConvertedInfoText).

Пример использования
-------------------------
.. code-block:: javascript

    // Предполагается, что tryxpath и tryxpath.functions уже определены.
    // Доступны результаты поиска.
    var results = {
        "message": "Message text",
        "title": "Title of results",
        "href": "https://example.com",
        "frameId": 123,
        "context": {
            "method": "method1",
            "expression": "expression1",
            "specifiedResultType": "type1",
            "resultType": "type2",
            "resolver": "resolver1",
            "itemDetail": [...] // массив деталей
        },
        "main": {
            "method": "method2",
            "expression": "expression2",
            "specifiedResultType": "type3",
            "resultType": "type4",
            "resolver": "resolver2",
            "itemDetails": [...] // массив деталей
        }
    };

    showAllResults(results);