# Модуль Voodoohop_Flux1Schnell

## Обзор

Модуль `Voodoohop_Flux1Schnell` предоставляет асинхронный генератор для создания изображений с использованием API Voodoohop Flux-1-Schnell. Он позволяет генерировать изображения на основе текстовых запросов, используя Hugging Face Space.

## Подробней

Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется генерация изображений на основе текстовых описаний. Он использует асинхронные запросы для взаимодействия с API Voodoohop Flux-1-Schnell и предоставляет возможность настройки параметров генерации изображений, таких как размеры, количество шагов и начальное зерно.

## Классы

### `Voodoohop_Flux1Schnell`

**Описание**: Класс `Voodoohop_Flux1Schnell` является поставщиком (provider) для генерации изображений через API Voodoohop Flux-1-Schnell. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему асинхронно генерировать изображения и предоставлять информацию о поддерживаемых моделях.

**Принцип работы**:
Класс определяет URL API, рабочее состояние, модель по умолчанию и псевдонимы моделей. Основная функциональность заключается в методе `create_async_generator`, который принимает параметры генерации изображения, формирует запрос к API и возвращает асинхронный генератор, выдающий URL сгенерированных изображений.

**Атрибуты**:
- `label` (str): Метка провайдера ("Voodoohop Flux-1-Schnell").
- `url` (str): URL Hugging Face Space ("https://voodoohop-flux-1-schnell.hf.space").
- `api_endpoint` (str): URL API ("https://voodoohop-flux-1-schnell.hf.space/call/infer").
- `working` (bool): Флаг, указывающий, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ("voodoohop-flux-1-schnell").
- `default_image_model` (str): Модель изображения по умолчанию, соответствует `default_model`.
- `model_aliases` (dict): Псевдонимы моделей ({"flux-schnell": default_model, "flux": default_model}).
- `image_models` (list): Список моделей изображений, полученный из ключей `model_aliases`.
- `models` (list): Список моделей, соответствует `image_models`.

**Методы**:
- `create_async_generator`: Асинхронно генерирует изображения на основе заданных параметров.

## Функции

### `create_async_generator`

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
    """
    Асинхронно генерирует изображения на основе заданных параметров, используя API Voodoohop Flux-1-Schnell.

    Args:
        cls: Класс, к которому принадлежит метод.
        model (str): Используемая модель.
        messages (Messages): Список сообщений для формирования запроса.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
        width (int, optional): Ширина изображения. По умолчанию 768.
        height (int, optional): Высота изображения. По умолчанию 768.
        num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 2.
        seed (int, optional): Начальное зерно для генерации. По умолчанию 0.
        randomize_seed (bool, optional): Флаг, указывающий, нужно ли рандомизировать зерно. По умолчанию `True`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий URL сгенерированных изображений.

    Raises:
        ResponseError: Если при генерации изображения произошла ошибка.

    """
    ...
```

**Назначение**: Метод `create_async_generator` создает и возвращает асинхронный генератор, который взаимодействует с API Voodoohop Flux-1-Schnell для генерации изображений на основе заданных параметров.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Модель для генерации изображения.
- `messages` (Messages): Список сообщений, используемых для формирования запроса.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `prompt` (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `width` (int, optional): Ширина изображения. По умолчанию 768.
- `height` (int, optional): Высота изображения. По умолчанию 768.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию 2.
- `seed` (int, optional): Зерно для генерации изображения. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг рандомизации зерна. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий URL сгенерированных изображений.

**Вызывает исключения**:
- `ResponseError`: Если при генерации изображения произошла ошибка.

**Как работает функция**:

1.  **Подготовка параметров**: Функция принимает параметры, необходимые для генерации изображения, и форматирует их.
2.  **Формирование полезной нагрузки (payload)**: Создается словарь `payload` с данными, необходимыми для запроса к API.
3.  **Асинхронный запрос к API**: Используется `ClientSession` для отправки POST-запроса к API Voodoohop Flux-1-Schnell с сформированной полезной нагрузкой.
4.  **Обработка ответа**: После успешного запроса извлекается `event_id` из ответа.
5.  **Цикл ожидания завершения генерации**: В цикле отправляются GET-запросы к API для получения статуса генерации изображения.
6.  **Обработка событий**: Полученные события обрабатываются. Если приходит событие `error`, выбрасывается исключение `ResponseError`. Если приходит событие `complete`, извлекается URL изображения и возвращается в виде `ImageResponse`.
7.  **Возврат результата**: Асинхронный генератор выдает URL сгенерированного изображения.

```
   Начало
     ↓
   Подготовка параметров (ширина, высота, запрос)
     ↓
   Формирование payload
     ↓
   Отправка POST-запроса к API
     ↓
   Получение event_id
     ↓
   Начало цикла ожидания
     ↓
   Отправка GET-запроса для получения статуса
     ↓
   Обработка события
     ├── event == error? -> Выброс ResponseError
     └── event == complete? -> Извлечение URL изображения, возврат ImageResponse
     ↓
   Конец цикла ожидания / Завершение
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, Optional, List, Dict

