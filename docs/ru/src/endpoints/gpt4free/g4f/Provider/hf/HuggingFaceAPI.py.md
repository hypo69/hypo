# Модуль для работы с Hugging Face API для генерации текста
## Обзор

Модуль `HuggingFaceAPI` предназначен для взаимодействия с API Hugging Face для генерации текста. Он наследует функциональность от класса `OpenaiTemplate` и предоставляет методы для получения моделей, создания асинхронных генераторов и обработки запросов к API Hugging Face.

## Подробней

Модуль `HuggingFaceAPI` предоставляет интерфейс для взаимодействия с различными моделями Hugging Face, включая модели для генерации текста и модели для работы с изображениями. Он использует API-инференс Hugging Face для выполнения запросов и обработки ответов. Модуль также поддерживает работу с провайдерами, такими как Novita.

## Классы

### `HuggingFaceAPI`

**Описание**: Класс для работы с API Hugging Face для генерации текста.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовую функциональность для работы с API OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера "HuggingFace (Text Generation)".
- `parent` (str): Родительский провайдер "HuggingFace".
- `url` (str): URL API Hugging Face "https://api-inference.huggingface.com".
- `api_base` (str): Базовый URL API Hugging Face "https://api-inference.huggingface.co/v1".
- `working` (bool): Указывает, что провайдер работает (True).
- `needs_auth` (bool): Указывает, что требуется аутентификация (True).
- `default_model` (str): Модель по умолчанию `default_llama_model`.
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию `default_vision_model`.
- `vision_models` (List[str]): Список моделей для работы с изображениями `vision_models`.
- `model_aliases` (Dict[str, str]): Алиасы моделей `model_aliases`.
- `fallback_models` (List[str]): Список запасных моделей `text_models` + `vision_models`.
- `provider_mapping` (Dict[str, Dict]): Соответствие моделей и провайдеров.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает имя модели.
- `get_models(**kwargs) -> list[str]`: Возвращает список доступных моделей.
- `get_mapping(model: str, api_key: str = None) -> dict`: Возвращает mapping для модели.
- `create_async_generator(model: str, messages: Messages, api_base: str = None, api_key: str = None, max_tokens: int = 2048, max_inputs_lenght: int = 10000, media: MediaListType = None, **kwargs)`: Создает асинхронный генератор для обработки запросов.

## Функции

### `calculate_lenght`

```python
def calculate_lenght(messages: Messages) -> int:
    """
    Вычисляет суммарную длину содержимого всех сообщений в списке.

    Args:
        messages (Messages): Список сообщений, каждое из которых является словарем с ключом "content".

    Returns:
        int: Суммарная длина содержимого всех сообщений.
    """
    ...
```

**Назначение**: Вычисляет суммарную длину содержимого всех сообщений в списке.

**Параметры**:
- `messages` (Messages): Список сообщений, каждое из которых является словарем с ключом "content".

**Возвращает**:
- `int`: Суммарная длина содержимого всех сообщений.

**Как работает функция**:

1.  Инициализирует переменную `total_length` значением 0.
2.  Перебирает каждое сообщение в списке `messages`.
3.  Для каждого сообщения вычисляет длину содержимого (message["content"]) и добавляет 16.
4.  Суммирует длины содержимого всех сообщений и возвращает результат.

```
Начало --> Инициализация_длины
|
--> Для_каждого_сообщения_в_messages
|   |
|   --> Вычисление_длины_сообщения
|   |
|   --> Суммирование_длин
|
--> Возврат_суммарной_длины
|
Конец
```

**Примеры**:

```python
from typing import List, Dict, Union, Optional

Messages = List[Dict[str, str]]

messages1: Messages = [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi"}]
length1 = calculate_lenght(messages1)
print(f"Length of messages1: {length1}")  # Output: Length of messages1: 21

messages2: Messages = [{"role": "user", "content": "This is a longer message"}]
length2 = calculate_lenght(messages2)
print(f"Length of messages2: {length2}")  # Output: Length of messages2: 41

messages3: Messages = []
length3 = calculate_lenght(messages3)
print(f"Length of messages3: {length3}")  # Output: Length of messages3: 0

```

### `HuggingFaceAPI.get_model`

```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        """
        Получает имя модели.

        Args:
            model (str): Имя модели.
            **kwargs: Дополнительные аргументы.

        Returns:
            str: Имя модели.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
        """
        ...
```

**Назначение**: Получает имя модели.

**Параметры**:
- `model` (str): Имя модели.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: Имя модели.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается.

**Как работает функция**:

1.  Пытается получить модель, используя метод `super().get_model(model, **kwargs)`.
2.  Если возникает исключение `ModelNotSupportedError`, возвращает исходное имя модели.

```
Начало --> Попытка_получения_модели
|
--> Если_ошибка
|   |
|   --> Возврат_имени_модели
|
--> Иначе
|   |
|   --> Возврат_полученной_модели
|
Конец
```

**Примеры**:

```python
# Пример использования get_model
model_name = HuggingFaceAPI.get_model("some_model")
print(f"Model name: {model_name}")

```

### `HuggingFaceAPI.get_models`

```python
    @classmethod
    def get_models(cls, **kwargs) -> list[str]:
        """
        Получает список доступных моделей из API Hugging Face.

        Args:
            **kwargs: Дополнительные аргументы.

        Returns:
            list[str]: Список доступных моделей.
        """
        ...
```

