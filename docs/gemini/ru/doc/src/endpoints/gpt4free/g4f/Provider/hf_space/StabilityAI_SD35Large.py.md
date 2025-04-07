# Модуль StabilityAI_SD35Large
## Обзор

Модуль `StabilityAI_SD35Large` предоставляет асинхронный генератор для создания изображений с использованием модели Stability AI SD-3.5-Large. Он интегрируется с API Stability AI через HTTP запросы и обрабатывает ответы для предоставления URL-адресов сгенерированных изображений.

## Подробней

Этот модуль используется для генерации изображений на основе текстовых запросов с использованием модели Stability AI SD-3.5-Large. Он поддерживает настройку параметров генерации, таких как негативные подсказки, соотношение сторон, размеры изображения, масштаб направляющих указаний, количество шагов вывода и зерно для воспроизводимости результатов. Модуль обрабатывает ответы от API Stability AI, включая ошибки и промежуточные результаты, такие как превью изображений.

## Классы

### `StabilityAI_SD35Large`

**Описание**: Класс `StabilityAI_SD35Large` предоставляет функциональность для генерации изображений с использованием модели Stability AI SD-3.5-Large.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, "StabilityAI SD-3.5-Large".
- `url` (str): URL API Stability AI, "https://stabilityai-stable-diffusion-3-5-large.hf.space".
- `api_endpoint` (str): Endpoint API для вызова, "/gradio_api/call/infer".
- `working` (bool): Указывает, работает ли провайдер, `True`.
- `default_model` (str): Модель по умолчанию, 'stabilityai-stable-diffusion-3-5-large'.
- `default_image_model` (str): Модель изображения по умолчанию, совпадает с `default_model`.
- `model_aliases` (dict): Псевдонимы моделей, `{"sd-3.5": default_model}`.
- `image_models` (list): Список моделей изображений, полученный из ключей `model_aliases`.
- `models` (list): Список поддерживаемых моделей, совпадает с `image_models`.

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
    """ Асинхронно генерирует изображения на основе предоставленных параметров, используя API Stability AI.

    Args:
        cls (StabilityAI_SD35Large): Ссылка на класс.
        model (str): Используемая модель.
        messages (Messages): Список сообщений для формирования запроса.
        prompt (str, optional): Основной текст запроса. Defaults to None.
        negative_prompt (str, optional): Негативный текст запроса. Defaults to None.
        api_key (str, optional): API ключ для доступа к Stability AI. Defaults to None.
        proxy (str, optional): Адрес прокси-сервера. Defaults to None.
        aspect_ratio (str, optional): Соотношение сторон изображения. Defaults to "1:1".
        width (int, optional): Ширина изображения. Defaults to None.
        height (int, optional): Высота изображения. Defaults to None.
        guidance_scale (float, optional): Масштаб направляющих указаний. Defaults to 4.5.
        num_inference_steps (int, optional): Количество шагов вывода. Defaults to 50.
        seed (int, optional): Зерно для воспроизводимости результатов. Defaults to 0.
        randomize_seed (bool, optional): Флаг рандомизации зерна. Defaults to True.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse` с URL-адресами изображений.

    Raises:
        ResponseError: Если превышен лимит токенов GPU.
        RuntimeError: Если не удалось распарсить URL изображения из ответа.

    Внутренние функции:
        Отсутствуют.
    """
    ...
```

**Параметры**:
- `cls` (StabilityAI_SD35Large): Ссылка на класс.
- `model` (str): Используемая модель.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Основной текст запроса. Defaults to None.
- `negative_prompt` (str, optional): Негативный текст запроса. Defaults to None.
- `api_key` (str, optional): API ключ для доступа к Stability AI. Defaults to None.
- `proxy` (str, optional): Адрес прокси-сервера. Defaults to None.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. Defaults to "1:1".
- `width` (int, optional): Ширина изображения. Defaults to None.
- `height` (int, optional): Высота изображения. Defaults to None.
- `guidance_scale` (float, optional): Масштаб направляющих указаний. Defaults to 4.5.
- `num_inference_steps` (int, optional): Количество шагов вывода. Defaults to 50.
- `seed` (int, optional): Зерно для воспроизводимости результатов. Defaults to 0.
- `randomize_seed` (bool, optional): Флаг рандомизации зерна. Defaults to True.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse` с URL-адресами изображений.

