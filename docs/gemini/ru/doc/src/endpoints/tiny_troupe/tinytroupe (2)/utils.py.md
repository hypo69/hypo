# Модуль `utils.py`

## Обзор

Модуль содержит набор общих утилит и вспомогательных функций, используемых в проекте `tinytroupe`. Он включает функции для работы с моделями LLM, обработки текста, валидации данных, prompt engineering, IO, логирования и JSON сериализации.

## Подробней

Этот модуль предоставляет набор инструментов для упрощения различных задач, таких как:
- Композиция сообщений для языковых моделей (LLM).
- Извлечение JSON и code blocks из текста.
- Повторный вызов функций при возникновении ошибок.
- Валидация и санитарная обработка строк и словарей.
- Работа с RAI (Responsible AI) шаблонами.
- Манипуляции с HTML и текстом.
- Чтение и обработка конфигурационных файлов.
- JSON сериализация и десериализация объектов.

## Функции

### `compose_initial_LLM_messages_with_templates`

```python
def compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}) -> list:
    """
    Composes the initial messages for the LLM model call, under the assumption that it always involves 
    a system (overall task description) and an optional user message (specific task description). 
    These messages are composed using the specified templates and rendering configurations.
    
    Args:
        system_template_name (str): Имя шаблона системного сообщения.
        user_template_name (str, optional): Имя шаблона пользовательского сообщения. По умолчанию `None`.
        rendering_configs (dict, optional): Словарь с конфигурациями для рендеринга шаблонов. По умолчанию `{}`.

    Returns:
        list: Список сообщений для LLM, содержащий системное сообщение и, возможно, пользовательское сообщение.

    Как работает функция:
    1. Формирует пути к шаблонам системного и пользовательского сообщений.
    2. Инициализирует пустой список `messages`.
    3. Добавляет в список системное сообщение, полученное путем рендеринга шаблона системного сообщения с использованием библиотеки `chevron` и переданных конфигураций рендеринга.
    4. Если указано имя шаблона пользовательского сообщения, добавляет в список пользовательское сообщение, полученное путем рендеринга шаблона пользовательского сообщения с использованием библиотеки `chevron` и переданных конфигураций рендеринга.
    5. Возвращает список сообщений.
    """
    ...
```

**Как работает функция**:

```
A: Формирование путей к шаблонам
|
B: Инициализация списка сообщений
|
C: Рендеринг системного сообщения
|
D: Добавление системного сообщения в список
|
E: Проверка наличия шаблона пользовательского сообщения
|
F: Рендеринг пользовательского сообщения (если есть)
|
G: Добавление пользовательского сообщения в список (если есть)
|
H: Возврат списка сообщений
```

**Примеры**:

```python
# Пример 1: Только системное сообщение
messages = compose_initial_LLM_messages_with_templates(system_template_name='system.txt', rendering_configs={'task': 'summarize'})

# Пример 2: Системное и пользовательское сообщение
messages = compose_initial_LLM_messages_with_templates(system_template_name='system.txt', user_template_name='user.txt', rendering_configs={'task': 'translate'})

# Пример 3: Без конфигураций рендеринга
messages = compose_initial_LLM_messages_with_templates(system_template_name='system.txt')
```

### `extract_json`

