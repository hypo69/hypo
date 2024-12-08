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
// Обработка событий клика по иконке расширения.
// Отправляет сообщение в активную вкладку с запросом данных.
chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обработчик сообщений, отправленных другими частями расширения.
 *
 * @param {object} message - Сообщение, полученное от отправителя.
 * @param {object} sender - Информация об отправителе сообщения.
 * @param {function} sendResponse - Функция для отправки ответа отправителю.
 *
 * @return {boolean} - Возвращает true, если обработка выполняется асинхронно.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Проверка действия сообщения.
    if (message.action === 'collectData') {
        // Отправка данных на сервер.
        sendDataToServer(message.url);
        return true; // Возвращает true, чтобы асинхронная функция могла ответить на запрос.
    }
    return false;
});

/**
 * Отправка данных на сервер.
 *
 * @param {string} url - URL страницы.
 */
function sendDataToServer(url) {
    // Адрес сервера. Заменить на фактический.
    const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php';
    // Получение сохраненных данных из хранилища.
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            // Проверка валидности данных.
            if (typeof collectedData !== 'object' || collectedData === null) {
                logger.error("Получены невалидные данные для отправки на сервер.");
                return;
            }
            // Отправка данных с помощью fetch.
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
            .then(response => {
                // Проверка успешной отправки.
                if (!response.ok) {
                    const errorMessage = `Ошибка отправки данных на сервер. Код ответа: ${response.status}`;
                    logger.error(errorMessage);
                    throw new Error(errorMessage);
                }
                logger.info('Данные успешно отправлены на сервер.');
            })
            .catch(error => {
                logger.error('Ошибка отправки данных на сервер:', error);
            });
        } else {
            logger.error('Не найдены сохраненные данные для отправки.');
        }
    });
}

// Импорт модуля для логирования.
from src.logger import logger;
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger`.
*   Изменен формат комментариев на RST.
*   Добавлена функция `sendDataToServer` с полным RST описанием и обработкой ошибок.
*   Добавлена проверка типа `collectedData` для предотвращения ошибок.
*   Изменён код обработки ответа `fetch`, добавлена обработка статуса `response.ok`.
*   Изменён код логирования ошибок с использованием `logger.error` и `logger.info`.
*   Добавлена асинхронность в обработчике сообщений.
*   Добавлена обработка пустых данных.
*   Внесена дополнительная ясность в комментарии.


# FULL Code

```javascript
// background.js
// Обработка событий клика по иконке расширения.
// Отправляет сообщение в активную вкладку с запросом данных.
chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


/**
 * Обработчик сообщений, отправленных другими частями расширения.
 *
 * @param {object} message - Сообщение, полученное от отправителя.
 * @param {object} sender - Информация об отправителе сообщения.
 * @param {function} sendResponse - Функция для отправки ответа отправителю.
 *
 * @return {boolean} - Возвращает true, если обработка выполняется асинхронно.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Проверка действия сообщения.
    if (message.action === 'collectData') {
        // Отправка данных на сервер.
        sendDataToServer(message.url);
        return true; // Возвращает true, чтобы асинхронная функция могла ответить на запрос.
    }
    return false;
});

/**
 * Отправка данных на сервер.
 *
 * @param {string} url - URL страницы.
 */
function sendDataToServer(url) {
    // Адрес сервера. Заменить на фактический.
    const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php';
    // Получение сохраненных данных из хранилища.
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            // Проверка валидности данных.
            if (typeof collectedData !== 'object' || collectedData === null) {
                logger.error("Получены невалидные данные для отправки на сервер.");
                return;
            }
            // Отправка данных с помощью fetch.
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
            .then(response => {
                // Проверка успешной отправки.
                if (!response.ok) {
                    const errorMessage = `Ошибка отправки данных на сервер. Код ответа: ${response.status}`;
                    logger.error(errorMessage);
                    throw new Error(errorMessage);
                }
                logger.info('Данные успешно отправлены на сервер.');
            })
            .catch(error => {
                logger.error('Ошибка отправки данных на сервер:', error);
            });
        } else {
            logger.error('Не найдены сохраненные данные для отправки.');
        }
    });
}

// Импорт модуля для логирования.
from src.logger import logger;