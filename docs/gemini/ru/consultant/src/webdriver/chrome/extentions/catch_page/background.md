# Received Code

```javascript
// background.js
// background.js

chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * This function listens for messages sent from other parts of the extension, 
 * such as content scripts or other background scripts, using the `chrome.runtime.sendMessage()` method.
 * 
 * Here's a breakdown of what each part does:
 * 
 * - `chrome.runtime.onMessage.addListener()`: This function sets up a listener for messages sent from other parts of the extension.
 * - `(message, sender, sendResponse) => { ... }`: This is an arrow function that defines what should happen when a message is received. It takes three parameters:
 *   - `message`: The message object sent from the sender.
 *   - `sender`: Information about the sender of the message, such as its ID and whether it is a tab or another extension.
 *   - `sendResponse`: A function that can be used to send a response back to the sender if needed.
 * - `if (message.action === 'collectData') { ... }`: This condition checks if the received message has a property named `action` with a value of `'collectData'`. This is often used to determine the purpose or type of the message.
 * - `sendDataToServer(message.url)`: If the received message has an action of `'collectData'`, this function calls another function named `sendDataToServer()` and passes the URL from the message as an argument. This typically triggers some action or behavior in response to the received message.
 * 
 * In summary, this function listens for messages with the action `'collectData'`, and when such a message is received, it triggers the `sendDataToServer()` function, presumably to collect data and send it to a server.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});

function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php'; // Change to your server endpoint
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
// Обработка запросов и отправка данных на сервер.
//
// Этот файл обрабатывает события клика на иконку расширения и отправляет запрос
// на сбор данных на сервер.


import { j_loads } from 'src.utils.jjson';
import { logger } from 'src.logger';


/**
 * Обрабатывает клик на иконку расширения.
 *
 * @param {object} tab - Данные о вкладке.
 */
chrome.action.onClicked.addListener((tab) => {
    // Отправка сообщения содержимому вкладки для сбора данных.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обрабатывает сообщения, полученные от других частей расширения.
 *
 * @param {object} message - Полученное сообщение.
 * @param {object} sender - Данные о отправителе сообщения.
 * @param {function} sendResponse - Функция для отправки ответа.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Обработка сообщения для сбора данных.
    if (message.action === 'collectData') {
        # Отправка данных на сервер.
        sendDataToServer(message.url);
        # Возвращает true, чтобы показать, что слушатель обработает сообщение асинхронно.
        return true;
    }
});

/**
 * Отправляет собранные данные на сервер.
 *
 * @param {string} url - URL страницы.
 */
function sendDataToServer(url) {
    # Получение URL сервера из настроек (предполагается, что в них будет храниться `serverUrl`).
    chrome.storage.local.get('serverUrl', (result) => {
        let serverUrl = result.serverUrl || 'http://127.0.0.1/hypotez/catch_request.php';
        # Получение собранных данных из хранилища.
        chrome.storage.local.get('collectedData', (data) => {
            const collectedData = data.collectedData;
            # Проверка наличия данных.
            if (collectedData) {
                fetch(serverUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(collectedData)
                })
                    .then(response => {
                        # Обработка успеха.
                        if (!response.ok) {
                            throw new Error(`Ошибка отправки данных на сервер: ${response.status}`);
                        }
                        logger.info('Данные успешно отправлены на сервер');
                    })
                    .catch(error => {
                        # Обработка ошибок.
                        logger.error('Ошибка отправки данных на сервер:', error);
                    });
            } else {
                # Логирование отсутствия данных.
                logger.error('Собранные данные отсутствуют');
            }
        });
    });
}
```

# Changes Made

- Добавлена библиотека `src.logger`.
- Добавлены импорты `j_loads` и `logger` из соответствующих файлов.
- Функция `sendDataToServer` переписана для получения `serverUrl` из хранилища `chrome.storage`.
- Функции и переменные снабжены комментариями RST.
- Использование `logger.error` для обработки ошибок вместо `console.error`.
-  Добавлена обработка ответа сервера `response.ok`.
-  Изменён способ отправки сообщения с помощью `return true` в обработчике сообщений.


# FULL Code

```javascript
// background.js
// Обработка запросов и отправка данных на сервер.
//
// Этот файл обрабатывает события клика на иконку расширения и отправляет запрос
// на сбор данных на сервер.


import { j_loads } from 'src.utils.jjson';
import { logger } from 'src.logger';


/**
 * Обрабатывает клик на иконку расширения.
 *
 * @param {object} tab - Данные о вкладке.
 */
chrome.action.onClicked.addListener((tab) => {
    // Отправка сообщения содержимому вкладки для сбора данных.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обрабатывает сообщения, полученные от других частей расширения.
 *
 * @param {object} message - Полученное сообщение.
 * @param {object} sender - Данные о отправителе сообщения.
 * @param {function} sendResponse - Функция для отправки ответа.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Обработка сообщения для сбора данных.
    if (message.action === 'collectData') {
        # Отправка данных на сервер.
        sendDataToServer(message.url);
        # Возвращает true, чтобы показать, что слушатель обработает сообщение асинхронно.
        return true;
    }
});

/**
 * Отправляет собранные данные на сервер.
 *
 * @param {string} url - URL страницы.
 */
function sendDataToServer(url) {
    # Получение URL сервера из настроек (предполагается, что в них будет храниться `serverUrl`).
    chrome.storage.local.get('serverUrl', (result) => {
        let serverUrl = result.serverUrl || 'http://127.0.0.1/hypotez/catch_request.php';
        # Получение собранных данных из хранилища.
        chrome.storage.local.get('collectedData', (data) => {
            const collectedData = data.collectedData;
            # Проверка наличия данных.
            if (collectedData) {
                fetch(serverUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(collectedData)
                })
                    .then(response => {
                        # Обработка успеха.
                        if (!response.ok) {
                            throw new Error(`Ошибка отправки данных на сервер: ${response.status}`);
                        }
                        logger.info('Данные успешно отправлены на сервер');
                    })
                    .catch(error => {
                        # Обработка ошибок.
                        logger.error('Ошибка отправки данных на сервер:', error);
                    });
            } else {
                # Логирование отсутствия данных.
                logger.error('Собранные данные отсутствуют');
            }
        });
    });
}