Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот фрагмент JavaScript-кода обрабатывает нажатие кнопки с id "sendUrlButton". При нажатии он получает URL активной вкладки в текущем окне Chrome, отправляет его в контекст расширения и обрабатывает ответ.

Шаги выполнения
-------------------------
1. **Обработка события клика:** Код добавляет обработчик события "click" к элементу с id "sendUrlButton". При нажатии кнопки выполняется функция анонимной функции.
2. **Вывод сообщения:** Выводит всплывающее сообщение "Hello, world!".
3. **Получение URL активной вкладки:**  Используя `chrome.tabs.query`, запрашивает информацию об активной вкладке в текущем окне.
4. **Извлечение URL:** Из массива результатов `tabs` извлекает URL активной вкладки и сохраняет его в переменной `activeTabUrl`.
5. **Отправка URL в расширение:** Используя `chrome.runtime.sendMessage`, отправляет сообщение в контекст расширения Chrome. Сообщение содержит информацию о типе действия ("sendUrl") и URL активной вкладки.
6. **Обработка ответа:** Функция обратного вызова `(response) => { ... }` получает ответ от расширения.
7. **Проверка статуса ответа:** Проверяет значение `response.status`.
8. **Успешная отправка:** Если `response.status` равно "success", выводит всплывающее сообщение "URL sent successfully!".
9. **Ошибка отправки:** В противном случае, выводит сообщение "Failed to send URL.".


Пример использования
-------------------------
.. code-block:: javascript

    <!DOCTYPE html>
    <html>
    <head>
        <title>Send URL</title>
    </head>
    <body>
        <button id="sendUrlButton">Send URL</button>
        <script>
            document.getElementById("sendUrlButton").addEventListener("click", () => {
                alert("Hello, world!");
                chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                    let activeTab = tabs[0];
                    let activeTabUrl = activeTab.url;
                    
                    chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
                        if (response.status === "success") {
                            alert("URL sent successfully!");
                        } else {
                            alert("Failed to send URL.");
                        }
                    });
                });
            });
        </script>
    </body>
    </html>