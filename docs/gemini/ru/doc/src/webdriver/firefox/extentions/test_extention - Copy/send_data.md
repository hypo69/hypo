# Модуль `send_data.js`

## Обзор

Этот скрипт JavaScript собирает информацию о загруженной странице (заголовок, URL, содержимое тела) и отправляет её на сервер по адресу `http://127.0.0.1/hypotez.online/api/` в формате JSON.  Скрипт использует `fetch` для отправки запроса.  При успешной отправке и получении ответа, скрипт выводит ответ в консоль.  В случае ошибки, скрипт выводит сообщение об ошибке в консоль.


## Функции

### `onPageLoad()`

**Описание**: Обрабатывает событие загрузки страницы.  Собирает информацию о странице, формирует JSON объект и отправляет его на сервер.

**Логика**:

1. **Сбор данных**: Получает заголовок страницы (`document.title`), URL (`window.location.href`) и HTML содержимое тела страницы (`document.body.innerHTML`).
2. **Формирование данных**: Создаёт объект `data` содержащий полученную информацию.
3. **Отправка запроса**: Использует `fetch` для отправки POST запроса на сервер с JSON данными.
4. **Обработка ответа**: Обрабатывает Promise `fetch`, обрабатывает успешный ответ и данные, полученные от сервера. Выводит ответ в консоль.  Обрабатывает ошибку в случае неуспешного ответа от сервера, выводит сообщение об ошибке в консоль.

**Вызывает исключения**:
- `Error`: В случае неуспешного ответа от сервера (`response.ok == false`).


**Пример использования**:
```javascript
onPageLoad(); // Вызов функции при загрузке страницы
```


## Методы


Этот скрипт не содержит методов в классическом понимании (т.е., методы класса).  Он содержит только функцию `onPageLoad()`.


## Дополнительные замечания

* Требуется серверная обработка для получения и обработки отправленных данных.
* Важно проверить корректность пути к серверу (`http://127.0.0.1/hypotez.online/api/`).
* Скрипт предполагает, что на сервере установлена обработка POST запросов с JSON данными.
* Обработка ошибок должна быть расширена для более информативных сообщений об ошибках.
* При некорректном формате отправляемых данных, необходимо предусмотреть обработку ошибок на стороне сервера.