# Модуль для работы с инструментами и API-ключами
## Обзор

Модуль `run_tools.py` предназначен для обработки различных инструментов, используемых в AI-моделях, таких как поиск в интернете, продолжение генерации текста и работа с хранилищем данных (bucket). Он также управляет API-ключами для аутентификации в различных провайдерах AI-моделей. Модуль содержит классы и функции для асинхронного и синхронного выполнения инструментов, а также для обработки промежуточных результатов (thinking chunks).

## Подробней

Этот модуль играет важную роль в расширении возможностей AI-моделей, позволяя им взаимодействовать с внешними ресурсами и выполнять сложные задачи. Он обеспечивает гибкость и расширяемость системы, позволяя подключать различные инструменты и провайдеры AI-моделей.

## Классы

### `ToolHandler`

**Описание**: Класс `ToolHandler` предназначен для обработки различных типов инструментов, используемых в AI-моделях.

**Принцип работы**:
Класс `ToolHandler` предоставляет статические методы для валидации аргументов инструментов, а также для обработки конкретных типов инструментов, таких как поиск в интернете, продолжение генерации текста и работа с хранилищем данных (bucket).

**Методы**:

- `validate_arguments(data: dict) -> dict`: Проверяет и разбирает аргументы инструмента.
- `process_search_tool(messages: Messages, tool: dict) -> Messages`: Обрабатывает запросы инструмента поиска.
- `process_continue_tool(messages: Messages, tool: dict, provider: Any) -> Tuple[Messages, Dict[str, Any]]`: Обрабатывает запросы инструмента продолжения генерации текста.
- `process_bucket_tool(messages: Messages, tool: dict) -> Messages`: Обрабатывает запросы инструмента работы с хранилищем данных (bucket).
- `process_tools(messages: Messages, tool_calls: List[dict], provider: Any) -> Tuple[Messages, Dict[str, Any]]`: Обрабатывает все вызовы инструментов и возвращает обновленные сообщения и аргументы.

#### `validate_arguments`

```python
    @staticmethod
    def validate_arguments(data: dict) -> dict:
        """Validate and parse tool arguments"""
        if "arguments" in data:
            if isinstance(data["arguments"], str):\
                data["arguments"] = json.loads(data["arguments"])\
            if not isinstance(data["arguments"], dict):\
                raise ValueError("Tool function arguments must be a dictionary or a json string")\
            else:\
                return filter_none(**data["arguments"])\
        else:\
            return {}
```

**Назначение**: Проверяет и разбирает аргументы инструмента, представленные в виде словаря или JSON-строки.

**Параметры**:
- `data` (dict): Словарь, содержащий аргументы инструмента.

**Возвращает**:
- `dict`: Словарь с проверенными и разобранными аргументами инструмента.

**Как работает функция**:

1.  Проверяет наличие ключа `"arguments"` в переданном словаре `data`.
2.  Если ключ `"arguments"` присутствует, проверяет, является ли значение по этому ключу строкой. Если да, пытается разобрать JSON-строку в словарь.
3.  Затем проверяет, является ли значение по ключу `"arguments"` словарём. Если нет, вызывает исключение `ValueError`.
4.  Если значение является словарём, применяет функцию `filter_none` для удаления элементов со значением `None` из словаря и возвращает результат.
5.  Если ключа `"arguments"` нет в словаре `data`, возвращает пустой словарь.

**Пример**:

```python
data1 = {"arguments": '{"param1": "value1", "param2": null}'}
result1 = ToolHandler.validate_arguments(data1)
# result1 будет {"param1": "value1"}

data2 = {"arguments": {"param1": "value1", "param2": "value2"}}
result2 = ToolHandler.validate_arguments(data2)
# result2 будет {"param1": "value1", "param2": "value2"}

data3 = {}
result3 = ToolHandler.validate_arguments(data3)
# result3 будет {}
```

#### `process_search_tool`

```python
    @staticmethod
    async def process_search_tool(messages: Messages, tool: dict) -> Messages:
        """Process search tool requests"""
        messages = messages.copy()
        args = ToolHandler.validate_arguments(tool["function"])
        messages[-1]["content"], sources = await do_search(\
            messages[-1]["content"],\
            **args
        )\
        return messages, sources
```

