# Анализ кода модуля `background.js`

**Качество кода**
9
- Плюсы
    - Код выполняет свою основную функцию: сбор и отправку данных на сервер.
    - Присутствует обработка ошибок при отправке данных.
    - Используется `chrome.storage.local` для получения данных.
- Минусы
    - Отсутствуют комментарии в формате reStructuredText (RST).
    - Отсутствует обработка ошибок при получении данных из `chrome.storage.local`.
    - Не используется `logger` для логирования ошибок.
    - URL сервера жестко закодирован, что не является гибким решением.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Добавить документацию в формате RST для всех функций.
3.  Использовать `logger` для логирования ошибок и отладки.
4.  Добавить обработку ошибок при получении данных из `chrome.storage.local`.
5.  Вынести URL сервера в конфигурацию или переменную окружения.
6.  Улучшить форматирование кода для лучшей читаемости.

**Оптимизированный код**
```python
"""
Модуль фонового скрипта для сбора и отправки данных на сервер.
==============================================================

Этот модуль прослушивает события нажатия на иконку расширения и сообщения от контентных скриптов
для сбора данных и их отправки на сервер.
"""

from src.logger.logger import logger
import json

# Слушатель события нажатия на иконку расширения
chrome.browserAction.onClicked.addListener(tab => {
    # Отправка сообщения контентному скрипту для сбора данных
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

# Слушатель сообщений от контентных скриптов
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    # Проверка действия сообщения
    if (message.action === 'collectData') {
        # Вызов функции отправки данных на сервер
        sendDataToServer(message.url);
    }
});


def sendDataToServer(url):
    """
    Отправляет собранные данные на сервер.

    :param url: URL страницы, с которой были собраны данные.
    :type url: str
    """
    # URL сервера, TODO: вынести в настройки
    serverUrl = 'http://127.0.0.1/hypotez.online/api/'
    # Получение данных из локального хранилища
    chrome.storage.local.get('collectedData', (result) => {
        # Проверка наличия данных
        if (chrome.runtime.lastError) {
            logger.error(f'Ошибка при получении данных из локального хранилища: {chrome.runtime.lastError}')
            return
        }
        collectedData = result.collectedData
        if collectedData:
            # Отправка данных на сервер
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
            .then(response => {
                if (!response.ok) {
                    # Логирование ошибки отправки данных
                    logger.error(f'Не удалось отправить данные на сервер: {response.status} {response.statusText}')
                    return
                }
                logger.info('Данные успешно отправлены на сервер');
            })
            .catch(error => {
                # Логирование ошибки отправки данных
                logger.error(f'Ошибка отправки данных на сервер: {error}')
            });
        else:
            # Логирование отсутствия собранных данных
            logger.error('Не найдены собранные данные');
    });
}
```