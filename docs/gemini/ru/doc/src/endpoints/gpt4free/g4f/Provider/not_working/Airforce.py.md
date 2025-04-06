# Модуль Airforce

## Обзор

Модуль `Airforce` предоставляет асинхронный интерфейс для взаимодействия с API Airforce для генерации текста и изображений. Он поддерживает стриминг ответов, работу с историей сообщений и системными сообщениями. Модуль включает в себя методы для фильтрации контента, обработки ошибок и выбора моделей.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для обеспечения доступа к возможностям генерации текста и изображений, предоставляемым API Airforce. Он включает в себя функции для обработки запросов, фильтрации ответов и управления моделями.

## Классы

### `Airforce`

**Описание**: Класс `Airforce` предоставляет методы для взаимодействия с API Airforce для генерации текста и изображений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): Базовый URL API Airforce.
- `api_endpoint_completions` (str): URL для запросов завершения текста.
- `api_endpoint_imagine2` (str): URL для запросов генерации изображений.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга ответов.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию для генерации текста.
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `models` (List[str]): Список поддерживаемых моделей для генерации текста.
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `hidden_models` (Set[str]): Набор скрытых моделей, которые не должны быть доступны пользователю.
- `additional_models_imagine` (List[str]): Список дополнительных моделей для генерации изображений.
- `model_aliases` (Dict[str, str]): Словарь, содержащий псевдонимы моделей для удобства использования.

**Методы**:
- `get_models()`: Возвращает список доступных моделей.
- `get_model(model: str) -> str`: Возвращает актуальное имя модели из псевдонима.
- `_filter_content(part_response: str) -> str`: Фильтрует нежелательный контент из частичного ответа.
- `_filter_response(response: str) -> str`: Фильтрует полный ответ, удаляя системные ошибки и нежелательный текст.
- `generate_image(model: str, prompt: str, size: str, seed: int, proxy: str = None) -> AsyncResult`: Генерирует изображение на основе заданных параметров.
- `generate_text(model: str, messages: Messages, max_tokens: int, temperature: float, top_p: float, stream: bool, proxy: str = None) -> AsyncResult`: Генерирует текст на основе заданных параметров.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, max_tokens: int = 512, temperature: float = 1, top_p: float = 1, stream: bool = True, size: str = "1:1", seed: int = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для генерации текста или изображений.

## Функции

### `split_message`

```python
def split_message(message: str, max_length: int = 1000) -> List[str]:
    """Splits the message into parts up to (max_length).

    Args:
        message (str): Сообщение для разделения.
        max_length (int, optional): Максимальная длина каждой части. По умолчанию 1000.

    Returns:
        List[str]: Список частей сообщения.
    """
    ...
```

**Назначение**: Разделяет сообщение на части длиной не более `max_length`.

**Параметры**:
- `message` (str): Сообщение, которое нужно разделить.
- `max_length` (int, optional): Максимальная длина каждой части сообщения. По умолчанию равна 1000.

**Возвращает**:
- `List[str]`: Список строк, представляющих собой части исходного сообщения.

**Как работает функция**:

1.  **Инициализация**: Создается пустой список `chunks` для хранения частей сообщения.
2.  **Цикл разделения**: Пока длина сообщения `message` превышает `max_length`, выполняется следующее:
    *   Находится индекс последнего пробела в пределах `max_length` символов от начала сообщения. Если пробел не найден, `split_point` устанавливается равным `max_length`.
    *   Первая часть сообщения (от начала до `split_point`) добавляется в список `chunks`.
    *   Оставшаяся часть сообщения (после `split_point`) обрезается и удаляются пробелы в начале.
3.  **Добавление остатка**: Если после цикла в сообщении еще что-то осталось, это добавляется в список `chunks`.
4.  **Возврат результата**: Функция возвращает список `chunks`, содержащий все части исходного сообщения.

