# Модуль для работы с FlowGpt
===========================

Модуль содержит класс `FlowGpt`, который предоставляет асинхронный генератор для взаимодействия с различными моделями через FlowGPT API.

## Обзор

Этот модуль позволяет взаимодействовать с различными моделями, такими как `gpt-3.5-turbo`, `gpt-4-turbo`, `google-gemini` и другими, используя API FlowGPT. Он поддерживает историю сообщений и системные сообщения, что позволяет создавать более контекстно-зависимые ответы.

## Подробнее

Модуль использует `aiohttp` для выполнения асинхронных HTTP-запросов к API FlowGPT. Он также включает логику для формирования заголовков запроса, включая подпись, и обработки ответов в режиме реального времени.

## Классы

### `FlowGpt`

**Описание**: Класс `FlowGpt` является асинхронным генератором провайдера и предоставляет методы для взаимодействия с API FlowGPT.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Добавляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL для взаимодействия с FlowGPT API (`https://flowgpt.com/chat`).
- `working` (bool): Указывает, работает ли провайдер. В данном случае всегда `False`.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-3.5-turbo`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от FlowGPT API.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    temperature: float = 0.7,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от FlowGPT API.

    Args:
        cls (FlowGpt): Ссылка на класс.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        temperature (float, optional): Температура для генерации ответов. По умолчанию `0.7`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от FlowGPT API.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с API.
    """
```

**Назначение**: Создает асинхронный генератор для получения ответов от FlowGPT API.

**Параметры**:
- `cls` (FlowGpt): Ссылка на класс.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `temperature` (float, optional): Температура для генерации ответов. По умолчанию `0.7`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от FlowGPT API.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с API.

**Как работает функция**:
1. **Получение модели**: Извлекает имя модели, используя `cls.get_model(model)`. Если передан псевдоним модели (например, "gemini"), он будет заменен на полное имя ("google-gemini").
2. **Формирование заголовков**:
   - Генерирует `timestamp`, `nonce` и `signature` для аутентификации.
   - Создает словарь `headers` с необходимыми HTTP-заголовками, включая User-Agent, Content-Type и Authorization.
3. **Подготовка данных**:
   - Извлекает историю сообщений из `messages`, исключая системные сообщения.
   - Формирует системное сообщение, объединяя все сообщения с ролью "system". Если системные сообщения отсутствуют, используется сообщение по умолчанию: "You are helpful assistant. Follow the user's instructions carefully." (Ты полезный помощник. Внимательно следуйте инструкциям пользователя.).
   - Создает словарь `data` с данными для отправки в API, включая модель, вопрос, историю сообщений, системное сообщение и температуру.
4. **Отправка запроса и обработка ответа**:
   - Использует `aiohttp.ClientSession` для отправки POST-запроса к API FlowGPT.
   - Обрабатывает ответ по частям (`chunk`) и извлекает текстовые данные из каждого чанка.
   - Для каждого чанка проверяет наличие события "text" и извлекает данные (`message["data"]`).
   - Генерирует текстовые данные, полученные из API.

```
A: Получение модели
|
B: Формирование заголовков
|
C: Подготовка данных
|
D: Отправка запроса и обработка ответа
|
E: Генерация данных
```

**Внутренние функции**: Нет

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

async def main():
    model: str = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Привет!"}
    ]
    proxy: Optional[str] = None
    temperature: float = 0.7

    async def process_generator(generator: AsyncGenerator[str, None]):
        async for message in generator:
            print(f"Message: {message}")

    generator: AsyncGenerator[str, None] = await FlowGpt.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        temperature=temperature
    )

    await process_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример 2 с использованием системного сообщения:
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

async def main():
    model: str = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": "Ты - полезный ассистент."},
        {"role": "user", "content": "Привет!"}
    ]
    proxy: Optional[str] = None
    temperature: float = 0.7

    async def process_generator(generator: AsyncGenerator[str, None]):
        async for message in generator:
            print(f"Message: {message}")

    generator: AsyncGenerator[str, None] = await FlowGpt.create_async_generator(
        model=model,
        messages=messages,
        proxy=proxy,
        temperature=temperature
    )

    await process_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())