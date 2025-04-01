# Модуль WhiteRabbitNeo

## Обзор

Модуль `WhiteRabbitNeo` предоставляет асинхронный генератор для взаимодействия с провайдером WhiteRabbitNeo. Он поддерживает историю сообщений и требует аутентификации. Модуль предназначен для использования в асинхронных приложениях, где необходимо получать ответы от модели WhiteRabbitNeo в режиме реального времени, обрабатывая ответы по частям (chunks).

## Подробней

Модуль `WhiteRabbitNeo` является частью системы, взаимодействующей с различными провайдерами, предоставляющими доступ к языковым моделям. Он использует асинхронный подход для эффективной обработки запросов и предназначен для интеграции в систему `hypotez`.  Для отправки запросов используется библиотека `aiohttp`

## Классы

### `WhiteRabbitNeo`

**Описание**: Класс `WhiteRabbitNeo` является асинхронным провайдером, взаимодействующим с сервисом WhiteRabbitNeo.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора.

**Атрибуты**:
- `url` (str): URL сервиса WhiteRabbitNeo (`https://www.whiterabbitneo.com`).
- `working` (bool): Флаг, указывающий на работоспособность провайдера (по умолчанию `True`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (по умолчанию `True`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (по умолчанию `True`).

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от сервиса WhiteRabbitNeo.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    cookies: Cookies = None,
    connector: BaseConnector = None,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от сервиса WhiteRabbitNeo.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        connector (BaseConnector, optional): Кастомный коннектор для aiohttp. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий чанки данных ответа.

    Raises:
        Exception: Если возникает ошибка при отправке запроса или обработке ответа.

    """
```

**Назначение**:
Функция `create_async_generator` создает и возвращает асинхронный генератор, который отправляет сообщения в WhiteRabbitNeo и выдает чанки ответа.

**Параметры**:
- `cls`: Ссылка на класс `WhiteRabbitNeo`.
- `model` (str): Модель, используемая для генерации ответов.
- `messages` (Messages): Список сообщений, отправляемых в запросе.
- `cookies` (Cookies, optional): Cookies для аутентификации. Если не предоставлены, используются cookies, полученные из домена "www.whiterabbitneo.com". По умолчанию `None`.
- `connector` (BaseConnector, optional): Кастомный коннектор для `aiohttp.ClientSession`. По умолчанию `None`.
- `proxy` (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает части (chunks) данных ответа.

**Вызывает исключения**:
- `Exception`: Может возникнуть, если произойдет ошибка во время выполнения запроса или обработки ответа.

**Как работает функция**:

1. **Инициализация**:
   - Если `cookies` не предоставлены, функция пытается получить их, используя `get_cookies("www.whiterabbitneo.com")`.

2. **Формирование заголовков**:
   - Создаются заголовки HTTP-запроса, включая `User-Agent`, `Accept`, `Accept-Language`, `Referer`, `Content-Type`, `Origin` и `Connection`.

3. **Создание асинхронной сессии**:
   - Используется `aiohttp.ClientSession` для выполнения запроса. Сессия настраивается с заголовками, cookies и коннектором (если предоставлен).

4. **Формирование данных запроса**:
   - Данные запроса формируются в виде словаря, содержащего `messages`, случайный `id`, флаги `enhancePrompt` и `useFunctions`.

5. **Отправка POST-запроса**:
   - Отправляется POST-запрос на URL `f"{cls.url}/api/chat"`.

6. **Обработка ответа**:
   - Вызывается `raise_for_status(response)` для проверки статуса ответа.
   - Функция итерируется по чанкам ответа, используя `response.content.iter_any()`, и декодирует каждый чанк в строку, используя `chunk.decode(errors="ignore")`.

7. **Генерация чанков**:
   - Каждый декодированный чанк выдается как часть асинхронного генератора.

```
                                  Начало
                                    ↓
                    Если cookies не предоставлены
                       ↓                           ↘ Да
        Получение cookies через get_cookies()     Cookies = None
                       ↓                           ↙ Нет
              Формирование заголовков HTTP
                       ↓
           Создание асинхронной сессии (ClientSession)
                       ↓
            Формирование данных запроса (JSON)
                       ↓
               Отправка POST-запроса на API
                       ↓
           Проверка статуса ответа (raise_for_status)
                       ↓
      Итерация по чанкам ответа (response.content.iter_any())
                       ↓
           Декодирование каждого чанка (decode)
                       ↓
           Выдача чанка через асинхронный генератор
                       ↓
                                  Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator

from aiohttp import BaseConnector

# Предположим, что у вас есть функция get_cookies и класс WhiteRabbitNeo
# from . import WhiteRabbitNeo  # Укажите правильный путь к WhiteRabbitNeo
# from ..helper import get_cookies

async def main():
    model = "default"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, WhiteRabbitNeo!"}]
    cookies = {"session_id": "12345"}
    proxy = "http://your_proxy:8080"
    connector: BaseConnector = None  # Замените на ваш коннектор, если необходимо

    async def consume_generator(generator: AsyncGenerator[str, None]) -> None:
        async for chunk in generator:
            print(chunk, end="")

    generator = WhiteRabbitNeo.create_async_generator(
        model=model,
        messages=messages,
        cookies=cookies,
        proxy=proxy,
        connector=connector
    )
    
    await consume_generator(await generator)

if __name__ == "__main__":
    asyncio.run(main())