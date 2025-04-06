# Модуль `Prodia`

## Обзор

Модуль `Prodia` предназначен для взаимодействия с API сервиса Prodia для генерации изображений на основе текстовых запросов. Он предоставляет асинхронные функции для отправки запросов к API Prodia и получения сгенерированных изображений. Модуль поддерживает выбор различных моделей, задание параметров генерации и обработку ошибок.

## Подробнее

Модуль `Prodia` асинхронно взаимодействует с API Prodia для генерации изображений. Он использует `aiohttp` для асинхронных HTTP-запросов.
Класс `Prodia` является подклассом `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему использовать общую логику для асинхронных провайдеров и моделей.

## Классы

### `Prodia`

**Описание**: Класс для взаимодействия с API Prodia для генерации изображений.

**Принцип работы**:
Класс использует асинхронные запросы к API Prodia для генерации изображений на основе заданных параметров, таких как модель, текст запроса, негативный промпт и другие параметры генерации.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных провайдеров, генерирующих результаты.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса Prodia.
- `api_endpoint` (str): URL API для генерации изображений.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `default_image_model` (str): Псевдоним для `default_model`.
- `image_models` (List[str]): Список доступных моделей для генерации изображений.
- `models` (List[str]): Список всех доступных моделей (в данном случае совпадает с `image_models`).

**Методы**:
- `get_model(model: str) -> str`: Возвращает имя модели, используемой для генерации изображений.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, negative_prompt: str = "", steps: str = 20, cfg: str = 7, seed: Optional[int] = None, sampler: str = "DPM++ 2M Karras", aspect_ratio: str = "square", **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения изображений от API Prodia.
- `_poll_job(session: ClientSession, job_id: str, proxy: str, max_attempts: int = 30, delay: int = 2) -> str`: Опрашивает API Prodia для получения статуса задания и URL сгенерированного изображения.

## Функции

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str) -> str:
        if model in cls.models:
            return model
        elif model in cls.model_aliases:
            return cls.model_aliases[model]
        else:
            return cls.default_model
```

**Назначение**: Функция определяет, какая модель будет использоваться для генерации изображений.

**Параметры**:
- `model` (str): Имя запрошенной модели.

**Возвращает**:
- `str`: Имя модели, которая будет использоваться.

**Как работает функция**:
1. Проверяет, находится ли запрошенная модель в списке доступных моделей (`cls.models`). Если да, возвращает её.
2. Если модель не найдена в списке доступных моделей, проверяет, есть ли она в псевдонимах моделей (`cls.model_aliases`). Если да, возвращает соответствующий псевдоним.
3. Если модель не найдена ни в списке доступных моделей, ни в псевдонимах, возвращает модель по умолчанию (`cls.default_model`).

```
Проверка наличия модели в списке -> Проверка наличия псевдонима -> Возврат модели по умолчанию
```

**Примеры**:

```python
# Пример 1: Модель есть в списке доступных моделей
model = Prodia.get_model('absolutereality_v181.safetensors [3d9d4d2b]')
print(model)  # Вывод: absolutereality_v181.safetensors [3d9d4d2b]

# Пример 2: Модель есть в псевдонимах моделей (предположим, что такой псевдоним существует)
Prodia.model_aliases = {'default': 'absolutereality_v181.safetensors [3d9d4d2b]'}
model = Prodia.get_model('default')
print(model)  # Вывод: absolutereality_v181.safetensors [3d9d4d2b]

# Пример 3: Модель отсутствует в списке и псевдонимах
model = Prodia.get_model('non_existent_model')
print(model)  # Вывод: absolutereality_v181.safetensors [3d9d4d2b]
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        negative_prompt: str = "",
        steps: str = 20, # 1-25
        cfg: str = 7, # 0-20
        seed: Optional[int] = None,
        sampler: str = "DPM++ 2M Karras", # "Euler", "Euler a", "Heun", "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM"
        aspect_ratio: str = "square", # "square", "portrait", "landscape"
        **kwargs
    ) -> AsyncResult:
        model = cls.get_model(model)
        
        if seed is None:
            seed = random.randint(0, 10000)
        
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "origin": cls.url,
            "referer": f"{cls.url}/",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
        
        async with ClientSession(headers=headers) as session:
            prompt = messages[-1][\'content\'] if messages else ""
            
            params = {
                "new": "true",
                "prompt": prompt,
                "model": model,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "cfg": cfg,
                "seed": seed,
                "sampler": sampler,
                "aspect_ratio": aspect_ratio
            }
            
            async with session.get(cls.api_endpoint, params=params, proxy=proxy) as response:
                response.raise_for_status()
                job_data = await response.json()
                job_id = job_data["job"]
                
                image_url = await cls._poll_job(session, job_id, proxy)
                yield ImageResponse(image_url, alt=prompt)
```

**Назначение**: Функция создает асинхронный генератор для получения изображений от API Prodia.

