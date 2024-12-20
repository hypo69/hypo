# Модуль `background.js`

## Обзор

Данный модуль отвечает за обработку сообщений, полученных от других частей расширения (например, контентных скриптов), и за отправку данных на сервер.  Он слушает сообщения с действием `'collectData'` и, при получении такого сообщения, вызывает функцию `sendDataToServer()`, для отправки URL на сервер для сбора данных.

## Функции

### `sendDataToServer`

**Описание**: Функция отправляет собранные данные на сервер.

**Параметры**:

- `url` (str): URL страницы, для которой необходимо собрать данные.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Обрабатывает исключения**:

- `Error`: Если возникает ошибка при отправке данных на сервер (например, сетевая ошибка).

**Подробное описание**:

Функция `sendDataToServer` отправляет данные на указанный сервер. Она использует API `chrome.storage.local` для получения ранее собранных данных и `fetch` API для отправки запроса POST на сервер. В случае успешной отправки, она выводит сообщение в консоль. При возникновении ошибки она выводит сообщение об ошибке в консоль.

### `chrome.action.onClicked.addListener`

**Описание**: Функция, которая реагирует на клик на иконке расширения.

**Параметры**:

- `tab` (object): Объект, содержащий информацию о вкладке, на которой был нажат клик.

**Возвращает**:
- Не имеет возвращаемого значения.

**Подробное описание**:

Функция `chrome.action.onClicked.addListener` обрабатывает события клика на иконке расширения. При нажатии на иконку, она отправляет сообщение в активную вкладку с действием `'collectData'` и URL текущей вкладки.


### `chrome.runtime.onMessage.addListener`

**Описание**: Функция, слушающая сообщения, отправленные из других частей расширения.

**Параметры**:

- `message` (object): Сообщение, отправленное из другой части расширения.
- `sender` (object): Информация о отправителе сообщения.
- `sendResponse` (function): Функция для отправки ответа отправителю.

**Возвращает**:
- boolean: `true`, чтобы удерживать канал связи, позволяя отправлять ответы.

**Подробное описание**:

Функция `chrome.runtime.onMessage.addListener` прослушивает сообщения, отправленные другими частями расширения. При получении сообщения с действием `'collectData'` она вызывает функцию `sendDataToServer`, передавая в нее URL из сообщения.  Возвращает `true`, чтобы закрыть канал связи.


## Хранилище


### `chrome.storage.local`

**Описание**: Используется для сохранения и получения данных в локальном хранилище расширения.

**Подробное описание**:

Функция `sendDataToServer` использует `chrome.storage.local.get('collectedData', ...)` для получения ранее собранных данных.  Эти данные, предполагается, были сохранены в расширении ранее.

## API


### `fetch`

**Описание**: Используется для отправки HTTP запросов.

**Подробное описание**:

В функции `sendDataToServer` используется метод `fetch` для отправки POST запроса на сервер `http://127.0.0.1/hypotez/catch_request.php`.  Важным является параметр `'Content-Type': 'application/json'`, который сообщает серверу о формате отправляемых данных.

## Замечания

- Необходимо заменить `'http://127.0.0.1/hypotez/catch_request.php'` на действительный адрес сервера.
- Функция `sendDataToServer` ожидает, что данные, которые необходимо отправить, будут доступны в `chrome.storage.local` с ключом `'collectedData'`.
- Необходимо добавить обработку сценариев, где данных нет (`collectedData === undefined`).