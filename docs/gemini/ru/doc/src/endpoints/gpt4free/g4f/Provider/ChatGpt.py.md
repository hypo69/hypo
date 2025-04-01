# Модуль ChatGpt

## Обзор

Модуль `ChatGpt` предоставляет класс `ChatGpt`, который является провайдером для взаимодействия с моделью ChatGpt. Он позволяет создавать запросы к ChatGpt и получать ответы, поддерживая потоковую передачу данных и управление историей сообщений.

## Подробней

Модуль предназначен для интеграции с различными AI-моделями через API ChatGpt, обеспечивая гибкость в выборе модели и настройке параметров запроса. Он включает в себя функции для форматирования сообщений, инициализации сессии и обработки ответов от API ChatGpt.

## Классы

### `ChatGpt`

**Описание**: Класс `ChatGpt` является провайдером для взаимодействия с моделью ChatGpt.

**Принцип работы**:
1.  Инициализируется с базовыми параметрами, такими как `label`, `url`, `working`, `supports_message_history`, `supports_system_message`, `supports_stream`, `default_model` и `models`.
2.  Поддерживает выбор различных моделей ChatGpt, таких как `gpt-3.5-turbo`, `gpt-4o`, `gpt-4` и другие.
3.  Использует методы для форматирования сообщений, инициализации сессии и создания запросов к API ChatGpt.
4.  Обрабатывает ответы от API ChatGpt, поддерживая потоковую передачу данных.

**Методы**:

*   `get_model(model: str) -> str`: Возвращает имя модели на основе предоставленного имени или псевдонима.
*   `create_completion(model: str, messages: Messages, stream: bool, **kwargs) -> CreateResult`: Создает запрос к API ChatGpt и возвращает результат.

#### `get_model`

```python
    @classmethod
    def get_model(cls, model: str) -> str:
        """
        Возвращает имя модели на основе предоставленного имени или псевдонима.

        Args:
            model (str): Имя модели или псевдоним.

        Returns:
            str: Имя модели.
        """
```

**Как работает функция**:

1.  Функция `get_model` принимает имя модели в качестве аргумента.
2.  Если имя модели есть в списке поддерживаемых моделей `cls.models`, функция возвращает это имя.
3.  Если имя модели есть в словаре псевдонимов `cls.model_aliases`, функция возвращает соответствующее значение из словаря.
4.  В противном случае функция возвращает имя модели по умолчанию `cls.default_model`.

**Примеры**:

```python
ChatGpt.get_model('gpt-4o')  # Возвращает 'chatgpt-4o-latest'
ChatGpt.get_model('gpt-3.5-turbo')  # Возвращает 'gpt-3.5-turbo'
ChatGpt.get_model('unknown-model')  # Возвращает 'auto'
```

#### `create_completion`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        **kwargs
    ) -> CreateResult:
        """
        Создает запрос к API ChatGpt и возвращает результат.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
            **kwargs: Дополнительные аргументы.

        Returns:
            CreateResult: Результат запроса.

        Raises:
            ValueError: Если указанная модель недоступна.
        """
```

**Как работает функция**:

1.  Функция `create_completion` принимает имя модели, список сообщений и флаг потоковой передачи данных в качестве аргументов.
2.  Функция вызывает `cls.get_model(model)` для получения имени модели на основе предоставленного имени или псевдонима.
3.  Если полученное имя модели отсутствует в списке поддерживаемых моделей `cls.models`, функция вызывает исключение `ValueError`.
4.  Функция инициализирует сессию с использованием `init_session(user_agent)`.
5.  Функция получает конфигурацию с использованием `get_config(user_agent)`.
6.  Функция получает токен требований с использованием `get_requirements_token(config)`.
7.  Функция отправляет POST-запрос к `https://chatgpt.com/backend-anon/sentinel/chat-requirements` для получения данных, необходимых для дальнейших запросов.
8.  Если требуется, функция обрабатывает `turnstile` с использованием `process_turnstile(turnstile_dx, pow_req)`.
9.  Функция отправляет POST-запрос к `https://chatgpt.com/backend-anon/conversation` с данными о разговоре и заголовками, содержащими токены безопасности.
10. Функция обрабатывает ответ от API ChatGpt, поддерживая потоковую передачу данных, и возвращает результат.

**Примеры**:

```python
messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
result = ChatGpt.create_completion(model='gpt-3.5-turbo', messages=messages, stream=True)
for token in result:
    print(token)
```

## Функции

### `format_conversation`

```python
def format_conversation(messages: list):
    """
    Форматирует список сообщений в формат, ожидаемый API ChatGpt.

    Args:
        messages (list): Список сообщений.

    Returns:
        list: Список сообщений в формате, ожидаемом API ChatGpt.
    """
```

**Как работает функция**:

1.  Функция `format_conversation` принимает список сообщений в качестве аргумента.
2.  Для каждого сообщения в списке функция создает словарь, содержащий информацию об идентификаторе сообщения, авторе, содержимом и метаданных.
3.  Функция возвращает список словарей, представляющих сообщения в формате, ожидаемом API ChatGpt.

**Примеры**:

```python
messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
formatted_messages = format_conversation(messages)
print(formatted_messages)
```

### `init_session`

```python
def init_session(user_agent):
    """
    Инициализирует сессию с заданным User-Agent.

    Args:
        user_agent: User-Agent для сессии.

    Returns:
        Session: Инициализированная сессия.
    """
```

**Как работает функция**:

1.  Функция `init_session` принимает User-Agent в качестве аргумента.
2.  Функция создает объект сессии `requests.Session`.
3.  Функция устанавливает куки и заголовки для сессии.
4.  Функция выполняет GET-запрос к `https://chatgpt.com/` для инициализации сессии.
5.  Функция возвращает объект сессии.

**Примеры**:

```python
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
session = init_session(user_agent)
print(session)