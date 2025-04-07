# Модуль для работы с GigaChat API
=====================================

Модуль содержит класс `GigaChat`, который используется для взаимодействия с API GigaChat от Sber. Он поддерживает асинхронные запросы, потоковую передачу данных и аутентификацию через API key.

## Обзор

Модуль предназначен для обеспечения возможности взаимодействия с GigaChat API для получения ответов на основе предоставленных сообщений. Он включает в себя поддержку потоковой передачи данных, аутентификации и обработки ошибок.

## Подробнее

Модуль `GigaChat.py` предоставляет асинхронный интерфейс для работы с API GigaChat. Он использует `aiohttp` для выполнения HTTP-запросов и обеспечивает поддержку потоковой передачи данных. Для аутентификации требуется API key, который используется для получения access token. Модуль также обрабатывает создание и использование SSL-сертификатов для безопасного подключения к API.

## Классы

### `GigaChat`

**Описание**: Класс `GigaChat` является асинхронным генератором и предоставляет методы для взаимодействия с API GigaChat. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL для доступа к API GigaChat ("https://developers.sber.ru/gigachat").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `default_model` (str): Модель, используемая по умолчанию ("GigaChat:latest").
- `models` (List[str]): Список поддерживаемых моделей ([default_model, "GigaChat-Plus", "GigaChat-Pro"]).

**Методы**:

- `create_async_generator`: Асинхронный генератор для получения ответов от API GigaChat.

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
    Асинхронный генератор для получения ответов от API GigaChat.

    Args:
        cls (type): Класс, для которого вызывается метод.
        model (str): Используемая модель.
        messages (Messages): Список сообщений для отправки.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию True.
        proxy (str): URL прокси-сервера. По умолчанию None.
        api_key (str): API ключ для аутентификации. По умолчанию None.
        connector (BaseConnector): Кастомный коннектор для aiohttp. По умолчанию None.
        scope (str): Область действия для получения access token. По умолчанию "GIGACHAT_API_PERS".
        update_interval (float): Интервал обновления. По умолчанию 0.
        **kwargs: Дополнительные параметры для передачи в API.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        MissingAuthError: Если отсутствует API ключ.
    """
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API GigaChat. Она получает access token, если он устарел, и отправляет запрос к API с предоставленными сообщениями и параметрами.

**Как работает функция**:

1. **Инициализация**:
   - Получает глобальные переменные `access_token` и `token_expires_at`.
   - Извлекает модель из входных параметров, используя `cls.get_model(model)`.
   - Проверяет наличие `api_key`. Если он отсутствует, вызывает исключение `MissingAuthError`.
   - Определяет путь к файлу сертификата `russian_trusted_root_ca.crt` в каталоге cookies.
   - Если файл сертификата не существует, записывает в него содержимое `RUSSIAN_CA_CERT`.
   - Если `has_ssl` и `connector` не предоставлены, создает SSL context и TCP connector.

2. **Получение Access Token**:
   - Проверяет, истек ли срок действия текущего `access_token`. Если срок истек или истекает в ближайшие 60 секунд:
     - Отправляет POST-запрос на URL `https://ngw.devices.sberbank.ru:9443/api/v2/oauth` для получения нового `access_token`.
     - Включает в запрос заголовок `Authorization` с API key, `RqUID` (случайный UUID) и `Content-Type`.
     - Передает область действия (`scope`) в теле запроса.
     - Обрабатывает ответ, извлекая `access_token` и время его истечения (`expires_at`).

3. **Отправка Запроса к API GigaChat**:
   - Отправляет POST-запрос на URL `https://gigachat.devices.sberbank.ru/api/v1/chat/completions` с использованием полученного `access_token`.
   - Включает в запрос заголовок `Authorization` с `access_token`.
   - Формирует JSON-тело запроса, включающее модель, сообщения, флаг потоковой передачи (`stream`), интервал обновления и дополнительные параметры.

4. **Обработка Потоковой Передачи Данных**:
   - Если `stream` установлен в `True`:
     - Итерирует по каждой строке в ответе от API.
     - Если строка начинается с `data:`, удаляет префикс `data: ` и суффикс `\n`.
     - Если строка содержит `[DONE]`, завершает генератор.
     - Иначе десериализует JSON-строку и извлекает содержимое сообщения (`content`) из поля `delta`.
     - Возвращает из генератора полученное содержимое.
     - Если в сообщении присутствует поле `finish_reason`, завершает генератор.
   - Если `stream` установлен в `False`:
     - Читает все строки ответа, декодирует их как UTF-8 и загружает как JSON.
     - Извлекает содержимое сообщения из поля `choices[0].message.content`.
     - Возвращает содержимое и завершает функцию.

**Внутренние функции**:
Внутри данной функции нет внутренних функций

**ASCII схема работы функции**:

```
    Начало
      ↓
    Проверка API ключа
      ↓
    Создание SSL Context (если необходимо)
      ↓
    Проверка срока действия access_token
      ↓
    Получение нового access_token (если необходимо)
      ↓
    Отправка POST запроса к API GigaChat
      ↓
    Обработка ответа (потоковая или полная)
      ↓
    Извлечение и возврат содержимого сообщения
      ↓
    Завершение
```

**Примеры**:

```python
# Пример использования с потоковой передачей данных
async for message in GigaChat.create_async_generator(model="GigaChat:latest", messages=[{"role": "user", "content": "Hello, GigaChat!"}], api_key="your_api_key"):
    print(message)

# Пример использования без потоковой передачи данных
message = await GigaChat.create_async_generator(model="GigaChat:latest", messages=[{"role": "user", "content": "Hello, GigaChat!"}], stream=False, api_key="your_api_key")
print(message)
```

```python
# Пример обработки ошибки MissingAuthError
try:
    async for message in GigaChat.create_async_generator(model="GigaChat:latest", messages=[{"role": "user", "content": "Hello, GigaChat!"}]):
        print(message)
except MissingAuthError as ex:
    print(f"Ошибка аутентификации: {ex}")