# Received Code

```javascript
document.getElementById("sendUrlButton").addEventListener("click", () => {
    alert("Hello, world!");
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        let activeTab = tabs[0];
        let activeTabUrl = activeTab.url;
        
        chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
            if (response.status === "success") {
                alert("URL sent successfully!");
            } else {
                alert("Failed to send URL.");
            }
        });
    });
});
```

# Improved Code

```javascript
"""
Модуль для отправки текущего URL активной вкладки в контекст расширения.
=======================================================================

Этот модуль содержит код, который отправляет URL активной вкладки в
контекст расширения. Код реагирует на нажатие кнопки "Отправить URL".
"""
import json

# Импорт модуля для логирования.
from src.logger import logger

# Функция для отправки URL активной вкладки.
async def send_active_tab_url():
    """Отправляет URL активной вкладки в контекст расширения.

    :raises Exception: Если возникает ошибка при получении URL или отправке сообщения.
    """
    try:
        # Получение активной вкладки.
        active_tab = await chrome.tabs.query({
            'active': True,
            'currentWindow': True,
        })

        # Проверка, что активная вкладка найдена.
        if not active_tab || active_tab.length === 0:
            logger.error("Активная вкладка не найдена.")
            return

        # Извлечение URL активной вкладки.
        active_tab_url = active_tab[0].url;
            
        # Проверка, что URL активной вкладки существует.
        if (!active_tab_url):
            logger.error("URL активной вкладки не найден.");
            return

        # Создание объекта сообщения для отправки.
        message = {
            'action': 'sendUrl',
            'url': active_tab_url
        }

        # Отправка сообщения в контекст расширения.
        chrome.runtime.sendMessage(message, (response) => {
            if (response && response.status === 'success') {
                logger.info("URL успешно отправлен.");
            } else {
                logger.error("Ошибка при отправке URL.");
            }
        });


    except Exception as e:
        logger.error("Ошибка при обработке URL активной вкладки:", e)
        return


# Добавление обработчика клика на кнопку.
document.getElementById("sendUrlButton").addEventListener("click", async () => {
   # Отправка URL активной вкладки.
   await send_active_tab_url();
});
```

# Changes Made

* Добавлена функция `send_active_tab_url()`, которая обрабатывает весь процесс отправки URL.
* Добавлена обработка ошибок с помощью `try...except` и логирования ошибок с помощью `logger.error()`.
* Добавлено условие проверки существования active_tab и active_tab_url, чтобы избежать ошибок.
* Изменен код для отправки сообщения через `chrome.runtime.sendMessage(message, (response))`.
* Добавлено описание функций, методов и переменных в формате RST.
* Подключен import модуля для логирования `from src.logger import logger`.
* Изменен стиль alert на использование логирования.
* Код отформатирован для лучшей читаемости.
* Добавлено логирование успешного отправления через `logger.info()`.
* Изменен синтаксис для проверки существования `active_tab`.
* Добавлен await для асинхронной функции.


# FULL Code

```javascript
"""
Модуль для отправки текущего URL активной вкладки в контекст расширения.
=======================================================================

Этот модуль содержит код, который отправляет URL активной вкладки в
контекст расширения. Код реагирует на нажатие кнопки "Отправить URL".
"""
import json

# Импорт модуля для логирования.
from src.logger import logger

# Функция для отправки URL активной вкладки.
async def send_active_tab_url():
    """Отправляет URL активной вкладки в контекст расширения.

    :raises Exception: Если возникает ошибка при получении URL или отправке сообщения.
    """
    try:
        # Получение активной вкладки.
        active_tab = await chrome.tabs.query({
            'active': True,
            'currentWindow': True,
        })

        # Проверка, что активная вкладка найдена.
        if not active_tab || active_tab.length === 0:
            logger.error("Активная вкладка не найдена.")
            return

        # Извлечение URL активной вкладки.
        active_tab_url = active_tab[0].url;
            
        # Проверка, что URL активной вкладки существует.
        if (!active_tab_url):
            logger.error("URL активной вкладки не найден.");
            return

        # Создание объекта сообщения для отправки.
        message = {
            'action': 'sendUrl',
            'url': active_tab_url
        }

        # Отправка сообщения в контекст расширения.
        chrome.runtime.sendMessage(message, (response) => {
            if (response && response.status === 'success') {
                logger.info("URL успешно отправлен.");
            } else {
                logger.error("Ошибка при отправке URL.");
            }
        });


    except Exception as e:
        logger.error("Ошибка при обработке URL активной вкладки:", e)
        return


# Добавление обработчика клика на кнопку.
document.getElementById("sendUrlButton").addEventListener("click", async () => {
   # Отправка URL активной вкладки.
   await send_active_tab_url();
});