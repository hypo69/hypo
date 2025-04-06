# Модуль Websim для асинхронного взаимодействия с Websim AI API

## Обзор

Модуль `Websim` предоставляет асинхронный интерфейс для взаимодействия с API Websim AI, позволяя генерировать текст и изображения. Он поддерживает как текстовые запросы (чат), так и запросы на генерацию изображений, используя различные модели, предоставляемые Websim AI.

## Подробней

Модуль предназначен для использования в асинхронных приложениях, требующих интеграции с Websim AI для генерации контента. Он включает в себя методы для формирования запросов, обработки ответов и управления повторными попытками при возникновении ошибок.

## Классы

### `Websim`

**Описание**: Класс `Websim` является асинхронным провайдером, реализующим взаимодействие с Websim AI API.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Аттрибуты**:
- `url` (str): URL Websim AI (`https://websim.ai`).
- `login_url` (str): URL для логина (в данном случае `None`).
- `chat_api_endpoint` (str): URL для API чата (`https://websim.ai/api/v1/inference/run_chat_completion`).
- `image_api_endpoint` (str): URL для API генерации изображений (`https://websim.ai/api/v1/inference/run_image_generation`).
- `working` (bool): Указывает, что провайдер работает (`True`).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (`False`).
- `use_nodriver` (bool): Указывает, использовать ли драйвер (`False`).
- `supports_stream` (bool): Указывает, поддерживает ли стриминг (`False`).
- `supports_system_message` (bool): Указывает, поддерживает ли системные сообщения (`True`).
- `supports_message_history` (bool): Указывает, поддерживает ли историю сообщений (`True`).
- `default_model` (str): Модель, используемая по умолчанию для чата (`gemini-1.5-pro`).
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений (`flux`).
- `image_models` (List[str]): Список моделей для генерации изображений (`['flux']`).
- `models` (List[str]): Список поддерживаемых моделей (`['gemini-1.5-pro', 'gemini-1.5-flash', 'flux']`).

