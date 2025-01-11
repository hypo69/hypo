# Описание манифеста расширения Try xpath

## Обзор

Этот документ описывает структуру и содержание файла `manifest.json` для расширения Firefox "Try xpath", предназначенного для отображения результатов оценки выражений xpath или CSS-селекторов.

## Оглавление

1.  [Обзор](#обзор)
2.  [Основные поля](#основные-поля)
3.  [Раздел applications](#раздел-applications)
4.  [Раздел permissions](#раздел-permissions)
5.  [Раздел background](#раздел-background)
6.  [Раздел browser_action](#раздел-browser_action)
7.  [Раздел web_accessible_resources](#раздел-web_accessible_resources)
8.  [Раздел content_scripts](#раздел-content_scripts)
9.  [Раздел options_ui](#раздел-options_ui)

## Основные поля

*   `name`: "Try xpath" - Название расширения.
*   `description`: "This add-on displays the result of evaluating xpath expression or CSS selector." - Описание расширения.
*   `manifest_version`: 2 - Версия манифеста.
*   `version`: "1.3.5" - Версия расширения.
*   `icons`:
    *   `48`: "icons/icon_48.png" - Иконка расширения размером 48x48 пикселей.

## Раздел applications

### `applications`

**Описание**: Настройки для конкретных приложений, в данном случае Firefox.
   * `gecko`:
        * `id`: "{ba6bb880-bcbe-4792-a020-fcfab8d67027}" - Уникальный идентификатор расширения.
        *  `strict_min_version`: "53.0" - Минимальная версия Firefox, поддерживающая расширение.
       
## Раздел permissions

### `permissions`

**Описание**: Список разрешений, необходимых расширению.
*   `<all_urls>`: Разрешение на доступ ко всем URL.
*   `storage`: Разрешение на использование локального хранилища.

## Раздел background

### `background`

**Описание**: Настройки для фоновых скриптов.
    *   `scripts`:
         *   `scripts/try_xpath_functions.js` - Файл со вспомогательными функциями.
         *    `background/try_xpath_background.js` - Основной фоновый скрипт расширения.

## Раздел browser_action

### `browser_action`

**Описание**: Настройки для кнопки расширения в панели инструментов браузера.
    *   `default_icon`: "icons/icon_48.png" - Иконка кнопки.
    *   `default_title`: "Try xpath" - Заголовок кнопки.
    *   `default_popup`: "popup/popup.html" - HTML-файл всплывающего окна.

## Раздел web_accessible_resources

### `web_accessible_resources`

**Описание**: Список ресурсов, доступных веб-страницам. В данном случае список пуст.

## Раздел content_scripts

### `content_scripts`

**Описание**: Список скриптов, которые будут выполняться на веб-страницах. В данном случае список пуст.

## Раздел options_ui

### `options_ui`

**Описание**: Настройки для страницы опций расширения.
    *   `page`: "/pages/options.html" - HTML-файл страницы опций.