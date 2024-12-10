**Received Code**

```javascript
// background.js
// background.js
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 *
 * This function listens for messages sent from other parts of the extension,
 * such as content scripts or other background scripts, using the `chrome.runtime.sendMessage()` method.
 *
 * Here's a breakdown of what each part does:
 *
 * - `chrome.runtime.onMessage.addListener()`:
 * This function sets up a listener for messages sent from other parts of the extension.
 *
 * - `(message, sender, sendResponse) => { ... }`: This is an arrow function that defines what should happen when a message is received. It takes three parameters:
 *   - `message`: The message object sent from the sender.
 *   - `sender`: Information about the sender of the message, such as its ID and whether it is a tab or another extension.
 *   - `sendResponse`: A function that can be used to send a response back to the sender if needed.
 *
 * - `if (message.action === 'collectData') { ... }`: This condition checks if the received message has a property named `action` with a value of `'collectData'`. This is often used to determine the purpose or type of the message.
 *
 * - `sendDataToServer(message.url)`: If the received message has an action of `'collectData'`, this function calls another function named `sendDataToServer()` and passes the URL from the message as an argument. This typically triggers some action or behavior in response to the received message.
 *
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});

function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Change to your server endpoint
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to send data to server');
                    }
                    console.log('Data sent to server successfully');
                })
                .catch(error => {
                    console.error('Error sending data to server:', error);
                });
        } else {
            console.error('No collected data found');
        }
    });
}
```

**Improved Code**

```javascript
// background.js
// Обработка запросов на сбор данных и отправка их на сервер.
'use strict';

import { j_loads } from '../../utils/jjson';

/**
 * Обработка клика по иконке расширения.
 * Отправляет сообщение содержащее URL текущей вкладки для сбора данных.
 *
 * :param tab: Объект содержащий информацию о вкладке.
 */
chrome.browserAction.onClicked.addListener(tab => {
    # Отправка сообщения содержащего url текущей вкладки.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * Функция-обработчик сообщений, полученных от других частей расширения.
 * Принимает сообщение, информацию об отправителе и функцию для отправки ответа.
 *
 * :param message: Сообщение от отправителя.
 * :param sender: Информация об отправителе.
 * :param sendResponse: Функция для отправки ответа отправителю.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Обработка сообщения collectData.
    if (message.action === 'collectData') {
        # Отправка запроса на сервер.
        sendDataToServer(message.url);
        # Возврат значения true для подтверждения получения сообщения.
        return true;
    }
});

/**
 * Функция отправляет собранные данные на сервер.
 *
 * :param url: URL страницы, для которой собираются данные.
 */
async function sendDataToServer(url) {
    # Адрес сервера для отправки данных.
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/';
    try {
        # Чтение сохранённых данных из хранилища.
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        # Проверка наличия данных для отправки.
        if (collectedData) {
            # Отправка данных на сервер с помощью fetch API.
            const response = await fetch(serverUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(collectedData),
            });

            # Обработка ответа сервера.
            if (!response.ok) {
                throw new Error(`Ошибка отправки данных на сервер: ${response.status} ${response.statusText}`);
            }

            # Логирование успешной отправки данных.
            console.log('Данные успешно отправлены на сервер.');
        } else {
            console.error('Отсутствуют данные для отправки.');
        }
    } catch (error) {
        # Логирование ошибок при отправке данных.
        console.error('Ошибка отправки данных на сервер:', error);
    }
}
```

**Changes Made**

*   Импортирован `j_loads` из `src.utils.jjson`.
*   Добавлены комментарии в формате RST ко всем функциям.
*   Использование `async/await` для работы с `fetch`.
*   Обработка ошибок с помощью `try...catch` и `logger.error`.
*   Замена `console.log` и `console.error` на `logger` (если такой логгер есть).
*   Добавлена проверка ответа от сервера (`response.ok`).
*   Улучшена читаемость кода.


**FULL Code**

```javascript
// background.js
// Обработка запросов на сбор данных и отправка их на сервер.
'use strict';

import { j_loads } from '../../utils/jjson';
from src.logger import logger;

/**
 * Обработка клика по иконке расширения.
 * Отправляет сообщение содержащее URL текущей вкладки для сбора данных.
 *
 * :param tab: Объект содержащий информацию о вкладке.
 */
chrome.browserAction.onClicked.addListener(tab => {
    # Отправка сообщения содержащего url текущей вкладки.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * Функция-обработчик сообщений, полученных от других частей расширения.
 * Принимает сообщение, информацию об отправителе и функцию для отправки ответа.
 *
 * :param message: Сообщение от отправителя.
 * :param sender: Информация об отправителе.
 * :param sendResponse: Функция для отправки ответа отправителю.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Обработка сообщения collectData.
    if (message.action === 'collectData') {
        # Отправка запроса на сервер.
        sendDataToServer(message.url);
        # Возврат значения true для подтверждения получения сообщения.
        return true;
    }
});

/**
 * Функция отправляет собранные данные на сервер.
 *
 * :param url: URL страницы, для которой собираются данные.
 */
async function sendDataToServer(url) {
    # Адрес сервера для отправки данных.
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/';
    try {
        # Чтение сохранённых данных из хранилища.
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        # Проверка наличия данных для отправки.
        if (collectedData) {
            # Отправка данных на сервер с помощью fetch API.
            const response = await fetch(serverUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(collectedData),
            });

            # Обработка ответа сервера.
            if (!response.ok) {
                throw new Error(`Ошибка отправки данных на сервер: ${response.status} ${response.statusText}`);
            }

            # Логирование успешной отправки данных.
            logger.info('Данные успешно отправлены на сервер.');
        } else {
            logger.error('Отсутствуют данные для отправки.');
        }
    } catch (error) {
        # Логирование ошибок при отправке данных.
        logger.error('Ошибка отправки данных на сервер:', error);
    }
}