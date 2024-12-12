# Конфигурационный файл `kazarinov.json`

## Обзор

Этот файл содержит конфигурационные настройки для проекта, включая режимы работы, настройки веб-драйвера, пути к файлам, обработчики URL, конфигурацию генерации, параметры Telegram-бота и настройки хранилища.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Параметры конфигурации](#параметры-конфигурации)
    - [mode](#mode)
    - [webdriver_name](#webdriver_name)
    - [webdriver_options](#webdriver_options)
    - [system_instruction](#system_instruction)
    - [questions_list_path](#questions_list_path)
    - [url_handlers](#url_handlers)
        - [suppliers](#suppliers)
        - [onetab](#onetab)
    - [generation_config](#generation_config)
        - [response_mime_type](#response_mime_type)
    - [telegram](#telegram)
        - [bot_name](#bot_name)
        - [log_path](#log_path)
    - [storage](#storage)
    - [avaiable_storages](#avaiable_storages)
4. [Пример использования](#пример-использования)

## Структура JSON

JSON-файл содержит объект с набором ключей и их соответствующих значений.

## Параметры конфигурации

### `mode`
**Описание**: Режим работы приложения.
**Тип**: `str`
**Значение**: `"test"`

### `webdriver_name`
**Описание**: Название используемого веб-драйвера.
**Тип**: `str`
**Значение**: `"firefox"`

### `webdriver_options`
**Описание**: Список дополнительных опций для веб-драйвера.
**Тип**: `list`
**Значение**: `[]` (пустой список)

### `system_instruction`
**Описание**: Путь к файлу с системными инструкциями.
**Тип**: `str`
**Значение**: `"system_instruction.txt"`

### `questions_list_path`
**Описание**: Путь к директории со списком вопросов.
**Тип**: `str`
**Значение**: `"kazarinov/prompts/train_data/q"`

### `url_handlers`
**Описание**: Объект, содержащий обработчики URL.
**Тип**: `dict`

#### `suppliers`
**Описание**: Список URL поставщиков.
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

#### `onetab`
**Описание**: Список URL для OneTab.
**Тип**: `list`
**Значение**: 
```
[
    "https://www.one-tab.com"
]
```

### `generation_config`
**Описание**: Объект, содержащий конфигурацию генерации ответов.
**Тип**: `dict`

#### `response_mime_type`
**Описание**: MIME-тип генерируемого ответа.
**Тип**: `str`
**Значение**: `"text/plain"`

### `telegram`
**Описание**: Объект, содержащий настройки Telegram-бота.
**Тип**: `dict`

#### `bot_name`
**Описание**: Имя Telegram-бота.
**Тип**: `str`
**Значение**: `"hypo69_kazarinov_bot"`

#### `log_path`
**Описание**: Шаблон пути для сохранения логов бота.
**Тип**: `str`
**Значение**: `"bot_logs/<user_id>/<timestamp>.txt"`

### `storage`
**Описание**: Тип используемого хранилища данных.
**Тип**: `str`
**Значение**: `"external_storage"`

### `avaiable_storages`
**Описание**: Список доступных типов хранилищ данных.
**Тип**: `list`
**Значение**: `["data", "google_drive", "external_storage"]`

## Пример использования

Этот файл используется для конфигурации различных компонентов приложения. Например, `webdriver_name` и `webdriver_options` определяют, какой браузер и с какими параметрами будет использоваться для автоматизации веб-страниц. `url_handlers` указывает, какие URL-адреса следует обрабатывать. Раздел `telegram` содержит настройки для взаимодействия с Telegram-ботом, включая имя бота и путь для сохранения логов.