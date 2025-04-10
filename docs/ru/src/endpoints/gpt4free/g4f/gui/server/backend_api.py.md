# Модуль backend_api.py

## Обзор

Модуль `backend_api.py` является частью проекта `hypotez` и предназначен для обработки различных эндпоинтов Flask-приложения, обеспечивающих взаимодействие с моделями, провайдерами и обработку различных функций, таких как работа с чатами, обработка ошибок и управление версиями.

## Подробней

Этот модуль содержит класс `Backend_Api`, который наследует класс `Api` и предоставляет методы для обработки HTTP-запросов, связанных с получением моделей, провайдеров, синтезом речи, управлением файлами и другими серверными операциями.
Он также включает в себя функциональность для работы с кэшем чатов, загрузкой и получением файлов cookie, а также интеграцию с внешними сервисами, такими как `mem0` для управления памятью пользователей.

## Классы

### `Backend_Api`

**Описание**:
Класс `Backend_Api` обрабатывает различные эндпоинты Flask-приложения для выполнения серверных операций. Он предоставляет методы для взаимодействия с моделями, провайдерами, а также для обработки различных функций, таких как работа с чатами, обработка ошибок и управление версиями.

**Наследует**:
`Api`

**Атрибуты**:
- `app` (Flask): Экземпляр Flask-приложения.
- `routes` (dict): Словарь, отображающий API-эндпоинты на соответствующие обработчики.
- `chat_cache` (dict): Кэш для хранения данных чатов.

**Методы**:

- `__init__(self, app: Flask) -> None`: Инициализирует API backend с заданным Flask-приложением.
- `handle_synthesize(self, provider: str)`: Обрабатывает запрос на синтез речи от указанного провайдера.
- `get_provider_models(self, provider: str)`: Получает список моделей, поддерживаемых указанным провайдером.
- `_format_json(self, response_type: str, content = None, **kwargs) -> str`: Форматирует и возвращает JSON-ответ.

## Функции

### `safe_iter_generator`

```python
def safe_iter_generator(generator: Generator) -> Generator:
    """
    Создает безопасный итератор-генератор.

    Args:
        generator (Generator): Исходный генератор.

    Returns:
        Generator: Безопасный итератор-генератор.

    Как работает функция:
    1. Получает первый элемент из исходного генератора.
    2. Определяет внутреннюю функцию iter_generator, которая сначала возвращает первый элемент,
       а затем итерируется по остальным элементам исходного генератора.
    3. Возвращает iter_generator.

    ASCII схема:
    Исходный генератор
        ↓
    Получение первого элемента (start)
        ↓
    Определение внутренней функции iter_generator (возвращает start, затем остаток генератора)
        ↓
    Возврат iter_generator

    Примеры:
    >>> def my_generator():
    ...     yield 1
    ...     yield 2
    ...     yield 3
    >>> safe_gen = safe_iter_generator(my_generator())
    >>> list(safe_gen)
    [1, 1, 2, 3]
    """
```

### `Backend_Api.__init__`

```python
    def __init__(self, app: Flask) -> None:
        """
        Инициализирует API backend с заданным Flask-приложением.

        Args:
            app (Flask): Flask application instance to attach routes to.
        """
```

**Назначение**:
Инициализация экземпляра класса `Backend_Api`.

**Параметры**:
- `app` (Flask): Экземпляр Flask-приложения, к которому будут привязаны маршруты.

**Как работает функция**:
1. Устанавливает переданное Flask-приложение в качестве атрибута `app` текущего экземпляра класса.
2. Инициализирует пустой словарь `chat_cache` для хранения данных чатов.
3. Определяет маршруты для различных эндпоинтов, используя декоратор `@app.route`.
   - Маршрут `/` (GET): отображает шаблоны `demo.html` или `home.html` в зависимости от значения `app.demo`.
   - Маршрут `/qrcode` и `/qrcode/<conversation_id>` (GET): отображает шаблон `qrcode.html` с параметрами `conversation_id` и `share_url`.
   - Маршруты `/backend-api/v2/models`, `/backend-api/v2/models/<provider>` и `/backend-api/v2/providers` (GET): возвращают JSON-ответы, содержащие модели и провайдеры, в зависимости от конфигурации приложения.
   - Маршрут `/backend-api/v2/conversation` (POST): обрабатывает запросы разговоров и возвращает потоковые ответы.
   - Маршруты `/backend-api/v2/usage` и `/backend-api/v2/log` (POST): добавляют данные об использовании и логи в файлы.
   - Маршруты `/backend-api/v2/memory/<user_id>` (POST, GET): управляют памятью пользователей с использованием внешнего клиента `mem0`.
   - Маршруты `/backend-api/v2/files/<bucket_id>` (GET, DELETE, POST): управляют файлами в бакетах.
   - Маршруты `/files/<bucket_id>/media/<filename>` (GET) и `/search/<search>` (GET): служат для получения медиа-файлов и поиска медиа-файлов.
   - Маршрут `/backend-api/v2/upload_cookies` (POST): загружает файлы cookie.
   - Маршруты `/backend-api/v2/chat/<share_id>` (GET, POST): управляют данными чатов.
