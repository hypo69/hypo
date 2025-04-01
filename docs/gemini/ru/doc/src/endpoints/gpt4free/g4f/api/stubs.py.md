# Модуль stubs

## Обзор

Модуль `stubs` содержит определения Pydantic моделей, используемых для конфигурации и обмена данными с API g4f (gpt4free). Эти модели описывают структуру запросов и ответов, используемых при взаимодействии с различными поставщиками (providers) и моделями. Модуль также включает обработку ошибок и вспомогательные классы для работы с данными.

## Подробнее

Модуль предоставляет статические структуры данных (модели), описывающие различные аспекты взаимодействия с API, включая конфигурацию чат-запросов, генерацию изображений, ответы провайдеров и моделей, а также обработку ошибок. Он используется для типизации данных и обеспечения соответствия структуры запросов и ответов ожидаемому формату.

## Классы

### `ChatCompletionsConfig`

**Описание**: Модель конфигурации для запросов завершения чата (chat completions).

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, определяет параметры, необходимые для запроса завершения чата. Включает в себя сообщения, модель, поставщика, параметры потоковой передачи, изображения, температуру, штрафы, максимальное количество токенов и другие параметры конфигурации.
Модель используется для структурирования и валидации данных, отправляемых в API для генерации чат-ответов.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `messages` (Messages): Список сообщений для чата. По умолчанию - пустой список с примером.
- `model` (str): Идентификатор модели. По умолчанию - пустая строка.
- `provider` (Optional[str]): Идентификатор поставщика. По умолчанию - `None`.
- `stream` (bool): Флаг потоковой передачи. По умолчанию - `False`.
- `image` (Optional[str]): Изображение. По умолчанию - `None`.
- `image_name` (Optional[str]): Имя изображения. По умолчанию - `None`.
- `images` (Optional[list[tuple[str, str]]]): Список изображений (путь и тип). По умолчанию - `None`.
- `media` (Optional[list[tuple[str, str]]]): Список медиафайлов (путь и тип). По умолчанию - `None`.
- `modalities` (Optional[list[str]]): Список модальностей (например, `["text", "audio"]`). По умолчанию - `["text", "audio"]`.
- `temperature` (Optional[float]): Температура для генерации текста. По умолчанию - `None`.
- `presence_penalty` (Optional[float]): Штраф за присутствие. По умолчанию - `None`.
- `frequency_penalty` (Optional[float]): Штраф за частоту. По умолчанию - `None`.
- `top_p` (Optional[float]): Top-p sampling. По умолчанию - `None`.
- `max_tokens` (Optional[int]): Максимальное количество токенов в ответе. По умолчанию - `None`.
- `stop` (Union[list[str], str, None]): Условия остановки генерации. По умолчанию - `None`.
- `api_key` (Optional[str]): Ключ API. По умолчанию - `None`.
- `api_base` (str): Базовый URL API. По умолчанию - `None`.
- `web_search` (Optional[bool]): Флаг использования веб-поиска. По умолчанию - `None`.
- `proxy` (Optional[str]): Прокси-сервер. По умолчанию - `None`.
- `conversation_id` (Optional[str]): Идентификатор разговора. По умолчанию - `None`.
- `conversation` (Optional[dict]): Словарь содержащий информацию о разговоре. По умолчанию - `None`.
- `return_conversation` (Optional[bool]): Флаг возврата информации о разговоре. По умолчанию - `None`.
- `history_disabled` (Optional[bool]): Флаг отключения истории. По умолчанию - `None`.
- `timeout` (Optional[int]): Время ожидания. По умолчанию - `None`.
- `tool_calls` (list): Список вызовов инструментов. По умолчанию - пустой список с примером.
- `tools` (list): Список инструментов. По умолчанию - `None`.
- `parallel_tool_calls` (bool): Флаг параллельных вызовов инструментов. По умолчанию - `None`.
- `tool_choice` (Optional[str]): Выбор инструмента. По умолчанию - `None`.
- `reasoning_effort` (Optional[str]): Уровень рассуждений. По умолчанию - `None`.
- `logit_bias` (Optional[dict]): Смещение логитов. По умолчанию - `None`.
- `modalities` (Optional[list[str]]): Список модальностей. По умолчанию - `None`.
- `audio` (Optional[dict]): Параметры аудио. По умолчанию - `None`.
- `response_format` (Optional[dict]): Формат ответа. По умолчанию - `None`.
- `extra_data` (Optional[dict]): Дополнительные данные. По умолчанию - `None`.