**Вызывает исключения**:
- `ResponseError`: Если превышен лимит токенов GPU.
- `RuntimeError`: Если не удалось распарсить URL изображения из ответа.

**Как работает функция**:

1. **Формирование заголовков запроса**: Функция формирует заголовки HTTP-запроса, включая `Content-Type` и `Authorization` (если предоставлен API-ключ).
2. **Создание сессии**: Создается асинхронная сессия `ClientSession` с использованием сформированных заголовков.
3. **Форматирование запроса**: Текстовый запрос формируется с использованием функции `format_image_prompt`.
4. **Настройка параметров изображения**: Параметры изображения, такие как ширина и высота, настраиваются с использованием функции `use_aspect_ratio`.
5. **Формирование данных запроса**: Данные запроса формируются в виде словаря, включающего текст запроса, негативный текст запроса, зерно, флаг рандомизации зерна, ширину, высоту, масштаб направляющих указаний и количество шагов вывода.
6. **Отправка запроса**: Отправляется POST-запрос к API Stability AI.
7. **Обработка ответа**: Обрабатывается ответ от API, включая промежуточные результаты и ошибки.
8. **Получение event_id**: Из JSON ответа извлекается `event_id`.
9. **Получение данных о событии**: С использованием `event_id` отправляется GET-запрос.
10. **Обработка чанков ответа**: Из потока чанков ответа извлекаются данные о статусе генерации.
11. **Обработка ошибок**: Если в событии приходит статус `error`, вызывается исключение `ResponseError`.
12. **Обработка статусов "complete" и "generating"**: Если статус равен `complete` или `generating`, происходит попытка извлечения URL изображения из JSON-данных.
13. **Генерация объектов `ImagePreview` и `ImageResponse`**: В зависимости от статуса, генерируются объекты `ImagePreview` (для промежуточных результатов) и `ImageResponse` (для окончательного результата).
14. **Завершение**: Генератор завершает работу после получения окончательного результата.

```
Формирование заголовков запроса
     ↓
Создание сессии
     ↓
Форматирование запроса
     ↓
Настройка параметров изображения
     ↓
Формирование данных запроса
     ↓
Отправка POST-запроса к API
     ↓
Обработка ответа
     ↓
Извлечение event_id
     ↓
Отправка GET-запроса к API с event_id
     ↓
Обработка чанков ответа
     ↓
Обработка ошибок / Обработка статусов "complete" и "generating"
     ↓
Генерация объектов ImagePreview и ImageResponse
     ↓
Завершение
```

**Примеры**:

Пример 1: Генерация изображения с использованием минимального набора параметров.

```python
model = 'stabilityai-stable-diffusion-3-5-large'
messages = [{'role': 'user', 'content': 'Generate a futuristic cityscape'}]
async for image in StabilityAI_SD35Large.create_async_generator(model=model, messages=messages):
    print(image.url)
```

Пример 2: Генерация изображения с указанием негативного запроса и API-ключа.

```python
model = 'stabilityai-stable-diffusion-3-5-large'
messages = [{'role': 'user', 'content': 'Generate a realistic portrait'}]
negative_prompt = 'blurry, low quality'
api_key = 'YOUR_API_KEY'
async for image in StabilityAI_SD35Large.create_async_generator(model=model, messages=messages, negative_prompt=negative_prompt, api_key=api_key):
    print(image.url)
```

Пример 3: Генерация изображения с использованием прокси и указанием размеров изображения.

```python
model = 'stabilityai-stable-diffusion-3-5-large'
messages = [{'role': 'user', 'content': 'Generate a landscape'}]
proxy = 'http://your_proxy:8080'
width = 512
height = 512
async for image in StabilityAI_SD35Large.create_async_generator(model=model, messages=messages, proxy=proxy, width=width, height=height):
    print(image.url)
```