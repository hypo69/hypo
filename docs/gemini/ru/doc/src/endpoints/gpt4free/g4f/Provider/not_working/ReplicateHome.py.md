# Модуль для работы с Replicate Home API
===========================================

Модуль :mod:`ReplicateHome` предназначен для взаимодействия с API Replicate Home для генерации текста и изображений.
Он предоставляет асинхронный генератор для получения результатов.

## Обзор

Модуль предоставляет класс `ReplicateHome`, который является асинхронным провайдером, способным генерировать как текстовые, так и графические данные, используя различные модели, размещенные на платформе Replicate. Он поддерживает потоковую передачу результатов и использует `aiohttp` для асинхронных HTTP-запросов.

## Подробнее

Этот модуль позволяет взаимодействовать с ReplicateHome API для выполнения задач генерации текста и изображений. Он определяет несколько моделей, как текстовых, так и графических, и предоставляет удобные псевдонимы для упрощения выбора моделей. Модуль использует асинхронные запросы для неблокирующей работы и поддерживает потоковую передачу результатов, что позволяет получать данные по мере их генерации.

## Классы

### `ReplicateHome`

**Описание**: Класс `ReplicateHome` является асинхронным провайдером для взаимодействия с API Replicate Home.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL главной страницы Replicate.
- `api_endpoint` (str): URL API для создания предсказаний.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.
- `default_model` (str): Модель, используемая по умолчанию для генерации текста.
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `text_models` (List[str]): Список поддерживаемых моделей для генерации текста.
- `models` (List[str]): Объединенный список всех поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей для упрощения выбора.
- `model_versions` (Dict[str, str]): Словарь версий моделей для обеспечения воспроизводимости.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    prompt: str = None,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с API Replicate Home.

    Args:
        cls (Type[ReplicateHome]): Класс ReplicateHome.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для формирования запроса.
        prompt (str, optional): Текст запроса. Defaults to None.
        proxy (str, optional): URL прокси-сервера. Defaults to None.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий результаты от API.

    Raises:
        Exception: Если предсказание не удалось или истекло время ожидания.
        ValueError: Если получен неожиданный формат ответа.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Replicate Home.

**Параметры**:
- `cls` (Type[ReplicateHome]): Класс ReplicateHome.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Текст запроса. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты от API.

**Вызывает исключения**:
- `Exception`: Если предсказание не удалось или истекло время ожидания.
- `ValueError`: Если получен неожиданный формат ответа.

**Как работает функция**:

1. **Получение модели**:
   - Определяется, какую модель использовать, применяя псевдоним, если он предоставлен.
2. **Подготовка заголовков**:
   - Формируются заголовки HTTP-запроса, включая `content-type`, `origin`, `referer` и `user-agent`.
3. **Создание сессии**:
   - Создается асинхронная сессия `ClientSession` с заданными заголовками и прокси-сервером (если указан).
4. **Формирование запроса**:
   - Если `prompt` не указан, он формируется на основе `messages`. Для моделей изображений берется последнее сообщение, для текстовых моделей используется функция `format_prompt`.
   - Подготавливаются данные для запроса, включая название модели, версию и текст запроса (`prompt`).
5. **Отправка запроса**:
   - Отправляется POST-запрос к `api_endpoint` с данными в формате JSON.
   - Проверяется статус ответа с помощью `raise_for_status`.
   - Извлекается `prediction_id` из JSON-ответа.
6. **Опрос API**:
   - Выполняется серия опросов API по адресу `poll_url` для получения результата предсказания.
   - Максимальное количество попыток опроса – `max_attempts` (30).
   - Задержка между попытками – `delay` (5 секунд).
7. **Обработка результата**:
   - Если статус предсказания `succeeded`:
     - Для моделей изображений извлекается URL изображения и возвращается объект `ImageResponse`.
     - Для текстовых моделей возвращаются чанки текста.
   - Если статус предсказания `failed`, вызывается исключение с сообщением об ошибке.
8. **Обработка ошибок**:
   - Если после всех попыток статус не `succeeded`, вызывается исключение о превышении времени ожидания.
   - В случае неожиданного формата ответа вызывается исключение `ValueError`.

**Внутренние функции**:

- Внутри функции `create_async_generator` не определены внутренние функции.

**ASCII flowchart**:

```
    A (Получение модели)
    |
    B (Подготовка заголовков)
    |
    C (Создание сессии)
    |
    D (Формирование запроса)
    |
    E (Отправка POST-запроса)
    |
    F (Опрос API)
    |
    G (Обработка результата)
    |
    H (Завершен или ошибка)
```

**Примеры**:

Пример 1: Генерация текста с использованием модели `gemma-2b`:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.not_working.ReplicateHome import ReplicateHome
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    messages: Messages = [{"role": "user", "content": "Hello, how are you?"}]
    async_generator = await ReplicateHome.create_async_generator(model="gemma-2b", messages=messages)
    async for chunk in async_generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

Пример 2: Генерация изображения с использованием модели `stable-diffusion-3`:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.not_working.ReplicateHome import ReplicateHome
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    messages: Messages = [{"role": "user", "content": "A beautiful landscape"}]
    async_generator = await ReplicateHome.create_async_generator(model="sd-3", messages=messages)
    async for image_response in async_generator:
        print(image_response.image_url)

if __name__ == "__main__":
    asyncio.run(main())