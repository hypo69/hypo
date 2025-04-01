# Модуль Copilot

## Обзор

Модуль `Copilot` предоставляет интерфейс для взаимодействия с Microsoft Copilot, используя веб-сокеты и HTTP-запросы. Он позволяет отправлять текстовые запросы и изображения, а также получать ответы в виде текста, изображений и предложений.

## Подробней

Модуль реализует класс `Copilot`, который является провайдером для работы с Copilot. Он использует библиотеку `curl_cffi` для установки соединения через веб-сокеты и выполнения HTTP-запросов. Если `curl_cffi` недоступен, модуль выдает исключение `MissingRequirementsError`.
Модуль также включает функции для получения access token и cookies, необходимых для аутентификации.

## Классы

### `Conversation`

**Описание**:
Класс `Conversation` представляет собой контейнер для хранения идентификатора беседы. Он наследуется от `JsonConversation`.

**Принцип работы**:
Класс предназначен для хранения `conversation_id`, который используется для идентификации текущей беседы с Copilot.

**Методы**:
- `__init__(self, conversation_id: str)`: Конструктор класса, принимающий `conversation_id` и инициализирующий атрибут `self.conversation_id`.

    ```python
    def __init__(self, conversation_id: str):
        """
        Инициализирует экземпляр класса Conversation.

        Args:
            conversation_id (str): Идентификатор беседы.
        """
        ...
    ```

### `Copilot`

**Описание**:
Класс `Copilot` является основным классом, реализующим взаимодействие с Microsoft Copilot. Он предоставляет методы для создания запросов, обработки ответов и аутентификации.

**Принцип работы**:
Класс использует `curl_cffi` для установки веб-сокет соединения и отправки запросов. Он также реализует логику для получения и обновления access token и cookies.

**Атрибуты**:
- `label` (str): Метка провайдера ("Microsoft Copilot").
- `url` (str): URL Microsoft Copilot ("https://copilot.microsoft.com").
- `working` (bool): Индикатор работоспособности провайдера (True).
- `supports_stream` (bool): Поддержка потоковой передачи данных (True).
- `default_model` (str): Модель по умолчанию ("Copilot").
- `models` (List[str]): Список поддерживаемых моделей (["Copilot", "Think Deeper"]).
- `model_aliases` (Dict[str, str]): Псевдонимы моделей.
- `websocket_url` (str): URL веб-сокета ("wss://copilot.microsoft.com/c/api/chat?api-version=2").
- `conversation_url` (str): URL для управления беседами (f"{url}/c/api/conversations").
- `_access_token` (str): Приватный атрибут для хранения access token.
- `_cookies` (dict): Приватный атрибут для хранения cookies.

**Методы**:
- `create_completion(cls, model: str, messages: Messages, stream: bool = False, proxy: str = None, timeout: int = 900, prompt: str = None, media: MediaListType = None, conversation: BaseConversation = None, return_conversation: bool = False, api_key: str = None, **kwargs) -> CreateResult`

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
        Создает запрос к Copilot и возвращает результат.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений для отправки.
            stream (bool, optional): Включить потоковый режим. По умолчанию False.
            proxy (str, optional): URL прокси-сервера. По умолчанию None.
            timeout (int, optional): Время ожидания запроса. По умолчанию 900.
            prompt (str, optional): Текст запроса. По умолчанию None.
            media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию None.
            conversation (BaseConversation, optional): Объект беседы. По умолчанию None.
            return_conversation (bool, optional): Вернуть объект беседы. По умолчанию False.
            api_key (str, optional): API ключ для аутентификации. По умолчанию None.

        Returns:
            CreateResult: Результат запроса.

        Raises:
            MissingRequirementsError: Если не установлен пакет `curl_cffi`.
            NoValidHarFileError: Если не найден валидный HAR-файл.
            MissingAuthError: Если access token недействителен.
            RuntimeError: Если произошла ошибка при взаимодействии с Copilot.
        """
        ...
    ```

## Функции

### `get_access_token_and_cookies(url: str, proxy: str = None, target: str = "ChatAI") -> tuple[str, dict]`

```python
async def get_access_token_and_cookies(url: str, proxy: str = None, target: str = "ChatAI",):
    """
    Асинхронно получает access token и cookies из браузера с использованием nodriver.

    Args:
        url (str): URL для получения access token и cookies.
        proxy (str, optional): URL прокси-сервера. По умолчанию None.
        target (str, optional): Цель для поиска access token. По умолчанию "ChatAI".

    Returns:
        tuple[str, dict]: Кортеж, содержащий access token и словарь cookies.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Функция `get_access_token_and_cookies` асинхронно запускает браузер с помощью `get_nodriver`, указывая прокси и каталог пользовательских данных.