**Назначение**: Обрабатывает запросы инструмента поиска, выполняя поиск в интернете и обновляя сообщения.

**Параметры**:
- `messages` (Messages): Список сообщений.
- `tool` (dict): Словарь, содержащий информацию об инструменте поиска.

**Возвращает**:
- `Messages`: Обновленный список сообщений с результатами поиска.

**Как работает функция**:

1.  Создает копию списка сообщений `messages`.
2.  Извлекает и проверяет аргументы инструмента поиска, используя метод `ToolHandler.validate_arguments`.
3.  Выполняет поиск в интернете, используя функцию `do_search`, передавая последний контент сообщения и аргументы инструмента.
4.  Обновляет контент последнего сообщения в списке `messages` результатами поиска.
5.  Возвращает обновленный список сообщений и источники поиска.

**Пример**:

```python
messages = [{"role": "user", "content": "search for latest news"}]
tool = {"function": {"arguments": {}}}
updated_messages = await ToolHandler.process_search_tool(messages, tool)
# updated_messages будет содержать результаты поиска в последнем сообщении
```

#### `process_continue_tool`

```python
    @staticmethod
    def process_continue_tool(messages: Messages, tool: dict, provider: Any) -> Tuple[Messages, Dict[str, Any]]:
        """Process continue tool requests"""
        kwargs = {}
        if provider not in ("OpenaiAccount", "HuggingFaceAPI"):\
            messages = messages.copy()
            last_line = messages[-1]["content"].strip().splitlines()[-1]\
            content = f"Carry on from this point:\\n{last_line}"
            messages.append({"role": "user", "content": content})\
        else:\
            # Enable provider native continue
            kwargs["action"] = "continue"\
        return messages, kwargs
```

**Назначение**: Обрабатывает запросы инструмента продолжения генерации текста, добавляя контекст для продолжения.

**Параметры**:
- `messages` (Messages): Список сообщений.
- `tool` (dict): Словарь, содержащий информацию об инструменте продолжения.
- `provider` (Any): Провайдер AI-модели.

**Возвращает**:
- `Tuple[Messages, Dict[str, Any]]`: Обновленный список сообщений и дополнительные аргументы.

**Как работает функция**:

1.  Инициализирует пустой словарь `kwargs`.
2.  Проверяет, является ли провайдер одним из `("OpenaiAccount", "HuggingFaceAPI")`.
3.  Если провайдер не входит в список, создает копию списка сообщений `messages`.
4.  Извлекает последнюю строку из контента последнего сообщения.
5.  Формирует новое сообщение с ролью "user", содержащее запрос на продолжение с указанием последней строки.
6.  Добавляет новое сообщение в список `messages`.
7.  Если провайдер входит в список, добавляет аргумент `"action": "continue"` в словарь `kwargs`.
8.  Возвращает обновленный список сообщений и словарь `kwargs`.

**Пример**:

```python
messages = [{"role": "user", "content": "This is the beginning of a story."}]
tool = {}
provider = "SomeOtherProvider"
updated_messages, kwargs = ToolHandler.process_continue_tool(messages, tool, provider)
# updated_messages будет содержать дополнительное сообщение с запросом на продолжение
# kwargs будет пустым словарем

messages = [{"role": "user", "content": "This is the beginning of a story."}]
tool = {}
provider = "OpenaiAccount"
updated_messages, kwargs = ToolHandler.process_continue_tool(messages, tool, provider)
# updated_messages останется без изменений
# kwargs будет содержать {"action": "continue"}
```

#### `process_bucket_tool`

```python
    @staticmethod
    def process_bucket_tool(messages: Messages, tool: dict) -> Messages:
        """Process bucket tool requests"""
        messages = messages.copy()
        
        def on_bucket(match):\
            return "".join(read_bucket(get_bucket_dir(match.group(1))))
            
        has_bucket = False
        for message in messages:\
            if "content" in message and isinstance(message["content"], str):\
                new_message_content = re.sub(r'{"bucket_id":"([^"]*)"}\', on_bucket, message["content"])\
                if new_message_content != message["content"]:\
                    has_bucket = True\
                    message["content"] = new_message_content\

        last_message_content = messages[-1]["content"]      
        if has_bucket and isinstance(last_message_content, str):\
            if "\\nSource: " in last_message_content:\
                messages[-1]["content"] = last_message_content + BUCKET_INSTRUCTIONS
                    
        return messages
```