from aiohttp import ClientSession

from ...typing import Messages
from ...providers.response import ImageResponse
from ...errors import ResponseError
from ...requests.raise_for_status import raise_for_status
from ..helper import format_image_prompt
from ..base_provider import AsyncGeneratorProvider, ProviderModelMixin


class Voodoohop_Flux1Schnell(AsyncGeneratorProvider, ProviderModelMixin):
    label: str = "Voodoohop Flux-1-Schnell"
    url: str = "https://voodoohop-flux-1-schnell.hf.space"
    api_endpoint: str = "https://voodoohop-flux-1-schnell.hf.space/call/infer"

    working: bool = True

    default_model: str = "voodoohop-flux-1-schnell"
    default_image_model: str = default_model
    model_aliases: Dict[str, str] = {"flux-schnell": default_model, "flux": default_model}
    image_models: List[str] = list(model_aliases.keys())
    models: List[str] = image_models


    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: Optional[str] = None,
        prompt: Optional[str] = None,
        width: int = 768,
        height: int = 768,
        num_inference_steps: int = 2,
        seed: int = 0,
        randomize_seed: bool = True,
        **kwargs
    ) -> AsyncGenerator[ImageResponse, None]:
        width = max(32, width - (width % 8))
        height = max(32, height - (height % 8))
        prompt = format_image_prompt(messages, prompt)
        payload = {
            "data": [
                prompt,
                seed,
                randomize_seed,
                width,
                height,
                num_inference_steps
            ]
        }
        async with ClientSession() as session:
            async with session.post(cls.api_endpoint, json=payload, proxy=proxy) as response:
                await raise_for_status(response)
                response_data = await response.json()
                event_id = response_data['event_id']
                while True:
                    async with session.get(f"{cls.api_endpoint}/{event_id}", proxy=proxy) as status_response:
                        await raise_for_status(status_response)
                        while not status_response.content.at_eof():
                            event = await status_response.content.readuntil(b'\n\n')
                            if event.startswith(b'event:'):
                                event_parts = event.split(b'\ndata: ')
                                if len(event_parts) < 2:
                                    continue
                                event_type = event_parts[0].split(b': ')[1]
                                data = event_parts[1]
                                if event_type == b'error':
                                    raise ResponseError(f"Error generating image: {data}")
                                elif event_type == b'complete':
                                    json_data = json.loads(data)
                                    image_url = json_data[0]['url']
                                    yield ImageResponse(images=[image_url], alt=prompt)
                                    return

# Пример вызова функции
async def main():
    messages: Messages = [{"role": "user", "content": "A cat wearing a hat"}]
    generator = Voodoohop_Flux1Schnell.create_async_generator(
        model="voodoohop-flux-1-schnell",
        messages=messages,
        width=512,
        height=512
    )
    async for image_response in await generator:
        print(f"Image URL: {image_response.images[0]}")

if __name__ == "__main__":
    asyncio.run(main())