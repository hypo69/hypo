# Модуль для работы с провайдером RubiksAI
## Обзор

Модуль `RubiksAI` предоставляет асинхронный интерфейс для взаимодействия с API Rubiks AI. Он позволяет генерировать текст на основе заданных сообщений, используя различные модели, поддерживаемые Rubiks AI. Модуль поддерживает потоковую передачу данных, системные сообщения и историю сообщений.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для обеспечения доступа к возможностям Rubiks AI для генерации текста. Он включает в себя функции для создания уникальных идентификаторов, формирования URL-адресов и отправки запросов к API Rubiks AI.
Провайдер RubiksAI позволяет использовать разные модели, такие как `gpt-4o-mini`, `gpt-4o`, `o1-mini`, `claude-3.5-sonnet`, `grok-beta`, `gemini-1.5-pro`, `nova-pro`, `llama-3.1-70b-versatile`.
Для запросов используется библиотека `aiohttp`. Результаты возвращаются в виде асинхронного генератора.

## Классы

### `RubiksAI`

**Описание**: Класс `RubiksAI` предоставляет асинхронный интерфейс для взаимодействия с API Rubiks AI. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих данные.
- `ProviderModelMixin`: Предоставляет вспомогательные методы для работы с моделями, такими как получение модели по имени или псевдониму.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Rubiks AI"`.
- `url` (str): URL главной страницы Rubiks AI, `"https://rubiks.ai"`.
- `api_endpoint` (str): URL API для отправки запросов, `"https://rubiks.ai/search/api/"`.
- `working` (bool): Указывает, работает ли провайдер, `True`.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных, `True`.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения, `True`.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений, `True`.
- `default_model` (str): Модель, используемая по умолчанию, `'gpt-4o-mini'`.
- `models` (List[str]): Список поддерживаемых моделей, включающий `default_model` и другие модели.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей, где ключ - псевдоним, значение - настоящее имя модели.

**Методы**:
- `generate_mid()`: Генерирует уникальный идентификатор сообщения.
- `create_referer(q: str, mid: str, model: str = '') -> str`: Создает URL-адрес Referer с динамическими значениями `q` (запрос) и `mid` (идентификатор сообщения).
- `create_async_generator(model: str, messages: Messages, proxy: str = None, web_search: bool = False, temperature: float = 0.6, **kwargs) -> AsyncResult`: Создает асинхронный генератор, отправляющий запросы к API Rubiks AI и возвращающий ответ.

## Функции

### `generate_mid`

```python
 @staticmethod
 def generate_mid() -> str:
     """
     Generates a 'mid' string following the pattern:
     6 characters - 4 characters - 4 characters - 4 characters - 12 characters
     Example: 0r7v7b-quw4-kdy3-rvdu-ekief6xbuuq4
     """
     ...
```

**Назначение**: Генерирует уникальный идентификатор сообщения (`mid`) в формате `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`, где `x` - случайный символ из букв нижнего регистра и цифр.

**Как работает функция**:

1.  **Генерация частей идентификатора**: Функция генерирует пять частей идентификатора, используя случайные символы из букв нижнего регистра и цифр.
2.  **Соединение частей**: Полученные части соединяются с помощью дефисов `-`.
3.  **Возврат идентификатора**: Функция возвращает полученный идентификатор в виде строки.

```
Генерация частей идентификатора --> Соединение частей с помощью дефисов --> Возврат идентификатора
```

**Примеры**:

```python
RubiksAI.generate_mid()  # Пример вызова функции
# Output: 'a1b2c3-d4e5-f6g7-h8i9-j0k1l2m3n4o5' (пример сгенерированного mid)
```

### `create_referer`

```python
@staticmethod
def create_referer(q: str, mid: str, model: str = '') -> str:
    """
    Creates a Referer URL with dynamic q and mid values, using urlencode for safe parameter encoding.
    """
    ...
```

