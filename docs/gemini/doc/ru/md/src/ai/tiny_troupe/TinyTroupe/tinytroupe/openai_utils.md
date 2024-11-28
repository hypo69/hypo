# Модуль openai_utils

## Обзор

Этот модуль предоставляет инструменты для взаимодействия с API OpenAI, включая настройку, отправку запросов и обработку ответов. Он поддерживает кэширование API-вызовов для повышения производительности.  Модуль также содержит классы для работы с различными типами API, включая OpenAI и Azure OpenAI.

## Оглавление

* [Модуль openai_utils](#модуль-openai_utils)
* [Функции](#функции)
    * [`default`](#default)
    * [`LLMCall`](#llmcall)
        * [`__init__`](#init)
        * [`call`](#call)
        * [`__repr__`](#repr)
    * [`OpenAIClient`](#openaiclient)
        * [`__init__`](#init-1)
        * [`set_api_cache`](#set_api_cache)
        * [`_setup_from_config`](#_setup_from_config)
        * [`send_message`](#send_message)
            * [`aux_exponential_backoff`](#aux_exponential_backoff)
            * [`_raw_model_call`](#_raw_model_call)
            * [`_raw_model_response_extractor`](#_raw_model_response_extractor)
            * [`_count_tokens`](#_count_tokens)
        * [`_save_cache`](#_save_cache)
        * [`_load_cache`](#_load_cache)
        * [`get_embedding`](#get_embedding)
            * [`_raw_embedding_model_call`](#_raw_embedding_model_call)
            * [`_raw_embedding_model_response_extractor`](#_raw_embedding_model_response_extractor)
    * [`AzureClient`](#azureclient)
        * [`__init__`](#init-2)
        * [`_setup_from_config`](#_setup_from_config-1)
        * [`_raw_model_call`](#_raw_model_call-1)
    * [`InvalidRequestError`](#invalidrequesterror)
    * [`NonTerminalError`](#nonterminalerror)
* [Регистрация и получение клиента](#регистрация-и-получение-клиента)
    * [`register_client`](#register_client)
    * [`_get_client_for_api_type`](#_get_client_for_api_type)
    * [`client`](#client)
* [Управление настройками API](#управление-настройками-api)
    * [`force_api_type`](#force_api_type)
    * [`force_api_cache`](#force_api_cache)
    * [`force_default_value`](#force_default_value)


## Функции

### `default`

Словарь, содержащий значения по умолчанию для параметров модели.

### `LLMCall`

Класс для представления вызова модели LLM.  Содержит входные сообщения, настройки модели и вывод модели.

#### `__init__`

**Описание**: Инициализирует экземпляр `LLMCall` с заданными системным и пользовательским шаблонами.

**Параметры**:
- `system_template_name` (str): Имя шаблона для системного сообщения.
- `user_template_name` (Optional[str], optional): Имя шаблона для пользовательского сообщения. По умолчанию `None`.
- `**model_params`:  Ключевые параметры, связанные с моделью.

#### `call`

**Описание**: Вызывает модель LLM с заданными конфигурациями рендеринга.

**Параметры**:
- `**rendering_configs`: Ключевые параметры, связанные с рендерингом.


**Возвращает**:
- `str | None`: Возвращает содержимое ответа модели или `None`, если в ответе отсутствует ключ 'content'.


#### `__repr__`

**Описание**: Возвращает строковое представление объекта.


### `OpenAIClient`

Класс для взаимодействия с API OpenAI.

#### `__init__`

**Описание**: Инициализирует экземпляр `OpenAIClient`.

**Параметры**:
- `cache_api_calls` (bool, optional): Флаг кэширования API-вызовов. По умолчанию - значение из `default`.
- `cache_file_name` (str, optional): Имя файла для кэша API-вызовов. По умолчанию - значение из `default`.

#### `set_api_cache`

**Описание**: Включает или отключает кэширование API-вызовов.

**Параметры**:
- `cache_api_calls` (bool): Флаг кэширования.
- `cache_file_name` (str, optional): Имя файла для кэша. По умолчанию - значение из `default`.


#### `_setup_from_config`

**Описание**: Настраивает конфигурацию OpenAI API для этого клиента.

#### `send_message`

**Описание**: Отправляет сообщение в API OpenAI и возвращает ответ.

**Параметры**:
- `current_messages`: Список словарей, представляющих историю диалога.
- `model` (str, optional): Идентификатор модели. По умолчанию - значение из `default`.
- ... (много параметров):  Параметры, связанные с моделью. Смотрите документацию к функции для полного списка.


**Возвращает**:
- `dict | None`: Возвращает словарь с результатом запроса или `None` в случае ошибки.


#### `_raw_model_call`, `_raw_model_response_extractor`, `_count_tokens`, `_save_cache`, `_load_cache`, `get_embedding`, `_raw_embedding_model_call`, `_raw_embedding_model_response_extractor`:

Подробные описания этих методов (методы для низкоуровневого взаимодействия с API и обработки) вы можете найти в самом коде.


### `AzureClient`

Класс для взаимодействия с Azure OpenAI Service API.  Наследуется от `OpenAIClient`.

### `InvalidRequestError`, `NonTerminalError`

Классы для обработки специфических исключений, связанных с API-запросами.


## Регистрация и получение клиента

### `register_client`, `_get_client_for_api_type`, `client`

Функции для регистрации и получения клиентов API.


## Управление настройками API

### `force_api_type`, `force_api_cache`, `force_default_value`

Функции для принудительного изменения параметров API.