**Назначение**: Обрабатывает запросы инструмента работы с хранилищем данных (bucket), заменяя идентификаторы хранилищ их содержимым.

**Параметры**:
- `messages` (Messages): Список сообщений.
- `tool` (dict): Словарь, содержащий информацию об инструменте работы с хранилищем.

**Возвращает**:
- `Messages`: Обновленный список сообщений с замененными идентификаторами хранилищ.

**Как работает функция**:

1.  Создает копию списка сообщений `messages`.
2.  Определяет внутреннюю функцию `on_bucket`, которая принимает объект совпадения регулярного выражения и возвращает содержимое хранилища, соответствующего идентификатору в совпадении.
3.  Итерируется по каждому сообщению в списке `messages`.
4.  Если сообщение содержит контент в виде строки, выполняет поиск всех идентификаторов хранилищ в контенте с использованием регулярного выражения.
5.  Заменяет каждый идентификатор хранилища его содержимым, полученным с помощью функции `on_bucket`.
6.  Если были найдены и заменены идентификаторы хранилищ, добавляет инструкцию о добавлении источников цитирования в последнее сообщение, если в нем уже есть указание на источник.
7.  Возвращает обновленный список сообщений.

**Пример**:

```python
messages = [{"role": "user", "content": "Please read this: {\"bucket_id\":\"123\"}"}]
tool = {}
updated_messages = ToolHandler.process_bucket_tool(messages, tool)
# updated_messages будет содержать контент хранилища вместо идентификатора
```

#### `process_tools`

```python
    @staticmethod
    async def process_tools(messages: Messages, tool_calls: List[dict], provider: Any) -> Tuple[Messages, Dict[str, Any]]:
        """Process all tool calls and return updated messages and kwargs"""
        if not tool_calls:\
            return messages, {}\
            
        extra_kwargs = {}\
        messages = messages.copy()
        sources = None
        
        for tool in tool_calls:\
            if tool.get("type") != "function":\
                continue\
                
            function_name = tool.get("function", {}).get("name")\
            
            if function_name == TOOL_NAMES["SEARCH"]:\
                messages, sources = await ToolHandler.process_search_tool(messages, tool)\
                
            elif function_name == TOOL_NAMES["CONTINUE"]:\
                messages, kwargs = ToolHandler.process_continue_tool(messages, tool, provider)\
                extra_kwargs.update(kwargs)\
                
            elif function_name == TOOL_NAMES["BUCKET"]:\
                messages = ToolHandler.process_bucket_tool(messages, tool)\
                
        return messages, sources, extra_kwargs
```

**Назначение**: Обрабатывает все вызовы инструментов в списке `tool_calls` и возвращает обновленные сообщения, источники и дополнительные аргументы.

**Параметры**:
- `messages` (Messages): Список сообщений.
- `tool_calls` (List[dict]): Список словарей, содержащих информацию о вызовах инструментов.
- `provider` (Any): Провайдер AI-модели.

**Возвращает**:
- `Tuple[Messages, Dict[str, Any]]`: Обновленный список сообщений, источники и словарь дополнительных аргументов.

**Как работает функция**:

1.  Если список `tool_calls` пуст, возвращает исходный список сообщений и пустой словарь.
2.  Инициализирует пустой словарь `extra_kwargs` для хранения дополнительных аргументов.
3.  Создает копию списка сообщений `messages`.
4.  Итерируется по каждому вызову инструмента в списке `tool_calls`.
5.  Если тип инструмента не "function", пропускает его.
6.  Извлекает имя функции из информации о вызове инструмента.
7.  В зависимости от имени функции вызывает соответствующий метод для обработки инструмента:
    - `TOOL_NAMES["SEARCH"]`: вызывает `ToolHandler.process_search_tool`.
    - `TOOL_NAMES["CONTINUE"]`: вызывает `ToolHandler.process_continue_tool` и обновляет словарь `extra_kwargs`.
    - `TOOL_NAMES["BUCKET"]`: вызывает `ToolHandler.process_bucket_tool`.