4. Определяет словарь `routes`, который связывает маршруты с соответствующими функциями и методами.

**Пример**:
```python
app = Flask(__name__)
backend_api = Backend_Api(app)
```

### `Backend_Api.handle_conversation`

```python
        def handle_conversation():
            """
            Обрабатывает запросы на разговор и передает ответы обратно потоком.

            Returns:
                Response: Объект Flask Response для потоковой передачи.
            """
```

**Назначение**:
Обрабатывает запросы на разговор и возвращает ответы потоком.

**Возвращает**:
- `Response`: Объект Flask Response для потоковой передачи.

**Как работает функция**:
1. Извлекает данные JSON из формы запроса или тела запроса.
2. Если в запросе есть файлы, добавляет их в данные JSON.
3. Если приложение находится в демонстрационном режиме и не указан провайдер, выбирает случайного провайдера.
4. Подготавливает аргументы для запроса к провайдеру.
5. Создает поток ответов и возвращает объект Flask Response.

### `Backend_Api.get_demo_models`

```python
        def get_demo_models():
            """
            Возвращает список демонстрационных моделей.

            Returns:
                list: Список демонстрационных моделей.
            """
```

**Назначение**:
Возвращает список демонстрационных моделей.

**Возвращает**:
- `list`: Список демонстрационных моделей, каждая из которых содержит информацию о названии, типе (изображение или зрение), провайдерах и флаге demo.

**Как работает функция**:
1. Итерируется по значениям словаря `models.demo_models`, где каждое значение представляет собой кортеж из модели и списка провайдеров.
2. Для каждой модели и провайдеров извлекает необходимые атрибуты (имя модели, тип изображения/зрения, имя провайдера).
3. Формирует словарь с информацией о модели и провайдерах.
4. Возвращает список этих словарей.

### `Backend_Api.add_usage`

```python
        @app.route(\'/backend-api/v2/usage\', methods=[\'POST\'])\n        def add_usage():
            """
            Добавляет информацию об использовании в файл лога.

            Returns:
                dict: Пустой словарь.
            """
```

**Назначение**:
Добавляет информацию об использовании в файл лога.

**Возвращает**:
- `dict`: Пустой словарь.

**Как работает функция**:
1. Определяет путь к директории и файлу кэша, где будет храниться информация об использовании.
2. Создает директорию кэша, если она не существует.
3. Открывает файл кэша (или создает его, если он не существует) в режиме добавления.
4. Записывает данные JSON из запроса в файл.
5. Возвращает пустой словарь.

### `Backend_Api.add_log`

```python
        @app.route(\'/backend-api/v2/log\', methods=[\'POST\'])\n        def add_log():
            """
            Добавляет информацию о логе в файл лога.

            Returns:
                dict: Пустой словарь.
            """
```

**Назначение**:
Добавляет информацию о логе в файл лога.

**Возвращает**:
- `dict`: Пустой словарь.

**Как работает функция**:
1. Определяет путь к директории и файлу кэша, где будет храниться информация о логе.
2. Создает директорию кэша, если она не существует.
3. Получает заголовок "origin" из запроса и объединяет его с данными JSON из тела запроса.
4. Открывает файл кэша (или создает его, если он не существует) в режиме добавления.
5. Записывает объединенные данные в файл в формате JSON.
6. Возвращает пустой словарь.

### `Backend_Api.add_memory`

```python
        @app.route(\'/backend-api/v2/memory/<user_id>\', methods=[\'POST\'])\n        def add_memory(user_id: str):
            """
            Добавляет элементы в память пользователя.

            Args:
                user_id (str): ID пользователя.

            Returns:
                dict: Словарь с количеством добавленных элементов.
            """
```

**Назначение**:
Добавляет элементы в память пользователя с использованием внешнего клиента `mem0`.

**Параметры**:
- `user_id` (str): ID пользователя, для которого добавляются элементы в память.

