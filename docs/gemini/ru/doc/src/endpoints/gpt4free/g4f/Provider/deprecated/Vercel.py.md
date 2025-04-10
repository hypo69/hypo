# Модуль Vercel

## Обзор

Модуль `Vercel` предоставляет реализацию для взаимодействия с моделями, размещенными на платформе Vercel. Он поддерживает как стандартные запросы, так и потоковую передачу данных, а также предоставляет механизм для обхода защиты от ботов. Модуль использует библиотеку `requests` для выполнения HTTP-запросов и `execjs` для выполнения JavaScript-кода, необходимого для получения токена защиты от ботов.

## Подробнее

Модуль предназначен для интеграции с различными AI-моделями, доступными через Vercel. Он включает в себя поддержку моделей GPT-3.5 Turbo и возможность ведения истории сообщений. Для работы модуля требуется установка пакета `PyExecJS`, который используется для выполнения JavaScript-кода.

## Классы

### `Vercel`

**Описание**: Класс `Vercel` является реализацией интерфейса `AbstractProvider` и предоставляет методы для взаимодействия с API Vercel.

**Наследует**: `AbstractProvider`

**Атрибуты**:
- `url` (str): URL-адрес API Vercel.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5 Turbo.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.

**Методы**:
- `create_completion`: Создает запрос на completion к API Vercel.

### `ModelInfo`

**Описание**: `TypedDict`, описывающий структуру информации о модели.

**Атрибуты**:
- `id` (str): Идентификатор модели.
- `default_params` (dict[str, Any]): Словарь с параметрами по умолчанию для модели.

## Функции

### `create_completion`

```python
@staticmethod
def create_completion(
    model: str,
    messages: Messages,
    stream: bool,
    proxy: str = None,
    **kwargs
) -> CreateResult:
    """
    Создает запрос на completion к API Vercel.

    Args:
        model (str): Идентификатор модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры для передачи в API.

    Returns:
        CreateResult: Генератор токенов или строка с результатом.

    Raises:
        MissingRequirementsError: Если не установлен пакет `PyExecJS`.
        ValueError: Если указанная модель не поддерживается Vercel.
    """
```

**Назначение**: Функция `create_completion` отправляет запрос к API Vercel для генерации текста на основе предоставленных сообщений и параметров модели. Она поддерживает потоковую передачу данных, что позволяет получать результат по частям.

**Параметры**:
- `model` (str): Идентификатор модели, которую необходимо использовать.
- `messages` (Messages): Список сообщений, передаваемых в API для генерации текста.
- `stream` (bool): Флаг, определяющий, использовать ли потоковый режим для получения результата.
- `proxy` (str, optional): URL прокси-сервера, используемого для подключения к API. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API Vercel.

**Возвращает**:
- `CreateResult`: Генератор токенов, если `stream=True`, или строка с полным результатом, если `stream=False`.

**Вызывает исключения**:
- `MissingRequirementsError`: Если отсутствует необходимый пакет `PyExecJS`.
- `ValueError`: Если указанная модель не поддерживается Vercel.

**Как работает функция**:

1. **Проверка зависимостей**: Функция проверяет, установлен ли пакет `PyExecJS`. Если нет, вызывается исключение `MissingRequirementsError`.
2. **Выбор модели**: Если модель не указана, используется модель "gpt-3.5-turbo" по умолчанию. Если указанная модель не найдена в списке поддерживаемых, вызывается исключение `ValueError`.
3. **Формирование заголовков**: Создаются заголовки HTTP-запроса, включая токен защиты от ботов, полученный с помощью функции `get_anti_bot_token`.
4. **Формирование тела запроса**: Создается JSON-тело запроса, включающее идентификатор модели, сообщения и дополнительные параметры.
5. **Выполнение запроса**: Функция выполняет POST-запрос к API Vercel с использованием библиотеки `requests`. Если `stream=True`, используется потоковый режим для получения данных.
6. **Обработка результата**: Если потоковый режим включен, функция возвращает генератор, который выдает токены по мере их поступления от API. В противном случае функция возвращает полную строку с результатом.
7. **Повторные попытки**: В случае неуспешного запроса функция повторяет попытки до `max_retries` раз.

