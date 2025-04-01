# Модуль StabilityAI_SD35Large

## Обзор

Модуль `StabilityAI_SD35Large` предоставляет асинхронный интерфейс для взаимодействия с моделью StabilityAI SD-3.5-Large, предназначенной для генерации изображений. Он позволяет отправлять запросы на генерацию изображений с заданными параметрами, такими как промт, негативный промт, размеры изображения и другие параметры. Модуль использует API StabilityAI через HTTP-запросы и предоставляет результаты в виде асинхронного генератора, который выдает превью и финальные изображения.

## Подробней

Этот модуль предназначен для интеграции в систему, где требуется генерация изображений на основе текстовых запросов. Он обеспечивает абстракцию от низкоуровневых деталей взаимодействия с API StabilityAI, предоставляя удобный интерфейс для отправки запросов и получения результатов.

## Классы

### `StabilityAI_SD35Large`

**Описание**: Класс `StabilityAI_SD35Large` является провайдером для генерации изображений с использованием модели StabilityAI SD-3.5-Large.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Аттрибуты**:
- `label` (str): Метка провайдера, отображаемая в интерфейсе. Значение: `"StabilityAI SD-3.5-Large"`.
- `url` (str): URL API StabilityAI. Значение: `"https://stabilityai-stable-diffusion-3-5-large.hf.space"`.
- `api_endpoint` (str): Эндпоинт API для вызова инференса. Значение: `"/gradio_api/call/infer"`.
- `working` (bool): Указывает, работает ли провайдер в данный момент. Значение: `True`.
- `default_model` (str): Модель, используемая по умолчанию. Значение: `'stabilityai-stable-diffusion-3-5-large'`.
- `default_image_model` (str): Модель изображения, используемая по умолчанию. Значение: совпадает с `default_model`.
- `model_aliases` (dict): Псевдонимы моделей. Значение: `{"sd-3.5": default_model}`.
- `image_models` (list): Список моделей изображений. Значение: список ключей из `model_aliases`.
- `models` (list): Список доступных моделей. Значение: совпадает с `image_models`.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения изображений.

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
    Создает асинхронный генератор для генерации изображений с использованием StabilityAI SD-3.5-Large.

    Args:
        cls (StabilityAI_SD35Large): Класс StabilityAI_SD35Large.
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для формирования промта.
        prompt (str, optional): Текстовый промт для генерации изображения. По умолчанию `None`.
        negative_prompt (str, optional): Негативный промт, описывающий, что не должно быть на изображении. По умолчанию `None`.
        api_key (str, optional): API-ключ для доступа к StabilityAI API. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера для выполнения запросов. По умолчанию `None`.
        aspect_ratio (str, optional): Соотношение сторон изображения (например, "1:1", "16:9"). По умолчанию `"1:1"`.
        width (int, optional): Ширина изображения в пикселях. Если не указана, используется значение из `aspect_ratio`.
        height (int, optional): Высота изображения в пикселях. Если не указана, используется значение из `aspect_ratio`.
        guidance_scale (float, optional): Масштаб соответствия промту. По умолчанию `4.5`.
        num_inference_steps (int, optional): Количество шагов инференса. По умолчанию `50`.
        seed (int, optional): Зерно для генерации случайных чисел, обеспечивающее воспроизводимость результата. По умолчанию `0`.
        randomize_seed (bool, optional): Если `True`, зерно будет случайным. По умолчанию `True`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий объекты `ImagePreview` и `ImageResponse`.

    Raises:
        ResponseError: Если превышен лимит токенов GPU.
        RuntimeError: Если не удалось распарсить URL изображения.
    """
    ...
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор, который отправляет запросы к API StabilityAI для генерации изображений и возвращает результаты в виде объектов `ImagePreview` (предварительный просмотр) и `ImageResponse` (полное изображение).

**Параметры**:
- `cls` (StabilityAI_SD35Large): Ссылка на класс.
- `model` (str): Имя модели для генерации изображения.
- `messages` (Messages): Список сообщений, используемых для формирования запроса.
- `prompt` (str, optional): Основной текстовый запрос для генерации изображения. По умолчанию `None`.
- `negative_prompt` (str, optional): Текст, описывающий, что не должно присутствовать на изображении. По умолчанию `None`.
- `api_key` (str, optional): API ключ для аутентификации запросов. По умолчанию `None`.
- `proxy` (str, optional): Адрес прокси-сервера для выполнения запросов. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон генерируемого изображения (например, "1:1"). По умолчанию `"1:1"`.
- `width` (int, optional): Ширина изображения в пикселях. По умолчанию `None`.
- `height` (int, optional): Высота изображения в пикселях. По умолчанию `None`.
- `guidance_scale` (float, optional): Параметр, определяющий, насколько строго изображение должно соответствовать запросу. По умолчанию `4.5`.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию `50`.
- `seed` (int, optional): Начальное значение для генератора случайных чисел, обеспечивающее воспроизводимость результатов. По умолчанию `0`.
- `randomize_seed` (bool, optional): Если установлено в `True`, зерно будет случайным, что приведет к разным результатам при каждом вызове. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает объекты типа `ImagePreview` и `ImageResponse`, представляющие собой предварительные и финальные результаты генерации изображения.

**Вызывает исключения**:
- `ResponseError`: Вызывается, если превышен лимит токенов GPU при запросе к API. Содержит сообщение об ошибке, возвращенное API.
- `RuntimeError`: Вызывается, если не удается распарсить URL изображения из ответа API.

**Как работает функция**:

1. **Подготовка заголовков запроса**:
   - Функция создает заголовки запроса, включая `Content-Type` и `Accept`.
   - Если предоставлен `api_key`, он добавляется в заголовок `Authorization`.

2. **Формирование данных запроса**:
   - Формируется промт изображения с использованием `format_image_prompt` и переданных сообщений.
   - Определяются размеры изображения на основе `aspect_ratio`, `width` и `height` с помощью функции `use_aspect_ratio`.
   - Создается словарь `data`, содержащий все необходимые параметры для запроса к API, такие как промт, негативный промт, зерно, размеры изображения, масштаб соответствия и количество шагов инференса.

3. **Отправка запроса и обработка ответа**:
   - Отправляется POST-запрос к API StabilityAI с использованием `ClientSession`.
   - Полученный `event_id` используется для последующего получения событий генерации.
   - Отправляется GET-запрос для получения событий, связанных с `event_id`.

4. **Обработка событий**:
   - Функция асинхронно обрабатывает чанки данных из ответа сервера.
   - Если событие `error`, выбрасывается исключение `ResponseError`.
   - Если событие `generating`, извлекается URL превью изображения и выдается объект `ImagePreview`.
   - Если событие `complete`, извлекается URL финального изображения и выдается объект `ImageResponse`, после чего генератор завершает работу.

5. **Обработка ошибок парсинга**:
   - В случае ошибок при парсинге JSON или извлечении URL изображения, выбрасывается исключение `RuntimeError`.

**ASCII flowchart**:

```
    [Подготовка заголовков запроса]
        |
    [Формирование данных запроса (промт, размеры, параметры)]
        |
    [Отправка POST-запроса к API StabilityAI]
        |
    [Получение event_id]
        |
    [Отправка GET-запроса для получения событий]
        |
    [Асинхронная обработка чанков данных]
        |
    [Обработка события: error, generating, complete]
        |
    [Выдача ImagePreview (generating) / ImageResponse (complete)]
        |
    [Завершение генератора (complete)]
```

**Примеры**:

```python
# Пример 1: Генерация изображения с минимальными параметрами
async for result in StabilityAI_SD35Large.create_async_generator(model='sd-3.5', messages=[{"role": "user", "content": "A cat"}])
    if isinstance(result, ImagePreview):
        print("Preview URL:", result.url)
    elif isinstance(result, ImageResponse):
        print("Final Image URL:", result.url)

# Пример 2: Генерация изображения с заданными размерами и негативным промтом
async for result in StabilityAI_SD35Large.create_async_generator(
    model='sd-3.5',
    messages=[{"role": "user", "content": "A futuristic cityscape"}],
    width=512,
    height=512,
    negative_prompt="people, cars"
):
    if isinstance(result, ImagePreview):
        print("Preview URL:", result.url)
    elif isinstance(result, ImageResponse):
        print("Final Image URL:", result.url)

# Пример 3: Генерация изображения с использованием API-ключа и прокси
async for result in StabilityAI_SD35Large.create_async_generator(
    model='sd-3.5',
    messages=[{"role": "user", "content": "A dragon"}],
    api_key="YOUR_API_KEY",
    proxy="http://your.proxy:8080"
):
    if isinstance(result, ImagePreview):
        print("Preview URL:", result.url)
    elif isinstance(result, ImageResponse):
        print("Final Image URL:", result.url)
```