# Модуль StabilityAI_SD35Large
## Обзор

Модуль `StabilityAI_SD35Large` предоставляет асинхронный интерфейс для генерации изображений с использованием модели Stability AI SD-3.5-Large через API Hugging Face Space. Он позволяет генерировать изображения на основе текстовых запросов, поддерживает различные параметры конфигурации и предоставляет возможность отслеживания процесса генерации изображений.

## Подробней

Этот модуль является частью системы, предназначенной для взаимодействия с различными моделями генерации изображений. Он использует асинхронные запросы (`aiohttp`) для обмена данными с API Stability AI. Модуль реализует функциональность генерации изображений на основе предоставленных текстовых запросов и параметров конфигурации. Он также включает обработку ошибок и предоставляет информацию о ходе генерации изображений. Расположение файла в проекте указывает на то, что он является одним из множества провайдеров, предлагающих различные модели и API для генерации изображений.

## Классы

### `StabilityAI_SD35Large`

**Описание**: Класс `StabilityAI_SD35Large` предоставляет асинхронный интерфейс для генерации изображений с использованием модели Stability AI SD-3.5-Large.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Добавляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("StabilityAI SD-3.5-Large").
- `url` (str): URL API Hugging Face Space ("https://stabilityai-stable-diffusion-3-5-large.hf.space").
- `api_endpoint` (str): Конечная точка API ("/gradio_api/call/infer").
- `working` (bool): Указывает, что провайдер работает (True).
- `default_model` (str): Модель по умолчанию ('stabilityai-stable-diffusion-3-5-large').
- `default_image_model` (str): Модель изображения по умолчанию, равна `default_model`.
- `model_aliases` (dict): Псевдонимы моделей ({"sd-3.5": default_model}).
- `image_models` (list): Список моделей изображений, полученный из ключей `model_aliases`.
- `models` (list): Список поддерживаемых моделей, равен `image_models`.

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
        """Создает асинхронный генератор для генерации изображений на основе модели Stability AI SD-3.5-Large.

        Args:
            model (str): Имя модели для генерации изображений.
            messages (Messages): Список сообщений, используемых для формирования запроса.
            prompt (str, optional): Основной текстовый запрос для генерации изображения. По умолчанию `None`.
            negative_prompt (str, optional): Негативный текстовый запрос, описывающий, что не должно быть на изображении. По умолчанию `None`.
            api_key (str, optional): API-ключ для доступа к Stability AI. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения (например, "1:1"). По умолчанию "1:1".
            width (int, optional): Ширина изображения. Если не указана, используется значение из `aspect_ratio`.
            height (int, optional): Высота изображения. Если не указана, используется значение из `aspect_ratio`.
            guidance_scale (float, optional): Масштаб соответствия запросу. По умолчанию 4.5.
            num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 50.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse` по мере генерации изображения.

        Raises:
            ResponseError: Если превышен лимит токенов GPU.
            RuntimeError: Если не удалось обработать URL изображения.
        """
```

**Назначение**: Создание асинхронного генератора для генерации изображений с использованием Stability AI SD-3.5-Large.

**Параметры**:
- `model` (str): Имя модели для генерации изображений.
- `messages` (Messages): Список сообщений, используемых для формирования запроса.
- `prompt` (str, optional): Основной текстовый запрос для генерации изображения. По умолчанию `None`.
- `negative_prompt` (str, optional): Негативный текстовый запрос, описывающий, что не должно быть на изображении. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для доступа к Stability AI. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения (например, "1:1"). По умолчанию "1:1".
- `width` (int, optional): Ширина изображения. Если не указана, используется значение из `aspect_ratio`.
- `height` (int, optional): Высота изображения. Если не указана, используется значение из `aspect_ratio`.
- `guidance_scale` (float, optional): Масштаб соответствия запросу. По умолчанию 4.5.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию 50.
- `seed` (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImagePreview` и `ImageResponse` по мере генерации изображения.

**Вызывает исключения**:
- `ResponseError`: Если превышен лимит токенов GPU.
- `RuntimeError`: Если не удалось обработать URL изображения.

**Как работает функция**:

1. **Формирование заголовков**: Функция формирует заголовки запроса, включая `Content-Type` и, при наличии, `Authorization` с API-ключом.
2. **Создание сессии**: Создается асинхронная клиентская сессия `aiohttp.ClientSession` с установленными заголовками.
3. **Форматирование запроса**: Текстовый запрос `prompt` форматируется с использованием предоставленных сообщений `messages`.
4. **Подготовка данных**: Подготавливаются данные для запроса, включая размеры изображения (`width`, `height`), соотношение сторон (`aspect_ratio`) и другие параметры конфигурации.
5. **Отправка запроса**: Отправляется POST-запрос к API Stability AI с данными в формате JSON.
6. **Обработка ответа**:
   - Получается `event_id` из JSON-ответа.
   - Отправляется GET-запрос к API для получения событий, связанных с `event_id`.
   - Асинхронно читаются чанки из ответа.
   - Если `event` равен "error", выбрасывается исключение `ResponseError`.
   - Если `event` равен "generating" или "complete":
     - Извлекается URL изображения из JSON-данных.
     - Если `event` равен "generating", возвращается объект `ImagePreview`.
     - Если `event` равен "complete", возвращается объект `ImageResponse` и генератор завершается.

**ASCII Flowchart**:

```
    Начало
     |
     V
Заголовки запроса (формирование)
     |
     V
   aiohttp.ClientSession (создание)
     |
     V
Текстовый запрос (форматирование)
     |
     V
  Данные (подготовка)
     |
     V
   POST-запрос (отправка)
     |
     V
  event_id (получение)
     |
     V
  GET-запрос (отправка)
     |
     V
Чтение чанков (асинхронное)
     |
     V
  event == "error"?
     |
     +-> Да: ResponseError (исключение)
     |
     V
  event == "generating" или "complete"?
     |
     +-> Нет: Продолжить чтение чанков
     |
     V
  URL изображения (извлечение)
     |
     V
event == "generating"?
     |
     +-> Да: ImagePreview (генерация)
     |
     V
ImageResponse (генерация)
     |
     V
    Конец
```

**Примеры**:

Пример 1: Генерация изображения с базовыми параметрами.

```python
model = "stabilityai-stable-diffusion-3-5-large"
messages = [{"role": "user", "content": "A futuristic cityscape"}]
async for result in StabilityAI_SD35Large.create_async_generator(model=model, messages=messages):
    print(result)
```

Пример 2: Генерация изображения с указанием негативного запроса и API-ключа.

```python
model = "stabilityai-stable-diffusion-3-5-large"
messages = [{"role": "user", "content": "A serene landscape"}]
negative_prompt = "people, text"
api_key = "YOUR_API_KEY"
async for result in StabilityAI_SD35Large.create_async_generator(model=model, messages=messages, negative_prompt=negative_prompt, api_key=api_key):
    print(result)
```