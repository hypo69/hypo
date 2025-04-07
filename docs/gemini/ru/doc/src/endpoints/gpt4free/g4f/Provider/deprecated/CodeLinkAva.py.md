# Модуль CodeLinkAva

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с API CodeLinkAva.
Этот модуль предназначен для использования в проекте `hypotez` и обеспечивает подключение к API CodeLinkAva для генерации текста на основе предоставленных сообщений.

## Подробней

Модуль `CodeLinkAva` является провайдером асинхронных генераторов и использует `aiohttp` для выполнения асинхронных HTTP-запросов. Он предназначен для интеграции с API CodeLinkAva, который предоставляет функциональность генерации текста на основе входных сообщений.

Модуль определяет следующие основные компоненты:

- URL: URL-адрес API CodeLinkAva.
- Поддержка GPT-3.5 Turbo: Указывает, что провайдер поддерживает модель GPT-3.5 Turbo.
- Рабочее состояние: Указывает, находится ли провайдер в рабочем состоянии.
- Асинхронный генератор: Создает асинхронный генератор для получения ответов от API CodeLinkAva.

## Классы

### `CodeLinkAva`

**Описание**: Класс `CodeLinkAva` является асинхронным генератором провайдера, который взаимодействует с API CodeLinkAva для генерации текста.

**Принцип работы**:
1.  Класс устанавливает URL-адрес API CodeLinkAva.
2.  Поддерживает модель GPT-3.5 Turbo.
3.  Создает асинхронный генератор для получения ответов от API CodeLinkAva.

**Наследует**:

-   `AsyncGeneratorProvider`: Класс наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:

-   `url` (str): URL-адрес API CodeLinkAva.
-   `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5 Turbo.
-   `working` (bool): Флаг, указывающий на текущее состояние работоспособности провайдера.

**Методы**:

-   `create_async_generator`: Создает асинхронный генератор для взаимодействия с API CodeLinkAva.

## Функции

### `create_async_generator`

```python
    async def create_async_generator(
        cls,
        model: str,
        messages: list[dict[str, str]],
        **kwargs
    ) -> AsyncGenerator:
        """Создает асинхронный генератор для взаимодействия с API CodeLinkAva.

        Args:
            cls (type[CodeLinkAva]): Класс CodeLinkAva.
            model (str): Название модели для генерации текста.
            messages (list[dict[str, str]]): Список сообщений для отправки в API.
            **kwargs: Дополнительные параметры для отправки в API.

        Returns:
            AsyncGenerator: Асинхронный генератор, выдающий сгенерированный текст.

        Raises:
            aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.
            json.JSONDecodeError: Если не удается декодировать JSON-ответ от API.
            Exception: Если возникает любая другая ошибка в процессе генерации.

        """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который взаимодействует с API CodeLinkAva для генерации текста на основе предоставленных сообщений.

**Параметры**:

*   `cls` (type\[CodeLinkAva]): Класс `CodeLinkAva`, передается автоматически.
*   `model` (str): Имя модели, используемой для генерации текста.
*   `messages` (list\[dict\[str, str]]): Список сообщений, отправляемых в API для генерации ответа.
*   `**kwargs`: Дополнительные параметры, которые будут переданы в API (например, параметры температуры).

**Возвращает**:

*   `AsyncGenerator`: Асинхронный генератор, который выдает сгенерированный текст.

**Вызывает исключения**:

*   `aiohttp.ClientResponseError`: Если HTTP-запрос к API завершается с ошибкой (например, ошибка сервера).
*   `json.JSONDecodeError`: Если не удается декодировать JSON-ответ, полученный от API.
*   `Exception`: В случае возникновения других ошибок в процессе генерации текста.

**Как работает функция**:

1.  **Формирование заголовков HTTP-запроса**: Функция создает заголовки HTTP-запроса, включая User-Agent, Accept, Accept-Language, Origin, Referer, Sec-Fetch-Dest, Sec-Fetch-Mode и Sec-Fetch-Site.

2.  **Создание сессии aiohttp**: Функция создает асинхронную сессию `aiohttp.ClientSession` с использованием сформированных заголовков.

3.  **Формирование данных запроса**: Функция формирует данные запроса, включая сообщения, температуру и другие параметры.

4.  **Отправка POST-запроса к API**: Функция отправляет POST-запрос к API CodeLinkAva с использованием созданной сессии и сформированных данных.

5.  **Обработка ответа от API**: Функция обрабатывает ответ от API, проверяя статус ответа и извлекая сгенерированный текст из JSON-ответа.

6.  **Генерация текста**: Функция выдает сгенерированный текст в виде асинхронного генератора.

7.  **Завершение работы**: Функция закрывает асинхронную сессию после завершения работы.

```text
    Начало
    │
    ├───  Установка заголовков HTTP-запроса
    │    │
    │    └──  Создание сессии aiohttp
    │         │
    │         └──  Формирование данных запроса (messages, temperature, stream, kwargs)
    │              │
    │              └──  Отправка POST-запроса к API CodeLinkAva
    │                   │
    │                   └──  Обработка ответа от API
    │                        │
    │                        └──  Извлечение сгенерированного текста из JSON-ответа
    │                             │
    │                             └──  Выдача сгенерированного текста через асинхронный генератор
    │                                  │
    │                                  └──  Закрытие асинхронной сессии
    │
    └──  Конец
```

**Примеры**:

```python
# Пример использования функции create_async_generator
import asyncio
from CodeLinkAva import CodeLinkAva

async def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for message in CodeLinkAva.create_async_generator(model="gpt-3.5-turbo", messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример использования с дополнительными параметрами
import asyncio
from CodeLinkAva import CodeLinkAva

async def main():
    messages = [{"role": "user", "content": "Tell me a joke."}]
    kwargs = {"temperature": 0.8}
    async for message in CodeLinkAva.create_async_generator(model="gpt-3.5-turbo", messages=messages, **kwargs):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```