```
Разделение сообщения
│
├── message > max_length?
│   ├── Да: Найти split_point (последний пробел или max_length)
│   │   ├── Добавить message[:split_point] в chunks
│   │   └── message = message[split_point:].strip()
│   └── Нет: Добавить message в chunks (если message не пустой)
│
└── Возврат chunks
```

**Примеры**:

```python
>>> split_message("This is a long message that needs to be split into smaller parts.", max_length=20)
['This is a long ', 'message that needs', ' to be split into', ' smaller parts.']

>>> split_message("Short message", max_length=100)
['Short message']
```

### `Airforce.get_models`

```python
@classmethod
def get_models(cls):
    """Get available models with error handling"""
    ...
```

**Назначение**: Получает список доступных моделей для генерации текста и изображений.

**Возвращает**:
- `List[str]`: Список доступных моделей.

**Как работает функция**:

1.  **Проверка наличия моделей изображений**: Если список `cls.image_models` пуст, то происходит попытка получить список моделей изображений с API Airforce.
    *   Выполняется GET-запрос к `f"{cls.url}/imagine2/models"`.
    *   В случае успеха, полученные данные преобразуются в JSON и сохраняются в `cls.image_models`.
    *   Если `cls.image_models` является списком, к нему добавляются модели из `cls.additional_models_imagine`. Если это не список, то `cls.image_models` присваивается копия `cls.additional_models_imagine`.
    *   В случае ошибки при получении списка моделей изображений, в `cls.image_models` присваивается копия `cls.additional_models_imagine`, а информация об ошибке логируется.
2.  **Проверка наличия текстовых моделей**: Если список `cls.models` пуст, то происходит попытка получить список текстовых моделей с API Airforce.
    *   Выполняется GET-запрос к `f"{cls.url}/models"`.
    *   В случае успеха, полученные данные преобразуются в JSON. Если в JSON есть ключ `data`, то извлекаются идентификаторы моделей и сохраняются в `cls.models`.
    *   К `cls.models` добавляются модели из `cls.image_models`. Из `cls.models` удаляются модели, находящиеся в `cls.hidden_models`.
    *   Если данные не содержат ключ `data`, то `cls.models` присваивается список ключей из `cls.model_aliases`.
    *   В случае ошибки при получении списка текстовых моделей, `cls.models` присваивается список ключей из `cls.model_aliases`, а информация об ошибке логируется.
3.  **Возврат результата**: Если `cls.models` содержит данные, то возвращается `cls.models`. В противном случае возвращается список ключей из `cls.model_aliases`.

```
Получение моделей
│
├── cls.image_models пуст?
│   ├── Да: Запрос к API imagine2/models
│   │   ├── Успех: Обновление cls.image_models
│   │   └── Ошибка: debug.log и использование fallback
│   └── Нет: Пропуск
│
├── cls.models пуст?
│   ├── Да: Запрос к API /models
│   │   ├── Успех: Обновление cls.models
│   │   └── Ошибка: debug.log и использование fallback
│   └── Нет: Пропуск
│
└── Возврат cls.models или ключи cls.model_aliases
```

**Примеры**:

```python
>>> Airforce.get_models()
['llama-3.1-70b-chat', 'flux']
```

### `Airforce.get_model`

```python
@classmethod
def get_model(cls, model: str) -> str:
    """Get the actual model name from alias"""
    ...
```

**Назначение**: Возвращает фактическое имя модели на основе заданного псевдонима.

**Параметры**:
- `model` (str): Псевдоним модели.

**Возвращает**:
- `str`: Фактическое имя модели.

**Как работает функция**:

1.  **Поиск псевдонима**: Функция пытается найти псевдоним `model` в словаре `cls.model_aliases`.
2.  **Возврат результата**: Если псевдоним найден, возвращается соответствующее ему значение (фактическое имя модели). Если псевдоним не найден, возвращается либо сам `model`, либо значение `cls.default_model`, если `model` пуст.