```
A [Проверка зависимостей и выбор модели]
|
B [Формирование заголовков и тела запроса]
|
C [Выполнение POST-запроса к API Vercel]
|
D [Обработка результата (потоковый или полный)]
|
E [Повторные попытки в случае неудачи]
```

**Примеры**:

```python
# Пример вызова функции с потоковой передачей данных
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = True
result = Vercel.create_completion(model=model, messages=messages, stream=stream)
for token in result:
    print(token, end="")

# Пример вызова функции без потоковой передачи данных
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = False
result = Vercel.create_completion(model=model, messages=messages, stream=stream)
print(result)
```

### `get_anti_bot_token`

```python
def get_anti_bot_token() -> str:
    """
    Получает токен защиты от ботов, необходимый для выполнения запросов к API Vercel.

    Returns:
        str: Токен защиты от ботов в формате base64.
    """
```

**Назначение**: Функция `get_anti_bot_token` получает токен защиты от ботов, необходимый для выполнения запросов к API Vercel. Этот токен генерируется на основе JavaScript-кода, который выполняется с помощью библиотеки `PyExecJS`.

**Возвращает**:
- `str`: Токен защиты от ботов в формате base64.

**Как работает функция**:

1. **Получение данных**: Функция отправляет GET-запрос к API Vercel для получения данных, необходимых для генерации токена.
2. **Декодирование данных**: Полученные данные, представленные в формате base64, декодируются и преобразуются в JSON-объект.
3. **Формирование JavaScript-скрипта**: На основе декодированных данных формируется JavaScript-скрипт, который будет выполнен с помощью `PyExecJS`.
4. **Выполнение скрипта**: Сформированный JavaScript-скрипт выполняется с помощью `PyExecJS`, и результат выполнения преобразуется в JSON-объект.
5. **Кодирование токена**: Полученный JSON-объект кодируется в формат base64 и возвращается в качестве токена защиты от ботов.

```
A [Отправка GET-запроса для получения данных]
|
B [Декодирование данных из base64]
|
C [Формирование JavaScript-скрипта]
|
D [Выполнение скрипта с помощью PyExecJS]
|
E [Кодирование токена в base64]
```

**Примеры**:

```python
# Пример вызова функции для получения токена защиты от ботов
token = get_anti_bot_token()
print(token)
```

### `model_info`

```python
model_info: dict[str, ModelInfo] = {
    # \'claude-instant-v1\': {
    #     \'id\': \'anthropic:claude-instant-v1\',\
    #     \'default_params\': {\
    #         \'temperature\': 1,\
    #         \'maximumLength\': 1024,\
    #         \'topP\': 1,\
    #         \'topK\': 1,\
    #         \'presencePenalty\': 1,\
    #         \'frequencyPenalty\': 1,\
    #         \'stopSequences\': [\'\\n\\nHuman:\'],\
    #     },\
    # },
    # ...
    \'text-davinci-003\': {\
        \'id\': \'openai:text-davinci-003\',\
        \'default_params\': {\
            \'temperature\': 0.5,\
            \'maximumLength\': 4097,\
            \'topP\': 1,\
            \'presencePenalty\': 0,\
            \'frequencyPenalty\': 0,\
            \'stopSequences\': [],\
        },\
    },\
}
```

**Описание**: Словарь `model_info` содержит информацию о поддерживаемых моделях, включая их идентификаторы и параметры по умолчанию.

**Назначение**: Предоставляет централизованный источник информации о моделях, используемых в модуле `Vercel`.

**Принцип работы**:
Словарь `model_info` содержит ключи, соответствующие именам моделей, и значения, являющиеся экземплярами `ModelInfo`. Каждый экземпляр `ModelInfo` содержит идентификатор модели (`id`) и словарь с параметрами по умолчанию (`default_params`).

**Примеры**:

```python
# Пример доступа к информации о модели
model_name = "gpt-3.5-turbo"
model_id = model_info[model_name]["id"]
default_temperature = model_info[model_name]["default_params"]["temperature"]
print(f"Model ID: {model_id}, Default Temperature: {default_temperature}")