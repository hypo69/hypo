# Модуль для работы с OpenAI API
====================================

Модуль предоставляет инструменты для взаимодействия с OpenAI API, включая поддержку кэширования запросов, обработки ошибок и управления различными типами клиентов (OpenAI и Azure).

## Обзор

Этот модуль предназначен для упрощения взаимодействия с OpenAI API. Он включает в себя классы для управления запросами к API, обработки ответов и кэширования результатов. Модуль поддерживает как стандартный OpenAI API, так и Azure OpenAI Service API, позволяя пользователям выбирать подходящий клиент в зависимости от конфигурации.

## Подробнее

Модуль предоставляет следующие возможности:

-   **Кэширование API-запросов**: Позволяет кэшировать запросы к API и повторно использовать результаты, что снижает нагрузку на API и ускоряет выполнение задач.
-   **Обработка ошибок**: Включает механизмы обработки ошибок, таких как ограничение скорости запросов и невалидные запросы, с возможностью повторных попыток.
-   **Поддержка различных типов клиентов**: Поддерживает как OpenAI, так и Azure OpenAI Service API, позволяя пользователям выбирать подходящий клиент в зависимости от конфигурации.
-   **Автоматическое преобразование типов данных**: Позволяет автоматически преобразовывать результаты, возвращаемые API, в нужные типы данных, такие как `bool`, `int`, `float` и `list`.

## Классы

### `LLMRequest`

**Описание**: Класс, представляющий запрос к языковой модели (LLM). Он содержит входные сообщения, конфигурацию модели и вывод модели.

**Принцип работы**:

Класс `LLMRequest` используется для формирования и выполнения запросов к большим языковым моделям. Он позволяет задавать системные и пользовательские промпты, параметры модели, а также типы ожидаемых выходных данных. Класс автоматически формирует сообщения для модели, вызывает API и преобразует результаты в нужный формат.

**Атрибуты**:

-   `system_template_name` (str, optional): Имя системного шаблона.
-   `system_prompt` (str, optional): Системный промпт.
-   `user_template_name` (str, optional): Имя пользовательского шаблона.
-   `user_prompt` (str, optional): Пользовательский промпт.
-   `output_type` (type, optional): Тип ожидаемых выходных данных.
-   `model_params` (dict): Параметры модели.
-   `model_output` (any): Вывод модели.
-   `messages` (list): Список сообщений для модели.
-   `response_raw` (str): Необработанный ответ от модели.
-   `response_json` (dict): JSON-ответ от модели.
-   `response_value` (any): Значение ответа модели.
-   `response_justification` (str): Обоснование ответа модели.
-   `response_confidence` (float): Уровень уверенности в ответе модели.

**Методы**:

-   `__init__(self, system_template_name: str = None, system_prompt: str = None, user_template_name: str = None, user_prompt: str = None, output_type=None, \*\*model_params)`: Инициализирует экземпляр `LLMRequest`.
-   `call(self, \*\*rendering_configs)`: Вызывает LLM модель с указанными конфигурациями рендеринга.

#### `__init__`

```python
def __init__(self, system_template_name: str = None, system_prompt: str = None, user_template_name: str = None, user_prompt: str = None, output_type=None, **model_params):
    """
    Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами или системными и пользовательскими промптами.
    Если указан шаблон, соответствующий промпт должен быть None, и наоборот.

    Args:
        system_template_name (str, optional): Имя системного шаблона.
        system_prompt (str, optional): Системный промпт.
        user_template_name (str, optional): Имя пользовательского шаблона.
        user_prompt (str, optional): Пользовательский промпт.
        output_type (type, optional): Тип ожидаемых выходных данных.
        **model_params: Дополнительные параметры модели.

    Raises:
        ValueError: Если указаны и шаблон, и промпт одновременно, или если не указан ни шаблон, ни промпт.
    """
    ...
```

**Как работает функция**:

1.  Проверяет, что указан либо шаблон, либо промпт, но не оба одновременно.
2.  Сохраняет имена шаблонов и сами промпты.
3.  Сохраняет тип выходных данных и параметры модели.
4.  Инициализирует пустой список сообщений и атрибуты для хранения результатов вызова модели.

##### ASCII flowchart

```
Проверка наличия шаблона или промпта --> Сохранение шаблонов и промптов --> Сохранение типа выходных данных и параметров модели --> Инициализация списка сообщений и атрибутов для результатов
```

#### `call`

```python
def call(self, **rendering_configs):
    """
    Вызывает LLM модель с указанными конфигурациями рендеринга.

    Args:
        rendering_configs: Конфигурации рендеринга (переменные шаблона) для использования при составлении начальных сообщений.

    Returns:
        The content of the model response.
    """
    ...
```

**Как работает функция**:

1.  Определяет, какие сообщения необходимо передать модели.
2.  Осуществляет вызов модели с заданными параметрами.
3.  Извлекает контент из ответа модели.
4.  Если указан тип выходных данных, преобразует результат в соответствующий тип.
5.  Возвращает значение, полученное от модели.