8.  Возвращает обновленный список сообщений, источники и словарь `extra_kwargs`.

**Пример**:

```python
messages = [{"role": "user", "content": "Please search for something."}]
tool_calls = [{"type": "function", "function": {"name": "search_tool", "arguments": {}}}]
provider = "SomeProvider"
updated_messages, sources, extra_kwargs = await ToolHandler.process_tools(messages, tool_calls, provider)
# updated_messages будет содержать результаты поиска
# extra_kwargs будет пустым словарем
```

### `AuthManager`

**Описание**: Класс `AuthManager` предназначен для управления API-ключами.

**Принцип работы**:
Класс `AuthManager` предоставляет статические методы для получения пути к файлу с API-ключом и загрузки API-ключа из файла конфигурации.

**Методы**:

- `get_api_key_file(cls) -> Path`: Получает путь к файлу API-ключа для провайдера.
- `load_api_key(provider: Any) -> Optional[str]`: Загружает API-ключ из файла конфигурации, если необходимо.

#### `get_api_key_file`

```python
    @staticmethod
    def get_api_key_file(cls) -> Path:\
        """Get the path to the API key file for a provider"""
        return Path(get_cookies_dir()) / f"api_key_{cls.parent if hasattr(cls, 'parent') else cls.__name__}.json"
```

**Назначение**: Возвращает путь к файлу, в котором хранится API-ключ для указанного провайдера.

**Параметры**:

*   `cls`: Класс провайдера, для которого требуется получить путь к файлу API-ключа.

**Возвращает**:

*   `Path`: Объект `Path`, представляющий путь к файлу API-ключа.

**Как работает функция**:

1.  Получает директорию для хранения cookie-файлов с помощью функции `get_cookies_dir()`.
2.  Формирует имя файла API-ключа на основе имени класса провайдера (или имени родительского класса, если у класса есть атрибут `parent`).
3.  Соединяет директорию cookie-файлов и имя файла API-ключа в объект `Path` и возвращает его.

**Пример**:

```python
class MyProvider:
    pass

api_key_file_path = AuthManager.get_api_key_file(MyProvider)
# api_key_file_path будет Path('/path/to/cookies/api_key_MyProvider.json')
```

#### `load_api_key`

```python
    @staticmethod
    def load_api_key(provider: Any) -> Optional[str]:
        """Load API key from config file if needed"""
        if not getattr(provider, "needs_auth", False):\
            return None\
            
        auth_file = AuthManager.get_api_key_file(provider)\
        try:\
            if auth_file.exists():\
                with auth_file.open("r") as f:\
                    auth_result = json.load(f)\
                return auth_result.get("api_key")\
        except (json.JSONDecodeError, PermissionError, FileNotFoundError) as e:\
            debug.error(f"Failed to load API key: {e.__class__.__name__}: {e}")\
        return None
```

**Назначение**: Загружает API-ключ из файла конфигурации, если это необходимо для указанного провайдера.

**Параметры**:

*   `provider`: Провайдер, для которого требуется загрузить API-ключ.

**Возвращает**:

*   `Optional[str]`: API-ключ в виде строки, если он найден и требуется для провайдера; в противном случае - `None`.

**Как работает функция**:

1.  Проверяет, требуется ли аутентификация для указанного провайдера, используя функцию `getattr(provider, "needs_auth", False)`. Если аутентификация не требуется, возвращает `None`.
2.  Получает путь к файлу API-ключа для провайдера с помощью функции `AuthManager.get_api_key_file(provider)`.
3.  Пытается открыть файл API-ключа и загрузить из него JSON-данные.
4.  Если файл существует и JSON-данные успешно загружены, извлекает API-ключ из JSON-данных по ключу `"api_key"` и возвращает его.
5.  Если при открытии или загрузке файла возникают исключения (`json.JSONDecodeError`, `PermissionError`, `FileNotFoundError`), перехватывает их, логирует сообщение об ошибке с использованием `debug.error()` и продолжает выполнение.
6.  Если API-ключ не найден или произошла ошибка при загрузке, возвращает `None`.

**Пример**:

```python
class MyProvider:
    needs_auth = True

    def __init__(self):
        # Создаем фейковый файл API-ключа для теста
        api_key_file = AuthManager.get_api_key_file(self)
        api_key_file.write_text('{"api_key": "test_api_key"}')

provider = MyProvider()
api_key = AuthManager.load_api_key(provider)
# api_key будет "test_api_key"
```

