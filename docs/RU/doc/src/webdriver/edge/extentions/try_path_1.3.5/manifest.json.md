# Документация для `manifest.json`

## Обзор

Файл `manifest.json` является файлом манифеста расширения для браузера Edge. Он содержит метаданные и настройки, необходимые для установки и работы расширения "Try xpath". Расширение предназначено для отображения результатов вычисления выражений XPath или CSS-селекторов на веб-странице.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [`name`](#name)
    - [`description`](#description)
    - [`manifest_version`](#manifest_version)
    - [`version`](#version)
    - [`icons`](#icons)
    - [`applications`](#applications)
        - [`gecko`](#gecko)
            - [`id`](#id)
            - [`strict_min_version`](#strict_min_version)
    - [`permissions`](#permissions)
    - [`background`](#background)
        - [`scripts`](#scripts)
    - [`browser_action`](#browser_action)
        - [`default_icon`](#default_icon)
        - [`default_title`](#default_title)
        - [`default_popup`](#default_popup)
    - [`web_accessible_resources`](#web_accessible_resources)
    - [`content_scripts`](#content_scripts)
    - [`options_ui`](#options_ui)
        - [`page`](#page)

## Структура файла

### `name`
**Описание**: Имя расширения, отображаемое в браузере. В данном случае - "Try xpath".

### `description`
**Описание**: Краткое описание функциональности расширения. В данном случае - "This add-on displays the result of evaluating xpath expression or CSS selector."

### `manifest_version`
**Описание**: Версия формата манифеста, используемая расширением. В данном случае - `2`.

### `version`
**Описание**: Версия расширения. В данном случае - `1.3.5`.

### `icons`
**Описание**: Набор иконок расширения, используемых в браузере.
  -  `48` (string): Путь к иконке 48x48 пикселей, `"icons/icon_48.png"`.

### `applications`
**Описание**: Специфичные настройки для конкретных браузеров.
    - `gecko` (object): Настройки для браузеров, основанных на движке Gecko (например, Firefox).
        - `id` (string): Уникальный идентификатор расширения для Firefox, `"\{ba6bb880-bcbe-4792-a020-fcfab8d67027\}"`.
        - `strict_min_version` (string): Минимальная версия браузера, совместимая с расширением, `"53.0"`.

### `permissions`
**Описание**: Список разрешений, необходимых для работы расширения.
  -  `<all_urls>` (string): Разрешение на доступ ко всем URL.
   - `storage` (string): Разрешение на использование API `storage`.

### `background`
**Описание**: Настройки для фоновых скриптов расширения.
    - `scripts` (array): Массив путей к JavaScript-файлам, которые будут выполняться в фоне.
        - `scripts[0]` (string): `"scripts/try_xpath_functions.js"` - файл с общими функциями.
        - `scripts[1]` (string): `"background/try_xpath_background.js"` - основной фоновый скрипт.

### `browser_action`
**Описание**: Настройки для кнопки расширения на панели инструментов браузера.
    - `default_icon` (string): Путь к иконке кнопки, `"icons/icon_48.png"`.
    - `default_title` (string): Текст подсказки для кнопки, `"Try xpath"`.
    - `default_popup` (string): Путь к HTML-файлу всплывающего окна, `"popup/popup.html"`.

### `web_accessible_resources`
**Описание**: Список ресурсов, доступных веб-страницам. В данном случае, список пуст.

### `content_scripts`
**Описание**: Список скриптов, внедряемых на веб-страницы. В данном случае, список пуст.

### `options_ui`
**Описание**: Настройки страницы параметров расширения.
    - `page` (string): Путь к HTML-файлу страницы параметров, `"/pages/options.html"`.