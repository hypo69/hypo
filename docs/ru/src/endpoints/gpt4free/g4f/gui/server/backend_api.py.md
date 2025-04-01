# Модуль backend_api.py

## Обзор

Модуль `backend_api.py` предоставляет API для взаимодействия с различными моделями, провайдерами и управления функциональностью, такой как обработка диалогов, обработка ошибок и управление версиями в Flask-приложении `hypotez`. Он включает в себя обработку запросов к моделям, провайдерам, а также функциональность для работы с файлами, куки и медиа-контентом.

## Подробнее

Этот модуль является ключевым компонентом backend-части приложения `hypotez`, обеспечивая взаимодействие между пользовательским интерфейсом и различными сервисами и моделями. Он обрабатывает HTTP-запросы, управляет сессиями диалогов, предоставляет доступ к моделям и провайдерам, а также обеспечивает загрузку и хранение файлов.

## Классы

### `Backend_Api`

**Описание**: Класс `Backend_Api` обрабатывает различные endpoint-ы Flask-приложения для backend-операций.

**Наследует**: `Api`

**Атрибуты**:

-   `app` (Flask): Экземпляр Flask-приложения.
-   `routes` (dict): Словарь, сопоставляющий API endpoint-ы с их обработчиками.

**Методы**:

-   `__init__(self, app: Flask) -> None`: Инициализирует backend API с заданным Flask-приложением.
-   `handle_synthesize(self, provider: str)`: Обрабатывает запросы на синтез речи от определенного провайдера.
-   `get_provider_models(self, provider: str)`: Возвращает список моделей, поддерживаемых указанным провайдером.
-   `_format_json(self, response_type: str, content = None, **kwargs) -> str`: Форматирует и возвращает JSON-ответ.

### `Backend_Api.__init__(self, app: Flask) -> None`

**Назначение**: Инициализирует экземпляр класса `Backend_Api`, настраивает маршруты для Flask-приложения и инициализирует кэш диалогов.

**Параметры**:

-   `app` (Flask): Экземпляр Flask-приложения, к которому будут привязаны маршруты.

**Как работает функция**:

1.  Сохраняет переданное Flask-приложение в атрибуте `self.app`.
2.  Инициализирует `self.chat_cache` как пустой словарь для кэширования данных диалогов.
3.  Определяет маршруты для различных endpoint-ов, используя декоратор `@app.route`.
4.  Функция `home` обрабатывает корневой URL (`/`) и отображает шаблон `home.html`. Если `app.demo` истинно, отображается шаблон `demo.html` с параметрами `backend_url` и `client_id`, полученными из переменных окружения.
5.  Функция `qrcode` обрабатывает endpoint `/qrcode` и `/qrcode/<conversation_id>` и отображает шаблон `qrcode.html` с параметрами `conversation_id` и `share_url`.
6.  Функция `jsonify_models` обрабатывает endpoint `/backend-api/v2/models` и возвращает JSON-ответ, полученный из `get_demo_models()` (если `app.demo` истинно) или `self.get_models()`.
7.  Функция `jsonify_provider_models` обрабатывает endpoint `/backend-api/v2/models/<provider>` и возвращает JSON-ответ, полученный из `self.get_provider_models()`.
8.  Функция `jsonify_providers` обрабатывает endpoint `/backend-api/v2/providers` и возвращает JSON-ответ, полученный из `self.get_providers()`.
9.  Функция `get_demo_models` возвращает список демонстрационных моделей с информацией о их именах, поддержке изображений и провайдерах.
10. Функция `handle_conversation` обрабатывает запросы диалогов и возвращает потоковые ответы.
11. Функция `_handle_conversation` вызывает `handle_conversation` для обработки запросов на диалог.
12. Функция `add_usage` обрабатывает endpoint `/backend-api/v2/usage` для логирования использования API.
13. Функция `add_log` обрабатывает endpoint `/backend-api/v2/log` для добавления логов.
14. Функции `add_memory` и `read_memory` обрабатывают endpoint-ы `/backend-api/v2/memory/<user_id>` для добавления и чтения данных из памяти.
15. Определяет словарь `self.routes`, содержащий endpoint-ы для получения версии API, синтеза речи, обслуживания изображений и медиа-файлов.
16. Функция `create` обрабатывает endpoint `/backend-api/v2/create` для создания контента с использованием моделей и инструментов.
17. Функция `manage_files` обрабатывает endpoint `/backend-api/v2/files/<bucket_id>` для управления файлами в bucket-ах.
18. Функция `upload_files` обрабатывает POST-запросы к `/backend-api/v2/files/<bucket_id>` для загрузки файлов в указанный bucket.
19. Функция `get_media` обрабатывает GET-запросы к `/files/<bucket_id>/media/<filename>` для получения медиа-файлов из bucket-а.
20. Функция `find_media` обрабатывает GET-запросы к `/search/<search>` для поиска медиа-файлов.
21. Функция `upload_cookies` обрабатывает POST-запросы к `/backend-api/v2/upload_cookies` для загрузки файлов cookie.
22. Функции `get_chat` и `upload_chat` обрабатывают endpoint-ы `/backend-api/v2/chat/<share_id>` для получения и загрузки данных диалога.

