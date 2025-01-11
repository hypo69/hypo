# Анализ кода модуля background.js

**Качество кода**

6
-  Плюсы
    -   Код логически структурирован, разделен на функции и обработчики событий.
    -   Используется `chrome.storage.local.get` для получения сохраненных данных.
    -   Присутствует обработка ошибок при отправке данных на сервер.
    -   Код содержит комментарии, объясняющие назначение основных частей.

-  Минусы
    -   Отсутствует импорт `logger`.
    -   Не стандартизировано использование одинарных/двойных кавычек.
    -   Не хватает документации в формате RST для функций и модуля.
    -   Обработка ошибок `fetch` выполняется через `console.log` и `console.error`, что не подходит для продакшн среды.
    -   Серверный URL жестко задан в коде.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Заменить `console.log` и `console.error` на `logger.info` и `logger.error` соответственно.
3.  Добавить try-except блоки для обработки ошибок в `sendDataToServer`.
4.  Добавить документацию в формате RST для функций и модуля.
5.  Перенести URL сервера в переменные окружения или в конфигурационный файл.
6.  Стандартизировать использование кавычек. Использовать только одинарные кавычки для строк в коде.
7.  Добавить проверку на наличие данных в `collectedData` перед отправкой.
8.  Добавить обработку ошибок при получении данных из `chrome.storage`.

**Оптимизированный код**

```python
"""
Модуль для обработки фоновых событий расширения Chrome.
=========================================================================================

Этот модуль прослушивает события нажатия на иконку расширения и сообщения,
отправляемые контентными скриптами, собирает данные и отправляет их на сервер.

Пример использования
--------------------

Пример использования обработчика нажатия на иконку расширения:

.. code-block:: javascript

    // В content script
    chrome.runtime.sendMessage({ action: 'collectData', url: window.location.href });

Пример использования обработчика сообщений из других частей расширения:

.. code-block:: javascript

    // В content script
    chrome.runtime.sendMessage({ action: 'collectData', url: window.location.href });
"""
from src.logger.logger import logger # импортируем logger

# Слушаем событие нажатия на иконку расширения.
chrome.browserAction.onClicked.addListener(tab => {
    # Отправляем сообщение контентному скрипту с запросом на сбор данных.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

# Слушаем сообщения от других частей расширения.
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Если сообщение содержит действие 'collectData', вызываем функцию отправки данных на сервер.
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});

async function sendDataToServer(url) {
    """
    Отправляет собранные данные на сервер.

    Args:
        url (str): URL страницы, с которой были собраны данные.

    Raises:
        Exception: Выводит ошибку в лог, если не удалось отправить данные на сервер.

    """
    # URL сервера, на который будут отправляться данные.
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; # Change to your server endpoint
    try:
        # Получаем сохраненные данные из локального хранилища.
        chrome.storage.local.get('collectedData', (result) => {
            const collectedData = result.collectedData;
            # Проверяем наличие данных перед отправкой.
            if (collectedData) {
                 # Отправляем данные на сервер с использованием метода POST.
                fetch(serverUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(collectedData)
                })
                    .then(response => {
                        if (!response.ok) {
                            # Выводит ошибку в лог, если запрос не успешен.
                            logger.error('Failed to send data to server')
                            throw new Error('Failed to send data to server');
                        }
                        # Выводит сообщение об успешной отправке данных в лог.
                        logger.info('Data sent to server successfully');
                    })
                    .catch(error => {
                        # Выводит ошибку в лог при возникновении исключения во время отправки данных.
                        logger.error('Error sending data to server:', error);
                    });
            } else {
                # Выводит ошибку в лог, если нет собранных данных.
                logger.error('No collected data found');
            }
        });
    except Exception as ex:
        # Выводит ошибку в лог при возникновении исключения во время отправки данных.
        logger.error(f'Ошибка при отправке данных на сервер: {ex}')

}
```