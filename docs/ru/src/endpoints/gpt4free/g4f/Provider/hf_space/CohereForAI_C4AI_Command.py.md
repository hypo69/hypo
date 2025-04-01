# Модуль CohereForAI_C4AI_Command
## Обзор

Модуль `CohereForAI_C4AI_Command` предназначен для взаимодействия с моделями CohereForAI C4AI Command через API. Он предоставляет асинхронный генератор для получения ответов от модели и поддерживает управление диалогом.

## Подробнее

Этот модуль обеспечивает интеграцию с моделями CohereForAI C4AI Command, позволяя отправлять запросы и получать ответы в асинхронном режиме. Он также поддерживает управление состоянием диалога через `JsonConversation` и предоставляет возможность генерации заголовков для ответов.

## Классы

### `CohereForAI_C4AI_Command`

**Описание**: Класс `CohereForAI_C4AI_Command` предоставляет методы для взаимодействия с моделями CohereForAI C4AI Command.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("CohereForAI C4AI Command").
- `url` (str): URL API CohereForAI C4AI Command ("https://cohereforai-c4ai-command.hf.space").
- `conversation_url` (str): URL для управления диалогами (`f"{url}/conversation"`).
- `working` (bool): Указывает, что провайдер в рабочем состоянии (`True`).
- `default_model` (str): Модель по умолчанию ("command-a-03-2025").
- `model_aliases` (dict): Псевдонимы для моделей (например, `"command-a": default_model`).
- `models` (list): Список доступных моделей.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает имя модели на основе псевдонима или переданного значения.
- `create_async_generator(model: str, messages: Messages, api_key: str = None, proxy: str = None, conversation: JsonConversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от модели.

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        if model in cls.model_aliases.values():
            return model
        return super().get_model(model, **kwargs)
```

**Назначение**: Метод `get_model` определяет, использовать ли предоставленное имя модели или его псевдоним.

**Параметры**:
- `model` (str): Имя модели или псевдоним.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:

1. **Проверка на псевдоним**: Проверяет, является ли предоставленное имя модели псевдонимом из `cls.model_aliases.values()`.
2. **Возврат модели**: Если имя модели является псевдонимом, возвращает его.
3. **Вызов родительского метода**: Если имя модели не является псевдонимом, вызывает метод `get_model` родительского класса.

```
Проверка псевдонима
    │
    ├─── True: Возврат имени модели
    │
    └─── False: Вызов родительского метода get_model
```

**Примеры**:

```python
model_name = CohereForAI_C4AI_Command.get_model("command-a")
print(model_name)
# Output: command-a-03-2025

model_name = CohereForAI_C4AI_Command.get_model("non_existent_model")
# Output: non_existent_model (если родительский класс возвращает переданное значение)
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
        model = cls.get_model(model)
        headers = {
            "Origin": cls.url,
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://cohereforai-c4ai-command.hf.space/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=4",
        }
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"
        async with ClientSession(
            headers=headers,
            cookies=None if conversation is None else conversation.cookies
        ) as session:
            system_prompt = "\\n".join([message["content"] for message in messages if message["role"] == "system"])
            messages = [message for message in messages if message["role"] != "system"]
            inputs = format_prompt(messages) if conversation is None else get_last_user_message(messages)
            if conversation is None or conversation.model != model or conversation.preprompt != system_prompt:
                data = {"model": model, "preprompt": system_prompt}
                async with session.post(cls.conversation_url, json=data, proxy=proxy) as response:
                    await raise_for_status(response)
                    conversation = JsonConversation(
                        **await response.json(),
                        **data,
                        cookies={n: c.value for n, c in response.cookies.items()}
                    )
                    if return_conversation:
                        yield conversation
            async with session.get(f"{cls.conversation_url}/{conversation.conversationId}/__data.json?x-sveltekit-invalidated=11", proxy=proxy) as response:
                await raise_for_status(response)
                node = json.loads((await response.text()).splitlines()[0])["nodes"][1]
                if node["type"] == "error":
                    raise RuntimeError(node["error"])
                data = node["data"]
                message_id = data[data[data[data[0]["messages"]][-1]]["id"]]
            data = FormData()
            data.add_field(
                "data",
                json.dumps({"inputs": inputs, "id": message_id, "is_retry": False, "is_continue": False, "web_search": False, "tools": []}),
                content_type="application/json"
            )
            async with session.post(f"{cls.conversation_url}/{conversation.conversationId}", data=data, proxy=proxy) as response:
                await raise_for_status(response)
                async for chunk in response.content:
                    try:
                        data = json.loads(chunk)
                    except (json.JSONDecodeError) as ex:
                        raise RuntimeError(f"Failed to read response: {chunk.decode(errors='replace')}", ex)
                    if data["type"] == "stream":
                        yield data["token"].replace("\\u0000", "")
                    elif data["type"] == "title":
                        yield TitleGeneration(data["title"])
                    elif data["type"] == "finalAnswer":
                        break
```