```
Получение имени модели
│
├── Поиск псевдонима модели в cls.model_aliases
│   ├── Псевдоним найден: Возврат соответствующего значения
│   └── Псевдоним не найден: Возврат model или cls.default_model
│
└── Конец
```

**Примеры**:

```python
>>> Airforce.get_model("openchat-3.5")
'openchat-3.5-0106'

>>> Airforce.get_model("unknown_model")
'unknown_model'

>>> Airforce.get_model("")
'llama-3.1-70b-chat'
```

### `Airforce._filter_content`

```python
@classmethod
def _filter_content(cls, part_response: str) -> str:
    """
    Filters out unwanted content from the partial response.
    """
    ...
```

**Назначение**: Фильтрует нежелательный контент из частичного ответа.

**Параметры**:
- `part_response` (str): Частичный ответ, который необходимо отфильтровать.

**Возвращает**:
- `str`: Отфильтрованный частичный ответ.

**Как работает функция**:

1.  **Удаление сообщений о превышении лимита символов**: Использует регулярное выражение для удаления сообщений о превышении лимита символов в сообщении и ссылок на Discord.
2.  **Удаление сообщений об ограничении скорости**: Использует регулярное выражение для удаления сообщений об ограничении скорости и ссылок на Discord.
3.  **Возврат результата**: Функция возвращает отфильтрованный `part_response`.

```
Фильтрация контента
│
├── Удаление сообщений о превышении лимита символов
│   │   (re.sub)
│
├── Удаление сообщений об ограничении скорости
│   │   (re.sub)
│
└── Возврат отфильтрованного part_response
```

**Примеры**:

```python
>>> Airforce._filter_content("One message exceeds the \\d+chars per message limit..+https:\\/\\/discord\\.com\\/invite\\/\\S+")
''

>>> Airforce._filter_content("Rate limit \\(\\d+\\/minute\\) exceeded\\. Join our discord for more: .+https:\\/\\/discord\\.com\\/invite\\/\\S+")
''
```

### `Airforce._filter_response`

```python
@classmethod
def _filter_response(cls, response: str) -> str:
    """
    Filters the full response to remove system errors and other unwanted text.
    """
    ...
```

**Назначение**: Фильтрует полный ответ, удаляя системные ошибки и нежелательный текст.

**Параметры**:
- `response` (str): Полный ответ, который необходимо отфильтровать.

**Возвращает**:
- `str`: Отфильтрованный полный ответ.

**Вызывает исключения**:
- `ValueError`: Если ответ содержит сообщение об ошибке "Model not found or too long input. Or any other error (xD)".

**Как работает функция**:

1.  **Проверка на наличие ошибок**: Если в ответе содержится сообщение "Model not found or too long input. Or any other error (xD)", выбрасывается исключение `ValueError`.
2.  **Удаление идентификаторов ошибок**: Использует регулярное выражение для удаления идентификаторов ошибок в формате `\\[ERROR\\] \'\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12}\'`.
3.  **Удаление токенов `<\\|im_end\\|>`**: Использует регулярное выражение для удаления токенов `<\\|im_end\\|>`.
4.  **Удаление токенов `</s>`**: Использует регулярное выражение для удаления токенов `</s>`.
5.  **Удаление префиксов**: Использует регулярное выражение для удаления префиксов "Assistant: ", "AI: ", "ANSWER: ", "Output: ".
6.  **Фильтрация содержимого**: Вызывает метод `cls._filter_content` для дополнительной фильтрации содержимого.
7.  **Возврат результата**: Функция возвращает отфильтрованный `response`.

```
Фильтрация полного ответа
│
├── Проверка на наличие ошибок
│   ├── Ошибка найдена: Выброс ValueError
│   └── Ошибка не найдена: Продолжение
│
├── Удаление идентификаторов ошибок
│   │   (re.sub)
│
├── Удаление токенов <\\|im_end\\|>
│   │   (re.sub)
│
├── Удаление токенов </s>
│   │   (re.sub)
│
├── Удаление префиксов
│   │   (re.sub)
│
├── Фильтрация содержимого
│   │   (cls._filter_content)
│
└── Возврат отфильтрованного response
```

