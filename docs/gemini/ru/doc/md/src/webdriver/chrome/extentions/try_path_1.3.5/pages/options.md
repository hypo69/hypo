# Модуль options.js

## Обзор

Этот файл JavaScript содержит код для страницы настроек расширения. Он позволяет пользователю изменять атрибуты и стили, используемые расширением для выделения элементов на странице.  Файл обрабатывает пользовательский ввод, сохраняет настройки в хранилище браузера и позволяет загрузить значения по умолчанию.


## Оглавление

* [Модуль options.js](#модуль-optionsjs)
    * [Обзор](#обзор)
    * [Функции](#функции)
        * [`isValidAttrName`](#isvalidattrname)
        * [`isValidAttrNames`](#isvalidattrnames)
        * [`isValidStyleLength`](#isvalidstylelength)
        * [`loadDefaultCss`](#loaddfaultcss)
        * [`extractBodyStyles`](#extractbodystyles)
        * [`createPopupCss`](#createpopupcss)


## Функции

### `isValidAttrName`

**Описание**: Проверяет, является ли заданное имя атрибута допустимым.

**Параметры**:

- `name` (строка): Имя атрибута.

**Возвращает**:

- `boolean`: `true`, если имя атрибута допустимо, `false` в противном случае.

**Обрабатываемые исключения**:
- `ex` (любое): Если возникает ошибка при проверке, функция возвращает `false`.


### `isValidAttrNames`

**Описание**: Проверяет, являются ли все имена атрибутов в массиве допустимыми.

**Параметры**:

- `names` (объект): Объект, содержащий имена атрибутов.

**Возвращает**:

- `boolean`: `true`, если все имена атрибутов допустимы, `false` в противном случае.

**Обрабатываемые исключения**:
- `ex` (любое): Возникает при возникновении ошибки во время проверки имен атрибутов.


### `isValidStyleLength`

**Описание**: Проверяет, является ли заданная длина стилей допустимой.

**Параметры**:

- `len` (строка): Длина стилей.

**Возвращает**:

- `boolean`: `true`, если длина стилей допустима, `false` в противном случае.


### `loadDefaultCss`

**Описание**: Загружает CSS файл по умолчанию.

**Возвращает**:

- `Promise<string>`: Обещание, которое разрешается текстом загруженного CSS файла.

**Обрабатываемые исключения**:
- `ex` (любое): Если возникает ошибка при загрузке файла, промис отклоняется.


### `extractBodyStyles`

**Описание**: Извлекает ширину и высоту тела попапа из CSS.

**Параметры**:

- `css` (строка): Строка CSS.

**Возвращает**:

- `object`: Объект, содержащий ширину и высоту тела попапа.

**Обрабатываемые исключения**:
- `ex` (любое): Не обрабатываются исключения в этой функции.


### `createPopupCss`

**Описание**: Создает CSS для тела попапа.

**Параметры**:

- `bodyStyles` (объект): Объект, содержащий ширину и высоту тела попапа.

**Возвращает**:

- `string`: Строка CSS для тела попапа.

**Обрабатываемые исключения**:
- `ex` (любое): Не обрабатываются исключения в этой функции.