# Модуль ChatGpt

## Обзор

Модуль `ChatGpt` предоставляет класс `ChatGpt`, который является провайдером для взаимодействия с API ChatGPT. Он позволяет отправлять сообщения и получать ответы, поддерживая потоковую передачу данных и управление историей сообщений. Модуль включает в себя функции для форматирования сообщений, инициализации сессии и обработки ответов от API ChatGPT.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями, предоставляемыми ChatGPT. Он обеспечивает унифицированный интерфейс для взаимодействия с этими моделями, абстрагируя детали реализации API.

## Содержание

- [Классы](#Классы)
    - [ChatGpt](#ChatGpt)
        - [Атрибуты](#Атрибуты)
        - [Методы](#Методы)
            - [get_model](#get_model)
            - [create_completion](#create_completion)
- [Функции](#Функции)
    - [format_conversation](#format_conversation)
    - [init_session](#init_session)

## Классы

### `ChatGpt`

**Описание**: Класс `ChatGpt` является провайдером для взаимодействия с API ChatGPT. Он наследует функциональность от `AbstractProvider` и `ProviderModelMixin`, предоставляя методы для отправки сообщений и получения ответов.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для провайдеров.
- `ProviderModelMixin`: Миксин, предоставляющий общую функциональность для работы с моделями.

#### Атрибуты:

- `label` (str): Метка провайдера ("ChatGpt").
- `url` (str): URL API ChatGPT ("https://chatgpt.com").
- `working` (bool): Флаг, указывающий, работает ли провайдер (False).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (True).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (True).
- `default_model` (str): Модель, используемая по умолчанию ('auto').
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

#### Методы:

- ### `get_model`
    ```python
    @classmethod
    def get_model(cls, model: str) -> str:
        """
        Возвращает имя модели, если она поддерживается, или псевдоним модели, если он существует.
        В противном случае возвращает модель по умолчанию.

        Args:
            model (str): Имя модели.

        Returns:
            str: Поддерживаемая модель или модель по умолчанию.
        """
        ...
    ```
    **Как работает функция**:

    1.  Функция `get_model` проверяет, находится ли запрошенная модель в списке поддерживаемых моделей (`cls.models`).
    2.  Если модель не найдена в списке поддерживаемых, функция проверяет, существует ли для нее псевдоним в словаре `cls.model_aliases`.
    3.  Если псевдоним найден, функция возвращает соответствующее значение псевдонима.
    4.  Если ни модель, ни псевдоним не найдены, функция возвращает модель по умолчанию (`cls.default_model`).

    **Примеры**:
    ```python
    # Пример 1: Модель поддерживается
    model = ChatGpt.get_model('gpt-3.5-turbo')
    print(model)  # Вывод: gpt-3.5-turbo

    # Пример 2: Модель имеет псевдоним
    model = ChatGpt.get_model('gpt-4o')
    print(model)  # Вывод: chatgpt-4o-latest

    # Пример 3: Модель не поддерживается, возвращается модель по умолчанию
    model = ChatGpt.get_model('unknown-model')
    print(model)  # Вывод: auto
    ```

    ASCII flowchart:

    ```
    Начало
    │
    Проверка: model in cls.models?
    │
    ├─── Да ─── Возврат model
    │
    └─── Нет ─── Проверка: model in cls.model_aliases?
        │
        ├─── Да ─── Возврат cls.model_aliases[model]
        │
        └─── Нет ─── Возврат cls.default_model
            │
            Конец
    ```
- ### `create_completion`
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
        Создает запрос на завершение текста с использованием API ChatGPT.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
            **kwargs: Дополнительные аргументы.

        Returns:
            CreateResult: Результат создания завершения текста.

        Raises:
            ValueError: Если указанная модель не поддерживается.
        """
        ...
    ```

    **Как работает функция**:

    1.  Функция `create_completion` принимает параметры, необходимые для создания запроса к API ChatGPT.
    2.  Сначала она вызывает функцию `cls.get_model(model)`, чтобы получить имя поддерживаемой модели. Если указанная модель не поддерживается, вызывается исключение `ValueError`.
    3.  Инициализируется сессия с использованием `init_session` для настройки заголовков и куки.
    4.  Получаются токены безопасности и конфигурация, необходимые для запроса.
    5.  Формируются заголовки запроса, включая токены безопасности и идентификаторы.
    6.  Создается JSON-структура данных для отправки в запросе, включающая сообщения, параметры модели и другие настройки.
    7.  Выполняется POST-запрос к API ChatGPT с использованием потоковой передачи данных (если `stream=True`).
    8.  Обрабатывается ответ от API, извлекая токены и контент из JSON-ответов.
    9.  Генерируется поток текста из полученных токенов и возвращается результат.

    ASCII flowchart:

    ```
    Начало
    │
    Получение имени модели: model = cls.get_model(model)
    │
    Проверка: model not in cls.models?
    │
    ├─── Да ─── Вызов исключения ValueError
    │
    └─── Нет ─── Инициализация сессии: session = init_session(user_agent)
        │
        Получение токенов и конфигурации
        │
        Формирование заголовков запроса
        │
        Создание JSON-структуры данных
        │
        Выполнение POST-запроса к API ChatGPT
        │
        Обработка ответа и извлечение данных
        │
        Генерация потока текста
        │
        Конец
    ```

    **Примеры**:

    ```python
    # Пример 1: Создание простого запроса
    messages = [{"role": "user", "content": "Hello, ChatGPT!"}]
    result = ChatGpt.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False)
    print(result)

    # Пример 2: Создание запроса с потоковой передачей
    messages = [{"role": "user", "content": "Tell me a story."}]
    result = ChatGpt.create_completion(model="gpt-4", messages=messages, stream=True)
    for token in result:
        print(token, end="")
    ```

## Функции

### `format_conversation`

```python
def format_conversation(messages: list):
    """
    Форматирует список сообщений в формат, требуемый API ChatGPT.

    Args:
        messages (list): Список сообщений в формате [{"role": "user" | "assistant", "content": "message text"}].

    Returns:
        list: Список сообщений, отформатированных для API ChatGPT.
    """
    ...
```

**Как работает функция**:

1.  Функция `format_conversation` принимает список сообщений в формате, который обычно используется в приложении.
2.  Для каждого сообщения в списке создается словарь, содержащий:
    *   `id`: Уникальный идентификатор сообщения, сгенерированный с помощью `uuid.uuid4()`.
    *   `author`: Информация об авторе сообщения, включая его роль (`user` или `assistant`).
    *   `content`: Содержимое сообщения, включая тип контента (`text`) и текст сообщения.
    *   `metadata`: Метаданные сообщения, содержащие информацию о смещениях символов.
    *   `create_time`: Время создания сообщения.
3.  Сформированный список сообщений возвращается.

ASCII flowchart:

```
Начало
│
Инициализация списка conversation = []
│
Для каждого message в messages:
│
    Создание словаря message_data
    │
    Добавление message_data в conversation
│
Возврат conversation
│
Конец
```

**Примеры**:
```python
# Пример вызова функции
messages = [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}]
formatted_messages = format_conversation(messages)
print(formatted_messages)
```

### `init_session`

```python
def init_session(user_agent):
    """
    Инициализирует сессию requests с необходимыми заголовками и куками.

    Args:
        user_agent (str): User-agent для использования в запросах.

    Returns:
        Session: Инициализированная сессия requests.
    """
    ...
```

**Как работает функция**:

1.  Функция `init_session` принимает user-agent в качестве аргумента.
2.  Создается объект сессии `requests.Session()`.
3.  Определяются куки `_dd_s`.
4.  Определяются заголовки, включающие user-agent, accept-language, и другие параметры.
5.  Выполняется GET-запрос к `https://chatgpt.com/` с использованием указанных куки и заголовков.
6.  Инициализированная сессия возвращается.

ASCII flowchart:

```
Начало
│
Создание сессии: session = Session()
│
Определение куки и заголовков
│
Выполнение GET-запроса к https://chatgpt.com/
│
Возврат session
│
Конец
```

**Примеры**:
```python
# Пример вызова функции
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
session = init_session(user_agent)
print(session.headers)