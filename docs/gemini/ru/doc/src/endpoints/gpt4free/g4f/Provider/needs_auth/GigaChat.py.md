# Модуль для работы с GigaChat от Sber
======================================

Модуль предоставляет асинхронный интерфейс для взаимодействия с GigaChat API от Sber.
Он поддерживает потоковую передачу данных, аутентификацию и выбор различных моделей GigaChat.

## Обзор

Модуль предназначен для обеспечения асинхронного взаимодействия с API GigaChat от Sber. Он включает в себя поддержку потоковой передачи данных, аутентификации через API-ключ, выбор различных моделей GigaChat и обработку ошибок. Основная цель модуля - предоставить удобный и гибкий интерфейс для интеграции с GigaChat в асинхронных приложениях.

## Подробнее

Модуль предназначен для асинхронного взаимодействия с API GigaChat от Sber, обеспечивая поддержку потоковой передачи данных, аутентификации и выбора различных моделей GigaChat. Он использует aiohttp для выполнения асинхронных запросов и включает обработку ошибок, а также механизм обновления токена доступа.

Модуль выполняет следующие ключевые функции:

1.  Аутентификация: Получение токена доступа с использованием предоставленного API-ключа.
2.  Взаимодействие с API GigaChat: Отправка запросов к API GigaChat для получения ответов на основе предоставленных сообщений.
3.  Потоковая передача данных: Поддержка потоковой передачи данных для получения ответов в реальном времени.
4.  Обработка ошибок: Обработка ошибок, связанных с аутентификацией и запросами к API GigaChat.
5.  Выбор модели: Поддержка выбора различных моделей GigaChat для получения ответов.

Модуль содержит следующие компоненты:

*   Импорт необходимых библиотек: `os`, `ssl`, `time`, `uuid`, `pathlib`, `json`, `aiohttp`.
*   Глобальные переменные: `access_token`, `token_expires_at`.
*   Строковая константа `RUSSIAN_CA_CERT` содержащая сертификат.
*   Класс `GigaChat`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.
*   Метод `create_async_generator`, который создает асинхронный генератор для взаимодействия с API GigaChat.

## Классы

### `GigaChat`

**Описание**: Класс `GigaChat` предоставляет асинхронный интерфейс для взаимодействия с API GigaChat от Sber.

**Наследует**:
*   `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных провайдеров, использующих генераторы.
*   `ProviderModelMixin`: Предоставляет функциональность для работы с моделями, поддерживаемыми провайдером.

**Атрибуты**:
*   `url` (str): URL для доступа к API GigaChat (`https://developers.sber.ru/gigachat`).
*   `working` (bool): Указывает, работает ли провайдер (в данном случае `True`).
*   `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
*   `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`True`).
*   `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
*   `needs_auth` (bool): Указывает, требуется ли аутентификация для работы с провайдером (`True`).
*   `default_model` (str): Модель, используемая по умолчанию (`GigaChat:latest`).
*   `models` (list): Список поддерживаемых моделей (`[default_model, "GigaChat-Plus", "GigaChat-Pro"]`).

**Методы**:
*   `create_async_generator`: Создает асинхронный генератор для взаимодействия с API GigaChat.

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
        model (str): Модель GigaChat для использования.
        messages (Messages): Список сообщений для отправки в GigaChat.
        stream (bool): Указывает, использовать ли потоковую передачу данных. По умолчанию `True`.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        connector (BaseConnector, optional): Кастомный коннектор для aiohttp. По умолчанию `None`.
        scope (str, optional): Область доступа для API-ключа. По умолчанию `"GIGACHAT_API_PERS"`.
        update_interval (float, optional): Интервал обновления. По умолчанию `0`.
        **kwargs: Дополнительные параметры для передачи в API GigaChat.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API GigaChat.

    Raises:
        MissingAuthError: Если отсутствует API-ключ.
        Exception: Если возникает ошибка при выполнении запроса к API GigaChat.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API GigaChat.

**Параметры**:
*   `cls`: Ссылка на класс `GigaChat`.
*   `model` (str): Модель GigaChat для использования.
*   `messages` (Messages): Список сообщений для отправки в GigaChat.
*   `stream` (bool): Указывает, использовать ли потоковую передачу данных. По умолчанию `True`.
*   `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
*   `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
*   `connector` (`BaseConnector`, optional): Кастомный коннектор для `aiohttp`. По умолчанию `None`.
*   `scope` (str, optional): Область доступа для API-ключа. По умолчанию `"GIGACHAT_API_PERS"`.
*   `update_interval` (float, optional): Интервал обновления. По умолчанию `0`.
*   `**kwargs`: Дополнительные параметры для передачи в API GigaChat.

**Возвращает**:
*   `AsyncResult`: Асинхронный генератор, возвращающий ответы от API GigaChat.

**Вызывает исключения**:
*   `MissingAuthError`: Если отсутствует API-ключ.

**Внутренние функции**: Нет.

**Как работает функция**:

1.  Проверяет наличие API-ключа. Если ключ отсутствует, вызывает исключение `MissingAuthError`.
2.  Определяет путь к файлу сертификата в директории cookies.
3.  Записывает содержимое сертификата в файл, если он не существует.
4.  Создает SSL-контекст, если включен SSL и не предоставлен коннектор.
5.  Использует `ClientSession` для выполнения асинхронных запросов.
6.  Проверяет, нужно ли обновить токен доступа. Если токен истек или скоро истечет, отправляет запрос на обновление токена.
7.  Отправляет запрос к API GigaChat с использованием полученного токена доступа.
8.  Обрабатывает ответы от API GigaChat в потоковом режиме, если `stream` установлен в `True`.
9.  Возвращает асинхронный генератор, который выдает ответы от API GigaChat.

**ASCII Flowchart**:

```
A: Проверка наличия API-ключа
|
B: Определение пути к файлу сертификата
|
C: Запись сертификата в файл (если не существует)
|
D: Создание SSL-контекста (если необходимо)
|
E: Создание ClientSession
|
F: Проверка необходимости обновления токена
|
G: Запрос на обновление токена (если необходимо)
|
H: Запрос к API GigaChat
|
I: Обработка потоковых ответов
|
J: Возврат асинхронного генератора
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from src.logger import logger  # Предполагается, что logger находится в src.logger

async def main():
    api_key = "YOUR_API_KEY"
    messages = [{"role": "user", "content": "Hello, GigaChat!"}]

    try:
        generator = await GigaChat.create_async_generator(
            model="GigaChat:latest",
            messages=messages,
            api_key=api_key
        )

        async for message in generator:
            print(message, end="")
    except Exception as ex:
        logger.error('Error while processing data', ex, exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())