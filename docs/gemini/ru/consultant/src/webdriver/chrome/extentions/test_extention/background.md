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

# Improved Code

```javascript
// background.js
import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON
import { logger } from 'src.logger'; // Импорт функции для логирования

/**
 * Модуль для обработки сообщений от контентных скриптов и отправки данных на сервер.
 * 
 * Этот модуль слушает события `chrome.browserAction.onClicked` и
 * `chrome.runtime.onMessage`. При получении сообщения с действием
 * `'collectData'` отправляет URL страницы на сервер.
 */

// Функция обработки клика по иконке расширения
chrome.browserAction.onClicked.addListener(async (tab) => {
    try {
        // Отправка сообщения контентному скрипту для сбора данных
        await chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
    } catch (error) {
        logger.error('Ошибка отправки сообщения контентному скрипту:', error);
    }
});


// Функция-обработчик сообщений
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message && message.action === 'collectData') {
        // Обработка URL и отправка на сервер
        sendDataToServer(message.url);
        return true; // Необходимо вернуть true, чтобы сохранить коммуникацию
    }
    return false;
});



/**
 * Отправляет URL страницы на сервер.
 * 
 * Функция извлекает сохраненные данные из хранилища и отправляет их на сервер.
 * 
 * :param url: URL страницы.
 */
async function sendDataToServer(url) {
    try {
        const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера
        // Чтение данных из хранилища chrome.storage.local
        const storageData = await chrome.storage.local.get('collectedData');
        const collectedData = storageData.collectedData;

        // Проверка наличия данных
        if (!collectedData) {
            logger.error('Отсутствуют данные для отправки на сервер.');
            return;
        }

        // Отправка данных на сервер с помощью fetch
        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        if (!response.ok) {
            const errorMessage = `Ошибка отправки данных на сервер: ${response.status} ${response.statusText}`;
            logger.error(errorMessage);
            throw new Error(errorMessage); // Перебрасываем ошибку для обработки
        }

        logger.info('Данные успешно отправлены на сервер.');

    } catch (error) {
        logger.error('Ошибка при отправке данных на сервер:', error);
    }
}
```

# Changes Made

* Добавлена строка импорта `import { j_loads } from 'src.utils.jjson';`.
* Добавлена строка импорта `import { logger } from 'src.logger';`.
* Функция `sendDataToServer` переписана для использования `async/await`.
* Добавлена обработка ошибок с помощью `try...catch` и `logger.error`.
* Изменен способ обработки ответа от сервера (`response.ok`).
* Удалены ненужные `console.log` и `console.error`.
* Добавлены комментарии в RST формате к функциям и блокам кода.
* Улучшен стиль и структура кода.
* Добавлено ключевое слово `return true;` в `chrome.runtime.onMessage.addListener`, чтобы функция не завершалась сразу.


# FULL Code

```javascript
// background.js
import { j_loads } from 'src.utils.jjson'; // Импорт функции для обработки JSON
import { logger } from 'src.logger'; // Импорт функции для логирования

/**
 * Модуль для обработки сообщений от контентных скриптов и отправки данных на сервер.
 * 
 * Этот модуль слушает события `chrome.browserAction.onClicked` и
 * `chrome.runtime.onMessage`. При получении сообщения с действием
 * `'collectData'` отправляет URL страницы на сервер.
 */

// Функция обработки клика по иконке расширения
chrome.browserAction.onClicked.addListener(async (tab) => {
    try {
        // Отправка сообщения контентному скрипту для сбора данных
        await chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
    } catch (error) {
        logger.error('Ошибка отправки сообщения контентному скрипту:', error);
    }
});


// Функция-обработчик сообщений
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message && message.action === 'collectData') {
        // Обработка URL и отправка на сервер
        sendDataToServer(message.url);
        return true; // Необходимо вернуть true, чтобы сохранить коммуникацию
    }
    return false;
});



/**
 * Отправляет URL страницы на сервер.
 * 
 * Функция извлекает сохраненные данные из хранилища и отправляет их на сервер.
 * 
 * :param url: URL страницы.
 */
async function sendDataToServer(url) {
    try {
        const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес сервера
        // Чтение данных из хранилища chrome.storage.local
        const storageData = await chrome.storage.local.get('collectedData');
        const collectedData = storageData.collectedData;

        // Проверка наличия данных
        if (!collectedData) {
            logger.error('Отсутствуют данные для отправки на сервер.');
            return;
        }

        // Отправка данных на сервер с помощью fetch
        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        if (!response.ok) {
            const errorMessage = `Ошибка отправки данных на сервер: ${response.status} ${response.statusText}`;
            logger.error(errorMessage);
            throw new Error(errorMessage); // Перебрасываем ошибку для обработки
        }

        logger.info('Данные успешно отправлены на сервер.');

    } catch (error) {
        logger.error('Ошибка при отправке данных на сервер:', error);
    }
}
```