### `ThinkingProcessor`

**Описание**: Класс `ThinkingProcessor` предназначен для обработки "размышляющих" фрагментов текста, выделяя этапы мышления и обычный текст.

**Принцип работы**: Класс использует статический метод `process_thinking_chunk` для анализа текстовых фрагментов на наличие специальных тегов `<think>` и `</think>`, которые обозначают начало и конец этапа "размышления". На основе этих тегов фрагменты текста разделяются на части, представляющие обычный текст, начало размышления, продолжение размышления и завершение размышления. Для каждого этапа создаются объекты `Reasoning`, которые содержат соответствующую информацию.

**Методы**:

- `process_thinking_chunk(chunk: str, start_time: float = 0) -> Tuple[float, List[Union[str, Reasoning]]]`: Обрабатывает фрагмент текста и возвращает время и результаты обработки.

#### `process_thinking_chunk`

```python
    @staticmethod
    def process_thinking_chunk(chunk: str, start_time: float = 0) -> Tuple[float, List[Union[str, Reasoning]]]:
        """Process a thinking chunk and return timing and results."""
        results = []
        
        # Handle non-thinking chunk
        if not start_time and "<think>" not in chunk and "</think>" not in chunk:\
            return 0, [chunk]
            
        # Handle thinking start
        if "<think>" in chunk and "`<think>`" not in chunk:\
            before_think, *after = chunk.split("<think>", 1)\
            
            if before_think:\
                results.append(before_think)\
                
            results.append(Reasoning(status="🤔 Is thinking...", is_thinking="<think>"))\
            
            if after:\
                if "</think>" in after[0]:\
                    after, *after_end = after[0].split("</think>", 1)\
                    results.append(Reasoning(after))\
                    results.append(Reasoning(status="Finished", is_thinking="</think>"))\
                    if after_end:\
                        results.append(after_end[0])\
                    return 0, results\
                else:\
                    results.append(Reasoning(after[0]))\
                
            return time.time(), results\
            
        # Handle thinking end
        if "</think>" in chunk:\
            before_end, *after = chunk.split("</think>", 1)\
            
            if before_end:\
                results.append(Reasoning(before_end))\
                
            thinking_duration = time.time() - start_time if start_time > 0 else 0\
            
            status = f"Thought for {thinking_duration:.2f}s" if thinking_duration > 1 else "Finished"\
            results.append(Reasoning(status=status, is_thinking="</think>"))\
            
            # Make sure to handle text after the closing tag
            if after and after[0].strip():\
                results.append(after[0])\
                
            return 0, results\
            
        # Handle ongoing thinking
        if start_time:\
            return start_time, [Reasoning(chunk)]\
            
        return start_time, [chunk]
```

**Назначение**: Обрабатывает фрагмент текста, содержащий этапы "размышления", и возвращает результаты обработки и время начала размышления.

**Параметры**:

*   `chunk` (str): Фрагмент текста для обработки.
*   `start_time` (float, optional): Время начала этапа "размышления". По умолчанию равно 0.

**Возвращает**:

*   `Tuple[float, List[Union[str, Reasoning]]]`: Кортеж, содержащий:

    *   Время начала этапа "размышления" (float).
    *   Список результатов обработки, каждый элемент которого может быть строкой (обычный текст) или объектом `Reasoning` (этап "размышления").

**Как работает функция**:

1.  Инициализирует пустой список `results` для хранения результатов обработки.
2.  Проверяет, является ли текущий фрагмент обычным текстом (не содержит тегов `<think>` и `</think>`). Если `start_time` равно 0 и теги отсутствуют, возвращает 0 и список, содержащий исходный фрагмент.
3.  Проверяет, начинается ли этап "размышления" (содержит тег `<think>`).
    *   Если тег `<think>` найден и не экранирован (т.е. не является `` `<think>` ``), разделяет фрагмент на части до и после тега.
    *   Добавляет текст до тега (если он есть) в список `results`.
    *   Добавляет объект `Reasoning` с информацией о начале этапа "размышления" в список `results`.
    *   Если после тега есть текст, проверяет, содержит ли он закрывающий тег `</think>`.
        *   Если закрывающий тег найден, разделяет текст после `<think>` на части до и после `</think>`.
        *   Добавляет объект `Reasoning` с текстом между тегами в список `results`.
        *   Добавляет объект `Reasoning` с информацией о завершении этапа "размышления" в список `results`.
        *   Добавляет текст после `</think>` (если он есть) в список `results`.
        *   Возвращает 0 и список `results`.
        *   Если закрывающий тег не найден, добавляет объект `Reasoning` с текстом после `<think>` в список `results`.
        *   Возвращает текущее время и список `results`.
