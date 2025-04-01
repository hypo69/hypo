# Модуль HuggingFaceInference

## Обзор

Модуль `HuggingFaceInference` предоставляет класс `HuggingFaceInference`, который позволяет взаимодействовать с моделями Hugging Face Inference API для генерации текста и изображений. Он поддерживает потоковую передачу данных и различные типы моделей, включая текстовые и графические. Этот модуль является частью провайдера `HuggingFace` и использует асинхронные запросы для взаимодействия с API.

## Подробнее

Модуль предназначен для интеграции с Hugging Face Inference API, обеспечивая возможность использования различных моделей для генерации текста и изображений. Класс `HuggingFaceInference` поддерживает потоковую передачу данных, что позволяет получать результаты по частям в реальном времени. Он также обрабатывает различные форматы запросов и ответов, адаптируясь к специфике каждой модели.

## Классы

### `HuggingFaceInference`

**Описание**: Класс `HuggingFaceInference` является асинхронным генераторным провайдером и миксином для моделей, который обеспечивает взаимодействие с Hugging Face Inference API.

**Принцип работы**:
1.  Получает список доступных моделей из API Hugging Face.
2.  Формирует запросы к API в зависимости от типа модели (текст или изображение).
3.  Обрабатывает ответы от API, возвращая результаты в виде потока текста или изображений.

**Наследует**:
*   `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
*   `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:

*   `url` (str): URL главной страницы Hugging Face.
*   `parent` (str): Название родительского провайдера ("HuggingFace").
*   `working` (bool): Флаг, указывающий на работоспособность провайдера.
*   `default_model` (str): Модель, используемая по умолчанию (определена в `default_model` из `models.py`).
*   `default_image_model` (str): Модель для генерации изображений, используемая по умолчанию (определена в `default_image_model` из `models.py`).
*   `model_aliases` (dict): Алиасы моделей (определены в `model_aliases` из `models.py`).
*   `image_models` (list): Список моделей для генерации изображений (определен в `image_models` из `models.py`).
*   `model_data` (dict[str, dict]): Кеш данных моделей.

**Методы**:

*   `get_models() -> list[str]`: Возвращает список доступных моделей.
*   `get_model_data(session: StreamSession, model: str) -> str`: Возвращает данные о модели из API Hugging Face.
*   `create_async_generator(\
         model: str,\
         messages: Messages,\
         stream: bool = True,\
         proxy: str = None,\
         timeout: int = 600,\
         api_base: str = "https://api-inference.huggingface.co",\
         api_key: str = None,\
         max_tokens: int = 1024,\
         temperature: float = None,\
         prompt: str = None,\
         action: str = None,\
         extra_data: dict = {},\
         seed: int = None,\
         aspect_ratio: str = None,\
         width: int = None,\
         height: int = None,\
         **kwargs\
     ) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с API Hugging Face.

### `HuggingFaceInference.get_models()`

**Назначение**:
Возвращает список доступных моделей из API Hugging Face.

**Как работает функция**:

1.  Проверяет, если список моделей уже был получен и сохранен в `cls.models`.
2.  Если список моделей отсутствует, то выполняет запросы к API Hugging Face для получения списка текстовых и графических моделей.
3.  Объединяет полученные списки моделей.
4.  Сохраняет полученный список в `cls.models`.

```
Проверка наличия cls.models --> Запрос к API для текстовых моделей --> Запрос к API для графических моделей --> Объединение списков --> Сохранение в cls.models --> Возврат cls.models
```

**Параметры**:
Отсутствуют.

**Возвращает**:
*   `list[str]`: Список идентификаторов доступных моделей.

**Примеры**:

```python
models = HuggingFaceInference.get_models()
print(models)
```

### `HuggingFaceInference.get_model_data`

```python
    @classmethod
    async def get_model_data(cls, session: StreamSession, model: str) -> str:
        """
        Асинхронно получает данные о модели из API Hugging Face.

        Args:
            session (StreamSession): Асинхровая сессия для выполнения HTTP-запросов.
            model (str): Идентификатор модели.

        Returns:
            str: Данные о модели в формате JSON.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
            ResponseError: Если произошла ошибка при выполнении запроса.

        Пример:
            >>> session = StreamSession()
            >>> model_data = await HuggingFaceInference.get_model_data(session, "gpt2")
            >>> print(model_data)
            {'model_id': 'gpt2', ...}
        """
        ...
