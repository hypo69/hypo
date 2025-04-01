# Модуль Opchatgpts

## Обзор

Модуль `Opchatgpts` предоставляет асинхронный генератор для взаимодействия с сервисом opchatgpts.net. Он позволяет отправлять запросы к API и получать ответы в виде асинхронного потока данных. Модуль поддерживает историю сообщений и модель GPT-3.5 Turbo.

## Подробней

Этот модуль предназначен для использования в асинхронных приложениях, требующих взаимодействия с API opchatgpts.net. Он предоставляет удобный интерфейс для отправки сообщений и обработки ответов в режиме реального времени.

## Классы

### `Opchatgpts`

**Описание**: Класс `Opchatgpts` является провайдером для взаимодействия с API opchatgpts.net. Он наследуется от `AsyncGeneratorProvider` и предоставляет методы для создания асинхронного генератора, который отправляет запросы и получает ответы.

**Наследует**:
- `AsyncGeneratorProvider`

**Аттрибуты**:
- `url` (str): URL сервиса opchatgpts.net.
- `working` (bool): Указывает, работает ли провайдер (по умолчанию `False`).
- `supports_message_history` (bool): Поддерживает ли провайдер историю сообщений (по умолчанию `True`).
- `supports_gpt_35_turbo` (bool): Поддерживает ли провайдер модель GPT-3.5 Turbo (по умолчанию `True`).

#### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None, **kwargs) -> AsyncResult:
        """ Создает асинхронный генератор для взаимодействия с API opchatgpts.net.

        Args:
            model (str): Модель, используемая для генерации ответа.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API.

        Raises:
            RuntimeError: Если получен некорректный формат данных от API.

        """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API opchatgpts.net.

**Параметры**:
- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если получен некорректный формат данных от API.

**Как работает функция**:

1.  **Формирование заголовков**: Функция формирует заголовки HTTP-запроса, включая User-Agent, Accept, Origin и Referer.
2.  **Создание сессии**: Создается асинхронная сессия `aiohttp.ClientSession` с использованием заданных заголовков.
3.  **Подготовка данных**: Подготавливаются данные для отправки в теле запроса, включая `botId`, `chatId`, `contextId`, `messages` и другие параметры.
4.  **Отправка запроса**: Отправляется POST-запрос к API `f"{cls.url}/wp-json/mwai-ui/v1/chats/submit"` с использованием созданной сессии и подготовленных данных.
5.  **Обработка ответа**:
    *   Функция итерируется по строкам в ответе сервера.
    *   Каждая строка проверяется на наличие префикса `b"data: "`.
    *   Если строка начинается с этого префикса, она декодируется и преобразуется в JSON.
    *   Проверяется наличие ключа `"type"` в полученном JSON.
    *   Если `line["type"] == "live"`, то извлекаются данные из `line["data"]` и возвращаются через `yield`.
    *   Если `line["type"] == "end"`, то цикл завершается.
6.  **Обработка ошибок**: Если в процессе обработки ответа возникают ошибки (например, некорректный формат JSON), выбрасывается исключение `RuntimeError`.

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.deprecated.Opchatgpts import Opchatgpts
from typing import List, Dict

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]
    proxy = None

    async for response in Opchatgpts.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```
В этом примере создается асинхронный генератор `Opchatgpts.create_async_generator` с моделью "gpt-3.5-turbo" и сообщением "Hello, how are you?". Затем происходит итерация по ответам, возвращаемым генератором, и каждый ответ выводится на экран.

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.deprecated.Opchatgpts import Opchatgpts
from typing import List, Dict

async def main():
    model = "gpt-3.5-turbo"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Tell me a joke."},
        {"role": "assistant", "content": "Why don't scientists trust atoms? Because they make up everything!"},
        {"role": "user", "content": "Tell me another one."}
    ]
    proxy = None

    async for response in Opchatgpts.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

В этом примере демонстрируется использование истории сообщений. Список `messages` содержит несколько сообщений, включая вопрос пользователя и ответ ассистента. Новый вопрос пользователя добавляется в конец списка, и вся история передается в `create_async_generator`.