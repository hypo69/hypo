# Модуль openai_utils

## Обзор

Этот модуль предоставляет инструменты для взаимодействия с API OpenAI, включая отправку сообщений, получение встраиваний и управление кэшем вызовов API. Он поддерживает как стандартный OpenAI API, так и Azure OpenAI Service. Модуль использует конфигурацию из файла `config.ini` для настройки параметров вызовов API и кэширования.


## Классы

### `LLMCall`

**Описание**: Класс, представляющий вызов модели LLM. Содержит входные сообщения, конфигурацию модели и выходные данные модели.

**Методы**:

- `__init__(self, system_template_name: str, user_template_name: str = None, **model_params)`:
    **Описание**: Инициализирует экземпляр `LLMCall` с указанными системными и пользовательскими шаблонами.
    **Параметры**:
        - `system_template_name` (str): Название системного шаблона.
        - `user_template_name` (str, необязательно): Название пользовательского шаблона. По умолчанию `None`.
        - `**model_params` (dict): Дополнительные параметры модели.
- `call(self, **rendering_configs)`:
    **Описание**: Вызывает модель LLM с указанными конфигурациями рендеринга.
    **Параметры**:
        - `**rendering_configs` (dict): Дополнительные параметры рендеринга.
    **Возвращает**:
        - `str | None`: Содержимое ответа модели или `None`, если произошла ошибка.


### `OpenAIClient`

**Описание**: Утилитарный класс для взаимодействия с API OpenAI.

**Методы**:

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`:
    **Описание**: Инициализирует экземпляр `OpenAIClient`.
    **Параметры**:
        - `cache_api_calls` (bool, необязательно): Флаг кэширования вызовов API. По умолчанию из `default`.
        - `cache_file_name` (str, необязательно): Имя файла для кэширования вызовов API. По умолчанию из `default`.
- `set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"])`:
    **Описание**: Включает или выключает кэширование вызовов API.
    **Параметры**:
        - `cache_file_name` (str): Имя файла для кэширования вызовов API.
- `_setup_from_config(self)`:
    **Описание**: Настраивает конфигурацию API OpenAI для данного клиента.
- `send_message(self, current_messages, ...)`:
    **Описание**: Отправляет сообщение в API OpenAI.
    **Параметры**:
        (много параметров - см. исходный код)
    **Возвращает**:
        - `dict | None`: Словарь с результатом работы API или `None` при ошибке.
    **Вызывает исключения**:
        - `InvalidRequestError`: Недопустимый запрос.
        - `RateLimitError`: Превышен лимит запросов.
        - `NonTerminalError`: Непредвиденная ошибка, но попытка повтора возможна.


### `AzureClient`

**Описание**: Подкласс `OpenAIClient` для работы с Azure OpenAI Service.

**Методы**:

- `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`:
    **Описание**: Инициализирует экземпляр `AzureClient`.
- `_setup_from_config(self)`:
    **Описание**: Настраивает конфигурацию API Azure OpenAI для данного клиента.
- `_raw_model_call(self, model, chat_api_params)`:
    **Описание**: Выполняет вызов модели в Azure OpenAI Service.


## Функции

### `register_client(api_type, client)`

**Описание**: Регистрирует клиента для заданного типа API.

**Параметры**:
    - `api_type` (str): Тип API.
    - `client`: Клиент для регистрации.

### `_get_client_for_api_type(api_type)`

**Описание**: Возвращает клиента для заданного типа API.

**Параметры**:
    - `api_type` (str): Тип API.

**Возвращает**:
    - `client`: Клиент.

### `client()`

**Описание**: Возвращает клиента для настроенного типа API.


### `force_api_type(api_type)`

**Описание**: Принудительно устанавливает тип API.

**Параметры**:
    - `api_type` (str): Тип API.

### `force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"])`

**Описание**: Принудительно устанавливает конфигурацию кэширования API.

**Параметры**:
    - `cache_api_calls` (bool): Флаг кэширования API.
    - `cache_file_name` (str, необязательно): Имя файла кэша.

### `force_default_value(key, value)`

**Описание**: Принудительно устанавливает значение по умолчанию для ключа.

**Параметры**:
    - `key` (str): Ключ.
    - `value`: Значение.


## Исключения

### `InvalidRequestError`

**Описание**: Исключение, возникающее при недопустимом запросе к API OpenAI.

### `NonTerminalError`

**Описание**: Исключение, возникающее при непредвиденной ошибке, но позволяющей повторить попытку.


##  Конфигурация

Модуль использует файл `config.ini` для получения параметров конфигурации.  Необходимо настроить переменные окружения `OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_KEY` если используете Azure.
```