##### ASCII flowchart

```
Определение передаваемых сообщений --> Вызов модели --> Извлечение контента из ответа --> Преобразование типа данных (если необходимо) --> Возврат значения
```

### `LLMScalarWithJustificationResponse`

**Описание**: Класс для представления типизированного ответа от языковой модели (LLM).

**Принцип работы**:

Этот класс используется для структурированного представления ответов от языковых моделей, которые включают значение, обоснование и уровень уверенности. Он обеспечивает типизацию данных и упрощает обработку результатов.

**Атрибуты**:

-   `value` (str | int | float | bool): Значение ответа.
-   `justification` (str): Обоснование или объяснение ответа.
-   `confidence` (float): Уровень уверенности в ответе.

### `OpenAIClient`

**Описание**: Класс для взаимодействия с OpenAI API.

**Принцип работы**:

Класс `OpenAIClient` предоставляет методы для отправки сообщений в OpenAI API, кэширования запросов и обработки ответов. Он поддерживает как стандартный OpenAI API, так и Azure OpenAI Service API.

**Методы**:

-   `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Инициализирует экземпляр `OpenAIClient`.
-   `set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"])`: Включает или отключает кэширование API-запросов.
-   `send_message(self, current_messages, model=default["model"], temperature=default["temperature"], max_tokens=default["max_tokens"], top_p=default["top_p"], frequency_penalty=default["frequency_penalty"], presence_penalty=default["presence_penalty"], stop=[], timeout=default["timeout"], max_attempts=default["max_attempts"], waiting_time=default["waiting_time"], exponential_backoff_factor=default["exponential_backoff_factor"], n=1, response_format=None, echo=False)`: Отправляет сообщение в OpenAI API и возвращает ответ.
-   `get_embedding(self, text, model=default["embedding_model"])`: Получает эмбеддинг для заданного текста с использованием указанной модели.

#### `__init__`

```python
def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None:
    """
    Инициализирует OpenAIClient.

    Args:
        cache_api_calls (bool): Следует ли кэшировать вызовы API.
        cache_file_name (str): Имя файла для использования для кэширования вызовов API.
    """
    ...
```

**Как работает функция**:

1.  Инициализирует клиент OpenAI.
2.  Устанавливает параметры кэширования API-вызовов.
3.  Загружает кэш API, если включено кэширование.

##### ASCII flowchart

```
Инициализация клиента OpenAI --> Установка параметров кэширования --> Загрузка кэша API (если включено кэширование)
```

#### `set_api_cache`

```python
def set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"]):
    """
    Включает или отключает кэширование API-вызовов.

    Args:
        cache_api_calls (bool): Следует ли кэшировать вызовы API.
        cache_file_name (str): Имя файла для использования для кэширования API-вызовов.
    """
    ...
```

**Как работает функция**:

1.  Устанавливает параметры кэширования API-вызовов.
2.  Загружает кэш API, если включено кэширование.

##### ASCII flowchart

```
Установка параметров кэширования --> Загрузка кэша API (если включено кэширование)
```

#### `send_message`

```python
def send_message(self, current_messages, model=default["model"], temperature=default["temperature"], max_tokens=default["max_tokens"], top_p=default["top_p"], frequency_penalty=default["frequency_penalty"], presence_penalty=default["presence_penalty"], stop=[], timeout=default["timeout"], max_attempts=default["max_attempts"], waiting_time=default["waiting_time"], exponential_backoff_factor=default["exponential_backoff_factor"], n=1, response_format=None, echo=False):
    """
    Отправляет сообщение в OpenAI API и возвращает ответ.

    Args:
        current_messages (list): Список словарей, представляющих историю разговора.
        model (str): ID модели для использования для генерации ответа.
        temperature (float): Контролирует "креативность" ответа. Более высокие значения приводят к более разнообразным ответам.
        max_tokens (int): Максимальное количество токенов (слов или знаков препинания) для генерации в ответе.
        top_p (float): Контролирует "качество" ответа. Более высокие значения приводят к более связным ответам.
        frequency_penalty (float): Контролирует "повторение" ответа. Более высокие значения приводят к меньшему повторению.
        presence_penalty (float): Контролирует "разнообразие" ответа. Более высокие значения приводят к более разнообразным ответам.
        stop (str): Строка, которая, если она встречается в сгенерированном ответе, приведет к остановке генерации.
        max_attempts (int): Максимальное количество попыток, которые нужно предпринять, прежде чем отказаться от генерации ответа.
        timeout (int): Максимальное количество секунд ожидания ответа от API.
        waiting_time (int): Количество секунд ожидания между запросами.
        exponential_backoff_factor (int): Фактор, на который следует увеличивать время ожидания между запросами.
        n (int): Количество завершений для генерации.
        response_format: Формат ответа, если есть.

    Returns:
        A dictionary representing the generated response.
    """
    ...
```