**Примеры**:

```python
>>> Airforce._filter_response("[ERROR] '12345678-1234-1234-1234-123456789012'")
''

>>> Airforce._filter_response("<|im_end|>")
''

>>> Airforce._filter_response("</s>")
''

>>> Airforce._filter_response("Assistant: Hello")
'Hello'
```

### `Airforce.generate_image`

```python
@classmethod
async def generate_image(
    cls,
    model: str,
    prompt: str,
    size: str,
    seed: int,
    proxy: str = None
) -> AsyncResult:
    """
    Generates image, buffers the response, filters it, and returns the final result.
    """
    ...
```

**Назначение**: Генерирует изображение на основе заданных параметров.

**Параметры**:
- `model` (str): Модель для генерации изображения.
- `prompt` (str): Текстовое описание желаемого изображения.
- `size` (str): Размер изображения.
- `seed` (int): Зерно для генерации случайных чисел, обеспечивающее воспроизводимость результатов.
- `proxy` (str, optional): Прокси-сервер для выполнения запроса. По умолчанию `None`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объект `ImageResponse` с URL изображения и альтернативным текстом.

**Вызывает исключения**:
- `RuntimeError`: Если генерация изображения завершается с ошибкой.

**Как работает функция**:

1.  **Подготовка заголовков**: Создаются заголовки HTTP-запроса, включающие User-Agent, Accept, Accept-Language и Content-Type.
2.  **Подготовка параметров**: Создаются параметры запроса, включающие модель, текстовое описание, размер и зерно.
3.  **Выполнение запроса**: Отправляется GET-запрос к API Airforce для генерации изображений. Используется `ClientSession` для асинхронного выполнения запроса.
4.  **Обработка ответа**:
    *   Если статус ответа равен 200, извлекается URL изображения и возвращается объект `ImageResponse`.
    *   Если статус ответа не равен 200, извлекается текст ошибки и выбрасывается исключение `RuntimeError`.

```
Генерация изображения
│
├── Подготовка заголовков и параметров запроса
│
├── Отправка GET-запроса к API Airforce
│   │   (ClientSession)
│
├── Обработка ответа
│   ├── Статус 200: Извлечение URL изображения и возврат ImageResponse
│   └── Статус != 200: Извлечение текста ошибки и выброс RuntimeError
│
└── Конец
```

**Примеры**:

```python
async for result in Airforce.generate_image(model="flux", prompt="A cat", size="1:1", seed=123):
    print(result)
```

### `Airforce.generate_text`

```python
@classmethod
async def generate_text(
    cls,
    model: str,
    messages: Messages,
    max_tokens: int,
    temperature: float,
    top_p: float,
    stream: bool,
    proxy: str = None
) -> AsyncResult:
    """
    Generates text, buffers the response, filters it, and returns the final result.
    """
    ...
```

**Назначение**: Генерирует текст на основе заданных параметров.

**Параметры**:
- `model` (str): Модель для генерации текста.
- `messages` (Messages): Список сообщений, представляющих собой контекст для генерации текста.
- `max_tokens` (int): Максимальное количество токенов в сгенерированном тексте.
- `temperature` (float): Температура для генерации текста (влияет на случайность).
- `top_p` (float): Top-p sampling для генерации текста (влияет на разнообразие).
- `stream` (bool): Флаг, указывающий на необходимость стриминга ответа.
- `proxy` (str, optional): Прокси-сервер для выполнения запроса. По умолчанию `None`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части сгенерированного текста.

**Вызывает исключения**:
- `ValueError`: Если ответ содержит сообщение об ошибке "Model not found or too long input. Or any other error (xD)".

**Как работает функция**:

1.  **Подготовка заголовков**: Создаются заголовки HTTP-запроса, включающие User-Agent, Accept, Accept-Language и Content-Type.
2.  **Подготовка сообщений**: Сообщения разделяются на части, если они превышают максимальную длину (1000 символов).
3.  **Подготовка данных**: Создаются данные запроса, включающие сообщения, модель, температуру, top_p и флаг стриминга.
4.  **Выполнение запроса**: Отправляется POST-запрос к API Airforce для генерации текста. Используется `ClientSession` для асинхронного выполнения запроса.
5.  **Обработка ответа**:
    *   Если `stream` равен `True`, ответ обрабатывается построчно, и каждая строка декодируется и фильтруется.
    *   Если `stream` равен `False`, извлекается JSON из ответа, фильтруется и возвращается.

```
Генерация текста
│
├── Подготовка заголовков и сообщений
│
├── Отправка POST-запроса к API Airforce
│   │   (ClientSession)
│
├── Обработка ответа
│   ├── stream == True: Обработка построчно и фильтрация
│   └── stream == False: Извлечение JSON, фильтрация и возврат
│
└── Конец
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello"}]
async for result in Airforce.generate_text(model="llama-3.1-70b-chat", messages=messages, max_tokens=100, temperature=0.7, top_p=0.9, stream=True):
    print(result)
```

### `Airforce.create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    prompt: str = None,
    proxy: str = None,
    max_tokens: int = 512,
    temperature: float = 1,
    top_p: float = 1,
    stream: bool = True,
    size: str = "1:1",
    seed: int = None,
    **kwargs
) -> AsyncResult:
    """
    Generates image, buffers the response, filters it, and returns the final result.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для генерации текста или изображений.

**Параметры**:
- `model` (str): Модель для генерации текста или изображения.
- `messages` (Messages): Список сообщений, представляющих собой контекст для генерации текста.
- `prompt` (str, optional): Текстовое описание желаемого изображения. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для выполнения запроса. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в сгенерированном тексте. По умолчанию 512.
- `temperature` (float, optional): Температура для генерации текста (влияет на случайность). По умолчанию 1.
- `top_p` (float, optional): Top-p sampling для генерации текста (влияет на разнообразие). По умолчанию 1.
- `stream` (bool, optional): Флаг, указывающий на необходимость стриминга ответа. По умолчанию `True`.
- `size` (str, optional): Размер изображения. По умолчанию "1:1".
- `seed` (int, optional): Зерно для генерации случайных чисел, обеспечивающее воспроизводимость результатов. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части сгенерированного текста или объект `ImageResponse` с URL изображения и альтернативным текстом.

**Как работает функция**:

1.  **Получение модели**: Вызывается метод `cls.get_model` для получения фактического имени модели на основе заданного псевдонима.
2.  **Проверка на модель изображения**: Если модель находится в списке моделей изображений (`cls.image_models`), генерируется изображение.
    *   Если `prompt` не задан, используется содержимое последнего сообщения.
    *   Если `seed` не задан, генерируется случайное число.
    *   Вызывается метод `cls.generate_image` для генерации изображения.
3.  **Генерация текста**: Если модель не является моделью изображения, генерируется текст.
    *   Вызывается метод `cls.generate_text` для генерации текста.

```
Создание асинхронного генератора
│
├── Получение модели (cls.get_model)
│
├── Проверка на модель изображения
│   ├── Модель изображения: Генерация изображения
│   │   ├── Подготовка параметров
│   │   └── Вызов cls.generate_image
│   └── Не модель изображения: Генерация текста
│       └── Вызов cls.generate_text
│
└── Конец
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Generate a cat image"}]
async for result in Airforce.create_async_generator(model="flux", messages=messages, prompt="A cat", size="1:1", seed=123):
    print(result)

messages = [{"role": "user", "content": "Hello"}]
async for result in Airforce.create_async_generator(model="llama-3.1-70b-chat", messages=messages, max_tokens=100, temperature=0.7, top_p=0.9, stream=True):
    print(result)