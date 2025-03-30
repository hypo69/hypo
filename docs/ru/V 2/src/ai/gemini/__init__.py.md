# Модуль `gemini`

## Обзор

Модуль `gemini` предназначен для работы с моделью Google Gemini. Он содержит класс `GoogleGenerativeAI`, предоставляющий интерфейс для взаимодействия с API Google Generative AI.

## Оглавление

- [Обзор](#обзор)
- [Модули](#модули)
    - [`generative_ai`](#generative_ai)

## Модули

### `generative_ai`

Модуль `generative_ai` содержит класс `GoogleGenerativeAI` для работы с API Google Generative AI.

- [`GoogleGenerativeAI`](#GoogleGenerativeAI)

#### `GoogleGenerativeAI`

**Описание**:
Класс `GoogleGenerativeAI` предоставляет интерфейс для взаимодействия с API Google Generative AI.

**Методы**:

- [`__init__`](#__init__)
- [`generate_content`](#generate_content)
- [`stream_generate_content`](#stream_generate_content)
- [`count_tokens`](#count_tokens)

##### `__init__`

**Описание**:
Инициализирует объект `GoogleGenerativeAI` с заданным API-ключом.

**Параметры**:
- `api_key` (str): API ключ Google Generative AI.

**Возвращает**:
- `None`

##### `generate_content`

**Описание**:
Генерирует контент на основе заданных параметров.

**Параметры**:
- `contents` (list[dict]): Список содержимого для генерации.
- `generation_config` (Optional[dict], optional): Параметры конфигурации генерации. По умолчанию `None`.
- `safety_settings` (Optional[list[dict]], optional): Настройки безопасности. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с результатом генерации или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`:  Возникает при ошибке во время генерации.

##### `stream_generate_content`

**Описание**:
Генерирует контент в потоковом режиме на основе заданных параметров.

**Параметры**:
- `contents` (list[dict]): Список содержимого для генерации.
- `generation_config` (Optional[dict], optional): Параметры конфигурации генерации. По умолчанию `None`.
- `safety_settings` (Optional[list[dict]], optional): Настройки безопасности. По умолчанию `None`.

**Возвращает**:
- `Iterator[dict] | None`: Итератор по результатам генерации или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время генерации.

##### `count_tokens`

**Описание**:
Подсчитывает количество токенов в заданном контенте.

**Параметры**:
- `contents` (list[dict]): Список содержимого для подсчета токенов.

**Возвращает**:
- `int | None`: Количество токенов или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время подсчета токенов.