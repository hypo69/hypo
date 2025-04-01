# Модуль `AI365VIP`

## Обзор

Модуль предназначен для взаимодействия с провайдером AI365VIP для получения ответов от языковых моделей, таких как GPT-3.5 Turbo и GPT-4o. Он использует асинхронные запросы для генерации текста на основе предоставленных сообщений.

## Подробней

Модуль предоставляет класс `AI365VIP`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он позволяет отправлять запросы к API AI365VIP и получать ответы в виде асинхронного генератора.

## Классы

### `AI365VIP`

**Описание**: Класс для взаимодействия с AI365VIP.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса AI365VIP.
- `api_endpoint` (str): Эндпоинт API для чата.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-3.5-turbo`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от AI365VIP.

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
    """Создает асинхронный генератор для получения ответов от AI365VIP.

    Args:
        cls (Type[AI365VIP]): Класс AI365VIP.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от AI365VIP.

    Raises:
        aiohttp.ClientResponseError: Если HTTP-запрос завершается с ошибкой.

    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API AI365VIP и получения ответов.

**Параметры**:
- `cls` (Type[AI365VIP]): Класс AI365VIP.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от AI365VIP.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.

**Как работает функция**:

1. **Подготовка заголовков**: Функция создает заголовки HTTP-запроса, включая User-Agent, Content-Type и другие необходимые параметры.
2. **Создание сессии**: Используется `aiohttp.ClientSession` для выполнения асинхронных HTTP-запросов.
3. **Формирование данных**: Создается словарь `data`, содержащий информацию о модели, сообщениях и других параметрах запроса. Сообщения форматируются с использованием `format_prompt`.
4. **Отправка запроса**: Отправляется POST-запрос к API AI365VIP с использованием `session.post`.
5. **Обработка ответа**: Полученный ответ обрабатывается по частям (chunks) и декодируется. Каждый чанк ответа передается через `yield`, что позволяет использовать функцию в качестве асинхронного генератора.

```
  Начало
  ↓
  Заголовки запроса  →  Создание сессии aiohttp
  ↓
  Формирование данных (модель, сообщения)
  ↓
  Отправка POST-запроса к API AI365VIP
  ↓
  Обработка ответа (по частям)
  ↓
  Выдача чанков ответа через yield
  ↓
  Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List

# Для запуска примера требуется настроенный асинхронный event loop

async def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    model = "gpt-3.5-turbo"

    async def consume_generator(generator: AsyncGenerator[str, None]):
        async for chunk in generator:
            print(chunk, end="")

    generator = AI365VIP.create_async_generator(model=model, messages=messages)
    if generator:
        await consume_generator(generator)
    else:
        print("Failed to create generator.")

if __name__ == "__main__":
    asyncio.run(main())