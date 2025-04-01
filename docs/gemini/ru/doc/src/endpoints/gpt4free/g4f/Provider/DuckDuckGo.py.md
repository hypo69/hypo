# Модуль для взаимодействия с DuckDuckGo AI Chat
## Обзор
Модуль предоставляет асинхронный интерфейс для взаимодействия с DuckDuckGo AI Chat, используя библиотеку `duckduckgo_search`. Он поддерживает потоковую передачу ответов, системные сообщения и историю сообщений. Модуль также включает механизм аутентификации без использования драйвера браузера (nodriver).
## Подробнее
Этот модуль позволяет взаимодействовать с DuckDuckGo AI Chat для получения ответов на запросы, используя различные модели, такие как `gpt-4o-mini`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`, `claude-3-haiku-20240307`, `o3-mini` и `mistralai/Mistral-Small-24B-Instruct-2501`. Он использует библиотеку `duckduckgo_search` для отправки запросов и получения ответов. Если библиотека не установлена, модуль выдает ошибку `ImportError`.
Также модуль содержит механизм аутентификации без использования драйвера браузера, который позволяет получить необходимые заголовки для взаимодействия с API DuckDuckGo AI Chat.

## Классы
### `DuckDuckGo`
Описание: Класс, предоставляющий асинхронный интерфейс для взаимодействия с DuckDuckGo AI Chat.
**Наследует:**
`AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты:**
- `label` (str): Метка провайдера (Duck.ai (duckduckgo_search)).
- `url` (str): URL DuckDuckGo AI Chat (https://duckduckgo.com/aichat).
- `api_base` (str): Базовый URL API DuckDuckGo (https://duckduckgo.com/duckchat/v1/).
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель по умолчанию (gpt-4o-mini).
- `models` (List[str]): Список поддерживаемых моделей.
- `ddgs` (DDGS): Объект DDGS для взаимодействия с DuckDuckGo Search API.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

#### `create_async_generator`
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
        """Асинхронный генератор для взаимодействия с DuckDuckGo AI Chat.
        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
            timeout (int, optional): Время ожидания запроса. По умолчанию 60.
        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от DuckDuckGo AI Chat.
        Raises:
            ImportError: Если не установлена библиотека duckduckgo_search.
        """
```

**Как работает функция**:
1. Проверяет, установлена ли библиотека `duckduckgo_search`. Если нет, вызывает исключение `ImportError`.
2. Инициализирует объект `DDGS`, если он еще не был инициализирован.
3. Аутентифицируется без использования драйвера, если `has_nodriver` равно `True`.
4. Получает имя модели, используя метод `get_model`.
5. Итерируется по ответам, возвращаемым генератором `cls.ddgs.chat_yield`, и передает каждый фрагмент ответа.

```ascii
Проверка установки duckduckgo_search --> Инициализация DDGS --> Аутентификация без драйвера (если необходимо) --> Получение имени модели --> Итерирование по ответам от DDGS и передача фрагментов
```

**Примеры**:
```python
# Пример вызова функции
async for chunk in DuckDuckGo.create_async_generator(model="gpt-4o-mini", messages=[{"role": "user", "content": "Hello"}], proxy="http://proxy.example.com:8080", timeout=30):
    print(chunk)
```
#### `nodriver_auth`
```python
    @classmethod
    async def nodriver_auth(cls, proxy: str = None):
        """Аутентификация без использования драйвера браузера.

        Args:
            proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
        """
```
**Как работает функция**:
1. Получает экземпляр браузера и функцию для его остановки, используя `get_nodriver`.
2. Определяет функцию `on_request`, которая перехватывает сетевые запросы и извлекает значения заголовков `X-Vqd-4`, `X-Vqd-Hash-1` и `F-Fe-Version`, если они присутствуют в запросе к `cls.api_base`.
3. Включает перехват сетевых запросов.
4. Добавляет обработчик для события `RequestWillBeSent`, чтобы вызывать функцию `on_request` при каждом запросе.
5. Открывает страницу `cls.url` в браузере.
6. Ожидает, пока не будет получено значение `cls.ddgs._chat_vqd`.
7. Закрывает страницу и останавливает браузер.

```ascii
Получение экземпляра браузера --> Определение функции перехвата запросов --> Включение перехвата запросов --> Добавление обработчика для события RequestWillBeSent --> Открытие страницы в браузере --> Ожидание получения значения cls.ddgs._chat_vqd --> Закрытие страницы и остановка браузера
```

**Примеры**:
```python
# Пример вызова функции
await DuckDuckGo.nodriver_auth(proxy="http://proxy.example.com:8080")
```

## Функции

### `get_last_user_message`
```python
from ..typing import Messages

def get_last_user_message(messages: Messages) -> str | None:
    """Получает последнее сообщение от пользователя из списка сообщений.

    Args:
        messages (Messages): Список сообщений, где каждое сообщение - словарь с ключами "role" и "content".

    Returns:
        str | None: Текст последнего сообщения от пользователя, или None, если таких сообщений нет.
    """
    if not messages:
        return None

    for message in reversed(messages):
        if message["role"] == "user":
            return message["content"]

    return None
```

**Как работает функция**:
1. Проверяет, является ли список сообщений пустым. Если да, возвращает `None`.
2. Итерируется по списку сообщений в обратном порядке.
3. Для каждого сообщения проверяет, является ли роль сообщения "user".
4. Если роль сообщения "user", возвращает содержимое сообщения.
5. Если ни одно сообщение не имеет роль "user", возвращает `None`.

```ascii
Проверка пустоты списка сообщений --> Итерация по списку сообщений в обратном порядке --> Проверка роли сообщения --> Возврат содержимого сообщения (если роль "user") --> Возврат None (если нет сообщений с ролью "user")
```

**Примеры**:
```python
# Пример вызова функции
messages = [
    {"role": "assistant", "content": "Hello"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I am fine."},
    {"role": "user", "content": "What is your name?"}
]
last_message = get_last_user_message(messages)
print(last_message)  # Вывод: What is your name?
```
```python
# Пример вызова функции с пустым списком сообщений
messages = []
last_message = get_last_user_message(messages)
print(last_message)  # Вывод: None
```
```python
# Пример вызова функции без сообщений от пользователя
messages = [
    {"role": "assistant", "content": "Hello"},
    {"role": "assistant", "content": "I am fine."}
]
last_message = get_last_user_message(messages)
print(last_message)  # Вывод: None