# Анализ кода модуля background.js

**Качество кода**
9
-  Плюсы
        - Код хорошо структурирован и понятен.
        - Используются асинхронные операции с `fetch` для отправки данных на сервер.
        - Обработка ошибок при отправке данных.
        - Логирование в консоль при успешной и неудачной отправке данных.
        - Использование `chrome.storage.local` для хранения данных.
        - Комментарии к коду, которые объясняют логику работы функций.

-  Минусы
    - Отсутствует обработка ошибок при получении данных из `chrome.storage.local`.
    - Не используется `src.logger.logger` для логирования.
    - URL сервера задан напрямую в коде, лучше использовать переменные окружения.
    - Нет reStructuredText (RST) документации для функций и модуля.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**
1. Добавить обработку ошибок при получении данных из `chrome.storage.local`.
2. Заменить `console.log` и `console.error` на использование `src.logger.logger`.
3. Вынести URL сервера в отдельную переменную окружения.
4. Добавить reStructuredText (RST) документацию для функций и модуля.
5. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` при работе с данными.
6. Добавить более информативные сообщения об ошибках.

**Оптимизированный код**

```python
"""
Модуль для фоновых скриптов расширения Edge.
==================================================

Этот модуль обрабатывает события расширения, такие как клик по иконке и получение сообщений,
а также отправляет собранные данные на сервер.
"""
from src.logger.logger import logger
from src.utils.jjson import j_loads

SERVER_URL = 'http://127.0.0.1/hypotez.online/api/'  # TODO: Вынести в переменные окружения


chrome.browserAction.onClicked.addListener(tab => {
    # Отправляет сообщение контентному скрипту для сбора данных
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    """
    Слушает сообщения, отправленные из других частей расширения.

    :param message: Сообщение, отправленное отправителем.
    :type message: dict
    :param sender: Информация об отправителе сообщения.
    :type sender: dict
    :param sendResponse: Функция для отправки ответа отправителю.
    :type sendResponse: function

    Если сообщение содержит действие `collectData`, вызывает функцию `sendDataToServer`
    с URL из сообщения.
    """
    if (message.action === 'collectData') {
        # Вызывает функцию отправки данных на сервер, передавая URL из сообщения
        sendDataToServer(message.url);
    }
});


def sendDataToServer(url: str):
    """
    Отправляет собранные данные на сервер.

    :param url: URL текущей вкладки, с которой были собраны данные.
    :type url: str

    Получает данные из локального хранилища, отправляет их на сервер,
    и логирует результат операции.
    """
    chrome.storage.local.get('collectedData', (result) => {
        #  Получает данные из локального хранилища
        collectedData = result.collectedData
        if not collectedData:
             # Если данные не найдены, логирует ошибку
             logger.error('No collected data found')
             return

        try:
            # Отправляет данные на сервер методом POST
            fetch(SERVER_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
                .then(response => {
                   # Проверяет статус ответа
                    if (!response.ok) {
                       # Если ответ не успешен, выбрасывает ошибку
                       raise Exception(f'Failed to send data to server: {response.status} {response.statusText}')
                    }
                     #  Логирует успешную отправку данных
                    logger.info('Data sent to server successfully')
                })
                .catch(error => {
                    # Логирует ошибку при отправке данных
                    logger.error(f'Error sending data to server: {error}')
                });
        except Exception as e:
              # Логирует ошибку при выполнении fetch
            logger.error(f'Error during fetch operation: {e}')
    });

```