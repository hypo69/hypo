# Received Code

```javascript
// background.js

chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * 
 * This function listens for messages sent from other parts of the extension, 
 * such as content scripts or other background scripts, using the `chrome.runtime.sendMessage()` method.

Here's a breakdown of what each part does:

- `chrome.runtime.onMessage.addListener()`: 
This function sets up a listener for messages sent from other parts of the extension.

- `(message, sender, sendResponse) => { ... }`: This is an arrow function that defines what should happen when a message is received. It takes three parameters:
  - `message`: The message object sent from the sender.
  - `sender`: Information about the sender of the message, such as its ID and whether it is a tab or another extension.
  - `sendResponse`: A function that can be used to send a response back to the sender if needed.

- `if (message.action === 'collectData') { ... }`: This condition checks if the received message has a property named `action` with a value of `'collectData'`. This is often used to determine the purpose or type of the message.

- `sendDataToServer(message.url)`: If the received message has an action of `'collectData'`, this function calls another function named `sendDataToServer()` and passes the URL from the message as an argument. This typically triggers some action or behavior in response to the received message.

In summary, this function listens for messages with the action `'collectData'`, and when such a message is received, it triggers the `sendDataToServer()` function, presumably to collect data and send it to a server.
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

# Improved Code

```javascript
// background.js
// Модуль для отправки данных на сервер

import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON
import { logger } from 'src.logger'; // Импорт логгера


/**
 * Обрабатывает клики по значку расширения.
 * Отправляет сообщение в активную вкладку с запросом данных.
 * 
 * :param tab: Объект вкладки.
 */
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Функция-обработчик сообщений от других частей расширения.
 * 
 * :param message: Полученное сообщение.
 * :param sender: Отправитель сообщения.
 * :param sendResponse: Функция для отправки ответа.
 * 
 * Обрабатывает сообщение с действием 'collectData'.
 * Вызывает функцию `sendDataToServer` для отправки данных на сервер.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
    return true; // Возвращает true, чтобы разрешить асинхронную обработку
});


/**
 * Отправляет собранные данные на сервер.
 * 
 * :param url: URL страницы, для которой собираются данные.
 * 
 * Читает данные из хранилища, сериализует их в JSON и отправляет POST-запрос на сервер.
 * Обрабатывает возможные ошибки.
 */
async function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера

    try {
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData; // Получение данных из хранилища

        if (!collectedData) {
            logger.error('No collected data found.');
            return;
        }

        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData) // Сформировать JSON
        });

        if (!response.ok) {
            const message = await response.text(); // Получить сообщение об ошибке
            logger.error(`Failed to send data to server: ${message}`);
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        logger.info('Data sent to server successfully');
    } catch (error) {
        logger.error('Error sending data to server:', error);
    }
}
```

# Changes Made

- Импортированы необходимые модули: `j_loads` из `src.utils.jjson` и `logger` из `src.logger`.
- Добавлены комментарии RST к функциям `sendDataToServer` и обработчику сообщений.
- Вместо `console.error` и `console.log` используются `logger.error` и `logger.info`.
- Добавлен `try...catch` блок для обработки ошибок `fetch`.
- `return true;` добавлено в `chrome.runtime.onMessage`, чтобы разрешить асинхронную обработку.
- Ошибка `JSON.stringify` отлову не поддаётся, поэтому `collectedData` извлекается без обработки как есть. 
- Выполнена проверка наличия `collectedData` перед отправкой.
- Попытка получить сообщение об ошибке и добавить в логирование.


# FULL Code

```javascript
// background.js
// Модуль для отправки данных на сервер

import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON
import { logger } from 'src.logger'; // Импорт логгера


/**
 * Обрабатывает клики по значку расширения.
 * Отправляет сообщение в активную вкладку с запросом данных.
 * 
 * :param tab: Объект вкладки.
 */
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Функция-обработчик сообщений от других частей расширения.
 * 
 * :param message: Полученное сообщение.
 * :param sender: Отправитель сообщения.
 * :param sendResponse: Функция для отправки ответа.
 * 
 * Обрабатывает сообщение с действием 'collectData'.
 * Вызывает функцию `sendDataToServer` для отправки данных на сервер.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
    return true; // Возвращает true, чтобы разрешить асинхронную обработку
});


/**
 * Отправляет собранные данные на сервер.
 * 
 * :param url: URL страницы, для которой собираются данные.
 * 
 * Читает данные из хранилища, сериализует их в JSON и отправляет POST-запрос на сервер.
 * Обрабатывает возможные ошибки.
 */
async function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера

    try {
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData; // Получение данных из хранилища

        if (!collectedData) {
            logger.error('No collected data found.');
            return;
        }

        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData) // Сформировать JSON
        });

        if (!response.ok) {
            const message = await response.text(); // Получить сообщение об ошибке
            logger.error(`Failed to send data to server: ${message}`);
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        logger.info('Data sent to server successfully');
    } catch (error) {
        logger.error('Error sending data to server:', error);
    }
}