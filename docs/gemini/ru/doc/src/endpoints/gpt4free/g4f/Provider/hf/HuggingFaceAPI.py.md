# Модуль HuggingFaceAPI

## Обзор

Модуль `HuggingFaceAPI` предназначен для взаимодействия с моделями Hugging Face для генерации текста. Он наследует функциональность от `OpenaiTemplate` и адаптирует её для работы с API Hugging Face, обеспечивая поддержку различных моделей, включая модели для обработки текста и изображений. Модуль обеспечивает аутентификацию, выбор моделей и обработку ответов от API Hugging Face.

## Подробнее

Модуль `HuggingFaceAPI` является частью системы для работы с различными поставщиками AI-моделей. Он предоставляет интерфейс для взаимодействия с Hugging Face API, позволяя выбирать модели, передавать запросы и получать ответы. Модуль поддерживает как текстовые, так и визуальные модели, а также обеспечивает обработку ошибок и выбор оптимального провайдера для каждой модели.

## Классы

### `HuggingFaceAPI`

**Описание**: Класс `HuggingFaceAPI` предоставляет методы для взаимодействия с API Hugging Face для генерации текста.

**Наследует**:
- `OpenaiTemplate`: Класс наследует от `OpenaiTemplate`, предоставляя общую структуру для работы с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера "HuggingFace (Text Generation)".
- `parent` (str): Родительский провайдер "HuggingFace".
- `url` (str): URL API Hugging Face.
- `api_base` (str): Базовый URL API Hugging Face.
- `working` (bool): Указывает, что провайдер находится в рабочем состоянии.
- `needs_auth` (bool): Указывает, что для работы с провайдером требуется аутентификация.
- `default_model` (str): Модель по умолчанию (`default_llama_model`).
- `default_vision_model` (str): Визуальная модель по умолчанию (`default_vision_model`).
- `vision_models` (list[str]): Список визуальных моделей.
- `model_aliases` (dict[str, str]): Псевдонимы моделей.
- `fallback_models` (list[str]): Список запасных моделей.
- `provider_mapping` (dict[str, dict]): Сопоставление моделей и провайдеров.

**Методы**:
- `get_model()`: Возвращает имя модели.
- `get_models()`: Возвращает список доступных моделей.
- `get_mapping()`: Возвращает сопоставление моделей и провайдеров.
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с API Hugging Face.

## Функции

### `get_model`

```python
 @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        """
        Метод для получения имени модели.

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

**Назначение**: Получение имени модели, при необходимости обращается к родительскому классу.

**Параметры**:
- `model` (str): Имя модели.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `str`: Имя модели.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается.

**Как работает функция**:

1.  Пытается получить модель, используя метод `get_model` родительского класса (`super()`).
2.  Если возникает исключение `ModelNotSupportedError`, возвращает исходное имя модели.

```
A: Попытка получения модели через родительский класс
|
B: Обработка исключения ModelNotSupportedError
|
C: Возврат имени модели
```

**Примеры**:
```python
model_name = HuggingFaceAPI.get_model("some_model")
print(model_name)
```

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs) -> list[str]:
        """
        Возвращает список доступных моделей Hugging Face.

        Args:
            **kwargs: Дополнительные аргументы.

        Returns:
            list[str]: Список доступных моделей.
        """
        ...
```

**Назначение**: Метод для получения списка доступных моделей из Hugging Face.

**Параметры**:
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `list[str]`: Список доступных моделей.

**Как работает функция**:

1.  Проверяет, был ли уже получен список моделей.
2.  Если список моделей не был получен, отправляет GET-запрос к API Hugging Face для получения списка моделей.
3.  Обрабатывает ответ API и извлекает идентификаторы моделей, у которых статус "live" и задача "conversational".
4.  Добавляет в список моделей ключи из `cls.provider_mapping`.
5.  Если запрос не удался, использует список запасных моделей (`cls.fallback_models`).
6.  Возвращает список моделей.

```
A: Проверка наличия списка моделей
|
B: Получение списка моделей из API Hugging Face
|
C: Извлечение идентификаторов моделей
|
D: Добавление ключей из provider_mapping
|
E: Использование списка запасных моделей при неудачном запросе
|
F: Возврат списка моделей
```

**Примеры**:
```python
models = HuggingFaceAPI.get_models()
print(models)
```

### `get_mapping`

```python
    @classmethod
    async def get_mapping(cls, model: str, api_key: str = None):
        """
        Получает сопоставление моделей и провайдеров.

        Args:
            model (str): Имя модели.
            api_key (str, optional): API-ключ. По умолчанию `None`.

        Returns:
            dict: Сопоставление моделей и провайдеров.
        """
        ...
```

**Назначение**: Получение сопоставления между моделями и провайдерами для Hugging Face.

