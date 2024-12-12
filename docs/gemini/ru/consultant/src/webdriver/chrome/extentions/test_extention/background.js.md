# Анализ кода модуля `background.js`

**Качество кода**
7
-  Плюсы
    - Код выполняет основную задачу: обрабатывает клик по иконке расширения и отправляет данные на сервер.
    - Используется `chrome.storage.local` для хранения данных.
    - Присутствует обработка ошибок при отправке данных на сервер.
    - Код использует `chrome.runtime.onMessage` для обмена сообщениями.
-  Минусы
    - Отсутствуют docstring и комментарии в формате RST.
    - Используется `console.log` и `console.error` для логирования, что не подходит для продакшена.
    - Нет обработки ошибок при получении данных из `chrome.storage.local`.
    - URL сервера (`serverUrl`) жестко закодирован в коде.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring для модуля и функций в формате RST, чтобы улучшить читаемость и понимание кода.
2.  **Логирование**: Заменить `console.log` и `console.error` на использование `logger` из `src.logger.logger` для централизованного логирования.
3.  **Обработка ошибок**: Добавить обработку ошибок при получении данных из `chrome.storage.local`.
4.  **Конфигурация**: Вынести URL сервера в конфигурацию или использовать переменные окружения.
5.  **Форматирование**: Применить форматирование кода для улучшения читаемости.

**Оптимизированный код**

```python
"""
Модуль background.js для обработки событий расширения Chrome.
===========================================================

Этот модуль обрабатывает клики по иконке расширения и сообщения
от контентных скриптов, а также отправляет собранные данные на сервер.

Функции:
    - chrome.browserAction.onClicked.addListener: Обрабатывает клик по иконке расширения.
    - chrome.runtime.onMessage.addListener: Слушает сообщения от других частей расширения.
    - sendDataToServer: Отправляет данные на сервер.

Пример использования:
    При клике на иконку расширения, данные со страницы отправляются на сервер.
"""
from src.logger.logger import logger
import json


# Обработчик клика по иконке расширения.
chrome.browserAction.onClicked.addListener(tab => {
    #  Отправка сообщения контентному скрипту для сбора данных.
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});


# Слушатель сообщений от контентных скриптов.
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Проверка, что сообщение имеет действие 'collectData'.
    if (message.action === 'collectData') {
        #  Вызов функции для отправки данных на сервер.
        sendDataToServer(message.url);
    }
});


def sendDataToServer(url: str):
    """
    Отправляет собранные данные на сервер.

    :param url: URL текущей страницы.
    :return: None
    """
    # URL сервера, куда будут отправляться данные.
    serverUrl = 'http://127.0.0.1/hypotez.online/api/';
    #  Получение данных из локального хранилища.
    chrome.storage.local.get('collectedData', (result) => {
        # Извлечение данных из результата.
        collectedData = result.collectedData;
        # Проверка, что данные существуют.
        if (collectedData) {
             # Отправка данных на сервер.
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: json.dumps(collectedData)
            })
            .then(response => {
                 # Проверка успешности ответа сервера.
                if (!response.ok) {
                    #  Логирование ошибки отправки данных.
                    logger.error(f'Failed to send data to server: {response.status} {response.statusText}')
                    return
                }
                # Логирование успешной отправки данных.
                logger.info('Data sent to server successfully');
            })
            .catch(error => {
                 # Логирование ошибок при отправке данных.
                logger.error(f'Error sending data to server: {error}');
            });
        } else {
            #  Логирование ошибки, если данные не найдены.
            logger.error('No collected data found');
        }
    });
}
```