4.  Проверяет, заканчивается ли этап "размышления" (содержит тег `</think>`).
    *   Если тег `</think>` найден, разделяет фрагмент на части до и после тега.
    *   Добавляет текст до тега (если он есть) в список `results`.
    *   Вычисляет продолжительность этапа "размышления" на основе `start_time`.
    *   Добавляет объект `Reasoning` с информацией о завершении этапа "размышления` в список `results`.
    *   Добавляет текст после `</think>` (если он есть) в список `results`.
    *   Возвращает 0 и список `results`.
5.  Если `start_time` не равно 0, добавляет объект `Reasoning` с текущим фрагментом в список `results` и возвращает `start_time` и список `results`.
6.  Если ни одно из условий не выполнено, возвращает `start_time` и список, содержащий исходный фрагмент.

**Примеры**:

```python
# Пример 1: Обычный текст
chunk = "This is a simple text."
start_time = 0
start_time, results = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
# start_time = 0
# results = ["This is a simple text."]

# Пример 2: Начало этапа "размышления"
chunk = "Some text before <think> the thinking part"
start_time = 0
start_time, results = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
# start_time = <current_time>
# results = ["Some text before ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning(after=' the thinking part')]

# Пример 3: Завершение этапа "размышления"
chunk = "the thinking part</think> and some text after"
start_time = <some_time>
start_time, results = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
# start_time = 0
# results = [Reasoning(before_end='the thinking part'), Reasoning(status="Finished", is_thinking="</think>"), ' and some text after']
```

## Функции

### `perform_web_search`

```python
async def perform_web_search(messages: Messages, web_search_param: Any) -> Tuple[Messages, Optional[Sources]]:
    """Perform web search and return updated messages and sources"""
    messages = messages.copy()
    sources = None
    
    if not web_search_param:\
        return messages, sources\
        
    try:\
        search_query = web_search_param if isinstance(web_search_param, str) and web_search_param != "true" else None
        messages[-1]["content"], sources = await do_search(messages[-1]["content"], search_query)\
    except Exception as e:\
        debug.error(f"Couldn\'t do web search: {e.__class__.__name__}: {e}")\
        
    return messages, sources
```

**Назначение**: Выполняет поиск в интернете и возвращает обновленные сообщения и источники.

**Параметры**:
- `messages` (Messages): Список сообщений.
- `web_search_param` (Any): Параметр для поиска в интернете.

**Возвращает**:
- `Tuple[Messages, Optional[Sources]]`: Кортеж, содержащий обновленный список сообщений и источники поиска (если есть).

**Как работает функция**:

1.  Создает копию списка сообщений `messages`.
2.  Если параметр `web_search_param` не задан, возвращает исходный список сообщений и `None`.
3.  Определяет поисковый запрос: если `web_search_param` является строкой и не равен `"true"`, использует его в качестве запроса; в противном случае устанавливает запрос в `None`.
4.  Выполняет поиск в интернете, используя функцию `do_search`, передавая контент последнего сообщения и поисковый запрос.
5.  Обновляет контент последнего сообщения в списке `messages` результатами поиска.
6.  Если во время поиска возникает исключение, логирует сообщение об ошибке с использованием `debug.error()`.
7.  Возвращает обновленный список сообщений и источники поиска.

**Пример**:

```python
messages = [{"role": "user", "content": "Tell me about the weather in London"}]
web_search_param = "weather in London"
updated_messages, sources = await perform_web_search(messages, web_search_param)
# updated_messages будет содержать информацию о погоде в Лондоне
# sources будет содержать источники информации
```

### `async_iter_run_tools`

