# Модуль для работы с провайдером AmigoChat
=========================================

Модуль содержит класс `AmigoChat`, который используется для взаимодействия с сервисом AmigoChat для получения ответов от различных AI-моделей и генерации изображений.

## Обзор

Этот модуль предоставляет асинхронный интерфейс для взаимодействия с AmigoChat API. Он поддерживает как текстовые ответы, так и генерацию изображений. В модуле определены модели, поддерживаемые AmigoChat, и их соответствующие идентификаторы персон. Он также включает в себя обработку ошибок и повторные попытки.

## Подробнее

Модуль `AmigoChat` предназначен для упрощения интеграции с AmigoChat API. Он автоматически управляет заголовками, формирует полезные нагрузки запросов и обрабатывает ответы, возвращая либо текст, сгенерированный AI-моделью, либо URL-адреса сгенерированных изображений.
Он используется как один из провайдеров в проекте `hypotez`

## Классы

### `AmigoChat`

**Описание**: Класс для взаимодействия с AmigoChat API.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Добавляет поддержку выбора моделей.

**Атрибуты**:
- `url` (str): Базовый URL сервиса AmigoChat.
- `chat_api_endpoint` (str): URL для запросов чата.
- `image_api_endpoint` (str): URL для запросов генерации изображений.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `chat_models` (list): Список поддерживаемых моделей чата.
- `image_models` (list): Список поддерживаемых моделей генерации изображений.
- `models` (list): Объединенный список моделей чата и изображений.
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_personaId(model: str) -> str`: Возвращает идентификатор персоны для заданной модели.
- `generate_chat_id() -> str`: Генерирует уникальный идентификатор чата.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API.

### `get_personaId`

```python
    @classmethod
    def get_personaId(cls, model: str) -> str:
        """Получает идентификатор personaId для указанной модели.

        Args:
            model (str): Название модели.

        Returns:
            str: Идентификатор personaId для данной модели.

        Raises:
            ValueError: Если модель не найдена в списке поддерживаемых моделей.
        """
        ...
```

**Назначение**:
Метод `get_personaId` предназначен для получения идентификатора `personaId` для заданной модели. Он проверяет, является ли модель моделью чата или моделью изображения, и возвращает соответствующий `personaId` из словаря `MODELS`.

**Параметры**:
- `model` (str): Название модели, для которой требуется получить `personaId`.

**Возвращает**:
- `str`: Идентификатор `personaId` для указанной модели.

**Вызывает исключения**:
- `ValueError`: Если модель не найдена ни в списке моделей чата, ни в списке моделей изображений.

**Как работает функция**:
1. **Проверка модели в списке моделей чата**:
   - Функция проверяет, присутствует ли указанная модель в списке `cls.chat_models`.
   - Если модель найдена, функция возвращает соответствующий `persona_id` из словаря `MODELS['chat'][model]['persona_id']`.
2. **Проверка модели в списке моделей изображений**:
   - Если модель не найдена в списке моделей чата, функция проверяет, присутствует ли модель в списке `cls.image_models`.
   - Если модель найдена, функция возвращает соответствующий `persona_id` из словаря `MODELS['image'][model]['persona_id']`.
3. **Генерация исключения `ValueError`**:
   - Если модель не найдена ни в одном из списков моделей, функция вызывает исключение `ValueError` с сообщением об ошибке, указывающим, что модель не найдена.

**Примеры**:
```python
persona_id = AmigoChat.get_personaId('gpt-4o-mini')
print(persona_id)  # Вывод: amigo

persona_id = AmigoChat.get_personaId('flux-pro/v1.1')
print(persona_id)  # Вывод: flux-1-1-pro

try:
    persona_id = AmigoChat.get_personaId('unsupported-model')
except ValueError as ex:
    print(ex)  # Вывод: Unknown model: unsupported-model
```

### `generate_chat_id`

```python
    @staticmethod
    def generate_chat_id() -> str:
        """Генерирует идентификатор чата в формате: 8-4-4-4-12 шестнадцатеричных цифр.

        Returns:
            str: Уникальный идентификатор чата.
        """
        ...
