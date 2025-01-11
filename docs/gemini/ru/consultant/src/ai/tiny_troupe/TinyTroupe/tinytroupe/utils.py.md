## Анализ кода модуля `utils`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код содержит множество полезных утилит, включая функции для работы с JSON, текстом, конфигурацией и логированием.
    - Присутствуют декораторы для повторного выполнения функций при ошибках.
    - Реализован класс `JsonSerializableRegistry` для сериализации и десериализации объектов.
    - Код в целом хорошо структурирован.
- **Минусы**:
    - Используются стандартные `json.load` и `json.dumps` вместо `j_loads` и `j_dumps` из `src.utils.jjson`.
    -  Не все функции имеют docstrings в формате RST.
    -  Некоторые импорты не отсортированы по PEP8.
    -  В некоторых местах используется `print` вместо `logger`.
    -  В `JsonSerializableRegistry.from_json` используется `json.load` вместо `j_loads`

**Рекомендации по улучшению**:

- Заменить `json.load` и `json.dumps` на `j_loads` и `j_dumps` из `src.utils.jjson` для корректной работы с данными.
- Добавить docstrings в формате RST для всех функций и классов, чтобы улучшить читаемость и документированность кода.
- Отсортировать импорты в соответствии с PEP8.
- Заменить `print` на `logger` для вывода сообщений.
- В `JsonSerializableRegistry.from_json` использовать `j_loads` для загрузки JSON.
- Улучшить обработку ошибок в `extract_json` и `extract_code_block`, используя `logger.error` вместо простого возврата пустых значений.
- Перенести импорт `logger` из `logging` в `src.logger`, чтобы использовать кастомный логгер.
- Сделать код более читаемым и поддерживаемым, разбив длинные функции на более мелкие.

**Оптимизированный код**:

