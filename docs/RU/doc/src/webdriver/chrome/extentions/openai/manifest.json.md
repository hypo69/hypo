# Описание манифеста расширения Chrome "OpenAI Model Interface"

## Обзор

Этот файл `manifest.json` описывает метаданные расширения Chrome "OpenAI Model Interface", которое предназначено для взаимодействия с моделями OpenAI. Он определяет имя расширения, версию, описание, необходимые разрешения, фоновый скрипт, всплывающее окно, иконки и политику безопасности контента.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [`manifest_version`](#manifest_version)
    - [`name`](#name)
    - [`version`](#version)
    - [`description`](#description)
    - [`permissions`](#permissions)
    - [`background`](#background)
    - [`action`](#action)
    - [`icons`](#icons)
    - [`content_security_policy`](#content_security_policy)

## Структура JSON

### `manifest_version`
- **Описание**: Версия манифеста. Используется 3.
- **Тип**: `number`

### `name`
- **Описание**: Название расширения.
- **Значение**: `"OpenAI Model Interface"`
- **Тип**: `string`

### `version`
- **Описание**: Версия расширения.
- **Значение**: `"1.0"`
- **Тип**: `string`

### `description`
- **Описание**: Краткое описание расширения.
- **Значение**: `"Interface for interacting with OpenAI model"`
- **Тип**: `string`

### `permissions`
- **Описание**: Массив разрешений, необходимых для работы расширения.
- **Значение**: `["activeTab"]`
- **Тип**: `array`
    - `"activeTab"`: Разрешение на доступ к текущей активной вкладке.

### `background`
- **Описание**: Описание фонового скрипта расширения.
- **Значение**: 
  ```json
  {
    "service_worker": "background.js"
  }
  ```
- **Тип**: `object`
    - `service_worker`: Путь к фоновому скрипту (`"background.js"`).

### `action`
- **Описание**: Описание действия расширения, включая всплывающее окно и иконки.
- **Значение**:
  ```json
    {
      "default_popup": "index.html",
      "default_icon": {
        "16": "icons/16.png",
        "48": "icons/48.png",
        "128": "icons/128.png"
      },
      "default_width": 750,
      "default_height": 600
    }
  ```
- **Тип**: `object`
    - `default_popup`: Путь к HTML-файлу всплывающего окна (`"index.html"`).
    - `default_icon`: Объект с путями к иконкам разных размеров.
        - `"16"`: Иконка 16x16 пикселей.
        - `"48"`: Иконка 48x48 пикселей.
        - `"128"`: Иконка 128x128 пикселей.
    - `default_width`: Ширина всплывающего окна по умолчанию (750 пикселей).
    - `default_height`: Высота всплывающего окна по умолчанию (600 пикселей).

### `icons`
- **Описание**: Объект с путями к иконкам расширения.
- **Значение**:
  ```json
    {
      "16": "icons/16.png",
      "48": "icons/48.png",
      "128": "icons/128.png"
    }
  ```
- **Тип**: `object`
    - `"16"`: Иконка 16x16 пикселей.
    - `"48"`: Иконка 48x48 пикселей.
    - `"128"`: Иконка 128x128 пикселей.

### `content_security_policy`
- **Описание**: Политика безопасности контента для страниц расширения.
- **Значение**:
  ```json
  {
    "extension_pages": "script-src \'self\'; object-src \'self\';"
  }
  ```
- **Тип**: `object`
    - `extension_pages`: Политика для страниц расширения. Разрешает загрузку скриптов и объектов только из самого расширения (`script-src 'self'; object-src 'self';`).