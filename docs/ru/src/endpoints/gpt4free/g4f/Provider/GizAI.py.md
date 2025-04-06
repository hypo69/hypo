# Модуль GizAI

## Обзор

Модуль `GizAI` предоставляет асинхронный класс `GizAI`, который используется для взаимодействия с API GizAI для генерации текста. Он поддерживает указание модели, прокси и передачу истории сообщений.

## Подробней

Модуль предназначен для интеграции с сервисом GizAI, предоставляя удобный интерфейс для отправки запросов к API и получения ответов. Класс `GizAI` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет использовать его как асинхронный генератор.

## Классы

### `GizAI(AsyncGeneratorProvider, ProviderModelMixin)`

**Описание**: Класс `GizAI` предоставляет интерфейс для взаимодействия с API GizAI.

**Принцип работы**:
1.  Инициализирует класс с URL и endpoint API GizAI.
2.  Определяет, поддерживает ли стриминг и системные сообщения.
3.  Позволяет получить модель, проверить ее наличие в списке поддерживаемых моделей или использовать псевдоним.
4.  Создает асинхронный генератор для получения ответов от API GizAI.

**Атрибуты**:

*   `url` (str): URL сервиса GizAI.
*   `api_endpoint` (str): URL API endpoint для запросов.
*   `working` (bool): Флаг, показывающий, что провайдер работает.
*   `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер стриминг.
*   `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
*   `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
*   `default_model` (str): Модель, используемая по умолчанию.
*   `models` (list): Список поддерживаемых моделей.
*   `model_aliases` (dict): Словарь с псевдонимами моделей.

**Методы**:

*   `get_model(model: str) -> str`: Возвращает модель, проверяя ее наличие в списке поддерживаемых моделей или используя псевдоним.
*   `create_async_generator(model: str, messages: Messages, proxy: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API GizAI.

## Функции

### `get_model(model: str) -> str`

```python
@classmethod
def get_model(cls, model: str) -> str:
    """
    Возвращает модель, проверяя ее наличие в списке поддерживаемых моделей или используя псевдоним.

    Args:
        model (str): Имя модели.

    Returns:
        str: Поддерживаемая модель или модель по умолчанию.
    """
    ...
```

**Назначение**: Функция `get_model` определяет, какая модель будет использоваться для запроса к API GizAI. Она проверяет, есть ли указанная модель в списке поддерживаемых, использует псевдоним, если он есть, или возвращает модель по умолчанию.

**Параметры**:

*   `model` (str): Имя модели, которую нужно получить.

**Возвращает**:

*   `str`: Строка, представляющая поддерживаемую модель.

**Как работает функция**:

1.  Проверяет, есть ли модель в списке `cls.models`.
2.  Если нет, проверяет, есть ли модель в словаре псевдонимов `cls.model_aliases`.
3.  Если и там нет, возвращает модель по умолчанию `cls.default_model`.

**Примеры**:

```python
# Пример 1: Модель из списка поддерживаемых
model = GizAI.get_model('chat-gemini-flash')
print(model)  # Вывод: chat-gemini-flash

# Пример 2: Модель через псевдоним
GizAI.model_aliases = {"gemini-1.5-flash": "chat-gemini-flash"}
model = GizAI.get_model('gemini-1.5-flash')
print(model)  # Вывод: chat-gemini-flash

# Пример 3: Модель по умолчанию
GizAI.models = ['chat-gemini-flash']
GizAI.model_aliases = {}
GizAI.default_model = 'chat-gemini-flash'
model = GizAI.get_model('unknown-model')
print(model) # Вывод: chat-gemini-flash
```

### `create_async_generator(model: str, messages: Messages, proxy: str = None, **kwargs) -> AsyncResult`

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
        proxy (str, optional): URL прокси-сервера. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов.

    Raises:
        Exception: Если статус ответа не 201.
    """
    ...
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор, который отправляет запросы к API GizAI и возвращает ответы.

**Параметры**:

*   `model` (str): Имя модели для использования.
*   `messages` (Messages): Список сообщений, которые нужно отправить в API.
*   `proxy` (str, optional): URL прокси-сервера (если требуется). По умолчанию `None`.
*   `**kwargs`: Дополнительные параметры.

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор, выдающий ответы от API GizAI.

**Вызывает исключения**:

*   `Exception`: Если статус ответа от API не равен 201.

**Как работает функция**:

1.  Определяет модель с помощью `cls.get_model(model)`.
2.  Формирует заголовки HTTP-запроса.
3.  Создает сессию `ClientSession` с заданными заголовками.
4.  Формирует данные запроса, преобразуя список сообщений в нужный формат.
5.  Отправляет POST-запрос к API GizAI.
6.  Если статус ответа равен 201, извлекает результат из JSON и выдает его через `yield`.
7.  Если статус ответа не равен 201, вызывает исключение с информацией об ошибке.

**ASCII flowchart**:

```
    Получение модели
        │
    Формирование заголовков
        │
    Создание сессии ClientSession
        │
    Формирование данных запроса
        │
    Отправка POST-запроса к API GizAI
        │
    Проверка статуса ответа == 201 ?
    ├─── Да ───→ Извлечение результата из JSON и выдача через yield
    └─── Нет ───→ Вызов исключения с информацией об ошибке
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict

async def main():
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Hello, GizAI!"}
    ]
    
    async for response in GizAI.create_async_generator(model='chat-gemini-flash', messages=messages):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())