```

**Назначение**:
Асинхронно получает данные о модели из API Hugging Face.

**Параметры**:

*   `session` (`StreamSession`): Асинхронная сессия для выполнения HTTP-запросов.
*   `model` (`str`): Идентификатор модели.

**Возвращает**:
*   `str`: Данные о модели в формате JSON.

**Вызывает исключения**:

*   `ModelNotSupportedError`: Если модель не поддерживается.
*   `ResponseError`: Если произошла ошибка при выполнении запроса.

**Как работает функция**:

1.  Проверяет, если данные о модели уже есть в кеше `cls.model_data`. Если есть, возвращает данные из кеша.
2.  Если данных в кеше нет, выполняет GET-запрос к API Hugging Face для получения данных о модели.
3.  Проверяет статус ответа. Если статус 404, выбрасывает исключение `ModelNotSupportedError`.
4.  Сохраняет полученные данные в кеш `cls.model_data`.
5.  Возвращает данные о модели.

```
Проверка наличия данных в cls.model_data --> GET-запрос к API --> Проверка статуса ответа --> Сохранение в cls.model_data --> Возврат данных
```

**Примеры**:

```python
session = StreamSession()
model_data = await HuggingFaceInference.get_model_data(session, "gpt2")
print(model_data)
```

### `HuggingFaceInference.create_async_generator`

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
        """
        Создает асинхронный генератор для взаимодействия с API Hugging Face.

        Args:
            model (str): Идентификатор модели.
            messages (Messages): Список сообщений для формирования запроса.
            stream (bool, optional): Флаг, указывающий на потоковую передачу данных. По умолчанию True.
            proxy (str, optional): URL прокси-сервера. По умолчанию None.
            timeout (int, optional): Время ожидания ответа от API. По умолчанию 600.
            api_base (str, optional): Базовый URL API Hugging Face. По умолчанию "https://api-inference.huggingface.co".
            api_key (str, optional): Ключ API. По умолчанию None.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 1024.
            temperature (float, optional): Температура для генерации текста. По умолчанию None.
            prompt (str, optional): Дополнительный промпт для генерации текста. По умолчанию None.
            action (str, optional): Действие, которое необходимо выполнить. По умолчанию None.
            extra_data (dict, optional): Дополнительные данные для запроса. По умолчанию {}.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию None.
            aspect_ratio (str, optional): Соотношение сторон для генерации изображений. По умолчанию None.
            width (int, optional): Ширина изображения. По умолчанию None.
            height (int, optional): Высота изображения. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий текст или изображение.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
            ResponseError: Если произошла ошибка при выполнении запроса.

        Пример:
            >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
            >>> async for chunk in HuggingFaceInference.create_async_generator(model="gpt2", messages=messages):
            ...     print(chunk, end="")
            I'm doing well, thank you for asking!
        """
        ...
```

**Назначение**:
Создает асинхронный генератор для взаимодействия с API Hugging Face.

**Параметры**:

*   `model` (`str`): Идентификатор модели.
*   `messages` (`Messages`): Список сообщений для формирования запроса.
*   `stream` (`bool`, optional): Флаг, указывающий на потоковую передачу данных. По умолчанию `True`.
*   `proxy` (`str`, optional): URL прокси-сервера. По умолчанию `None`.
*   `timeout` (`int`, optional): Время ожидания ответа от API. По умолчанию 600.
*   `api_base` (`str`, optional): Базовый URL API Hugging Face. По умолчанию `"https://api-inference.huggingface.co"`.
*   `api_key` (`str`, optional): Ключ API. По умолчанию `None`.
*   `max_tokens` (`int`, optional): Максимальное количество токенов в ответе. По умолчанию 1024.
*   `temperature` (`float`, optional): Температура для генерации текста. По умолчанию `None`.
*   `prompt` (`str`, optional): Дополнительный промпт для генерации текста. По умолчанию `None`.
*   `action` (`str`, optional): Действие, которое необходимо выполнить. По умолчанию `None`.
*   `extra_data` (`dict`, optional): Дополнительные данные для запроса. По умолчанию `{}`.
*   `seed` (`int`, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
*   `aspect_ratio` (`str`, optional): Соотношение сторон для генерации изображений. По умолчанию `None`.
*   `width` (`int`, optional): Ширина изображения. По умолчанию `None`.
*   `height` (`int`, optional): Высота изображения. По умолчанию `None`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:
*   `AsyncResult`: Асинхронный генератор, возвращающий текст или изображение.

**Вызывает исключения**:

*   `ModelNotSupportedError`: Если модель не поддерживается.
*   `ResponseError`: Если произошла ошибка при выполнении запроса.

**Как работает функция**:

1.  Определяет заголовки запроса, включая `Authorization`, если предоставлен `api_key`.
2.  Создает асинхронную сессию `StreamSession` с заданными заголовками, прокси и таймаутом.
3.  В зависимости от типа модели (текст или изображение) формирует тело запроса `payload`.
4.  Выполняет POST-запрос к API Hugging Face.
5.  Если `stream` равен `True`, обрабатывает потоковый ответ, извлекая текст из каждого чанка данных и возвращая его через генератор.
6.  Если `stream` равен `False`, обрабатывает ответ как изображение, сохраняя его и возвращая URL изображения через генератор.

```
Определение заголовков --> Создание StreamSession --> Формирование payload (текст/изображение) --> POST-запрос к API --> Обработка потокового ответа (stream=True) / Обработка ответа как изображения (stream=False) --> Возврат данных через генератор
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for chunk in HuggingFaceInference.create_async_generator(model="gpt2", messages=messages):
    print(chunk, end="")
```

## Функции

### `format_prompt_mistral`

```python
def format_prompt_mistral(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Mistral.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированный промпт.
    """
    ...
```

**Назначение**:
Форматирует сообщения для модели Mistral.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированный промпт.

**Как работает функция**:

1.  Извлекает системные сообщения из списка сообщений.
2.  Формирует вопрос из последнего сообщения пользователя и системных сообщений.
3.  Формирует историю диалога из предыдущих сообщений пользователя и ассистента.
4.  Если `do_continue` равен `True`, возвращает историю диалога без завершающего токена.
5.  Если `do_continue` равен `False`, возвращает полную строку запроса, содержащую историю и вопрос.

```
Извлечение системных сообщений --> Формирование вопроса --> Формирование истории диалога --> Проверка do_continue --> Возврат отформатированного промпта
```

### `format_prompt_qwen`

```python
def format_prompt_qwen(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Qwen.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированный промпт.
    """
    ...
```

**Назначение**:
Форматирует сообщения для модели Qwen.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированный промпт.

**Как работает функция**:

1.  Формирует промпт, объединяя сообщения с префиксами и суффиксами, указывающими роль каждого сообщения.
2.  Добавляет токен начала сообщения ассистента, если `do_continue` равен `False`.
3.  Если `do_continue` равен `True`, удаляет завершающий токен из промпта.

```
Формирование промпта с префиксами и суффиксами --> Добавление токена ассистента (если !do_continue) --> Удаление завершающего токена (если do_continue) --> Возврат отформатированного промпта
```

### `format_prompt_qwen2`

```python
def format_prompt_qwen2(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Qwen2.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированный промпт.
    """
    ...
```

**Назначение**:
Форматирует сообщения для модели Qwen2.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированный промпт.

**Как работает функция**:

1.  Формирует промпт, объединяя сообщения с префиксами и суффиксами, указывающими роль каждого сообщения.
2.  Добавляет токен начала сообщения ассистента, если `do_continue` равен `False`.
3.  Если `do_continue` равен `True`, удаляет завершающий токен из промпта.

```
Формирование промпта с префиксами и суффиксами --> Добавление токена ассистента (если !do_continue) --> Удаление завершающего токена (если do_continue) --> Возврат отформатированного промпта
```

### `format_prompt_llama`

```python
def format_prompt_llama(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Llama.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированный промпт.
    """
    ...
```

**Назначение**:
Форматирует сообщения для модели Llama.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированный промпт.

**Как работает функция**:

1.  Формирует промпт, объединяя сообщения с префиксами и суффиксами, указывающими роль каждого сообщения.
2.  Добавляет токен начала сообщения ассистента, если `do_continue` равен `False`.
3.  Если `do_continue` равен `True`, удаляет завершающий токен из промпта.

```
Формирование промпта с префиксами и суффиксами --> Добавление токена ассистента (если !do_continue) --> Удаление завершающего токена (если do_continue) --> Возврат отформатированного промпта
```

### `format_prompt_custom`

```python
def format_prompt_custom(messages: Messages, end_token: str = "</s>", do_continue: bool = False) -> str:
    """
    Форматирует сообщения с пользовательским завершающим токеном.

    Args:
        messages (Messages): Список сообщений.
        end_token (str, optional): Завершающий токен. По умолчанию "</s>".
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированный промпт.
    """
    ...
```

**Назначение**:
Форматирует сообщения с пользовательским завершающим токеном.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `end_token` (`str`, optional): Завершающий токен. По умолчанию `"</s>"`.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированный промпт.

**Как работает функция**:

1.  Формирует промпт, объединяя сообщения с префиксами и суффиксами, указывающими роль каждого сообщения и используя заданный `end_token`.
2.  Добавляет токен начала сообщения ассистента, если `do_continue` равен `False`.
3.  Если `do_continue` равен `True`, удаляет завершающий токен из промпта.

```
Формирование промпта с префиксами, суффиксами и end_token --> Добавление токена ассистента (если !do_continue) --> Удаление завершающего токена (если do_continue) --> Возврат отформатированного промпта
```

### `get_inputs`

```python
def get_inputs(messages: Messages, model_data: dict, model_type: str, do_continue: bool = False) -> str:
    """
    Получает отформатированные входные данные для модели.

    Args:
        messages (Messages): Список сообщений.
        model_data (dict): Данные о модели.
        model_type (str): Тип модели.
        do_continue (bool): Флаг, указывающий на продолжение предыдущего диалога.

    Returns:
        str: Отформатированные входные данные.
    """
    ...
```

**Назначение**:
Получает отформатированные входные данные для модели.

**Параметры**:
*   `messages` (`Messages`): Список сообщений.
*   `model_data` (`dict`): Данные о модели.
*   `model_type` (`str`): Тип модели.
*   `do_continue` (`bool`): Флаг, указывающий на продолжение предыдущего диалога.

**Возвращает**:
*   `str`: Отформатированные входные данные.

**Как работает функция**:

1.  В зависимости от типа модели и данных о модели выбирает функцию для форматирования промпта.
2.  Вызывает выбранную функцию форматирования и возвращает результат.

```
Определение функции форматирования промпта (в зависимости от model_type и model_data) --> Вызов функции форматирования --> Возврат отформатированных входных данных