**Назначение**: Создает URL-адрес Referer с динамическими значениями `q` (запрос), `mid` (идентификатор сообщения) и `model` (модель), используя `urlencode` для безопасного кодирования параметров.

**Параметры**:
- `q` (str): Текст запроса.
- `mid` (str): Уникальный идентификатор сообщения.
- `model` (str, optional): Модель, используемая для запроса. По умолчанию `''`.

**Возвращает**:
- `str`: Сформированный URL-адрес Referer.

**Как работает функция**:

1.  **Создание словаря параметров**: Функция создает словарь, содержащий параметры `q`, `model` и `mid`.
2.  **Кодирование параметров**: Функция кодирует параметры URL с помощью `urlencode`.
3.  **Формирование URL**: Функция формирует URL-адрес Referer, добавляя закодированные параметры к базовому URL `https://rubiks.ai/search/?`.
4.  **Возврат URL**: Функция возвращает полученный URL-адрес.

```
Создание словаря параметров --> Кодирование параметров URL --> Формирование URL-адреса --> Возврат URL
```

**Примеры**:

```python
RubiksAI.create_referer(q='text generation', mid='a1b2c3-d4e5-f6g7-h8i9-j0k1l2m3n4o5', model='gpt-4o')
# Output: 'https://rubiks.ai/search/?q=text+generation&model=gpt-4o&mid=a1b2c3-d4e5-f6g7-h8i9-j0k1l2m3n4o5'
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    web_search: bool = False,
    temperature: float = 0.6,
    **kwargs
) -> AsyncResult:
    """
    Creates an asynchronous generator that sends requests to the Rubiks AI API and yields the response.

    Parameters:
    - model (str): The model to use in the request.
    - messages (Messages): The messages to send as a prompt.
    - proxy (str, optional): Proxy URL, if needed.
    - web_search (bool, optional): Indicates whether to include search sources in the response. Defaults to False.
    """
    ...
```

**Назначение**: Создает асинхронный генератор, который отправляет запросы к API Rubiks AI и возвращает ответ в виде потока данных.

**Параметры**:
- `model` (str): Модель, используемая для запроса.
- `messages` (Messages): Список сообщений для отправки в качестве запроса.
- `proxy` (str, optional): URL прокси-сервера, если необходимо. По умолчанию `None`.
- `web_search` (bool, optional): Указывает, следует ли включать источники из веб-поиска в ответ. По умолчанию `False`.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию `0.6`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст от API Rubiks AI.

**Как работает функция**:

1.  **Подготовка данных**:
    *   Получает модель, используя `cls.get_model(model)`.
    *   Генерирует уникальный идентификатор сообщения (`mid_value`).
    *   Создает URL-адрес Referer, используя `cls.create_referer()`.
    *   Формирует словарь `data` с сообщениями, моделью, настройками поиска и температуры.
    *   Определяет заголовки запроса, включая Referer и User-Agent.
2.  **Отправка запроса и обработка ответа**:
    *   Создает асинхронную сессию `ClientSession`.
    *   Отправляет POST-запрос к API Rubiks AI (`cls.api_endpoint`) с заголовками и данными.
    *   Обрабатывает ответ, декодируя каждую строку и извлекая данные.
    *   Ищет источники (`url` и `title`) и добавляет их в список `sources`, если `web_search` включен.
    *   Извлекает содержимое из `choices` и возвращает его через `yield content`.
3.  **Возврат результатов**:
    *   Если `web_search` включен и есть источники, возвращает `Sources(sources)`.

```
Подготовка данных (модель, mid, Referer, data, headers) --> Отправка POST-запроса к API --> Обработка ответа (декодирование, извлечение данных, поиск источников, извлечение содержимого) --> Возврат результатов (текст, источники)
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Tell me a joke."}]
async for message in RubiksAI.create_async_generator(model='gpt-4o-mini', messages=messages, web_search=False):
    print(message)