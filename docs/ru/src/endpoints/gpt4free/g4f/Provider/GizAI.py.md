# Модуль GizAI

## Обзор

Модуль `GizAI` предоставляет асинхронный генератор для взаимодействия с API GizAI. Он позволяет отправлять запросы к моделям GizAI, включая `chat-gemini-flash` и `gemini-1.5-flash`, и получать ответы в асинхронном режиме. Модуль поддерживает системные сообщения и историю сообщений.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-провайдерами, в частности, с GizAI. Он обеспечивает унифицированный интерфейс для отправки запросов и получения ответов от AI-моделей, что позволяет легко переключаться между различными провайдерами и моделями.

## Классы

### `GizAI`

**Описание**: Класс `GizAI` является асинхронным генератором и миксином для работы с API GizAI. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Принцип работы**:
Класс инициализирует URL и endpoint API GizAI, определяет поддерживаемые функции (стриминг, системные сообщения, историю сообщений), а также устанавливает модель по умолчанию и её alias.
Основной метод `create_async_generator` создает асинхронный генератор для отправки запросов к API GizAI и получения ответов.

**Атрибуты**:
- `url` (str): URL API GizAI.
- `api_endpoint` (str): Endpoint API для отправки запросов.
- `working` (bool): Флаг, указывающий, что провайдер работает.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер стриминг.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель по умолчанию (`chat-gemini-flash`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь alias моделей.

**Методы**:

- `get_model(model: str) -> str`
    ```python
    @classmethod
    def get_model(cls, model: str) -> str:
        """
        Определяет и возвращает модель для запроса.

        Args:
            model (str): Название модели.

        Returns:
            str: Название модели для запроса. Если указанная модель есть в списке alias, возвращает соответствующую модель.
                 В противном случае возвращает модель по умолчанию.

        Как работает функция:
        1. Проверяет, есть ли указанная модель в списке поддерживаемых моделей (`cls.models`).
        2. Если модель есть в списке поддерживаемых, возвращает её.
        3. Если модель есть в списке alias (`cls.model_aliases`), возвращает соответствующую модель.
        4. Если модель не найдена ни в списке поддерживаемых, ни в списке alias, возвращает модель по умолчанию (`cls.default_model`).

        Примеры:
            >>> GizAI.get_model('chat-gemini-flash')
            'chat-gemini-flash'
            >>> GizAI.get_model('gemini-1.5-flash')
            'chat-gemini-flash'
            >>> GizAI.get_model('unknown_model')
            'chat-gemini-flash'
        """
    ```

- `create_async_generator(model: str, messages: Messages, proxy: str = None, **kwargs) -> AsyncResult`
    ```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для отправки запросов к API GizAI.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API GizAI.

        Raises:
            Exception: Если статус ответа не 201.

        Как работает функция:
        1. Получает модель для запроса с помощью метода `get_model`.
        2. Формирует заголовки запроса (`headers`).
        3. Создает асинхронную сессию (`ClientSession`) с заданными заголовками.
        4. Формирует данные запроса (`data`) на основе списка сообщений. Системные сообщения добавляются как есть,
           а сообщения с ролями "user" и "ai" преобразуются в формат, требуемый API GizAI.
        5. Отправляет POST-запрос к API GizAI (`cls.api_endpoint`) с данными и прокси (если указан).
        6. Если статус ответа равен 201, извлекает результат (`result`) из JSON-ответа и возвращает его.
        7. В случае ошибки (статус ответа не равен 201) выбрасывает исключение с информацией о статусе и тексте ответа.

        Примеры:
            # Пример использования (требуется асинхронный контекст)
            messages = [{"role": "user", "content": "Hello, how are you?"}]
            async for message in GizAI.create_async_generator(model='chat-gemini-flash', messages=messages):
                print(message)
        """
    ```

## Функции

### `get_model`

```python
@classmethod
def get_model(cls, model: str) -> str:
    """
    Определяет и возвращает модель для запроса.

    Args:
        model (str): Название модели.

    Returns:
        str: Название модели для запроса. Если указанная модель есть в списке alias, возвращает соответствующую модель.
             В противном случае возвращает модель по умолчанию.

    Как работает функция:
    1. Проверяет, есть ли указанная модель в списке поддерживаемых моделей (`cls.models`).
    2. Если модель есть в списке поддерживаемых, возвращает её.
    3. Если модель есть в списке alias (`cls.model_aliases`), возвращает соответствующую модель.
    4. Если модель не найдена ни в списке поддерживаемых, ни в списке alias, возвращает модель по умолчанию (`cls.default_model`).

    Примеры:
        >>> GizAI.get_model('chat-gemini-flash')
        'chat-gemini-flash'
        >>> GizAI.get_model('gemini-1.5-flash')
        'chat-gemini-flash'
        >>> GizAI.get_model('unknown_model')
        'chat-gemini-flash'
    """
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для отправки запросов к API GizAI.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API GizAI.

    Raises:
        Exception: Если статус ответа не 201.

    Как работает функция:
    1. Получает модель для запроса с помощью метода `get_model`.
    2. Формирует заголовки запроса (`headers`).
    3. Создает асинхронную сессию (`ClientSession`) с заданными заголовками.
    4. Формирует данные запроса (`data`) на основе списка сообщений. Системные сообщения добавляются как есть,
       а сообщения с ролями "user" и "ai" преобразуются в формат, требуемый API GizAI.
    5. Отправляет POST-запрос к API GizAI (`cls.api_endpoint`) с данными и прокси (если указан).
    6. Если статус ответа равен 201, извлекает результат (`result`) из JSON-ответа и возвращает его.
    7. В случае ошибки (статус ответа не равен 201) выбрасывает исключение с информацией о статусе и тексте ответа.

    Примеры:
        # Пример использования (требуется асинхронный контекст)
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        async for message in GizAI.create_async_generator(model='chat-gemini-flash', messages=messages):
            print(message)
    """