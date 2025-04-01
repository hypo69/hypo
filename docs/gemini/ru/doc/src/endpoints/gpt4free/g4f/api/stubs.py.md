# Модуль stubs.py

## Обзор

Модуль `stubs.py` содержит определения структур данных, используемых для конфигурации и обмена данными с API g4f (GPT4Free). Он включает классы конфигурации для чат-завершений и генерации изображений, а также модели ответов от провайдеров, моделей и ошибок. Модуль использует библиотеку `pydantic` для определения схем данных и аннотации типов для обеспечения строгой типизации.

## Подробнее

Этот модуль предоставляет структуры данных, которые используются для взаимодействия с API g4f. Он содержит классы для конфигурации запросов к API, а также классы для представления ответов от API. Это позволяет стандартизировать обмен данными между различными компонентами системы и обеспечивает проверку типов данных.

## Классы

### `ChatCompletionsConfig`

**Описание**: Класс конфигурации для запросов на чат-завершения.

**Принцип работы**:
Класс `ChatCompletionsConfig` определяет параметры, необходимые для запроса на завершение чата. Он включает в себя сообщения, модель, провайдера, параметры потоковой передачи, изображения, температуру, штрафы, максимальное количество токенов, стоп-слова, ключи API, прокси, идентификаторы разговоров, инструменты и другие параметры, необходимые для настройки запроса.

**Параметры**:
- `messages` (Messages): Список сообщений для чата. Пример: `[{"role": "system", "content": ""}, {"role": "user", "content": ""}]`.
- `model` (str): Имя модели для использования. По умолчанию "".
- `provider` (Optional[str]): Провайдер модели. По умолчанию `None`.
- `stream` (bool): Определяет, использовать ли потоковую передачу. По умолчанию `False`.
- `image` (Optional[str]): Путь к изображению. По умолчанию `None`.
- `image_name` (Optional[str]): Имя изображения. По умолчанию `None`.
- `images` (Optional[list[tuple[str, str]]]): Список кортежей (путь к изображению, имя изображения). По умолчанию `None`.
- `media` (Optional[list[tuple[str, str]]]): Список кортежей (путь к медиафайлу, имя медиафайла). По умолчанию `None`.
- `modalities` (Optional[list[str]]): Список модальностей (например, "text", "audio"). По умолчанию `["text", "audio"]`.
- `temperature` (Optional[float]): Температура для генерации текста. По умолчанию `None`.
- `presence_penalty` (Optional[float]): Штраф за присутствие токенов. По умолчанию `None`.
- `frequency_penalty` (Optional[float]): Штраф за частоту токенов. По умолчанию `None`.
- `top_p` (Optional[float]): Top-p значение для выбора токенов. По умолчанию `None`.
- `max_tokens` (Optional[int]): Максимальное количество токенов в ответе. По умолчанию `None`.
- `stop` (Union[list[str], str, None]): Список стоп-слов или одно стоп-слово. По умолчанию `None`.
- `api_key` (Optional[str]): Ключ API. По умолчанию `None`.
- `api_base` (str): Базовый URL API. По умолчанию `None`.
- `web_search` (Optional[bool]): Определяет, использовать ли веб-поиск. По умолчанию `None`.
- `proxy` (Optional[str]): Прокси-сервер. По умолчанию `None`.
- `conversation_id` (Optional[str]): Идентификатор разговора. По умолчанию `None`.
- `conversation` (Optional[dict]): Словарь с информацией о разговоре. По умолчанию `None`.
- `return_conversation` (Optional[bool]): Определяет, возвращать ли информацию о разговоре. По умолчанию `None`.
- `history_disabled` (Optional[bool]): Определяет, отключать ли историю разговоров. По умолчанию `None`.
- `timeout` (Optional[int]): Время ожидания запроса. По умолчанию `None`.
- `tool_calls` (list): Список инструментов для вызова.
- `tools` (list): Список доступных инструментов. По умолчанию `None`.
- `parallel_tool_calls` (bool): Разрешить параллельные вызовы инструментов. По умолчанию `None`.
- `tool_choice` (Optional[str]): Выбор инструмента. По умолчанию `None`.
- `reasoning_effort` (Optional[str]): Уровень усилий для рассуждений. По умолчанию `None`.
- `logit_bias` (Optional[dict]): Смещение логитов. По умолчанию `None`.
- `modalities` (Optional[list[str]]): Список модальностей (например, "text", "audio"). По умолчанию `None`.
- `audio` (Optional[dict]): Параметры аудио. По умолчанию `None`.
- `response_format` (Optional[dict]): Формат ответа. По умолчанию `None`.
- `extra_data` (Optional[dict]): Дополнительные данные. По умолчанию `None`.

**Примеры**

```python
config = ChatCompletionsConfig(
    messages=[{"role": "user", "content": "Hello"}],
    model="gpt-3.5-turbo",
    temperature=0.7
)
```

### `ImageGenerationConfig`

**Описание**: Класс конфигурации для запросов на генерацию изображений.

**Принцип работы**:
Класс `ImageGenerationConfig` определяет параметры, необходимые для запроса на генерацию изображения. Он включает в себя текстовое описание, модель, провайдера, формат ответа, ключ API, прокси, ширину, высоту, количество шагов, зерно, масштаб руководства, соотношение сторон, количество изображений, негативный запрос и разрешение.

