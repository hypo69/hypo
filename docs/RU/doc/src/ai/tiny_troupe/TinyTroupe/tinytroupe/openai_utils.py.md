# tinytroupe.openai_utils

## Обзор

Модуль `tinytroupe.openai_utils` предоставляет утилиты для взаимодействия с API OpenAI и Azure OpenAI Service. Он включает в себя классы для управления API-клиентами, кэширования запросов, обработки ошибок и подсчета токенов.

## Содержание

- [Константы](#Константы)
- [Классы](#Классы)
  - [`LLMCall`](#LLMCall)
  - [`OpenAIClient`](#OpenAIClient)
  - [`AzureClient`](#AzureClient)
  - [`InvalidRequestError`](#InvalidRequestError)
  - [`NonTerminalError`](#NonTerminalError)
- [Функции](#Функции)
  - [`register_client`](#register_client)
  - [`_get_client_for_api_type`](#_get_client_for_api_type)
  - [`client`](#client)
  - [`force_api_type`](#force_api_type)
  - [`force_api_cache`](#force_api_cache)
  - [`force_default_value`](#force_default_value)

## Константы

В данном модуле определены значения по умолчанию для параметров OpenAI API, которые могут быть переопределены в файле конфигурации `config.ini`.

- `default`: Словарь со значениями по умолчанию для параметров OpenAI API, включая модель, максимальное количество токенов, температуру, вероятность top_p, штрафы за частоту и присутствие, таймаут, максимальное количество попыток, время ожидания, коэффициент экспоненциального отката, модель эмбеддингов, кэширование API-вызовов и имя файла кэша.

## Классы

### `LLMCall`

**Описание**:
Класс, представляющий вызов LLM модели. Содержит входные сообщения, конфигурацию модели и вывод модели.

**Методы**:

#### `__init__`
```python
def __init__(self, system_template_name:str, user_template_name:str=None, **model_params)
```
**Описание**:
Инициализирует экземпляр `LLMCall` с указанными системными и пользовательскими шаблонами.

**Параметры**:
- `system_template_name` (str): Имя системного шаблона.
- `user_template_name` (Optional[str], optional): Имя пользовательского шаблона. По умолчанию `None`.
- `**model_params`: Дополнительные параметры для вызова модели.

#### `call`
```python
def call(self, **rendering_configs) -> str | None
```
**Описание**:
Вызывает LLM модель с указанными конфигурациями рендеринга.

**Параметры**:
- `**rendering_configs`: Конфигурации рендеринга для шаблонов.

**Возвращает**:
- `str | None`: Содержимое ответа модели или `None`, если ответ не содержит ключ 'content'.

#### `__repr__`
```python
def __repr__(self) -> str
```
**Описание**:
Возвращает строковое представление объекта `LLMCall`.

**Возвращает**:
- `str`: Строковое представление объекта `LLMCall`.

### `OpenAIClient`

**Описание**:
Утилитарный класс для взаимодействия с API OpenAI.

**Методы**:

#### `__init__`
```python
def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None
```
**Описание**:
Инициализирует экземпляр `OpenAIClient`.

**Параметры**:
- `cache_api_calls` (bool, optional): Следует ли кэшировать вызовы API. По умолчанию берется из `default["cache_api_calls"]`.
- `cache_file_name` (str, optional): Имя файла для кэширования API-вызовов. По умолчанию берется из `default["cache_file_name"]`.

#### `set_api_cache`
```python
def set_api_cache(self, cache_api_calls: bool, cache_file_name: str = default["cache_file_name"]) -> None
```
**Описание**:
Включает или отключает кэширование вызовов API.

**Параметры**:
- `cache_api_calls` (bool): Определяет, следует ли кэшировать API-вызовы.
- `cache_file_name` (str, optional): Имя файла для кэширования API-вызовов. По умолчанию берется из `default["cache_file_name"]`.

#### `_setup_from_config`
```python
def _setup_from_config(self) -> None
```
**Описание**:
Настраивает конфигурации API OpenAI для этого клиента.

#### `send_message`
```python
def send_message(self, current_messages: list, model: str = default["model"], temperature: float = default["temperature"], max_tokens: int = default["max_tokens"], top_p: int = default["top_p"], frequency_penalty: float = default["frequency_penalty"], presence_penalty: float = default["presence_penalty"], stop: list = [], timeout: float = default["timeout"], max_attempts: int = default["max_attempts"], waiting_time: float = default["waiting_time"], exponential_backoff_factor: float = default["exponential_backoff_factor"], n: int = 1, echo: bool = False) -> dict | None
```
**Описание**:
Отправляет сообщение в API OpenAI и возвращает ответ.

**Параметры**:
- `current_messages` (list): Список словарей, представляющих историю разговоров.
- `model` (str, optional): ID модели для генерации ответа. По умолчанию берется из `default["model"]`.
- `temperature` (float, optional): Контролирует "креативность" ответа. По умолчанию берется из `default["temperature"]`.
- `max_tokens` (int, optional): Максимальное количество токенов для генерации в ответе. По умолчанию берется из `default["max_tokens"]`.
- `top_p` (float, optional): Контролирует "качество" ответа. По умолчанию берется из `default["top_p"]`.
- `frequency_penalty` (float, optional): Контролирует "повторение" ответа. По умолчанию берется из `default["frequency_penalty"]`.
- `presence_penalty` (float, optional): Контролирует "разнообразие" ответа. По умолчанию берется из `default["presence_penalty"]`.
- `stop` (list, optional): Список строк, которые, если встречаются в сгенерированном ответе, вызывают остановку генерации. По умолчанию `[]`.
- `timeout` (float, optional): Максимальное время ожидания ответа от API в секундах. По умолчанию берется из `default["timeout"]`.
- `max_attempts` (int, optional): Максимальное количество попыток получения ответа. По умолчанию берется из `default["max_attempts"]`.
- `waiting_time` (float, optional): Время ожидания между запросами в секундах. По умолчанию берется из `default["waiting_time"]`.
- `exponential_backoff_factor` (float, optional): Коэффициент экспоненциального отката. По умолчанию берется из `default["exponential_backoff_factor"]`.
- `n` (int, optional): Количество ответов. По умолчанию 1.
- `echo` (bool, optional): Следует ли возвращать запрос. По умолчанию `False`.

**Возвращает**:
- `dict | None`: Словарь, представляющий сгенерированный ответ, или `None`, если не удалось получить ответ.

#### `_raw_model_call`
```python
def _raw_model_call(self, model: str, chat_api_params: dict) -> dict
```
**Описание**:
Вызывает API OpenAI с заданными параметрами. Подклассы должны переопределять этот метод для реализации собственных вызовов API.

**Параметры**:
- `model` (str): ID модели для вызова.
- `chat_api_params` (dict): Словарь с параметрами для API-вызова.

**Возвращает**:
- `dict`: Ответ от API.

#### `_raw_model_response_extractor`
```python
def _raw_model_response_extractor(self, response: dict) -> dict
```
**Описание**:
Извлекает ответ из ответа API. Подклассы должны переопределять этот метод для реализации собственного извлечения ответа.

**Параметры**:
- `response` (dict): Ответ от API.

**Возвращает**:
- `dict`: Извлеченный ответ.

#### `_count_tokens`
```python
def _count_tokens(self, messages: list, model: str) -> int | None
```
**Описание**:
Подсчитывает количество токенов OpenAI в списке сообщений с помощью tiktoken.

**Параметры**:
- `messages` (list): Список словарей, представляющих историю разговоров.
- `model` (str): Название модели для кодирования строки.

**Возвращает**:
- `int | None`: Количество токенов или `None`, если произошла ошибка при подсчете.

#### `_save_cache`
```python
def _save_cache(self) -> None
```
**Описание**:
Сохраняет кэш API на диск, используя pickle, так как некоторые объекты не сериализуются в JSON.

#### `_load_cache`
```python
def _load_cache(self) -> dict
```
**Описание**:
Загружает кэш API с диска.

**Возвращает**:
- `dict`: Загруженный кэш API или пустой словарь, если файл кэша не существует.

#### `get_embedding`
```python
def get_embedding(self, text: str, model: str = default["embedding_model"]) -> list
```
**Описание**:
Получает эмбеддинг заданного текста, используя указанную модель.

**Параметры**:
- `text` (str): Текст для эмбеддинга.
- `model` (str, optional): Название модели для эмбеддинга. По умолчанию берется из `default["embedding_model"]`.

**Возвращает**:
- `list`: Эмбеддинг текста.

#### `_raw_embedding_model_call`
```python
def _raw_embedding_model_call(self, text: str, model: str) -> dict
```
**Описание**:
Вызывает API OpenAI для получения эмбеддинга заданного текста. Подклассы должны переопределять этот метод для реализации собственных вызовов API.

**Параметры**:
- `text` (str): Текст для эмбеддинга.
- `model` (str): Название модели для эмбеддинга.

**Возвращает**:
- `dict`: Ответ от API.

#### `_raw_embedding_model_response_extractor`
```python
def _raw_embedding_model_response_extractor(self, response: dict) -> list
```
**Описание**:
Извлекает эмбеддинг из ответа API. Подклассы должны переопределять этот метод для реализации собственного извлечения.

**Параметры**:
- `response` (dict): Ответ от API.

**Возвращает**:
- `list`: Извлеченный эмбеддинг.

### `AzureClient`

**Описание**:
Класс-наследник `OpenAIClient` для взаимодействия с API Azure OpenAI Service.

**Методы**:

#### `__init__`
```python
def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None
```
**Описание**:
Инициализирует экземпляр `AzureClient`.

**Параметры**:
- `cache_api_calls` (bool, optional): Следует ли кэшировать вызовы API. По умолчанию берется из `default["cache_api_calls"]`.
- `cache_file_name` (str, optional): Имя файла для кэширования API-вызовов. По умолчанию берется из `default["cache_file_name"]`.

#### `_setup_from_config`
```python
def _setup_from_config(self) -> None
```
**Описание**:
Настраивает конфигурации API Azure OpenAI Service для этого клиента, включая конечную точку и ключ API.

#### `_raw_model_call`
```python
def _raw_model_call(self, model: str, chat_api_params: dict) -> dict
```
**Описание**:
Вызывает API Azure OpenAI Service с заданными параметрами.

**Параметры**:
- `model` (str): ID модели для вызова.
- `chat_api_params` (dict): Словарь с параметрами для API-вызова.

**Возвращает**:
- `dict`: Ответ от API.

### `InvalidRequestError`

**Описание**:
Исключение, которое возникает, когда запрос к API OpenAI недействителен.

### `NonTerminalError`

**Описание**:
Исключение, которое возникает при возникновении неуточненной ошибки, но известно, что можно повторить запрос.

## Функции

### `register_client`
```python
def register_client(api_type: str, client: object) -> None
```
**Описание**:
Регистрирует клиент для заданного типа API.

**Параметры**:
- `api_type` (str): Тип API, для которого регистрируется клиент.
- `client`: Клиент, который необходимо зарегистрировать.

### `_get_client_for_api_type`
```python
def _get_client_for_api_type(api_type: str) -> object
```
**Описание**:
Возвращает клиент для заданного типа API.

**Параметры**:
- `api_type` (str): Тип API, для которого нужно получить клиент.

**Возвращает**:
- `object`: Клиент для заданного типа API.

**Вызывает исключения**:
- `ValueError`: Если тип API не поддерживается.

### `client`
```python
def client() -> object
```
**Описание**:
Возвращает клиент для настроенного типа API.

**Возвращает**:
- `object`: Клиент для настроенного типа API.

### `force_api_type`
```python
def force_api_type(api_type: str) -> None
```
**Описание**:
Принудительно устанавливает использование заданного типа API, переопределяя любую другую конфигурацию.

**Параметры**:
- `api_type` (str): Тип API, который следует использовать.

### `force_api_cache`
```python
def force_api_cache(cache_api_calls: bool, cache_file_name: str = default["cache_file_name"]) -> None
```
**Описание**:
Принудительно устанавливает использование заданной конфигурации кэша API, переопределяя любую другую конфигурацию.

**Параметры**:
- `cache_api_calls` (bool): Определяет, следует ли кэшировать вызовы API.
- `cache_file_name` (str, optional): Имя файла для кэширования API-вызовов. По умолчанию берется из `default["cache_file_name"]`.

### `force_default_value`
```python
def force_default_value(key: str, value: object) -> None
```
**Описание**:
Принудительно устанавливает использование заданного значения конфигурации по умолчанию для указанного ключа, переопределяя любую другую конфигурацию.

**Параметры**:
- `key` (str): Ключ, который необходимо переопределить.
- `value`: Значение, которое следует использовать для ключа.

**Вызывает исключения**:
- `ValueError`: Если ключ не является допустимым ключом конфигурации.