**Параметры**:
- `model` (str): Имя модели для генерации изображения.
- `messages` (Messages): Список сообщений, содержащих запрос пользователя.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `negative_prompt` (str, optional): Негативный промпт для генерации изображения. По умолчанию "".
- `steps` (str, optional): Количество шагов для генерации изображения. По умолчанию "20".
- `cfg` (str, optional): CFG scale для генерации изображения. По умолчанию "7".
- `seed` (Optional[int], optional): Зерно для генерации изображения. По умолчанию `None`.
- `sampler` (str, optional): Сэмплер для генерации изображения. По умолчанию "DPM++ 2M Karras".
- `aspect_ratio` (str, optional): Соотношение сторон для генерации изображения. По умолчанию "square".
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImageResponse` с URL сгенерированного изображения.

**Как работает функция**:
1. Получает имя модели с помощью `cls.get_model(model)`.
2. Если `seed` не задан, генерирует случайное зерно.
3. Определяет заголовки запроса.
4. Создает асинхронную сессию `ClientSession` с заданными заголовками.
5. Извлекает текст запроса из последнего сообщения в списке `messages`.
6. Определяет параметры запроса, включая текст запроса, модель, негативный промпт и другие параметры генерации.
7. Отправляет асинхронный GET-запрос к API Prodia с заданными параметрами и заголовками.
8. Обрабатывает ответ API, извлекает `job_id` из JSON-ответа.
9. Опрашивает API Prodia для получения URL сгенерированного изображения с помощью `cls._poll_job(session, job_id, proxy)`.
10. Возвращает объект `ImageResponse` с URL сгенерированного изображения и текстом запроса.

```
Получение модели -> Генерация зерна (если не задано) -> Определение заголовков -> Создание сессии -> Извлечение текста запроса -> Определение параметров -> Отправка запроса -> Обработка ответа -> Опрос API -> Возврат ImageResponse
```

**Примеры**:

```python
# Пример 1: Генерация изображения с использованием модели по умолчанию
messages = [{'content': 'A cat sitting on a mat'}]
async for image_response in Prodia.create_async_generator(model=Prodia.default_model, messages=messages):
    print(image_response.url)

# Пример 2: Генерация изображения с заданным зерном и негативным промптом
messages = [{'content': 'A dog playing in the park'}]
async for image_response in Prodia.create_async_generator(model='absolutereality_v181.safetensors [3d9d4d2b]', messages=messages, seed=42, negative_prompt='ugly, deformed'):
    print(image_response.url)
```

### `_poll_job`

```python
    @classmethod
    async def _poll_job(cls, session: ClientSession, job_id: str, proxy: str, max_attempts: int = 30, delay: int = 2) -> str:
        for _ in range(max_attempts):\
            async with session.get(f"https://api.prodia.com/job/{job_id}", proxy=proxy) as response:\
                response.raise_for_status()\
                job_status = await response.json()\
\
                if job_status["status"] == "succeeded":\
                    return f"https://images.prodia.xyz/{job_id}.png"\
                elif job_status["status"] == "failed":\
                    raise Exception("Image generation failed")\
\
            await asyncio.sleep(delay)\
\
        raise Exception("Timeout waiting for image generation")
```

**Назначение**: Функция опрашивает API Prodia для получения статуса задания и URL сгенерированного изображения.

**Параметры**:
- `session` (ClientSession): Асинхронная сессия для выполнения HTTP-запросов.
- `job_id` (str): ID задания для отслеживания.
- `proxy` (str): Адрес прокси-сервера.
- `max_attempts` (int, optional): Максимальное количество попыток опроса API. По умолчанию 30.
- `delay` (int, optional): Задержка в секундах между попытками опроса API. По умолчанию 2.

**Возвращает**:
- `str`: URL сгенерированного изображения.

**Вызывает исключения**:
- `Exception`: Если генерация изображения не удалась или истекло время ожидания.

**Как работает функция**:
1. Выполняет цикл опроса API Prodia `max_attempts` раз.
2. Внутри цикла отправляет асинхронный GET-запрос к API Prodia для получения статуса задания.
3. Обрабатывает ответ API, извлекает статус задания из JSON-ответа.
4. Если статус задания "succeeded", возвращает URL сгенерированного изображения.
5. Если статус задания "failed", вызывает исключение `Exception` с сообщением об ошибке.
6. Если после `max_attempts` попыток статус задания не "succeeded" и не "failed", вызывает исключение `Exception` с сообщением о таймауте.
7. Между попытками опроса API ожидает `delay` секунд с помощью `asyncio.sleep(delay)`.

```
Цикл опроса -> Отправка запроса -> Обработка ответа -> Проверка статуса -> Возврат URL (если успешно) / Вызов исключения (если ошибка или таймаут) -> Задержка
```

**Примеры**:

```python
# Пример: Опрос API для получения URL сгенерированного изображения
import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        job_id = '12345'
        try:
            image_url = await Prodia._poll_job(session, job_id, proxy=None)
            print(f'Image URL: {image_url}')
        except Exception as ex:
            print(f'Error: {ex}')

if __name__ == "__main__":
    asyncio.run(main())