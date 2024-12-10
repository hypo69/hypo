# Модуль tinytroupe.openai_utils

## Обзор

Данный модуль предоставляет инструменты для взаимодействия с API OpenAI, включая настройку, кэширование запросов и обработку ответов. Он поддерживает как стандартный OpenAI API, так и Azure OpenAI Service. Модуль содержит классы для работы с различными типами API, функции для настройки параметров вызовов и кэширования, а также механизм регистрации пользовательских клиентов.

## Оглавление

- [Модуль tinytroupe.openai_utils](#модуль-tinytroupeopenai_utils)
- [Обзор](#обзор)
- [Классы](#классы)
    - [`LLMCall`](#llmcall)
    - [`OpenAIClient`](#openaiclient)
    - [`AzureClient`](#azureclient)
- [Исключения](#исключения)
    - [`InvalidRequestError`](#invalidrequesterror)
    - [`NonTerminalError`](#nonterminalerror)
- [Функции](#функции)
    - [`client()`](#client)
    - [`register_client()`](#register_client)
    - [`_get_client_for_api_type()`](#_get_client_for_api_type)
    - [`force_api_type()`](#force_api_type)
    - [`force_api_cache()`](#force_api_cache)
    - [`force_default_value()`](#force_default_value)
    - [`_count_tokens()`](#_count_tokens)


## Классы

### `LLMCall`

**Описание**: Представляет вызов модели LLM. Содержит входные сообщения, конфигурацию модели и выход модели.

**Методы**:

- `__init__(self, system_template_name: str, user_template_name: str = None, **model_params)`: Инициализирует экземпляр `LLMCall` с указанными шаблонами для системных и пользовательских сообщений.
- `call(self, **rendering_configs)`: Вызывает модель LLM с заданными конфигурациями рендеринга. Возвращает сгенерированный текст или `None` при ошибке.

**Параметры**:

- `system_template_name (str)`: Название шаблона для системного сообщения.
- `user_template_name (str, optional)`: Название шаблона для пользовательского сообщения. По умолчанию `None`.
- `**model_params`: Дополнительные параметры для модели (например, `model`, `max_tokens`).


### `OpenAIClient`

**Описание**: Утилита для взаимодействия с API OpenAI.


**Методы**:

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Инициализирует клиент.
- `set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"])`: Включает или отключает кэширование API-вызовов.
- `_setup_from_config(self)`: Настраивает конфигурацию API OpenAI для этого клиента.
- `send_message(self, current_messages, ...)`: Отправляет сообщение в OpenAI API и возвращает ответ.
- `_raw_model_call(self, model, chat_api_params)`: Делегирует вызов API.
- `_raw_model_response_extractor(self, response)`: Извлекает ответ из API-ответа.
- `_count_tokens(self, messages: list, model: str)`: Подсчитывает количество токенов в сообщениях для данной модели.


**Параметры**:

- `cache_api_calls (bool, optional)`: Кэшировать ли API вызовы. По умолчанию `False`
- `cache_file_name (str, optional)`: Имя файла для кэша API вызовов.
- `current_messages (list)`: Список словарей, представляющих историю разговора.
- `model (str, optional)`: Идентификатор модели для генерации ответа.
- `...`: Дополнительные параметры для вызова модели.


### `AzureClient`

**Описание**: Клиент для взаимодействия с Azure OpenAI Service. Наследует от `OpenAIClient`.

**Методы**:

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Инициализирует клиент.
- `_setup_from_config(self)`: Настраивает конфигурацию API Azure OpenAI Service.
- `_raw_model_call(self, model, chat_api_params)`: Делегирует вызов API.


## Исключения

### `InvalidRequestError`

**Описание**: Исключение, возникающее при некорректном запросе к OpenAI API.

### `NonTerminalError`

**Описание**: Исключение, возникающее при ошибке, которая может быть обработана и после которой можно повторить запрос.

## Функции

### `client()`

**Описание**: Возвращает клиент для API, настроенный согласно конфигурации.

### `register_client(api_type, client)`

**Описание**: Регистрирует клиент для данного типа API.

### `_get_client_for_api_type(api_type)`

**Описание**: Возвращает зарегистрированный клиент для указанного типа API.

### `force_api_type(api_type)`

**Описание**: Принудительно устанавливает тип API.

### `force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"])`

**Описание**: Принудительно устанавливает конфигурацию кэширования API.

### `force_default_value(key, value)`

**Описание**: Принудительно устанавливает значение по умолчанию для указанного параметра.

### `_count_tokens(self, messages: list, model: str)`

**Описание**: Подсчитывает количество токенов OpenAI в списке сообщений с использованием tiktoken.

**Параметры:**
- `messages (list)`: Список словарей, представляющих историю разговора.
- `model (str)`: Название модели для кодирования строки.

**Возвращает:** Количество токенов или `None` при ошибке.

```