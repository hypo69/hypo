# Модуль send_data.js

## Обзор

Данный модуль JavaScript отвечает за сбор информации о загруженной странице (заголовок, URL, содержимое) и отправку этих данных на сервер по заданному API-адресу. Модуль использует `fetch` API для асинхронной отправки данных.

## Функции

### `onPageLoad`

**Описание**: Функция `onPageLoad` собирает информацию о загруженной странице, формирует объект данных и отправляет его на сервер с помощью запроса POST.

**Детали**:

1. **Сбор информации:** Извлекает заголовок страницы (`document.title`), URL страницы (`window.location.href`) и содержимое тела страницы (`document.body.innerHTML`).
2. **Формирование данных:** Создает объект `data` с полученной информацией.
3. **Отправка данных:** Использует `fetch` API для отправки запроса POST на заданный API-адрес ('http://127.0.0.1/hypotez.online/api/'). Заголовок запроса устанавливается как `application/json`.  Тело запроса содержит JSON-представление объекта `data`.
4. **Обработка ответа:** Обрабатывает ответ от сервера. Если ответ не успешный (`response.ok`), генерируется ошибка. В противном случае, функция `then` преобразует ответ в JSON и выводит полученный JSON в консоль.
5. **Обработка ошибок:** Обрабатывает возможные ошибки при отправке запроса или обработке ответа. В случае ошибки, выводит ошибку в консоль.


##  Обработка событий

### `window.addEventListener('load', onPageLoad);`

**Описание**: Устанавливает обработчик события `load` для окна браузера. Когда страница загружается, функция `onPageLoad` вызывается автоматически.

**Детали**:  Это гарантирует, что функция `onPageLoad` будет выполнена только после полной загрузки страницы.