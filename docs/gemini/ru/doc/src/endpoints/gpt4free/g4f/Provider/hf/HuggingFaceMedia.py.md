# Модуль HuggingFaceMedia

## Обзор

Модуль `HuggingFaceMedia` предназначен для работы с моделями Hugging Face, специализирующимися на генерации медиаконтента, такого как изображения и видео. Он предоставляет асинхронный интерфейс для взаимодействия с различными API Hugging Face, включая поддержку различных провайдеров и задач.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает функциональность для генерации изображений и видео с использованием различных моделей, размещенных на платформе Hugging Face. Он поддерживает выбор моделей, провайдеров и настройку параметров генерации, таких как соотношение сторон, высота и ширина изображения, а также разрешение видео.

## Классы

### `HuggingFaceMedia`

**Описание**: Класс `HuggingFaceMedia` предоставляет методы для асинхронной генерации медиаконтента с использованием моделей Hugging Face.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Реализует общую логику для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("HuggingFace (Image/Video Generation)").
- `parent` (str): Родительский провайдер ("HuggingFace").
- `url` (str): URL главной страницы Hugging Face ("https://huggingface.co").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (True).
- `tasks` (List[str]): Список поддерживаемых задач (["text-to-image", "text-to-video"]).
- `provider_mapping` (Dict[str, Dict]): Словарь соответствия моделей и провайдеров.
- `task_mapping` (Dict[str, str]): Словарь соответствия моделей и задач.
- `models` (List[str]): Список доступных моделей.
- `image_models` (List[str]): Список доступных моделей для генерации изображений.
- `video_models` (List[str]): Список доступных моделей для генерации видео.

**Методы**:
- `get_models(**kwargs)`: Возвращает список доступных моделей.
- `get_mapping(model: str, api_key: str = None)`: Получает соответствие между моделью и провайдером.
- `create_async_generator(model: str, messages: Messages, api_key: str = None, extra_data: dict = {}, prompt: str = None, proxy: str = None, timeout: int = 0, n: int = 1, aspect_ratio: str = None, height: int = None, width: int = None, resolution: str = "480p", **kwargs)`: Создает асинхронный генератор для генерации медиаконтента.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, **kwargs) -> list[str]:
    """
    Получает список доступных моделей с платформы Hugging Face.

    Args:
        **kwargs: Дополнительные аргументы.

    Returns:
        list[str]: Список доступных моделей.
    """
```

**Назначение**: Функция `get_models` извлекает и возвращает список доступных моделей с платформы Hugging Face, которые поддерживают задачи генерации изображений и видео.

**Как работает функция**:

1.  Проверяется, был ли уже получен список моделей. Если `cls.models` пуст, то происходит запрос к API Hugging Face.
2.  Выполняется GET-запрос к API Hugging Face для получения списка моделей.
3.  Фильтруются модели, у которых есть хотя бы один "live" провайдер, поддерживающий задачи генерации изображений или видео.
4.  Формируется словарь `providers`, где ключами являются идентификаторы моделей, а значениями - списки провайдеров, соответствующих этим моделям.
5.  Создается список `new_models`, содержащий идентификаторы моделей и имена их провайдеров.
6.  Создается словарь `task_mapping`, сопоставляющий идентификаторы моделей с соответствующими задачами (генерация изображений или видео).
7.  Определяются списки `image_models` и `video_models` на основе `task_mapping`.
8.  Возвращается список доступных моделей.

**Примеры**:

```python
models = HuggingFaceMedia.get_models()
print(models)
# ['model_id1', 'model_id2:provider1', 'model_id3', ...]
```

### `get_mapping`

```python
@classmethod
async def get_mapping(cls, model: str, api_key: str = None):
    """
    Получает соответствие между моделью и провайдером.

    Args:
        model (str): Идентификатор модели.
        api_key (str, optional): API ключ. По умолчанию `None`.

    Returns:
        Dict[str, Dict]: Словарь соответствия между моделью и провайдером.
    """
```

**Назначение**: Функция `get_mapping` асинхронно получает соответствие между указанной моделью Hugging Face и её провайдерами, используя API Hugging Face.

**Параметры**:
- `model` (str): Идентификатор модели, для которой необходимо получить соответствие.
- `api_key` (str, optional): API-ключ для аутентификации запроса. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Dict]`: Словарь, где ключи - идентификаторы провайдеров, а значения - информация о провайдерах.

**Как работает функция**:

1. Проверяет, есть ли уже соответствие для данной модели в `cls.provider_mapping`. Если есть, возвращает его.
2. Формирует заголовки запроса, включая API-ключ, если он предоставлен.
3. Выполняет асинхронный GET-запрос к API Hugging Face для получения информации о модели.
4. Извлекает соответствия между моделью и провайдерами из полученных данных и сохраняет их в `cls.provider_mapping`.
5. Возвращает соответствие.

**Примеры**:

```python
model_mapping = await HuggingFaceMedia.get_mapping(model='stabilityai/stable-diffusion-2', api_key='YOUR_API_KEY')
print(model_mapping)
# {'provider_id1': {'status': 'live', 'task': 'text-to-image', ...}, 'provider_id2': {...}}
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    extra_data: dict = {},
    prompt: str = None,
    proxy: str = None,
    timeout: int = 0,
    # Video & Image Generation
    n: int = 1,
    aspect_ratio: str = None,
    # Only for Image Generation
    height: int = None,
    width: int = None,
    # Video Generation
    resolution: str = "480p",
    **kwargs
):
    """
    Создает асинхронный генератор для генерации медиаконтента.

    Args:
        model (str): Идентификатор модели.
        messages (Messages): Список сообщений.
        api_key (str, optional): API ключ. По умолчанию `None`.
        extra_data (dict, optional): Дополнительные данные. По умолчанию `{}`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        proxy (str, optional): Прокси сервер. По умолчанию `None`.
        timeout (int, optional): Время ожидания. По умолчанию `0`.
        n (int, optional): Количество генерируемых элементов. По умолчанию `1`.
        aspect_ratio (str, optional): Соотношение сторон. По умолчанию `None`.
        height (int, optional): Высота изображения. По умолчанию `None`.
        width (int, optional): Ширина изображения. По умолчанию `None`.
        resolution (str, optional): Разрешение видео. По умолчанию `"480p"`.
        **kwargs: Дополнительные аргументы.

    Yields:
        ProviderInfo: Информация о провайдере.
        ImageResponse | VideoResponse | Reasoning: Ответ с медиаконтентом или информацией о процессе.
    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для генерации медиаконтента (изображений или видео) с использованием указанной модели Hugging Face и различных провайдеров.

**Параметры**:

*   `model` (str): Идентификатор модели Hugging Face для использования. Если указан в формате `model:provider`, будет использоваться конкретный провайдер.
*   `messages` (Messages): Список сообщений для формирования запроса.
*   `api_key` (str, optional): API-ключ для аутентификации запросов. По умолчанию `None`.
*   `extra_data` (dict, optional): Дополнительные данные, передаваемые провайдеру. По умолчанию `{}`.
*   `prompt` (str, optional): Текст запроса для генерации. По умолчанию `None`.
*   `proxy` (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
*   `timeout` (int, optional): Максимальное время ожидания ответа от провайдера. По умолчанию `0`.
*   `n` (int, optional): Количество медиафайлов для генерации. По умолчанию `1`.
*   `aspect_ratio` (str, optional): Соотношение сторон генерируемого изображения или видео. По умолчанию `None`.
*   `height` (int, optional): Высота генерируемого изображения (только для изображений). По умолчанию `None`.
*   `width` (int, optional): Ширина генерируемого изображения (только для изображений). По умолчанию `None`.
*   `resolution` (str, optional): Разрешение генерируемого видео (только для видео). По умолчанию `"480p"`.
*   `**kwargs`: Дополнительные параметры, передаваемые провайдеру.

**Как работает функция**:

1.  Разбирает параметры модели, чтобы определить, указан ли конкретный провайдер.
2.  Форматирует запрос `prompt` с использованием предоставленных сообщений.
3.  Получает соответствие между моделью и провайдерами с помощью `cls.get_mapping`.
4.  Определяет асинхронную функцию `generate`, которая выполняет генерацию медиаконтента для каждого провайдера.
5.  В цикле запускает несколько задач генерации (`n` раз) в фоновом режиме.
6.  Ожидает завершения всех задач и возвращает результаты в виде асинхронного генератора.
7.  Для каждого провайдера:
    *   Формирует информацию о провайдере `provider_info`.
    *   Определяет базовый URL API провайдера.
    *   Извлекает задачу (генерация изображения или видео) и идентификатор провайдера.
    *   Вызывает исключение `ModelNotSupportedError`, если задача не поддерживается.
    *   Настраивает дополнительные данные `extra_data` в зависимости от задачи и провайдера, включая соотношение сторон, высоту и ширину изображения, разрешение видео и другие параметры.
    *   Формирует URL для запроса к API провайдера.
    *   Формирует данные `data` для запроса, включая текст запроса и дополнительные параметры.
    *   Выполняет POST-запрос к API провайдера с использованием асинхронной сессии `StreamSession`.
    *   Обрабатывает различные статусы ответа (400, 401, 402, 404) и вызывает исключения в случае ошибок.
    *   Сохраняет полученный медиаконтент с помощью `save_response_media`.
    *   Возвращает информацию о провайдере и сгенерированный медиаконтент (`ImageResponse` или `VideoResponse`).

**Примеры**:

```python
async for item in HuggingFaceMedia.create_async_generator(
    model="stabilityai/stable-diffusion-2",
    messages=[{"role": "user", "content": "Generate a futuristic car"}],
    api_key="YOUR_API_KEY",
    n=2
):
    print(item)
#   (ProviderInfo, ImageResponse)
```

```python
async for item in HuggingFaceMedia.create_async_generator(
    model="cerspense/zeroscope_v2_XL",
    messages=[{"role": "user", "content": "Generate a cat running"}],
    api_key="YOUR_API_KEY",
    n=1
):
    print(item)
#   (ProviderInfo, VideoResponse)
```