```

**Назначение**:
Метод `generate_chat_id` предназначен для генерации уникального идентификатора чата. Идентификатор генерируется в формате 8-4-4-4-12 шестнадцатеричных цифр с использованием библиотеки `uuid`.

**Возвращает**:
- `str`: Уникальный идентификатор чата в формате UUID.

**Как работает функция**:
1. **Генерация UUID**:
   - Функция использует `uuid.uuid4()` для генерации случайного UUID.
2. **Преобразование в строку**:
   - Функция преобразует UUID в строку с помощью `str()`.

**Примеры**:
```python
chat_id = AmigoChat.generate_chat_id()
print(chat_id)  # Вывод: Пример: a1b2c3d4-e5f6-7890-1234-567890abcdef
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
        """Создает асинхронный генератор для взаимодействия с API AmigoChat.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            stream (bool, optional): Использовать ли потоковую передачу. По умолчанию `False`.
            timeout (int, optional): Время ожидания ответа. По умолчанию 300.
            frequency_penalty (float, optional): Штраф за частоту. По умолчанию 0.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4000.
            presence_penalty (float, optional): Штраф за присутствие. По умолчанию 0.
            temperature (float, optional): Температура генерации. По умолчанию 0.5.
            top_p (float, optional): Top P. По умолчанию 0.95.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов от API.

        Raises:
            Exception: Если возникает ошибка при взаимодействии с API после нескольких попыток.
        """
        ...
```

**Назначение**:
Метод `create_async_generator` предназначен для создания асинхронного генератора, который взаимодействует с AmigoChat API для получения ответов на основе предоставленных сообщений и параметров. Он поддерживает как текстовые ответы, так и генерацию изображений.

**Параметры**:
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `stream` (bool, optional): Использовать ли потоковую передачу. По умолчанию `False`.
- `timeout` (int, optional): Время ожидания ответа. По умолчанию 300.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию 0.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 4000.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию 0.
- `temperature` (float, optional): Температура генерации. По умолчанию 0.5.
- `top_p` (float, optional): Top P. По умолчанию 0.95.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API. В случае генерации изображений возвращает `ImageResponse`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при взаимодействии с API после нескольких попыток.

**Как работает функция**:
1. **Подготовка параметров**:
   - Получает модель, используя `cls.get_model(model)`.
   - Генерирует уникальный `device_uuid` для каждого запроса и устанавливает максимальное количество повторных попыток (`max_retries`).
2. **Цикл повторных попыток**:
   - Функция выполняет несколько попыток отправки запроса, если возникают ошибки.
   - Устанавливает заголовки запроса, включая `user-agent`, `content-type` и `x-device-*`.
3. **Создание асинхронной сессии**:
   - Использует `StreamSession` для выполнения асинхронных HTTP-запросов.
4. **Обработка моделей чата**:
   - Если модель не является моделью изображения (`model not in cls.image_models`):
     - Формирует полезную нагрузку запроса, включая `chatId`, `messages`, `model`, `personaId` и другие параметры.
     - Отправляет POST-запрос на `cls.chat_api_endpoint`.
     - Обрабатывает потоковый ответ, если `stream=True`:
       - Читает ответ построчно.
       - Извлекает контент из каждого фрагмента JSON и возвращает его через `yield`.
5. **Обработка моделей изображений**:
   - Если модель является моделью изображения:
     - Извлекает `prompt` из последнего сообщения.
     - Формирует полезную нагрузку запроса, включая `prompt`, `model` и `personaId`.
     - Отправляет POST-запрос на `cls.image_api_endpoint`.
     - Обрабатывает JSON-ответ и извлекает URL-адреса изображений.
     - Возвращает `ImageResponse` с URL-адресами изображений и `prompt`.
6. **Обработка ошибок**:
   - Перехватывает исключения `ResponseStatusError` и `Exception`.
   - Повторяет запрос до `max_retries` раз.
   - Если все попытки не удались, вызывает исключение.

**Примеры**:
```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
model = "gpt-4o-mini"

async def run_chat():
    async for message in AmigoChat.create_async_generator(model=model, messages=messages):
        print(message, end="")

# Пример генерации изображений
messages = [{"role": "user", "content": "A cat sitting on a mat"}]
model = "flux-pro/v1.1"

async def run_image():
    async for response in AmigoChat.create_async_generator(model=model, messages=messages):
        if isinstance(response, ImageResponse):
            print(response.image_urls)

# Пример обработки ошибок
messages = [{"role": "user", "content": "Hello, how are you?"}]
model = "unsupported-model"

async def run_chat_error():
    try:
        async for message in AmigoChat.create_async_generator(model=model, messages=messages):
            print(message, end="")
    except Exception as ex:
        print(f"Error: {ex}")