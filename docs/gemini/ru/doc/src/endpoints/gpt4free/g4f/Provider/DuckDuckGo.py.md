# Модуль DuckDuckGo

## Обзор

Модуль `DuckDuckGo.py` предоставляет асинхронный интерфейс для взаимодействия с чат-ботом DuckDuckGo AI через библиотеку `duckduckgo_search`. Он позволяет генерировать ответы на основе предоставленных сообщений, используя различные модели, поддерживаемые DuckDuckGo. Модуль также включает механизм аутентификации через `nodriver` для получения необходимых заголовков для API запросов.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими доступа к возможностям чат-бота DuckDuckGo AI. Он обеспечивает асинхронную генерацию ответов, что позволяет эффективно использовать ресурсы и обрабатывать запросы параллельно.

## Классы

### `DuckDuckGo`

**Описание**: Класс `DuckDuckGo` является асинхронным провайдером, который использует API DuckDuckGo для генерации ответов на основе предоставленных сообщений.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных провайдеров генерации.
- `ProviderModelMixin`: Предоставляет утилиты для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера (отображаемое имя) - `"Duck.ai (duckduckgo_search)"`.
- `url` (str): URL чат-бота DuckDuckGo - `"https://duckduckgo.com/aichat"`.
- `api_base` (str): Базовый URL API DuckDuckGo - `"https://duckduckgo.com/duckchat/v1/"`.
- `working` (bool): Указывает, работает ли провайдер в данный момент (по умолчанию `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу ответов (по умолчанию `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (по умолчанию `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (по умолчанию `True`).
- `default_model` (str): Модель, используемая по умолчанию - `"gpt-4o-mini"`.
- `models` (List[str]): Список поддерживаемых моделей.
- `ddgs` (DDGS): Инстанс класса `DDGS` из библиотеки `duckduckgo_search` (инициализируется при первом использовании).
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от DuckDuckGo AI.
- `nodriver_auth`: Аутентифицируется с использованием `nodriver` для получения необходимых заголовков для API запросов.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 60,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от DuckDuckGo AI.

    Args:
        cls (DuckDuckGo): Класс DuckDuckGo.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для передачи в чат-бот.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию 60.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа от DuckDuckGo AI.

    Raises:
        ImportError: Если не установлена библиотека `duckduckgo_search`.
    """
```

**Назначение**:
Создает асинхронный генератор для получения ответов от DuckDuckGo AI. Эта функция отвечает за подготовку и отправку запроса в DuckDuckGo AI, а также за обработку потока ответов.

**Параметры**:
- `cls` (DuckDuckGo): Класс DuckDuckGo.
- `model` (str): Имя используемой модели.
- `messages (Messages)`: Список сообщений для передачи в чат-бот.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию 60.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа от DuckDuckGo AI.

**Вызывает исключения**:
- `ImportError`: Если не установлена библиотека `duckduckgo_search`.

**Как работает функция**:
1. **Проверка зависимостей**:
   - Проверяет, установлена ли библиотека `duckduckgo_search`. Если нет, вызывает исключение `ImportError`.
2. **Инициализация DDGS**:
   - Если `cls.ddgs` еще не инициализирован, создает экземпляр `DDGS` с использованием предоставленных параметров `proxy` и `timeout`.
   - Если `has_nodriver` равен `True`, вызывает функцию `cls.nodriver_auth` для аутентификации через `nodriver`.
3. **Получение модели**:
   - Вызывает `cls.get_model(model)` для получения имени модели.
4. **Генерация ответа**:
   - Вызывает `cls.ddgs.chat_yield` для получения асинхронного генератора, возвращающего части ответа от DuckDuckGo AI.
   - Передает в `cls.ddgs.chat_yield` последнее сообщение пользователя из списка сообщений, имя модели и время ожидания.
5. **Возврат генератора**:
   - Возвращает асинхронный генератор, который можно использовать для получения частей ответа.

```
A: Проверка зависимостей и инициализация
|
-- B: Аутентификация через nodriver (если необходимо)
|
C: Получение модели
|
D: Генерация ответа через ddgs.chat_yield
|
E: Возврат асинхронного генератора
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator, Optional

from src.endpoints.gpt4free.g4f.typing import Messages
from src.endpoints.gpt4free.g4f.Provider.DuckDuckGo import DuckDuckGo

async def main():
    model: str = "gpt-4o-mini"
    messages: Messages = [{"role": "user", "content": "Привет, как дела?"}]
    proxy: Optional[str] = None
    timeout: int = 60

    generator: AsyncGenerator = await DuckDuckGo.create_async_generator(
        model=model, messages=messages, proxy=proxy, timeout=timeout
    )

    async for chunk in generator:
        print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

### `nodriver_auth`

```python
    @classmethod
    async def nodriver_auth(cls, proxy: str = None):
        """Аутентифицируется с использованием `nodriver` для получения необходимых заголовков для API запросов.

        Args:
            cls (DuckDuckGo): Класс DuckDuckGo.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        """
```

**Назначение**:
Аутентифицируется с использованием `nodriver` для получения необходимых заголовков (`X-Vqd-4`, `X-Vqd-Hash-1`, `F-Fe-Version`) для API запросов к DuckDuckGo.

**Параметры**:
- `cls` (DuckDuckGo): Класс DuckDuckGo.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.

**Как работает функция**:
1. **Запуск браузера `nodriver`**:
   - Запускает браузер с использованием `get_nodriver` с переданным `proxy`. Функция возвращает объект браузера и функцию остановки браузера (`stop_browser`).
2. **Обработка запросов**:
   - Определяет функцию `on_request`, которая будет вызываться при каждом запросе, отправленном браузером.
   - Внутри `on_request` проверяется, содержит ли URL запроса `cls.api_base`. Если да, то извлекаются заголовки `X-Vqd-4`, `X-Vqd-Hash-1` и `F-Fe-Version` из заголовков запроса и сохраняются в атрибутах `cls.ddgs._chat_vqd`, `cls.ddgs._chat_vqd_hash` и `cls.ddgs._chat_xfe` соответственно.
3. **Подключение обработчика запросов**:
   - Включает перехват сетевых запросов с помощью `page.send(nodriver.cdp.network.enable())`.
   - Добавляет обработчик `on_request` для события `nodriver.cdp.network.RequestWillBeSent`.
4. **Переход на страницу**:
   - Открывает страницу `cls.url` в браузере с использованием `browser.get(cls.url)`.
5. **Ожидание аутентификации**:
   - Ожидает, пока не будет установлен атрибут `cls.ddgs._chat_vqd`. Это означает, что необходимые заголовки были получены.
6. **Закрытие страницы**:
   - Закрывает текущую страницу с помощью `page.close()`.
7. **Остановка браузера**:
   - В блоке `finally` вызывается функция `stop_browser()` для остановки браузера, независимо от того, произошла ли ошибка или нет.

```
A: Запуск браузера nodriver
|
-- B: Определение функции on_request для перехвата заголовков
|
C: Подключение обработчика запросов
|
D: Переход на страницу cls.url
|
E: Ожидание аутентификации (получения заголовков)
|
F: Закрытие страницы
|
G: Остановка браузера (finally)
```

**Примеры**:

```python
# Пример использования nodriver_auth
import asyncio
from src.endpoints.gpt4free.g4f.Provider.DuckDuckGo import DuckDuckGo

async def main():
    proxy: str = None  # Замените на ваш прокси, если необходимо

    await DuckDuckGo.nodriver_auth(proxy=proxy)

    print(f"Чат VQD: {DuckDuckGo.ddgs._chat_vqd}")
    print(f"Чат VQD Hash: {DuckDuckGo.ddgs._chat_vqd_hash}")
    print(f"Чат XFE: {DuckDuckGo.ddgs._chat_xfe}")

if __name__ == "__main__":
    asyncio.run(main())