```python
async def async_iter_run_tools(\
    provider: ProviderType, \
    model: str, \
    messages: Messages, \
    tool_calls: Optional[List[dict]] = None, \
    **kwargs\
) -> AsyncIterator:\
    """Asynchronously run tools and yield results"""
    # Process web search
    sources = None
    web_search = kwargs.get('web_search')\
    if web_search:\
        messages, sources = await perform_web_search(messages, web_search)\
    
    # Get API key if needed
    api_key = AuthManager.load_api_key(provider)\
    if api_key and "api_key" not in kwargs:\
        kwargs["api_key"] = api_key\
    
    # Process tool calls
    if tool_calls:\
        messages, sources, extra_kwargs = await ToolHandler.process_tools(messages, tool_calls, provider)\
        kwargs.update(extra_kwargs)\
    
    # Generate response
    create_function = provider.get_async_create_function()\
    response = to_async_iterator(create_function(model=model, messages=messages, **kwargs))\
    
    async for chunk in response:\
        yield chunk\
        
    # Yield sources if available
    if sources:\
        yield sources
```

**Назначение**: Асинхронно выполняет инструменты и возвращает результаты в виде асинхронного итератора.

**Параметры**:

*   `provider` (`ProviderType`): Провайдер AI-модели.
*   `model` (`str`): Имя модели AI.
*   `messages` (`Messages`): Список сообщений для обработки.
*   `tool_calls` (`Optional[List[dict]]`, optional): Список вызовов инструментов. По умолчанию `None`.
*   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

*   `AsyncIterator`: Асинхронный итератор, возвращающий результаты выполнения инструментов.

**Как работает функция**:

1.  Выполняет поиск в интернете, если задан параметр `web_search` в `kwargs`.
2.  Загружает API-ключ для провайдера, если это необходимо.
3.  Обрабатывает вызовы инструментов, используя `ToolHandler.process_tools`.
4.  Получает функцию для генерации ответа от провайдера и преобразует ее в асинхронный итератор.
5.  Итерируется по ответам, полученным от провайдера, и возвращает их.
6.  Если есть источники, полученные в результате поиска, возвращает их.

**Примеры**:

```python
provider = MyProvider()
model = "my_model"
messages = [{"role": "user", "content": "Tell me a joke"}]
tool_calls = None
kwargs = {"web_search": "joke"}

async for chunk in async_iter_run_tools(provider, model, messages, tool_calls, **kwargs):
    print(chunk)
```

```ascii
  web_search = kwargs.get('web_search')
  │
  ├───> web_search is not None:
  │     │
  │     └───> perform_web_search(messages, web_search)
  │           │
  │           ├───> messages = messages.copy()
  │           │
  │           ├───> perform do_search(...)
  │           │
  │           └───> messages[-1]["content"], sources = ...
  │
  └───> web_search is None:
        │
        └───> pass

  api_key = AuthManager.load_api_key(provider)
  │
  ├───> api_key is not None and "api_key" not in kwargs:
  │     │
  │     └───> kwargs["api_key"] = api_key
  │
  └───> not (api_key is not None and "api_key" not in kwargs):
        │
        └───> pass

  tool_calls is not None
  │
  ├───> tool_calls is not None:
  │     │
  │     └───> ToolHandler.process_tools(messages, tool_calls, provider)
  │           │
  │           ├───> tool_calls is empty:
  │           │     └───> return messages, {}
  │           │
  │           └───> tool_calls is not empty:
  │                 │
  │                 └───> iterate tool_calls and process each tool
  │                       │
  │                       └───> messages, sources, extra_kwargs = ...
  │
  └───> tool_calls is None:
        │
        └───> pass

  create_function = provider.get_async_create_function()

  response = to_async_iterator(create_function(model=model, messages=messages, **kwargs))

  iterate response and yield each chunk

  sources is not None
  │
  └───> yield sources
```

### `iter_run_tools`

```python
def iter_run_tools(\
    iter_callback: Callable,\
    model: str,\
    messages: Messages,\
    provider: Optional[str] = None,\
    tool_calls: Optional[List[dict]] = None,\
    **kwargs\
) -> Iterator:\
    """Run tools synchronously and yield results"""
    # Process web search
    web_search = kwargs.get('web_search