2.  **Получение страницы**: Открывает указанный URL (`url`) в браузере.
3.  **Извлечение Access Token**:
    *   Выполняет JavaScript-код на странице для поиска access token в `localStorage`.
    *   Access token извлекается, если он имеет тип `AccessToken`, не истек и включает указанную цель (`target`).
    *   Если access token не найден, функция ждет 1 секунду и повторяет попытку.
4.  **Извлечение Cookies**:
    *   Получает все cookies для указанного URL с использованием `nodriver.cdp.network.get_cookies`.
    *   Преобразует список cookies в словарь, где ключом является имя cookie, а значением - его значение.
5.  **Закрытие страницы и браузера**:
    *   Закрывает текущую страницу.
    *   Останавливает браузер.
6.  **Возврат данных**: Возвращает извлеченный access token и словарь cookies.

**Примеры**:

```python
# Пример вызова функции
import asyncio
async def main():
    access_token, cookies = await get_access_token_and_cookies("https://copilot.microsoft.com")
    print(f"Access Token: {access_token}")
    print(f"Cookies: {cookies}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `readHAR(url: str) -> tuple[str, dict]`

```python
def readHAR(url: str):
    """
    Читает HAR-файлы для получения access token и cookies.

    Args:
        url (str): URL для поиска в HAR-файлах.

    Returns:
        tuple[str, dict]: Кортеж, содержащий access token и словарь cookies.

    Raises:
        NoValidHarFileError: Если не найден access token в HAR-файлах.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Функция `readHAR` предназначена для чтения HAR-файлов (HTTP Archive) и извлечения из них access token и cookies, необходимых для аутентификации.
2.  **Поиск HAR-файлов**: Использует функцию `get_har_files()` для получения списка путей к HAR-файлам.
3.  **Перебор HAR-файлов**:
    *   Перебирает каждый файл в списке, пытаясь открыть и прочитать его содержимое как JSON.
    *   Если файл не удается прочитать как JSON, переходит к следующему файлу.
4.  **Анализ записей в HAR-файле**:
    *   Для каждого HAR-файла перебирает записи (`entries`) в разделе `log`.
    *   Проверяет, начинается ли URL запроса (`request.url`) с указанного URL (`url`).
5.  **Извлечение Access Token и Cookies**:
    *   Если URL совпадает, извлекает заголовки запроса (`request.headers`) с помощью функции `get_headers`.
    *   Ищет заголовок `authorization` и, если он найден, извлекает access token, разделяя строку по пробелу и беря последний элемент.
    *   Извлекает cookies из запроса (`request.cookies`) и преобразует их в словарь, где ключом является имя cookie, а значением - его значение.
6.  **Проверка наличия Access Token**:
    *   Если после перебора всех HAR-файлов access token не найден, вызывает исключение `NoValidHarFileError`.
7.  **Возврат данных**: Возвращает извлеченный access token и словарь cookies.

**Примеры**:

```python
# Пример вызова функции
try:
    access_token, cookies = readHAR("https://copilot.microsoft.com")
    print(f"Access Token: {access_token}")
    print(f"Cookies: {cookies}")
except NoValidHarFileError as ex:
    print(f"Error: {ex}")
```

### `get_clarity() -> bytes`

```python
def get_clarity() -> bytes:
    """
    Возвращает декодированные данные Clarity.

    Returns:
        bytes: Декодированные данные Clarity.
    """
    ...
```

**Как работает функция**:

1.  **Декодирование Base64**: Функция `get_clarity` возвращает декодированные данные, представляющие собой тело запроса для сервиса Clarity. Эти данные закодированы в формате Base64.
2.  **Возврат декодированных данных**: Декодированная строка возвращается как байтовый массив.

**Примеры**:

```python
# Пример вызова функции
clarity_data = get_clarity()
print(f"Clarity Data: {clarity_data}")