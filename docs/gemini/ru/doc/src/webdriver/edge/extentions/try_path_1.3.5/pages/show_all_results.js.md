# Документация для `show_all_results.js`

## Обзор

Данный JavaScript-файл отвечает за отображение результатов выполнения XPath-запросов на странице расширения. Он обрабатывает данные, полученные от фоновой страницы, и отображает их в HTML-элементах. Файл также предоставляет возможность экспорта результатов в текстовый файл и выделения элементов на странице.

## Содержание

1. [Функции](#функции)
    - [`showAllResults`](#showallresults)
    - [`makeTextDownloadUrl`](#maketextdownloadurl)
    - [`makeInfoText`](#makeinfotext)
    - [`makeConvertedInfoText`](#makeconvertedinfotext)
2. [События](#события)
    - [`window.addEventListener("load")`](#windowaddeventlistenerload)

## Функции

### `showAllResults`

**Описание**: Функция отображает результаты выполнения XPath-запроса на странице.

**Параметры**:
- `results` (object): Объект, содержащий результаты запроса.
    - `message` (string): Сообщение об ошибке или успехе.
    - `title` (string): Заголовок страницы.
    - `href` (string): URL страницы.
    - `frameId` (number): ID фрейма.
    - `context` (object, optional): Объект, содержащий информацию о контексте запроса.
        - `method` (string): Метод контекста.
        - `expression` (string): Выражение контекста.
        - `specifiedResultType` (string): Заданный тип результата контекста.
        - `resultType` (string): Фактический тип результата контекста.
        - `resolver` (string): Резолвер контекста.
        - `itemDetail` (object, optional): Детали объекта контекста.
            - `type` (string): Тип объекта.
            - `name` (string): Имя объекта.
            - `value` (string): Значение объекта.
            - `textContent` (string): Текстовое содержимое объекта.
    - `main` (object): Объект, содержащий основную информацию о запросе.
        - `method` (string): Метод запроса.
        - `expression` (string): Выражение запроса.
        - `specifiedResultType` (string): Заданный тип результата запроса.
        - `resultType` (string): Фактический тип результата запроса.
        - `resolver` (string): Резолвер запроса.
        - `itemDetails` (Array<object>): Массив объектов с деталями результата запроса.
            - `type` (string): Тип объекта.
            - `name` (string): Имя объекта.
            - `value` (string): Значение объекта.
            - `textContent` (string): Текстовое содержимое объекта.

**Возвращает**:
- `undefined`: Функция ничего не возвращает.

**Вызывает исключения**:
- `onError`: Функция `fu.onError` вызывается при ошибке обновления таблицы деталей.

### `makeTextDownloadUrl`

**Описание**: Функция создает URL для скачивания текстового файла.

**Параметры**:
- `text` (string): Текст для скачивания.

**Возвращает**:
- `string`: URL для скачивания текстового файла.

### `makeInfoText`

**Описание**: Функция формирует текстовое представление результатов запроса.

**Параметры**:
- `results` (object): Объект, содержащий результаты запроса. (см. описание `showAllResults`)

**Возвращает**:
- `string`: Текстовое представление результатов.

### `makeConvertedInfoText`

**Описание**: Функция формирует текстовое представление результатов запроса с JSON-представлением значений.

**Параметры**:
- `results` (object): Объект, содержащий результаты запроса. (см. описание `showAllResults`)

**Возвращает**:
- `string`: Текстовое представление результатов с JSON.

## События

### `window.addEventListener("load")`

**Описание**: Функция обрабатывает событие загрузки страницы.

**Действия**:
- Отправляет сообщение `loadResults` фоновой странице для получения результатов.
- Устанавливает атрибуты `download` и `href` для ссылок экспорта.
- Вызывает функцию `showAllResults` для отображения данных.
- Устанавливает обработчики событий клика для таблиц деталей, чтобы выделять элементы на странице.

**Параметры**:
- `event` (Event): Событие загрузки страницы.

**Возвращает**:
- `undefined`: Функция ничего не возвращает.

**Вызывает исключения**:
- `onError`: Функция `fu.onError` вызывается при ошибке получения результатов или при ошибке в обработчиках событий.