# Received Code

```javascript
// Создаем обработчик события для загрузки страницы
function onPageLoad() {
    // Собираем информацию о странице
    var title = document.title;
    var url = window.location.href;
    var body = document.body.innerHTML;

    // Формируем объект с данными для отправки
    var data = {
        title: title,
        url: url,
        body: body
    };

    // Отправляем данные на указанный адрес
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            console.log('Response:', json);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Добавляем обработчик события для загрузки страницы
window.addEventListener('load', onPageLoad);
```

# Improved Code

```javascript
// Модуль для отправки данных с загруженной страницы на сервер
// ===========================================================

/**
 * Функция для сбора информации с загруженной страницы.
 *
 * Сбор заголовка страницы, URL и содержимого body.
 *
 * :return: Объект с собранными данными.
 */
function collectPageDetails() {
    // Получаем заголовок страницы
    const title = document.title;
    // Получаем URL страницы
    const url = window.location.href;
    // Получаем содержимое body страницы
    const body = document.body.innerHTML;

    // Возвращаем объект с данными
    return {
        title,
        url,
        body
    };
}


/**
 * Функция отправки данных на сервер.
 *
 * :param data: Объект с данными для отправки.
 */
async function sendDataToServer(data) {
    try {
        // Отправляем данные на сервер с помощью fetch.
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверка успешности ответа от сервера.
        if (!response.ok) {
            const errorText = `Ошибка отправки данных: HTTP статус ${response.status}`;
            throw new Error(errorText);
        }

        // Парсим ответ от сервера как JSON.
        const jsonResponse = await response.json();
        // Выводим ответ на консоль.
        console.log('Ответ сервера:', jsonResponse);
    } catch (error) {
        // Логируем ошибку, если произошла ошибка при отправке данных.
        const errorMessage = `Ошибка отправки данных на сервер: ${error.message}`;
        console.error(errorMessage);
        // Логируем подробную информацию об ошибке.
        import {logger} from 'src.logger'
        logger.error(errorMessage, error)
    }
}

/**
 * Функция для инициализации отправки данных после загрузки страницы.
 */
function initializePageLoadHandler() {
    // Обработчик события загрузки страницы
    window.addEventListener('load', () => {
        // Сбор данных с страницы
        const pageData = collectPageDetails();
        // Отправка данных на сервер
        sendDataToServer(pageData)
    });
}


// Инициализация обработчика событий
initializePageLoadHandler()
```

# Changes Made

*   Добавлены комментарии RST для функций и блоков кода.
*   Используется `async/await` для обработки `fetch` запроса, избегая цепочек `.then`.
*   Добавлена обработка ошибок с использованием `try...catch` и `logger.error` из `src.logger`.
*   Изменён способ сбора данных. Теперь это функция collectPageDetails().
*   Изменён способ отправки данных - теперь это функция sendDataToServer().
*   Изменён способ инициализации обработчика события - теперь это функция initializePageLoadHandler().
*   Добавлено обращение к logger.
*   Добавлены проверки на `response.ok`.
*   Изменён стиль импорта и логирования ошибок.

# FULL Code

```javascript
// Модуль для отправки данных с загруженной страницы на сервер
// ===========================================================

/**
 * Функция для сбора информации с загруженной страницы.
 *
 * Сбор заголовка страницы, URL и содержимого body.
 *
 * :return: Объект с собранными данными.
 */
function collectPageDetails() {
    // Получаем заголовок страницы
    const title = document.title;
    // Получаем URL страницы
    const url = window.location.href;
    // Получаем содержимое body страницы
    const body = document.body.innerHTML;

    // Возвращаем объект с данными
    return {
        title,
        url,
        body
    };
}


/**
 * Функция отправки данных на сервер.
 *
 * :param data: Объект с данными для отправки.
 */
async function sendDataToServer(data) {
    try {
        // Отправляем данные на сервер с помощью fetch.
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверка успешности ответа от сервера.
        if (!response.ok) {
            const errorText = `Ошибка отправки данных: HTTP статус ${response.status}`;
            throw new Error(errorText);
        }

        // Парсим ответ от сервера как JSON.
        const jsonResponse = await response.json();
        // Выводим ответ на консоль.
        console.log('Ответ сервера:', jsonResponse);
    } catch (error) {
        // Логируем ошибку, если произошла ошибка при отправке данных.
        const errorMessage = `Ошибка отправки данных на сервер: ${error.message}`;
        console.error(errorMessage);
        // Логируем подробную информацию об ошибке.
        import {logger} from 'src.logger'
        logger.error(errorMessage, error)
    }
}

/**
 * Функция для инициализации отправки данных после загрузки страницы.
 */
function initializePageLoadHandler() {
    // Обработчик события загрузки страницы
    window.addEventListener('load', () => {
        // Сбор данных с страницы
        const pageData = collectPageDetails();
        // Отправка данных на сервер
        sendDataToServer(pageData)
    });
}


// Инициализация обработчика событий
initializePageLoadHandler()