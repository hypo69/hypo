# Модуль HuggingFaceInference

## Обзор

Модуль `HuggingFaceInference` предоставляет асинхронный генератор для взаимодействия с моделями Hugging Face Inference API.
Он включает в себя поддержку текстовых и графических моделей, а также обработку различных форматов запросов.

## Подробнее

Этот модуль позволяет использовать модели машинного обучения, размещенные на платформе Hugging Face, для генерации текста и изображений. Он поддерживает потоковую передачу данных для текстовых моделей и сохранение медиа-файлов для графических моделей. Модуль содержит классы и методы для обработки API-запросов к Hugging Face, включая обработку ошибок и выбор оптимальных моделей.

## Классы

### `HuggingFaceInference`

**Описание**: Класс `HuggingFaceInference` предоставляет асинхронный генератор для взаимодействия с API Hugging Face Inference.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Добавляет функциональность выбора и управления моделями.

**Атрибуты**:
- `url` (str): URL Hugging Face.
- `parent` (str): Имя родительского провайдера.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию.
- `default_image_model` (str): Графическая модель, используемая по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список графических моделей.
- `model_data` (dict[str, dict]): Кеш данных моделей.

**Методы**:
- `get_models()`: Возвращает список поддерживаемых моделей.
- `get_model_data(session: StreamSession, model: str) -> str`: Получает данные о модели из API Hugging Face.
- `create_async_generator(...)`: Создает асинхронный генератор для выполнения запросов к API Hugging Face.

#### `get_models`

```python
@classmethod
def get_models(cls) -> list[str]:
    """Возвращает список поддерживаемых моделей.

    Args:
        cls: Ссылка на класс.

    Returns:
        list[str]: Список поддерживаемых моделей.
    """
    ...
```

**Назначение**: Метод `get_models` возвращает список доступных моделей, которые можно использовать через API Hugging Face Inference.

**Как работает функция**:
1. Проверяет, был ли уже инициализирован список моделей (`cls.models`).
2. Если список моделей пуст, инициализирует его, начиная с копии `text_models`.
3. Выполняет HTTP-запрос к API Hugging Face для получения списка моделей с тегом `text-generation` и `trendingScore` >= 10.
4. Добавляет полученные модели в список, а также модели из `vision_models`.
5. Аналогично, выполняет HTTP-запрос для получения списка моделей с тегом `text-to-image` и `trendingScore` >= 20, добавляя их в `cls.image_models`.
6. Объединяет списки текстовых и графических моделей, исключая дубликаты.
7. Сохраняет полученный список в `cls.models` и возвращает его.

**ASCII flowchart**:
```
A (Проверка cls.models)
│
├──→ B (Если cls.models пуст)
│   │
│   ├──→ C (Инициализация models = text_models.copy())
│   │   │
│   │   ├──→ D (HTTP-запрос к API Hugging Face для text-generation)
│   │   │   │
│   │   │   ├──→ E (Обработка ответа и добавление моделей)
│   │   │   │
│   │   │   ├──→ F (Добавление vision_models)
│   │   │
│   │   ├──→ G (HTTP-запрос к API Hugging Face для text-to-image)
│   │   │   │
│   │   │   ├──→ H (Обработка ответа и добавление моделей в cls.image_models)
│   │   │
│   │   ├──→ I (Объединение списков моделей)
│   │   │
│   │   └──→ J (Сохранение и возврат cls.models)
│   │
│   └──→ K (Если cls.models не пуст)
│       │
│       └──→ L (Возврат существующего cls.models)
│
└──→ M (Возврат cls.models)
```
**Примеры**:

```python
# Пример вызова метода get_models
models = HuggingFaceInference.get_models()
print(models)
```

#### `get_model_data`

```python
@classmethod
async def get_model_data(cls, session: StreamSession, model: str) -> str:
    """Получает данные о модели из API Hugging Face.

    Args:
        session (StreamSession): Асинхровая сессия для выполнения HTTP-запросов.
        model (str): Имя модели.

    Returns:
        str: Данные о модели в формате JSON.

    Raises:
        ModelNotSupportedError: Если модель не поддерживается.
    """
    ...
```

**Назначение**: Метод `get_model_data` асинхронно получает информацию о конкретной модели из API Hugging Face.