**Методы**:
- `generate_project_id(for_image: bool) -> str`: Генерирует ID проекта в зависимости от типа запроса (чат или изображение).
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, aspect_ratio: str = "1:1", project_id: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для выполнения запросов к API.
- `_handle_image_request(project_id: str, messages: Messages, prompt: str, aspect_ratio: str, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос на генерацию изображений.
- `_handle_chat_request(project_id: str, messages: Messages, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос чата.

## Функции

### `generate_project_id`

```python
    @staticmethod
    def generate_project_id(for_image=False):
        """
        Generate a project ID in the appropriate format
        
        For chat: format like \'ke3_xh5gai3gjkmruomu\'
        For image: format like \'kx0m131_rzz66qb2xoy7\'
        """
```

**Назначение**: Генерирует уникальный идентификатор проекта в зависимости от того, предназначен ли он для запроса изображения или чата.

**Параметры**:
- `for_image` (bool): Если `True`, генерирует ID для запроса изображения, иначе - для чата. По умолчанию `False`.

**Возвращает**:
- `str`: Строка, представляющая сгенерированный ID проекта. Формат ID зависит от значения `for_image`.

**Как работает функция**:

1. **Определение набора символов**:
   - Определяется набор символов, включающий строчные буквы ASCII и цифры, которые будут использоваться для генерации ID.
2. **Генерация ID для изображения**:
   - Если `for_image` равно `True`, генерируется ID, состоящий из двух частей:
     - Первая часть: 7 случайных символов из набора.
     - Вторая часть: 12 случайных символов из набора.
     - Обе части соединяются символом `_`.
3. **Генерация ID для чата**:
   - Если `for_image` равно `False`, генерируется ID, состоящий из двух частей:
     - Префикс: 3 случайных символа из набора.
     - Суффикс: 15 случайных символов из набора.
     - Префикс и суффикс соединяются символом `_`.

```
    Определение символов  
    │
    ├── for_image == True?
    │   ├── Генерация первой части ID (7 символов)
    │   ├── Генерация второй части ID (12 символов)
    │   └── Формирование ID: первая_часть + "_" + вторая_часть
    │
    └── for_image == False?
        ├── Генерация префикса (3 символа)
        ├── Генерация суффикса (15 символов)
        └── Формирование ID: префикс + "_" + суффикс
```

**Примеры**:

```python
# Пример генерации ID для изображения
project_id_image = Websim.generate_project_id(for_image=True)
print(f"ID проекта для изображения: {project_id_image}")

# Пример генерации ID для чата
project_id_chat = Websim.generate_project_id(for_image=False)
print(f"ID проекта для чата: {project_id_chat}")
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        prompt: str = None,
        proxy: str = None,
        aspect_ratio: str = "1:1",
        project_id: str = None,
        **kwargs
    ) -> AsyncResult:
        """

        """
```

**Назначение**: Создает асинхронный генератор для обработки запросов к API Websim AI.

**Параметры**:
- `cls`: Ссылка на класс `Websim`.
- `model` (str): Модель для использования (например, `gemini-1.5-pro` или `flux`).
- `messages` (Messages): Список сообщений для отправки в API.
- `prompt` (str, optional): Дополнительный промпт для запроса. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон для генерации изображений. По умолчанию `"1:1"`.
- `project_id` (str, optional): ID проекта для использования. Если не указан, генерируется автоматически. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, передаваемые в функции обработки запросов.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты из API Websim AI.

**Как работает функция**:

1. **Определение типа запроса**:
   - Проверяет, является ли запрос запросом изображения, сравнивая `model` со списком `cls.image_models`.
2. **Генерация ID проекта**:
   - Если `project_id` не указан, он генерируется с использованием `cls.generate_project_id` в зависимости от типа запроса.
3. **Формирование заголовков**:
   - Определяет заголовки HTTP-запроса, включая `accept`, `accept-language`, `content-type`, `origin`, `user-agent` и `websim-flags;`.
   - Для запросов изображений добавляет `referer`.
4. **Обработка запроса**:
   - Если это запрос изображения (`is_image_request` равно `True`):
     - Устанавливает `referer` для API генерации изображений.
     - Вызывает `cls._handle_image_request` для обработки запроса изображения, передавая необходимые параметры.
     - Передает результаты, возвращаемые генератором `cls._handle_image_request`.
   - Если это запрос чата (`is_image_request` равно `False`):
     - Устанавливает `referer` для API чата.
     - Вызывает `cls._handle_chat_request` для обработки запроса чата, передавая необходимые параметры.
     - Передает результаты, возвращаемые генератором `cls._handle_chat_request`.

```
    Определение типа запроса (изображение или чат)
    │
    ├── project_id указан?
    │   └── Нет: Генерация project_id
    │
    ├── Формирование заголовков HTTP
    │
    ├── Запрос изображения?
    │   ├── Вызов _handle_image_request
    │   └── Передача результатов
    │
    └── Запрос чата?
        ├── Вызов _handle_chat_request
        └── Передача результатов
```

**Примеры**:

```python
# Пример создания асинхронного генератора для чата
messages = [{"role": "user", "content": "Hello, Websim!"}]
async_generator_chat = Websim.create_async_generator(model="gemini-1.5-pro", messages=messages)

# Пример создания асинхронного генератора для изображения
messages = [{"role": "user", "content": "A beautiful landscape"}]
async_generator_image = Websim.create_async_generator(model="flux", messages=messages)
```

### `_handle_image_request`

```python
    @classmethod
    async def _handle_image_request(
        cls,
        project_id: str,
        messages: Messages,
        prompt: str,
        aspect_ratio: str,
        headers: dict,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """

        """
```

**Назначение**: Обрабатывает запрос на генерацию изображения, отправляя запрос к API Websim AI и возвращая URL изображения.

**Параметры**:
- `cls`: Ссылка на класс `Websim`.
- `project_id` (str): ID проекта для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `prompt` (str): Промпт для генерации изображения.
- `aspect_ratio` (str): Соотношение сторон изображения.
- `headers` (dict): Заголовки HTTP-запроса.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объект `ImageResponse` с URL изображения и альтернативным текстом.

**Как работает функция**:

1. **Форматирование промпта**:
   - Использует функцию `format_image_prompt` для формирования промпта на основе `messages` и `prompt`.
2. **Создание сессии**:
   - Создает асинхронную сессию `ClientSession` с заданными заголовками.
3. **Формирование данных запроса**:
   - Создает словарь `data`, включающий `project_id`, `prompt` (отформатированный) и `aspect_ratio`.
4. **Отправка запроса**:
   - Отправляет `POST` запрос к `cls.image_api_endpoint` с использованием `session.post`, передавая `data` в формате JSON и `proxy`.
5. **Обработка ответа**:
   - Вызывает `raise_for_status` для проверки статуса ответа.
   - Читает текст ответа и преобразует его в JSON.
   - Извлекает URL изображения из JSON (`response_json.get("url")`).
6. **Генерация результата**:
   - Если URL изображения получен, создает объект `ImageResponse` с URL и `used_prompt` в качестве альтернативного текста.
   - Передает объект `ImageResponse` через генератор.

```
    Форматирование промпта
    │
    ├── Создание асинхронной сессии
    │
    ├── Формирование данных запроса (project_id, prompt, aspect_ratio)
    │
    ├── Отправка POST запроса к image_api_endpoint
    │
    ├── Обработка ответа
    │   ├── Проверка статуса ответа
    │   ├── Чтение и преобразование JSON
    │   └── Извлечение URL изображения
    │
    └── Генерация и возврат ImageResponse
```

**Примеры**:

```python
# Пример обработки запроса изображения
project_id = "kx0m131_rzz66qb2xoy7"
messages = [{"role": "user", "content": "A futuristic cityscape"}]
prompt = "High quality, detailed"
aspect_ratio = "16:9"
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://websim.ai',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'websim-flags;': ''
}

async def process_image_request():
    async for result in Websim._handle_image_request(
        project_id=project_id,
        messages=messages,
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        headers=headers
    ):
        print(result)

asyncio.run(process_image_request())
```

### `_handle_chat_request`

```python
    @classmethod
    async def _handle_chat_request(
        cls,
        project_id: str,
        messages: Messages,
        headers: dict,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """

        """
```

**Назначение**: Обрабатывает запрос чата, отправляя сообщения в API Websim AI и возвращая ответ.

**Параметры**:
- `cls`: Ссылка на класс `Websim`.
- `project_id` (str): ID проекта для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `headers` (dict): Заголовки HTTP-запроса.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текстовый контент ответа от API Websim AI.

**Как работает функция**:

1. **Настройка повторных попыток**:
   - Устанавливает максимальное количество повторных попыток (`max_retries = 3`) и счетчик попыток (`retry_count = 0`).
   - Инициализирует переменную `last_error` для хранения последней ошибки.
2. **Цикл повторных попыток**:
   - Выполняет цикл, пока `retry_count` меньше `max_retries`.
3. **Создание сессии**:
   - Создает асинхронную сессию `ClientSession` с заданными заголовками.
4. **Формирование данных запроса**:
   - Создает словарь `data`, включающий `project_id` и `messages`.
5. **Отправка запроса**:
   - Отправляет `POST` запрос к `cls.chat_api_endpoint` с использованием `session.post`, передавая `data` в формате JSON и `proxy`.
6. **Обработка ответа**:
   - Проверяет статус ответа:
     - Если статус `429` (Rate limit exceeded):
       - Читает текст ответа, создает исключение `ResponseStatusError` и увеличивает счетчик `retry_count`.
       - Если `retry_count` меньше `max_retries`, ждет `2 ** retry_count` секунд перед повторной попыткой.
       - Если `retry_count` достиг `max_retries`, выбрасывает последнее исключение `last_error`.
     - Если статус не `429`, вызывает `raise_for_status` для проверки статуса ответа.
   - Читает текст ответа и пытается преобразовать его в JSON.
   - Извлекает контент из JSON (`response_json.get("content", "")`) и передает его через генератор, удаляя пробелы с обеих сторон (`content.strip()`).
   - Прерывает цикл, если контент успешно получен.
7. **Обработка исключений**:
   - Обрабатывает исключение `ResponseStatusError`:
     - Если ошибка содержит "Rate limit exceeded" и `retry_count` меньше `max_retries`, увеличивает `retry_count` и ждет перед повторной попыткой.
     - Если `retry_count` достиг `max_retries`, выбрасывает исключение.
   - Обрабатывает любые другие исключения, выбрасывая их.

```
    Настройка повторных попыток
    │
    ├── Цикл повторных попыток
    │   ├── Создание асинхронной сессии
    │   ├── Формирование данных запроса (project_id, messages)
    │   ├── Отправка POST запроса к chat_api_endpoint
    │   ├── Обработка ответа
    │   │   ├── Статус == 429 (Rate limit)?
    │   │   │   ├── Увеличение retry_count
    │   │   │   ├── Ожидание перед повторной попыткой
    │   │   │   └── Если достигнут max_retries, выброс исключения
    │   │   └── Проверка статуса ответа (raise_for_status)
    │   │   ├── Чтение и преобразование JSON
    │   │   └── Извлечение контента
    │   └── Обработка исключений
    │       ├── ResponseStatusError (Rate limit)?
    │       │   ├── Увеличение retry_count
    │       │   ├── Ожидание перед повторной попыткой
    │       │   └── Если достигнут max_retries, выброс исключения
    │       └── Другие исключения: выброс исключения
    │
    └── Возврат контента через генератор
```

**Примеры**:

```python
# Пример обработки запроса чата
project_id = "ke3_xh5gai3gjkmruomu"
messages = [{"role": "user", "content": "Как дела?"}]
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://websim.ai',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'websim-flags;': ''
}

async def process_chat_request():
    async for result in Websim._handle_chat_request(
        project_id=project_id,
        messages=messages,
        headers=headers
    ):
        print(result)

asyncio.run(process_chat_request())