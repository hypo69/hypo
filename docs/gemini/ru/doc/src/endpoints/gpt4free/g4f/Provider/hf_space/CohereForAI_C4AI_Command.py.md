# Модуль `CohereForAI_C4AI_Command.py`

## Обзор

Модуль `CohereForAI_C4AI_Command.py` предназначен для взаимодействия с моделями CohereForAI C4AI Command через Hugging Face Space. Он предоставляет асинхронный генератор для получения ответов от модели и поддерживает управление состоянием разговора.

## Подробнее

Модуль обеспечивает возможность обмена сообщениями с моделями CohereForAI C4AI Command, используя асинхронные запросы. Он включает в себя функциональность для создания и поддержания контекста разговора, а также обработки ответов от модели в реальном времени. Модуль также поддерживает выбор различных моделей CohereForAI и передачу ключа API для аутентификации.

## Классы

### `CohereForAI_C4AI_Command`

**Описание**: Класс `CohereForAI_C4AI_Command` предоставляет функциональность для взаимодействия с моделями CohereForAI C4AI Command через Hugging Face Space.

**Принцип работы**:
Класс использует асинхронные запросы для обмена сообщениями с моделью CohereForAI C4AI Command. Он поддерживает создание и поддержание контекста разговора, а также обработку ответов от модели в реальном времени.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера, `"CohereForAI C4AI Command"`.
- `url` (str): URL Hugging Face Space, `"https://cohereforai-c4ai-command.hf.space"`.
- `conversation_url` (str): URL для ведения разговоров, формируется из `url`.
- `working` (bool): Указывает, работает ли провайдер, `True`.
- `default_model` (str): Модель по умолчанию, `"command-a-03-2025"`.
- `model_aliases` (dict): Словарь псевдонимов моделей.
- `models` (list): Список доступных моделей, формируется из ключей `model_aliases`.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает имя модели на основе псевдонима.
- `create_async_generator(model: str, messages: Messages, api_key: str = None, proxy: str = None, conversation: JsonConversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        """Возвращает имя модели на основе псевдонима.

        Args:
            model (str): Имя модели или псевдоним.
            **kwargs: Дополнительные аргументы.

        Returns:
            str: Имя модели.
        """
        ...
```

**Назначение**:
Функция `get_model` предназначена для получения полного имени модели на основе предоставленного псевдонима. Если предоставленное имя модели содержится в списке псевдонимов, функция возвращает соответствующее значение. В противном случае вызывается метод `get_model` родительского класса для обработки имени модели.

**Как работает функция**:

1. **Проверка псевдонима**: Проверяется, содержится ли предоставленное имя модели в словаре `model_aliases`.
2. **Возврат имени модели**: Если имя модели найдено в списке псевдонимов, возвращается соответствующее значение.
3. **Вызов родительского метода**: Если имя модели не найдено в списке псевдонимов, вызывается метод `get_model` родительского класса для обработки имени модели.

```
A: Проверка наличия модели в model_aliases
|
B: Возврат значения из model_aliases
|
C: Вызов get_model родительского класса
```

**Примеры**:

```python
# Пример 1: Получение имени модели по псевдониму
model_name = CohereForAI_C4AI_Command.get_model("command-r")
print(model_name)

# Пример 2: Получение имени модели, которое уже является полным именем
model_name = CohereForAI_C4AI_Command.get_model("command-a-03-2025")
print(model_name)
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
            messages (Messages): Список сообщений для отправки.
            api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            conversation (JsonConversation, optional): Объект разговора для поддержания контекста. По умолчанию `None`.
            return_conversation (bool, optional): Возвращать ли объект разговора. По умолчанию `False`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов от модели.
        """
        ...
```

**Назначение**:
Функция `create_async_generator` создает асинхронный генератор для получения ответов от указанной модели CohereForAI C4AI Command. Она устанавливает соединение с Hugging Face Space, отправляет сообщения и обрабатывает ответы в реальном времени.

**Как работает функция**:

1. **Получение имени модели**: Вызывается функция `get_model` для получения полного имени модели.
2. **Формирование заголовков**: Формируются заголовки HTTP-запроса, включая `Origin`, `User-Agent`, `Accept`, `Accept-Language`, `Referer`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site` и `Priority`.
3. **Добавление ключа API (если есть)**: Если предоставлен ключ API, он добавляется в заголовок `Authorization`.
4. **Создание асинхронной сессии**: Создается асинхронная сессия `ClientSession` с установленными заголовками и куками (если есть объект разговора).
5. **Обработка системных сообщений**: Из списка сообщений извлекаются системные сообщения и объединяются в строку `system_prompt`.
6. **Форматирование сообщений**: Форматируются сообщения для отправки в запросе.
7. **Создание или обновление разговора**:
   - Если объект разговора отсутствует или модель/системный промпт изменились, отправляется запрос на создание нового разговора.
   - В противном случае используется существующий объект разговора.
8. **Получение ID сообщения**: Получается ID последнего сообщения в разговоре.
9. **Формирование данных для запроса**: Формируются данные для отправки в запросе, включая входные данные, ID сообщения и флаги.
10. **Отправка запроса и обработка ответов**:
    - Отправляется POST-запрос с данными на URL разговора.
    - Асинхронно обрабатываются чанки ответа.
    - Если тип чанка `"stream"`, извлекается токен и возвращается.
    - Если тип чанка `"title"`, извлекается заголовок и возвращается объект `TitleGeneration`.
    - Если тип чанка `"finalAnswer"`, обработка завершается.
11. **Обработка ошибок**: Если происходит ошибка при чтении ответа, выбрасывается исключение `RuntimeError`.

```
A: Получение имени модели
|
B: Формирование заголовков
|
C: Создание асинхронной сессии
|
D: Обработка системных сообщений
|
E: Форматирование сообщений
|
F: Создание или обновление разговора
|
G: Получение ID сообщения
|
H: Формирование данных для запроса
|
I: Отправка запроса и обработка ответов
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с минимальными параметрами
messages = [{"role": "user", "content": "Hello, model!"}]
generator = CohereForAI_C4AI_Command.create_async_generator(model="command-a", messages=messages)

# Пример 2: Создание асинхронного генератора с ключом API и прокси
messages = [{"role": "user", "content": "Hello, model!"}]
generator = CohereForAI_C4AI_Command.create_async_generator(
    model="command-a", messages=messages, api_key="YOUR_API_KEY", proxy="http://your-proxy:8080"
)

# Пример 3: Создание асинхронного генератора с существующим разговором
conversation = JsonConversation(conversationId="123", model="command-a", preprompt="You are a helpful assistant.")
messages = [{"role": "user", "content": "Continue the conversation."}]
generator = CohereForAI_C4AI_Command.create_async_generator(
    model="command-a", messages=messages, conversation=conversation
)