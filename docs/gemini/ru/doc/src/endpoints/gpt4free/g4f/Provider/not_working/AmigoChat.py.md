# Модуль `AmigoChat.py`

## Обзор

Модуль предоставляет класс `AmigoChat`, который является асинхронным генератором для взаимодействия с API AmigoChat.io для генерации текста и изображений. Он поддерживает стриминг ответов для текстовых моделей и предоставляет возможность выбора различных моделей, включая `gpt-4o`, `llama-3.1-405b`, `claude-3.5-sonnet` и другие. Также модуль поддерживает генерацию изображений через API AmigoChat.io.

## Подробней

Модуль предназначен для интеграции с API AmigoChat.io, позволяя пользователям генерировать текст и изображения с использованием различных моделей. Класс `AmigoChat` предоставляет удобный интерфейс для отправки запросов к API и получения ответов в асинхронном режиме. Модуль также обрабатывает ошибки и поддерживает повторные попытки при возникновении проблем с подключением к API.

## Классы

### `AmigoChat`

**Описание**: Класс `AmigoChat` является асинхронным генератором для взаимодействия с API AmigoChat.io.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовый функционал для асинхронных генераторов.
- `ProviderModelMixin`: Обеспечивает поддержку выбора моделей.

**Атрибуты**:
- `url` (str): Базовый URL AmigoChat.io (`https://amigochat.io/chat/`).
- `chat_api_endpoint` (str): URL для API генерации текста (`https://api.amigochat.io/v1/chat/completions`).
- `image_api_endpoint` (str): URL для API генерации изображений (`https://api.amigochat.io/v1/images/generations`).
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_stream` (bool): Поддерживает ли потоковую передачу данных (в данном случае `True`).
- `supports_system_message` (bool): Поддерживает ли передачу системных сообщений (в данном случае `True`).
- `supports_message_history` (bool): Поддерживает ли историю сообщений (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `chat_models` (List[str]): Список поддерживаемых моделей чата.
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `models` (List[str]): Объединенный список моделей чата и изображений.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_personaId(cls, model: str) -> str`: Возвращает `personaId` для указанной модели.
- `generate_chat_id() -> str`: Генерирует уникальный идентификатор чата.
- `create_async_generator(cls, model: str, messages: Messages, proxy: str = None, stream: bool = False, timeout: int = 300, frequency_penalty: float = 0, max_tokens: int = 4000, presence_penalty: float = 0, temperature: float = 0.5, top_p: float = 0.95, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от API AmigoChat.io.

## Функции

### `get_personaId`

```python
    @classmethod
    def get_personaId(cls, model: str) -> str:
        """Возвращает personaId для указанной модели.

        Args:
            model (str): Имя модели.

        Returns:
            str: `personaId` для указанной модели.

        Raises:
            ValueError: Если модель не найдена в списках `chat_models` или `image_models`.
        """
        ...
```

**Назначение**:
Функция `get_personaId` возвращает идентификатор `personaId`, связанный с определенной моделью, используемой в API AmigoChat.

**Параметры**:
- `model` (str): Имя модели, для которой нужно получить `personaId`.

**Возвращает**:
- `str`: Идентификатор `personaId` для указанной модели.

**Вызывает исключения**:
- `ValueError`: Если модель не найдена ни в списке моделей чата (`chat_models`), ни в списке моделей изображений (`image_models`).

**Как работает функция**:

1. **Проверка наличия в моделях чата**: Функция сначала проверяет, содержится ли переданное имя модели (`model`) в списке моделей чата (`cls.chat_models`). Если модель найдена в этом списке, функция извлекает и возвращает соответствующий `persona_id` из словаря `MODELS['chat'][model]`.

2. **Проверка наличия в моделях изображений**: Если модель не найдена в списке моделей чата, функция проверяет, содержится ли она в списке моделей изображений (`cls.image_models`). Если модель найдена в этом списке, функция извлекает и возвращает соответствующий `persona_id` из словаря `MODELS['image'][model]`.

3. **Обработка ошибки**: Если модель не найдена ни в одном из списков (моделей чата или моделей изображений), функция вызывает исключение `ValueError` с сообщением о том, что модель не распознана.

```
graph TD
    A[Проверка model in cls.chat_models]
    B[Извлечение persona_id из MODELS['chat'][model]]
    C[Проверка model in cls.image_models]
    D[Извлечение persona_id из MODELS['image'][model]]
    E[Вызов ValueError("Unknown model")]

    A -- True --> B
    A -- False --> C
    C -- True --> D
    C -- False --> E
```

**Примеры**:
```python
# Пример получения personaId для модели чата
persona_id = AmigoChat.get_personaId('gpt-4o-mini')
print(persona_id)  # Вывод: amigo

# Пример получения personaId для модели изображения
persona_id = AmigoChat.get_personaId('flux-dev')
print(persona_id)  # Вывод: flux-dev

# Пример вызова исключения ValueError
try:
    persona_id = AmigoChat.get_personaId('unknown-model')
except ValueError as ex:
    print(ex)  # Вывод: Unknown model: unknown-model
```

### `generate_chat_id`

```python
    @staticmethod
    def generate_chat_id() -> str:
        """Generate a chat ID in format: 8-4-4-4-12 hexadecimal digits"""
        return str(uuid.uuid4())
```

**Назначение**:
Функция `generate_chat_id` генерирует уникальный идентификатор чата в формате `8-4-4-4-12` шестнадцатеричных цифр.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Уникальный идентификатор чата в формате строки.

**Как работает функция**:

1. **Генерация UUID**: Функция использует `uuid.uuid4()` для генерации случайного UUID (Universally Unique Identifier).

2. **Преобразование в строку**: Сгенерированный UUID преобразуется в строковое представление с помощью `str()`.

3. **Возврат идентификатора**: Строковое представление UUID возвращается в качестве идентификатора чата.

```
graph TD
    A[Генерация UUID с помощью uuid.uuid4()]
    B[Преобразование UUID в строку str()]
    C[Возврат строкового представления UUID]

    A --> B --> C
