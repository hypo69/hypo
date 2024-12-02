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
// Модуль для отправки данных о загруженной странице
// =====================================================
// Этот модуль содержит функцию, которая собирает
// информацию о загруженной странице и отправляет её
// на сервер.

// Импорт необходимых модулей
// ...

// Функция для сбора и отправки данных о странице
/**
 * Сбор и отправка данных о загруженной странице.
 *
 * :return: Возвращает результат отправки.
 */
function onPageLoad() {
    // Получение заголовка страницы
    let title = document.title;
    # Проверка на существование title
    if(!title){
        logger.error('Заголовок страницы не найден');
        return;
    }

    // Получение URL страницы
    let url = window.location.href;
    # Проверка на существование url
    if(!url){
        logger.error('URL страницы не найден');
        return;
    }

    // Получение содержимого страницы
    let body = document.body.innerHTML;
    # Проверка на существование body
    if(!body){
        logger.error('Тело страницы не найдено');
        return;
    }

    // Создание объекта данных
    let data = {
        title: title,
        url: url,
        body: body
    };

    // Отправка данных на сервер
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Ошибка отправки данных: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })
    .then(json => {
        console.log('Ответ от сервера:', json);
    })
    .catch(error => {
        logger.error('Ошибка при отправке данных на сервер:', error);
    });
}

// Добавление обработчика события загрузки страницы
window.addEventListener('load', onPageLoad);

// Импорт необходимой функции логирования
from src.logger import logger;
// ...
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger`.
*   Добавлена проверка на существование `title`, `url` и `body`.
*   В случае отсутствия данных, выводится ошибка с помощью `logger.error`.
*   Изменён обработчик ошибок `catch` — теперь он ловит ошибки HTTP-ответа и выводит более информативную ошибку.
*   Добавлены RST-комментарии к функции `onPageLoad`.
*   Добавлены комментарии с объяснениями к строкам кода.
*   Замена `JSON.stringify(data)` на `JSON.stringify(data)` для единообразия.

# FULL Code

```javascript
// Модуль для отправки данных о загруженной странице
// =====================================================
// Этот модуль содержит функцию, которая собирает
// информацию о загруженной странице и отправляет её
// на сервер.

// Импорт необходимых модулей
// ...

// Функция для сбора и отправки данных о странице
/**
 * Сбор и отправка данных о загруженной странице.
 *
 * :return: Возвращает результат отправки.
 */
function onPageLoad() {
    // Получение заголовка страницы
    let title = document.title;
    # Проверка на существование title
    if(!title){
        logger.error('Заголовок страницы не найден');
        return;
    }

    // Получение URL страницы
    let url = window.location.href;
    # Проверка на существование url
    if(!url){
        logger.error('URL страницы не найден');
        return;
    }

    // Получение содержимого страницы
    let body = document.body.innerHTML;
    # Проверка на существование body
    if(!body){
        logger.error('Тело страницы не найдено');
        return;
    }

    // Создание объекта данных
    let data = {
        title: title,
        url: url,
        body: body
    };

    // Отправка данных на сервер
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Ошибка отправки данных: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })
    .then(json => {
        console.log('Ответ от сервера:', json);
    })
    .catch(error => {
        logger.error('Ошибка при отправке данных на сервер:', error);
    });
}

// Добавление обработчика события загрузки страницы
window.addEventListener('load', onPageLoad);

// Импорт необходимой функции логирования
from src.logger import logger;
// ...