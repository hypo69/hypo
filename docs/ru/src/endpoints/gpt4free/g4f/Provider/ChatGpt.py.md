# Модуль ChatGpt

## Обзор

Модуль `ChatGpt` предоставляет класс `ChatGpt`, который является провайдером для взаимодействия с моделью ChatGPT. Он позволяет создавать запросы к модели, получать ответы и обрабатывать их. Модуль поддерживает историю сообщений, системные сообщения и потоковую передачу данных.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для обеспечения возможности взаимодействия с моделью ChatGPT через API. Класс `ChatGpt` наследуется от `AbstractProvider` и `ProviderModelMixin`, что позволяет ему интегрироваться в систему провайдеров проекта. Модуль использует библиотеки `requests`, `uuid`, `time`, `random` и `json` для выполнения HTTP-запросов, генерации уникальных идентификаторов, работы со временем, генерации случайных чисел и обработки данных в формате JSON.

## Классы

### `ChatGpt(AbstractProvider, ProviderModelMixin)`

**Описание**: Класс `ChatGpt` является провайдером для взаимодействия с моделью ChatGPT. Он наследуется от `AbstractProvider` и `ProviderModelMixin`.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для провайдеров.
- `ProviderModelMixin`: Миксин, предоставляющий общую функциональность для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера, в данном случае `"ChatGpt"`.
- `url` (str): URL-адрес ChatGPT, `"https://chatgpt.com"`.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.
- `default_model` (str): Модель, используемая по умолчанию, `'auto'`.
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей.

**Методы**:
- `get_model(model: str) -> str`: Возвращает имя модели на основе псевдонима или имени по умолчанию.
- `create_completion(model: str, messages: Messages, stream: bool, **kwargs) -> CreateResult`: Создает запрос к модели ChatGPT и возвращает результат.

## Функции

### `format_conversation(messages: list) -> list`

**Назначение**: Форматирует список сообщений в формат, ожидаемый API ChatGPT.

**Параметры**:
- `messages` (list): Список сообщений, где каждое сообщение представляет собой словарь с ключами `'role'` и `'content'`.

**Возвращает**:
- `list`: Список словарей, представляющих сообщения в формате, ожидаемом API ChatGPT.

**Как работает функция**:
1. Инициализирует пустой список `conversation`.
2. Перебирает каждое сообщение в списке `messages`.
3. Для каждого сообщения создает словарь, содержащий:
   - `'id'`: Случайно сгенерированный UUID.
   - `'author'`: Словарь с ролью автора (`'role'`).
   - `'content'`: Словарь с типом контента (`'content_type'`) и содержимым (`'parts'`).
   - `'metadata'`: Словарь с метаданными сериализации.
   - `'create_time'`: Текущее время в формате Unix timestamp с точностью до миллисекунд.
4. Добавляет созданный словарь в список `conversation`.
5. Возвращает список `conversation`.

**Внутренние логические блоки функции**:
```
A [Начало]
|
B [Инициализация списка conversation]
|
C [Цикл по messages]
|
D [Создание словаря message_data]
|
E [Добавление message_data в conversation]
|
F [Конец цикла]
|
G [Возврат conversation]
|
H [Конец]
```

**Примеры**:

```python
messages = [
    {'role': 'user', 'content': 'Hello'},
    {'role': 'assistant', 'content': 'Hi there!'}
]
formatted_messages = format_conversation(messages)
print(formatted_messages)
# Вывод:
# [{'id': '...', 'author': {'role': 'user'}, 'content': {'content_type': 'text', 'parts': ['Hello']}, 'metadata': {'serialization_metadata': {'custom_symbol_offsets': []}}, 'create_time': ...},
#  {'id': '...', 'author': {'role': 'assistant'}, 'content': {'content_type': 'text', 'parts': ['Hi there!']}, 'metadata': {'serialization_metadata': {'custom_symbol_offsets': []}}, 'create_time': ...}]
```

### `init_session(user_agent: str) -> Session`

**Назначение**: Инициализирует сессию `requests.Session` с необходимыми заголовками и куки для взаимодействия с ChatGPT.

**Параметры**:
- `user_agent` (str): Строка User-Agent, которая будет использоваться в заголовках запроса.

**Возвращает**:
- `Session`: Инициализированный объект сессии `requests.Session`.

