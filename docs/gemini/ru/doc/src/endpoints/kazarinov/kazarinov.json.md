# Документация файла `kazarinov.json`

## Обзор

Файл `kazarinov.json` содержит конфигурационные параметры для работы системы, включая настройки веб-драйвера, пути к файлам, URL-адреса поставщиков, параметры генерации ответов, настройки телеграм-бота, а также настройки хранения данных.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [`mode`](#mode)
    - [`webdriver_name`](#webdriver_name)
    - [`webdriver_options`](#webdriver_options)
    - [`system_instruction`](#system_instruction)
    - [`questions_list_path`](#questions_list_path)
    - [`url_handlers`](#url_handlers)
        - [`suppliers`](#suppliers)
        - [`onetab`](#onetab)
    - [`generation_config`](#generation_config)
        - [`response_mime_type`](#response_mime_type)
    - [`telegram`](#telegram)
        - [`bot_name`](#bot_name)
        - [`log_path`](#log_path)
    - [`storage`](#storage)
    - [`avaiable_storages`](#avaiable_storages)

## Структура файла

### `mode`

**Описание**: Режим работы системы.
**Тип**: `str`
**Возможные значения**: `"test"`, `"production"`.
В данном случае: `"test"`

### `webdriver_name`

**Описание**: Имя используемого веб-драйвера.
**Тип**: `str`
**Возможные значения**: `"chrome"`, `"firefox"`, `"safari"`, `"edge"`.
В данном случае: `"firefox"`

### `webdriver_options`

**Описание**: Список дополнительных опций для веб-драйвера.
**Тип**: `list`
**Пример**: `["--headless", "--disable-gpu"]`.
В данном случае: `[]` (пустой список)

### `system_instruction`

**Описание**: Путь к файлу, содержащему системные инструкции.
**Тип**: `str`
**Пример**: `"system_instruction.txt"`

### `questions_list_path`

**Описание**: Путь к директории, содержащей файлы со списком вопросов.
**Тип**: `str`
**Пример**: `"kazarinov/prompts/train_data/q"`

### `url_handlers`

**Описание**: Объект, содержащий URL-адреса для различных целей.
**Тип**: `dict`
#### `suppliers`

**Описание**: Список URL-адресов поставщиков.
**Тип**: `list`
**Пример**: `["https://morlevi.co.il", "https://www.ksp.co.il"]`

#### `onetab`

**Описание**: Список URL-адресов для OneTab.
**Тип**: `list`
**Пример**: `["https://www.one-tab.com"]`

### `generation_config`

**Описание**: Объект, содержащий настройки генерации ответов.
**Тип**: `dict`
#### `response_mime_type`

**Описание**: MIME-тип ответа.
**Тип**: `str`
**Возможные значения**: `"text/plain"`, `"application/json"`.
В данном случае: `"text/plain"`

### `telegram`

**Описание**: Объект, содержащий настройки телеграм-бота.
**Тип**: `dict`

#### `bot_name`

**Описание**: Имя телеграм-бота.
**Тип**: `str`
**Пример**: `"hypo69_kazarinov_bot"`

#### `log_path`

**Описание**: Шаблон пути для сохранения логов бота.
**Тип**: `str`
**Пример**: `"bot_logs/<user_id>/<timestamp>.txt"`

### `storage`

**Описание**: Указание на текущий тип хранилища.
**Тип**: `str`
**Возможные значения**: `"data"`, `"google_drive"`, `"external_storage"`.
В данном случае: `"external_storage"`

### `avaiable_storages`

**Описание**: Список доступных типов хранилищ.
**Тип**: `list`
**Пример**: `["data", "google_drive", "external_storage"]`