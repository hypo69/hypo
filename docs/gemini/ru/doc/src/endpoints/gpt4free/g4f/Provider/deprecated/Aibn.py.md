# Модуль для работы с провайдером Aibn
=========================================

Модуль содержит класс `Aibn`, который является асинхронным генераторным провайдером.
Этот класс используется для взаимодействия с сервисом Aibn через его API для генерации текста.
Он поддерживает историю сообщений и модель GPT-3.5 Turbo.

## Обзор

Модуль `Aibn` предоставляет возможность асинхронного взаимодействия с API сервиса Aibn для генерации текста на основе предоставленных сообщений. Он использует асинхронные запросы для обеспечения неблокирующего ввода-вывода и поддерживает прокси для обхода ограничений сети.

## Подробней

Модуль предназначен для использования в асинхронных приложениях, где требуется генерация текста с использованием модели GPT-3.5 Turbo через API сервиса Aibn. Он обеспечивает возможность передачи истории сообщений для контекстной генерации текста и поддерживает использование прокси для обхода сетевых ограничений.

## Классы

### `Aibn`

**Описание**: Класс `Aibn` является асинхронным генераторным провайдером.

**Принцип работы**:
1.  Устанавливает URL сервиса Aibn.
2.  Указывает, что провайдер поддерживает историю сообщений и модель GPT-3.5 Turbo.
3.  Реализует метод `create_async_generator` для асинхронной генерации текста.

**Аттрибуты**:
-   `url` (str): URL сервиса Aibn (`https://aibn.cc`).
-   `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
-   `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
-   `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель GPT-3.5 Turbo (`True`).

**Методы**:
-   `create_async_generator`: Асинхронно генерирует текст на основе предоставленных сообщений.

#### `create_async_generator`

```python
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 120,
        **kwargs
    ) -> AsyncResult:
        """ Асинхронно генерирует текст на основе предоставленных сообщений, используя API сервиса Aibn.
        Args:
            cls (Aibn): Ссылка на класс `Aibn`.
            model (str): Имя модели для генерации текста.
            messages (Messages): Список сообщений для передачи в API.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            timeout (int, optional): Время ожидания ответа от сервера в секундах. По умолчанию `120`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор текста.

        Raises:
            Exception: Если возникает ошибка при запросе к API.

        """
```

**Назначение**: Асинхронно генерирует текст на основе предоставленных сообщений, используя API сервиса Aibn.

**Параметры**:

*   `cls` (`Aibn`): Ссылка на класс `Aibn`.
*   `model` (`str`): Имя модели для генерации текста.
*   `messages` (`Messages`): Список сообщений для передачи в API.
*   `proxy` (`str`, optional): URL прокси-сервера. По умолчанию `None`.
*   `timeout` (`int`, optional): Время ожидания ответа от сервера в секундах. По умолчанию `120`.
*   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

*   `AsyncResult`: Асинхронный генератор текста.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при запросе к API.

**Как работает функция**:

1.  Функция принимает параметры, необходимые для генерации текста, такие как модель, сообщения, прокси и время ожидания.
2.  Инициализирует асинхронную сессию с использованием `StreamSession` для выполнения запросов.
3.  Формирует данные для отправки в API, включая сообщения, подпись и временную метку.
4.  Выполняет POST-запрос к API сервиса Aibn.
5.  Получает ответ от сервера и итерируется по его содержимому, декодируя каждый чанк и передавая его в генератор.

```
create_async_generator
│
├───► Инициализация асинхронной сессии (StreamSession)
│
├───► Формирование данных для API (messages, sign, time)
│
├───► POST-запрос к API сервиса Aibn
│
└───► Итерация по чанкам ответа и передача в генератор
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

from g4f.Provider.deprecated.Aibn import Aibn
from g4f.typing import Messages


async def main():
    model: str = "gpt_35_turbo"  # str #Example: "gpt_35_turbo"
    messages: Messages = [{"role": "user", "content": "Hello"}]  # List[Dict[str, str]] #Example: [{"role": "user", "content": "Hello"}]
    proxy: Optional[str] = None  # Optional[str] #Example: None
    timeout: int = 120  # int #Example: 120
    generator: AsyncGenerator = await Aibn.create_async_generator(model=model, messages=messages, proxy=proxy, timeout=timeout)
    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `generate_signature`

```python
def generate_signature(timestamp: int, message: str, secret: str = "undefined") -> str:
    """ Генерирует подпись для запроса к API сервиса Aibn.

    Args:
        timestamp (int): Временная метка запроса.
        message (str): Сообщение для подписи.
        secret (str, optional): Секретный ключ. По умолчанию "undefined".

    Returns:
        str: Подпись запроса в формате SHA256.

    """
```

**Назначение**: Генерирует подпись для запроса к API сервиса Aibn.

**Параметры**:

*   `timestamp` (`int`): Временная метка запроса.
*   `message` (`str`): Сообщение для подписи.
*   `secret` (`str`, optional): Секретный ключ. По умолчанию `"undefined"`.

**Возвращает**:

*   `str`: Подпись запроса в формате SHA256.

**Как работает функция**:

1.  Функция принимает временную метку, сообщение и секретный ключ.
2.  Формирует строку данных для подписи, объединяя временную метку, сообщение и секретный ключ.
3.  Вычисляет SHA256-хеш от полученной строки данных.
4.  Возвращает полученный хеш в шестнадцатеричном формате.

```
generate_signature
│
├───► Формирование строки данных для подписи (timestamp:message:secret)
│
├───► Вычисление SHA256-хеша от строки данных
│
└───► Возврат хеша в шестнадцатеричном формате
```

**Примеры**:

```python
# Пример использования generate_signature
from g4f.Provider.deprecated.Aibn import generate_signature

timestamp = 1678886400  # int #Example: 1678886400
message = "Hello"  # str #Example: "Hello"
secret = "undefined"  # str #Example: "undefined"
signature = generate_signature(timestamp, message, secret)
print(signature)
# Вывод:
# 'e5a8e5b1c0b8b3b9c1b1c0b8b3b9c1b1c0b8b3b9c1b1c0b8b3b9c1b1c0b8b3b9'