**Параметры**:
- `model` (str): Имя модели.
- `api_key` (str, optional): API-ключ. По умолчанию `None`.

**Возвращает**:
- `dict`: Сопоставление моделей и провайдеров.

**Как работает функция**:

1.  Проверяет, есть ли сопоставление для данной модели в `cls.provider_mapping`.
2.  Если сопоставление найдено, возвращает его.
3.  Если сопоставление не найдено, отправляет асинхронный GET-запрос к API Hugging Face для получения информации о модели и её сопоставлении с провайдерами.
4.  Сохраняет полученное сопоставление в `cls.provider_mapping`.
5.  Возвращает сопоставление.

```
A: Проверка наличия сопоставления в provider_mapping
|
B: Отправка асинхронного GET-запроса к API Hugging Face
|
C: Сохранение сопоставления в provider_mapping
|
D: Возврат сопоставления
```

**Примеры**:
```python
import asyncio

async def main():
    mapping = await HuggingFaceAPI.get_mapping("some_model")
    print(mapping)

asyncio.run(main())
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
        Создает асинхронный генератор для взаимодействия с API Hugging Face.

        Args:
            model (str): Имя модели.
            messages (Messages): Список сообщений для отправки.
            api_base (str, optional): Базовый URL API. По умолчанию `None`.
            api_key (str, optional): API-ключ. По умолчанию `None`.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
            max_inputs_lenght (int, optional): Максимальная длина входных данных. По умолчанию 10000.
            media (MediaListType, optional): Список медиафайлов. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.
        """
        ...
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API Hugging Face для генерации текста.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для отправки.
- `api_base` (str, optional): Базовый URL API. По умолчанию `None`.
- `api_key` (str, optional): API-ключ. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 2048.
- `max_inputs_lenght` (int, optional): Максимальная длина входных данных. По умолчанию 10000.
- `media` (MediaListType, optional): Список медиафайлов. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Как работает функция**:

1.  Если модель не указана и есть медиафайлы, использует модель по умолчанию для обработки изображений.
2.  Получает имя модели с помощью `cls.get_model()`.
3.  Получает сопоставление модели и провайдера с помощью `cls.get_mapping()`.
4.  Если сопоставление не найдено, вызывает исключение `ModelNotSupportedError`.
5.  Итерируется по провайдерам в сопоставлении.
6.  Формирует URL API на основе информации о провайдере.
7.  Проверяет, что задача провайдера — "conversational". Если это не так, вызывает исключение `ModelNotSupportedError`.
8.  Извлекает идентификатор модели провайдера.
9.  Возвращает информацию о провайдере (`ProviderInfo`).
10. Вызывает `super().create_async_generator()` для фактической генерации текста, используя выбранного провайдера и модель.
11. Перехватывает исключение `PaymentRequiredError` и пытается использовать другого провайдера.
12. Если все провайдеры вызывают исключение `PaymentRequiredError`, вызывает последнее исключение.

```
A: Проверка наличия медиафайлов и выбор модели по умолчанию
|
B: Получение имени модели
|
C: Получение сопоставления модели и провайдера
|
D: Итерация по провайдерам
|
E: Формирование URL API
|
F: Проверка задачи провайдера
|
G: Вызов super().create_async_generator()
|
H: Обработка исключения PaymentRequiredError
|
I: Вызов исключения, если все провайдеры вызвали PaymentRequiredError
```

**Примеры**:

```python
import asyncio
from typing import List, Dict

Messages = List[Dict[str, str]]

async def main():
    messages: Messages = [{"role": "user", "content": "Hello, how are you?"}]
    generator = HuggingFaceAPI.create_async_generator(model="google/gemma-3-27b-it", messages=messages)
    async for chunk in generator:
        print(chunk)

asyncio.run(main())
```

### `calculate_lenght`

```python
def calculate_lenght(messages: Messages) -> int:\n    return sum([len(message["content"]) + 16 for message in messages])
```

**Назначение**: Подсчет длины сообщений.

**Параметры**:
- `messages` (Messages): Список сообщений, где каждое сообщение представляет собой словарь с ключом "content".

**Возвращает**:
- `int`: Суммарная длина всех сообщений, увеличенная на 16 для каждого сообщения.

**Как работает функция**:

1.  Вычисляет длину содержимого каждого сообщения в списке `messages` и добавляет к ней число 16.
2.  Суммирует полученные значения для всех сообщений.
3.  Возвращает общую сумму, представляющую собой оценку общей длины сообщений.

```
A: Вычисление длины содержимого каждого сообщения + 16
|
B: Суммирование полученных значений
|
C: Возврат общей суммы
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there"}]
total_length = calculate_lenght(messages)
print(total_length)  # Вывод: 21