**Назначение**: Получает список доступных моделей из API Hugging Face.

**Параметры**:
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `list[str]`: Список доступных моделей.

**Как работает функция**:

1.  Проверяет, если список моделей (`cls.models`) пуст.
2.  Если список пуст, выполняет запрос к API Hugging Face для получения списка моделей.
3.  Фильтрует список моделей, оставляя только те, у которых статус "live" и задача "conversational".
4.  Добавляет ключи из `cls.provider_mapping` к списку моделей.
5.  Если запрос к API не удался, использует список `cls.fallback_models` в качестве запасного варианта.
6.  Возвращает список доступных моделей.

```
Начало --> Проверка_пустоты_списка_моделей
|
--> Если_список_пуст
|   |
|   --> Запрос_к_API_Hugging_Face
|   |
|   --> Фильтрация_моделей
|   |
|   --> Добавление_ключей_из_provider_mapping
|   |
|   --> Если_запрос_не_удался
|   |   |
|   |   --> Использование_fallback_models
|
--> Возврат_списка_моделей
|
Конец
```

**Примеры**:

```python
# Пример использования get_models
available_models = HuggingFaceAPI.get_models()
print(f"Available models: {available_models}")
```

### `HuggingFaceAPI.get_mapping`

```python
    @classmethod
    async def get_mapping(cls, model: str, api_key: str = None) -> dict:
        """
        Получает mapping для модели.

        Args:
            model (str): Имя модели.
            api_key (str, optional): API ключ. По умолчанию None.

        Returns:
            dict: Mapping для модели.
        """
        ...
```

**Назначение**: Получает mapping для модели.

**Параметры**:
- `model` (str): Имя модели.
- `api_key` (str, optional): API ключ. По умолчанию `None`.

**Возвращает**:
- `dict`: Mapping для модели.

**Как работает функция**:

1.  Проверяет, если mapping для модели уже существует в `cls.provider_mapping`.
2.  Если mapping существует, возвращает его.
3.  Если mapping не существует, выполняет запрос к API Hugging Face для получения mapping.
4.  Сохраняет полученный mapping в `cls.provider_mapping`.
5.  Возвращает mapping для модели.

```
Начало --> Проверка_существования_mapping
|
--> Если_mapping_существует
|   |
|   --> Возврат_mapping
|
--> Иначе
|   |
|   --> Запрос_к_API_Hugging_Face
|   |
|   --> Сохранение_mapping
|   |
|   --> Возврат_mapping
|
Конец
```

**Примеры**:

```python
# Пример использования get_mapping
import asyncio

async def main():
    model_mapping = await HuggingFaceAPI.get_mapping("some_model", api_key="some_api_key")
    print(f"Model mapping: {model_mapping}")

asyncio.run(main())
```

### `HuggingFaceAPI.create_async_generator`

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
        Создает асинхронный генератор для обработки запросов.

        Args:
            model (str): Имя модели.
            messages (Messages): Список сообщений.
            api_base (str, optional): Базовый URL API. По умолчанию None.
            api_key (str, optional): API ключ. По умолчанию None.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
            max_inputs_lenght (int, optional): Максимальная длина входных данных. По умолчанию 10000.
            media (MediaListType, optional): Список медиафайлов. По умолчанию None.
            **kwargs: Дополнительные аргументы.

        Yields:
            ProviderInfo: Информация о провайдере.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для обработки запросов.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений.
- `api_base` (str, optional): Базовый URL API. По умолчанию `None`.
- `api_key` (str, optional): API ключ. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
- `max_inputs_lenght` (int, optional): Максимальная длина входных данных. По умолчанию 10000.
- `media` (MediaListType, optional): Список медиафайлов. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Yields**:
- `ProviderInfo`: Информация о провайдере.

**Как работает функция**:

1.  Если модель не указана и есть медиафайлы, использует `cls.default_vision_model`.
2.  Получает имя модели, используя метод `cls.get_model(model)`.
3.  Получает mapping для модели, используя метод `cls.get_mapping(model, api_key)`.
4.  Если mapping не существует, вызывает исключение `ModelNotSupportedError`.
5.  Перебирает провайдеров в mapping.
6.  Для каждого провайдера определяет `api_path` и `api_base`.
7.  Проверяет, если задача провайдера "conversational". Если нет, вызывает исключение `ModelNotSupportedError`.
8.  Извлекает `providerId` из mapping.
9.  Генерирует `ProviderInfo` и передает его в yield.
10. Вызывает `super().create_async_generator` для обработки запроса.

```
Начало --> Проверка_модели_и_медиа
|
--> Получение_имени_модели
|
--> Получение_mapping
|
--> Если_mapping_не_существует
|   |
|   --> Вызов_исключения_ModelNotSupportedError
|
--> Перебор_провайдеров
|   |
|   --> Определение_api_path_и_api_base
|   |
|   --> Проверка_задачи_провайдера
|   |
|   --> Если_задача_не_conversational
|   |   |
|   |   --> Вызов_исключения_ModelNotSupportedError
|
--> Извлечение_providerId
|
--> Генерация_ProviderInfo_и_yield
|
--> Вызов_super_create_async_generator
|
Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, Union, Optional

Messages = List[Dict[str, str]]

async def main():
    messages: Messages = [{"role": "user", "content": "Hello"}]
    async for chunk in HuggingFaceAPI.create_async_generator(model="some_model", messages=messages, api_key="some_api_key"):
        print(chunk)

asyncio.run(main())