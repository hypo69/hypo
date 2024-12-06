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
// Модуль для отправки данных с загруженной страницы на сервер.
// ======================================================================================

/**
 * Обработчик события загрузки страницы.
 *
 * Эта функция собирает заголовок, URL и содержимое тела страницы
 * и отправляет эти данные на сервер для обработки.
 */
async function onPageLoad() {
    try {
        // Получаем заголовок страницы.
        const title = document.title;
        // Получаем URL страницы.
        const url = window.location.href;
        // Получаем содержимое тела страницы.
        const body = document.body.innerHTML;

        // Создаем объект с данными для отправки.
        const data = {
            title: title,
            url: url,
            body: body
        };

        // Отправляем данные на сервер.
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверка успешности ответа.
        if (!response.ok) {
            throw new Error(`Ошибка отправки данных: ${response.status} ${response.statusText}`);
        }

        // Обрабатываем ответ от сервера.
        const jsonResponse = await response.json();
        console.log('Ответ сервера:', jsonResponse);
    } catch (error) {
        // Обработка ошибок.
        const errorMessage = `Ошибка: ${error.message}`;
        console.error(errorMessage); // Выводим ошибку в консоль
        // Логирование ошибок для последующей обработки.
        // Используем logger из модуля src.logger.
        from src.logger import logger;
        logger.error(errorMessage, error); //Логируем ошибку с контекстом
    }
}


// Добавляем обработчик события загрузки страницы.
window.addEventListener('load', onPageLoad);
```

# Changes Made

*   Добавлены комментарии RST для описания функций и блоков кода.
*   Используется `async/await` для асинхронной обработки запроса.
*   Добавлена обработка ошибок с использованием `try...catch`.
*   Используется `logger.error` для записи сообщений об ошибках в лог.
*   Изменен способ обработки ошибок, добавлена информация о статусе ответа.
*   Исправлены комментарии.
*   Добавлен импорт `from src.logger import logger`.


# FULL Code

```javascript
// Модуль для отправки данных с загруженной страницы на сервер.
// ======================================================================================

/**
 * Обработчик события загрузки страницы.
 *
 * Эта функция собирает заголовок, URL и содержимое тела страницы
 * и отправляет эти данные на сервер для обработки.
 */
async function onPageLoad() {
    try {
        // Получаем заголовок страницы.
        const title = document.title;
        // Получаем URL страницы.
        const url = window.location.href;
        // Получаем содержимое тела страницы.
        const body = document.body.innerHTML;

        // Создаем объект с данными для отправки.
        const data = {
            title: title,
            url: url,
            body: body
        };

        // Отправляем данные на сервер.
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверка успешности ответа.
        if (!response.ok) {
            throw new Error(`Ошибка отправки данных: ${response.status} ${response.statusText}`);
        }

        // Обрабатываем ответ от сервера.
        const jsonResponse = await response.json();
        console.log('Ответ сервера:', jsonResponse);
    } catch (error) {
        // Обработка ошибок.
        const errorMessage = `Ошибка: ${error.message}`;
        console.error(errorMessage); // Выводим ошибку в консоль
        // Логирование ошибок для последующей обработки.
        // Используем logger из модуля src.logger.
        from src.logger import logger;
        logger.error(errorMessage, error); //Логируем ошибку с контекстом
    }
}


// Добавляем обработчик события загрузки страницы.
window.addEventListener('load', onPageLoad);