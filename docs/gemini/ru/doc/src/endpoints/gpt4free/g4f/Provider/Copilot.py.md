# Модуль для взаимодействия с Microsoft Copilot

## Обзор

Модуль `Copilot.py` предоставляет интерфейс для взаимодействия с Microsoft Copilot. Он включает в себя функции для создания запросов к Copilot, обработки ответов, работы с изображениями и управления сессиями. Модуль поддерживает стриминг ответов, работу через прокси и аутентификацию с использованием access token.

## Подробнее

Модуль предназначен для интеграции Copilot в проекты, требующие взаимодействия с AI-моделью Microsoft. Он использует библиотеку `curl_cffi` для выполнения HTTP-запросов и WebSocket-соединений, а также `nodriver` для автоматического получения access token и cookies.

## Классы

### `Conversation`

**Описание**: Класс представляет собой идентификатор разговора с Copilot.
**Наследует**: `JsonConversation` - абстрактный базовый класс для представления ID беседы.

**Атрибуты**:

-   `conversation_id` (str): Уникальный идентификатор разговора.

**Методы**:
Отсутствуют

### `Copilot`

**Описание**: Класс для взаимодействия с Microsoft Copilot. Предоставляет методы для создания и управления сессиями Copilot, отправки запросов и получения ответов.

**Наследует**: `AbstractProvider`, `ProviderModelMixin`.
`AbstractProvider` - абстрактный базовый класс для всех поставщиков.
`ProviderModelMixin` - класс, примесь для управления моделями поставщика.

**Атрибуты**:

-   `label` (str): Метка провайдера ("Microsoft Copilot").
-   `url` (str): URL главной страницы Copilot ("https://copilot.microsoft.com").
-   `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
-   `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи (True).
-   `default_model` (str): Модель, используемая по умолчанию ("Copilot").
-   `models` (list[str]): Список поддерживаемых моделей (["Copilot", "Think Deeper"]).
-   `model_aliases` (dict[str, str]): Словарь псевдонимов моделей ({"gpt-4": "Copilot", "gpt-4o": "Copilot", "o1": "Think Deeper", "reasoning": "Think Deeper", "dall-e-3": "Copilot"}).
-   `websocket_url` (str): URL для WebSocket-соединения ("wss://copilot.microsoft.com/c/api/chat?api-version=2").
-   `conversation_url` (str): URL для управления разговорами ("https://copilot.microsoft.com/c/api/conversations").
-   `_access_token` (str): Приватный атрибут для хранения access token.
-   `_cookies` (dict): Приватный атрибут для хранения cookies.

**Методы**:

-   `create_completion()`: Отправляет запрос к Copilot и возвращает ответ.

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
    Создает запрос к Copilot и возвращает ответ.

    Args:
        model (str): Используемая модель.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Включить потоковый режим. По умолчанию False.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию None.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 900.
        prompt (str, optional): Текст запроса. По умолчанию None.
        media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию None.
        conversation (BaseConversation, optional): Объект разговора. По умолчанию None.
        return_conversation (bool, optional): Вернуть объект разговора. По умолчанию False.
        api_key (str, optional): API ключ для аутентификации. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Returns:
        CreateResult: Результат запроса.

    Raises:
        MissingRequirementsError: Если не установлен пакет `curl_cffi`.
        NoValidHarFileError: Если не найден валидный HAR-файл.
        MissingAuthError: Если получен статус 401 (неверный access token).
        RuntimeError: Если произошла ошибка при взаимодействии с Copilot.

    """
```

**Назначение**: Функция `create_completion` отвечает за отправку запроса к Microsoft Copilot и получение ответа. Она обрабатывает аутентификацию, создание или использование существующей сессии разговора, загрузку медиафайлов и отправку запроса через WebSocket. Функция поддерживает потоковый режим, позволяя получать ответы по частям.

**Как работает функция**:

1.  **Проверка зависимостей**:
    -   Проверяет, установлен ли пакет `curl_cffi`. Если нет, вызывает исключение `MissingRequirementsError`.
2.  **Подготовка параметров**:
    -   Определяет используемую модель Copilot.
    -   Определяет URL WebSocket для подключения.
3.  **Аутентификация**:
    -   Проверяет наличие access token. Если токен не предоставлен или устарел, пытается прочитать его из HAR-файла или получить с использованием `nodriver`.
    -   Если не удается получить access token, пытается получить его автоматически, используя `nodriver` для открытия браузера и извлечения токена из localStorage.
    -   Если автоматическое получение не удается, вызывает исключение `MissingAuthError`.
4.  **Создание сессии**:
    -   Использует `Session` из `curl_cffi` для выполнения HTTP-запросов и WebSocket-соединений.
    -   Если не предоставлен объект разговора, создает новый разговор, отправляя POST-запрос к `conversation_url`.
    -   Формирует текст запроса из списка сообщений.
5.  **Загрузка медиафайлов**:
    -   Если предоставлены медиафайлы, загружает их на сервер Copilot и получает URL для доступа.
6.  **Отправка запроса через WebSocket**:
    -   Устанавливает WebSocket-соединение с сервером Copilot.
    -   Отправляет сообщение с текстом запроса и информацией о загруженных медиафайлах.
7.  **Обработка ответов**:
    -   Получает сообщения от сервера Copilot через WebSocket.
    -   Обрабатывает различные типы сообщений, такие как текст, изображения, предложения и ошибки.
    -   Возвращает результат запроса в потоковом режиме или целиком.
8.  **Обработка ошибок**:
    -   Обрабатывает ошибки, возникающие при взаимодействии с Copilot, и вызывает исключения `RuntimeError` в случае необходимости.
9.  **Закрытие соединения**:
    -   Закрывает WebSocket-соединение после завершения обмена сообщениями.

**ASCII flowchart**:

```
    [Проверка зависимостей curl_cffi]
    |
    [Определение используемой модели Copilot]
    |
    [Аутентификация: проверка и получение access token]
    |
    [Создание сессии curl_cffi]
    |
    [Создание или использование существующего разговора]
    |
    [Формирование текста запроса]
    |
    [Загрузка медиафайлов (если есть)]
    |
    [Установка WebSocket-соединения]
    |
    [Отправка сообщения с запросом]
    |
    [Обработка ответов Copilot]
    |
    [Закрытие WebSocket-соединения]
```

**Примеры**:

```python
# Пример 1: Отправка текстового запроса
messages = [{"role": "user", "content": "Напиши короткое стихотворение о весне."}]
result = Copilot.create_completion(model="Copilot", messages=messages)
for part in result:
    print(part, end="")

# Пример 2: Отправка запроса с изображением
media = "path/to/image.jpg"
messages = [{"role": "user", "content": "Опиши, что изображено на картинке."}]
result = Copilot.create_completion(model="Copilot", messages=messages, media=media)
for part in result:
    print(part, end="")

# Пример 3: Использование существующего разговора
conversation = Conversation(conversation_id="12345")
messages = [{"role": "user", "content": "Продолжи разговор."}]
result = Copilot.create_completion(model="Copilot", messages=messages, conversation=conversation)
for part in result:
    print(part, end="")
```

### `get_access_token_and_cookies`

```python
async def get_access_token_and_cookies(url: str, proxy: str = None, target: str = "ChatAI",):
    """
    Асинхронно получает access token и cookies, используя автоматизированный браузер.

    Args:
        url (str): URL для получения access token.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию None.
        target (str, optional): Цель для access token. По умолчанию "ChatAI".

    Returns:
        tuple[str, dict]: Access token и словарь cookies.

    Raises:
        Exception: Если не удалось получить access token или cookies.

    """
```

**Назначение**: Функция `get_access_token_and_cookies` использует автоматизированный браузер для получения access token и cookies с заданной страницы. Это необходимо для аутентификации в Copilot, когда прямой доступ к access token невозможен.

**Как работает функция**:

1.  **Запуск браузера**:
    -   Использует `get_nodriver` для запуска автоматизированного браузера (например, Chrome или Firefox) с заданным прокси-сервером и каталогом пользовательских данных.
2.  **Получение страницы**:
    -   Открывает заданный URL в браузере.
3.  **Извлечение access token**:
    -   Выполняет JavaScript-код в браузере для извлечения access token из localStorage.
    -   JavaScript-код ищет элементы localStorage, содержащие credentialType "AccessToken", не истекшие по времени и содержащие заданную цель (target).
    -   Если access token не найден, повторяет попытку через 1 секунду.
4.  **Получение cookies**:
    -   Получает все cookies для заданного URL из браузера.
5.  **Закрытие страницы и остановка браузера**:
    -   Закрывает страницу в браузере.
    -   Останавливает автоматизированный браузер.
6.  **Возврат результата**:
    -   Возвращает access token и словарь cookies.

**ASCII flowchart**:

```
    [Запуск автоматизированного браузера]
    |
    [Открытие URL в браузере]
    |
    [Выполнение JavaScript-кода для извлечения access token из localStorage]
    |
    [Получение cookies для URL]
    |
    [Закрытие страницы и остановка браузера]
    |
    [Возврат access token и cookies]
```

**Примеры**:

```python
# Пример: Получение access token и cookies
url = "https://copilot.microsoft.com"
access_token, cookies = asyncio.run(get_access_token_and_cookies(url))
print(f"Access Token: {access_token}")
print(f"Cookies: {cookies}")
```

### `readHAR`

```python
def readHAR(url: str):
    """
    Читает HAR-файлы в поисках access token и cookies.

    Args:
        url (str): URL для поиска в HAR-файлах.

    Returns:
        tuple[str, dict]: Access token и словарь cookies.

    Raises:
        NoValidHarFileError: Если access token не найден в HAR-файлах.

    """
```

**Назначение**: Функция `readHAR` анализирует HAR-файлы (HTTP Archive) для извлечения access token и cookies, связанных с заданным URL. HAR-файлы содержат записи HTTP-трафика, которые могут быть использованы для получения учетных данных.

**Как работает функция**:

1.  **Поиск HAR-файлов**:
    -   Использует `get_har_files` для получения списка путей к HAR-файлам.
2.  **Анализ HAR-файлов**:
    -   Перебирает HAR-файлы в списке.
    -   Читает содержимое каждого HAR-файла.
    -   Ищет записи, соответствующие заданному URL.
    -   Извлекает access token из заголовка "authorization".
    -   Извлекает cookies из запроса.
3.  **Возврат результата**:
    -   Если access token найден, возвращает его и словарь cookies.
    -   Если access token не найден ни в одном HAR-файле, вызывает исключение `NoValidHarFileError`.

**ASCII flowchart**:

```
    [Получение списка HAR-файлов]
    |
    [Перебор HAR-файлов]
    |
    [Чтение содержимого HAR-файла]
    |
    [Поиск записей, соответствующих URL]
    |
    [Извлечение access token из заголовка "authorization"]
    |
    [Извлечение cookies из запроса]
    |
    [Возврат access token и cookies]
```

**Примеры**:

```python
# Пример: Чтение access token и cookies из HAR-файла
url = "https://copilot.microsoft.com"
try:
    access_token, cookies = readHAR(url)
    print(f"Access Token: {access_token}")
    print(f"Cookies: {cookies}")
except NoValidHarFileError as ex:
    print(f"Error: {ex}")
```

### `get_clarity`

```python
def get_clarity() -> bytes:
    """
    Возвращает закодированное тело запроса для сервиса Clarity.

    Returns:
        bytes: Закодированное тело запроса.
    """
```

**Назначение**: Функция `get_clarity` возвращает закодированное тело запроса, используемое для взаимодействия с сервисом Microsoft Clarity. Сервис Clarity предназначен для анализа поведения пользователей на веб-сайтах.

**Как работает функция**:

1.  **Определение закодированного тела запроса**:
    -   Закодированное тело запроса представлено в виде строки base64.
2.  **Декодирование тела запроса**:
    -   Строка base64 декодируется с использованием `base64.b64decode`.
3.  **Возврат результата**:
    -   Возвращает декодированное тело запроса в виде байтов.

**ASCII flowchart**:

```
    [Определение закодированного тела запроса в base64]
    |
    [Декодирование строки base64]
    |
    [Возврат декодированного тела запроса в виде байтов]
```

**Примеры**:

```python
# Пример: Получение тела запроса для сервиса Clarity
body = get_clarity()
print(f"Body: {body}")