# Модуль `Qwen_QVQ_72B`

## Обзор

Модуль `Qwen_QVQ_72B` предоставляет реализацию асинхронного провайдера для взаимодействия с моделью Qwen QVQ-72B, размещенной на платформе Hugging Face Space. Он поддерживает как текстовые запросы, так и запросы с изображениями. Модуль использует `aiohttp` для асинхронных HTTP-запросов и предоставляет функциональность для загрузки изображений и форматирования запросов.

## Подробней

Этот модуль является частью системы провайдеров, позволяющей взаимодействовать с различными языковыми моделями. Он предназначен для работы с моделью Qwen QVQ-72B, доступной через API Hugging Face Space. Модуль обеспечивает асинхронную отправку запросов к API, обработку ответов и генерацию результатов.

## Классы

### `Qwen_QVQ_72B`

**Описание**: Класс `Qwen_QVQ_72B` реализует асинхронный провайдер для взаимодействия с моделью Qwen QVQ-72B.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих результаты.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Название провайдера ("Qwen QVQ-72B").
- `url` (str): URL Hugging Face Space, где размещена модель ("https://qwen-qvq-72b-preview.hf.space").
- `api_endpoint` (str): Конечная точка API для генерации текста ("/gradio_api/call/generate").
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ("qwen-qvq-72b-preview").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (совпадает с `default_model`).
- `model_aliases` (dict): Псевдонимы моделей ({"qvq-72b": default_vision_model}).
- `vision_models` (list): Список моделей, поддерживающих обработку изображений.
- `models` (list): Список всех поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для обработки запроса к модели.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls, model: str, messages: Messages,
    media: MediaListType = None,
    api_key: str = None, 
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для обработки запроса к модели.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        media (MediaListType, optional): Список медиафайлов (изображений). По умолчанию `None`.
        api_key (str, optional): API ключ. По умолчанию `None`.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий результаты от модели.

    Raises:
        ResponseError: Если получен статус ошибки от API.
        RuntimeError: Если не удалось прочитать ответ от API.

    """
```

**Назначение**: Создает асинхронный генератор для отправки запроса к модели Qwen QVQ-72B и получения результатов.

**Параметры**:
- `cls`: Ссылка на класс `Qwen_QVQ_72B`.
- `model` (str): Название модели.
- `messages` (Messages): Список сообщений для отправки в запросе.
- `media` (MediaListType, optional): Список медиафайлов (изображений) для отправки. По умолчанию `None`.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий результаты от модели.

**Вызывает исключения**:
- `ResponseError`: Если получен статус ошибки от API.
- `RuntimeError`: Если не удалось прочитать ответ от API.

**Внутренние функции**:
- Отсутствуют.

**Как работает функция**:

1. **Инициализация**:
   - Устанавливает заголовки запроса, включая `Accept: application/json` и, при наличии, `Authorization: Bearer {api_key}`.
   - Создает асинхронную сессию `ClientSession` с установленными заголовками.
2. **Обработка медиафайлов (изображений)**:
   - Если `media` не `None`, функция выполняет следующие действия:
     - Создает объект `FormData` для отправки данных формы.
     - Преобразует изображение в байты с помощью `to_bytes(media[0][0])`.
     - Добавляет поле `files` в `FormData` с байтами изображения, типом контента, полученным из `is_accepted_format(data_bytes)`, и именем файла `media[0][1]`.
     - Отправляет POST-запрос на URL для загрузки изображения (`{cls.url}/gradio_api/upload?upload_id={get_random_string()}`).
     - Получает ответ и извлекает путь к загруженному изображению из JSON.
     - Формирует данные запроса `data` в виде словаря, содержащего путь к изображению и отформатированный запрос `format_prompt(messages)`.
   - Если `media` равно `None`, функция формирует данные запроса `data` в виде словаря, содержащего `None` для изображения и отформатированный запрос `format_prompt(messages)`.
3. **Отправка запроса и получение ответа**:
   - Отправляет POST-запрос на URL API (`{cls.url}{cls.api_endpoint}`) с данными запроса `data`.
   - Получает `event_id` из JSON ответа.
   - Отправляет GET-запрос на URL для получения событий (`{cls.url}{cls.api_endpoint}/{event_id}`).
   - Читает данные из ответа по частям (chunks).
4. **Обработка событий**:
   - Для каждого чанка данных:
     - Если чанк начинается с `b"event: "`, извлекает тип события (например, "error", "complete", "generating").
     - Если чанк начинается с `b"data: "`:
       - Если событие "error", вызывает исключение `ResponseError` с сообщением об ошибке.
       - Если событие "complete" или "generating":
         - Пытается десериализовать JSON из чанка данных.
         - Если событие "generating", извлекает текст из данных и возвращает его с помощью `yield`, начиная с позиции `text_position`. Обновляет `text_position`.
         - Если событие "complete", завершает генерацию.

**ASCII Flowchart**:

```
   Инициализация -> Формирование данных запроса -> Отправка POST-запроса -> Получение event_id
       ↓
   Обработка медиа -> Отправка GET-запроса к event_id -> Чтение чанков данных
                                                         ↓
                                                         Обработка события -> ("error": raise ResponseError, "generating": yield text, "complete": break)
```

**Примеры**:

Пример 1: Текстовый запрос

```python
model = "qwen-qvq-72b-preview"
messages = [{"role": "user", "content": "Напиши короткое стихотворение о весне."}]
async for chunk in Qwen_QVQ_72B.create_async_generator(model=model, messages=messages):
    print(chunk, end="")
```

Пример 2: Запрос с изображением

```python
from pathlib import Path

model = "qwen-qvq-72b-preview"
messages = [{"role": "user", "content": "Что изображено на картинке?"}]
image_path = Path("path/to/image.jpg")
media = [[image_path, "image.jpg"]]

async for chunk in Qwen_QVQ_72B.create_async_generator(model=model, messages=messages, media=media):
    print(chunk, end="")