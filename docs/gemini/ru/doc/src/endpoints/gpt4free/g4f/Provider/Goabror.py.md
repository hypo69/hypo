# Модуль Goabror

## Обзор

Модуль `Goabror` предоставляет асинхронный генератор для взаимодействия с API `goabror.uz`. Он позволяет отправлять запросы к API и получать ответы в виде асинхронного генератора текста. Модуль использует библиотеку `aiohttp` для асинхронных HTTP-запросов и предназначен для работы с моделью `gpt-4`.

## Подробней

Модуль предназначен для интеграции с сервисом `goabror.uz`, предоставляющим доступ к языковой модели `gpt-4`. Он выполняет следующие функции:

1.  Форматирует запросы в соответствии с требованиями API `goabror.uz`.
2.  Отправляет асинхронные запросы к API с использованием `aiohttp`.
3.  Обрабатывает ответы API, возвращая их в виде асинхронного генератора.
4.  Обеспечивает обработку ошибок и исключений при взаимодействии с API.

Этот модуль является частью проекта `hypotez` и используется для обеспечения взаимодействия с внешним сервисом `goabror.uz`. Он предоставляет удобный интерфейс для отправки запросов и получения ответов в асинхронном режиме, что позволяет эффективно использовать ресурсы и обеспечивает высокую производительность.

## Классы

### `Goabror`

**Описание**: Класс `Goabror` является асинхронным провайдером и предоставляет методы для взаимодействия с API `goabror.uz`.

**Наследует**:

*   `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, возвращающих результаты в виде генератора.
*   `ProviderModelMixin`: Предоставляет общие методы для работы с моделями, такими как `default_model` и `models`.

**Атрибуты**:

*   `url` (str): URL веб-сайта `goabror.uz`.
*   `api_endpoint` (str): URL API для взаимодействия с `goabror.uz`.
*   `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `True`).
*   `default_model` (str): Модель, используемая по умолчанию (`gpt-4`).
*   `models` (list): Список поддерживаемых моделей (в данном случае `[default_model]`).

**Методы**:

*   `create_async_generator()`: Создает асинхронный генератор для получения ответов от API `goabror.uz`.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API goabror.uz.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.
    """
```

**Назначение**:
Метод `create_async_generator` создает асинхронный генератор, который отправляет запросы к API `goabror.uz` и возвращает ответы в виде последовательности текстовых фрагментов.

**Параметры**:

*   `cls`: Ссылка на класс `Goabror`.
*   `model` (str): Модель для использования (например, `gpt-4`).
*   `messages` (Messages): Список сообщений, которые будут отправлены в API.
*   `proxy` (str, optional): URL прокси-сервера для использования при отправке запроса. По умолчанию `None`.
*   `**kwargs`: Дополнительные именованные аргументы, которые могут быть переданы в функцию (не используются в данной реализации).

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор, который при итерации возвращает текстовые фрагменты от API `goabror.uz`.

**Вызывает исключения**:

*   `aiohttp.ClientResponseError`: Если HTTP-ответ содержит код ошибки (например, 400, 500).
*   `json.JSONDecodeError`: Если ответ от API не является корректным JSON.
*   `Exception`: В случае других ошибок при выполнении запроса.

**Как работает функция**:

1.  **Подготовка заголовков**:
    - Функция начинает с определения заголовков HTTP-запроса, включая `accept`, `accept-language` и `user-agent`.

2.  **Создание асинхронной сессии**:
    - Затем создается асинхронная сессия `aiohttp.ClientSession` с заданными заголовками.

3.  **Формирование параметров запроса**:
    - Формируются параметры запроса `params`, включающие `user` (содержимое сообщений пользователя) и `system` (системное сообщение).

4.  **Выполнение GET-запроса**:
    - Выполняется GET-запрос к API-endpoint (`cls.api_endpoint`) с использованием асинхронной сессии, параметров запроса и прокси-сервера (если указан).

5.  **Обработка ответа**:
    - После получения ответа проверяется его статус с помощью `raise_for_status(response)`, что вызывает исключение в случае ошибки HTTP.

6.  **Извлечение текста ответа**:
    - Извлекается текст ответа с помощью `await response.text()`.

7.  **Обработка JSON-ответа**:
    - Предпринимается попытка декодирования текста ответа как JSON.

8.  **Генерация данных**:
    - Если декодирование JSON успешно, и в JSON-ответе присутствует ключ `data`, функция генерирует значение этого ключа.
    - Если декодирование JSON не удалось или ключ `data` отсутствует, функция генерирует текст ответа как есть.

```text
    Начало
    │
    ├── Заголовки HTTP (accept, accept-language, user-agent)
    │
    ├── Создание асинхронной сессии aiohttp.ClientSession
    │
    ├── Формирование параметров запроса (user, system)
    │
    ├── GET-запрос к API-endpoint
    │
    ├── Проверка статуса ответа raise_for_status(response)
    │
    ├── Извлечение текста ответа
    │
    ├── Попытка декодирования JSON
    │   └── Успешно: Проверка наличия ключа "data"
    │       ├── Ключ "data" присутствует: Генерация значения ключа
    │       └── Ключ "data" отсутствует: Генерация текста ответа
    │   └── Ошибка: Генерация текста ответа
    │
    └── Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict

async def main():
    model = "gpt-4"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "system", "content": "I am doing well, thank you!"}
    ]
    proxy = None

    async for message in Goabror.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
```

В этом примере `create_async_generator` вызывается с моделью `gpt-4`, списком сообщений и без прокси-сервера. Затем асинхронно перебираются сообщения, возвращаемые генератором, и выводятся на экран.