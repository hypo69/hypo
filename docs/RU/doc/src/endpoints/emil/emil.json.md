# Конфигурационный файл `emil.json`

## Обзор

Файл `emil.json` содержит настройки для работы приложения, включая режим работы, параметры веб-драйвера, обработчики URL-адресов, настройки генерации ответов, параметры телеграм-бота и настройки хранилища.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [mode](#mode)
    - [webdriver_name](#webdriver_name)
    - [webdriver_options](#webdriver_options)
    - [url_handlers](#url_handlers)
    - [generation_config](#generation_config)
    - [telegram](#telegram)
    - [storage](#storage)
    - [avaiable_storages](#avaiable_storages)

## Структура файла

### `mode`

**Описание**: Режим работы приложения.

**Тип**: `string`

**Значение**: `"test"`

### `webdriver_name`

**Описание**: Название используемого веб-драйвера.

**Тип**: `string`

**Значение**: `"firefox"`

### `webdriver_options`

**Описание**: Список дополнительных опций для веб-драйвера.

**Тип**: `list`

**Значение**: `[]` (пустой список)

### `url_handlers`

**Описание**: Настройки обработчиков URL-адресов.

**Тип**: `dict`

#### `url_handlers.suppliers`

**Описание**: Список URL-адресов поставщиков.

**Тип**: `list`

**Значение**: 
```
[
  "https://morlevi.co.il",
  "https://www.morlevi.co.il",
  "https://grandadvance.co.il",
  "https://www.grandadvance.co.il",
  "https://ksp.co.il",
  "https://www.ksp.co.il",
  "https://ivory.co.il",
  "https://www.ivory.co.il"
]
```

#### `url_handlers.onetab`

**Описание**: Список URL-адресов для OneTab.

**Тип**: `list`

**Значение**: `["https://www.one-tab.com"]`

### `generation_config`

**Описание**: Настройки генерации ответов.

**Тип**: `dict`

#### `generation_config.response_mime_type`

**Описание**: MIME-тип ответа.

**Тип**: `string`

**Значение**: `"text/plain"`

### `telegram`

**Описание**: Настройки телеграм-бота.

**Тип**: `dict`

#### `telegram.bot_name`

**Описание**: Имя телеграм-бота.

**Тип**: `string`

**Значение**: `"hypo69_kazarinov_bot"`

#### `telegram.log_path`

**Описание**: Путь к файлу логов телеграм-бота, содержащий плейсхолдеры для `user_id` и `timestamp`.

**Тип**: `string`

**Значение**: `"bot_logs/<user_id>/<timestamp>.txt"`

### `storage`

**Описание**: Название используемого хранилища.

**Тип**: `string`

**Значение**: `"external_storage"`

### `avaiable_storages`

**Описание**: Список доступных хранилищ.

**Тип**: `list`

**Значение**: `["data", "google_drive", "external_storage"]`