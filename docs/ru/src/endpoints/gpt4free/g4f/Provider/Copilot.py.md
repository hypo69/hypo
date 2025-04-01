# Модуль для взаимодействия с Microsoft Copilot

## Обзор

Модуль `Copilot.py` предоставляет класс `Copilot` для взаимодействия с Microsoft Copilot API. Он поддерживает отправку текстовых сообщений и изображений, а также получение ответов в реальном времени через WebSocket.

## Подробнее

Этот модуль позволяет использовать Microsoft Copilot для генерации текста и изображений. Он включает в себя механизмы для аутентификации, создания и управления беседами, а также обработки медиа-вложений. В модуле реализована поддержка как потоковой передачи ответов, так и получения полных ответов.

## Классы

### `Conversation`

**Описание**: Класс для представления беседы с Copilot.

**Атрибуты**:
- `conversation_id` (str): Идентификатор беседы.

### `Copilot`

**Описание**: Класс для взаимодействия с Microsoft Copilot API.

**Наследует**:
- `AbstractProvider`: Предоставляет базовую функциональность для взаимодействия с API.
- `ProviderModelMixin`: Реализует общую логику для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Microsoft Copilot").
- `url` (str): URL Copilot ("https://copilot.microsoft.com").
- `working` (bool): Индикатор работоспособности провайдера (True).
- `supports_stream` (bool): Поддержка потоковой передачи (True).
- `default_model` (str): Модель по умолчанию ("Copilot").
- `models` (List[str]): Список поддерживаемых моделей (["Copilot", "Think Deeper"]).
- `model_aliases` (Dict[str, str]): Псевдонимы моделей.
- `websocket_url` (str): URL WebSocket API ("wss://copilot.microsoft.com/c/api/chat?api-version=2").
- `conversation_url` (str): URL для управления беседами ("https://copilot.microsoft.com/c/api/conversations").
- `_access_token` (str): Токен доступа.
- `_cookies` (dict): Куки для аутентификации.

**Методы**:
- `create_completion`: Создает запрос на завершение.

## Функции

### `create_completion`

```python
@classmethod
def create_completion(
    cls,
    model: str,
    messages: Messages,
    stream: bool = False,
    proxy: str = None,
    timeout: int = 900,
    prompt: str = None,
    media: MediaListType = None,
    conversation: BaseConversation = None,
    return_conversation: bool = False,
    api_key: str = None,
    **kwargs
) -> CreateResult:
    """
    Создает запрос на завершение и возвращает результат.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Включить потоковую передачу. По умолчанию `False`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `900`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
        conversation (BaseConversation, optional): Объект беседы. По умолчанию `None`.
        return_conversation (bool, optional): Вернуть объект беседы. По умолчанию `False`.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        CreateResult: Результат завершения.

    Raises:
        MissingRequirementsError: Если не установлен пакет `curl_cffi`.
        NoValidHarFileError: Если не найден валидный HAR-файл.
        MissingAuthError: Если не удалось получить токен доступа.

    """
```

**Назначение**: Создает запрос на завершение беседы с Copilot, отправляет сообщения и медиафайлы, обрабатывает ответы в реальном времени или возвращает результат целиком.

**Параметры**:
- `cls`: Ссылка на класс `Copilot`.
- `model` (str): Название модели для использования (например, "Copilot" или "Think Deeper").
- `messages` (Messages): Список сообщений для отправки в Copilot.
- `stream` (bool, optional): Флаг, указывающий, следует ли использовать потоковую передачу ответов. По умолчанию `False`.
- `proxy` (str, optional): URL прокси-сервера для использования при подключении к Copilot. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа от Copilot в секундах. По умолчанию `900`.
- `prompt` (str, optional): Текст запроса, если он не содержится в `messages`. По умолчанию `None`.
- `media` (MediaListType, optional): Список медиафайлов (изображений) для отправки в Copilot. По умолчанию `None`.
- `conversation` (BaseConversation, optional): Объект беседы для продолжения существующей беседы. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, следует ли возвращать объект беседы. По умолчанию `False`.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в Copilot API.

