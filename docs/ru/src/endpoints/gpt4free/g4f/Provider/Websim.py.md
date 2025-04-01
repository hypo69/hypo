# Модуль Websim для работы с AI-сервисом Websim.ai

## Обзор

Модуль `Websim` предоставляет асинхронный интерфейс для взаимодействия с AI-сервисом [Websim.ai](https://websim.ai). Он включает в себя функциональность для генерации текста и изображений на основе предоставленных сообщений и параметров. Модуль поддерживает работу через прокси и предоставляет методы для обработки запросов к API чата и API генерации изображений Websim.ai.

## Подробнее

Этот модуль предназначен для интеграции с сервисом Websim.ai, который предоставляет услуги AI, такие как чат-боты и генерация изображений. Он использует асинхронные запросы для неблокирующего взаимодействия с API сервиса. Модуль автоматически генерирует идентификаторы проектов и обрабатывает ответы от API, возвращая результаты в формате, пригодном для дальнейшей обработки.

## Классы

### `Websim`

**Описание**: Класс `Websim` является асинхронным провайдером для работы с AI-сервисом Websim.ai.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Добавляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса Websim.ai.
- `login_url` (str | None): URL для логина (в данном случае `None`).
- `chat_api_endpoint` (str): URL API для взаимодействия с чат-ботом.
- `image_api_endpoint` (str): URL API для генерации изображений.
- `working` (bool): Указывает, что провайдер работает.
- `needs_auth` (bool): Указывает, требуется ли аутентификация (в данном случае `False`).
- `use_nodriver` (bool): Определяет, использовать ли драйвер (в данном случае `False`).
- `supports_stream` (bool): Указывает, поддерживает ли потоковую передачу данных (в данном случае `False`).
- `supports_system_message` (bool): Указывает, поддерживает ли системные сообщения (в данном случае `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли историю сообщений (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию для чата (`'gemini-1.5-pro'`).
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений (`'flux'`).
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `models` (List[str]): Список всех поддерживаемых моделей (чат и изображения).

**Методы**:
- `generate_project_id(for_image: bool = False) -> str`: Генерирует идентификатор проекта в зависимости от типа запроса (чат или изображение).
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, aspect_ratio: str = "1:1", project_id: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для обработки запросов к API Websim.ai.
- `_handle_image_request(project_id: str, messages: Messages, prompt: str, aspect_ratio: str, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос на генерацию изображения.
- `_handle_chat_request(project_id: str, messages: Messages, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос к чат-боту.

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

**Назначение**: Генерирует идентификатор проекта в нужном формате.

**Параметры**:
- `for_image` (bool): Если `True`, генерирует идентификатор для запроса изображения, иначе - для запроса чата. По умолчанию `False`.

**Возвращает**:
- `str`: Сгенерированный идентификатор проекта.

**Как работает функция**:
1. Определяет набор символов для генерации идентификатора (строчные буквы и цифры).
2. Если `for_image` равен `True`, генерирует идентификатор в формате `'kx0m131_rzz66qb2xoy7'`, иначе - в формате `'ke3_xh5gai3gjkmruomu'`.
3. Возвращает сгенерированный идентификатор.

```
for_image = False
|
Определение символов для ID
|
Генерация ID для чата
|
Возврат ID
```

**Примеры**:

```python
>>> Websim.generate_project_id()
'abc_123xyz456def789'

>>> Websim.generate_project_id(for_image=True)
'abc1234_xyz56789012'
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
        ...
```

**Назначение**: Создает асинхронный генератор для выполнения запросов к Websim.ai.

**Параметры**:
- `model` (str): Модель для использования (например, `'gemini-1.5-pro'` или `'flux'`).
- `messages` (Messages): Список сообщений для отправки.
- `prompt` (str, optional): Дополнительный текст запроса. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения (например, `'1:1'`). По умолчанию `'1:1'`.
- `project_id` (str, optional): Идентификатор проекта. Если не указан, генерируется автоматически. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты запроса.

**Как работает функция**:
1. Определяет, является ли запрос запросом изображения на основе выбранной модели.
2. Если `project_id` не указан, генерирует новый с использованием `generate_project_id`.
3. Формирует заголовки запроса, включая `referer` в зависимости от типа запроса (чат или изображение).
4. Вызывает `_handle_image_request` для запросов изображений или `_handle_chat_request` для запросов чата, передавая необходимые параметры.
5. Передает результаты, полученные от этих обработчиков, через асинхронный генератор.

```
Определение типа запроса (изображение/чат)
|
Генерация project_id, если не предоставлен
|
Установка заголовков запроса
|
Вызов _handle_image_request или _handle_chat_request
|
Генерация результата
```

**Примеры**:

```python
# Пример для запроса чата
messages = [{"role": "user", "content": "Hello!"}]
async for result in Websim.create_async_generator(model='gemini-1.5-pro', messages=messages):
    print(result)

# Пример для запроса генерации изображения
messages = [{"role": "user", "content": "A cat"}]
async for result in Websim.create_async_generator(model='flux', messages=messages, prompt="A cat with sunglasses"):
    print(result)
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
        ...
```

**Назначение**: Обрабатывает запрос на генерацию изображения.

**Параметры**:
- `project_id` (str): Идентификатор проекта.
- `messages` (Messages): Список сообщений.
- `prompt` (str): Текст запроса.
- `aspect_ratio` (str): Соотношение сторон изображения.
- `headers` (dict): Заголовки запроса.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий URL изображения.

**Как работает функция**:
1. Форматирует текст запроса с использованием `format_image_prompt`.
2. Отправляет POST-запрос к `image_api_endpoint` с данными, содержащими `project_id`, отформатированный текст запроса и `aspect_ratio`.
3. Обрабатывает ответ от API, извлекает URL изображения из JSON-ответа.
4. Возвращает объект `ImageResponse` с URL изображения и текстом запроса.

```
Форматирование текста запроса
|
Отправка POST-запроса к image_api_endpoint
|
Извлечение URL изображения из JSON-ответа
|
Возврат ImageResponse
```

**Примеры**:

```python
# Пример вызова (внутри create_async_generator)
project_id = "abc123xyz"
messages = [{"role": "user", "content": "A cat"}]
prompt = "A cat with sunglasses"
aspect_ratio = "1:1"
headers = {"Content-Type": "application/json"}

async for result in Websim._handle_image_request(project_id, messages, prompt, aspect_ratio, headers):
    print(result)
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
        ...
```

**Назначение**: Обрабатывает запрос к чат-боту.

**Параметры**:
- `project_id` (str): Идентификатор проекта.
- `messages` (Messages): Список сообщений.
- `headers` (dict): Заголовки запроса.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответ от чат-бота.

**Как работает функция**:
1. Устанавливает максимальное количество повторных попыток и начальное значение счетчика попыток.
2. В цикле (пока не достигнуто максимальное количество попыток) отправляет POST-запрос к `chat_api_endpoint` с данными, содержащими `project_id` и список сообщений.
3. Обрабатывает ответ от API:
   - Если получен статус 429 (превышение лимита запросов), увеличивает счетчик попыток, ожидает некоторое время (экспоненциально увеличивающееся) и повторяет запрос.
   - Если получен другой статус ошибки, вызывает исключение `ResponseStatusError`.
   - Если запрос успешен, извлекает содержимое ответа из JSON-ответа и возвращает его.
4. Если после всех попыток запрос не удался, вызывает последнее возникшее исключение.

```
Установка параметров повторных попыток
|
Цикл повторных попыток
|
Отправка POST-запроса к chat_api_endpoint
|
Обработка ответа (успех, ошибка 429, другая ошибка)
|
Извлечение содержимого ответа
|
Возврат содержимого или исключения
```

**Примеры**:

```python
# Пример вызова (внутри create_async_generator)
project_id = "xyz123abc"
messages = [{"role": "user", "content": "What is the capital of France?"}]
headers = {"Content-Type": "application/json"}

async for result in Websim._handle_chat_request(project_id, messages, headers):
    print(result)