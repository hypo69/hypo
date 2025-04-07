# Модуль Websim

## Обзор

Модуль `Websim` предоставляет асинхронный интерфейс для взаимодействия с сервисом Websim AI, который предоставляет функциональность чат-ботов и генерации изображений. Он включает в себя классы и методы для генерации project ID, обработки запросов чата и генерации изображений через API Websim.

## Подробнее

Этот модуль предназначен для интеграции с Websim AI, позволяя использовать его возможности в асинхронном режиме. Он поддерживает как текстовые запросы (чат), так и запросы на генерацию изображений, обеспечивая гибкость и масштабируемость при работе с AI-сервисами.

## Классы

### `Websim`

**Описание**: Класс `Websim` является основным классом, предоставляющим функциональность для взаимодействия с сервисом Websim AI. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет миксин для работы с моделями.

**Атрибуты**:

- `url` (str): URL сервиса Websim AI.
- `login_url` (str): URL для логина (в данном случае `None`).
- `chat_api_endpoint` (str): URL API для чат-ботов.
- `image_api_endpoint` (str): URL API для генерации изображений.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации.
- `use_nodriver` (bool): Флаг, указывающий на использование драйвера.
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию для чата.
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `models` (List[str]): Список всех поддерживаемых моделей (чат и изображения).

**Методы**:

- `generate_project_id(for_image: bool = False) -> str`: Генерирует идентификатор проекта в зависимости от типа запроса (чат или изображение).
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, aspect_ratio: str = "1:1", project_id: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для обработки запросов к Websim AI.
- `_handle_image_request(project_id: str, messages: Messages, prompt: str, aspect_ratio: str, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос на генерацию изображения.
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

**Назначение**: Генерирует идентификатор проекта (project ID) в формате, соответствующем типу запроса (изображение или чат).

**Параметры**:

- `for_image` (bool): Указывает, предназначен ли ID для запроса изображения. По умолчанию `False`.

**Возвращает**:

- `str`: Сгенерированный project ID.

**Как работает функция**:

1. Определяется набор символов, используемых для генерации ID (строчные буквы и цифры).
2. Если `for_image` равен `True`, генерируется ID для запроса изображения в формате `xxxxxxx_xxxxxxxxxxxx`, где `x` - случайный символ из набора.
3. Если `for_image` равен `False`, генерируется ID для запроса чата в формате `xxx_xxxxxxxxxxxxxxx`, где `x` - случайный символ из набора.
4. Возвращается сгенерированный ID.

**ASCII flowchart**:

```
A[Определение типа запроса (изображение или чат)]
|
B[Генерация случайных символов]
|
C[Форматирование ID в зависимости от типа запроса]
|
D[Возврат сгенерированного ID]
```

**Примеры**:

```python
project_id_chat = Websim.generate_project_id(for_image=False)
print(f"Project ID для чата: {project_id_chat}")

project_id_image = Websim.generate_project_id(for_image=True)
print(f"Project ID для изображения: {project_id_image}")
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
        """  """
```

**Назначение**: Создает асинхронный генератор для обработки запросов к Websim AI.

**Параметры**:

- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `prompt` (str, optional): Дополнительный промпт. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон для изображений. По умолчанию `"1:1"`.
- `project_id` (str, optional): Идентификатор проекта. Если `None`, генерируется автоматически.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий результаты запроса.

**Как работает функция**:

1. Определяется, является ли запрос запросом изображения на основе модели.
2. Если `project_id` не предоставлен, он генерируется с помощью `generate_project_id`.
3. Формируются заголовки запроса.
4. В зависимости от типа запроса (изображение или чат) вызывается соответствующий метод (`_handle_image_request` или `_handle_chat_request`) для обработки запроса и возвращается результат.

**ASCII flowchart**:

```
A[Проверка, является ли запрос запросом изображения]
|
B[Генерация project_id, если он не предоставлен]
|
C[Формирование заголовков запроса]
|
D[Вызов _handle_image_request или _handle_chat_request в зависимости от типа запроса]
|
E[Возврат результата]
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, Websim!"}]
async for result in Websim.create_async_generator(model="gemini-1.5-pro", messages=messages):
    print(result)

async for result in Websim.create_async_generator(model="flux", messages=messages, prompt="A cat"):
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
        """  """
```

**Назначение**: Обрабатывает запрос на генерацию изображения.

**Параметры**:

- `project_id` (str): Идентификатор проекта.
- `messages` (Messages): Список сообщений для отправки.
- `prompt` (str): Промпт для генерации изображения.
- `aspect_ratio` (str): Соотношение сторон изображения.
- `headers` (dict): Заголовки запроса.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий URL изображения.

**Как работает функция**:

1. Форматируется промпт с использованием `format_image_prompt`.
2. Создается `ClientSession` с заданными заголовками.
3. Формируются данные запроса.
4. Отправляется POST-запрос к `image_api_endpoint` с данными и прокси.
5. Обрабатывается ответ, извлекается URL изображения.
6. Возвращается `ImageResponse` с URL изображения и промптом.

**ASCII flowchart**:

```
A[Форматирование промпта]
|
B[Создание ClientSession]
|
C[Формирование данных запроса]
|
D[Отправка POST-запроса к image_api_endpoint]
|
E[Обработка ответа и извлечение URL изображения]
|
F[Возврат ImageResponse]
```

**Примеры**:

```python
messages = [{"role": "user", "content": "A cat"}]
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://websim.ai',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'websim-flags;': ''
}
async for result in Websim._handle_image_request(project_id="test_123", messages=messages, prompt="A cat", aspect_ratio="1:1", headers=headers):
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
        """  """
```

**Назначение**: Обрабатывает запрос чата.

**Параметры**:

- `project_id` (str): Идентификатор проекта.
- `messages` (Messages): Список сообщений для отправки.
- `headers` (dict): Заголовки запроса.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий контент ответа.

**Как работает функция**:

1. Устанавливается максимальное количество попыток повтора запроса и счетчик попыток.
2. В цикле (пока не достигнуто максимальное количество попыток) выполняются следующие действия:
    - Создается `ClientSession` с заданными заголовками.
    - Формируются данные запроса.
    - Отправляется POST-запрос к `chat_api_endpoint` с данными и прокси.
    - Если получен статус 429 (слишком много запросов), увеличивается счетчик попыток, вычисляется время ожидания и выполняется задержка. Если достигнуто максимальное количество попыток, выбрасывается исключение `ResponseStatusError`.
    - Обрабатывается ответ, извлекается контент.
    - Если ответ получен в формате JSON, извлекается контент из JSON и возвращается.
    - Если ответ не в формате JSON, возвращается текст ответа.
3. Если в процессе обработки произошла ошибка `ResponseStatusError`, и достигнуто максимальное количество попыток, ошибка перевыбрасывается.
4. Если произошла другая ошибка, она перевыбрасывается.

**ASCII flowchart**:

```
A[Установка параметров повторных попыток]
|
B[Цикл повторных попыток]
|
C[Создание ClientSession]
|
D[Формирование данных запроса]
|
E[Отправка POST-запроса к chat_api_endpoint]
|
F[Обработка статуса ответа (429 или другой)]
|
G[Извлечение контента из ответа]
|
H[Возврат контента]
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, Websim!"}]
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://websim.ai',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'websim-flags;': ''
}
async for result in Websim._handle_chat_request(project_id="test_123", messages=messages, headers=headers):
    print(result)