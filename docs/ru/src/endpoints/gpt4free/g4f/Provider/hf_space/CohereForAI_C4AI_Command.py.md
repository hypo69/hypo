# Модуль `CohereForAI_C4AI_Command.py`

## Обзор

Модуль `CohereForAI_C4AI_Command.py` предназначен для взаимодействия с моделью CohereForAI C4AI Command через API. Он предоставляет асинхронный генератор для получения ответов от модели, а также поддерживает управление историей разговоров.

## Подробней

Модуль позволяет отправлять запросы к модели CohereForAI C4AI Command и получать ответы в режиме реального времени. Он также поддерживает управление историей разговоров, что позволяет модели учитывать предыдущие сообщения при генерации ответа.

## Классы

### `CohereForAI_C4AI_Command`

**Описание**: Класс `CohereForAI_C4AI_Command` предоставляет функциональность для взаимодействия с моделью CohereForAI C4AI Command. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Содержит общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера (по умолчанию `"CohereForAI C4AI Command"`).
- `url` (str): URL API (по умолчанию `"https://cohereforai-c4ai-command.hf.space"`).
- `conversation_url` (str): URL для ведения разговоров (формируется на основе `url`).
- `working` (bool): Указывает, работает ли провайдер (по умолчанию `True`).
- `default_model` (str): Модель, используемая по умолчанию (по умолчанию `"command-a-03-2025"`).
- `model_aliases` (dict): Словарь псевдонимов моделей.
- `models` (list): Список доступных моделей.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает имя модели. Если модель есть в `model_aliases.values()`, то возвращается это значение, иначе вызывается `super().get_model(model, **kwargs)`.
- `create_async_generator(model: str, messages: Messages, api_key: str = None, proxy: str = None, conversation: JsonConversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        """Возвращает имя модели.

        Args:
            model (str): Имя модели.
            **kwargs: Дополнительные аргументы.

        Returns:
            str: Имя модели.
        """
        ...
```

**Назначение**: Возвращает имя модели, используемое для запроса.

**Параметры**:
- `model` (str): Имя модели.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:

1.  Функция `get_model` проверяет, является ли предоставленное имя модели (`model`) одним из известных значений в `cls.model_aliases.values()`.
2.  Если `model` содержится в значениях `model_aliases`, функция возвращает это значение как допустимую модель.
3.  В противном случае функция вызывает метод `get_model` из суперкласса (`super().get_model(model, **kwargs)`) для обработки имени модели.

```
Проверка наличия model в aliases.values()  -> Возврат model : super().get_model(model, **kwargs)
```

**Примеры**:
```python
# Пример 1: Использование псевдонима модели
model_name = CohereForAI_C4AI_Command.get_model("command-a")
print(model_name)  # Вывод: command-a-03-2025

# Пример 2: Использование полного имени модели
model_name = CohereForAI_C4AI_Command.get_model("command-r-plus-08-2024")
print(model_name)  # Вывод: command-r-plus-08-2024

# Пример 3: Использование неизвестного имени модели (предполагается, что суперкласс обработает его)
# В данном случае поведение зависит от реализации get_model в суперклассе
# model_name = CohereForAI_C4AI_Command.get_model("unknown-model")
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls, model: str, messages: Messages,
        api_key: str = None, 
        proxy: str = None,
        conversation: JsonConversation = None,
        return_conversation: bool = False,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения ответов от модели.

        Args:
            model (str): Имя модели.
            messages (Messages): Список сообщений.
            api_key (str, optional): API ключ. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            conversation (JsonConversation, optional): Объект разговора. По умолчанию `None`.
            return_conversation (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для получения ответов от модели CohereForAI C4AI Command.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для отправки.
- `api_key` (str, optional): API ключ. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `conversation` (JsonConversation, optional): Объект разговора. По умолчанию `None`.
- `return_conversation` (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор.

**Как работает функция**:

1.  Функция `create_async_generator` принимает параметры, необходимые для настройки асинхронного взаимодействия с моделью CohereForAI C4AI Command.
2.  Определяет заголовки (`headers`), которые будут использоваться при отправке запросов. В эти заголовки включаются Origin, User-Agent, Accept, Accept-Language, Referer, Sec-Fetch-Dest, Sec-Fetch-Mode, Sec-Fetch-Site и Priority. Если предоставлен `api_key`, он также добавляется в заголовок Authorization.
3.  Использует `ClientSession` из библиотеки `aiohttp` для асинхронных HTTP-запросов.
4.  Разделяет сообщения на системные и пользовательские, извлекая системные сообщения для создания `system_prompt`.
5.  Форматирует входные данные (`inputs`) на основе наличия существующего разговора (`conversation`).
6.  Если разговор отсутствует или модель разговора не совпадает с текущей моделью, отправляет POST-запрос для создания нового разговора. Если `return_conversation` имеет значение `True`, функция возвращает объект разговора.
7.  Отправляет GET-запрос для получения `message_id`.
8.  Формирует данные формы (`data`) с входными данными, `message_id` и параметрами запроса (например, `is_retry`, `is_continue`, `web_search`, `tools`).
9.  Отправляет POST-запрос с данными формы для получения ответа от модели.
10. Обрабатывает ответ модели, извлекая данные из JSON-фрагментов. Если тип данных (`data["type"]`) равен "stream", возвращает сгенерированный токен. Если тип данных равен "title", возвращает сгенерированный заголовок. Если тип данных равен "finalAnswer", завершает генерацию.

```
Получение аргументов -> Определение заголовков -> Создание ClientSession -> Разделение сообщений -> Форматирование входных данных -> 
    Если нет conversation или conversation.model != model:
        Создание нового conversation
        Если return_conversation:
            Возврат conversation
    Получение message_id -> Формирование данных формы -> Отправка POST-запроса -> Обработка ответа модели
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с минимальными параметрами
messages = [{"role": "user", "content": "Hello, how are you?"}]
async_generator = CohereForAI_C4AI_Command.create_async_generator(model="command-a", messages=messages)

# Пример 2: Создание асинхронного генератора с API-ключом и прокси
messages = [{"role": "user", "content": "Translate 'hello' to French."}]
async_generator = CohereForAI_C4AI_Command.create_async_generator(
    model="command-r-plus", messages=messages, api_key="YOUR_API_KEY", proxy="http://your-proxy:8080"
)

# Пример 3: Создание асинхронного генератора с существующим conversation
messages = [{"role": "user", "content": "And what about in Spanish?"}]
conversation = JsonConversation(conversationId="123", model="command-a", preprompt="")
async_generator = CohereForAI_C4AI_Command.create_async_generator(
    model="command-a", messages=messages, conversation=conversation
)