**Внутренние функции**:

-   `home()`:
    -   **Назначение**: Обрабатывает корневой URL (`/`) и отображает шаблон `home.html` или `demo.html` в зависимости от значения `app.demo`.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `str`: HTML-контент для отображения.

-   `qrcode(conversation_id: str = "")`:
    -   **Назначение**: Обрабатывает endpoint `/qrcode` и `/qrcode/<conversation_id>` и отображает шаблон `qrcode.html`.
    -   **Параметры**:
        -   `conversation_id` (str, optional): Идентификатор диалога. По умолчанию пустая строка.
    -   **Возвращает**: `str`: HTML-контент для отображения.

-   `jsonify_models(**kwargs)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/models` и возвращает JSON-ответ, полученный из `get_demo_models()` (если `app.demo` истинно) или `self.get_models()`.
    -   **Параметры**:
        -   `**kwargs`: Дополнительные аргументы.
    -   **Возвращает**: `flask.Response`: JSON-ответ.

-   `jsonify_provider_models(**kwargs)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/models/<provider>` и возвращает JSON-ответ, полученный из `self.get_provider_models()`.
    -   **Параметры**:
        -   `**kwargs`: Дополнительные аргументы.
    -   **Возвращает**: `flask.Response`: JSON-ответ.

-   `jsonify_providers(**kwargs)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/providers` и возвращает JSON-ответ, полученный из `self.get_providers()`.
    -   **Параметры**:
        -   `**kwargs`: Дополнительные аргументы.
    -   **Возвращает**: `flask.Response`: JSON-ответ.

-   `get_demo_models()`:
    -   **Назначение**: Возвращает список демонстрационных моделей с информацией о их именах, поддержке изображений и провайдерах.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `list`: Список моделей.

-   `handle_conversation()`:
    -   **Назначение**: Обрабатывает запросы диалогов и возвращает потоковые ответы.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `Response`: Объект Flask-ответа для потоковой передачи.

-   `_handle_conversation()`:
    -   **Назначение**: Вызывает `handle_conversation` для обработки запросов на диалог.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `Response`: Объект Flask-ответа.

-   `add_usage()`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/usage` для логирования использования API.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `dict`: Пустой словарь.

-   `add_log()`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/log` для добавления логов.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `dict`: Пустой словарь.

-   `add_memory(user_id: str)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/memory/<user_id>` для добавления данных в память.
    -   **Параметры**:
        -   `user_id` (str): Идентификатор пользователя.
    -   **Возвращает**: `dict`: Словарь с количеством добавленных элементов.

-   `read_memory(user_id: str)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/memory/<user_id>` для чтения данных из памяти.
    -   **Параметры**:
        -   `user_id` (str): Идентификатор пользователя.
    -   **Возвращает**: `list | dict`: Список или словарь с данными из памяти.