**Как работает функция**:

1.  Настраивает параметры для запроса к OpenAI API.
2.  Вызывает OpenAI API с заданными параметрами.
3.  Обрабатывает ответы от API и возвращает результаты.
4.  Использует кэширование, если оно включено.
5.  В случае ошибок, повторяет запрос с экспоненциальной задержкой.

##### ASCII flowchart

```
Настройка параметров API --> Вызов OpenAI API --> Обработка ответа --> Кэширование (если включено) --> Повторные попытки при ошибках
```

#### `get_embedding`

```python
def get_embedding(self, text, model=default["embedding_model"]):
    """
    Получает эмбеддинг для заданного текста с использованием указанной модели.

    Args:
        text (str): Текст для эмбеддинга.
        model (str): Имя модели для использования для эмбеддинга текста.

    Returns:
        Эмбеддинг текста.
    """
    ...
```

**Как работает функция**:

1.  Вызывает OpenAI API для получения эмбеддинга текста.
2.  Обрабатывает ответ от API и возвращает эмбеддинг.

##### ASCII flowchart

```
Вызов OpenAI API для эмбеддинга --> Обработка ответа --> Возврат эмбеддинга
```

### `AzureClient`

**Описание**: Класс для взаимодействия с Azure OpenAI Service API.

**Принцип работы**:

Класс `AzureClient` наследует функциональность от `OpenAIClient` и переопределяет метод `_setup_from_config` для настройки параметров, специфичных для Azure OpenAI Service API.

**Методы**:

-   `__init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"])`: Инициализирует экземпляр `AzureClient`.

#### `__init__`

```python
def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None:
    """
    Инициализирует AzureClient.

    Args:
        cache_api_calls (bool): Следует ли кэшировать вызовы API.
        cache_file_name (str): Имя файла для использования для кэширования вызовов API.
    """
    ...
```

**Как работает функция**:

1.  Вызывает конструктор родительского класса `OpenAIClient`.
2.  Инициализирует клиент Azure OpenAI.

##### ASCII flowchart

```
Вызов конструктора OpenAIClient --> Инициализация клиента Azure OpenAI
```

## Функции

### `register_client`

```python
def register_client(api_type, client):
    """
    Регистрирует клиент для заданного типа API.

    Args:
        api_type (str): Тип API, для которого мы хотим зарегистрировать клиент.
        client: Клиент для регистрации.
    """
    ...
```

**Как работает функция**:

1.  Регистрирует клиент для заданного типа API в глобальном словаре `_api_type_to_client`.

##### ASCII flowchart

```
Регистрация клиента в словаре _api_type_to_client
```

### `client`

```python
def client():
    """
    Возвращает клиент для настроенного типа API.
    """
    ...
```

**Как работает функция**:

1.  Определяет тип API из конфигурации.
2.  Возвращает клиент, зарегистрированный для этого типа API.

##### ASCII flowchart

```
Определение типа API --> Возврат клиента для типа API
```

### `force_api_type`

```python
def force_api_type(api_type):
    """
    Принудительно использует заданный тип API, тем самым переопределяя любую другую конфигурацию.

    Args:
        api_type (str): Тип API для использования.
    """
    ...
```

**Как работает функция**:

1.  Устанавливает глобальную переменную `_api_type_override` в заданный тип API.

##### ASCII flowchart

```
Установка _api_type_override в заданный тип API
```

### `force_api_cache`

```python
def force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"]):
    """
    Принудительно использует заданную конфигурацию кэша API, тем самым переопределяя любую другую конфигурацию.

    Args:
        cache_api_calls (bool): Следует ли кэшировать вызовы API.
        cache_file_name (str): Имя файла для использования для кэширования вызовов API.
    """
    ...
```

**Как работает функция**:

1.  Устанавливает параметры кэширования API-вызовов для всех зарегистрированных клиентов.

##### ASCII flowchart

```
Установка параметров кэширования для всех клиентов
```

## Исключения

### `InvalidRequestError`

**Описание**: Исключение, которое вызывается, когда запрос к OpenAI API является недействительным.

### `NonTerminalError`

**Описание**: Исключение, которое вызывается, когда происходит неуказанная ошибка, но мы знаем, что можем повторить попытку.

## Примеры

### Инициализация и использование `LLMRequest`

```python
from tinytroupe.openai_utils import LLMRequest

llm_request = LLMRequest(
    system_prompt="You are a helpful assistant.",
    user_prompt="What is the capital of France?",
    model_params={"model": "gpt-3.5-turbo"}
)

response = llm_request.call()
print(response)  # Вывод: Paris
```

### Инициализация и использование `OpenAIClient`

```python
from tinytroupe.openai_utils import OpenAIClient

client = OpenAIClient()
messages = [{"role": "user", "content": "Hello, how are you?"}]
response = client.send_message(messages)
print(response)  # Вывод: {'role': 'assistant', 'content': 'I am doing well, thank you! How can I assist you today?'}