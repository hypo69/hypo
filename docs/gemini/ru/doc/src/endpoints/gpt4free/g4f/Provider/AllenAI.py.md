# Модуль AllenAI
## Обзор

Модуль `AllenAI` предоставляет асинхронтный генератор для взаимодействия с моделями AllenAI через API. Он включает в себя классы `Conversation` для управления историей сообщений и `AllenAI` для отправки запросов к API AllenAI и получения ответов.

## Подробней

Модуль предназначен для интеграции с сервисами AllenAI, такими как Ai2 Playground, и обеспечивает возможность обмена сообщениями с различными моделями, поддерживаемыми AllenAI. Он поддерживает потоковую передачу данных и позволяет сохранять историю разговоров.
В модуле реализована поддержка асинхронного взаимодействия, что позволяет эффективно использовать ресурсы при обработке запросов.

## Классы

### `Conversation`
**Описание**: Класс для хранения истории разговоров с AI-моделью.
**Наследует**: `JsonConversation`

**Атрибуты**:
- `parent` (str, optional): Идентификатор родительского сообщения в контексте разговора. По умолчанию `None`.
- `x_anonymous_user_id` (str, optional): Анонимный идентификатор пользователя. Генерируется случайным образом при создании экземпляра класса.
- `model` (str): Модель, используемая в разговоре.
- `messages` (List[dict]): Список сообщений в разговоре, где каждое сообщение представлено в виде словаря с ключами `role` и `content`.

**Методы**:
- `__init__(self, model: str)`: Инициализирует новый экземпляр класса `Conversation`.

### `AllenAI`
**Описание**: Класс для взаимодействия с API AllenAI.

**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:
- `label` (str): Метка провайдера (значение: "Ai2 Playground").
- `url` (str): URL сервиса Ai2 Playground (значение: "https://playground.allenai.org").
- `login_url` (str): URL для входа в систему (значение: `None`).
- `api_endpoint` (str): URL API для отправки сообщений (значение: "https://olmo-api.allen.ai/v4/message/stream").
- `working` (bool): Указывает, работает ли провайдер в данный момент (значение: `True`).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования провайдера (значение: `False`).
- `use_nodriver` (bool): Указывает, использовать ли драйвер для автоматизации браузера (значение: `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (значение: `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (значение: `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (значение: `True`).
- `default_model` (str): Модель, используемая по умолчанию (значение: `'tulu3-405b'`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `create_async_generator(model: str, messages: Messages, proxy: str = None, host: str = "inferd", private: bool = True, top_p: float = None, temperature: float = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для отправки запроса к API AllenAI и получения ответа.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    host: str = "inferd",
    private: bool = True,
    top_p: float = None,
    temperature: float = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API AllenAI.

    Args:
        cls: Ссылка на класс `AllenAI`.
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        host (str, optional): Хост для запроса. По умолчанию `"inferd"`.
        private (bool, optional): Указывает, является ли разговор приватным. По умолчанию `True`.
        top_p (float, optional): Значение top_p для модели. По умолчанию `None`.
        temperature (float, optional): Температура для модели. По умолчанию `None`.
        conversation (Conversation, optional): Объект разговора. По умолчанию `None`.
        return_conversation (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа от API AllenAI.

    Raises:
        Не вызывает исключений напрямую, но использует `raise_for_status` для проверки статуса ответа.

    """
```
**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который отправляет запрос к API AllenAI и получает ответ в виде потока данных. Она отвечает за формирование запроса, отправку данных и обработку полученных чанков, а также за обновление состояния разговора.

**Как работает функция**:

1.  **Подготовка данных**:
    *   Форматирует входные сообщения для отправки в запросе. Если `conversation` не указан, используется `format_prompt`, иначе используется последнее сообщение пользователя из `messages` через `get_last_user_message`.
    *   Инициализирует или обновляет объект `Conversation`.
    *   Генерирует уникальный разделитель `boundary` для формирования `multipart/form-data` запроса.

2.  **Формирование заголовков**:
    *   Создает словарь `headers` с необходимыми HTTP-заголовками, включая `content-type` с динамически сгенерированным `boundary` и `x-anonymous-user-id` из объекта `conversation`.

3.  **Создание тела запроса**:
    *   Формирует тело запроса в формате `multipart/form-data`, добавляя параметры, такие как `model`, `host`, `content` (сообщение пользователя) и `private`.
    *   Если в `conversation` присутствует `parent`, он также добавляется в тело запроса.
    *   Добавляет параметры `temperature` и `top_p`, если они указаны.

4.  **Отправка запроса и обработка ответа**:
    *   Использует `ClientSession` из библиотеки `aiohttp` для отправки асинхронного `POST` запроса к `api_endpoint` с сформированными заголовками и данными.
    *   Вызывает `raise_for_status` для проверки статуса ответа. Если статус указывает на ошибку, вызывается исключение.
    *   Итерируется по чанкам полученного ответа.

5.  **Обработка чанков**:
    *   Декодирует каждый чанк и разделяет его на строки.
    *   Парсит каждую строку как JSON.
    *   Обновляет `current_parent` на основе идентификатора ассистента в ответе.
    *   Извлекает и возвращает контент ответа, если он присутствует в данных и не является пустым.
    *   Обрабатывает финальный ответ, обновляет `conversation.parent`, добавляет сообщения в `conversation.messages` и возвращает `FinishReason("stop")`.

6.  **Возврат результата**:
    *   Возвращает асинхронный генератор, который выдает части ответа, а также объект `conversation`, если `return_conversation` имеет значение `True`.

**ASCII flowchart**:

```
Начало
  │
  │ Получение/Форматирование prompt (сообщения пользователя)
  │
  │ Инициализация/Обновление conversation
  │
  │ Генерация boundary (разделителя)
  │
  │ Формирование headers (заголовков)
  │
  │ Создание data (тела запроса multipart/form-data)
  │
  │ Отправка POST запроса к api_endpoint
  │
  │ Проверка статуса ответа (raise_for_status)
  │
  │ Итерация по chunk в response.content
  │
  │ Декодирование и разделение chunk на строки
  │
  │ Попытка парсинга строки как JSON
  │
  │ Обновление current_parent на основе ответа
  │
  │ Извлечение и yield контента ответа
  │
  │ Обработка финального ответа (update conversation, yield FinishReason)
  │
Конец
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с минимальными параметрами
async def example():
    model = "tulu3-405b"
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for response in AllenAI.create_async_generator(model=model, messages=messages):
        print(response)

# Пример 2: Создание асинхронного генератора с указанием прокси и температуры
async def example_with_proxy():
    model = "tulu3-405b"
    messages = [{"role": "user", "content": "Tell me a joke."}]
    proxy = "http://your-proxy-url:8080"
    temperature = 0.7
    async for response in AllenAI.create_async_generator(model=model, messages=messages, proxy=proxy, temperature=temperature):
        print(response)

# Пример 3: Использование существующего conversation и получение conversation в ответе
async def example_with_conversation():
    model = "tulu3-405b"
    messages = [{"role": "user", "content": "Continue the story."}]
    conversation = Conversation(model)
    conversation.parent = "some_parent_id"
    async for response in AllenAI.create_async_generator(model=model, messages=messages, conversation=conversation, return_conversation=True):
        if isinstance(response, Conversation):
            print("Conversation object:", response)
        else:
            print(response)