# Модуль show_all_results.js

## Обзор

Этот модуль отвечает за отображение результатов поиска, полученных через расширение браузера. Он динамически обновляет содержимое страницы, отображая результаты запроса в виде таблиц и текстовых полей.  Модуль также предоставляет возможность экспорта результатов в текстовые файлы в различных форматах.

## Функции

### `showAllResults`

**Описание**: Функция отображает результаты поиска на странице. Она принимает объект `results` содержащий данные о поиске и обновляет элементы страницы с соответствующей информацией.

**Параметры**:

- `results` (объект): Объект, содержащий результаты поиска. Должен содержать поля `message`, `title`, `href`, `frameId`, `context` (опционально), и `main`.

**Возвращает**:
  - Не имеет возвращаемого значения.


**Вызывает исключения**:
-  `fu.onError`: Функция обработки ошибок.


### `makeTextDownloadUrl`

**Описание**: Функция генерирует URL для скачивания текстового файла.

**Параметры**:

- `text` (строка): Текст, который нужно сохранить в файле.

**Возвращает**:
- `строка`: URL для скачивания текстового файла.

**Вызывает исключения**:
- Не вызывает исключений.


### `makeInfoText`

**Описание**: Функция формирует текстовое представление результатов поиска в формате, подходящем для экспорта.

**Параметры**:

- `results` (объект): Объект, содержащий результаты поиска.

**Возвращает**:
- `строка`: Текстовое представление результатов поиска.

**Вызывает исключения**:
- Не вызывает исключений.


### `makeConvertedInfoText`

**Описание**: Функция формирует текстовое представление результатов поиска в формате, подходящем для экспорта, с преобразованием значений в JSON.

**Параметры**:

- `results` (объект): Объект, содержащий результаты поиска.

**Возвращает**:
- `строка`: Текстовое представление результатов поиска.

**Вызывает исключения**:
- Не вызывает исключений.


##  Обработчики событий

### `window.addEventListener("load")`

**Описание**: Вешает обработчик события `load` на глобальный объект `window`. При загрузке страницы, отправляет запрос `browser.runtime.sendMessage({"event":"loadResults"})` для получения результатов поиска и отображения их на странице. Обрабатывает полученные результаты.

**Параметры**:

- Не имеет параметров.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `fu.onError`: Обработчик ошибок.

### `contDetail.addEventListener("click")`

**Описание**:  Вешает обработчик события `click` на элемент с `id="context-detail"`. Обрабатывает нажатия на кнопки внутри таблицы деталей контекста и отправляет соответствующий запрос `browser.tabs.sendMessage` для фокусировки на выбранном элементе.

**Параметры**:

- `event` (объект события): Объект события нажатия.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- Не вызывает исключений.


### `mainDetails.addEventListener("click")`

**Описание**: Вешает обработчик события `click` на элемент с `id="main-details"`. Обрабатывает нажатия на кнопки внутри таблицы деталей основных результатов и отправляет соответствующий запрос `browser.tabs.sendMessage` для фокусировки на выбранном элементе.

**Параметры**:

- `event` (объект события): Объект события нажатия.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- Не вызывает исключений.


##  Вспомогательные переменные и функции

**Примечание**: В данном коде присутствуют `detailKeys`, `headerValues` и другие переменные, которые представляют собой массивы. Подробное описание этих массивов, скорее всего, содержится в других частях кода или в документации к ним.  Также, в коде присутствует функция `fu.updateDetailsTable` и `fu.onError`, которые должны быть описаны в других модулях.