# Модуль StabilityAI_SD35Large

## Обзор

Модуль `StabilityAI_SD35Large` предоставляет асинхронный генератор для взаимодействия с Stability AI SD-3.5-Large API. Он позволяет генерировать изображения на основе текстовых запросов, используя API Stability AI.
Модуль поддерживает настройку различных параметров генерации изображений, таких как соотношение сторон, размеры изображения, seed и другие.

## Подробнее

Этот модуль является частью набора инструментов для работы с различными моделями генерации изображений. Он предоставляет удобный интерфейс для асинхронного взаимодействия с API Stability AI, позволяя генерировать изображения на основе текстовых запросов. Модуль использует `aiohttp` для асинхронных HTTP-запросов и предоставляет функциональность для обработки ответов API, включая обработку ошибок и извлечение URL-адресов изображений.

## Классы

### `StabilityAI_SD35Large`

**Описание**: Класс `StabilityAI_SD35Large` предоставляет методы для взаимодействия с Stability AI SD-3.5-Large API для генерации изображений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общую функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("StabilityAI SD-3.5-Large").
- `url` (str): URL API ("https://stabilityai-stable-diffusion-3-5-large.hf.space").
- `api_endpoint` (str): Эндпоинт API ("/gradio_api/call/infer").
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ('stabilityai-stable-diffusion-3-5-large').
- `default_image_model` (str): Модель изображения по умолчанию.
- `model_aliases` (dict): Алиасы моделей ({"sd-3.5": default_model}).
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для генерации изображений.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls, model: str, messages: Messages,
        prompt: str = None,
        negative_prompt: str = None,
        api_key: str = None, 
        proxy: str = None,
        aspect_ratio: str = "1:1",
        width: int = None,
        height: int = None,
        guidance_scale: float = 4.5,
        num_inference_steps: int = 50,
        seed: int = 0,
        randomize_seed: bool = True,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для генерации изображений с использованием Stability AI SD-3.5-Large API.

        Args:
            cls (type): Класс, для которого вызывается метод.
            model (str): Используемая модель.
            messages (Messages): Список сообщений для формирования запроса.
            prompt (str, optional): Положительный запрос для генерации изображения. Defaults to None.
            negative_prompt (str, optional): Отрицательный запрос для генерации изображения. Defaults to None.
            api_key (str, optional): API ключ для доступа к Stability AI API. Defaults to None.
            proxy (str, optional): Адрес прокси-сервера. Defaults to None.
            aspect_ratio (str, optional): Соотношение сторон изображения. Defaults to "1:1".
            width (int, optional): Ширина изображения. Defaults to None.
            height (int, optional): Высота изображения. Defaults to None.
            guidance_scale (float, optional): Масштаб соответствия запросу. Defaults to 4.5.
            num_inference_steps (int, optional): Количество шагов для генерации изображения. Defaults to 50.
            seed (int, optional): Seed для генерации изображения. Defaults to 0.
            randomize_seed (bool, optional): Флаг для рандомизации seed. Defaults to True.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse`.

        Raises:
            ResponseError: Если превышен лимит токенов GPU.
            RuntimeError: Если не удалось разобрать URL изображения.
        """
        ...
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для взаимодействия с Stability AI SD-3.5-Large API. Она принимает различные параметры для настройки генерации изображений и возвращает асинхронный генератор, который выдает предварительные просмотры и окончательные изображения.

**Параметры**:
- `cls` (type): Класс, для которого вызывается метод.
- `model` (str): Используемая модель.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Положительный запрос для генерации изображения. По умолчанию `None`.
- `negative_prompt` (str, optional): Отрицательный запрос для генерации изображения. По умолчанию `None`.
- `api_key` (str, optional): API ключ для доступа к Stability AI API. По умолчанию `None`.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию `"1:1"`.
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `guidance_scale` (float, optional): Масштаб соответствия запросу. По умолчанию `4.5`.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию `50`.
- `seed` (int, optional): Seed для генерации изображения. По умолчанию `0`.
- `randomize_seed` (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse`.

**Вызывает исключения**:
- `ResponseError`: Если превышен лимит токенов GPU.
- `RuntimeError`: Если не удалось разобрать URL изображения.

**Как работает функция**:

1. **Подготовка заголовков**: Формируются заголовки запроса, включая `Content-Type` и `Authorization` (если предоставлен `api_key`).
2. **Создание сессии**: Создается асинхронная сессия `ClientSession` с заданными заголовками.
3. **Формирование запроса**: Формируется запрос на основе предоставленных параметров, включая `prompt`, `negative_prompt`, `seed`, `randomize_seed`, `width`, `height`, `guidance_scale` и `num_inference_steps`.
4. **Отправка запроса**: Отправляется POST-запрос к API Stability AI с сформированными данными.
5. **Обработка ответа**: Обрабатывается ответ от API, включая проверку на ошибки и извлечение `event_id`.
6. **Получение событий**: Отправляется GET-запрос для получения событий, связанных с `event_id`.
7. **Асинхронный стриминг**: Асинхронно обрабатываются чанки данных из ответа.
8. **Обработка событий**:
   - Если событие `error`, вызывается исключение `ResponseError`.
   - Если событие `generating`, извлекается URL изображения и возвращается объект `ImagePreview`.
   - Если событие `complete`, извлекается URL изображения и возвращается объект `ImageResponse`, после чего генератор завершает работу.

**ASII flowchart**:

```
   Подготовка заголовков и создание сессии
   ↓
   Формирование запроса
   ↓
   Отправка POST-запроса к API
   ↓
   Обработка ответа и извлечение event_id
   ↓
   Отправка GET-запроса для получения событий
   │
   Асинхронный стриминг чанков данных
   │
   Обработка событий:
   ├───> event == "error"  --> ResponseError
   ├───> event == "generating" --> ImagePreview
   └───> event == "complete"   --> ImageResponse --> Завершение
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, Optional, List

from ...typing import Messages
from .hf_space.StabilityAI_SD35Large import StabilityAI_SD35Large
from ...providers.response import ImageResponse, ImagePreview

async def main():
    model: str = "stabilityai-stable-diffusion-3-5-large"
    messages: Messages = [{"role": "user", "content": "A cat"}]
    prompt: str = "A cat in a hat"
    negative_prompt: str = "ugly, deformed"
    api_key: Optional[str] = None
    proxy: Optional[str] = None
    aspect_ratio: str = "1:1"
    width: Optional[int] = None
    height: Optional[int] = None
    guidance_scale: float = 4.5
    num_inference_steps: int = 50
    seed: int = 0
    randomize_seed: bool = True

    generator: AsyncGenerator[ImageResponse | ImagePreview, None] = StabilityAI_SD35Large.create_async_generator(
        model=model,
        messages=messages,
        prompt=prompt,
        negative_prompt=negative_prompt,
        api_key=api_key,
        proxy=proxy,
        aspect_ratio=aspect_ratio,
        width=width,
        height=height,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        seed=seed,
        randomize_seed=randomize_seed
    )

    async for item in generator:
        if isinstance(item, ImagePreview):
            print(f"Preview URL: {item.image_url}")
        elif isinstance(item, ImageResponse):
            print(f"Final URL: {item.image_url}")
            break

if __name__ == "__main__":
    asyncio.run(main())