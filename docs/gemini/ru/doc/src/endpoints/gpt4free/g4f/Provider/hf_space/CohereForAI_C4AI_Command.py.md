# Модуль `CohereForAI_C4AI_Command`

## Обзор

Модуль `CohereForAI_C4AI_Command` предоставляет класс `CohereForAI_C4AI_Command`, который является асинхронным провайдером для взаимодействия с моделями CohereForAI C4AI Command. Он позволяет генерировать текст на основе предоставленных сообщений, используя API CohereForAI через HTTP запросы.

## Подробней

Модуль интегрируется с сервисом CohereForAI, используя его API для генерации текста. Он поддерживает различные модели, предоставляемые CohereForAI, и обеспечивает асинхронное взаимодействие для неблокирующей обработки запросов. Класс `CohereForAI_C4AI_Command` наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему использовать общую логику для асинхронных провайдеров и управления моделями.

## Классы

### `CohereForAI_C4AI_Command`

**Описание**: Класс `CohereForAI_C4AI_Command` реализует взаимодействие с моделями CohereForAI C4AI Command. Он позволяет отправлять запросы на генерацию текста и получать результаты в асинхронном режиме.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных провайдеров.
- `ProviderModelMixin`: Предоставляет методы для управления и выбора моделей.

**Атрибуты**:
- `label` (str): Метка провайдера, используемая для идентификации (`"CohereForAI C4AI Command"`).
- `url` (str): URL сервиса CohereForAI (`"https://cohereforai-c4ai-command.hf.space"`).
- `conversation_url` (str): URL для начала диалога (`f"{url}/conversation"`).
- `working` (bool): Флаг, указывающий, что провайдер находится в рабочем состоянии (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`"command-a-03-2025"`).
- `model_aliases` (dict): Словарь псевдонимов моделей для упрощения выбора.
- `models` (list): Список доступных моделей.

**Методы**:
- `get_model(model: str, **kwargs) -> str`: Возвращает имя модели на основе псевдонима или текущего имени.
- `create_async_generator(model: str, messages: Messages, api_key: str = None, proxy: str = None, conversation: JsonConversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `get_model`

```python
@classmethod
def get_model(cls, model: str, **kwargs) -> str:
    """Возвращает имя модели на основе псевдонима или текущего имени.

    Args:
        model (str): Имя модели или псевдоним.
        **kwargs: Дополнительные аргументы.

    Returns:
        str: Имя модели.
    """
    ...
```

**Назначение**: Функция `get_model` позволяет получить полное имя модели на основе предоставленного псевдонима. Если модель указана в списке псевдонимов, возвращается соответствующее значение; в противном случае вызывается метод `get_model` родительского класса.

**Параметры**:
- `model` (str): Имя модели или псевдоним.
- `**kwargs`: Дополнительные аргументы, которые могут быть переданы в метод `get_model` родительского класса.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:
1. **Проверка псевдонима**: Функция проверяет, содержится ли предоставленное имя модели в списке псевдонимов (`cls.model_aliases.values()`).
2. **Возврат модели**: Если имя модели найдено в псевдонимах, функция возвращает его.
3. **Вызов родительского метода**: Если имя модели не найдено в псевдонимах, функция вызывает метод `get_model` родительского класса (`super().get_model(model, **kwargs)`) для обработки.

**ASCII схема работы функции**:

```
Проверка псевдонима модели
│
├───> Модель в псевдонимах?
│     └───> Да: Вернуть имя модели
│     └───> Нет: Вызвать get_model родительского класса
│
Вернуть имя модели
```

**Примеры**:

```python
# Пример 1: Получение имени модели по псевдониму
model_name = CohereForAI_C4AI_Command.get_model("command-r-plus")
print(model_name)  # Вывод: command-r-plus-08-2024

