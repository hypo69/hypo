# Анализ кода модуля `send_data.js`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою задачу - сбор данных со страницы и отправку на сервер.
    - Используется `fetch` для отправки данных, что является современным подходом.
    - Присутствует обработка ошибок при запросе.
    - Данные формируются в JSON объект.
-  Минусы
    - Отсутствует документация и комментарии в формате reStructuredText (RST).
    - Нет обработки возможных ошибок JSON.stringify.
    - Не используются логирование ошибок.
    - Захардкожен URL для отправки запроса.
    - Желательно использовать более точные наименования переменных.
    - Нет проверки, что body не пустой перед отправкой.

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для модуля и функции.
2.  Использовать `logger.error` для логирования ошибок вместо `console.error`.
3.  Вынести URL в конфигурацию или переменную.
4.  Добавить проверку на пустоту `body` перед отправкой.
5.  Добавить обработку ошибок `JSON.stringify`.
6.  Использовать более точные имена для переменных.
7. Добавить проверку на `document` и `window` прежде чем работать с ними.

**Оптимизированный код**

```javascript
/**
 * Модуль для сбора и отправки данных о странице на сервер.
 * =======================================================
 *
 * Этот модуль собирает информацию о текущей странице, такую как заголовок, URL и HTML-содержимое,
 * и отправляет эти данные на указанный сервер.
 *
 * .. code-block:: javascript
 *
 *   // Пример использования модуля
 *   // После загрузки страницы данные автоматически отправляются на сервер.
 */

import { logger } from '../../../utils/logger';

/**
 * Функция обработчик события загрузки страницы.
 *
 * Собирает заголовок, URL и HTML-содержимое страницы и отправляет их на сервер.
 *
 * :raises Error: Если произошла ошибка при отправке данных.
 */
function onPageLoad() {
    // Код проверяет, что document и window существуют перед продолжением.
    if (!document || !window) {
        logger.error('Document or window object is not available.');
        return;
    }

    let pageTitle;
    let pageUrl;
    let pageBody;

    // Код извлекает заголовок страницы.
    try {
        pageTitle = document.title;
    } catch (error) {
        logger.error('Ошибка при получении заголовка страницы', error);
        return;
    }

    // Код извлекает URL страницы.
    try {
        pageUrl = window.location.href;
    } catch (error) {
        logger.error('Ошибка при получении URL страницы', error);
        return;
    }

    // Код извлекает HTML-содержимое страницы.
     try {
        pageBody = document.body.innerHTML;
    } catch (error) {
        logger.error('Ошибка при получении содержимого страницы', error);
        return;
    }

    // Код проверяет, что содержимое страницы не пустое.
    if (!pageBody) {
        logger.warn('Содержимое страницы пустое, отправка отменена.');
        return;
    }

    // Код формирует объект с данными для отправки.
    const data = {
        title: pageTitle,
        url: pageUrl,
        body: pageBody,
    };

    // Код преобразует объект данных в JSON-строку.
    let jsonData;
    try {
        jsonData = JSON.stringify(data);
    } catch (error) {
         logger.error('Ошибка при преобразовании данных в JSON', error);
         return;
    }

    // Код отправляет данные на указанный адрес.
    const apiUrl = 'http://127.0.0.1/hypotez.online/api/';
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: jsonData,
    })
        .then((response) => {
            // Код проверяет, что ответ от сервера успешный.
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.status}`);
            }
            return response.json();
        })
        .then((json) => {
             // Код выводит ответ от сервера.
            console.log('Response:', json);
        })
        .catch((error) => {
            // Код логирует ошибки при запросе.
             logger.error('Ошибка при отправке данных', error);
        });
}

// Код добавляет обработчик события для загрузки страницы.
if (window) {
   window.addEventListener('load', onPageLoad);
} else {
    logger.error('Window object is not available, event listener not attached.');
}
```