**Возвращает**:
- `CreateResult`: Генератор, возвращающий части ответа, объекты `ImageResponse`, `FinishReason` или `SuggestedFollowups`.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлен пакет `curl_cffi`.
- `NoValidHarFileError`: Если не найден валидный HAR-файл.
- `MissingAuthError`: Если не удалось получить токен доступа.
- `RuntimeError`: При получении сообщения об ошибке от Copilot.

**Как работает функция**:

1. **Проверка зависимостей**:
   - Проверяет, установлен ли пакет `curl_cffi`. Если нет, вызывает исключение `MissingRequirementsError`.

2. **Получение модели**:
   - Получает название модели из аргумента `model` с использованием `cls.get_model(model)`.

3. **Аутентификация**:
   - Проверяет наличие токена доступа `cls._access_token`.
   - Если токен отсутствует, пытается прочитать его из HAR-файла с помощью `readHAR(cls.url)`.
   - Если HAR-файл не найден или не содержит токен, пытается получить его с помощью `get_access_token_and_cookies(cls.url, proxy)` через браузер, используя `nodriver`.

4. **Создание сессии**:
   - Создает сессию с использованием `curl_cffi.requests.Session` с заданными параметрами (таймаут, прокси, заголовки, куки).

5. **Получение информации о пользователе**:
   - Отправляет запрос к API для получения информации о пользователе.
   - Если возвращается статус 401, вызывает исключение `MissingAuthError`.

6. **Создание или использование существующей беседы**:
   - Если `conversation` равен `None`, создает новую беседу, отправляя POST-запрос к `cls.conversation_url`.
   - Если `conversation` предоставлен, использует существующую беседу.

7. **Загрузка медиафайлов**:
   - Если в аргументе `media` переданы медиафайлы, загружает их на сервер Copilot и получает URL.

8. **Установка WebSocket-соединения**:
   - Устанавливает WebSocket-соединение с `cls.websocket_url`.

9. **Отправка сообщений**:
   - Отправляет сообщения в формате JSON через WebSocket.

10. **Обработка ответов**:
    - Принимает сообщения через WebSocket и обрабатывает их в цикле.
    - В зависимости от типа события (`appendText`, `generatingImage`, `imageGenerated`, `done`, `suggestedFollowups`, `replaceText`, `error`) генерирует соответствующие результаты.

11. **Завершение**:
    - Закрывает WebSocket-соединение.

**ASCII Flowchart**:

```
     Начало
     ↓
     Проверка зависимостей (curl_cffi)
     ↓
     Получение или обновление токена доступа
     ↓
     Создание сессии
     ↓
     Получение информации о пользователе
     ↓
     Создание или использование беседы
     ↓
     Загрузка медиафайлов (если есть)
     ↓
     Установка WebSocket-соединения
     ↓
     Отправка сообщения через WebSocket
     ↓
     Обработка ответов WebSocket
     ├── appendText      → Генерация текста
     ├── generatingImage → Запрос на генерацию изображения
     ├── imageGenerated  → Возврат URL изображения
     ├── done            → Завершение
     ├── suggestedFollowups → Предложенные следующие шаги
     ├── replaceText     → Замена текста
     └── error           → Обработка ошибки
     ↓
     Закрытие WebSocket-соединения
     ↓
     Конец
```

**Примеры**:

```python
# Пример 1: Создание простого текстового запроса
messages = [{"role": "user", "content": "Напиши короткое стихотворение о весне."}]
result = Copilot.create_completion(model="Copilot", messages=messages)
for chunk in result:
    print(chunk, end="")

# Пример 2: Создание запроса с потоковой передачей
messages = [{"role": "user", "content": "Расскажи о последних новостях в мире."}]
result = Copilot.create_completion(model="Think Deeper", messages=messages, stream=True)
for chunk in result:
    print(chunk, end="")

# Пример 3: Отправка изображения и текстового запроса
media = "path/to/image.jpg"
messages = [{"role": "user", "content": "Опиши, что ты видишь на этой картинке."}]
result = Copilot.create_completion(model="Copilot", messages=messages, media=media)
for chunk in result:
    print(chunk, end="")
```

### `get_access_token_and_cookies`

```python
async def get_access_token_and_cookies(url: str, proxy: str = None, target: str = "ChatAI",):
    """
    Получает токен доступа и куки из браузера с использованием nodriver.

    Args:
        url (str): URL для открытия в браузере.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        target (str, optional): Цель для поиска токена доступа. По умолчанию "ChatAI".

    Returns:
        Tuple[str, dict]: Токен доступа и словарь куки.

    """
```