-   `create()`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/create` для создания контента с использованием моделей и инструментов.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `Response`: Объект Flask-ответа с контентом.

-   `manage_files(bucket_id: str)`:
    -   **Назначение**: Обрабатывает endpoint `/backend-api/v2/files/<bucket_id>` для управления файлами в bucket-ах.
    -   **Параметры**:
        -   `bucket_id` (str): Идентификатор bucket-а.
    -   **Возвращает**: `Response`: Объект Flask-ответа с информацией о файлах.

-   `upload_files(bucket_id: str)`:
    -   **Назначение**: Обрабатывает POST-запросы к `/backend-api/v2/files/<bucket_id>` для загрузки файлов в указанный bucket.
    -   **Параметры**:
        -   `bucket_id` (str): Идентификатор bucket-а.
    -   **Возвращает**: `dict`: Словарь с информацией о загруженных файлах.

-   `get_media(bucket_id, filename, dirname: str = None)`:
    -   **Назначение**: Обрабатывает GET-запросы к `/files/<bucket_id>/media/<filename>` для получения медиа-файлов из bucket-а.
    -   **Параметры**:
        -   `bucket_id`: Идентификатор bucket-а.
        -   `filename`: Имя файла.
        -   `dirname` (str, optional): Имя директории. По умолчанию `None`.
    -   **Возвращает**: `Response`: Объект Flask-ответа с медиа-файлом.

-   `find_media(search: str)`:
    -   **Назначение**: Обрабатывает GET-запросы к `/search/<search>` для поиска медиа-файлов.
    -   **Параметры**:
        -   `search` (str): Строка поиска.
    -   **Возвращает**: `Response`: Объект Flask-ответа с перенаправлением на найденный файл.

-   `upload_cookies()`:
    -   **Назначение**: Обрабатывает POST-запросы к `/backend-api/v2/upload_cookies` для загрузки файлов cookie.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `str`: Строка с сообщением об успешной загрузке.

-   `get_chat(share_id: str) -> str`:
    -   **Назначение**: Обрабатывает GET-запросы к `/backend-api/v2/chat/<share_id>` для получения данных диалога.
    -   **Параметры**:
        -   `share_id` (str): Идентификатор общего ресурса.
    -   **Возвращает**: `str`: JSON-ответ с данными диалога.

-   `upload_chat(share_id: str) -> dict`:
    -   **Назначение**: Обрабатывает POST-запросы к `/backend-api/v2/chat/<share_id>` для загрузки данных диалога.
    -   **Параметры**:
        -   `share_id` (str): Идентификатор общего ресурса.
    -   **Возвращает**: `dict`: Словарь с идентификатором общего ресурса.

**Пример**:

```python
from flask import Flask

app = Flask(__name__)
backend_api = Backend_Api(app)

# Пример использования одного из маршрутов, например, получения версии API:
with app.test_request_context('/backend-api/v2/version', method='GET'):
    response = backend_api.get_version()
    print(response)
```

### `Backend_Api.handle_synthesize(self, provider: str)`

**Назначение**: Обрабатывает запросы на синтез речи от определенного провайдера.

**Параметры**:

-   `provider` (str): Название провайдера, который будет использоваться для синтеза речи.

**Возвращает**:

-   `Response`: Flask-response с синтезированной речью или сообщением об ошибке.

**Вызывает исключения**:

-   `ProviderNotFoundError`: Если указанный провайдер не найден.

**Как работает функция**:

1.  Пытается преобразовать имя провайдера в объект провайдера с помощью `convert_to_provider(provider)`.
2.  Если провайдер не найден, возвращает сообщение об ошибке "Provider not found" с кодом 404.
3.  Проверяет, поддерживает ли провайдер метод `synthesize`. Если нет, возвращает сообщение об ошибке "Provider doesn\'t support synthesize" с кодом 500.
4.  Вызывает метод `synthesize` провайдера, передавая параметры запроса.
5.  Если `synthesize` является асинхронной функцией, запускает ее с помощью `asyncio.run()`.
6.  Если `synthesize` возвращает асинхронный итератор, преобразует его в синхронный генератор с помощью `to_sync_generator()`.
7.  Оборачивает генератор в `safe_iter_generator()` для безопасной итерации.
8.  Определяет тип контента ответа из атрибута `synthesize_content_type` провайдера (по умолчанию "application/octet-stream").
9.  Создает Flask-response с данными синтезированной речи и устанавливает заголовок `Content-Type`.
10. Устанавливает заголовок `Cache-Control` для кэширования ответа на 7 дней.
11. Возвращает Flask-response.

**Внутренние функции**:
    Отсутствуют

**Примеры**:

```python
from flask import Flask
from ...client.service import convert_to_provider
from ...providers import Bard