**Как работает функция**:
1. Проверяет, есть ли данные о модели в кеше `cls.model_data`. Если есть, возвращает их.
2. Если данных в кеше нет, выполняет асинхронный HTTP-запрос к API Hugging Face для получения информации о модели.
3. Обрабатывает ответ: если статус код 404, выбрасывает исключение `ModelNotSupportedError`.
4. Сохраняет полученные данные в кеше `cls.model_data` и возвращает их.

**ASCII flowchart**:
```
A (Проверка наличия данных о модели в cls.model_data)
│
├──→ B (Если данные есть)
│   │
│   └──→ C (Возврат данных из cls.model_data)
│
└──→ D (Если данных нет)
    │
    ├──→ E (Асинхронный HTTP-запрос к API Hugging Face)
    │   │
    │   ├──→ F (Проверка статус кода ответа)
    │   │   │
    │   │   ├──→ G (Если статус код 404, выброс ModelNotSupportedError)
    │   │   │
    │   │   └──→ H (Сохранение данных в cls.model_data)
    │   │
    │   └──→ I (Возврат данных о модели)
    │
    └──→ J (Возврат данных о модели)
```

**Примеры**:

```python
# Пример вызова метода get_model_data
import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        model_data = await HuggingFaceInference.get_model_data(session, "gpt2")
        print(model_data)

asyncio.run(main())
```

#### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    proxy: str = None,
    timeout: int = 600,
    api_base: str = "https://api-inference.huggingface.co",
    api_key: str = None,
    max_tokens: int = 1024,
    temperature: float = None,
    prompt: str = None,
    action: str = None,
    extra_data: dict = {},
    seed: int = None,
    aspect_ratio: str = None,
    width: int = None,
    height: int = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для выполнения запросов к API Hugging Face.

    Args:
        model (str): Имя модели.
        messages (Messages): Список сообщений для отправки.
        stream (bool): Флаг потоковой передачи данных.
        proxy (str): URL прокси-сервера.
        timeout (int): Время ожидания запроса.
        api_base (str): Базовый URL API Hugging Face.
        api_key (str): Ключ API.
        max_tokens (int): Максимальное количество токенов в ответе.
        temperature (float): Температура для генерации текста.
        prompt (str): Дополнительный промпт.
        action (str): Действие ("continue" для продолжения генерации).
        extra_data (dict): Дополнительные данные для запроса.
        seed (int): Зерно для генерации случайных чисел.
        aspect_ratio (str): Соотношение сторон изображения.
        width (int): Ширина изображения.
        height (int): Высота изображения.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор результатов.

    Raises:
        ModelNotSupportedError: Если модель не поддерживается.
        ResponseError: Если произошла ошибка в ответе от API.
    """
    ...
```

**Назначение**: Метод `create_async_generator` создает и возвращает асинхронный генератор для взаимодействия с API Hugging Face Inference. Он позволяет выполнять запросы к различным моделям, поддерживая как текстовую, так и графическую генерацию, а также потоковую передачу данных.

**Как работает функция**:

1.  **Инициализация**:
    *   Пытается получить модель с помощью `cls.get_model(model)`. Если модель не поддерживается, переходит к следующему шагу.
    *   Формирует заголовки запроса, включая `Content-Type` и `Authorization` (если предоставлен `api_key`).
    *   Определяет дополнительные данные для запросов к графическим моделям, используя `use_aspect_ratio`.
2.  **Создание сессии**:
    *   Инициализирует `StreamSession` с заданными заголовками, прокси и таймаутом.
3.  **Обработка запроса**:
    *   **Together AI Models**:
        *   Если модель находится в списке `provider_together_urls`, формирует запрос к API Together AI для генерации изображений.
        *   Формирует данные запроса, включая `prompt`, `model` и `image_extra_data`.
        *   Выполняет POST-запрос к API.
        *   Если запрос успешен, извлекает URL изображений из ответа и возвращает `ImageResponse`.
    *   **Hugging Face Models**:
        *   Если модель не поддерживается, определяет `payload` и `params` для запроса.
        *   Получает данные модели с помощью `cls.get_model_data(session, model)`.
        *   Определяет `pipeline_tag` модели.
        *   **Text-to-Image**:
            *   Если `pipeline_tag` равен "text-to-image", формирует `payload` с использованием `format_image_prompt` и случайного `seed`.
            *   Выполняет POST-запрос к API и возвращает `ImageResponse`.
        *   **Text-Generation или Image-to-Text**:
            *   Если `pipeline_tag` равен "text-generation" или "image-text-to-text", формирует `inputs` с использованием `get_inputs`.
            *   Если длина `inputs` превышает 4096, усекает `messages`.
            *   Формирует `payload` с использованием `inputs`, `params` и флага `stream`.
            *   Выполняет POST-запрос к API.
            *   Если `stream` равен `True` (потоковая передача):
                *   Обрабатывает ответ построчно, извлекая текст из каждой строки данных.
                *   Пропускает специальные токены.
                *   Возвращает текст чанками через `yield`.
            *   Если `stream` равен `False` (непотоковая передача):
                *   Сохраняет медиа-файлы с использованием `save_response_media`.
                *   Возвращает сгенерированный текст.
4.  **Обработка ошибок**:
    *   Обрабатывает `ModelNotSupportedError` и `ResponseError`.
    *   Логирует ошибки с использованием `logger.error`.

**ASCII flowchart**:

```
A (Инициализация)
│
├──→ B (Создание сессии StreamSession)
│   │
│   ├──→ C (Обработка запроса)
│   │   │
│   │   ├──→ D (Проверка модели в provider_together_urls)
│   │   │   │
│   │   │   ├──→ E (Формирование запроса к Together AI)
│   │   │   │   │
│   │   │   │   └──→ F (Выполнение POST-запроса к API Together AI)
│   │   │   │   │
│   │   │   │   └──→ G (Обработка ответа и возврат ImageResponse)
│   │   │   │
│   │   │   └──→ H (Формирование payload и params для Hugging Face)
│   │   │   │
│   │   │   └──→ I (Получение данных модели)
│   │   │   │
│   │   │   └──→ J (Определение pipeline_tag)
│   │   │   │
│   │   │   ├──→ K (Text-to-Image)
│   │   │   │   │
│   │   │   │   └──→ L (Формирование payload с format_image_prompt)
│   │   │   │   │
│   │   │   │   └──→ M (Выполнение POST-запроса и возврат ImageResponse)
│   │   │   │
│   │   │   └──→ N (Text-Generation или Image-to-Text)
│   │   │   │   │
│   │   │   │   └──→ O (Формирование inputs с get_inputs)
│   │   │   │   │
│   │   │   │   └──→ P (Выполнение POST-запроса)
│   │   │   │   │
│   │   │   │   ├──→ Q (stream == True)
│   │   │   │   │   │
│   │   │   │   │   └──→ R (Обработка потокового ответа)
│   │   │   │   │   │
│   │   │   │   │   └──→ S (Возврат текста чанками через yield)
│   │   │   │   │
│   │   │   │   └──→ T (stream == False)
│   │   │   │   │   │
│   │   │   │   │   └──→ U (Сохранение медиа-файлов)
│   │   │   │   │   │
│   │   │   │   │   └──→ V (Возврат сгенерированного текста)
│   │   │   │
│   │   │   └──→ W (Обработка ошибок)
│   │   │
│   │   └──→ X (Возврат асинхронного генератора)
│   │
│   └──→ Y (Обработка исключений)
│
└──→ Z (Конец)
```

**Примеры**:

```python
# Пример вызова метода create_async_generator
import asyncio
from aiohttp import ClientSession

async def main():
    messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
    async for chunk in HuggingFaceInference.create_async_generator(model="gpt2", messages=messages):
        print(chunk, end="")

asyncio.run(main())
```

## Функции

### `format_prompt_mistral`

```python
def format_prompt_mistral(messages: Messages, do_continue: bool = False) -> str:
    """Форматирует промпт для модели Mistral.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Сформатированный промпт.
    """
    ...
```

**Назначение**: Функция `format_prompt_mistral` форматирует список сообщений в строку, пригодную для использования в качестве промпта для моделей Mistral.

**Как работает функция**:

1.  Извлекает все системные сообщения из списка `messages`.
2.  Формирует вопрос, объединяя последнее сообщение пользователя с системными сообщениями.
3.  Собирает историю взаимодействий, форматируя сообщения пользователя и ассистента в формате `<s>[INST]...[/INST]...</s>`.
4.  Если `do_continue` равно `True`, возвращает историю без завершающего тега `</s>`.
5.  Если `do_continue` равно `False`, добавляет к истории вопрос в формате `<s>[INST]...[/INST]`.

**ASCII flowchart**:

```
A (Извлечение системных сообщений)
│
├──→ B (Формирование вопроса)
│   │
│   └──→ C (Сборка истории взаимодействий)
│       │
│       ├──→ D (Проверка do_continue)
│       │   │
│       │   ├──→ E (do_continue == True: возврат истории без </s>)
│       │   │
│       │   └──→ F (do_continue == False: добавление вопроса к истории)
│       │
│       └──→ G (Возврат отформатированного промпта)
│
└──→ H (Конец)
```

**Примеры**:

```python
# Пример вызова функции format_prompt_mistral
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
prompt = format_prompt_mistral(messages)
print(prompt)
```

### `format_prompt_qwen`

```python
def format_prompt_qwen(messages: Messages, do_continue: bool = False) -> str:
    """Форматирует промпт для модели Qwen.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Сформатированный промпт.
    """
    ...
```

**Назначение**: Функция `format_prompt_qwen` форматирует список сообщений в строку, пригодную для использования в качестве промпта для моделей Qwen.

**Как работает функция**:

1.  Собирает сообщения, форматируя их в виде `<|im_start|>role\\ncontent\\n<|im_end|>\\n`.
2.  Если `do_continue` равно `False`, добавляет `<|im_start|>assistant\\n`.
3.  Если `do_continue` равно `True`, удаляет `\\n<|im_end|>\\n` из конца строки.

**ASCII flowchart**:

```
A (Форматирование сообщений)
│
├──→ B (Проверка do_continue)
│   │
│   ├──→ C (do_continue == False: добавление <|im_start|>assistant\\n)
│   │
│   └──→ D (do_continue == True: удаление \\n<|im_end|>\\n)
│
└──→ E (Возврат отформатированного промпта)
```

**Примеры**:

```python
# Пример вызова функции format_prompt_qwen
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
prompt = format_prompt_qwen(messages)
print(prompt)
```

### `format_prompt_qwen2`

```python
def format_prompt_qwen2(messages: Messages, do_continue: bool = False) -> str:
    """Форматирует промпт для модели Qwen2.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Сформатированный промпт.
    """
    ...
```

**Назначение**: Функция `format_prompt_qwen2` форматирует список сообщений в строку, пригодную для использования в качестве промпта для моделей Qwen2.

**Как работает функция**:

1.  Собирает сообщения, форматируя их в виде `\\u003C｜Role｜\\u003EContent\\u003C｜end of sentence｜\\u003E`.
2.  Если `do_continue` равно `False`, добавляет `\\u003C｜Assistant｜\\u003E`.
3.  Если `do_continue` равно `True`, удаляет `\\u003C｜Assistant｜\\u003E` из конца строки.

**ASCII flowchart**:

```
A (Форматирование сообщений)
│
├──→ B (Проверка do_continue)
│   │
│   ├──→ C (do_continue == False: добавление \\u003C｜Assistant｜\\u003E)
│   │
│   └──→ D (do_continue == True: удаление \\u003C｜Assistant｜\\u003E)
│
└──→ E (Возврат отформатированного промпта)
```

**Примеры**:

```python
# Пример вызова функции format_prompt_qwen2
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
prompt = format_prompt_qwen2(messages)
print(prompt)
```

### `format_prompt_llama`

```python
def format_prompt_llama(messages: Messages, do_continue: bool = False) -> str:
    """Форматирует промпт для модели Llama.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Сформатированный промпт.
    """
    ...
```

**Назначение**: Функция `format_prompt_llama` форматирует список сообщений в строку, пригодную для использования в качестве промпта для моделей Llama.

**Как работает функция**:

1.  Собирает сообщения, форматируя их в виде `<|start_header_id|>role<|end_header_id|>\\n\\ncontent\\n<|eot_id|>\\n`.
2.  Если `do_continue` равно `False`, добавляет `<|start_header_id|>assistant<|end_header_id|>\\n\\n`.
3.  Если `do_continue` равно `True`, удаляет `\\n<|eot_id|>\\n` из конца строки.

**ASCII flowchart**:

```
A (Форматирование сообщений)
│
├──→ B (Проверка do_continue)
│   │
│   ├──→ C (do_continue == False: добавление <|start_header_id|>assistant<|end_header_id|>\\n\\n)
│   │
│   └──→ D (do_continue == True: удаление \\n<|eot_id|>\\n)
│
└──→ E (Возврат отформатированного промпта)
```

**Примеры**:

```python
# Пример вызова функции format_prompt_llama
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
prompt = format_prompt_llama(messages)
print(prompt)
```

### `format_prompt_custom`

```python
def format_prompt_custom(messages: Messages, end_token: str = "</s>", do_continue: bool = False) -> str:
    """Форматирует промпт с пользовательским токеном конца.

    Args:
        messages (Messages): Список сообщений.
        end_token (str): Токен конца сообщения.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Сформатированный промпт.
    """
    ...
```

**Назначение**: Функция `format_prompt_custom` форматирует список сообщений в строку, используя заданный токен конца сообщения.

**Как работает функция**:

1.  Собирает сообщения, форматируя их в виде `<|role|>\\ncontent{end_token}\\n`.
2.  Если `do_continue` равно `False`, добавляет `<|assistant|>\\n`.
3.  Если `do_continue` равно `True`, удаляет `end_token + "\\n"` из конца строки.

**ASCII flowchart**:

```
A (Форматирование сообщений)
│
├──→ B (Проверка do_continue)
│   │
│   ├──→ C (do_continue == False: добавление <|assistant|>\\n)
│   │
│   └──→ D (do_continue == True: удаление end_token + "\\n")
│
└──→ E (Возврат отформатированного промпта)
```

**Примеры**:

```python
# Пример вызова функции format_prompt_custom
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
prompt = format_prompt_custom(messages, end_token="<|file_separator|>")
print(prompt)
```

### `get_inputs`

```python
def get_inputs(messages: Messages, model_data: dict, model_type: str, do_continue: bool = False) -> str:
    """Получает входные данные для модели.

    Args:
        messages (Messages): Список сообщений.
        model_data (dict): Данные о модели.
        model_type (str): Тип модели.
        do_continue (bool): Флаг продолжения генерации.

    Returns:
        str: Входные данные для модели.
    """
    ...
```

**Назначение**: Функция `get_inputs` выбирает и применяет соответствующую функцию форматирования промпта в зависимости от типа модели.

**Как работает функция**:

1.  Проверяет `model_type`:
    *   Если `model_type` равен "gpt2", "gpt_neo", "gemma" или "gemma2", использует `format_prompt`.
    *   Если `model_type` равен "mistral" и `model_data["author"]` равен "mistralai", использует `format_prompt_mistral`.
    *   Иначе, проверяет наличие `eos_token` в `model_data["config"]["tokenizer_config"]`:
        *   Если `eos_token` равен "<|endoftext|>", "<eos>" или "</s>", использует `format_prompt_custom`.
        *   Если `eos_token` равен "<|im_end|>", использует `format_prompt_qwen`.
        *   Если `eos_token["content"]` равен "\\u003C｜end of sentence｜\\u003E", использует `format_prompt_qwen2`.
        *   Если `eos_token` равен "<|eot_id|>", использует `format_prompt_llama`.
        *   Иначе, использует `format_prompt`.
2.  Возвращает отформатированный промпт.

**ASCII flowchart**:

```
A (Проверка model_type)
│
├──→ B (model_type in ("gpt2", "gpt_neo", "gemma", "gemma2"): format_prompt)
│   │
├──→ C (model_type == "mistral" and model_data["author"] == "mistralai": format_prompt_mistral)
│   │
└──→ D (Проверка eos_token)
    │
    ├──→ E (eos_token in ("<|endoftext|>", "<eos>", "</s>"): format_prompt_custom)
    │
    ├──→ F (eos_token == "<|im_end|>": format_prompt_qwen)
    │
    ├──→ G (eos_token["content"] == "\\u003C｜end of sentence｜\\u003E": format_prompt_qwen2)
    │
    ├──→ H (eos_token == "<|eot_id|>": format_prompt_llama)
    │
    └──→ I (default: format_prompt)
```

**Примеры**:

```python
# Пример вызова функции get_inputs
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
model_data = {"config": {"tokenizer_config": {"eos_token": "<|file_separator|>"}}}
model_type = "custom"
inputs = get_inputs(messages, model_data, model_type)
print(inputs)
```