**Назначение**: Получает токен доступа и куки из браузера с использованием `nodriver`.

**Параметры**:
- `url` (str): URL для открытия в браузере.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `target` (str, optional): Цель для поиска токена доступа. По умолчанию "ChatAI".

**Возвращает**:
- `Tuple[str, dict]`: Кортеж, содержащий токен доступа и словарь куки.

**Как работает функция**:

1. **Запуск браузера**:
   - Запускает браузер с использованием `get_nodriver(proxy=proxy, user_data_dir="copilot")`.

2. **Открытие страницы**:
   - Открывает страницу с заданным `url`.

3. **Извлечение токена доступа**:
   - Выполняет JavaScript-код в браузере для извлечения токена доступа из `localStorage`.

4. **Извлечение куки**:
   - Получает куки из браузера.

5. **Завершение**:
   - Закрывает страницу и останавливает браузер.

**ASCII Flowchart**:

```
     Начало
     ↓
     Запуск браузера (nodriver)
     ↓
     Открытие страницы (url)
     ↓
     Извлечение токена доступа (localStorage)
     ↓
     Извлечение куки
     ↓
     Закрытие страницы и остановка браузера
     ↓
     Конец
```

**Примеры**:

```python
# Пример получения токена доступа и куки
import asyncio

async def main():
    url = "https://copilot.microsoft.com"
    token, cookies = await get_access_token_and_cookies(url)
    print(f"Токен доступа: {token}")
    print(f"Куки: {cookies}")

asyncio.run(main())
```

### `readHAR`

```python
def readHAR(url: str):
    """
    Читает HAR-файлы и извлекает токен доступа и куки.

    Args:
        url (str): URL для поиска в HAR-файлах.

    Returns:
        Tuple[str, dict]: Токен доступа и словарь куки.

    Raises:
        NoValidHarFileError: Если не найдены HAR-файлы или токен доступа.

    """
```

**Назначение**: Читает HAR-файлы и извлекает токен доступа и куки.

**Параметры**:
- `url` (str): URL для поиска в HAR-файлах.

**Возвращает**:
- `Tuple[str, dict]`: Кортеж, содержащий токен доступа и словарь куки.

**Вызывает исключения**:
- `NoValidHarFileError`: Если не найдены HAR-файлы или токен доступа.

**Как работает функция**:

1. **Поиск HAR-файлов**:
   - Получает список HAR-файлов с помощью `get_har_files()`.

2. **Чтение HAR-файлов**:
   - Читает каждый HAR-файл и ищет записи, соответствующие заданному `url`.

3. **Извлечение токена доступа и куки**:
   - Извлекает токен доступа из заголовка `authorization` и куки из запроса.

4. **Завершение**:
   - Возвращает токен доступа и куки.

**ASCII Flowchart**:

```
     Начало
     ↓
     Поиск HAR-файлов
     ↓
     Чтение HAR-файлов
     ↓
     Поиск записей с заданным URL
     ↓
     Извлечение токена доступа и куки
     ↓
     Конец
```

**Примеры**:

```python
# Пример чтения HAR-файла
url = "https://copilot.microsoft.com"
try:
    token, cookies = readHAR(url)
    print(f"Токен доступа: {token}")
    print(f"Куки: {cookies}")
except NoValidHarFileError as ex:
    print(f"Ошибка: {ex}")
```

### `get_clarity`

```python
def get_clarity() -> bytes:
    """
    Возвращает тело запроса для Clarity.

    Returns:
        bytes: Тело запроса в виде байтов.

    """
```

**Назначение**: Возвращает тело запроса для Clarity.

**Возвращает**:
- `bytes`: Тело запроса в виде байтов.

**Как работает функция**:

1. **Декодирование Base64**:
   - Декодирует строку Base64, содержащую данные для Clarity.

2. **Завершение**:
   - Возвращает декодированные данные.

**ASCII Flowchart**:

```
     Начало
     ↓
     Декодирование Base64
     ↓
     Конец
```

**Примеры**:

```python
# Пример получения тела запроса для Clarity
body = get_clarity()
print(f"Тело запроса: {body}")