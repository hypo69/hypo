# Модуль HuggingFaceAPI

## Обзор

Модуль `HuggingFaceAPI` предназначен для взаимодействия с API Hugging Face для генерации текста. Он предоставляет класс `HuggingFaceAPI`, который наследуется от `OpenaiTemplate` и реализует методы для получения моделей, создания асинхронных генераторов и обработки ответов от API Hugging Face.

## Подробнее

Модуль `HuggingFaceAPI` является частью проекта `hypotez` и обеспечивает интеграцию с платформой Hugging Face для выполнения задач, связанных с генерацией текста и обработки естественного языка. Он использует API Hugging Face для доступа к различным моделям и выполнения запросов.

## Классы

### `HuggingFaceAPI`

**Описание**: Класс для взаимодействия с API Hugging Face для генерации текста.

**Наследует**:
- `OpenaiTemplate`: Обеспечивает базовый функционал для работы с API OpenAI-подобного типа.

**Атрибуты**:
- `label` (str): Метка провайдера, `"HuggingFace (Text Generation)"`.
- `parent` (str): Родительский провайдер, `"HuggingFace"`.
- `url` (str): URL API, `"https://api-inference.huggingface.com"`.
- `api_base` (str): Базовый URL API, `"https://api-inference.huggingface.co/v1"`.
- `working` (bool): Статус работоспособности, `True`.
- `needs_auth` (bool): Требуется ли авторизация, `True`.
- `default_model` (str): Модель по умолчанию, `default_llama_model`.
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию, `default_vision_model`.
- `vision_models` (list[str]): Список моделей для работы с изображениями, `vision_models`.
- `model_aliases` (dict[str, str]): Алиасы моделей, `model_aliases`.
- `fallback_models` (list[str]): Список резервных моделей, `text_models + vision_models`.
- `provider_mapping` (dict[str, dict]): Маппинг моделей провайдеров.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает модель.
- `get_models(**kwargs) -> list[str]`: Возвращает список доступных моделей.
- `get_mapping(model: str, api_key: str = None)`: Получает маппинг для модели.
- `create_async_generator(model: str, messages: Messages, api_base: str = None, api_key: str = None, max_tokens: int = 2048, max_inputs_lenght: int = 10000, media: MediaListType = None, **kwargs)`: Создает асинхронный генератор для обработки запросов к API Hugging Face.

## Функции

### `get_model`

```python
@classmethod
def get_model(cls, model: str, **kwargs) -> str:
    """
    Получает модель.

    Args:
        model (str): Название модели.
        **kwargs: Дополнительные аргументы.

    Returns:
        str: Название модели.
    """
```

**Назначение**:
Функция `get_model` используется для получения имени модели. Если модель не поддерживается, возвращается исходное имя модели.

**Параметры**:
- `model` (str): Название модели, которую необходимо получить.
- `**kwargs`: Дополнительные аргументы, которые могут быть переданы.

**Возвращает**:
- `str`: Название модели.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается.

**Как работает функция**:

1. Пытается получить модель, используя метод `super().get_model(model, **kwargs)` класса `OpenaiTemplate`.
2. Если возникает исключение `ModelNotSupportedError`, возвращает исходное имя модели.

```
A
|
B
|
C
```

Где:
- `A`: Начало функции.
- `B`: Попытка получить модель с помощью `super().get_model()`.
- `C`: Возврат имени модели (либо полученного, либо исходного, если произошла ошибка).

**Примеры**:
```python
HuggingFaceAPI.get_model("llama-2-7b")
HuggingFaceAPI.get_model("gpt-3.5-turbo", custom_arg="value")
```

### `get_models`

```python
@classmethod
def get_models(cls, **kwargs) -> list[str]:
    """
    Получает список доступных моделей.

    Args:
        **kwargs: Дополнительные аргументы.

    Returns:
        list[str]: Список доступных моделей.
    """
```

**Назначение**:
Функция `get_models` используется для получения списка доступных моделей из API Hugging Face. Если список моделей еще не был получен, функция выполняет HTTP-запрос к API Hugging Face для получения списка моделей, которые поддерживаются и имеют статус "live".

**Параметры**:
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[str]`: Список доступных моделей.

**Как работает функция**:

1. Проверяет, был ли уже получен список моделей (если `cls.models` не пуст).
2. Если список моделей не был получен, выполняет HTTP-запрос к API Hugging Face для получения списка моделей.
3. Фильтрует полученный список моделей, чтобы включить только те модели, которые имеют статус "live" и поддерживают задачу "conversational".
4. Если HTTP-запрос не удался, использует список резервных моделей (`cls.fallback_models`).
5. Возвращает список доступных моделей.

```
A
|
B
|
C
|
D
```

Где:
- `A`: Начало функции.
- `B`: Проверка, был ли уже получен список моделей.
- `C`: Если список моделей не был получен, выполняется HTTP-запрос к API Hugging Face.
- `D`: Возврат списка доступных моделей.

**Примеры**:
```python
HuggingFaceAPI.get_models()
```

### `get_mapping`

```python
@classmethod
async def get_mapping(cls, model: str, api_key: str = None):
    """
    Получает маппинг для модели.

    Args:
        model (str): Название модели.
        api_key (str, optional): API ключ. По умолчанию `None`.

    Returns:
        dict: Маппинг для модели.
    """