**Примеры**:

```python
from g4f.api.stubs import ChatCompletionsConfig, Messages

# Пример конфигурации с минимальными параметрами
config = ChatCompletionsConfig(messages=[{"role": "user", "content": "Hello"}], model="gpt-3.5-turbo")

# Пример конфигурации с расширенными параметрами
messages: Messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}]
config = ChatCompletionsConfig(
    messages=messages,
    model="gpt-4",
    provider="openai",
    stream=True,
    temperature=0.7,
    max_tokens=100,
    stop=["\n", "."],
)
```

### `ImageGenerationConfig`

**Описание**: Модель конфигурации для запросов генерации изображений.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, определяет параметры, необходимые для запроса генерации изображений. Включает в себя prompt, модель, поставщика, формат ответа, API ключ, прокси, размеры изображения, количество шагов вывода, seed, scale, aspect_ratio и другие параметры конфигурации.
Модель используется для структурирования и валидации данных, отправляемых в API для генерации изображений.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `prompt` (str): Текстовое описание желаемого изображения.
- `model` (Optional[str]): Идентификатор модели. По умолчанию - `None`.
- `provider` (Optional[str]): Идентификатор поставщика. По умолчанию - `None`.
- `response_format` (Optional[str]): Формат ответа (например, "url" или "base64"). По умолчанию - `None`.
- `api_key` (Optional[str]): Ключ API. По умолчанию - `None`.
- `proxy` (Optional[str]): Прокси-сервер. По умолчанию - `None`.
- `width` (Optional[int]): Ширина изображения. По умолчанию - `None`.
- `height` (Optional[int]): Высота изображения. По умолчанию - `None`.
- `num_inference_steps` (Optional[int]): Количество шагов вывода. По умолчанию - `None`.
- `seed` (Optional[int]): Зерно для генерации случайных чисел. По умолчанию - `None`.
- `guidance_scale` (Optional[float]): Масштаб руководства. По умолчанию - `None`.
- `aspect_ratio` (Optional[str]): Соотношение сторон изображения. По умолчанию - `None`.
- `n` (Optional[int]): Количество сгенерированных изображений. По умолчанию - `None`.
- `negative_prompt` (Optional[str]): Негативный промпт (чего не должно быть на изображении). По умолчанию - `None`.
- `resolution` (Optional[str]): Разрешение изображения. По умолчанию - `None`.

**Примеры**:

```python
from g4f.api.stubs import ImageGenerationConfig

# Пример конфигурации с минимальными параметрами
config = ImageGenerationConfig(prompt="A cat sitting on a mat")

# Пример конфигурации с расширенными параметрами
config = ImageGenerationConfig(
    prompt="A futuristic cityscape at sunset",
    model="dall-e-3",
    provider="openai",
    response_format="url",
    width=1024,
    height=1024,
    num_inference_steps=50,
    seed=42,
)
```

### `ProviderResponseModel`

**Описание**: Модель ответа от поставщика (provider).

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру ответа, полученного от поставщика услуг. Он содержит идентификатор, тип объекта (всегда "provider"), время создания, URL и метку (label).

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `id` (str): Уникальный идентификатор ответа поставщика.
- `object` (str): Тип объекта (всегда "provider").
- `created` (int): Время создания ответа (timestamp).
- `url` (Optional[str]): URL, связанный с ответом (например, URL изображения). По умолчанию - `None`.
- `label` (Optional[str]): Метка (label) ответа. По умолчанию - `None`.

**Примеры**:

```python
from g4f.api.stubs import ProviderResponseModel

# Пример создания модели ответа поставщика
response = ProviderResponseModel(
    id="12345",
    created=1678886400,
    url="https://example.com/image.jpg",
    label="Generated image",
)
```

### `ProviderResponseDetailModel`

**Описание**: Модель детального ответа от поставщика.

