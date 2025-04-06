# Модуль BlackForestLabs_Flux1Schnell

## Обзор

Модуль `BlackForestLabs_Flux1Schnell` предоставляет асинхронный интерфейс для взаимодействия с сервисом BlackForestLabs Flux-1-Schnell, предназначенным для генерации изображений на основе текстовых запросов. Этот модуль позволяет отправлять запросы к API BlackForestLabs и получать сгенерированные изображения.

## Подробнее

Модуль интегрируется с API BlackForestLabs Flux-1-Schnell через асинхронные HTTP-запросы. Он поддерживает настройку параметров генерации изображений, таких как размеры изображения, количество шагов inference и seed для воспроизводимости результатов. Модуль также обрабатывает ошибки, возвращаемые API, и предоставляет сгенерированные изображения в удобном формате.

## Классы

### `BlackForestLabs_Flux1Schnell`

**Описание**: Класс `BlackForestLabs_Flux1Schnell` является основным классом, предоставляющим функциональность для генерации изображений с использованием BlackForestLabs Flux-1-Schnell.

**Принцип работы**:
Класс наследует от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему асинхронно генерировать изображения и управлять моделями. Он определяет endpoint API, параметры моделей, а также методы для создания асинхронного генератора изображений.

**Атрибуты**:
- `label (str)`: Метка провайдера "BlackForestLabs Flux-1-Schnell".
- `url (str)`: URL сервиса BlackForestLabs Flux-1-Schnell.
- `api_endpoint (str)`: Endpoint API для отправки запросов на генерацию изображений.
- `working (bool)`: Указывает, что провайдер находится в рабочем состоянии.
- `default_model (str)`: Модель, используемая по умолчанию для генерации изображений.
- `default_image_model (str)`: Псевдоним для `default_model`.
- `model_aliases (dict)`: Словарь псевдонимов моделей.
- `image_models (list)`: Список поддерживаемых моделей изображений.
- `models (list)`: Список поддерживаемых моделей (совпадает с `image_models`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения изображений на основе текстового запроса.

## Функции

### `create_async_generator`

```python
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
        Создает асинхронный генератор для получения изображений на основе текстового запроса.

        Args:
            cls (BlackForestLabs_Flux1Schnell): Класс, для которого вызывается метод.
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений для формирования запроса.
            proxy (str, optional): Прокси-сервер для использования при подключении к API. По умолчанию `None`.
            prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            width (int, optional): Ширина изображения в пикселях. По умолчанию 768.
            height (int, optional): Высота изображения в пикселях. По умолчанию 768.
            num_inference_steps (int, optional): Количество шагов inference. По умолчанию 2.
            seed (int, optional): Seed для воспроизводимости результатов. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий изображения в формате `ImageResponse`.

        Raises:
            ResponseError: Если API возвращает ошибку.

        """
```

**Назначение**: Создает асинхронный генератор для получения изображений на основе текстового запроса.

**Параметры**:
- `cls (BlackForestLabs_Flux1Schnell)`: Класс, для которого вызывается метод.
- `model (str)`: Модель для генерации изображений.
- `messages (Messages)`: Список сообщений для формирования запроса.
- `proxy (str, optional)`: Прокси-сервер для использования при подключении к API. По умолчанию `None`.
- `prompt (str, optional)`: Текстовый запрос для генерации изображения. По умолчанию `None`.
- `width (int, optional)`: Ширина изображения в пикселях. По умолчанию 768.
- `height (int, optional)`: Высота изображения в пикселях. По умолчанию 768.
- `num_inference_steps (int, optional)`: Количество шагов inference. По умолчанию 2.
- `seed (int, optional)`: Seed для воспроизводимости результатов. По умолчанию 0.
- `randomize_seed (bool, optional)`: Флаг для рандомизации seed. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий изображения в формате `ImageResponse`.

**Вызывает исключения**:
- `ResponseError`: Если API возвращает ошибку.

**Как работает функция**:

1.  **Подготовка параметров**: Функция принимает параметры, такие как модель, сообщения, прокси, текстовый запрос, ширину и высоту изображения, количество шагов inference, seed и флаг рандомизации seed.
2.  **Форматирование запроса**: Формируется полезная нагрузка (payload) для запроса к API, включающая текстовый запрос, seed, флаг рандомизации seed, ширину и высоту изображения, а также количество шагов inference.
3.  **Отправка запроса и получение результата**: Функция отправляет POST-запрос к API endpoint с сформированной полезной нагрузкой, используя `aiohttp.ClientSession`.
4.  **Обработка ответа**: Функция ожидает ответа от API и обрабатывает его. Если API возвращает ошибку, вызывается исключение `ResponseError`.
5.  **Асинхронный генератор**: Если запрос успешен, функция возвращает асинхронный генератор, который выдает изображения в формате `ImageResponse`.

```ascii
    Настройка параметров -> Форматирование запроса
        |
        |
        V
    Отправка POST-запроса к API
        |
        |
        V
    Получение ответа от API
        |
        |
    +-----------------------+
    | Ошибка?              |
    +-----------------------+
        | Да                |
        V                   
    Вызов исключения ResponseError
        | Нет               |
        V                   
    Создание асинхронного генератора -> Выдача изображения в формате ImageResponse
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.BlackForestLabs_Flux1Schnell import BlackForestLabs_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "black-forest-labs-flux-1-schnell"
    messages: Messages = [{"role": "user", "content": "A beautiful landscape"}]
    
    generator = BlackForestLabs_Flux1Schnell.create_async_generator(model=model, messages=messages)
    
    async for image_response in generator:
        print(f"Image URL: {image_response.images[0]}")
        break

if __name__ == "__main__":
    asyncio.run(main())
```

```python
# Пример использования create_async_generator с прокси
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.BlackForestLabs_Flux1Schnell import BlackForestLabs_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "black-forest-labs-flux-1-schnell"
    messages: Messages = [{"role": "user", "content": "A futuristic city"}]
    proxy = "http://your_proxy:8080"
    
    generator = BlackForestLabs_Flux1Schnell.create_async_generator(model=model, messages=messages, proxy=proxy)
    
    async for image_response in generator:
        print(f"Image URL: {image_response.images[0]}")
        break

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример обработки исключения ResponseError
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.BlackForestLabs_Flux1Schnell import BlackForestLabs_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages
from src.endpoints.gpt4free.g4f.errors import ResponseError

async def main():
    model = "black-forest-labs-flux-1-schnell"
    messages: Messages = [{"role": "user", "content": "An impossible request"}]
    
    try:
        generator = BlackForestLabs_Flux1Schnell.create_async_generator(model=model, messages=messages)
        
        async for image_response in generator:
            print(f"Image URL: {image_response.images[0]}")
            break
    except ResponseError as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())