```

**Назначение**:
Функция `get_mapping` используется для получения маппинга для указанной модели из API Hugging Face. Маппинг содержит информацию о том, какой провайдер используется для данной модели.

**Параметры**:
- `model` (str): Название модели, для которой необходимо получить маппинг.
- `api_key` (str, optional): API ключ, который будет использоваться для аутентификации при запросе к API Hugging Face. По умолчанию `None`.

**Возвращает**:
- `dict`: Маппинг для модели.

**Как работает функция**:

1. Проверяет, есть ли маппинг для данной модели в `cls.provider_mapping`. Если есть, возвращает его.
2. Если маппинга нет, выполняет HTTP-запрос к API Hugging Face для получения маппинга.
3. Сохраняет полученный маппинг в `cls.provider_mapping`.
4. Возвращает маппинг для модели.

```
A
|
B
|
C
|
D
```

Где:
- `A`: Начало функции.
- `B`: Проверка, есть ли маппинг для данной модели в `cls.provider_mapping`.
- `C`: Если маппинга нет, выполняется HTTP-запрос к API Hugging Face для получения маппинга.
- `D`: Возврат маппинга для модели.

**Примеры**:
```python
await HuggingFaceAPI.get_mapping("llama-2-7b", api_key="YOUR_API_KEY")
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_base: str = None,
    api_key: str = None,
    max_tokens: int = 2048,
    max_inputs_lenght: int = 10000,
    media: MediaListType = None,
    **kwargs
):
    """
    Создает асинхронный генератор для обработки запросов к API Hugging Face.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений.
        api_base (str, optional): Базовый URL API. По умолчанию `None`.
        api_key (str, optional): API ключ. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
        max_inputs_lenght (int, optional): Максимальная длина входных данных. По умолчанию 10000.
        media (MediaListType, optional): Список медиафайлов. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncGenerator: Асинхронный генератор для обработки запросов к API Hugging Face.
    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор для обработки запросов к API Hugging Face. Она получает информацию о модели, сообщения, API-ключ и другие параметры, необходимые для выполнения запроса, и возвращает генератор, который может использоваться для получения чанков ответа от API Hugging Face.

**Параметры**:
- `model` (str): Название модели, которую необходимо использовать для генерации текста.
- `messages` (Messages): Список сообщений, которые будут отправлены в API Hugging Face.
- `api_base` (str, optional): Базовый URL API Hugging Face. По умолчанию `None`.
- `api_key` (str, optional): API ключ для аутентификации в API Hugging Face. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов, которое должно быть сгенерировано в ответе. По умолчанию 2048.
- `max_inputs_lenght` (int, optional): Максимальная длина входных данных. По умолчанию 10000.
- `media` (MediaListType, optional): Список медиафайлов, которые будут отправлены в API Hugging Face. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncGenerator`: Асинхронный генератор для обработки запросов к API Hugging Face.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается.
- `PaymentRequiredError`: Если требуется оплата для использования модели.

**Как работает функция**:

1. Если модель не указана и есть медиафайлы, использует `cls.default_vision_model` как модель по умолчанию.
2. Получает модель, используя метод `cls.get_model(model)`.
3. Получает маппинг для модели, используя метод `cls.get_mapping(model, api_key)`.
4. Если маппинг не найден, вызывает исключение `ModelNotSupportedError`.
5. Итерируется по провайдерам в маппинге.
6. Формирует `api_path` и `api_base` для каждого провайдера.
7. Проверяет, что задача для модели - "conversational". Если нет, вызывает исключение `ModelNotSupportedError`.
8. Обновляет название модели из маппинга провайдера.
9. Создает и возвращает `ProviderInfo` объект.
10. Вызывает `super().create_async_generator` для создания асинхронного генератора.
11. Перехватывает исключение `PaymentRequiredError` и пытается продолжить с другим провайдером.
12. Если все провайдеры не удались и было исключение `PaymentRequiredError`, вызывает это исключение повторно.

```
A
|
B
|
C
|
D
|
E
|
F
|
G
|
H
|
I
|
J
```

Где:
- `A`: Начало функции.
- `B`: Проверка наличия модели и медиафайлов.
- `C`: Получение модели.
- `D`: Получение маппинга для модели.
- `E`: Проверка наличия маппинга.
- `F`: Итерация по провайдерам в маппинге.
- `G`: Формирование `api_path` и `api_base`.
- `H`: Проверка задачи для модели.
- `I`: Обновление названия модели.
- `J`: Вызов `super().create_async_generator` и обработка исключений.

**Примеры**:
```python
async for chunk in HuggingFaceAPI.create_async_generator(
    model="llama-2-7b",
    messages=[{"role": "user", "content": "Hello"}],
    api_key="YOUR_API_KEY"
):
    print(chunk)
```

### `calculate_lenght`

```python
def calculate_lenght(messages: Messages) -> int:
    """
    Вычисляет длину списка сообщений.

    Args:
        messages (Messages): Список сообщений.

    Returns:
        int: Длина списка сообщений.
    """
```

**Назначение**:
Функция `calculate_lenght` используется для вычисления общей длины списка сообщений. Она складывает длину содержимого каждого сообщения и добавляет 16 к каждому.

**Параметры**:
- `messages` (Messages): Список сообщений, для которого необходимо вычислить длину.

**Возвращает**:
- `int`: Общая длина списка сообщений.

**Как работает функция**:

1. Итерируется по списку сообщений.
2. Для каждого сообщения вычисляет длину содержимого и добавляет 16.
3. Суммирует все вычисленные значения и возвращает общую длину.

```
A
|
B
|
C
```

Где:
- `A`: Начало функции.
- `B`: Итерация по списку сообщений.
- `C`: Вычисление и суммирование длин сообщений.

**Примеры**:
```python
messages = [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi"}]
calculate_lenght(messages)  # Возвращает 21 (5 + 16 + 2 + 16)