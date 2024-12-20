# Модуль send_data.js

## Обзор

Данный модуль JavaScript содержит код для сбора информации о загруженной веб-странице и отправки её на сервер. Модуль использует `fetch` API для асинхронной отправки данных.

## Функции

### `onPageLoad`

**Описание**: Обработчик события загрузки страницы. Сбор информации о заголовке, URL и содержимом страницы, её сериализация в JSON и отправка на сервер.

**Описание параметров**:
Нет параметров.

**Возвращает**:
Нет возвращаемого значения.

**Обрабатывает исключения**:
- `Error`: Если HTTP-ответ не успешный (например, ошибка 400 или 500), или при ошибке во время обработки ответа от сервера. Ошибка логгируется в консоль.

### `fetch`

**Описание**: Асинхронная функция для отправки запроса на сервер.

**Описание параметров**:
- `'http://127.0.0.1/hypotez.online/api/'` (строка): URL-адрес сервера, куда будут отправляться данные.
- `{ method: 'POST', ... }` (объект): Параметры запроса:
    - `method: 'POST'`: Метод HTTP-запроса (POST).
    - `headers: {'Content-Type': 'application/json'}` (объект): Заголовок запроса, указывающий на тип данных (JSON).
    - `body: JSON.stringify(data)` (строка): Тело запроса - данные в формате JSON.

**Возвращает**:
- `Promise`: Объект `Promise`, содержащий результат запроса.

**Обрабатывает исключения**:
- `Error`: Если HTTP-ответ не успешный (например, ошибка 400 или 500), или при ошибке во время обработки ответа от сервера.
- `json`: Возвращает данные в формате JSON, полученные от сервера.


##  Использование

Функция `onPageLoad` вызывается автоматически при загрузке страницы. Данные, собранные с помощью этой функции, отправляются на сервер по указанному URL. Обработка ответа от сервера происходит в цепочке промисов.  Обратите внимание на обработку ошибок с помощью `.catch()`, чтобы предотвратить сбой скрипта при некорректном ответе сервера.


## Примечания

- Необходимо убедиться, что сервер, указанный в URL, готов принимать запросы POST и обрабатывать полученные данные.
-  Обработка ошибок (`.catch`) жизненно необходима для предотвращения ошибок при сбоях в коммуникации с сервером.
-  Дополнительно можно добавить логирование на сервере для отладки.
-  В коде используется `JSON.stringify(data)`, что важно для корректной передачи данных в формате JSON.