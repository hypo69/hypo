# Модуль HuggingFaceInference

## Обзор

Модуль `HuggingFaceInference` предоставляет асинхронный генератор для взаимодействия с моделями Hugging Face Inference API.
Он включает в себя поддержку текстовых и графических моделей, а также обработку различных форматов подсказок и потоковой передачи ответов.

## Подробней

Этот модуль позволяет взаимодействовать с API Hugging Face Inference для генерации текста и изображений.
Он поддерживает различные модели, включая модели от `black-forest-labs`, и автоматически определяет необходимые параметры и форматы запросов.
Модуль также обрабатывает потоковую передачу ответов и сохранение сгенерированных изображений.

## Классы

### `HuggingFaceInference`

**Описание**: Класс для асинхронного взаимодействия с API Hugging Face Inference.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL API Hugging Face.
- `parent` (str): Имя родительского провайдера ("HuggingFace").
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию для генерации текста.
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список поддерживаемых моделей изображений.
- `model_data` (dict[str, dict]): Кэш данных моделей.

**Методы**:
- `get_models()`: Возвращает список доступных моделей.
- `get_model_data(session: StreamSession, model: str) -> str`: Получает данные о модели из API.
- `create_async_generator(...)`: Создает асинхронный генератор для выполнения запросов к API.

### `get_models`

```python
    @classmethod
    def get_models(cls) -> list[str]:
        """Возвращает список доступных моделей.

        Returns:
            list[str]: Список доступных моделей.
        """
```

**Назначение**: Получение списка доступных моделей из API Hugging Face.

**Как работает функция**:
1. Проверяет, был ли уже получен список моделей (`cls.models`). Если да, возвращает его.
2. Инициализирует список `models` копией `text_models`.
3. Выполняет GET-запрос к API Hugging Face для получения списка моделей, поддерживающих `text-generation`.
4. Если запрос успешен, добавляет модели с `trendingScore` >= 10 в список `extra_models`.
5. Объединяет `extra_models`, `vision_models` и `models`, исключая дубликаты.
6. Выполняет GET-запрос к API Hugging Face для получения списка моделей, поддерживающих `text-to-image`.
7. Обновляет `cls.image_models` и добавляет модели с `trendingScore` >= 20 из ответа.
8. Добавляет модели из `cls.image_models`, которых еще нет в `models`.
9. Сохраняет полученный список в `cls.models` и возвращает его.

```
  Проверка наличия cls.models
  │
  └──► Инициализация списка models из text_models
       │
       └──► GET-запрос к API для text-generation
            │
            └──► Обработка ответа и добавление моделей в extra_models
                 │
                 └──► Объединение списков моделей
                      │
                      └──► GET-запрос к API для text-to-image
                           │
                           └──► Обработка ответа и обновление cls.image_models
                                │
                                └──► Добавление моделей из cls.image_models в models
                                     │
                                     └──► Сохранение и возврат списка models
```

**Примеры**:
```python
models = HuggingFaceInference.get_models()
print(models)
```

### `get_model_data`

```python
    @classmethod
    async def get_model_data(cls, session: StreamSession, model: str) -> str:
        """Получает данные о модели из API.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения запросов.
            model (str): Имя модели.

        Returns:
            str: Данные модели в формате JSON.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
        """
```

**Назначение**: Получение данных о конкретной модели из API Hugging Face.

**Параметры**:
- `session` (`StreamSession`): Асинхронная сессия для выполнения HTTP-запросов.
- `model` (`str`): Идентификатор модели, для которой требуется получить данные.

**Возвращает**:
- `str`: Данные модели в формате JSON.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается API.

**Как работает функция**:

1.  **Проверка кэша**: Проверяет, есть ли данные для указанной модели в кэше `cls.model_data`. Если да, возвращает закэшированные данные.

2.  **Выполнение GET-запроса**: Если данные в кэше отсутствуют, выполняет GET-запрос к API Hugging Face для получения информации о модели.

3.  **Обработка ошибок**: Если статус ответа 404, вызывает исключение `ModelNotSupportedError`.

4.  **Сохранение и возврат данных**: Сохраняет полученные данные в кэш `cls.model_data` и возвращает их.

```
Проверка наличия данных в кэше
│
└──► Выполнение GET-запроса к API
     │
     └──► Обработка ошибок (404 -> ModelNotSupportedError)
          │
          └──► Сохранение данных в кэш
               │
               └──► Возврат данных
```

**Примеры**:

```python
async def get_data():
    async with StreamSession() as session:
        data = await HuggingFaceInference.get_model_data(session, "gpt2")
        print(data)
```

### `create_async_generator`

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
            messages (Messages): Список сообщений для формирования запроса.
            stream (bool, optional): Включить потоковую передачу. По умолчанию True.
            proxy (str, optional): URL прокси-сервера. По умолчанию None.
            timeout (int, optional): Время ожидания запроса. По умолчанию 600.
            api_base (str, optional): Базовый URL API. По умолчанию "https://api-inference.huggingface.co".
            api_key (str, optional): API ключ. По умолчанию None.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 1024.
            temperature (float, optional): Температура для генерации. По умолчанию None.
            prompt (str, optional): Дополнительный промпт. По умолчанию None.
            action (str, optional): Действие (например, "continue"). По умолчанию None.
            extra_data (dict, optional): Дополнительные данные для запроса. По умолчанию {}.
            seed (int, optional): Зерно для воспроизводимости результатов. По умолчанию None.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию None.
            width (int, optional): Ширина изображения. По умолчанию None.
            height (int, optional): Высота изображения. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Yields:
            str | ImageResponse: Части ответа или объект ImageResponse.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
            ResponseError: Если произошла ошибка в ответе от API.
        """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API Hugging Face.

**Параметры**:
- `model` (`str`): Имя используемой модели.
- `messages` (`Messages`): Список сообщений для формирования запроса.
- `stream` (`bool`, optional): Включить потоковую передачу данных. По умолчанию `True`.
- `proxy` (`str`, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (`int`, optional): Максимальное время ожидания запроса в секундах. По умолчанию 600.
- `api_base` (`str`, optional): Базовый URL API. По умолчанию `"https://api-inference.huggingface.co"`.
- `api_key` (`str`, optional): Ключ API для аутентификации. По умолчанию `None`.
- `max_tokens` (`int`, optional): Максимальное количество токенов в ответе. По умолчанию 1024.
- `temperature` (`float`, optional): Температура для генерации текста. По умолчанию `None`.
- `prompt` (`str`, optional): Дополнительный промпт для запроса. По умолчанию `None`.
- `action` (`str`, optional): Действие, которое нужно выполнить (например, "continue"). По умолчанию `None`.
- `extra_data` (`dict`, optional): Дополнительные данные для передачи в запросе. По умолчанию `{}`.
- `seed` (`int`, optional): Зерно для генерации случайных чисел, для воспроизводимости результатов. По умолчанию `None`.
- `aspect_ratio` (`str`, optional): Соотношение сторон изображения. По умолчанию `None`.
- `width` (`int`, optional): Ширина изображения. По умолчанию `None`.
- `height` (`int`, optional): Высота изображения. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, которые могут потребоваться.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий части ответа от API. Может возвращать строки текста или объекты `ImageResponse`.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если указанная модель не поддерживается.
- `ResponseError`: Если API возвращает ошибку.

**Как работает функция**:

1.  **Подготовка заголовков**: Создает заголовки для HTTP-запроса, включая `Content-Type` и, при необходимости, `Authorization` с API-ключом.
    
2.  **Обработка параметров изображения**: Если указаны `aspect_ratio`, `width` или `height`, формирует параметры для генерации изображений.
    
3.  **Создание сессии**: Создает асинхронную сессию `StreamSession` для выполнения запросов.
    
4.  **Обработка моделей `black-forest-labs`**: Если модель находится в списке `provider_together_urls`, формирует запрос к соответствующему URL для генерации изображения и возвращает URL изображения в объекте `ImageResponse`.
    
5.  **Формирование полезной нагрузки (payload)**:
    
    *   Определяет тип задачи (генерация текста или изображения) на основе `pipeline_tag` в данных модели.
    *   Для генерации текста формирует `inputs` с использованием функций `get_inputs` и параметров модели.
    *   Для генерации изображений формирует `inputs` с использованием `format_image_prompt`.
        
6.  **Выполнение POST-запроса**: Отправляет POST-запрос к API Hugging Face с сформированной полезной нагрузкой.
    
7.  **Обработка потоковых ответов**:
    
    *   Если `stream=True`, читает ответ построчно, извлекая данные из JSON-объектов в каждой строке.
    *   Проверяет наличие ошибок в ответе.
    *   Извлекает текст из токенов и возвращает его частями через `yield`.
    *   Определяет причину завершения генерации (`stop` или `length`) на основе специальных токенов.
        
8.  **Обработка не потоковых ответов**:
    
    *   Если `stream=False`, обрабатывает ответ как JSON и извлекает сгенерированный текст или URL изображения.
    *   Возвращает результат через `yield`.
    
```
   Подготовка заголовков
   │
   └──► Обработка параметров изображения
        │
        └──► Создание асинхронной сессии
             │
             └──► Обработка моделей black-forest-labs
                  │
                  └──► Формирование полезной нагрузки (payload)
                       │
                       └──► Выполнение POST-запроса
                            │
                            └──► Обработка потоковых ответов (stream=True)
                                 │
                                 └──► Обработка не потоковых ответов (stream=False)
```

**Примеры**:

```python
async def generate_text():
    messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
    async for chunk in HuggingFaceInference.create_async_generator(model="gpt2", messages=messages):
        print(chunk, end="")

async def generate_image():
    messages = [{"role": "user", "content": "A cat"}]
    async for chunk in HuggingFaceInference.create_async_generator(model="stabilityai/stable-diffusion-2", messages=messages, width=512, height=512):
        print(chunk)
```

## Функции

### `format_prompt_mistral`

```python
def format_prompt_mistral(messages: Messages, do_continue: bool = False) -> str:
    """Форматирует сообщения для модели Mistral.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированная строка промпта.
    """
```

**Назначение**: Форматирование сообщений для использования в модели Mistral.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированная строка, готовая для использования в запросе к модели Mistral.

**Как работает функция**:

1.  **Извлечение системных сообщений**: Извлекает все сообщения с ролью "system" и сохраняет их контент в списке `system_messages`.
    
2.  **Формирование вопроса**: Объединяет контент последнего сообщения пользователя и все системные сообщения в одну строку `question`.
    
3.  **Формирование истории**: Создает строку `history`, содержащую все предыдущие сообщения ассистента и пользователя, отформатированные в виде `<s>[INST]...[/INST]...</s>`.
    
4.  **Обработка флага `do_continue`**: Если `do_continue` равен `True`, обрезает последний тег `</s>` из истории.
    
5.  **Объединение истории и вопроса**: Объединяет историю и вопрос в финальный промпт.
    
```
Извлечение системных сообщений
│
└──► Формирование вопроса
     │
     └──► Формирование истории
          │
          └──► Обработка флага do_continue
               │
               └──► Объединение истории и вопроса
```

**Примеры**:

```python
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
    """Форматирует сообщения для модели Qwen.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированная строка промпта.
    """
```

**Назначение**: Форматирование сообщений для использования в модели Qwen.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированная строка, готовая для использования в запросе к модели Qwen.

**Как работает функция**:

1.  **Формирование промпта**: Создает строку `prompt`, объединяя все сообщения и форматируя их в виде `<|im_start|>{role}\n{content}\n<|im_end|>\n`.
    
2.  **Обработка флага `do_continue`**: Если `do_continue` равен `True`, обрезает последний тег `\n<|im_end|>\n` из промпта.
    
3.  **Добавление тега ассистента**: Если `do_continue` равен `False`, добавляет тег `<|im_start|>assistant\n` в конец промпта.
    

```
Формирование промпта
│
└──► Обработка флага do_continue
     │
     └──► Добавление тега ассистента
```

**Примеры**:

```python
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
    """Форматирует сообщения для модели Qwen2.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированная строка промпта.
    """
```

**Назначение**: Форматирование сообщений для использования в модели Qwen2.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированная строка, готовая для использования в запросе к модели Qwen2.

**Как работает функция**:

1.  **Формирование промпта**: Создает строку `prompt`, объединяя все сообщения и форматируя их в виде `\u003C｜{role.capitalize()}｜\u003E{content}\u003C｜end of sentence｜\u003E`.
    
2.  **Обработка флага `do_continue`**: Если `do_continue` равен `True`, обрезает тег `\u003C｜Assistant｜\u003E` из промпта.
    
3.  **Добавление тега ассистента**: Если `do_continue` равен `False`, добавляет тег `\u003C｜Assistant｜\u003E` в конец промпта.
    

```
Формирование промпта
│
└──► Обработка флага do_continue
     │
     └──► Добавление тега ассистента
```

**Примеры**:

```python
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
    """Форматирует сообщения для модели Llama.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированная строка промпта.
    """
```

**Назначение**: Форматирование сообщений для использования в модели Llama.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированная строка, готовая для использования в запросе к модели Llama.

**Как работает функция**:

1.  **Формирование промпта**: Создает строку `prompt`, объединяя все сообщения и форматируя их в виде `<|begin_of_text|><|start_header_id|>{role}<|end_header_id|>\n\n{content}\n<|eot_id|>\n`.
    
2.  **Обработка флага `do_continue`**: Если `do_continue` равен `True`, обрезает тег `\n<|eot_id|>\n` из промпта.
    
3.  **Добавление тега ассистента**: Если `do_continue` равен `False`, добавляет тег `<|start_header_id|>assistant<|end_header_id|>\n\n` в конец промпта.
    

```
Формирование промпта
│
└──► Обработка флага do_continue
     │
     └──► Добавление тега ассистента
```

**Примеры**:

```python
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
    """Форматирует сообщения с использованием пользовательского токена завершения.

    Args:
        messages (Messages): Список сообщений.
        end_token (str, optional): Токен завершения. По умолчанию "</s>".
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированная строка промпта.
    """
```

**Назначение**: Форматирование сообщений с использованием пользовательского токена завершения.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `end_token` (`str`, optional): Токен завершения. По умолчанию `"</s>"`.
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированная строка, готовая для использования в запросе.

**Как работает функция**:

1.  **Формирование промпта**: Создает строку `prompt`, объединяя все сообщения и форматируя их в виде `<|{role}|>\n{content}{end_token}\n`.
    
2.  **Обработка флага `do_continue`**: Если `do_continue` равен `True`, обрезает `end_token + "\n"` из промпта.
    
3.  **Добавление тега ассистента**: Если `do_continue` равен `False`, добавляет тег `<|assistant|>\n` в конец промпта.
    

```
Формирование промпта
│
└──► Обработка флага do_continue
     │
     └──► Добавление тега ассистента
```

**Примеры**:

```python
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
    """Определяет и возвращает отформатированные входные данные для модели.

    Args:
        messages (Messages): Список сообщений.
        model_data (dict): Данные модели.
        model_type (str): Тип модели.
        do_continue (bool, optional): Флаг для продолжения генерации. По умолчанию False.

    Returns:
        str: Отформатированные входные данные.
    """
```

**Назначение**: Определение и возврат отформатированных входных данных для модели.

**Параметры**:
- `messages` (`Messages`): Список сообщений, содержащих информацию о ролях и контенте.
- `model_data` (`dict`): Данные о модели, включая конфигурацию и тип токенизатора.
- `model_type` (`str`): Тип модели (например, `"gpt2"`, `"mistral"`).
- `do_continue` (`bool`, optional): Флаг, указывающий, нужно ли продолжать предыдущий контекст. По умолчанию `False`.

**Возвращает**:
- `str`: Отформатированные входные данные для модели.

**Как работает функция**:

1.  **Обработка различных типов моделей**:
    
    *   Если `model_type` является одним из `"gpt2"`, `"gpt_neo"`, `"gemma"`, `"gemma2"`, использует функцию `format_prompt` для форматирования сообщений.
    *   Если `model_type` является `"mistral"` и автор модели `"mistralai"`, использует функцию `format_prompt_mistral`.
    *   В противном случае, пытается определить токен завершения из `model_data["config"]["tokenizer_config"]["eos_token"]` и использует соответствующую функцию форматирования:
        *   Если `eos_token` является одним из `"<|endoftext|>"`, `"<eos>"` или `"</s>"`, использует `format_prompt_custom`.
        *   Если `eos_token` является `"<|im_end|>"` использует `format_prompt_qwen`.
        *   Если `eos_token["content"] == "\\u003C｜end of sentence｜\\u003E"`, использует `format_prompt_qwen2`.
        *   Если `eos_token == "<|eot_id|>"` использует `format_prompt_llama`.
        *   В противном случае, использует функцию `format_prompt`.
        
2.  **Возврат отформатированных входных данных**: Возвращает отформатированные входные данные.
    

```
Обработка типа модели (gpt2, gpt_neo, gemma, gemma2)
│
└──► Обработка типа модели (mistral)
     │
     └──► Определение токена завершения (eos_token)
          │
          └──► Форматирование с использованием соответствующей функции
               │
               └──► Возврат отформатированных входных данных
```

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты - полезный ассистент."},
    {"role": "user", "content": "Как дела?"},
    {"role": "assistant", "content": "У меня все хорошо, спасибо!"},
    {"role": "user", "content": "Что ты умеешь?"}
]
model_data = {
    "config": {
        "tokenizer_config": {
            "eos_token": "</s>"
        }
    }
}
inputs = get_inputs(messages, model_data, "gpt2")
print(inputs)