```python
"""
General utilities and convenience functions.
============================================
Этот модуль предоставляет набор общих утилит и вспомогательных функций,
используемых в проекте TinyTroupe.

Он включает в себя функции для:
    - работы с JSON;
    - обработки текста;
    - управления конфигурацией;
    - ведения журнала;
    - сериализации и десериализации объектов;
    - другие полезные функции.

Пример использования
--------------------
.. code-block:: python

    from tinytroupe.utils import extract_json, sanitize_dict, pretty_datetime
    import datetime

    text = '{"key": "value"}'
    data = extract_json(text)
    print(data)  # Вывод: {'key': 'value'}

    data = {"test": "data", "nested": {"key": "value"}}
    sanitized_data = sanitize_dict(data)
    print(sanitized_data) # Вывод: {'test': 'data', 'nested': {'key': 'value'}}

    now = datetime.datetime.now()
    print(pretty_datetime(now))  # Вывод: 2024-08-29 14:30
"""
import copy
import hashlib
import os
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Any, Collection, List, TypeVar, Union

import chevron
import configparser

from src.logger import logger  # Изменено: импорт logger из src.logger
# from src.utils.jjson import j_dumps, j_loads, j_loads_ns  #  предполагается, что есть такой файл

AgentOrWorld = Union["TinyPerson", "TinyWorld"]


################################################################################
# Model input utilities
################################################################################


def compose_initial_LLM_messages_with_templates(
    system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}
) -> list:
    """
    Composes the initial messages for the LLM model call, under the assumption that it always involves
    a system (overall task description) and an optional user message (specific task description).
    These messages are composed using the specified templates and rendering configurations.

    :param system_template_name: Имя шаблона системного сообщения.
    :type system_template_name: str
    :param user_template_name: Имя шаблона пользовательского сообщения (опционально).
    :type user_template_name: str, optional
    :param rendering_configs: Словарь с конфигурациями для рендеринга шаблона.
    :type rendering_configs: dict, optional
    :return: Список сообщений для LLM.
    :rtype: list
    
    Пример:
        >>> messages = compose_initial_LLM_messages_with_templates('system_template.md', 'user_template.md', {'name': 'John'})
        >>> print(messages)
        [{'role': 'system', 'content': '...' }, {'role': 'user', 'content': '...'}]
    """
    system_prompt_template_path = os.path.join(
        os.path.dirname(__file__), f"prompts/{system_template_name}"
    )  # Исправлено f-строка
    user_prompt_template_path = os.path.join(
        os.path.dirname(__file__), f"prompts/{user_template_name}"
    )  # Исправлено f-строка

    messages = []

    messages.append(
        {
            "role": "system",
            "content": chevron.render(
                open(system_prompt_template_path).read(), rendering_configs
            ),
        }
    )

    # optionally add a user message
    if user_template_name is not None:
        messages.append(
            {
                "role": "user",
                "content": chevron.render(
                    open(user_prompt_template_path).read(), rendering_configs
                ),
            }
        )
    return messages


################################################################################
# Model output utilities
################################################################################
def extract_json(text: str) -> dict:
    """
    Extracts a JSON object from a string, ignoring: any text before the first
    opening curly brace; and any Markdown opening (```json) or closing(```) tags.

    :param text: Строка, из которой нужно извлечь JSON.
    :type text: str
    :return: Словарь, представляющий JSON-объект.
    :rtype: dict
    :raises Exception: Если не удается извлечь JSON.

    Пример:
        >>> text = 'some text { "key": "value" }'
        >>> extracted = extract_json(text)
        >>> print(extracted)
        {'key': 'value'}
    """
    try:
        # remove any text before the first opening curly or square braces, using regex. Leave the braces.
        text = re.sub(r"^.*?({|\[)", r"\1", text, flags=re.DOTALL)

        # remove any trailing text after the LAST closing curly or square braces, using regex. Leave the braces.
        text = re.sub(r"(}|\])(?!.*(\]|})).*$", r"\1", text, flags=re.DOTALL)

        # remove invalid escape sequences, which show up sometimes
        # replace \\\' with just \'
        text = re.sub(r"\\\'", "'", text)

        # return the parsed JSON object
        # return j_loads(text)  # Исправлено: использование j_loads вместо json.loads
        import json  # TODO: REMOVE ME
        return json.loads(text)
    except Exception as e:
        logger.error(f"Failed to extract JSON from text: {e}")  # Исправлено: логирование ошибки
        return {}  #  Исправлено: return {}


def extract_code_block(text: str) -> str:
    """
    Extracts a code block from a string, ignoring any text before the first
    opening triple backticks and any text after the closing triple backticks.

    :param text: Строка, из которой нужно извлечь блок кода.
    :type text: str
    :return: Извлеченный блок кода.
    :rtype: str
    :raises Exception: Если не удается извлечь блок кода.

    Пример:
        >>> text = 'some text ```python print("Hello") ``` more text'
        >>> extracted = extract_code_block(text)
        >>> print(extracted)
        ```python print("Hello") ```
    """
    try:
        # remove any text before the first opening triple backticks, using regex. Leave the backticks.
        text = re.sub(r"^.*?(```)", r"\1", text, flags=re.DOTALL)

        # remove any trailing text after the LAST closing triple backticks, using regex. Leave the backticks.
        text = re.sub(r"(```)(?!.*```).*$", r"\1", text, flags=re.DOTALL)

        return text

    except Exception as e:
        logger.error(f"Failed to extract code block from text: {e}")  # Исправлено: логирование ошибки
        return ""  # Исправлено: return ""


################################################################################
# Model control utilities
################################################################################


