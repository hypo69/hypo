# Модуль `GigaChat.py`

## Обзор

Модуль предназначен для взаимодействия с GigaChat API от Сбербанка для генерации текста на основе предоставленных сообщений. Он поддерживает потоковую передачу данных, использование системных сообщений, а также требует аутентификации.

## Подробнее

Этот модуль предоставляет асинхронный генератор для получения ответов от GigaChat API. Он использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов. Для работы с GigaChat API требуется API-ключ, который используется для получения токена доступа. Модуль также поддерживает использование прокси-серверов и SSL для безопасного соединения.

В модуле реализована автоматическая перезагрузка токена доступа, если срок его действия истекает. Кроме того, модуль предоставляет возможность работы с доверенным сертификатом для установки безопасного соединения с серверами Сбербанка.

## Классы

### `GigaChat`

**Описание**: Класс `GigaChat` предоставляет функциональность для взаимодействия с API GigaChat от Сбербанка. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin` и предназначен для генерации текста на основе предоставленных сообщений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL для доступа к API GigaChat (`https://developers.sber.ru/gigachat`).
- `working` (bool): Флаг, указывающий, работает ли провайдер (всегда `True`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (всегда `True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (всегда `True`).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (всегда `True`).
- `needs_auth` (bool): Флаг, указывающий, требуется ли аутентификация для работы с провайдером (всегда `True`).
- `default_model` (str): Модель, используемая по умолчанию (`GigaChat:latest`).
- `models` (List[str]): Список поддерживаемых моделей (`[default_model, "GigaChat-Plus", "GigaChat-Pro"]`).

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    proxy: str = None,
    api_key: str = None,
    connector: BaseConnector = None,
    scope: str = "GIGACHAT_API_PERS",
    update_interval: float = 0,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API GigaChat.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        connector (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
        scope (str, optional): Область действия для получения токена доступа. По умолчанию `"GIGACHAT_API_PERS"`.
        update_interval (float, optional): Интервал обновления. По умолчанию `0`.
        **kwargs: Дополнительные аргументы для передачи в API.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от API.

    Raises:
        MissingAuthError: Если отсутствует API-ключ.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API GigaChat.

**Параметры**:
- `cls`: Ссылка на класс `GigaChat`.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `connector` (BaseConnector, optional): Aiohttp коннектор. По умолчанию `None`.
- `scope` (str, optional): Область действия для получения токена доступа. По умолчанию `"GIGACHAT_API_PERS"`.
- `update_interval` (float, optional): Интервал обновления. По умолчанию `0`.
- `**kwargs`: Дополнительные аргументы для передачи в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует API-ключ.

**Как работает функция**:

1. **Проверка наличия API-ключа**:
   - Проверяется, передан ли `api_key`. Если он отсутствует, вызывается исключение `MissingAuthError`.
2. **Создание файла сертификата**:
   - Определяется путь к каталогу для хранения cookie-файлов.
   - Формируется путь к файлу сертификата `russian_trusted_root_ca.crt`.
   - Если файл сертификата не существует, он создается и в него записывается содержимое `RUSSIAN_CA_CERT`.
3. **Создание SSL-контекста**:
   - Если `has_ssl` равно `True` и `connector` не передан, создается SSL-контекст с использованием файла сертификата.
   - Создается `TCPConnector` с использованием созданного SSL-контекста.
4. **Создание сессии aiohttp**:
   - Создается асинхронная сессия `ClientSession` с использованием `connector` (с прокси, если указан).
5. **Обновление токена доступа**:
   - Проверяется, истек ли срок действия текущего токена доступа (`access_token`). Если до истечения осталось менее 60 секунд, выполняется запрос на обновление токена.
   - Отправляется POST-запрос к `https://ngw.devices.sberbank.ru:9443/api/v2/oauth` с использованием API-ключа для получения нового токена доступа.
   - Полученный токен доступа и время его истечения сохраняются в глобальных переменных `access_token` и `token_expires_at`.
6. **Отправка запроса к GigaChat API**:
   - Отправляется POST-запрос к `https://gigachat.devices.sberbank.ru/api/v1/chat/completions` с использованием полученного токена доступа.
   - В теле запроса передаются параметры: модель, сообщения, флаг потоковой передачи данных и дополнительные аргументы.
7. **Обработка потоковых данных**:
   - Если `stream` равен `True`, функция асинхронно итерируется по строкам в ответе.
   - Каждая строка проверяется на наличие префикса `data:`. Если префикс присутствует, строка декодируется и извлекается содержимое сообщения.
   - Если строка содержит `[DONE]`, функция завершает работу.
   - Извлеченное содержимое сообщения передается через `yield`.
8. **Обработка не потоковых данных**:
   - Если `stream` равен `False`, функция ожидает получения всего ответа, декодирует его и извлекает содержимое сообщения.
   - Извлеченное содержимое сообщения передается через `yield`.

**Внутренние функции**: Нет

**Примеры**:

Пример использования с потоковой передачей данных:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.needs_auth.GigaChat import GigaChat

async def main():
    api_key = "<api_key>"  # <инструкция для модели gemini: укажите свой api_key>
    messages = [{"role": "user", "content": "Напиши короткий стих о Москве"}]
    generator = await GigaChat.create_async_generator(model="GigaChat:latest", messages=messages, api_key=api_key)
    async for message in generator:
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

Пример использования без потоковой передачи данных:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.needs_auth.GigaChat import GigaChat

async def main():
    api_key = "<api_key>"  # <инструкция для модели gemini: укажите свой api_key>
    messages = [{"role": "user", "content": "Напиши короткий стих о Москве"}]
    generator = await GigaChat.create_async_generator(model="GigaChat:latest", messages=messages, api_key=api_key, stream=False)
    async for message in generator:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
```

```ascii
A: Проверка наличия API-ключа
|
B: Создание файла сертификата, если он не существует
|
C: Создание SSL-контекста и TCPConnector
|
D: Создание сессии aiohttp
|
E: Проверка срока действия токена
|  No: Отправка запроса к GigaChat API
|  |
|  F: Получение нового токена доступа
|  |
|  Yes: Отправка запроса к GigaChat API
|
G: Обработка потоковых данных или получение всего ответа
|
H: Извлечение содержимого сообщения и передача через yield
|
I: Завершение работы