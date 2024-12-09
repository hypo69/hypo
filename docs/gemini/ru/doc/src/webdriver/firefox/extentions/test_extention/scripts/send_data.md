# Модуль `send_data.js`

## Обзор

Этот скрипт JavaScript собирает информацию о загруженной веб-странице (заголовок, URL, содержимое) и отправляет её на сервер по заданному API-адресу.

## Функции

### `onPageLoad`

**Описание**: Обработчик события `load` для браузера.  Выполняется после полной загрузки страницы. Сбор данных о странице и отправка их на сервер.

**Вызывает исключения**:
- `Error`:  Возникает, если запрос к серверу не был успешным (например, сервер вернул ошибку).


```javascript
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
```


## Дополнительные пояснения

* Функция `onPageLoad` использует `fetch` для отправки POST-запроса на указанный API-адрес.
* Данные отправляются в формате JSON.
* Обработка ошибок `catch` позволяет ловить и выводить ошибки в консоль.
* `response.ok` проверяет, был ли запрос успешен. Если нет, выбрасывается исключение `Error` с соответствующим сообщением.
* Обработчик `then` для успешного ответа обрабатывает полученный JSON-ответ.
* В JavaScript нет явной типизации параметров и возвращаемых значений, как в Python.
*  Функции, использующие `fetch`, асинхронны, и требуется использовать `then` и `catch` для обработки успешного ответа и ошибок.


## Особенности использования

Для запуска скрипта необходимо, чтобы страница была загружена. Обработчик `addEventListener`  обеспечивает вызов `onPageLoad` при загрузке страницы.