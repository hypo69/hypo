# Модуль `show_all_results.js`

## Обзор

Этот JavaScript-модуль отвечает за отображение результатов поиска, полученных из расширения `tryxpath`. Он заполняет элементы HTML на странице, отображая информацию о контексте и основных результатах.  Модуль включает функции для загрузки результатов в текстовом формате, а также для фокусировки на конкретных элементах результатов в открытом вкладе.

## Функции

### `showAllResults`

**Описание**: Функция отображает результаты поиска в интерфейсе пользователя. Она принимает объект `results`, содержащий информацию о поиске, и обновляет соответствующие HTML-элементы.

**Параметры**:
- `results` (объект): Объект с результатами поиска, содержащий информацию о сообщении, заголовке, URL, идентификаторе фрейма, контексте и основных результатах.

**Возвращает**:
- Не имеет значения возвращаемого значения.

**Вызывает исключения**:
- `fu.onError`:  Вызывается в случае возникновения ошибки при обновлении таблицы деталей.

### `makeTextDownloadUrl`

**Описание**: Функция генерирует URL для скачивания текста.

**Параметры**:
- `text` (строка): Текст, который нужно скачать.

**Возвращает**:
- `string`: URL для скачивания текста.

**Вызывает исключения**:
- Не вызывает исключений.

### `makeInfoText`

**Описание**: Функция создает текстовое представление результатов для скачивания, в формате, удобном для чтения.

**Параметры**:
- `results` (объект): Объект с результатами поиска.

**Возвращает**:
- `string`: Строка, содержащая отформатированную информацию о результатах.


**Вызывает исключения**:
- Не вызывает исключений.

### `makeConvertedInfoText`

**Описание**: Функция создает текстовое представление результатов для скачивания, в формате с JSON-представлением значений.

**Параметры**:
- `results` (объект): Объект с результатами поиска.


**Возвращает**:
- `string`: Строка, содержащая отформатированную информацию о результатах.


**Вызывает исключения**:
- Не вызывает исключений.


## Обработка событий

### `window.addEventListener("load", ...)`

**Описание**:  Слушает событие загрузки страницы и выполняет дальнейшие действия по обработке результатов.

**Описание**:  Получает результаты поиска из расширения, инициализирует и обновляет элементы HTML, а также устанавливает обработчики событий для кнопок фокусировки на элементах результатов.

**Вызывает исключения**:
- `fu.onError`: Обрабатывает любые ошибки, возникающие при запросе результатов от расширения.

### Обработчики событий кнопок

- **Обработчик клика на кнопках `context-detail`**:
    - Отправляет сообщение в текущую вкладку, запрашивая фокусировку на элементе контекста.
- **Обработчик клика на кнопках `main-details`**:
    - Отправляет сообщение в текущую вкладку, запрашивая фокусировку на элементе результатов.


## Вспомогательные переменные и функции

- `tx`, `fu`:  Псевдонимы для `tryxpath` и функций `tryxpath`.
- `detailKeys`, `headerValues`: Массивы ключей и заголовков для таблиц результатов.
- `relatedTabId`, `relatedFrameId`, `executionId`: Переменные для хранения идентификаторов вкладки и фрейма, а также идентификатора выполнения, используемые для взаимодействия с расширением.
- `updateDetailsTable`: Функция из `tryxpath.functions`, которая обновляет таблицу деталей.
- `makeDetailText`: Функция из `tryxpath.functions`, которая генерирует строку для отображения деталей.

## Замечания

- Функции `makeInfoText` и `makeConvertedInfoText` генерируют текстовые строки с информацией о результатах для скачивания.
- Модуль использует `browser.runtime.sendMessage` для коммуникации с расширением.
- Модуль использует `browser.tabs.sendMessage` для взаимодействия с вкладами.