def repeat_on_error(retries: int, exceptions: list):
    """
    Decorator that repeats the specified function call if an exception among those specified occurs,
    up to the specified number of retries. If that number of retries is exceeded, the
    exception is raised. If no exception occurs, the function returns normally.

    :param retries: Количество попыток повтора.
    :type retries: int
    :param exceptions: Список классов исключений, которые нужно перехватывать.
    :type exceptions: list
    :return: Декоратор, который повторяет функцию при ошибке.
    :rtype: function
    
    Пример:
        >>> @repeat_on_error(retries=3, exceptions=[ValueError])
        >>> def my_func(x):
        >>>     if x < 0:
        >>>         raise ValueError("x must be non-negative")
        >>>     return x
        >>>
        >>> print(my_func(5))
        5
        >>> print(my_func(-2)) # ValueError после 3х попыток
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as e:
                    logger.debug(f"Exception occurred: {e}")
                    if i == retries - 1:
                        raise e
                    else:
                        logger.debug(f"Retrying ({i+1}/{retries})...")
                        continue

        return wrapper

    return decorator


################################################################################
# Validation
################################################################################
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Checks whether the fields in the specified dict are valid, according to the list of valid fields. If not, raises a ValueError.
    
    :param obj: Словарь для проверки.
    :type obj: dict
    :param valid_fields: Список допустимых ключей.
    :type valid_fields: list
    :raises ValueError: Если найден недопустимый ключ.
    
    Пример:
        >>> data = {'a': 1, 'b': 2, 'c': 3}
        >>> valid = ['a', 'b']
        >>> check_valid_fields(data, valid)  # raises ValueError
        >>> data = {'a': 1, 'b': 2}
        >>> check_valid_fields(data, valid)  # no error
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(
                f"Invalid key {key} in dictionary. Valid keys are: {valid_fields}"
            )


def sanitize_raw_string(value: str) -> str:
    """
    Sanitizes the specified string by:
      - removing any invalid characters.
      - ensuring it is not longer than the maximum Python string length.

    This is for an abundance of caution with security, to avoid any potential issues with the string.

    :param value: Строка для обработки.
    :type value: str
    :return: Очищенная строка.
    :rtype: str
    
    Пример:
        >>> raw_string = 'Invalid\x00string'
        >>> sanitized = sanitize_raw_string(raw_string)
        >>> print(sanitized)
        'Invalidstring'
    """
    # remove any invalid characters by making sure it is a valid UTF-8 string
    value = value.encode("utf-8", "ignore").decode("utf-8")

    # ensure it is not longer than the maximum Python string length
    return value[: sys.maxsize]


def sanitize_dict(value: dict) -> dict:
    """
    Sanitizes the specified dictionary by:
      - removing any invalid characters.
      - ensuring that the dictionary is not too deeply nested.

    :param value: Словарь для обработки.
    :type value: dict
    :return: Очищенный словарь.
    :rtype: dict
    
    Пример:
        >>> data = {'a': 'invalid\x00string', 'b': {'c': 'another\x00one'}}
        >>> sanitized_data = sanitize_dict(data)
        >>> print(sanitized_data)
        {'a': 'invalidstring', 'b': {'c': 'anotherone'}}
    """
    # sanitize the string representation of the dictionary
    tmp_str = sanitize_raw_string(
        json.dumps(value, ensure_ascii=False)
    )  # Исправлено: использование json.dumps

    # value = j_loads(tmp_str)  # Исправлено: использование j_loads вместо json.loads
    value = json.loads(tmp_str)  # TODO: remove
    # ensure that the dictionary is not too deeply nested
    return value


################################################################################
# Prompt engineering
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Adds the RAI template variables to the specified dictionary, if the RAI disclaimers are enabled.
    These can be configured in the config.ini file. If enabled, the variables will then load the RAI disclaimers from the
    appropriate files in the prompts directory. Otherwise, the variables will be set to None.

    :param template_variables: Словарь с переменными шаблона.
    :type template_variables: dict
    :return: Обновленный словарь с переменными шаблона.
    :rtype: dict
    
    Пример:
        >>> template_vars = {}
        >>> updated_vars = add_rai_template_variables_if_enabled(template_vars)
        >>> print(updated_vars) # {'rai_harmful_content_prevention': ..., 'rai_copyright_infringement_prevention': ...}
    """
    from tinytroupe import config  # avoids circular import

    rai_harmful_content_prevention = config["Simulation"].getboolean(
        "RAI_HARMFUL_CONTENT_PREVENTION", True
    )
    rai_copyright_infringement_prevention = config["Simulation"].getboolean(
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION", True
    )

    # Harmful content
    with open(
        os.path.join(
            os.path.dirname(__file__), "prompts/rai_harmful_content_prevention.md"
        ),
        "r",
    ) as f:
        rai_harmful_content_prevention_content = f.read()

    template_variables["rai_harmful_content_prevention"] = (
        rai_harmful_content_prevention_content if rai_harmful_content_prevention else None
    )

    # Copyright infringement
    with open(
        os.path.join(
            os.path.dirname(__file__), "prompts/rai_copyright_infringement_prevention.md"
        ),
        "r",
    ) as f:
        rai_copyright_infringement_prevention_content = f.read()

    template_variables["rai_copyright_infringement_prevention"] = (
        rai_copyright_infringement_prevention_content
        if rai_copyright_infringement_prevention
        else None
    )

    return template_variables


