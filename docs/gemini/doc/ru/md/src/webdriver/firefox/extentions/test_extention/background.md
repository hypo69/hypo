# Документация для файла background.js

## Обзор

Этот файл содержит скрипт расширения браузера, который выполняет код при нажатии на значок расширения. Он использует API `browser.scripting.executeScript` для запуска сценария `contentScript.js` в активной вкладке.

## Функции

### `browser.browserAction.onClicked.addListener`

**Описание**: Регистрирует обработчик события, который выполняется при нажатии на значок расширения.

**Параметры**:

- `(tab)` (object): Объект, содержащий информацию о вкладке, на которой произошёл клик.

**Возвращает**:
-  (void): Функция не возвращает никакого значения.

**Вызывает исключения**:
-  (None):  Не вызывает никаких исключений.


### `browser.scripting.executeScript`

**Описание**: Выполняет заданный скрипт в контексте указанной вкладки.

**Параметры**:

- `(options)` (object): Объект, содержащий параметры выполнения скрипта.
    - `target` (object): Параметр, описывающий контекст выполнения скрипта.
        - `tabId` (int): Идентификатор вкладки, в которой необходимо выполнить скрипт.
    - `files` (array): Массив путей к файлам скриптов, которые необходимо выполнить.


**Возвращает**:
-  (Promise): Обещание, которое разрешается, когда выполнение скрипта завершится. Возвращает результат выполнения скрипта.
   В случае ошибки или отсутствия результата, возвращает значение `undefined`.

**Вызывает исключения**:
- (Error):  Возможны ошибки при выполнении скрипта, например, если указан несуществующий `tabId` или `files` не найдены.