# Модуль options.js

## Обзор

Этот модуль JavaScript отвечает за обработку взаимодействия с пользовательским интерфейсом (UI) плагина. Он позволяет пользователю настраивать атрибуты и CSS, используемые плагином для поиска элементов на веб-странице.  Модуль взаимодействует с хранилищем браузера для сохранения настроек и с функциями плагина для их применения.


## Функции

### `isValidAttrName`

**Описание**: Проверяет, является ли переданное имя атрибута допустимым для установки.

**Параметры**:
- `name` (str): Имя атрибута.

**Возвращает**:
- `bool`: `true`, если имя атрибута является допустимым, `false` в противном случае.

**Вызывает исключения**:
- `ex` (любое): Любые исключения, возникшие при попытке установить атрибут.


### `isValidAttrNames`

**Описание**: Проверяет, являются ли все имена атрибутов в массиве допустимыми.

**Параметры**:
- `names` (array): Массив имён атрибутов.

**Возвращает**:
- `bool`: `true`, если все имена атрибутов допустимы, `false` в противном случае.

**Вызывает исключения**:
- `ex` (любое): Любые исключения, возникшие при проверке отдельных атрибутов.


### `isValidStyleLength`

**Описание**: Проверяет, соответствует ли переданная строка формату длины CSS-стиля.

**Параметры**:
- `len` (str): Строка, представляющая длину.

**Возвращает**:
- `bool`: `true`, если строка соответствует формату, `false` в противном случае.


### `loadDefaultCss`

**Описание**: Загружает CSS-стили по умолчанию из файла `try_xpath_insert.css`.

**Возвращает**:
- `Promise<string>`: Promise, содержащий текст загруженного CSS. В случае успеха содержит текст CSS, в случае ошибки — отклоняет Promise с ошибкой.

**Вызывает исключения**:
- `ex` (любое): Любые исключения, возникшие при загрузке CSS.


### `extractBodyStyles`

**Описание**: Извлекает значения ширины и высоты из строки CSS.

**Параметры**:
- `css` (str): Строка CSS.

**Возвращает**:
- `object`: Объект, содержащий значения ширины (`width`) и высоты (`height`).


### `createPopupCss`

**Описание**: Формирует строку CSS для стилей тела всплывающего окна.

**Параметры**:
- `bodyStyles` (object): Объект со значениями для ширины и высоты.

**Возвращает**:
- `string`: Строка CSS для стилей тела всплывающего окна.



### <ins>Другое</ins>

Этот модуль содержит также переменные, представляющие элементы DOM и функции для взаимодействия с хранилищем браузера. Ключевым аспектом является настройка атрибутов и стилей плагина, загрузка стилей по умолчанию и сохранение пользовательских настроек.


## Обработка событий

### `window.addEventListener("load", ...)`

**Описание**: Обработчик события `load` для окна браузера.  Инициализирует элементы управления, запрашивает настройки из браузера и обрабатывает событие сохранения.



### `document.getElementById("save").addEventListener("click", ...)`

**Описание**: Обработчик события клика по кнопке "Сохранить".  Обрабатывает входные данные, валидирует атрибуты и стили, сохраняет настройки в хранилище браузера и отображает сообщения об успехе или ошибке.


### `document.getElementById("show-default").addEventListener("click", ...)`

**Описание**: Обработчик события клика по кнопке "Восстановить по умолчанию". Устанавливает значения атрибутов и стилей по умолчанию, загружая CSS-стили по умолчанию.