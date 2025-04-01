# Модуль Vitalentum

## Обзор

Модуль `Vitalentum` предоставляет асинхронный генератор для взаимодействия с API Vitalentum, который использует модель GPT-3.5 Turbo. Он позволяет получать ответы от модели в виде асинхронного потока данных.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для работы с одним из провайдеров GPT4Free. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов к API Vitalentum. Модуль определяет класс `Vitalentum`, который наследуется от `AsyncGeneratorProvider` и реализует метод `create_async_generator` для создания асинхронного генератора ответов.

## Классы

### `Vitalentum`

**Описание**: Класс для взаимодействия с API Vitalentum и получения ответов от модели GPT-3.5 Turbo в виде асинхронного генератора.

**Наследует**:
- `AsyncGeneratorProvider`: Класс, предоставляющий базовый интерфейс для асинхронных провайдеров генераторов.

**Атрибуты**:
- `url` (str): URL API Vitalentum.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5 Turbo.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API Vitalentum.

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
        Создает асинхронный генератор для получения ответов от API Vitalentum.

        Args:
            model (str): Название модели, используемой для генерации ответа.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы для передачи в API.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий текст ответа от API Vitalentum.

        Raises:
            aiohttp.ClientResponseError: Если возникает ошибка при выполнении HTTP-запроса.

        """
```

**Назначение**: Создает асинхронный генератор для получения ответов от API Vitalentum.

**Параметры**:
- `cls`: Ссылка на класс `Vitalentum`.
- `model` (str): Название модели, используемой для генерации ответа.
- `messages` (Messages): Список сообщений для отправки в API. Сообщения должны быть в формате, совместимом с API Vitalentum.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для передачи в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст ответа от API Vitalentum.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Если возникает ошибка при выполнении HTTP-запроса.

**Как работает функция**:

1. **Формирование заголовков**: Создаются заголовки HTTP-запроса, включая User-Agent, Accept, Origin, Referer и другие.
2. **Преобразование сообщений**: Список сообщений преобразуется в формат JSON, ожидаемый API Vitalentum. Роль "user" преобразуется в "human", а роль "bot" остается "bot".
3. **Формирование данных запроса**: Данные запроса формируются в виде словаря, включающего преобразованные сообщения, температуру и дополнительные аргументы.
4. **Выполнение асинхронного запроса**: Используется `aiohttp.ClientSession` для выполнения асинхронного POST-запроса к API Vitalentum.
5. **Обработка ответа**: Ответ от API обрабатывается построчно. Если строка начинается с "data: ", она интерпретируется как часть ответа. Если строка содержит "[DONE]", генерация завершается. Полученные данные преобразуются из JSON и извлекается содержимое.
6. **Генерация ответа**: Извлеченное содержимое передается в генератор для последующего использования.

**Внутренние функции**:
- Нет

**ASCII flowchart**:

```
A: Формирование заголовков и данных запроса
|
B: Выполнение POST-запроса к API Vitalentum
|
C: Обработка ответа построчно
|
D: Проверка на "data: " и "[DONE]"
|
E: Извлечение содержимого из JSON
|
F: Генерация содержимого
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, how are you?"}
    ]

    async def print_generator(generator: AsyncGenerator[str, None]):
        async for chunk in generator:
            print(chunk, end="")

    generator = Vitalentum.create_async_generator(model=model, messages=messages)
    await print_generator(await generator)

if __name__ == "__main__":
    asyncio.run(main())