# Модуль CablyAI для работы с OpenAI API через CablyAI

## Обзор

Модуль `CablyAI` предоставляет класс `CablyAI`, который является подклассом `OpenaiTemplate`. Он предназначен для взаимодействия с API CablyAI, который, в свою очередь, предоставляет доступ к моделям OpenAI. Этот модуль обеспечивает поддержку аутентификации, потоковой передачи данных, системных сообщений и истории сообщений. Он адаптирован для использования с асинхронными генераторами.

## Подробней

Модуль `CablyAI` позволяет взаимодействовать с OpenAI API через сервис CablyAI. Он определяет URL, базовый URL API, указывает на необходимость аутентификации и поддерживает потоковую передачу данных. Основная функциональность заключается в создании асинхронного генератора для обмена сообщениями с моделью OpenAI через CablyAI.

## Классы

### `CablyAI`

**Описание**: Класс `CablyAI` является подклассом `OpenaiTemplate` и предоставляет интерфейс для работы с API CablyAI, который, в свою очередь, предоставляет доступ к моделям OpenAI.

**Наследует**:
- `OpenaiTemplate`: Наследует функциональность шаблона OpenAI.

**Атрибуты**:
- `url` (str): URL сервиса CablyAI.
- `login_url` (str): URL страницы для входа в CablyAI.
- `api_base` (str): Базовый URL API CablyAI.
- `working` (bool): Указывает, что сервис CablyAI работает.
- `needs_auth` (bool): Указывает на необходимость аутентификации.
- `supports_stream` (bool): Указывает на поддержку потоковой передачи данных.
- `supports_system_message` (bool): Указывает на поддержку системных сообщений.
- `supports_message_history` (bool): Указывает на поддержку истории сообщений.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API CablyAI.

## Функции

### `create_async_generator`

```python
@classmethod
def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    stream: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API CablyAI.

    Args:
        model (str): Имя модели OpenAI для использования.
        messages (Messages): Список сообщений для отправки в API.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        stream (bool, optional): Указывает, следует ли использовать потоковую передачу данных. По умолчанию `False`.
        **kwargs: Дополнительные параметры для передачи в базовый класс.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.

    Raises:
        ModelNotSupportedError: Если указанная модель не поддерживается.

    """
```

**Назначение**: Создает асинхронный генератор для обмена сообщениями с моделью OpenAI через API CablyAI.

**Параметры**:
- `cls`: Ссылка на класс `CablyAI`.
- `model` (str): Имя модели OpenAI для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу данных. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры для передачи в базовый класс.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если указанная модель не поддерживается.

**Как работает функция**:

1.  **Определение заголовков**: Функция создает заголовки HTTP-запроса, включая токен авторизации (API ключ), тип контента, источник запроса и User-Agent.
2.  **Вызов родительского метода**:  Функция вызывает метод `create_async_generator` из родительского класса (`OpenaiTemplate`), передавая все необходимые параметры, включая заголовки.

```
Определение заголовков --> Вызов create_async_generator из OpenaiTemplate
```

**Примеры**:

```python
# Пример использования create_async_generator
from g4f.Provider.needs_auth import CablyAI
from g4f.models import gpt_35_turbo

# Предположим, что у вас есть список сообщений messages и API ключ api_key
messages = [{"role": "user", "content": "Hello, CablyAI!"}]
api_key = "ваш_api_ключ"

# Создание асинхронного генератора
async_generator = CablyAI.create_async_generator(model=gpt_35_turbo.name, messages=messages, api_key=api_key, stream=True)

# Дальнейшая работа с асинхронным генератором
# async for response in async_generator:
#     print(response)