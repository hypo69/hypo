# Received Code

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
// Обработка запросов на сбор данных и отправка на сервер.

import { logger } from 'src.logger'; // Импорт функции логирования
import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON

/**
 * Модуль для обработки сообщений о сборе данных и отправке на сервер.
 */

chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обрабатывает сообщения от других частей расширения.
 *
 * :param message: Сообщение от отправителя.
 * :param sender: Информация об отправителе.
 *
 * :raises Exception: При возникновении ошибок.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Проверка типа сообщения.
    if (message && message.action === 'collectData') {
        # Отправка данных на сервер.
        sendDataToServer(message.url);
        return true; # Необходимо для асинхронной обработки
    }
    return false; # Обработка асинхронных запросов
});


/**
 * Отправляет собранные данные на сервер.
 *
 * :param url: URL страницы, для которой собираются данные.
 *
 * :raises Exception: При возникновении ошибок.
 */
async function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера (изменить на ваш)

    try {
        # Получение собранных данных из хранилища.
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        # Проверка наличия данных.
        if (!collectedData) {
            logger.error('No collected data found');
            return;
        }

        # Отправка данных с использованием fetch.
        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        # Обработка ответа сервера.
        if (!response.ok) {
            const errorText = await response.text(); // Считываем текст ошибки
            logger.error(`Ошибка отправки данных на сервер: ${errorText}`);
            throw new Error(`Ошибка отправки данных на сервер: ${errorText}`);
        }
        logger.info('Данные успешно отправлены на сервер');
    } catch (error) {
        logger.error('Ошибка отправки данных на сервер:', error);
    }
}
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger` и `j_loads` из `src.utils.jjson`.
*   Добавлены комментарии в формате RST для функций и блоков кода.
*   Изменен стиль обработки ошибок: теперь используется `try...catch` с логированием ошибок через `logger.error`.
*   Изменен формат логирования.
*   Добавлена проверка на существование данных в хранилище.
*   Добавлено асинхронное ожидание для `fetch`.
*   Добавлено чтение ответа сервера для обработки ошибок.
*   Заменены `console.log` и `console.error` на `logger.info` и `logger.error`.
*   Добавлен `return true` в обработчике сообщений для асинхронных вызовов.


# FULL Code

```javascript
// background.js
// Обработка запросов на сбор данных и отправка на сервер.

import { logger } from 'src.logger'; // Импорт функции логирования
import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON

/**
 * Модуль для обработки сообщений о сборе данных и отправке на сервер.
 */

chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обрабатывает сообщения от других частей расширения.
 *
 * :param message: Сообщение от отправителя.
 * :param sender: Информация об отправителе.
 *
 * :raises Exception: При возникновении ошибок.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Проверка типа сообщения.
    if (message && message.action === 'collectData') {
        # Отправка данных на сервер.
        sendDataToServer(message.url);
        return true; # Необходимо для асинхронной обработки
    }
    return false; # Обработка асинхронных запросов
});


/**
 * Отправляет собранные данные на сервер.
 *
 * :param url: URL страницы, для которой собираются данные.
 *
 * :raises Exception: При возникновении ошибок.
 */
async function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера (изменить на ваш)

    try {
        # Получение собранных данных из хранилища.
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        # Проверка наличия данных.
        if (!collectedData) {
            logger.error('No collected data found');
            return;
        }

        # Отправка данных с использованием fetch.
        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        # Обработка ответа сервера.
        if (!response.ok) {
            const errorText = await response.text(); // Считываем текст ошибки
            logger.error(`Ошибка отправки данных на сервер: ${errorText}`);
            throw new Error(`Ошибка отправки данных на сервер: ${errorText}`);
        }
        logger.info('Данные успешно отправлены на сервер');
    } catch (error) {
        logger.error('Ошибка отправки данных на сервер:', error);
    }
}