```

**Примеры**:
```python
# Пример генерации идентификатора чата
chat_id = AmigoChat.generate_chat_id()
print(chat_id)  # Вывод: Пример: 123e4567-e89b-12d3-a456-426614174000 (случайный UUID)
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
        """Создает асинхронный генератор для получения ответов от API AmigoChat.io.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера. По умолчанию None.
            stream (bool, optional): Включить ли потоковую передачу ответов. По умолчанию False.
            timeout (int, optional): Время ожидания ответа от API в секундах. По умолчанию 300.
            frequency_penalty (float, optional): Штраф за частоту использования токенов. По умолчанию 0.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4000.
            presence_penalty (float, optional): Штраф за наличие токенов в ответе. По умолчанию 0.
            temperature (float, optional): Температура для генерации текста. По умолчанию 0.5.
            top_p (float, optional): Top-p для генерации текста. По умолчанию 0.95.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API.

        Raises:
            Exception: Если происходит ошибка при подключении к API или обработке ответа.
        """
        ...
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор, который взаимодействует с API AmigoChat.io для генерации текста или изображений на основе предоставленных сообщений и параметров модели.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `stream` (bool, optional): Включить ли потоковую передачу ответов. По умолчанию `False`.
- `timeout` (int, optional): Время ожидания ответа от API в секундах. По умолчанию `300`.
- `frequency_penalty` (float, optional): Штраф за частоту использования токенов. По умолчанию `0`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `4000`.
- `presence_penalty` (float, optional): Штраф за наличие токенов в ответе. По умолчанию `0`.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию `0.5`.
- `top_p` (float, optional): Top-p для генерации текста. По умолчанию `0.95`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при подключении к API или обработке ответа.

**Как работает функция**:

1. **Подготовка параметров**:
   - Получает имя модели, используя `cls.get_model(model)`.
   - Генерирует уникальный идентификатор устройства (`device_uuid`).
   - Устанавливает максимальное количество повторных попыток (`max_retries`) равным 3.
   - Инициализирует счетчик повторных попыток (`retry_count`) равным 0.

2. **Цикл повторных попыток**:
   - Запускает цикл `while`, который выполняется до тех пор, пока `retry_count` меньше `max_retries`.

3. **Настройка заголовков**:
   - Внутри цикла настраиваются заголовки HTTP-запроса, включая `user-agent`, `content-type` и другие необходимые параметры.

4. **Создание асинхронной сессии**:
   - Создается асинхронная сессия с использованием `StreamSession` для выполнения HTTP-запросов.

5. **Обработка различных типов моделей**:
   - Проверяется, является ли выбранная модель (`model`) моделью для генерации изображений (присутствует ли она в списке `cls.image_models`).

6. **Генерация текста (если модель не для изображений)**:
   - Формируется словарь `data` с параметрами запроса, такими как `chatId`, `messages`, `model`, `personaId` и другие.
   - Выполняется POST-запрос к API (`cls.chat_api_endpoint`) с использованием асинхронной сессии.
   - Полученные данные обрабатываются построчно, извлекается содержимое (`content`) из JSON-ответа и передается через `yield`.

7. **Генерация изображений (если модель для изображений)**:
   - Извлекается текст запроса (`prompt`) из последнего сообщения в списке `messages`.
   - Формируется словарь `data` с параметрами запроса для генерации изображений.
   - Выполняется POST-запрос к API (`cls.image_api_endpoint`) с использованием асинхронной сессии.
   - Полученные URL изображений извлекаются из JSON-ответа и передаются через `yield` в виде объекта `ImageResponse`.

8. **Обработка ошибок**:
   - Если во время выполнения запроса возникают исключения `ResponseStatusError` или другие исключения, счетчик `retry_count` увеличивается.
   - Если количество повторных попыток превышает `max_retries`, исключение перебрасывается.
   - При каждой повторной попытке генерируется новый `device_uuid`.

```
graph TD
    A[Получение model через cls.get_model(model)]
    B[Генерация device_uuid]
    C[Цикл: retry_count < max_retries]
    D[Настройка заголовков HTTP-запроса]
    E[Создание асинхронной сессии StreamSession]
    F[Проверка model in cls.image_models]
    G[Формирование data для запроса текста]
    H[POST-запрос к cls.chat_api_endpoint]
    I[Обработка ответа построчно, извлечение content и yield]
    J[Формирование data для запроса изображения]
    K[POST-запрос к cls.image_api_endpoint]
    L[Извлечение URL изображений из JSON-ответа и yield ImageResponse]
    M[Обработка исключений ResponseStatusError или Exception]
    N[Увеличение retry_count]
    O[Проверка retry_count >= max_retries]
    P[Переброс исключения]

    A --> B --> C
    C -- True --> D --> E --> F
    F -- False --> G --> H --> I --> C
    F -- True --> J --> K --> L --> C
    C -- False --> End
    I -- Exception --> M --> N --> O
    L -- Exception --> M --> N --> O
    O -- True --> P
    O -- False --> B
    End[Конец]
```

**Примеры**:
```python
# Пример использования для генерации текста
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for chunk in AmigoChat.create_async_generator(model='gpt-4o-mini', messages=messages):
    print(chunk, end="")

# Пример использования для генерации изображения
messages = [{"role": "user", "content": "A beautiful sunset"}]
async for image_response in AmigoChat.create_async_generator(model='flux-dev', messages=messages):
    if image_response:
        print(image_response.image_urls)