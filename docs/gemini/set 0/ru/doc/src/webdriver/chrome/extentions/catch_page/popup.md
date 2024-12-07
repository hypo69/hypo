# Модуль popup.js

## Обзор

Данный скрипт обрабатывает нажатие кнопки "Отправить URL" в всплывающем окне расширения Chrome. Он получает активную вкладку, извлекает ее URL и отправляет его в background script для дальнейшей обработки.

## Функции

### `addEventListener`

**Описание**:  Регистрирует обработчик события `click` для элемента с id `sendUrlButton`.

**Параметры**:
- `event`:  Событие нажатия кнопки.

**Вызывает исключения**:
  - `Error`: Любые ошибки во время обработки события.


### Анонимная функция (обработчик события `click`)

**Описание**: Выполняется при нажатии кнопки "Отправить URL". Выводит диалоговое окно с сообщением "Hello, world!", получает активную вкладку и отправляет ее URL в background script.

**Вызывает исключения**:
  - `Error`: Любые ошибки при получении активной вкладки или отправке сообщения.

### `chrome.tabs.query`

**Описание**: Запрашивает информацию об активной вкладке.

**Параметры**:
- `{ active: true, currentWindow: true }`:  Критерий для выбора активной вкладки в текущем окне.

**Возвращает**:
- `tabs`: Массив, содержащий информацию об активной вкладке.

**Вызывает исключения**:
  - `Error`: Ошибки при запросе информации о вкладке.

### `tabs[0]`

**Описание**: Возвращает первую (и единственную, в данном случае) вкладку из массива `tabs`.

**Параметры**:
  - `tabs`: Массив вкладок, полученный из `chrome.tabs.query`.

**Возвращает**:
- `activeTab`: Объект, содержащий информацию об активной вкладке.

### `activeTab.url`

**Описание**: Извлекает URL активной вкладки.

**Параметры**:
- `activeTab`: Объект, содержащий информацию об активной вкладке.

**Возвращает**:
- `string`: Строка, содержащая URL активной вкладки.

### `chrome.runtime.sendMessage`

**Описание**: Отправляет сообщение в background script.

**Параметры**:
- `{ action: "sendUrl", url: activeTabUrl }`: Объект с параметрами для сообщения.
    - `action`: Строка, определяющая действие, которое необходимо выполнить в background script.
    - `url`: URL активной вкладки, полученный из `activeTab.url`.
- `(response) => { ... }`: Обработчик ответа от background script.


**Возвращает**:
- `response`: Объект, содержащий ответ от background script.

**Вызывает исключения**:
  - `Error`: Любые ошибки при отправке сообщения или получении ответа.

### `alert`

**Описание**: Выводит диалоговое окно с сообщением.

**Параметры**:
- `message`: Текст сообщения для отображения в диалоговом окне.

**Возвращает**:
- `void`: Данная функция не возвращает значений.

**Вызывает исключения**:
  - `Error`: Любые ошибки при отображении диалогового окна.