# Модуль `Berlin`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с API Berlin, который предоставляет доступ к моделям, подобным GPT-3.5 Turbo. Модуль использует `aiohttp` для асинхронных HTTP-запросов и предоставляет удобный способ получения ответов от API Berlin в виде асинхронного генератора.

## Подробнее

Модуль предназначен для использования в асинхронных приложениях, где требуется взаимодействие с Berlin API для генерации текста на основе предоставленных сообщений. Он автоматически управляет аутентификацией, используя токен, и предоставляет гибкие параметры для настройки запросов к API. Модуль является частью большого проекта `hypotez`

## Классы

### `Berlin`

**Описание**: Класс `Berlin` предоставляет асинхронный генератор для взаимодействия с Berlin API.

**Принцип работы**:
1. Класс использует URL `https://ai.berlin4h.top` для взаимодействия с API.
2. Поддерживает модель `gpt-3.5-turbo`.
3. Аутентифицируется с использованием учетных данных и сохраняет токен для последующих запросов.
4. Форматирует сообщения и отправляет их в API для получения ответов.
5. Возвращает ответы в виде асинхронного генератора.

**Атрибуты**:
- `url` (str): URL для взаимодействия с API (`https://ai.berlin4h.top`).
- `working` (bool): Указывает, работает ли провайдер. Изначально установлено в `False`.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo`. Установлено в `True`.
- `_token` (str | None): Токен аутентификации, полученный от API. Изначально установлено в `None`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API.

## Функции

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
    Создает асинхронный генератор для взаимодействия с API Berlin.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы для передачи в API.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        RuntimeError: Если возникает ошибка при обработке ответа от API.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Berlin.

**Параметры**:
- `cls` (class): Ссылка на класс `Berlin`.
- `model` (str): Название модели для использования. Если не указано, используется `gpt-3.5-turbo`.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для передачи в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если возникает ошибка при обработке ответа от API.

**Как работает функция**:

1. **Проверка и установка модели**: Если модель не указана, устанавливается значение по умолчанию `gpt-3.5-turbo`.
2. **Формирование заголовков**: Создаются HTTP-заголовки, необходимые для запроса к API.
3. **Создание сессии `aiohttp`**: Создается асинхронная сессия `aiohttp` для выполнения HTTP-запросов.
4. **Аутентификация**:
   - Если токен отсутствует (`cls._token is None`), выполняется запрос на аутентификацию для получения токена.
   - Учетные данные для аутентификации: `account`: `'免费使用GPT3.5模型@163.com'`, `password`: `'659e945c2d004686bad1a75b708c962f'`.
   - Полученный токен сохраняется в `cls._token` для последующих запросов.
5. **Формирование данных запроса**:
   - Форматируются сообщения с использованием функции `format_prompt(messages)`.
   - Создается словарь `data`, содержащий параметры запроса, включая `prompt`, `parentMessageId`, `options` (модель, температура, штрафы и максимальное количество токенов).
6. **Отправка запроса и обработка ответа**:
   - Отправляется POST-запрос к API (`f"{cls.url}/api/chat/completions"`) с использованием `aiohttp`.
   - Ответ обрабатывается по частям (chunks) в асинхронном режиме.
   - Каждая часть ответа преобразуется из JSON и извлекается содержимое (`["content"]`).
   - Если при обработке JSON возникает ошибка, вызывается исключение `RuntimeError` с информацией о необработанном содержимом.
7. **Генерация результатов**:
   - Функция является асинхронным генератором, который выдает извлеченное содержимое (`content`) из каждой части ответа.

**Внутренние функции**: Отсутствуют

**ASCII flowchart**:

```
A [Проверка наличия модели]
|
B [Если модель отсутствует, установка gpt-3.5-turbo]
|
C [Формирование HTTP-заголовков]
|
D [Создание асинхронной сессии aiohttp]
|
E [Проверка наличия токена]
|
F [Если токен отсутствует, выполнение запроса аутентификации]
|
G [Получение и сохранение токена]
|
H [Форматирование сообщений]
|
I [Создание данных запроса (data)]
|
J [Отправка POST-запроса к API]
|
K [Обработка ответа по частям (chunks)]
|
L [Преобразование JSON и извлечение содержимого]
|
M [Генерация содержимого (yield)]
|
N [Если ошибка при обработке JSON, вызов RuntimeError]
```

**Примеры**:

```python
# Пример использования с минимальными параметрами
import asyncio
from typing import AsyncGenerator, List, Dict, Any

from hypotez.src.endpoints.gpt4free.g4f.Provider.deprecated.Berlin import Berlin
from hypotez.src.endpoints.gpt4free.g4f.typing import Messages


async def main():
    messages: Messages = [{"role": "user", "content": "Hello, world!"}]
    generator: AsyncGenerator = Berlin.create_async_generator(model="gpt-3.5-turbo", messages=messages)
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

```python
# Пример использования с прокси и дополнительными параметрами
import asyncio
from typing import AsyncGenerator, List, Dict, Any, Optional

from hypotez.src.endpoints.gpt4free.g4f.Provider.deprecated.Berlin import Berlin
from hypotez.src.endpoints.gpt4free.g4f.typing import Messages


async def main():
    messages: Messages = [{"role": "user", "content": "Как написать Hello World на Python?"}]
    proxy: Optional[str] = "http://your_proxy:8080"  # Замените на ваш прокси
    kwargs: Dict[str, Any] = {"temperature": 0.7, "max_tokens": 200}
    generator: AsyncGenerator = Berlin.create_async_generator(model="gpt-3.5-turbo", messages=messages, proxy=proxy, **kwargs)
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())