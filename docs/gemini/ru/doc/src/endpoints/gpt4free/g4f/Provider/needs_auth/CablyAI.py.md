# Модуль `CablyAI.py`

## Обзор

Модуль `CablyAI.py` предназначен для работы с провайдером CablyAI, который предоставляет API для взаимодействия с моделями OpenAI. Он наследует функциональность от класса `OpenaiTemplate` и адаптирует её для специфических требований CablyAI. Модуль поддерживает аутентификацию, потоковую передачу данных, системные сообщения и историю сообщений.

## Подробней

Этот модуль является частью системы `gpt4free` в проекте `hypotez` и отвечает за взаимодействие с сервисом CablyAI. Он использует шаблон `OpenaiTemplate` для реализации основных функций и переопределяет необходимые параметры, такие как URL, заголовки и требования к аутентификации.

## Классы

### `CablyAI`

**Описание**: Класс `CablyAI` предоставляет интерфейс для взаимодействия с API CablyAI.

**Наследует**:
- `OpenaiTemplate`: Класс наследует от `OpenaiTemplate`, который предоставляет базовую функциональность для работы с API OpenAI.

**Атрибуты**:
- `url` (str): URL для доступа к чату CablyAI (`https://cablyai.com/chat`).
- `login_url` (str): URL для входа в CablyAI (`https://cablyai.com`).
- `api_base` (str): Базовый URL для API CablyAI (`https://cablyai.com/v1`).
- `working` (bool): Указывает, что провайдер CablyAI в настоящее время работает (`True`).
- `needs_auth` (bool): Указывает, что для доступа к CablyAI требуется аутентификация (`True`).
- `supports_stream` (bool): Указывает, что CablyAI поддерживает потоковую передачу данных (`True`).
- `supports_system_message` (bool): Указывает, что CablyAI поддерживает системные сообщения (`True`).
- `supports_message_history` (bool): Указывает, что CablyAI поддерживает историю сообщений (`True`).

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
    """Создает асинхронный генератор для взаимодействия с API CablyAI.

    Args:
        cls: Ссылка на класс.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий, следует ли использовать потоковую передачу данных. По умолчанию `False`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный результат.

    Raises:
        ModelNotSupportedError: Если указанная модель не поддерживается.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API CablyAI.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Имя используемой модели.
- `messages (Messages)`: Список сообщений для отправки.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `stream` (bool, optional): Флаг, указывающий, следует ли использовать потоковую передачу данных. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный результат.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если указанная модель не поддерживается.

**Как работает функция**:
1. Функция создает заголовки, необходимые для аутентификации и взаимодействия с API CablyAI. В заголовки включается API-ключ, тип контента, информация о браузере пользователя и другие параметры.
2. Вызывается метод `create_async_generator` из суперкласса `OpenaiTemplate` с передачей необходимых параметров, включая модель, сообщения, API-ключ, флаг потоковой передачи и заголовки.

**ASCII flowchart**:

```
A: Создание заголовков
|
B: Вызов create_async_generator из OpenaiTemplate
|
C: Возврат AsyncResult
```

**Примеры**:

```python
# Пример использования create_async_generator
from typing import List, Dict, Optional

class Messages:
    def __init__(self, messages: List[Dict]):
        self.messages = messages

    def __iter__(self):
        return iter(self.messages)

    def __len__(self):
        return len(self.messages)

    def __getitem__(self, index):
        return self.messages[index]

async def example():
    model = "gpt-3.5-turbo"
    messages = Messages([{"role": "user", "content": "Hello"}])
    api_key = "your_api_key"
    stream = True
    result = CablyAI.create_async_generator(model=model, messages=messages, api_key=api_key, stream=stream)
    print(result)

# Запустите пример
# import asyncio
# asyncio.run(example())