```python
def extract_json(text: str) -> dict:
    """
    Extracts a JSON object from a string, ignoring: any text before the first 
    opening curly brace; and any Markdown opening (```json) or closing(```) tags.
    
    Args:
        text (str): Строка, из которой нужно извлечь JSON.

    Returns:
        dict: Извлеченный JSON объект в виде словаря. Возвращает пустой словарь, если извлечение не удалось.

    Как работает функция:
    1. Удаляет весь текст до первой открывающей фигурной или квадратной скобки.
    2. Удаляет весь текст после последней закрывающей фигурной или квадратной скобки.
    3. Заменяет некорректные escape-последовательности (`\\'`) на одинарные кавычки (`'`).
    4. Пытается распарсить полученный текст как JSON.
    5. В случае успеха возвращает полученный словарь, иначе - пустой словарь.
    """
    ...
```

**Как работает функция**:

```
A: Удаление текста до первой скобки
|
B: Удаление текста после последней скобки
|
C: Замена некорректных escape-последовательностей
|
D: Попытка распарсить JSON
|
E: Возврат JSON объекта или пустого словаря в случае ошибки
```

**Примеры**:

```python
# Пример 1: Извлечение JSON из строки
json_data = extract_json('Some text {"key": "value"}')

# Пример 2: Строка без JSON
json_data = extract_json('Some text without JSON')

# Пример 3: JSON с некорректными escape-последовательностями
json_data = extract_json('{\'key\': \\\'value\\\'}')
```

### `extract_code_block`

```python
def extract_code_block(text: str) -> str:
    """
    Extracts a code block from a string, ignoring any text before the first 
    opening triple backticks and any text after the closing triple backticks.
    
    Args:
        text (str): Строка, из которой нужно извлечь code block.

    Returns:
        str: Извлеченный code block. Возвращает пустую строку, если извлечение не удалось.

    Как работает функция:
    1. Удаляет весь текст до первого набора из трех обратных кавычек (```).
    2. Удаляет весь текст после последнего набора из трех обратных кавычек (```).
    3. Возвращает полученный code block. В случае ошибки возвращает пустую строку.
    """
    ...
```

**Как работает функция**:

```
A: Удаление текста до первого ```
|
B: Удаление текста после последнего ```
|
C: Возврат code block или пустой строки в случае ошибки
```

**Примеры**:

```python
# Пример 1: Извлечение code block из строки
code = extract_code_block('Some text ```python\nprint("Hello")\n```')

# Пример 2: Строка без code block
code = extract_code_block('Some text without code block')
```

### `repeat_on_error`

```python
def repeat_on_error(retries: int, exceptions: list):
    """
    Decorator that repeats the specified function call if an exception among those specified occurs, 
    up to the specified number of retries. If that number of retries is exceeded, the
    exception is raised. If no exception occurs, the function returns normally.
    
    Args:
        retries (int): The number of retries to attempt.
        exceptions (list): The list of exception classes to catch.
    """
    ...
```

**Как работает функция**:

```
A: Определение декоратора
|
B: Определение wrapper-функции
|
C: Цикл повторных попыток
|
D: Вызов декорируемой функции
|
E: Обработка исключения
|
F: Логирование исключения
|
G: Проверка количества попыток
|
H: Повторный вызов или поднятие исключения
|
I: Возврат результата функции в случае успеха
```

**Примеры**:

```python
# Пример 1: Повторный вызов функции при ошибке ValueError или TypeError
@repeat_on_error(retries=3, exceptions=[ValueError, TypeError])
def my_function():
    ...

# Пример 2: Повторный вызов функции при любой ошибке Exception
@repeat_on_error(retries=2, exceptions=[Exception])
def another_function():
    ...
```

### `check_valid_fields`

```python
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Checks whether the fields in the specified dict are valid, according to the list of valid fields. If not, raises a ValueError.
    
    Args:
        obj (dict): Проверяемый словарь.
        valid_fields (list): Список допустимых ключей.

    Raises:
        ValueError: Если в словаре `obj` есть недопустимые ключи.

    Как работает функция:
    1. Итерируется по ключам в словаре `obj`.
    2. Для каждого ключа проверяет, содержится ли он в списке `valid_fields`.
    3. Если ключ отсутствует в списке допустимых ключей, вызывается исключение `ValueError` с сообщением об ошибке.
    """
    ...
```

**Как работает функция**:

```
A: Итерация по ключам словаря
|
B: Проверка ключа на допустимость
|
C: Вызов исключения ValueError (если ключ недопустим)
```

**Примеры**:

```python
# Пример 1: Проверка допустимых полей в словаре
data = {'name': 'John', 'age': 30, 'city': 'New York'}
valid_keys = ['name', 'age']
check_valid_fields(data, valid_keys)  # Вызовет ValueError, так как 'city' отсутствует в valid_keys

# Пример 2: Все поля допустимы
data = {'name': 'John', 'age': 30}
valid_keys = ['name', 'age', 'city']
check_valid_fields(data, valid_keys)  # Не вызовет исключение
```

### `sanitize_raw_string`

```python
def sanitize_raw_string(value: str) -> str:
    """
    Sanitizes the specified string by: 
      - removing any invalid characters.
      - ensuring it is not longer than the maximum Python string length.
    
    This is for an abundance of caution with security, to avoid any potential issues with the string.
    
    Args:
        value (str): Строка для санитарной обработки.

    Returns:
        str: Санитарно обработанная строка.

    Как работает функция:
    1. Удаляет все недопустимые символы, кодируя строку в UTF-8 и декодируя обратно, игнорируя ошибки.
    2. Укорачивает строку до максимальной длины, поддерживаемой Python.
    3. Возвращает санитарно обработанную строку.
    """
    ...
```

**Как работает функция**:

```
A: Удаление недопустимых символов
|
B: Укорачивание строки до максимальной длины
|
C: Возврат санитарно обработанной строки
```

**Примеры**:

```python
# Пример 1: Санитарная обработка строки с недопустимыми символами
text = "Hello\x00World!"
sanitized_text = sanitize_raw_string(text)  # sanitized_text будет "HelloWorld!"

# Пример 2: Санитарная обработка длинной строки
long_text = "A" * (sys.maxsize + 100)
sanitized_text = sanitize_raw_string(long_text)  # sanitized_text будет усечена до sys.maxsize
```

### `sanitize_dict`

```python
def sanitize_dict(value: dict) -> dict:
    """
    Sanitizes the specified dictionary by:
      - removing any invalid characters.
      - ensuring that the dictionary is not too deeply nested.
    
    Args:
        value (dict): Словарь для санитарной обработки.

    Returns:
        dict: Санитарно обработанный словарь.

    Как работает функция:
    1. Преобразует словарь в строку JSON.
    2. Санирует полученную строку с помощью функции `sanitize_raw_string`.
    3. Преобразует санированную строку обратно в словарь JSON.
    4. Возвращает санитарно обработанный словарь.
    """
    ...
```

**Как работает функция**:

```
A: Преобразование словаря в JSON строку
|
B: Санитарная обработка JSON строки
|
C: Преобразование JSON строки обратно в словарь
|
D: Возврат санитарно обработанного словаря
```

**Примеры**:

```python
# Пример 1: Санитарная обработка словаря с недопустимыми символами
data = {"name": "John\x00", "age": 30}
sanitized_data = sanitize_dict(data)  # sanitized_data будет {"name": "John", "age": 30}

# Пример 2: Санитарная обработка вложенного словаря
data = {"name": "John", "details": {"city": "New York\x00"}}
sanitized_data = sanitize_dict(data)  # sanitized_data будет {"name": "John", "details": {"city": "New York"}}
```

### `add_rai_template_variables_if_enabled`

```python
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Adds the RAI template variables to the specified dictionary, if the RAI disclaimers are enabled.
    These can be configured in the config.ini file. If enabled, the variables will then load the RAI disclaimers from the 
    appropriate files in the prompts directory. Otherwise, the variables will be set to None.
    
    Args:
        template_variables (dict): The dictionary of template variables to add the RAI variables to.

    Returns:
        dict: The updated dictionary of template variables.

    Как работает функция:
    1. Импортирует модуль `config` из `tinytroupe` для избежания циклического импорта.
    2. Определяет, включена ли опция предотвращения вредоносного контента (RAI_HARMFUL_CONTENT_PREVENTION) в конфигурационном файле.
    3. Определяет, включена ли опция предотвращения нарушения авторских прав (RAI_COPYRIGHT_INFRINGEMENT_PREVENTION) в конфигурационном файле.
    4. Если опция предотвращения вредоносного контента включена, считывает содержимое файла `rai_harmful_content_prevention.md` и добавляет его в словарь `template_variables` под ключом `rai_harmful_content_prevention`. В противном случае, устанавливает значение `None` для этого ключа.
    5. Если опция предотвращения нарушения авторских прав включена, считывает содержимое файла `rai_copyright_infringement_prevention.md` и добавляет его в словарь `template_variables` под ключом `rai_copyright_infringement_prevention`. В противном случае, устанавливает значение `None` для этого ключа.
    6. Возвращает обновленный словарь `template_variables`.
    """
    ...
```

**Как работает функция**:

```
A: Импорт модуля config
|
B: Определение, включена ли опция предотвращения вредоносного контента
|
C: Определение, включена ли опция предотвращения нарушения авторских прав
|
D: Считывание содержимого файла rai_harmful_content_prevention.md (если опция включена)
|
E: Добавление содержимого файла или None в словарь template_variables
|
F: Считывание содержимого файла rai_copyright_infringement_prevention.md (если опция включена)
|
G: Добавление содержимого файла или None в словарь template_variables
|
H: Возврат обновленного словаря template_variables
```

**Примеры**:

```python
# Пример 1: RAI отключены
template_vars = {}
updated_vars = add_rai_template_variables_if_enabled(template_vars)  # updated_vars будет {'rai_harmful_content_prevention': None, 'rai_copyright_infringement_prevention': None}

# Пример 2: RAI включены (предполагается, что файлы существуют и опции включены в config.ini)
template_vars = {}
updated_vars = add_rai_template_variables_if_enabled(template_vars)  # updated_vars будет содержать содержимое файлов
```

### `inject_html_css_style_prefix`

```python
def inject_html_css_style_prefix(html: str, style_prefix_attributes: str) -> str:
    """
    Injects a style prefix to all style attributes in the given HTML string.
    
    For example, if you want to add a style prefix to all style attributes in the HTML string
    ``<div style="color: red;">Hello</div>``, you can use this function as follows:\n    inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')
    """
    ...
```

### `break_text_at_length`

```python
def break_text_at_length(text: str | dict, max_length: int = None) -> str:
    """
    Breaks the text (or JSON) at the specified length, inserting a "(...)" string at the break point.
    If the maximum length is `None`, the content is returned as is.
    
    Args:
        text (str | dict): Текст или JSON для обрезки.
        max_length (int, optional): Максимальная длина текста. По умолчанию `None`.

    Returns:
        str: Обрезанный текст с добавленной строкой "(...)", если длина текста превышает `max_length`. В противном случае возвращает исходный текст.

    Как работает функция:
    1. Проверяет, является ли входной текст словарем. Если да, преобразует его в JSON строку с отступами.
    2. Если `max_length` равен `None` или длина текста меньше или равна `max_length`, возвращает текст без изменений.
    3. Иначе, обрезает текст до `max_length` символов и добавляет в конце строку "(...)".
    """
    ...
```

**Как работает функция**:

```
A: Проверка типа входного текста
|
B: Преобразование словаря в JSON строку (если необходимо)
|
C: Проверка значения max_length
|
D: Возврат исходного текста (если max_length равен None или длина текста меньше или равна max_length)
|
E: Обрезка текста и добавление "(...)" (если длина текста больше max_length)
```

**Примеры**:

```python
# Пример 1: Обрезка длинного текста
text = "This is a very long text that needs to be truncated."
truncated_text = break_text_at_length(text, max_length=20)  # truncated_text будет "This is a very long (...)"

# Пример 2: Текст не требует обрезки
text = "Short text"
truncated_text = break_text_at_length(text, max_length=30)  # truncated_text будет "Short text"

# Пример 3: max_length равен None
text = "Some text"
truncated_text = break_text_at_length(text, max_length=None)  # truncated_text будет "Some text"

# Пример 4: Входной текст - словарь
data = {"name": "John", "age": 30, "city": "New York"}
truncated_text = break_text_at_length(data, max_length=50)  # truncated_text будет "{\n    "name": "John",\n    "age": 30,\n    "city": (...)"
```

### `pretty_datetime`

```python
def pretty_datetime(dt: datetime) -> str:
    """
    Returns a pretty string representation of the specified datetime object.
    
    Args:
        dt (datetime): Объект datetime.

    Returns:
        str: Строковое представление объекта datetime в формате "YYYY-MM-DD HH:MM".

    Как работает функция:
    1. Форматирует объект `datetime` в строку в формате "%Y-%m-%d %H:%M".
    2. Возвращает отформатированную строку.
    """
    ...
```

**Как работает функция**:

```
A: Форматирование объекта datetime
|
B: Возврат отформатированной строки
```

**Примеры**:

```python
# Пример 1: Преобразование datetime в строку
now = datetime.now()
pretty_date = pretty_datetime(now)  # pretty_date будет строкой вида "2023-10-26 15:30"
```

### `dedent`

```python
def dedent(text: str) -> str:
    """
    Dedents the specified text, removing any leading whitespace and identation.
    
    Args:
        text (str): Текст для удаления отступов.

    Returns:
        str: Текст без начальных отступов и пробелов.

    Как работает функция:
    1. Удаляет общие начальные пробелы из каждой строки в тексте с помощью `textwrap.dedent`.
    2. Удаляет начальные и конечные пробельные символы с помощью `strip`.
    3. Возвращает обработанный текст.
    """
    ...
```

**Как работает функция**:

```
A: Удаление общих начальных пробелов
|
B: Удаление начальных и конечных пробелов
|
C: Возврат обработанного текста
```

**Примеры**:

```python
# Пример 1: Удаление отступов из текста
text = "  Hello\n  World"
dedented_text = dedent(text)  # dedented_text будет "Hello\nWorld"
```

### `read_config_file`

```python
def read_config_file(use_cache: bool = True, verbose: bool = True) -> configparser.ConfigParser:
    """
    Reads a configuration file using the configparser module.

    Args:
        use_cache (bool, optional): Whether to use a cached configuration if available. Defaults to True.
        verbose (bool, optional): Whether to print verbose output during configuration loading. Defaults to True.

    Returns:
        configparser.ConfigParser: The configuration object.
    """
    ...
```

### `pretty_print_config`

```python
def pretty_print_config(config):
    """
    Pretty prints the configuration settings.

    Args:
        config: The configuration object.
    """
    ...
```

### `start_logger`

```python
def start_logger(config: configparser.ConfigParser):
    """
    Initializes and configures a logger instance.

    Args:
        config (configparser.ConfigParser): The configuration object containing logger settings.
    """
    ...
```

## Классы

### `JsonSerializableRegistry`

```python
class JsonSerializableRegistry:
    """
    A mixin class that provides JSON serialization, deserialization, and subclass registration.
    """

    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Returns a JSON representation of the object.

        Args:
            include (list, optional): Attributes to include in the serialization.
            suppress (list, optional): Attributes to suppress from the serialization.
            file_path (str, optional): Path to a file where the JSON will be written.
        """
        ...

    @classmethod
    def from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None):
        """
        Loads a JSON representation of the object and creates an instance of the class.

        Args:
            json_dict_or_path (dict or str): The JSON dictionary representing the object or a file path to load the JSON from.
            suppress (list, optional): Attributes to suppress from being loaded.

        Returns:
            An instance of the class populated with the data from json_dict_or_path.
        """
        ...

    def __init_subclass__(cls, **kwargs):
        """
        Registers subclasses and extends serializable attributes and custom initializers from parent classes.

        Args:
            **kwargs: Additional keyword arguments.
        """
        ...

    def _post_deserialization_init(self, **kwargs):
        """
        Post-deserialization initialization method.

        Args:
            **kwargs: Additional keyword arguments.
        """
        ...
```

**Описание**: Mixin-класс, предоставляющий функциональность для JSON-сериализации, десериализации и регистрации подклассов.

**Принцип работы**:
Класс `JsonSerializableRegistry` предназначен для упрощения сериализации и десериализации объектов в JSON-формат. Он предоставляет методы для преобразования объектов в JSON и обратно, а также механизм регистрации подклассов для правильной десериализации.

**Методы**:
- `to_json`: Преобразует объект в JSON-представление.
- `from_json`: Загружает JSON-представление объекта и создает экземпляр класса.
- `__init_subclass__`: Регистрирует подклассы и расширяет атрибуты сериализации и инициализаторы.
- `_post_deserialization_init`: Вызывается после десериализации объекта.

### `post_init`

```python
def post_init(cls):
    """
    Decorator to enforce a post-initialization method call in a class, if it has one.
    The method must be named `_post_init`.
    """
    ...
```

### `name_or_empty`

```python
def name_or_empty(named_entity: AgentOrWorld):
    """
    Returns the name of the specified agent or environment, or an empty string if the agent is None.
    
    Args:
        named_entity (AgentOrWorld): Агент или окружение.

    Returns:
        str: Имя агента или окружения, или пустая строка, если агент равен `None`.

    Как работает функция:
    1. Проверяет, является ли `named_entity` равным `None`.
    2. Если `named_entity` равен `None`, возвращает пустую строку.
    3. Иначе, возвращает атрибут `name` объекта `named_entity`.
    """
    ...
```

**Как работает функция**:

```
A: Проверка named_entity на None
|
B: Возврат пустой строки (если named_entity равен None)
|
C: Возврат имени (если named_entity не равен None)
```

**Примеры**:

```python
# Пример 1: Агент равен None
agent = None
name = name_or_empty(agent)  # name будет ""

# Пример 2: Агент имеет имя
class Agent:
    def __init__(self, name):
        self.name = name

agent = Agent("John")
name = name_or_empty(agent)  # name будет "John"
```

### `custom_hash`

```python
def custom_hash(obj):
    """
    Returns a hash for the specified object. The object is first converted
    to a string, to make it hashable. This method is deterministic,
    contrary to the built-in hash() function.
    
    Args:
        obj: Объект для хеширования.

    Returns:
        str: SHA256 хеш объекта в виде шестнадцатеричной строки.

    Как работает функция:
    1. Преобразует объект в строку с помощью `str()`.
    2. Кодирует строку в байты с использованием кодировки UTF-8.
    3. Вычисляет SHA256 хеш полученных байтов.
    4. Преобразует хеш в шестнадцатеричную строку.
    5. Возвращает шестнадцатеричную строку.
    """
    ...
```

**Как работает функция**:

```
A: Преобразование объекта в строку
|
B: Кодирование строки в байты
|
C: Вычисление SHA256 хеша
|
D: Преобразование хеша в шестнадцатеричную строку
|
E: Возврат шестнадцатеричной строки
```

**Примеры**:

```python
# Пример 1: Хеширование строки
text = "Hello"
hash_value = custom_hash(text)  # hash_value будет "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"

# Пример 2: Хеширование числа
number = 123
hash_value = custom_hash(number)  # hash_value будет "a665a45920422f9d417e4867efdc4fb8a04a1f3fff219ca8983f5a4e8605c2f7"
```

### `fresh_id`

```python
def fresh_id():
    """
    Returns a fresh ID for a new object. This is useful for generating unique IDs for objects.
    
    Returns:
        int: Уникальный идентификатор.

    Как работает функция:
    1. Увеличивает значение глобального счетчика `_fresh_id_counter` на 1.
    2. Возвращает текущее значение счетчика.
    """
    ...
```

**Как работает функция**:

```
A: Увеличение счетчика
|
B: Возврат счетчика
```

**Примеры**:

```python
# Пример 1: Получение уникального идентификатора
id1 = fresh_id()  # id1 будет 1
id2 = fresh_id()  # id2 будет 2
```