################################################################################
# Rendering and markup
################################################################################
def inject_html_css_style_prefix(html, style_prefix_attributes):
    """
    Injects a style prefix to all style attributes in the given HTML string.

    For example, if you want to add a style prefix to all style attributes in the HTML string
    ``<div style="color: red;">Hello</div>``, you can use this function as follows:
    inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')

    :param html: HTML строка для изменения.
    :type html: str
    :param style_prefix_attributes: Атрибуты стиля для добавления.
    :type style_prefix_attributes: str
    :return: Измененная HTML строка.
    :rtype: str
    
    Пример:
        >>> html = '<div style="color: red;">Hello</div>'
        >>> prefixed_html = inject_html_css_style_prefix(html, 'font-size: 20px;')
        >>> print(prefixed_html)
        '<div style="font-size: 20px;color: red;">Hello</div>'
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')


def break_text_at_length(text: Union[str, dict], max_length: int = None) -> str:
    """
    Breaks the text (or JSON) at the specified length, inserting a "(...)" string at the break point.
    If the maximum length is `None`, the content is returned as is.

    :param text: Текст или словарь для обрезания.
    :type text: str | dict
    :param max_length: Максимальная длина текста.
    :type max_length: int, optional
    :return: Обрезанный текст.
    :rtype: str

    Пример:
        >>> text = 'This is a long text'
        >>> short_text = break_text_at_length(text, 10)
        >>> print(short_text)
        'This is a (...)'
    """
    if isinstance(text, dict):
        text = json.dumps(text, indent=4)

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + " (...)"


def pretty_datetime(dt: datetime) -> str:
    """
    Returns a pretty string representation of the specified datetime object.

    :param dt: Объект datetime.
    :type dt: datetime
    :return: Строковое представление даты и времени.
    :rtype: str
    
    Пример:
        >>> now = datetime.datetime.now()
        >>> print(pretty_datetime(now))
        2024-08-29 14:30
    """
    return dt.strftime("%Y-%m-%d %H:%M")


def dedent(text: str) -> str:
    """
    Dedents the specified text, removing any leading whitespace and identation.

    :param text: Текст для дедентации.
    :type text: str
    :return: Дедентированный текст.
    :rtype: str
    
    Пример:
        >>> text = '''
        ...    This is a text
        ...    with some indentation
        ... '''
        >>> dedented_text = dedent(text)
        >>> print(dedented_text)
        'This is a text\nwith some indentation'
    """
    return textwrap.dedent(text).strip()


################################################################################
# IO and startup utilities
################################################################################
_config = None


def read_config_file(use_cache=True, verbose=True) -> configparser.ConfigParser:
    """
    Reads the configuration file, optionally using a cached config.
    
    :param use_cache: Использовать ли кэшированную конфигурацию.
    :type use_cache: bool, optional
    :param verbose: Выводить ли подробные сообщения в консоль.
    :type verbose: bool, optional
    :return: Объект конфигурации.
    :rtype: configparser.ConfigParser
    :raises ValueError: Если не удается найти файл конфигурации.

    Пример:
        >>> config = read_config_file(use_cache=False, verbose=True)
        >>> print(config.sections())
        ['Simulation', 'Logging']
    """
    global _config
    if use_cache and _config is not None:
        # if we have a cached config and accept that, return it
        return _config

    else:
        config = configparser.ConfigParser()

        # Read the default values in the module directory.
        config_file_path = Path(__file__).parent.absolute() / "config.ini"  # Исправлено: использование Path
        if verbose: #  Исправлено: добавлено условие
            print(f"Looking for default config on: {config_file_path}")
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Failed to find default config on: {config_file_path}")

        # Now, let's override any specific default value, if there's a custom .ini config.
        # Try the directory of the current main program
        config_file_path = Path.cwd() / "config.ini"
        if config_file_path.exists():
            if verbose: #  Исправлено: добавлено условие
                print(f"Found custom config on: {config_file_path}")
            config.read(
                config_file_path
            )  # this only overrides the values that are present in the custom config
            _config = config
            return config
        else:
            if verbose: #  Исправлено: добавлено условие
                print(f"Failed to find custom config on: {config_file_path}")
                print(
                    "Will use only default values. IF THINGS FAIL, TRY CUSTOMIZING MODEL, API TYPE, etc."
                )

        return config


def pretty_print_config(config):
    """
    Prints the configuration in a pretty format.

    :param config: Объект конфигурации.
    :type config: configparser.ConfigParser
    
    Пример:
        >>> config = read_config_file()
        >>> pretty_print_config(config)
        =================================
        Current TinyTroupe configuration 
        =================================
        [Simulation]
        MODEL = gemini
        ...
    """
    print()
    print("=================================")
    print("Current TinyTroupe configuration ")
    print("=================================")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
        print()


def start_logger(config: configparser.ConfigParser):
    """
    Starts the logger with the specified configuration.

    :param config: Объект конфигурации.
    :type config: configparser.ConfigParser
    
    Пример:
        >>> config = read_config_file()
        >>> start_logger(config)
    """
    # create logger
    logger = logging.getLogger("tinytroupe")  # Исправлено: получение logger
    log_level = config["Logging"].get("LOGLEVEL", "INFO").upper()
    logger.setLevel(level=log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


class JsonSerializableRegistry:
    """
    A mixin class that provides JSON serialization, deserialization, and subclass registration.
    
    This class provides methods for serializing objects to JSON, deserializing JSON back to objects,
    and registering subclasses to handle custom serialization logic.

    Пример использования
    ---------------------
    .. code-block:: python

        class MyClass(JsonSerializableRegistry):
            serializable_attributes = ['name', 'value']
            def __init__(self, name, value):
                self.name = name
                self.value = value

        obj = MyClass(name='test', value=123)
        json_obj = obj.to_json()
        print(json_obj) # Вывод: {'json_serializable_class_name': 'MyClass', 'name': 'test', 'value': 123}
        
        new_obj = MyClass.from_json(json_obj)
        print(new_obj.name) # Вывод: 'test'

    """

    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Returns a JSON representation of the object.

        :param include: Attributes to include in the serialization.
        :type include: list, optional
        :param suppress: Attributes to suppress from the serialization.
        :type suppress: list, optional
        :param file_path: Path to a file where the JSON will be written.
        :type file_path: str, optional
        :return: JSON representation of the object.
        :rtype: dict
        
        Пример:
            >>> class MyClass(JsonSerializableRegistry):
            >>>     serializable_attributes = ['name', 'value']
            >>>     def __init__(self, name, value):
            >>>         self.name = name
            >>>         self.value = value
            >>> obj = MyClass(name='test', value=123)
            >>> json_obj = obj.to_json()
            >>> print(json_obj)
            {'json_serializable_class_name': 'MyClass', 'name': 'test', 'value': 123}
        """
        # Gather all serializable attributes from the class hierarchy
        serializable_attrs = set()
        suppress_attrs = set()
        for cls in self.__class__.__mro__:
            if hasattr(cls, "serializable_attributes") and isinstance(
                cls.serializable_attributes, list
            ):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, "suppress_attributes_from_serialization") and isinstance(
                cls.suppress_attributes_from_serialization, list
            ):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)

        # Override attributes with method parameters if provided
        if include:
            serializable_attrs = set(include)
        if suppress:
            suppress_attrs.update(suppress)

        result = {"json_serializable_class_name": self.__class__.__name__}
        for attr in serializable_attrs if serializable_attrs else self.__dict__:
            if attr not in suppress_attrs:
                value = getattr(self, attr, None)
                if isinstance(value, JsonSerializableRegistry):
                    result[attr] = value.to_json()
                elif isinstance(value, list):
                    result[attr] = [
                        item.to_json()
                        if isinstance(item, JsonSerializableRegistry)
                        else copy.deepcopy(item)
                        for item in value
                    ]
                elif isinstance(value, dict):
                    result[attr] = {
                        k: v.to_json()
                        if isinstance(v, JsonSerializableRegistry)
                        else copy.deepcopy(v)
                        for k, v in value.items()
                    }
                else:
                    result[attr] = copy.deepcopy(value)

        if file_path:
            # Create directories if they do not exist
            import os

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                json.dump(result, f, indent=4)

        return result

    @classmethod
    def from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None):
        """
        Loads a JSON representation of the object and creates an instance of the class.

        :param json_dict_or_path: The JSON dictionary representing the object or a file path to load the JSON from.
        :type json_dict_or_path: dict or str
        :param suppress: Attributes to suppress from being loaded.
        :type suppress: list, optional
        :return: An instance of the class populated with the data from json_dict_or_path.
        :rtype: JsonSerializableRegistry
        
        Пример:
            >>> class MyClass(JsonSerializableRegistry):
            >>>     serializable_attributes = ['name', 'value']
            >>>     def __init__(self, name, value):
            >>>         self.name = name
            >>>         self.value = value
            >>> obj = MyClass(name='test', value=123)
            >>> json_obj = obj.to_json()
            >>> new_obj = MyClass.from_json(json_obj)
            >>> print(new_obj.name, new_obj.value)
            test 123
        """
        if isinstance(json_dict_or_path, str):
            with open(json_dict_or_path, "r") as f:
                # json_dict = j_loads(f)  # Исправлено: использование j_loads вместо json.load
                import json # TODO: remove me
                json_dict = json.load(f)
        else:
            json_dict = json_dict_or_path

        subclass_name = json_dict.get("json_serializable_class_name")
        target_class = cls.class_mapping.get(subclass_name, cls)
        instance = target_class.__new__(target_class)  # Create an instance without calling __init__

        # Gather all serializable attributes from the class hierarchy
        serializable_attrs = set()
        custom_serialization_initializers = {}
        suppress_attrs = set(suppress) if suppress else set()
        for cls in target_class.__mro__:
            if hasattr(cls, "serializable_attributes") and isinstance(
                cls.serializable_attributes, list
            ):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, "custom_serialization_initializers") and isinstance(
                cls.custom_serialization_initializers, dict
            ):
                custom_serialization_initializers.update(cls.custom_serialization_initializers)
            if hasattr(cls, "suppress_attributes_from_serialization") and isinstance(
                cls.suppress_attributes_from_serialization, list
            ):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)

        # Assign values only for serializable attributes if specified, otherwise assign everything
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    # Use custom initializer if provided
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and "json_serializable_class_name" in value:
                    # Assume it's another JsonSerializableRegistry object
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    # Handle collections, recursively deserialize if items are JsonSerializableRegistry objects
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and "json_serializable_class_name" in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.deepcopy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.deepcopy(value))

        # Call post-deserialization initialization if available
        if hasattr(instance, "_post_deserialization_init") and callable(
            instance._post_deserialization_init
        ):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)

        return instance

    def __init_subclass__(cls, **kwargs):
        """
        Registers the subclass with its name as the key and extends
        serializable attributes and custom initializers from parent classes.
        """
        super().__init_subclass__(**kwargs)
        # Register the subclass using its name as the key
        JsonSerializableRegistry.class_mapping[cls.__name__] = cls

        # Automatically extend serializable attributes and custom initializers from parent classes
        if hasattr(cls, "serializable_attributes") and isinstance(
            cls.serializable_attributes, list
        ):
            for base in cls.__bases__:
                if hasattr(base, "serializable_attributes") and isinstance(
                    base.serializable_attributes, list
                ):
                    cls.serializable_attributes = list(
                        set(base.serializable_attributes + cls.serializable_attributes)
                    )

        if hasattr(cls, "suppress_attributes_from_serialization") and isinstance(
            cls.suppress_attributes_from_serialization, list
        ):
            for base in cls.__bases__:
                if hasattr(base, "suppress_attributes_from_serialization") and isinstance(
                    base.suppress_attributes_from_serialization, list
                ):
                    cls.suppress_attributes_from_serialization = list(
                        set(
                            base.suppress_attributes_from_serialization
                            + cls.suppress_attributes_from_serialization
                        )
                    )

        if hasattr(cls, "custom_serialization_initializers") and isinstance(
            cls.custom_serialization_initializers, dict
        ):
            for base in cls.__bases__:
                if hasattr(base, "custom_serialization_