**Принцип работы**: Этот класс, наследуемый от `ProviderResponseModel`, расширяет модель ответа от поставщика, добавляя списки поддерживаемых моделей, моделей изображений, моделей машинного зрения и параметров.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `models` (list[str]): Список идентификаторов поддерживаемых моделей.
- `image_models` (list[str]): Список идентификаторов моделей для генерации изображений.
- `vision_models` (list[str]): Список идентификаторов моделей машинного зрения.
- `params` (list[str]): Список поддерживаемых параметров.
- Наследует все параметры от `ProviderResponseModel`.

**Примеры**:

```python
from g4f.api.stubs import ProviderResponseDetailModel

# Пример создания модели детального ответа поставщика
response = ProviderResponseDetailModel(
    id="67890",
    created=1678886400,
    models=["gpt-3.5-turbo", "gpt-4"],
    image_models=["dall-e-2", "dall-e-3"],
    vision_models=[],
    params=["temperature", "max_tokens"],
)
```

### `ModelResponseModel`

**Описание**: Модель ответа о модели.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру ответа, содержащую информацию о конкретной модели. Он содержит идентификатор модели, тип объекта (всегда "model"), время создания и владельца модели.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `id` (str): Уникальный идентификатор модели.
- `object` (str): Тип объекта (всегда "model").
- `created` (int): Время создания записи о модели (timestamp).
- `owned_by` (Optional[str]): Владелец модели. По умолчанию - `None`.

**Примеры**:

```python
from g4f.api.stubs import ModelResponseModel

# Пример создания модели ответа о модели
response = ModelResponseModel(
    id="gpt-3.5-turbo",
    created=1678886400,
    owned_by="openai",
)
```

### `UploadResponseModel`

**Описание**: Модель ответа на загрузку файла.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру ответа, полученного после загрузки файла. Он содержит идентификатор бакета (bucket_id) и URL загруженного файла.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `bucket_id` (str): Идентификатор бакета, в который был загружен файл.
- `url` (str): URL загруженного файла.

**Примеры**:

```python
from g4f.api.stubs import UploadResponseModel

# Пример создания модели ответа на загрузку файла
response = UploadResponseModel(
    bucket_id="my-bucket",
    url="https://example.com/my-bucket/uploaded_file.txt",
)
```

### `ErrorResponseModel`

**Описание**: Модель ответа об ошибке.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру ответа об ошибке. Он содержит объект `ErrorResponseMessageModel`, который содержит сообщение об ошибке, а также идентификаторы модели и поставщика, если они применимы.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `error` (ErrorResponseMessageModel): Модель сообщения об ошибке.
- `model` (Optional[str]): Идентификатор модели, вызвавшей ошибку. По умолчанию - `None`.
- `provider` (Optional[str]): Идентификатор поставщика, вызвавшего ошибку. По умолчанию - `None`.

**Примеры**:

```python
from g4f.api.stubs import ErrorResponseModel, ErrorResponseMessageModel

# Пример создания модели ответа об ошибке
error_message = ErrorResponseMessageModel(message="Invalid API key")
response = ErrorResponseModel(
    error=error_message,
    model="gpt-3.5-turbo",
    provider="openai",
)
```

### `ErrorResponseMessageModel`

**Описание**: Модель сообщения об ошибке.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру сообщения об ошибке. Он содержит только поле `message` с текстом сообщения об ошибке.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:
- `message` (str): Текст сообщения об ошибке.

**Примеры**:

```python
from g4f.api.stubs import ErrorResponseMessageModel

# Пример создания модели сообщения об ошибке
message = ErrorResponseMessageModel(message="Request failed with status code 404")
```

### `FileResponseModel`

**Описание**: Модель ответа, содержащая информацию о файле.

**Принцип работы**: Этот класс, наследуемый от `BaseModel`, представляет структуру ответа, содержащую имя файла.

**Методы**: Отсутствуют явно определенные методы, так как класс является моделью данных.

**Параметры**:

- `filename` (str): Имя файла.

**Примеры**:

```python
from g4f.api.stubs import FileResponseModel

# Пример создания модели ответа с информацией о файле
file_info = FileResponseModel(filename="example.txt")
```

## Функции

В данном модуле нет явно определенных функций, только классы моделей данных.