**Назначение**: Метод `create_async_generator` создает асинхронный генератор для получения ответов от модели CohereForAI C4AI Command.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для отправки модели.
- `api_key` (str, optional): API ключ. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `conversation` (JsonConversation, optional): Объект диалога. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект диалога. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от модели.

**Вызывает исключения**:
- `RuntimeError`: Если происходит ошибка при получении ответа от API.

**Как работает функция**:

1. **Получение имени модели**: Использует метод `get_model` для получения имени модели.
2. **Подготовка заголовков**: Создает заголовки для HTTP-запросов, включая `Origin`, `User-Agent`, `Accept`, `Accept-Language`, `Referer`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site` и `Priority`. Если предоставлен `api_key`, добавляет заголовок `Authorization`.
3. **Создание сессии**: Создает асинхронную сессию `ClientSession` с подготовленными заголовками и куками из объекта `conversation`, если он предоставлен.
4. **Обработка системных сообщений**: Извлекает системные сообщения из списка `messages` и объединяет их в строку `system_prompt`. Удаляет системные сообщения из списка `messages`.
5. **Форматирование входных данных**: Форматирует входные данные `inputs` из списка `messages` с использованием `format_prompt` или `get_last_user_message` в зависимости от наличия объекта `conversation`.
6. **Инициализация диалога**: Если объект `conversation` не предоставлен или параметры модели и системного запроса изменились, отправляет POST-запрос на URL `cls.conversation_url` для инициализации диалога.
7. **Получение ID сообщения**: Отправляет GET-запрос для получения ID сообщения.
8. **Подготовка данных для запроса**: Создает объект `FormData` с данными для отправки, включая `inputs`, `id` сообщения, флаги `is_retry`, `is_continue`, `web_search` и `tools`.
9. **Отправка запроса и обработка ответа**: Отправляет POST-запрос на URL `f"{cls.conversation_url}/{conversation.conversationId}"` с данными и обрабатывает ответ, извлекая токены, заголовки или финальные ответы из JSON-данных.
10. **Генерация результатов**: Генерирует токены, заголовки или завершает работу в зависимости от типа данных, полученных из ответа.

```
Получение имени модели
    │
    └─── Подготовка заголовков
         │
         └─── Создание сессии
              │
              └─── Обработка системных сообщений
                   │
                   └─── Форматирование входных данных
                        │
                        └─── Инициализация диалога (если необходимо)
                             │
                             └─── Получение ID сообщения
                                  │
                                  └─── Подготовка данных для запроса
                                       │
                                       └─── Отправка запроса и обработка ответа
                                            │
                                            └─── Генерация результатов
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
async def run_generator():
    async for message in CohereForAI_C4AI_Command.create_async_generator(model="command-a", messages=messages):
        print(message)

# asyncio.run(run_generator())