# Модуль `GizAI`

## Обзор

Модуль `GizAI` предоставляет асинхронный генератор для взаимодействия с API GizAI. Он позволяет генерировать ответы от AI-моделей, таких как `chat-gemini-flash`. Модуль поддерживает системные сообщения и историю сообщений.

## Подробнее

Этот модуль используется для обмена сообщениями с AI-моделями через API GizAI. Он форматирует сообщения и отправляет их в API, а затем генерирует ответы, используя асинхронные генераторы.

## Классы

### `GizAI`

**Описание**: Класс `GizAI` является поставщиком асинхронного генератора и миксином для работы с моделями.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса GizAI (`https://app.giz.ai/assistant`).
- `api_endpoint` (str): URL API для отправки запросов (`https://app.giz.ai/api/data/users/inferenceServer.infer`).
- `working` (bool): Указывает, работает ли провайдер (всегда `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (всегда `False`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (всегда `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (всегда `True`).
- `default_model` (str): Модель, используемая по умолчанию (`chat-gemini-flash`).
- `models` (list[str]): Список поддерживаемых моделей (только `default_model`).
- `model_aliases` (dict[str, str]): Псевдонимы моделей (например, `{"gemini-1.5-flash": "chat-gemini-flash"}`).

**Методы**:
- `get_model(model: str) -> str`: Возвращает имя модели на основе псевдонима или использует модель по умолчанию.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API GizAI.

## Функции

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str) -> str:
        """
        Возвращает имя модели на основе псевдонима или использует модель по умолчанию.

        Args:
            model (str): Имя модели или псевдоним.

        Returns:
            str: Имя модели.
        """
        ...
```

**Назначение**: Функция `get_model` преобразует входное имя модели в поддерживаемое. Если указана модель из списка псевдонимов, возвращается соответствующая модель. В противном случае возвращается модель по умолчанию.

**Параметры**:
- `model` (str): Имя модели или псевдоним модели.

**Возвращает**:
- `str`: Имя модели, которое будет использоваться для запроса.

**Как работает функция**:

1.  **Проверка наличия модели в списке `models`**: Проверяется, является ли входная модель (`model`) одним из элементов списка `cls.models`.
2.  **Проверка наличия модели в списке псевдонимов `model_aliases`**: Если модель не найдена в основном списке, проверяется, есть ли она в словаре псевдонимов `cls.model_aliases`.
3.  **Возврат модели по умолчанию**: Если модель не найдена ни в основном списке, ни в списке псевдонимов, возвращается модель по умолчанию `cls.default_model`.

```
Модель_или_псевдоним --> [Проверка в cls.models]
|   Нет                Да
|   --> [Проверка в cls.model_aliases] --> Модель
|       Нет               Да
|       --> Модель по умолчанию
```

**Примеры**:

```python
# Пример 1: Использование поддерживаемой модели
model = GizAI.get_model('chat-gemini-flash')
print(model)  # Вывод: chat-gemini-flash

# Пример 2: Использование псевдонима модели
model = GizAI.get_model('gemini-1.5-flash')
print(model)  # Вывод: chat-gemini-flash

# Пример 3: Использование неподдерживаемой модели
model = GizAI.get_model('unsupported-model')
print(model)  # Вывод: chat-gemini-flash
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
        Создает асинхронный генератор для получения ответов от API GizAI.

        Args:
            model (str): Имя модели.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API.

        Raises:
            Exception: Если возникает ошибка при запросе к API.
        """
        ...
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API GizAI. Она принимает сообщения, модель и прокси (опционально), отправляет запрос к API и генерирует ответы.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера (если требуется). По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Вызывает исключения**:
- `Exception`: Вызывается, если статус ответа не равен 201 или при возникновении других ошибок при запросе к API.

**Внутренние функции**:
- Отсутствуют.

**Как работает функция**:

1.  **Получение имени модели**: Использует функцию `cls.get_model(model)` для получения корректного имени модели.
2.  **Формирование заголовков**: Создает словарь `headers` с необходимыми HTTP-заголовками для запроса.
3.  **Асинхронный контекст `ClientSession`**: Использует `aiohttp.ClientSession` для выполнения асинхронных HTTP-запросов.
4.  **Формирование данных запроса**: Создает словарь `data` с параметрами запроса, включая модель и сообщения. Сообщения форматируются в соответствии с требованиями API GizAI.
5.  **Отправка POST-запроса**: Отправляет POST-запрос к `cls.api_endpoint` с использованием `session.post()`.
6.  **Обработка ответа**:
    *   Если статус ответа равен 201, извлекает результат из JSON-ответа и выдает его с помощью `yield`.
    *   В противном случае вызывает исключение `Exception` с информацией о статусе ответа и текстом ошибки.

```
Начало --> Получение имени модели --> Формирование заголовков --> Асинхронный контекст ClientSession
|
--> Формирование данных запроса --> Отправка POST-запроса --> Обработка ответа
|   Статус 201 --> Извлечение и выдача результата
|   Статус !201 --> Вызов исключения
```

**Примеры**:

```python
# Пример использования асинхронного генератора
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, how are you?"}
    ]

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for message in generator:
            print(f"Response: {message}")

    generator = GizAI.create_async_generator(model='chat-gemini-flash', messages=messages)
    await consume_generator(generator)

if __name__ == "__main__":
    asyncio.run(main())