app = Flask(__name__)

def test_handle_synthesize():
    # Mock request arguments
    with app.test_request_context('/handle_synthesize?text=hello', method='GET'):
        backend_api = Backend_Api(app)
        # Mock convert_to_provider
        convert_to_provider = lambda x: Bard
        app.convert_to_provider = convert_to_provider
        # Call the function
        response = backend_api.handle_synthesize(provider="Bard")
        # Assertions
        assert response.status_code == 200
```

### `Backend_Api.get_provider_models(self, provider: str)`

**Назначение**: Возвращает список моделей, поддерживаемых указанным провайдером.

**Параметры**:

-   `provider` (str): Название провайдера, для которого нужно получить список моделей.

**Возвращает**:

-   `list`: Список моделей, поддерживаемых провайдером.
-   `str`: Сообщение об ошибке "Provider not found", если провайдер не найден.

**Как работает функция**:

1.  Получает значения заголовков `x_api_key` и `x_api_base` из запроса.
2.  Вызывает метод `get_provider_models` родительского класса `Api`, передавая имя провайдера, API-ключ и базовый URL.
3.  Если метод возвращает `None`, возвращает сообщение об ошибке "Provider not found" с кодом 404.
4.  Возвращает список моделей, полученный от родительского класса.

**Внутренние функции**:
    Отсутствуют

**Примеры**:

```python
from flask import Flask

app = Flask(__name__)
backend_api = Backend_Api(app)

# Пример вызова с указанием провайдера:
with app.test_request_context('/backend-api/v2/models/openai', method='GET'):
    response = backend_api.get_provider_models(provider='openai')
    print(response)
```

### `Backend_Api._format_json(self, response_type: str, content = None, **kwargs) -> str`

**Назначение**: Форматирует и возвращает JSON-ответ.

**Параметры**:

-   `response_type` (str): Тип ответа.
-   `content`: Содержимое, которое нужно включить в ответ.
-   `**kwargs`: Дополнительные параметры.

**Возвращает**:

-   `str`: JSON-форматированная строка.

**Как работает функция**:

1.  Вызывает метод `_format_json` родительского класса `Api`, передавая тип ответа, содержимое и дополнительные параметры.
2.  Преобразует результат в JSON-форматированную строку с помощью `json.dumps()`.
3.  Добавляет символ новой строки (`\n`) в конец строки.
4.  Возвращает JSON-форматированную строку.

**Внутренние функции**:
    Отсутствуют

**Примеры**:

```python
from flask import Flask

app = Flask(__name__)
backend_api = Backend_Api(app)

# Пример вызова с указанием типа ответа и содержимого:
response = backend_api._format_json(response_type='success', content={'message': 'OK'})
print(response)
```

## Функции

### `safe_iter_generator(generator: Generator) -> Generator`

**Назначение**: Преобразует генератор в безопасный итератор.

**Параметры**:

-   `generator` (Generator): Генератор, который нужно преобразовать.

**Возвращает**:

-   `Generator`: Безопасный итератор.

**Как работает функция**:

1.  Сохраняет первый элемент генератора в переменной `start`.
2.  Определяет внутреннюю функцию `iter_generator`, которая сначала возвращает сохраненный первый элемент, а затем итерируется по остальным элементам исходного генератора.
3.  Возвращает `iter_generator()`.

**Внутренние функции**:

-   `iter_generator()`:
    -   **Назначение**: Итерируется по элементам исходного генератора, сначала возвращая сохраненный первый элемент.
    -   **Параметры**: Отсутствуют.
    -   **Возвращает**: `Generator`: Генератор, возвращающий элементы исходного генератора.

**Примеры**:

```python
def my_generator():
    yield 1
    yield 2
    yield 3

safe_generator = safe_iter_generator(my_generator())
for item in safe_generator:
    print(item)
```

ASCII flowchart:

```
my_generator()
    ↓
safe_iter_generator()
    ↓
start = next(generator)  --- iter_generator()
    ↓                   ↗       ↓
yield start         yield from generator