**Возвращает**:
- `dict`: Словарь с ключом "count", содержащим количество добавленных элементов.

**Как работает функция**:
1. Получает API-ключ из заголовка запроса `x_api_key`.
2. Извлекает данные JSON из тела запроса.
3. Импортирует класс `MemoryClient` из модуля `mem0`.
4. Создает экземпляр `MemoryClient` с использованием полученного API-ключа.
5. Добавляет элементы в память пользователя, преобразуя элементы из `json_data.get("items")` в формат, требуемый для `MemoryClient.add`.
6. Возвращает словарь с количеством добавленных элементов.

### `Backend_Api.read_memory`

```python
        @app.route(\'/backend-api/v2/memory/<user_id>\', methods=[\'GET\'])\n        def read_memory(user_id: str):
            """
            Читает память пользователя.

            Args:
                user_id (str): ID пользователя.

            Returns:
                dict: Данные из памяти пользователя.
            """
```

**Назначение**:
Читает память пользователя с использованием внешнего клиента `mem0`.

**Параметры**:
- `user_id` (str): ID пользователя, память которого нужно прочитать.

**Возвращает**:
- `dict`: Данные из памяти пользователя, полученные из `MemoryClient`.

**Как работает функция**:
1. Получает API-ключ из заголовка запроса `x_api_key`.
2. Импортирует класс `MemoryClient` из модуля `mem0`.
3. Создает экземпляр `MemoryClient` с использованием полученного API-ключа.
4. Проверяет, есть ли параметр `search` в аргументах запроса.
   - Если параметр `search` присутствует, выполняет поиск по памяти пользователя с использованием `client.search` и возвращает результаты поиска.
   - Если параметр `search` отсутствует, получает все записи из памяти пользователя с использованием `client.get_all` и возвращает их.

### `Backend_Api.create`

```python
        @app.route(\'/backend-api/v2/create\', methods=[\'GET\', \'POST\'])\n        def create():
            """
            Создает ответ на основе запроса.

            Returns:
                Response: Объект Flask Response с результатом.
            """
```

**Назначение**:
Создает ответ на основе запроса, используя инструменты (tool_calls) и фильтры markdown.

**Возвращает**:
- `Response`: Объект Flask Response с результатом в виде потока текста или JSON в случае ошибки.

**Как работает функция**:
1. Определяет список инструментов (`tool_calls`) для вызова. Всегда включает инструмент `bucket_tool`.
2. Если в запросе есть параметр `web_search`, добавляет инструмент `search_tool` с параметрами запроса.
3. Получает параметры из запроса, такие как `model`, `messages`, `provider`, `stream`, `ignore_stream`, `tool_calls`.
4. Если указан `cache_id`, пытается получить результат из кэша. Если в кэше нет, вызывает `iter_run_tools` для создания ответа и сохраняет его в кэш.
5. Если `cache_id` не указан, вызывает `iter_run_tools` для создания ответа.
6. Если указан `do_filter_markdown`, фильтрует результат с помощью `filter_markdown` и возвращает отфильтрованный текст.
7. Если `do_filter_markdown` не указан, преобразует поток ответов в поток строк и возвращает его.
8. В случае возникновения исключения логирует ошибку и возвращает JSON с информацией об ошибке.

### `Backend_Api.manage_files`

```python
        @app.route(\'/backend-api/v2/files/<bucket_id>\', methods=[\'GET\', \'DELETE\'])\n        def manage_files(bucket_id: str):
            """
            Управляет файлами в бакете.

            Args:
                bucket_id (str): ID бакета.

            Returns:
                Response: Объект Flask Response с результатом.
            """
```

**Назначение**:
Управляет файлами в указанном бакете. Поддерживает удаление бакета и получение содержимого бакета в виде потока.

**Параметры**:
- `bucket_id` (str): ID бакета, для которого выполняется управление файлами.

**Возвращает**:
- `Response`: Объект Flask Response с результатом операции. В случае GET-запроса возвращает поток данных из бакета, в случае DELETE-запроса возвращает сообщение об успешном удалении. В случае ошибки возвращает JSON с информацией об ошибке.

**Как работает функция**:
1. Очищает `bucket_id` с помощью `secure_filename`.
2. Определяет директорию бакета с помощью `get_bucket_dir`.
3. Проверяет, существует ли директория бакета. Если не существует, возвращает JSON с ошибкой.
4. Если метод запроса `DELETE`, пытается удалить директорию бакета. В случае успеха возвращает JSON с сообщением об успехе, в случае ошибки возвращает JSON с информацией об ошибке.
5. Если метод запроса `GET`, получает параметры запроса `delete_files`, `refine_chunks_with_spacy` и `event_stream`.
6. Возвращает `Response` с потоком данных из бакета, используя функцию `get_streaming`.

