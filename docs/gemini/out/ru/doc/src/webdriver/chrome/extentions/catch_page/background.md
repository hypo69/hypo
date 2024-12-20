# Документация для файла background.js

## Обзор

Данный файл `background.js` служит обработчиком событий для расширения Chrome. Он реагирует на клики по иконке расширения и собирает данные с активной страницы. Полученные данные отправляются на сервер для дальнейшей обработки.

## Обработчики событий

### `chrome.action.onClicked.addListener`

**Описание**: Этот обработчик запускается при клике по иконке расширения.

**Параметры**:

- `tab` (object): Объект, содержащий информацию о текущей вкладке.

**Действия**:

- Отправляет сообщение в активную вкладку с запросом на сбор данных.

### `chrome.runtime.onMessage.addListener`

**Описание**: Обработчик сообщений, слушает сообщения, отправленные из других частей расширения.

**Параметры**:

- `message` (object): Сообщение, полученное от другой части расширения.
- `sender` (object): Информация об отправителе сообщения.
- `sendResponse` (function): Функция, позволяющая отправить ответ отправителю.

**Действия**:

- Проверяет, является ли полученное сообщение запросом на сбор данных (`message.action === 'collectData'`).
- Если да, вызывает функцию `sendDataToServer` с URL текущей вкладки (`message.url`).

## Функции

### `sendDataToServer`

**Описание**: Отправляет собранные данные на сервер.

**Параметры**:

- `url` (string): URL текущей страницы.

**Действия**:

- Определяет адрес сервера (`serverUrl`).
- Получает данные из хранилища `chrome.storage.local` (`collectedData`).
- Если данные найдены:
    - Инициализирует `fetch` запрос к серверу с методом `POST` и данными в формате JSON.
    - Обрабатывает успешное отправление данных (`response.ok`).
    - Обрабатывает ошибки при отправке (`error`).
- Если данные не найдены, выводит сообщение об ошибке.


**Возвращает**:

- `undefined`.

**Вызывает исключения**:

- `Error`: Возникает, если возникла ошибка при отправке данных на сервер.


## Хранилище данных

Для сохранения данных используется хранилище `chrome.storage.local`, которое позволяет хранить данные в браузере между сеансами.


## Подробности о `fetch`

Функция `fetch` используется для отправки HTTP-запросов.  Важно учитывать статус ответа (`response.ok`) для обработки успешного или неуспешного выполнения запроса, а также возможные ошибки.  Обработка ошибок (`catch`) критична для стабильной работы расширения.  Обратите внимание на настройку заголовков (`headers`) для корректной отправки данных в формате JSON.


##  Взаимодействие с сервером

Этот код предполагает существование сервера на адресе `http://127.0.0.1/hypotez/catch_request.php`.  Необходимо настроить сервер для обработки `POST` запросов с JSON данными.


##  Возможное улучшение

В случае необходимости обработки ошибки (`Error`) следует предоставить более подробное сообщение об ошибке, включая информацию о типе ошибки и ее причине.  Это поможет в отладке расширения.  Добавление логов поможет отследить весь процесс.