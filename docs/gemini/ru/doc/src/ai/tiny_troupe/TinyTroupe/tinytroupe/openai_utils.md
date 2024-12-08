# Модуль openai_utils

## Обзор

Данный модуль предоставляет инструменты для взаимодействия с API OpenAI, включая настройку, кэширование и обработку вызовов моделей. Модуль поддерживает как стандартный OpenAI API, так и Azure OpenAI Service API.  Он обеспечивает гибкость в настройке параметров вызовов, обработку ошибок и кэширование результатов API-запросов.

## Оглавление

- [Модуль openai_utils](#модуль-openai_utils)
- [Обзор](#обзор)
- [Класс `LLMCall`](#класс-llmcall)
- [Класс `OpenAIClient`](#класс-openaiclient)
- [Класс `AzureClient`](#класс-azureclient)
- [Функции](#функции)
    - [`client()`](#client)
    - [`register_client()`](#register_client)
    - [`_get_client_for_api_type()`](#_get_client_for_api_type)
    - [`force_api_type()`](#force_api_type)
    - [`force_api_cache()`](#force_api_cache)
    - [`force_default_value()`](#force_default_value)
- [Исключения](#исключения)
    - [`InvalidRequestError`](#invalidrequesterror)
    - [`NonTerminalError`](#nonterminalerror)


## Класс `LLMCall`

**Описание**: Класс для представления вызова модели LLM. Содержит сообщения, конфигурацию модели и результат вызова.

**Методы**:

- `__init__(self, system_template_name: str, user_template_name: str = None, **model_params)`: Инициализирует экземпляр `LLMCall` с указанными системами и пользовательскими шаблонами.
    - `system_template_name` (str): Имя шаблона для системы.
    - `user_template_name` (str, optional): Имя шаблона для пользователя. По умолчанию `None`.
    - `**model_params`: Дополнительные параметры для модели.
- `call(self, **rendering_configs)`: Вызывает модель LLM с указанными конфигурациями отрисовки.
    - `**rendering_configs`: Дополнительные параметры для отрисовки.
    - Возвращает (str | None): Содержимое ответа модели или `None` в случае ошибки.

## Класс `OpenAIClient`

**Описание**: Утилитарный класс для взаимодействия с API OpenAI.

**Методы**:

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Инициализирует экземпляр `OpenAIClient`.
    - `cache_api_calls` (bool, optional): Флаг кэширования вызовов API. По умолчанию значение из `default`.
    - `cache_file_name` (str, optional): Имя файла кэша. По умолчанию значение из `default`.
- `set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"])`: Включает/выключает кэширование API-вызовов.
    - `cache_api_calls` (bool): Флаг кэширования.
    - `cache_file_name` (str): Имя файла для кэширования.
- `_setup_from_config(self)`: Настраивает параметры OpenAI API для данного клиента.
- `send_message(self, current_messages, ...)`: Отправляет сообщение в API OpenAI.
    - См. подробное описание в документации функции.

... (остальная документация, аналогично приведенным примерам, для остальных классов и функций, включая подробные описания параметров, возвращаемых значений и исключений)