### `Backend_Api.upload_files`

```python
        @self.app.route(\'/backend-api/v2/files/<bucket_id>\', methods=[\'POST\'])\n        def upload_files(bucket_id: str):
            """
            Загружает файлы в бакет.

            Args:
                bucket_id (str): ID бакета.

            Returns:
                dict: Словарь с информацией о загруженных файлах.
            """
```

**Назначение**:
Загружает файлы в указанный бакет.

**Параметры**:
- `bucket_id` (str): ID бакета, в который загружаются файлы.

**Возвращает**:
- `dict`: Словарь с информацией о загруженных файлах, включая `bucket_id`, список файлов (`files`) и список медиа-файлов (`media`).

**Как работает функция**:
1. Очищает `bucket_id` с помощью `secure_filename`.
2. Определяет директорию бакета с помощью `get_bucket_dir`.
3. Создает директорию бакета и поддиректорию `media`, если они не существуют.
4. Итерируется по списку файлов, переданных в запросе.
5. Для каждого файла очищает имя файла с помощью `secure_filename`.
6. Проверяет расширение файла с помощью `is_allowed_extension`. Если расширение разрешено, сохраняет файл в поддиректорию `media`. Если расширение не разрешено, проверяет, поддерживается ли имя файла с помощью `supports_filename`. Если имя файла поддерживается, сохраняет файл в директорию бакета.
7. Записывает список загруженных файлов в файл `files.txt` в директории бакета.
8. Возвращает словарь с информацией о загруженных файлах.

### `Backend_Api.get_media`

```python
        @app.route(\'/files/<bucket_id>/media/<filename>\', methods=[\'GET\'])\n        def get_media(bucket_id, filename, dirname: str = None):
            """
            Возвращает медиа-файл из бакета.

            Args:
                bucket_id (str): ID бакета.
                filename (str): Имя файла.
                dirname (str, optional): Имя директории. Defaults to None.

            Returns:
                Response: Объект Flask Response с медиа-файлом.
            """
```

**Назначение**:
Возвращает медиа-файл из указанного бакета.

**Параметры**:
- `bucket_id` (str): ID бакета, из которого нужно получить медиа-файл.
- `filename` (str): Имя медиа-файла, который нужно получить.
- `dirname` (str, optional): Имя директории. По умолчанию `None`.

**Возвращает**:
- `Response`: Объект Flask Response с медиа-файлом. Если файл не найден и указан `source_url` в параметрах запроса, выполняет перенаправление на `source_url`.

**Как работает функция**:
1. Определяет директорию медиа-файлов с помощью `get_bucket_dir`.
2. Пытается вернуть медиа-файл с помощью `send_from_directory`.
3. Если файл не найден, пытается получить `source_url` из параметров запроса.
4. Если `source_url` получен, выполняет перенаправление на `source_url`.
5. Если `source_url` не получен, вызывает исключение `NotFound`.

### `Backend_Api.find_media`

```python
        @app.route(\'/search/<search>\', methods=[\'GET\'])\n        def find_media(search: str):
            """
            Ищет медиа-файлы.

            Args:
                search (str): Параметр поиска.

            Returns:
                Response: Объект Flask Response с перенаправлением на найденный медиа-файл.
            """
```

**Назначение**:
Ищет медиа-файлы на основе поискового запроса.

**Параметры**:
- `search` (str): Поисковый запрос.

**Возвращает**:
- `Response`: Объект Flask Response с перенаправлением на найденный медиа-файл.

**Как работает функция**:
1. Очищает поисковый запрос с помощью `secure_filename`.
2. Проверяет наличие прав на чтение директории с изображениями.
3. Выполняет поиск медиа-файлов в директории с изображениями.
4. Возвращает перенаправление на найденный медиа-файл.

### `Backend_Api.upload_cookies`

```python
        @app.route(\'/backend-api/v2/upload_cookies\', methods=[\'POST\'])\n        def upload_cookies():
            """
            Загружает файлы cookie.

            Returns:
                str: Сообщение об успешной загрузке или ошибке.
            """
```

**Назначение**:
Загружает файлы cookie на сервер.

**Возвращает**:
- `str`: Сообщение об успешной загрузке или ошибке.

**Как работает функция**:
1. Получает файл из запроса.
2. Проверяет имя файла на соответствие разрешенным расширениям (.json или .har).
3. Сохраняет файл в директорию с cookie.
4. Возвращает сообщение об успехе или ошибке.