# Пример 2: Получение имени модели, которое уже является полным именем
model_name = CohereForAI_C4AI_Command.get_model("command-r7b-12-2024")
print(model_name)  # Вывод: command-r7b-12-2024
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
            api_key (str, optional): API ключ. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            conversation (JsonConversation, optional): Объект диалога. По умолчанию `None`.
            return_conversation (bool, optional): Возвращать ли объект диалога. По умолчанию `False`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов.
        """
        ...
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для взаимодействия с моделью CohereForAI. Она отправляет сообщения пользователя в API CohereForAI и возвращает асинхронный генератор, который выдает ответы модели по мере их поступления.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений, представляющих историю диалога.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `conversation` (JsonConversation, optional): Объект диалога для поддержания состояния беседы. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, следует ли возвращать объект диалога. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы, передаваемые в базовые методы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы модели.

**Как работает функция**:

1. **Выбор модели**:
   - Функция получает имя модели, используя метод `cls.get_model(model)`. Это позволяет использовать псевдонимы моделей.
2. **Подготовка заголовков**:
   - Создаются заголовки HTTP-запроса, включая `Origin`, `User-Agent`, `Accept`, `Accept-Language`, `Referer`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site` и `Priority`.
   - Если предоставлен `api_key`, он добавляется в заголовок `Authorization`.
3. **Создание сессии**:
   - Создается асинхронная сессия `ClientSession` с использованием подготовленных заголовков и cookies из объекта `conversation`, если он предоставлен.
4. **Обработка системных сообщений**:
   - Извлекаются и объединяются все системные сообщения из списка `messages` в строку `system_prompt`.
   - Оставляются только сообщения, не являющиеся системными.
5. **Форматирование ввода**:
   - Форматируется ввод для запроса. Если `conversation` отсутствует, используется метод `format_prompt(messages)`. В противном случае используется последнее сообщение пользователя из списка `messages`.
6. **Создание или обновление диалога**:
   - Если `conversation` отсутствует или параметры модели/системного промпта изменились, создается новый диалог:
     - Формируются данные запроса (`data`) с использованием `model` и `preprompt` (системный промпт).
     - Отправляется POST-запрос к `cls.conversation_url` с данными `data`.
     - Создается объект `JsonConversation` на основе ответа сервера, включающий cookies для поддержания сессии.
     - Если `return_conversation` равен `True`, объект `conversation` выдается через `yield`.
7. **Получение идентификатора сообщения**:
   - Отправляется GET-запрос к `f"{cls.conversation_url}/{conversation.conversationId}/__data.json?x-sveltekit-invalidated=11"` для получения данных о текущем состоянии диалога.
   - Извлекается идентификатор последнего сообщения (`message_id`) из полученных данных.
8. **Отправка запроса на генерацию**:
   - Создается объект `FormData` с данными для запроса, включающими `inputs` (сформатированный ввод), `id` (идентификатор сообщения), флаги `is_retry`, `is_continue`, `web_search` и `tools`.
   - Отправляется POST-запрос к `f"{cls.conversation_url}/{conversation.conversationId}"` с данными `data`.
9. **Обработка потока ответов**:
   - Читаются данные из потока ответов (`response.content`) по частям (`chunk`).
   - Каждая часть преобразуется в JSON.
   - Если `data["type"]` равно `"stream"`, извлекается текст (`data["token"]`) и выдается через `yield`.
   - Если `data["type"]` равно `"title"`, извлекается заголовок (`data["title"]`) и выдается через `yield` в виде объекта `TitleGeneration`.
   - Если `data["type"]` равно `"finalAnswer"`, цикл завершается.

**ASCII схема работы функции**:

```
Выбор модели
│
Подготовка заголовков
│
Создание сессии
│
Обработка системных сообщений
│
Форматирование ввода
│
Создание или обновление диалога
│
Получение идентификатора сообщения
│
Отправка запроса на генерацию
│
Обработка потока ответов
│
└───> Чтение части ответа (chunk)
│     └───> Преобразование в JSON (data)
│     └───> Проверка типа ответа (data["type"])
│           ├───> "stream": Извлечение и выдача текста (yield data["token"])
│           ├───> "title": Извлечение и выдача заголовка (yield TitleGeneration(data["title"]))
│           └───> "finalAnswer": Завершение цикла
│
Конец
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с минимальными параметрами
messages = [{"role": "user", "content": "Привет, как дела?"}]
generator = CohereForAI_C4AI_Command.create_async_generator(model="command-a", messages=messages)

# Пример 2: Создание асинхронного генератора с API ключом и прокси
messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
generator = CohereForAI_C4AI_Command.create_async_generator(model="command-r", messages=messages, api_key="YOUR_API_KEY", proxy="http://your_proxy:8080")

# Пример 3: Создание асинхронного генератора с существующим диалогом
conversation = JsonConversation(conversationId="123", model="command-a", preprompt="Ты ассистент.")
messages = [{"role": "user", "content": "Продолжи рассказ."}]
generator = CohereForAI_C4AI_Command.create_async_generator(model="command-a", messages=messages, conversation=conversation)