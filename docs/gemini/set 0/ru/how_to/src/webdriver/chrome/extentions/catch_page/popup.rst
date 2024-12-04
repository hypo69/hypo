Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код обрабатывает клик на кнопку с id "sendUrlButton". При клике он получает URL активной вкладки, отправляет его в фоновый скрипт расширения с действием "sendUrl" и отображает соответствующее сообщение об успехе или неудаче отправки.

Шаги выполнения
-------------------------
1. **Получение ссылки активной вкладки:** Функция `chrome.tabs.query` запрашивает информацию об активной вкладке текущего окна.
2. **Извлечение URL:** Из массива результатов `tabs` извлекается объект активной вкладки (`tabs[0]`). Далее извлекается значение `url` активной вкладки.
3. **Отправка URL в фоновый скрипт:** Функция `chrome.runtime.sendMessage` отправляет сообщение в фоновый скрипт расширения. Сообщение содержит `action: "sendUrl"` и поле `url` с извлечённой ссылкой.
4. **Обработка ответа:** Функция `chrome.runtime.sendMessage` принимает функцию обратного вызова, которая обрабатывает ответ от фонового скрипта.
5. **Проверка статуса:** В функции обратного вызова проверяется значение `response.status`.
6. **Вывод сообщений об успехе/неудачи:** В зависимости от значения `response.status` отображается соответствующее сообщение: "URL sent successfully!" или "Failed to send URL."

Пример использования
-------------------------
.. code-block:: javascript

    // В HTML-разметке popup.html:
    <button id="sendUrlButton">Отправить URL</button>

    // В popup.js (код, приведенный в запросе):
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