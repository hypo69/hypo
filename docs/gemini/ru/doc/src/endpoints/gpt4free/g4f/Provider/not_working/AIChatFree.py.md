# Модуль `AIChatFree`

## Обзор

Модуль `AIChatFree` предоставляет асинхронный интерфейс для взаимодействия с сервисом AIChatFree.info. Он позволяет генерировать текст на основе предоставленных сообщений, используя модель `gemini-1.5-pro` по умолчанию. Модуль поддерживает потоковую передачу данных и сохранение истории сообщений.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется взаимодействие с AI-моделями через API AIChatFree. Он использует асинхронные запросы для неблокирующей работы и предоставляет методы для обработки ответов от сервера.

## Функции

### `generate_signature`

```python
def generate_signature(time: int, text: str, secret: str = ""):
    """
    Генерирует SHA256-хеш для подписи запроса.

    Args:
        time (int): Временная метка в миллисекундах.
        text (str): Текст сообщения.
        secret (str, optional): Секретный ключ. По умолчанию "".

    Returns:
        str: SHA256-хеш, представленный в виде шестнадцатеричной строки.

    Как работает функция:
    1. Формирует строку сообщения, объединяя временную метку, текст и секретный ключ через двоеточие.
    2. Кодирует строку сообщения в байты, используя кодировку UTF-8.
    3. Вычисляет SHA256-хеш от закодированной строки.
    4. Возвращает хеш в виде шестнадцатеричной строки.

    ASCII Flowchart:

    Создание строки сообщения
    │
    └──> Кодирование строки в байты
         │
         └──> Вычисление SHA256-хеша
              │
              └──> Возврат хеша в виде шестнадцатеричной строки

    Примеры:
        >>> generate_signature(1678886400, "Hello", "secret")
        'e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4'
    """
    ...
```

### Класс `AIChatFree`

```python
class AIChatFree(AsyncGeneratorProvider, ProviderModelMixin):
    """
    Асинхронный провайдер для взаимодействия с сервисом AIChatFree.

    Inherits:
        AsyncGeneratorProvider: Базовый класс для асинхронных провайдеров, генерирующих данные.
        ProviderModelMixin: Миксин для работы с моделями провайдера.

    Attributes:
        url (str): URL сервиса AIChatFree.
        working (bool): Флаг, указывающий на работоспособность провайдера.
        supports_stream (bool): Флаг, указывающий на поддержку потоковой передачи данных.
        supports_message_history (bool): Флаг, указывающий на поддержку сохранения истории сообщений.
        default_model (str): Модель, используемая по умолчанию (`gemini-1.5-pro`).

    Methods:
        create_async_generator(model: str, messages: Messages, proxy: str = None, connector: BaseConnector = None, **kwargs) -> AsyncResult:
            Создает асинхронный генератор для получения ответов от сервиса.
    """
    ...
```

#### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        connector: BaseConnector = None,
        **kwargs,
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от сервиса AIChatFree.

        Args:
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            connector (BaseConnector, optional): Aiohttp connector. По умолчанию `None`.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от сервиса.

        Raises:
            RateLimitError: Если достигнут лимит запросов.
            Exception: В случае других ошибок при выполнении запроса.

        Как работает функция:
        1. Формирует заголовки запроса, включая User-Agent, Accept и Content-Type.
        2. Создает сессию aiohttp с использованием предоставленного коннектора и заголовков.
        3. Генерирует timestamp и подпись для запроса.
        4. Формирует данные запроса, преобразуя сообщения в формат, ожидаемый сервисом.
        5. Отправляет POST-запрос к API сервиса.
        6. Обрабатывает ответ, проверяя на наличие ошибок и лимитов.
        7. Возвращает асинхронный генератор, который выдает чанки данных из ответа.

        Внутренние функции:
        Нет

        ASCII Flowchart:

        Формирование заголовков запроса
        │
        └──> Создание aiohttp сессии
             │
             └──> Генерация timestamp и подписи
                  │
                  └──> Формирование данных запроса
                       │
                       └──> Отправка POST-запроса к API
                            │
                            └──> Обработка ответа
                                 │
                                 └──> Возврат асинхронного генератора

        Примеры:
            async for chunk in AIChatFree.create_async_generator(model="gemini-1.5-pro", messages=[{"role": "user", "content": "Hello"}]):
                print(chunk)
        """
    ...