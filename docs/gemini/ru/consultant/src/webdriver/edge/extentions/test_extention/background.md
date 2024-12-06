# Received Code

```javascript
// background.js
// background.js

chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * 
 * Эта функция прослушивает сообщения, отправленные из других частей расширения, таких как скрипты контента или другие фоновые скрипты, с помощью метода `chrome.runtime.sendMessage()`.
 *
 * Разбиение по частям:
 *
 * - `chrome.runtime.onMessage.addListener()`: Эта функция устанавливает прослушиватель сообщений, отправленных из других частей расширения.
 *
 * - `(message, sender, sendResponse) => { ... }`: Это стрелочная функция, которая определяет, что должно произойти при получении сообщения. Она принимает три параметра:
 *   - `message`: Объект сообщения, отправленный отправителем.
 *   - `sender`: Информация об отправителе сообщения, такая как его идентификатор и является ли это вкладка или другое расширение.
 *   - `sendResponse`: Функция, которая может использоваться для отправки ответа отправителю, если это необходимо.
 *
 * - `if (message.action === 'collectData') { ... }`: Это условие проверяет, есть ли у полученного сообщения свойство `action` со значением `'collectData'`. Это часто используется для определения цели или типа сообщения.
 *
 * - `sendDataToServer(message.url)`: Если полученное сообщение имеет действие `'collectData'`, эта функция вызывает другую функцию `sendDataToServer()`, передавая URL из сообщения в качестве аргумента. Это, как правило, запускает какое-то действие или поведение в ответ на полученное сообщение.
 *
 * Подводя итог, эта функция прослушивает сообщения с действием `'collectData'`, и при получении такого сообщения запускает функцию `sendDataToServer()`, предположительно для сбора данных и отправки их на сервер.
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
                        throw new Error('Не удалось отправить данные на сервер');
                    }
                    console.log('Данные отправлены на сервер успешно');
                })
                .catch(error => {
                    console.error('Ошибка при отправке данных на сервер:', error);
                });
        } else {
            console.error('Собранные данные не найдены');
        }
    });
}
```

# Improved Code

```javascript
// background.js
// Модуль для отправки данных на сервер через API.
// Обрабатывает сообщения о сборе данных и отправляет их на сервер.

import { logger } from 'src.logger';
import { j_loads } from 'src.utils.jjson'; // Импорт функции для парсинга JSON

/**
 * Функция обрабатывает клики по иконке расширения.
 * Отправляет сообщение в активную вкладку для сбора данных.
 *
 * @param {object} tab - Объект вкладки.
 */
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * Функция-обработчик сообщений.
 *
 * @param {object} message - Принятое сообщение.
 * @param {object} sender - Отправитель сообщения.
 * @param {function} sendResponse - Функция для отправки ответа.
 * @returns {boolean} - Возвращает true, чтобы разрешить асинхронную операцию.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        # Код отправляет запрос на сервер для обработки данных.
        sendDataToServer(message.url);
    }
    return true; // Разрешаем асинхронную операцию
});

/**
 * Функция отправляет собранные данные на сервер.
 *
 * @param {string} url - URL страницы, с которой собирались данные.
 */
async function sendDataToServer(url) {
    let serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес API сервера.  # Измените на ваш адрес сервера.
    try {
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        if (!collectedData) {
            logger.error('Собранные данные не найдены');
            return;
        }

        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        if (!response.ok) {
            const errorText = await response.text(); // Получаем текст ошибки.
            const errorMessage = `Ошибка при отправке данных на сервер: ${errorText}`;
            logger.error(errorMessage);
            throw new Error(errorMessage);
        }

        logger.info('Данные отправлены на сервер успешно');
    } catch (error) {
        logger.error('Ошибка при отправке данных на сервер:', error);
    }
}
```

# Changes Made

* Импортирован `logger` из `src.logger` и `j_loads` из `src.utils.jjson`.
* Добавлены комментарии RST к функциям `sendDataToServer` и `chrome.runtime.onMessage.addListener`.
* Изменены консольные логи на использование `logger`.
* Добавлен `return true` в `chrome.runtime.onMessage.addListener` для асинхронности.
* Обработка ошибок с помощью `try...catch` и `logger.error`.
* Заменено `console.error` на `logger.error`.
* Добавлен `async/await` для `fetch`.
* Изменён `console.log` на `logger.info` для успешного отправления данных.
* Переписаны комментарии в стиле RST.
* Добавлено описание переменной `serverUrl`
* Обработка ошибок `response.ok` теперь использует `response.text()` для получения текста ошибки.
* Изменены названия переменных, чтобы соответствовать стилю кода (например, `collectedData` вместо `result`).

# FULL Code

```javascript
// background.js
// Модуль для отправки данных на сервер через API.
// Обрабатывает сообщения о сборе данных и отправляет их на сервер.

import { logger } from 'src.logger';
import { j_loads } from 'src.utils.jjson'; // Импорт функции для парсинга JSON

/**
 * Функция обрабатывает клики по иконке расширения.
 * Отправляет сообщение в активную вкладку для сбора данных.
 *
 * @param {object} tab - Объект вкладки.
 */
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

/**
 * Функция-обработчик сообщений.
 *
 * @param {object} message - Принятое сообщение.
 * @param {object} sender - Отправитель сообщения.
 * @param {function} sendResponse - Функция для отправки ответа.
 * @returns {boolean} - Возвращает true, чтобы разрешить асинхронную операцию.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        # Код отправляет запрос на сервер для обработки данных.
        sendDataToServer(message.url);
    }
    return true; // Разрешаем асинхронную операцию
});

/**
 * Функция отправляет собранные данные на сервер.
 *
 * @param {string} url - URL страницы, с которой собирались данные.
 */
async function sendDataToServer(url) {
    let serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Адрес API сервера.  # Измените на ваш адрес сервера.
    try {
        const storedData = await chrome.storage.local.get('collectedData');
        const collectedData = storedData.collectedData;

        if (!collectedData) {
            logger.error('Собранные данные не найдены');
            return;
        }

        const response = await fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(collectedData)
        });

        if (!response.ok) {
            const errorText = await response.text(); // Получаем текст ошибки.
            const errorMessage = `Ошибка при отправке данных на сервер: ${errorText}`;
            logger.error(errorMessage);
            throw new Error(errorMessage);
        }

        logger.info('Данные отправлены на сервер успешно');
    } catch (error) {
        logger.error('Ошибка при отправке данных на сервер:', error);
    }
}