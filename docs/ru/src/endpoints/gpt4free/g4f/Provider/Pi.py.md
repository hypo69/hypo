# Модуль `Pi`

## Обзор

Модуль `Pi` предназначен для асинхронного взаимодействия с AI-сервисом Pi.ai для генерации текста. Он предоставляет класс `Pi`, который наследуется от `AsyncGeneratorProvider` и использует асинхронные генераторы для потоковой передачи ответов. Модуль поддерживает работу через прокси, установку таймаутов и сохранение истории переписки.

## Подробней

Модуль `Pi` является провайдером для библиотеки `g4f` и обеспечивает интеграцию с сервисом Pi.ai. Он использует асинхронные запросы для обмена сообщениями с сервером и поддерживает потоковую передачу данных, что позволяет получать ответы в реальном времени.

## Классы

### `Pi`

**Описание**: Класс `Pi` предоставляет методы для взаимодействия с сервисом Pi.ai. Он позволяет начинать новые диалоги, отправлять запросы и получать ответы в асинхронном режиме.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:
- `url` (str): URL-адрес сервиса Pi.ai.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `use_nodriver` (bool): Флаг, указывающий на использование без драйвера.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных.
- `default_model` (str): Модель, используемая по умолчанию ("pi").
- `models` (List[str]): Список поддерживаемых моделей (только "pi").
- `_headers` (dict): Заголовки HTTP-запроса.
- `_cookies` (Cookies): Куки для HTTP-запроса.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от сервиса.
- `start_conversation()`: Начинает новый диалог с сервисом и возвращает идентификатор диалога.
- `get_chat_history()`: Получает историю переписки по идентификатору диалога.
- `ask()`: Отправляет запрос в сервис и возвращает асинхронный генератор ответов.

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        proxy: str = None,
        timeout: int = 180,
        conversation_id: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от сервиса Pi.ai.

        Args:
            model (str): Модель для генерации текста.
            messages (Messages): Список сообщений для отправки в сервис.
            stream (bool): Флаг, указывающий на необходимость потоковой передачи данных.
            proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
            timeout (int, optional): Время ожидания ответа от сервиса. По умолчанию 180.
            conversation_id (str, optional): Идентификатор существующего диалога. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от сервиса.

        Как работает функция:
        1. Проверяет, инициализированы ли заголовки запроса (`cls._headers`). Если нет, получает их с помощью `get_args_from_nodriver`.
        2. Использует `StreamSession` для выполнения асинхронных запросов.
        3. Если `conversation_id` не передан, начинает новый диалог с помощью `start_conversation`.
        4. Форматирует запрос с помощью `format_prompt`.
        5. Отправляет запрос в сервис с помощью `ask` и получает асинхронный генератор ответов.

        Внутренние функции: нет

        """
```

#### ASCII Flowchart функции `create_async_generator`

```
    Начало
    │
    ├──> Проверка инициализации заголовков (cls._headers)
    │   └──> Нет: Получение заголовков и куки через get_args_from_nodriver
    │
    ├──> Создание StreamSession
    │
    ├──> Проверка conversation_id
    │   └──> Нет: Запуск нового диалога через start_conversation
    │
    ├──> Форматирование запроса через format_prompt
    │
    └──> Отправка запроса через ask
    │   └──> Получение асинхронного генератора ответов
    │
    Конец
```

#### Примеры вызова функции `create_async_generator`

```python
# Пример 1: Создание генератора для нового диалога
async for message in Pi.create_async_generator(model='pi', messages=[{'role': 'user', 'content': 'Hello'}], stream=True):
    print(message)

# Пример 2: Создание генератора для существующего диалога
async for message in Pi.create_async_generator(model='pi', messages=[{'role': 'user', 'content': 'Continue'}], stream=True, conversation_id='123'):
    print(message)
```

### `start_conversation`

```python
    @classmethod
    async def start_conversation(cls, session: StreamSession) -> str:
        """
        Начинает новый диалог с сервисом Pi.ai и возвращает идентификатор диалога.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения запросов.

        Returns:
            str: Идентификатор нового диалога.

        Как работает функция:
        1. Отправляет POST-запрос на URL-адрес `https://pi.ai/api/chat/start` с пустыми данными.
        2. Устанавливает заголовок `accept` в значение `application/json` и `x-api-version` в значение `3`.
        3. Извлекает идентификатор диалога (`sid`) из JSON-ответа.

        Внутренние функции: нет
        """
```

#### ASCII Flowchart функции `start_conversation`

```
    Начало
    │
    ├──> Отправка POST-запроса на https://pi.ai/api/chat/start
    │   └──> Установка заголовков accept и x-api-version
    │
    ├──> Извлечение идентификатора диалога (sid) из JSON-ответа
    │
    Конец
```

#### Примеры вызова функции `start_conversation`

```python
# Пример: Запуск нового диалога
session = StreamSession()
conversation_id = await Pi.start_conversation(session)
print(conversation_id)
```

### `get_chat_history`

```python
    async def get_chat_history(session: StreamSession, conversation_id: str):
        """
        Получает историю переписки по идентификатору диалога.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения запросов.
            conversation_id (str): Идентификатор диалога.

        Returns:
            dict: JSON-ответ, содержащий историю переписки.

        Как работает функция:
        1. Формирует параметры запроса, включая `conversation_id`.
        2. Отправляет GET-запрос на URL-адрес `https://pi.ai/api/chat/history` с параметрами.
        3. Возвращает JSON-ответ, содержащий историю переписки.

        Внутренние функции: нет
        """
```

#### ASCII Flowchart функции `get_chat_history`

```
    Начало
    │
    ├──> Формирование параметров запроса (conversation_id)
    │
    ├──> Отправка GET-запроса на https://pi.ai/api/chat/history
    │
    └──> Возврат JSON-ответа с историей переписки
    │
    Конец
```

#### Примеры вызова функции `get_chat_history`

```python
# Пример: Получение истории переписки
session = StreamSession()
history = await Pi.get_chat_history(session, '123')
print(history)
```

### `ask`

```python
    @classmethod
    async def ask(cls, session: StreamSession, prompt: str, conversation_id: str):
        """
        Отправляет запрос в сервис Pi.ai и возвращает асинхронный генератор ответов.

        Args:
            session (StreamSession): Асинхронная сессия для выполнения запросов.
            prompt (str): Текст запроса.
            conversation_id (str): Идентификатор диалога.

        Yields:
            str: Часть ответа от сервиса.

        Как работает функция:
        1. Формирует JSON-данные для запроса, включая `text`, `conversation_id` и `mode`.
        2. Отправляет POST-запрос на URL-адрес `https://pi.ai/api/chat` с JSON-данными.
        3. Обновляет куки (`cls._cookies`) на основе ответа.
        4. Итерируется по строкам ответа и извлекает текстовые данные из строк, начинающихся с `data: {"text":` или `data: {"title":`.

        Внутренние функции: нет
        """
```

#### ASCII Flowchart функции `ask`

```
    Начало
    │
    ├──> Формирование JSON-данных для запроса
    │   └──> Включение text, conversation_id и mode
    │
    ├──> Отправка POST-запроса на https://pi.ai/api/chat
    │
    ├──> Обновление куки (cls._cookies)
    │
    ├──> Итерация по строкам ответа
    │   └──> Извлечение текстовых данных из строк, начинающихся с data: {"text": или data: {"title":
    │
    Конец
```

#### Примеры вызова функции `ask`

```python
# Пример: Отправка запроса и получение ответа
session = StreamSession()
async for line in Pi.ask(session, 'Hello', '123'):
    print(line)