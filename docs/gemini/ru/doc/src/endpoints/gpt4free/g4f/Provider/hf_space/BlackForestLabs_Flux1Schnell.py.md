# Модуль BlackForestLabs_Flux1Schnell

## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с моделью BlackForestLabs Flux-1-Schnell, размещенной на платформе Hugging Face Spaces. Он позволяет генерировать изображения на основе текстовых запросов, используя API Hugging Face Spaces.

## Подробнее

Этот модуль предоставляет класс `BlackForestLabs_Flux1Schnell`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов к API Hugging Face Spaces. Модуль поддерживает настройку параметров генерации изображений, таких как ширина, высота, количество шагов логического вывода и начальное значение seed. Он обрабатывает ответы от API, проверяет наличие ошибок и возвращает URL-адреса сгенерированных изображений.

## Классы

### `BlackForestLabs_Flux1Schnell`

**Описание**: Класс для взаимодействия с моделью BlackForestLabs Flux-1-Schnell через API Hugging Face Spaces.
**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, `"BlackForestLabs Flux-1-Schnell"`.
- `url` (str): URL главной страницы Hugging Face Space, `"https://black-forest-labs-flux-1-schnell.hf.space"`.
- `api_endpoint` (str): URL API для вызова логического вывода, `"https://black-forest-labs-flux-1-schnell.hf.space/call/infer"`.
- `working` (bool): Указывает, работает ли провайдер, `True`.
- `default_model` (str): Модель по умолчанию, `"black-forest-labs-flux-1-schnell"`.
- `default_image_model` (str): Модель изображения по умолчанию, совпадает с `default_model`.
- `model_aliases` (dict): Псевдонимы моделей, `{"flux-schnell": default_image_model, "flux": default_image_model}`.
- `image_models` (list): Список моделей изображений, полученный из ключей `model_aliases`.
- `models` (list): Список моделей, совпадает с `image_models`.

#### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        prompt: str = None,
        width: int = 768,
        height: int = 768,
        num_inference_steps: int = 2,
        seed: int = 0,
        randomize_seed: bool = True,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для генерации изображений на основе текстового запроса.

        Args:
            model (str): Имя модели для генерации изображений.
            messages (Messages): Список сообщений, используемых для формирования запроса.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            prompt (str, optional): Дополнительный текст запроса. По умолчанию `None`.
            width (int, optional): Ширина изображения в пикселях. По умолчанию 768.
            height (int, optional): Высота изображения в пикселях. По умолчанию 768.
            num_inference_steps (int, optional): Количество шагов логического вывода. По умолчанию 2.
            seed (int, optional): Начальное значение seed для генерации случайных чисел. По умолчанию 0.
            randomize_seed (bool, optional): Флаг, указывающий, нужно ли рандомизировать seed. По умолчанию `True`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий объекты `ImageResponse` с URL-адресами сгенерированных изображений.

        Raises:
            ResponseError: Если при генерации изображения произошла ошибка.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для получения изображений от модели `BlackForestLabs_Flux1Schnell`.

**Параметры**:
- `cls` (class): Ссылка на класс `BlackForestLabs_Flux1Schnell`.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для генерации изображения.
- `proxy` (str, optional): URL прокси-сервера, если требуется. По умолчанию `None`.
- `prompt` (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `width` (int, optional): Ширина генерируемого изображения. По умолчанию 768.
- `height` (int, optional): Высота генерируемого изображения. По умолчанию 768.
- `num_inference_steps` (int, optional): Количество шагов для логического вывода. По умолчанию 2.
- `seed` (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг, указывающий, нужно ли рандомизировать зерно. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий объекты `ImageResponse` с URL-адресами сгенерированных изображений.

**Вызывает исключения**:
- `ResponseError`: Если при генерации изображения произошла ошибка.

**Как работает функция**:

1. **Подготовка параметров**: Функция корректирует значения `width` и `height`, чтобы они были кратны 8, и форматирует запрос `prompt` с использованием предоставленных сообщений `messages`.
2. **Формирование payload**: Создается словарь `payload` с данными, необходимыми для запроса к API, включая текст запроса, seed, размеры изображения и количество шагов логического вывода.
3. **Асинхронный HTTP-запрос**: Используется `aiohttp.ClientSession` для отправки POST-запроса к API Hugging Face Space.
4. **Обработка ответа**: Функция ожидает ответа от API и обрабатывает его, получая `event_id` для дальнейшего отслеживания статуса генерации изображения.
5. **Получение статуса генерации**: В цикле отправляются GET-запросы к API для получения статуса генерации изображения. Ответы обрабатываются построчно, и извлекаются данные о событиях.
6. **Обработка событий**: Функция проверяет тип события (`error` или `complete`). В случае ошибки выбрасывается исключение `ResponseError`. В случае завершения генерации извлекается URL-адрес изображения и возвращается объект `ImageResponse`.

**ASCII Flowchart**:

```
    Начало
      ↓
    Подготовка параметров
      ↓
    Формирование payload
      ↓
    Отправка POST-запроса к API
      ↓
    Получение event_id
      ↓
    Начало цикла получения статуса
      ↓
    Отправка GET-запроса для получения статуса
      ↓
    Обработка ответа
      │
    Проверка типа события
      │
    ┌───────┴───────┐
    │       Error     │       Complete   │
    │       ResponseError     │       Извлечение URL-адреса изображения   │
    │                │                │
    └───→ Выход      └───→ Создание ImageResponse → Выход
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List, Optional, Dict, Any

from g4f.providers.response import ImageResponse
from g4f.client import Client
from g4f.models import Model, model_to_provider

async def main():
    model: Model = Model.open_journey_v4
    messages: List[Dict[str, str]] = [{"role": "user", "content": "A cat"}]
    provider = model_to_provider(model)
    generator: AsyncGenerator[ImageResponse, Any] = await provider.create_async_generator(
        model=model.name,
        messages=messages
    )
    image_response: ImageResponse = await generator.__anext__()
    print(image_response.images)

asyncio.run(main())

# async def process_image(prompt:str):
#     provider = BlackForestLabs_Flux1Schnell()
#     generator: AsyncGenerator[ImageResponse, Any] = await provider.create_async_generator(
#         model=provider.default_image_model,
#         messages=[{"role": "user", "content": prompt}]
#     )
#     image_response: ImageResponse = await generator.__anext__()
#     print(image_response.images)
#
# asyncio.run(process_image("cat"))
```