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
// Модуль для отправки данных с веб-страницы на сервер
// ===================================================

/**
 * Функция для сбора информации с загруженной страницы.
 * 
 * Сбор заголовка страницы, URL и содержимого тела.
 * 
 * :return: Объект с собранными данными.
 */
function collectPageData() {
    // Сбор информации о странице
    const title = document.title;
    const url = window.location.href;
    const body = document.body.innerHTML;
  
    // Возвращаем собранные данные
    return {
        title,
        url,
        body
    };
}

/**
 * Функция для отправки данных на сервер.
 * 
 * Отправляет собранную информацию с использованием fetch API.
 * 
 * :param data: Объект с данными для отправки.
 */
async function sendDataToAPI(data) {
    try {
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Ошибка при отправке данных: ${response.status} ${response.statusText}`);
        }

        const jsonResponse = await response.json();
        console.log('Ответ сервера:', jsonResponse);
        return jsonResponse; // Возвращаем ответ от сервера
    } catch (error) {
        // Обработка ошибок
        console.error('Ошибка отправки:', error);
        // Более подробное логирование ошибок
        from src.logger import logger
        logger.error('Ошибка при отправке данных на сервер:', error);
        return null; // Указываем, что ответ не получен
    }
}


/**
 * Обработчик события загрузки страницы.
 * 
 * Выполняет сбор данных и отправку на сервер.
 */
async function onPageLoad() {
    const pageData = collectPageData(); // Сбор данных
    const response = await sendDataToAPI(pageData); // Отправка данных на сервер
    if (!response) {
        // Обработка случая, когда ответ не получен
        console.log('Ошибка отправки или нет ответа от сервера.');
    }
}


// Добавление обработчика события загрузки страницы
window.addEventListener('load', onPageLoad);
```

# Changes Made

*   Добавлены комментарии в формате RST ко всем функциям и блокам кода.
*   Используется `async/await` для обработки асинхронного запроса `fetch`.
*   Добавлена функция `collectPageData` для улучшения структуры.
*   Функция `sendDataToAPI` возвращает результат или null в случае ошибки.
*   Обработка ошибок `fetch` API улучшена.
*   Добавлена обработка ответа сервера (возвращается результат)
*   Добавлена обработка ошибки при отсутствии ответа или ошибке отправки.
*   Использование `logger` для логирования ошибок.
*   Улучшен код обработки ошибок, теперь он возвращает null в случае ошибки.

# FULL Code

```javascript
// Модуль для отправки данных с веб-страницы на сервер
// ===================================================

/**
 * Функция для сбора информации с загруженной страницы.
 * 
 * Сбор заголовка страницы, URL и содержимого тела.
 * 
 * :return: Объект с собранными данными.
 */
function collectPageData() {
    // Сбор информации о странице
    const title = document.title;
    const url = window.location.href;
    const body = document.body.innerHTML;
  
    // Возвращаем собранные данные
    return {
        title,
        url,
        body
    };
}

/**
 * Функция для отправки данных на сервер.
 * 
 * Отправляет собранную информацию с использованием fetch API.
 * 
 * :param data: Объект с данными для отправки.
 */
async function sendDataToAPI(data) {
    try {
        const response = await fetch('http://127.0.0.1/hypotez.online/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Ошибка при отправке данных: ${response.status} ${response.statusText}`);
        }

        const jsonResponse = await response.json();
        console.log('Ответ сервера:', jsonResponse);
        return jsonResponse; // Возвращаем ответ от сервера
    } catch (error) {
        // Обработка ошибок
        console.error('Ошибка отправки:', error);
        // Более подробное логирование ошибок
        from src.logger import logger
        logger.error('Ошибка при отправке данных на сервер:', error);
        return null; // Указываем, что ответ не получен
    }
}


/**
 * Обработчик события загрузки страницы.
 * 
 * Выполняет сбор данных и отправку на сервер.
 */
async function onPageLoad() {
    const pageData = collectPageData(); // Сбор данных
    const response = await sendDataToAPI(pageData); // Отправка данных на сервер
    if (!response) {
        // Обработка случая, когда ответ не получен
        console.log('Ошибка отправки или нет ответа от сервера.');
    }
}


// Добавление обработчика события загрузки страницы
window.addEventListener('load', onPageLoad);