# Модуль `AmigoChat.py`

## Обзор

Модуль `AmigoChat.py` предназначен для взаимодействия с провайдером AmigoChat, предоставляющим доступ к различным моделям, включая модели для генерации текста и изображений. Он содержит класс `AmigoChat`, который реализует асинхронный генератор для работы с API AmigoChat.

## Подробней

Модуль содержит модели для работы с API AmigoChat, такие как `gpt-4o-2024-11-20`, `gpt-4o-mini`, `flux-pro/v1.1` и другие. Он обеспечивает поддержку стриминга, системных сообщений и истории сообщений.

## Классы

### `AmigoChat`

**Описание**: Класс `AmigoChat` реализует функциональность асинхронного генератора для взаимодействия с API AmigoChat.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Аттрибуты**:
- `url` (str): URL сервиса AmigoChat.
- `chat_api_endpoint` (str): URL для API чата.
- `image_api_endpoint` (str): URL для API генерации изображений.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `chat_models` (list): Список моделей для чата.
- `image_models` (list): Список моделей для генерации изображений.
- `models` (list): Объединенный список моделей для чата и генерации изображений.
- `model_aliases` (dict): Словарь псевдонимов моделей.

**Методы**:
- `get_personaId(model: str) -> str`: Возвращает `personaId` для указанной модели.
- `generate_chat_id() -> str`: Генерирует уникальный идентификатор чата.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API.

### `get_personaId`

```python
    @classmethod
    def get_personaId(cls, model: str) -> str:
        """Возвращает personaId для указанной модели.

        Args:
            model (str): Название модели.

        Returns:
            str: Значение persona_id для указанной модели.

        Raises:
            ValueError: Если модель не найдена в списках `chat_models` и `image_models`.
        """
        ...
```

**Назначение**:
Метод `get_personaId` извлекает идентификатор персоны (`persona_id`) для заданной модели из словаря `MODELS`.

**Параметры**:
- `model` (str): Название модели, для которой требуется получить `persona_id`.

**Возвращает**:
- `str`: Значение `persona_id`, соответствующее указанной модели.

**Вызывает исключения**:
- `ValueError`: Вызывается, если модель не найдена ни в списке моделей чата (`chat_models`), ни в списке моделей изображений (`image_models`).

**Как работает функция**:

1. Проверяет, находится ли указанная модель в списке моделей чата (`cls.chat_models`).
2. Если модель найдена в списке моделей чата, метод возвращает соответствующее значение `persona_id` из словаря `MODELS['chat'][model]['persona_id']`.
3. Если модель не найдена в списке моделей чата, проверяет, находится ли она в списке моделей изображений (`cls.image_models`).
4. Если модель найдена в списке моделей изображений, метод возвращает соответствующее значение `persona_id` из словаря `MODELS['image'][model]['persona_id']`.
5. Если модель не найдена ни в одном из списков, метод вызывает исключение `ValueError` с сообщением об ошибке "Unknown model".

```
  ModelCheck -> ChatModelFound? --YES--> ChatModelPersonaId
          |
          NO
          V
  ImageModelCheck -> ImageModelFound? --YES--> ImageModelPersonaId
                 |
                 NO
                 V
                 ValueError
```
**Примеры**:

```python
# Пример 1: Получение persona_id для модели чата
persona_id = AmigoChat.get_personaId('gpt-4o-mini')
print(persona_id)  # Вывод: amigo

# Пример 2: Получение persona_id для модели изображений
persona_id = AmigoChat.get_personaId('flux-dev')
print(persona_id)  # Вывод: flux-dev

# Пример 3: Попытка получения persona_id для несуществующей модели
try:
    persona_id = AmigoChat.get_personaId('non-existent-model')
except ValueError as ex:
    print(ex)  # Вывод: Unknown model: non-existent-model
```

### `generate_chat_id`

```python
    @staticmethod
    def generate_chat_id() -> str:
        """Generate a chat ID in format: 8-4-4-4-12 hexadecimal digits"""
        return str(uuid.uuid4())
```

**Назначение**:
Метод `generate_chat_id` генерирует уникальный идентификатор чата в формате UUID (Universally Unique Identifier).

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Уникальный идентификатор чата в виде строки, состоящей из 32 шестнадцатеричных цифр, разделенных дефисами в формате "8-4-4-4-12".

**Как работает функция**:
1. Использует функцию `uuid.uuid4()` из модуля `uuid` для генерации UUID.
2. Преобразует UUID в строку с помощью `str()`.

```
UUIDgeneration -> UUIDstring
```

**Примеры**:

```python
# Пример: Генерация chat_id
chat_id = AmigoChat.generate_chat_id()
print(chat_id)  # Вывод: Например, 'a1b2c3d4-e5f6-7890-1234-567890abcdef'
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        stream: bool = False,
        timeout: int = 300,
        frequency_penalty: float = 0,
        max_tokens: int = 4000,
        presence_penalty: float = 0,
        temperature: float = 0.5,
        top_p: float = 0.95,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения ответов от API AmigoChat.

        Args:
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            stream (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию `False`.
            timeout (int, optional): Время ожидания ответа от сервера в секундах. По умолчанию `300`.
            frequency_penalty (float, optional): Штраф за частоту слов. По умолчанию `0`.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `4000`.
            presence_penalty (float, optional): Штраф за присутствие слов. По умолчанию `0`.
            temperature (float, optional): Температура для генерации текста. По умолчанию `0.5`.
            top_p (float, optional): Значение top_p для генерации текста. По умолчанию `0.95`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API. Может возвращать текст или `ImageResponse` в случае генерации изображений.

        Raises:
            Exception: Если достигнуто максимальное количество попыток переподключения.
        """
        ...
```

**Назначение**:
Метод `create_async_generator` создает асинхронный генератор для взаимодействия с API AmigoChat, позволяя получать ответы в асинхронном режиме.

**Параметры**:
- `model` (str): Название используемой модели.
- `messages (Messages)`: Список сообщений для отправки в API.
- `proxy (str, optional)`: Прокси-сервер для использования. По умолчанию `None`.
- `stream (bool, optional)`: Флаг, указывающий на использование стриминга. По умолчанию `False`.
- `timeout (int, optional)`: Время ожидания ответа от сервера в секундах. По умолчанию `300`.
- `frequency_penalty (float, optional)`: Штраф за частоту слов. По умолчанию `0`.
- `max_tokens (int, optional)`: Максимальное количество токенов в ответе. По умолчанию `4000`.
- `presence_penalty (float, optional)`: Штраф за присутствие слов. По умолчанию `0`.
- `temperature (float, optional)`: Температура для генерации текста. По умолчанию `0.5`.
- `top_p (float, optional)`: Значение top_p для генерации текста. По умолчанию `0.95`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API. Может возвращать текст или `ImageResponse` в случае генерации изображений.

**Вызывает исключения**:
- `Exception`: Если достигнуто максимальное количество попыток переподключения.

**Как работает функция**:

1. **Инициализация**:
   - Определяет модель, используя `cls.get_model(model)`.
   - Генерирует `device_uuid` для идентификации устройства.
   - Устанавливает максимальное количество попыток `max_retries` равным 3.
   - Инициализирует счетчик попыток `retry_count` равным 0.

2. **Цикл повторных попыток**:
   - Запускает цикл `while retry_count < max_retries` для повторных попыток подключения в случае ошибок.

3. **Формирование заголовков**:
   - Определяет заголовки `headers` для HTTP-запроса, включая `user-agent`, `content-type` и другие необходимые параметры.

4. **Создание сессии**:
   - Использует `StreamSession` для создания асинхронной сессии с заданными заголовками и прокси-сервером.

5. **Обработка моделей изображений и текста**:
   - Проверяет, является ли модель моделью для генерации изображений (`model not in cls.image_models`).
     - **Для текстовых моделей**:
       - Формирует данные `data` для отправки в API чата, включая `chatId`, `messages`, `model`, `personaId` и другие параметры.
       - Отправляет POST-запрос на `cls.chat_api_endpoint` с данными `data` и таймаутом `timeout`.
       - Итерируется по строкам ответа, декодирует их и извлекает контент из JSON-структуры.
       - Извлекает `content` из полей `delta` или `text` внутри `choices`.
       - Возвращает `content` через `yield`.
     - **Для моделей изображений**:
       - Извлекает `prompt` из последнего сообщения в списке `messages`.
       - Формирует данные `data` для отправки в API генерации изображений, включая `prompt`, `model` и `personaId`.
       - Отправляет POST-запрос на `cls.image_api_endpoint` с данными `data`.
       - Извлекает URL-адреса изображений из JSON-ответа и возвращает `ImageResponse` через `yield`.

6. **Обработка ошибок**:
   - Перехватывает исключения `ResponseStatusError` и `Exception`.
   - Увеличивает счетчик `retry_count` на 1.
   - Если `retry_count` достигает `max_retries`, вызывает исключение.
   - Генерирует новый `device_uuid` для следующей попытки.

```
Init -> ModelCheck -> TextModel? --YES--> TextRequest -> IterateLines -> ExtractContent -> YieldContent
          |                                      ^ NO
          NO                                     |
          V                                      ImageRequest -> ExtractImageUrls -> YieldImageResponse
          ^                                      |
          |                                      Exception
          Exception
```

**Примеры**:

```python
# Пример 1: Использование create_async_generator для текстовой модели
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for content in AmigoChat.create_async_generator(model='gpt-4o-mini', messages=messages):
    print(content)

# Пример 2: Использование create_async_generator для модели изображений
messages = [{"role": "user", "content": "A cat in space"}]
async for response in AmigoChat.create_async_generator(model='flux-dev', messages=messages):
    if isinstance(response, ImageResponse):
        print(response.image_urls)