### `Backend_Api.get_chat`

```python
        @self.app.route(\'/backend-api/v2/chat/<share_id>\', methods=[\'GET\'])\n        def get_chat(share_id: str) -> str:
            """
            Получает данные чата по share_id.

            Args:
                share_id (str): ID чата.

            Returns:
                str: Данные чата в формате JSON.
            """
```

**Назначение**:
Получает данные чата по `share_id`.

**Параметры**:
- `share_id` (str): ID чата.

**Возвращает**:
- `str`: Данные чата в формате JSON.

**Как работает функция**:
1. Очищает `share_id` с помощью `secure_filename`.
2. Проверяет, не был ли чат изменен с момента последнего запроса.
3. Читает данные чата из файла `chat.json`.
4. Возвращает данные чата в формате JSON.

### `Backend_Api.upload_chat`

```python
        @self.app.route(\'/backend-api/v2/chat/<share_id>\', methods=[\'POST\'])\n        def upload_chat(share_id: str) -> dict:
            """
            Загружает данные чата.

            Args:
                share_id (str): ID чата.

            Returns:
                dict: Словарь с share_id.
            """
```

**Назначение**:
Загружает данные чата на сервер.

**Параметры**:
- `share_id` (str): ID чата.

**Возвращает**:
- `dict`: Словарь с `share_id`.

**Как работает функция**:
1. Извлекает данные чата из запроса.
2. Проверяет, не устарели ли данные чата.
3. Очищает `share_id` с помощью `secure_filename`.
4. Сохраняет данные чата в файл `chat.json`.
5. Возвращает словарь с `share_id`.

### `Backend_Api.handle_synthesize`

```python
    def handle_synthesize(self, provider: str):
        """
        Обрабатывает запрос на синтез речи от указанного провайдера.

        Args:
            provider (str): Имя провайдера.

        Returns:
            Response: Объект Flask Response с синтезированной речью.
        """
```

**Назначение**:
Обрабатывает запрос на синтез речи от указанного провайдера.

**Параметры**:
- `provider` (str): Имя провайдера, который будет использоваться для синтеза речи.

**Возвращает**:
- `Response`: Объект Flask Response с синтезированной речью.

**Вызывает исключения**:
- `ProviderNotFoundError`: Если указанный провайдер не найден.

**Как работает функция**:
1. Преобразует имя провайдера в объект провайдера с помощью `convert_to_provider`.
2. Проверяет, поддерживает ли провайдер функцию синтеза речи.
3. Вызывает функцию синтеза речи провайдера с параметрами запроса.
4. Преобразует результат синтеза речи в поток данных.
5. Создает объект Flask Response с потоком данных и типом контента.
6. Устанавливает заголовок `Cache-Control` для кэширования ответа.
7. Возвращает объект Flask Response.

### `Backend_Api.get_provider_models`

```python
    def get_provider_models(self, provider: str):
        """
        Получает список моделей, поддерживаемых указанным провайдером.

        Args:
            provider (str): Имя провайдера.

        Returns:
            list: Список моделей, поддерживаемых провайдером.
        """
```

**Назначение**:
Получает список моделей, поддерживаемых указанным провайдером.

**Параметры**:
- `provider` (str): Имя провайдера, для которого нужно получить список моделей.

**Возвращает**:
- `list`: Список моделей, поддерживаемых провайдером.

**Как работает функция**:
1. Получает API-ключ и API-базу из заголовков запроса.
2. Вызывает метод `get_provider_models` родительского класса `Api` для получения списка моделей.
3. Если список моделей не найден, возвращает сообщение об ошибке.
4. Возвращает список моделей.

### `Backend_Api._format_json`

```python
    def _format_json(self, response_type: str, content = None, **kwargs) -> str:
        """
        Форматирует и возвращает JSON-ответ.

        Args:
            response_type (str): The type of the response.
            content: The content to be included in the response.

        Returns:
            str: A JSON formatted string.
        """
```

**Назначение**:
Форматирует и возвращает JSON-ответ.

**Параметры**:
- `response_type` (str): Тип ответа.
- `content`: Содержимое ответа.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: JSON-строка.

**Как работает функция**:
1. Вызывает метод `_format_json` родительского класса `Api` для форматирования ответа.
2. Преобразует отформатированный ответ в JSON-строку с помощью `json.dumps`.
3. Добавляет символ новой строки в конец JSON-строки.
4. Возвращает JSON-строку.