**Как работает функция**:
1. Создает новый объект сессии `requests.Session`.
2. Определяет словарь `cookies` с начальным значением `_dd_s`.
3. Определяет словарь `headers` с необходимыми заголовками, включая `User-Agent`.
4. Выполняет GET-запрос к `https://chatgpt.com/` с использованием заданных куки и заголовков.
5. Возвращает объект сессии.

**Внутренние логические блоки функции**:
```
A [Начало]
|
B [Создание сессии]
|
C [Определение cookies]
|
D [Определение headers]
|
E [Выполнение GET-запроса]
|
F [Возврат сессии]
|
G [Конец]
```

**Примеры**:

```python
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
session = init_session(user_agent)
print(session)
# Вывод:
# <requests.sessions.Session object at 0x...>
```

### `ChatGpt.get_model(model: str) -> str`

**Назначение**: Возвращает имя модели на основе псевдонима или имени по умолчанию.

**Параметры**:
- `model` (str): Имя модели или псевдоним.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:
1. Проверяет, есть ли модель в списке поддерживаемых моделей (`cls.models`).
2. Если модель найдена в списке, возвращает ее имя.
3. Если модель найдена в словаре псевдонимов (`cls.model_aliases`), возвращает соответствующее имя модели.
4. Если модель не найдена ни в списке, ни в словаре, возвращает имя модели по умолчанию (`cls.default_model`).

**Внутренние логические блоки функции**:
```
A [Начало]
|
B [Проверка model в cls.models]
|
C [Возврат model, если найдена]
|
D [Проверка model в cls.model_aliases]
|
E [Возврат cls.model_aliases[model], если найдена]
|
F [Возврат cls.default_model]
|
G [Конец]
```

**Примеры**:

```python
model_name = ChatGpt.get_model('gpt-4o')
print(model_name)
# Вывод:
# chatgpt-4o-latest

model_name = ChatGpt.get_model('gpt-3.5-turbo')
print(model_name)
# Вывод:
# gpt-3.5-turbo

model_name = ChatGpt.get_model('unknown-model')
print(model_name)
# Вывод:
# auto
```

### `ChatGpt.create_completion(model: str, messages: Messages, stream: bool, **kwargs) -> CreateResult`

**Назначение**: Создает запрос к модели ChatGPT и возвращает результат.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений.
- `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `CreateResult`: Результат запроса.

**Вызывает исключения**:
- `ValueError`: Если указанная модель недоступна.

**Как работает функция**:
1. Получает имя модели с помощью `cls.get_model(model)`.
2. Проверяет, доступна ли модель в списке `cls.models`. Если нет, вызывает исключение `ValueError`.
3. Инициализирует сессию с помощью `init_session`.
4. Получает конфигурацию с помощью `get_config`.
5. Получает токен требований с помощью `get_requirements_token`.
6. Формирует заголовки запроса, включая токены.
7. Отправляет POST-запрос к `https://chatgpt.com/backend-anon/sentinel/chat-requirements` для получения токена turnstile.
8. Если получен ответ с кодом, отличным от 200, возвращает `None`.
9. Извлекает данные из ответа, включая токен turnstile.
10. Формирует заголовки запроса, включая токен turnstile и токен требований.
11. Формирует данные запроса в формате JSON, включая сообщения, параметры модели и другие параметры.
12. Отправляет POST-запрос к `https://chatgpt.com/backend-anon/conversation` с использованием потоковой передачи данных.
13. Обрабатывает ответ, извлекая токены и возвращая их.

**Внутренние логические блоки функции**:
```
A [Начало]
|
B [Получение имени модели]
|
C [Проверка доступности модели]
|
D [Инициализация сессии]
|
E [Получение конфигурации]
|
F [Получение токена требований]
|
G [Формирование заголовков запроса]
|
H [Отправка POST-запроса для получения токена turnstile]
|
I [Извлечение данных из ответа]
|
J [Формирование заголовков запроса с токеном turnstile]
|
K [Формирование данных запроса в формате JSON]
|
L [Отправка POST-запроса с потоковой передачей данных]
|
M [Обработка ответа и извлечение токенов]
|
N [Конец]
```

**Примеры**:

```python
messages = [
    {'role': 'user', 'content': 'Hello'}
]
result = ChatGpt.create_completion(model='gpt-3.5-turbo', messages=messages, stream=True)
print(result)
# Вывод:
# <generator object Client.create_completion.<locals>.process_response at 0x...>