**Параметры**:
- `prompt` (str): Текстовое описание изображения.
- `model` (Optional[str]): Имя модели для использования. По умолчанию `None`.
- `provider` (Optional[str]): Провайдер модели. По умолчанию `None`.
- `response_format` (Optional[str]): Формат ответа. По умолчанию `None`.
- `api_key` (Optional[str]): Ключ API. По умолчанию `None`.
- `proxy` (Optional[str]): Прокси-сервер. По умолчанию `None`.
- `width` (Optional[int]): Ширина изображения. По умолчанию `None`.
- `height` (Optional[int]): Высота изображения. По умолчанию `None`.
- `num_inference_steps` (Optional[int]): Количество шагов для генерации. По умолчанию `None`.
- `seed` (Optional[int]): Зерно для генерации. По умолчанию `None`.
- `guidance_scale` (Optional[int]): Масштаб руководства. По умолчанию `None`.
- `aspect_ratio` (Optional[str]): Соотношение сторон. По умолчанию `None`.
- `n` (Optional[int]): Количество изображений для генерации. По умолчанию `None`.
- `negative_prompt` (Optional[str]): Негативное описание. По умолчанию `None`.
- `resolution` (Optional[str]): Разрешение изображения. По умолчанию `None`.

**Примеры**

```python
config = ImageGenerationConfig(
    prompt="A cat sitting on a mat",
    model="dall-e-3",
    width=512,
    height=512
)
```

### `ProviderResponseModel`

**Описание**: Базовая модель ответа от провайдера.

**Принцип работы**:
Класс `ProviderResponseModel` представляет базовую структуру ответа от провайдера. Он содержит идентификатор, объект (всегда "provider"), время создания, URL и метку.

**Параметры**:
- `id` (str): Идентификатор ответа.
- `object` (str): Тип объекта (всегда "provider").
- `created` (int): Время создания.
- `url` (Optional[str]): URL. По умолчанию `None`.
- `label` (Optional[str]): Метка. По умолчанию `None`.

**Примеры**

```python
response = ProviderResponseModel(
    id="123",
    created=1678886400,
    url="http://example.com",
    label="Example"
)
```

### `ProviderResponseDetailModel`

**Описание**: Модель детального ответа от провайдера.

**Принцип работы**:
Класс `ProviderResponseDetailModel` расширяет `ProviderResponseModel` и добавляет информацию о моделях, моделях изображений, моделях зрения и параметрах, поддерживаемых провайдером.

**Параметры**:
- `id` (str): Идентификатор ответа.
- `object` (str): Тип объекта (всегда "provider").
- `created` (int): Время создания.
- `url` (Optional[str]): URL. По умолчанию `None`.
- `label` (Optional[str]): Метка. По умолчанию `None`.
- `models` (list[str]): Список поддерживаемых моделей.
- `image_models` (list[str]): Список поддерживаемых моделей изображений.
- `vision_models` (list[str]): Список поддерживаемых моделей зрения.
- `params` (list[str]): Список поддерживаемых параметров.

**Примеры**

```python
response = ProviderResponseDetailModel(
    id="456",
    created=1678886500,
    models=["gpt-3.5-turbo", "gpt-4"],
    image_models=["dall-e-3"],
    vision_models=[],
    params=["temperature", "top_p"]
)
```

### `ModelResponseModel`

**Описание**: Модель ответа о модели.

**Принцип работы**:
Класс `ModelResponseModel` представляет структуру ответа, содержащую информацию о модели. Он включает в себя идентификатор, объект (всегда "model"), время создания и владельца.

**Параметры**:
- `id` (str): Идентификатор модели.
- `object` (str): Тип объекта (всегда "model").
- `created` (int): Время создания.
- `owned_by` (Optional[str]): Владелец модели. По умолчанию `None`.

**Примеры**

```python
response = ModelResponseModel(
    id="gpt-3.5-turbo",
    created=1678886600,
    owned_by="openai"
)
```

### `UploadResponseModel`

**Описание**: Модель ответа на загрузку файла.

**Принцип работы**:
Класс `UploadResponseModel` представляет структуру ответа на загрузку файла. Он содержит идентификатор бакета и URL загруженного файла.

**Параметры**:
- `bucket_id` (str): Идентификатор бакета.
- `url` (str): URL загруженного файла.

**Примеры**

```python
response = UploadResponseModel(
    bucket_id="my-bucket",
    url="http://example.com/my-file.txt"
)
```

### `ErrorResponseModel`

**Описание**: Модель ответа об ошибке.

**Принцип работы**:
Класс `ErrorResponseModel` представляет структуру ответа об ошибке. Он содержит объект ошибки, модель и провайдера.

**Параметры**:
- `error` (ErrorResponseMessageModel): Объект ошибки.
- `model` (Optional[str]): Модель, вызвавшая ошибку. По умолчанию `None`.
- `provider` (Optional[str]): Провайдер, вызвавший ошибку. По умолчанию `None`.

**Примеры**

```python
error_message = ErrorResponseMessageModel(message="Something went wrong")
response = ErrorResponseModel(
    error=error_message,
    model="gpt-3.5-turbo"
)
```

### `ErrorResponseMessageModel`

**Описание**: Модель сообщения об ошибке.

**Принцип работы**:
Класс `ErrorResponseMessageModel` представляет структуру сообщения об ошибке. Он содержит сообщение об ошибке.

**Параметры**:
- `message` (str): Сообщение об ошибке.

**Примеры**

```python
message = ErrorResponseMessageModel(message="Something went wrong")
```

### `FileResponseModel`

**Описание**: Модель ответа о файле.

**Принцип работы**:
Класс `FileResponseModel` представляет структуру ответа, содержащую информацию о файле. Он включает имя файла.

**Параметры**:

- `filename` (str): Имя файла.

**Примеры**:

```python
response = FileResponseModel(filename="example.txt")