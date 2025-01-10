## Анализ кода модуля `utils.py`

**Качество кода:** 8/10
- Плюсы:
    - Код хорошо структурирован и разделен на логические блоки.
    - Используются docstring для описания функций.
    - Присутствует обработка ошибок, хотя и не всегда оптимальна.
    - Есть механизмы для работы с конфигурационными файлами и логированием.
    - Реализована поддержка JSON сериализации/десериализации с возможностью регистрации подклассов.
- Минусы:
    - Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    - Не все функции имеют подробные docstring с примерами и аргументами.
    - Некоторые конструкции `try-except` можно заменить на `logger.error`.
    - В некоторых местах используется `print` для вывода, вместо `logger`.
    - Отсутствует импорт `from src.logger.logger import logger`.
    - Есть некоторая избыточность в использовании `copy.deepcopy`, можно оптимизировать.
    - Не везде используется одинарный кавычки в коде

**Рекомендации по улучшению:**

1.  Заменить все вызовы `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить подробные docstring с примерами использования и описанием аргументов для всех функций, методов и классов.
3.  Заменить блоки `try-except` на `logger.error` для более лаконичной обработки ошибок.
4.  Использовать `logger` из `from src.logger.logger import logger` для логирования.
5.  Удалить лишние вызовы `copy.deepcopy` там где это не нужно.
6.  Использовать одинарные кавычки для строк внутри кода (кроме `print`, `input` и `logger`).
7.  Удалить `print` для отладки, заменив на `logger.debug` или `logger.info`.
8.  Улучшить форматирование docstring для соответствия стандартам Sphinx.

**Оптимизированный код:**

```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль содержит набор утилит и вспомогательных функций, которые используются в проекте.
Включает функции для работы с шаблонами, JSON, текстом, конфигурационными файлами, логированием,
сериализацией и десериализацией объектов, а также другие общие утилиты.

Пример использования
--------------------

.. code-block:: python

    from tinytroupe.utils import compose_initial_LLM_messages_with_templates, extract_json
    from pathlib import Path
    from datetime import datetime

    # Пример использования compose_initial_LLM_messages_with_templates
    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.md',
        user_template_name='user_prompt.md',
        rendering_configs={'name': 'Test'}
    )

    # Пример использования extract_json
    json_string = '{"key": "value"}'
    extracted_json = extract_json(json_string)

    # Пример использования pretty_datetime
    now = datetime.now()
    pretty_date = pretty_datetime(now)

"""
import re
import os
import sys
import hashlib
import textwrap
from datetime import datetime
from pathlib import Path
import configparser
import chevron
import copy
from typing import Collection, Any, TypeVar, Union, List, Dict
from src.logger.logger import logger
from src.utils.jjson import j_loads #  импорт j_loads для загрузки json
AgentOrWorld = Union["TinyPerson", "TinyWorld"]


################################################################################
# Model input utilities
################################################################################

def compose_initial_LLM_messages_with_templates(system_template_name:str, user_template_name:str=None, rendering_configs:dict={}) -> list:
    """
    Составляет начальные сообщения для вызова LLM, предполагая, что всегда используется
    системное сообщение (общее описание задачи) и опциональное пользовательское сообщение (специфическое описание задачи).
    Сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

    Args:
        system_template_name (str): Имя файла шаблона системного сообщения.
        user_template_name (str, optional): Имя файла шаблона пользовательского сообщения. Defaults to None.
        rendering_configs (dict, optional): Словарь с конфигурациями для рендеринга шаблонов. Defaults to {}.

    Returns:
        list: Список сообщений для LLM.

    Example:
         >>> messages = compose_initial_LLM_messages_with_templates(
         ...     system_template_name='system_prompt.md',
         ...     user_template_name='user_prompt.md',
         ...     rendering_configs={'name': 'Test'}
         ... )
         >>> print(messages)
         [{'role': 'system', 'content': '...'}]
    """
    #  формирование путей к файлам шаблонов
    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    # добавление системного сообщения
    messages.append({'role': 'system',
                         'content': chevron.render(
                             open(system_prompt_template_path).read(),
                             rendering_configs)})
    
    # опциональное добавление пользовательского сообщения
    if user_template_name is not None:
        messages.append({'role': 'user',
                            'content': chevron.render(
                                    open(user_prompt_template_path).read(),
                                    rendering_configs)})
    return messages


################################################################################	
# Model output utilities
################################################################################
def extract_json(text: str) -> dict:
    """
    Извлекает JSON объект из строки, игнорируя текст до первой открывающей фигурной скобки,
    а также Markdown теги открытия (```json) и закрытия (```).

    Args:
        text (str): Строка для извлечения JSON.

    Returns:
        dict: Извлеченный JSON объект в виде словаря.

    Example:
        >>> json_string = '{"key": "value"}'
        >>> extracted_json = extract_json(json_string)
        >>> print(extracted_json)
        {'key': 'value'}

        >>> text_with_prefix = 'Some text before {"key": "value"}'
        >>> extracted_json = extract_json(text_with_prefix)
        >>> print(extracted_json)
        {'key': 'value'}

        >>> text_with_markdown = '```json\\n{"key": "value"}\\n```'
        >>> extracted_json = extract_json(text_with_markdown)
        >>> print(extracted_json)
        {'key': 'value'}
    """
    try:
        # удаление текста до первой открывающей фигурной или квадратной скобки с помощью regex
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.DOTALL)

        # удаление текста после последней закрывающей фигурной или квадратной скобки с помощью regex
        text  =  re.sub(r'(}|\])(?!.*(\]|})).*$', r'\1', text, flags=re.DOTALL)
        
        # удаление недопустимых escape-последовательностей
        text =  re.sub(r'\\\\\'', '\'', text)

        #  возвращение JSON объекта
        return j_loads(text)
    
    except Exception as e:
        logger.error(f'Ошибка при извлечении JSON: {e}')
        return {}

def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя текст до первых открывающих тройных обратных кавычек
    и любой текст после закрывающих тройных обратных кавычек.

    Args:
        text (str): Строка для извлечения блока кода.

    Returns:
        str: Извлеченный блок кода.

    Example:
        >>> code_text = '```python\\nprint("Hello")\\n```'
        >>> extracted_code = extract_code_block(code_text)
        >>> print(extracted_code)
        ```python\\nprint("Hello")\\n```

        >>> text_with_prefix = 'Some text before ```python\\nprint("Hello")\\n```'
        >>> extracted_code = extract_code_block(text_with_prefix)
        >>> print(extracted_code)
        ```python\\nprint("Hello")\\n```
    """
    try:
        # удаление текста до первых открывающих тройных обратных кавычек с помощью regex
        text = re.sub(r'^.*?(```)', r'\1', text, flags=re.DOTALL)

        # удаление текста после последних закрывающих тройных обратных кавычек с помощью regex
        text  =  re.sub(r'(```)(?!.*```).*$', r'\1', text, flags=re.DOTALL)
        
        return text
    
    except Exception as e:
        logger.error(f'Ошибка при извлечении блока кода: {e}')
        return ''

################################################################################
# Model control utilities
################################################################################    
@repeat_on_error(retries=3, exceptions=[Exception])
def repeat_on_error(retries:int, exceptions:list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из указанного списка,
    до указанного количества попыток. Если количество попыток превышено, исключение выбрасывается.
    Если исключение не возникает, функция возвращает результат.

    Args:
        retries (int): Количество попыток повторения.
        exceptions (list): Список классов исключений, которые нужно перехватывать.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as e:
                    logger.debug(f"Исключение: {e}")
                    if i == retries - 1:
                        raise e
                    else:
                        logger.debug(f"Повторная попытка ({i+1}/{retries})...")
                        continue
        return wrapper
    return decorator
   

################################################################################
# Validation
################################################################################
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Проверяет, являются ли поля в указанном словаре допустимыми, согласно списку допустимых полей.
    Если нет, выбрасывает ValueError.

    Args:
        obj (dict): Словарь для проверки.
        valid_fields (list): Список допустимых полей.

    Raises:
        ValueError: Если обнаружено недопустимое поле.

    Example:
        >>> check_valid_fields({'a': 1, 'b': 2}, ['a', 'b'])

        >>> check_valid_fields({'a': 1, 'c': 3}, ['a', 'b'])
        ValueError: Invalid key c in dictionary. Valid keys are: ['a', 'b']
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(f'Недопустимый ключ {key} в словаре. Допустимые ключи: {valid_fields}')

def sanitize_raw_string(value: str) -> str:
    """
    Очищает указанную строку, удаляя недопустимые символы
    и гарантируя, что она не превышает максимальную длину строки Python.
    Используется для обеспечения безопасности и избежания потенциальных проблем со строкой.

    Args:
        value (str): Строка для очистки.

    Returns:
        str: Очищенная строка.

    Example:
        >>> sanitize_raw_string("тест\\x00")
        'тест'
        >>> sanitize_raw_string("a" * 2**30)
        'aaaaaaaaaa...'
    """
    # удаление недопустимых символов
    value = value.encode('utf-8', 'ignore').decode('utf-8')

    # проверка максимальной длинны строки
    return value[:sys.maxsize]

def sanitize_dict(value: dict) -> dict:
    """
    Очищает указанный словарь, удаляя недопустимые символы и гарантируя, что словарь не является слишком вложенным.
    """

    # очистка строкового представления словаря
    tmp_str = sanitize_raw_string(j_loads(j_dumps(value, ensure_ascii=False))) #  использования j_dumps для сериализации

    value = j_loads(tmp_str) #  использования j_loads для десериализации

    # проверка глубины вложенности словаря
    return value
    
    
################################################################################
# Prompt engineering
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет переменные шаблона RAI в указанный словарь, если включены отказы от ответственности RAI.
    Это можно настроить в файле config.ini. Если включено, переменные загрузят отказы от ответственности RAI из
    соответствующих файлов в каталоге prompts. В противном случае переменные будут установлены в None.

    Args:
        template_variables (dict): Словарь переменных шаблона, в который нужно добавить переменные RAI.

    Returns:
        dict: Обновленный словарь переменных шаблона.

    Example:
        >>> template_vars = {}
        >>> updated_vars = add_rai_template_variables_if_enabled(template_vars)
        >>> print(updated_vars)
        {'rai_harmful_content_prevention': '...', 'rai_copyright_infringement_prevention': '...'}
    """

    from tinytroupe import config #  импорт config для избежания циклического импорта
    rai_harmful_content_prevention = config['Simulation'].getboolean(
        'RAI_HARMFUL_CONTENT_PREVENTION', True
    )
    rai_copyright_infringement_prevention = config['Simulation'].getboolean(
        'RAI_COPYRIGHT_INFRINGEMENT_PREVENTION', True
    )

    # вредный контент
    with open(os.path.join(os.path.dirname(__file__), 'prompts/rai_harmful_content_prevention.md'), 'r') as f:
        rai_harmful_content_prevention_content = f.read()

    template_variables['rai_harmful_content_prevention'] = rai_harmful_content_prevention_content if rai_harmful_content_prevention else None

    # нарушение авторских прав
    with open(os.path.join(os.path.dirname(__file__), 'prompts/rai_copyright_infringement_prevention.md'), 'r') as f:
        rai_copyright_infringement_prevention_content = f.read()

    template_variables['rai_copyright_infringement_prevention'] = rai_copyright_infringement_prevention_content if rai_copyright_infringement_prevention else None

    return template_variables

################################################################################
# Rendering and markup 
################################################################################
def inject_html_css_style_prefix(html: str, style_prefix_attributes: str) -> str:
    """
    Вставляет префикс стиля ко всем атрибутам стиля в заданной HTML-строке.

    Args:
        html (str): HTML строка для вставки префикса.
        style_prefix_attributes (str): Префикс стиля для вставки.

    Returns:
        str: HTML строка с вставленным префиксом.

    Example:
        >>> inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')
        '<div style="font-size: 20px;color: red;">Hello</div>'
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')

def break_text_at_length(text: Union[str, dict], max_length: int=None) -> str:
    """
    Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)" в точке разрыва.
    Если максимальная длина равна `None`, контент возвращается как есть.

    Args:
        text (Union[str, dict]): Текст или JSON для разбиения.
        max_length (int, optional): Максимальная длина текста. Defaults to None.

    Returns:
        str: Разбитый текст.

    Example:
        >>> break_text_at_length('This is a long text', 10)
        'This is a (...)'
        >>> break_text_at_length({'key': 'value'}, 10)
        '{
            "key": "value"
        } (...)'
        >>> break_text_at_length('Short text', None)
        'Short text'
    """
    if isinstance(text, dict):
        text = j_dumps(text, indent=4)  #  использования j_dumps для сериализации json

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + ' (...)'

def pretty_datetime(dt: datetime) -> str:
    """
    Возвращает строковое представление указанного объекта datetime.

    Args:
        dt (datetime): Объект datetime.

    Returns:
        str: Строковое представление datetime.

    Example:
        >>> now = datetime(2023, 10, 27, 10, 30)
        >>> pretty_datetime(now)
        '2023-10-27 10:30'
    """
    return dt.strftime('%Y-%m-%d %H:%M')

def dedent(text: str) -> str:
    """
    Удаляет отступы из указанного текста, удаляя все начальные пробелы и отступы.

    Args:
        text (str): Текст для удаления отступов.

    Returns:
        str: Текст без отступов.

    Example:
        >>> text = '''
        ...    This is a
        ...    multiline text
        ... '''
        >>> dedent(text)
        'This is a\\nmultiline text'
    """
    return textwrap.dedent(text).strip()

################################################################################
# IO and startup utilities
################################################################################
_config = None

def read_config_file(use_cache=True, verbose=True) -> configparser.ConfigParser:
    """
    Читает файл конфигурации, используя кэш при необходимости.
    Ищет файл конфигурации сначала в каталоге модуля, затем в текущем рабочем каталоге.

    Args:
        use_cache (bool, optional): Использовать кэш конфигурации. Defaults to True.
        verbose (bool, optional): Выводить подробные сообщения. Defaults to True.

    Returns:
        configparser.ConfigParser: Объект конфигурации.

    Raises:
        ValueError: Если не удается найти файл конфигурации.

    Example:
        >>> config = read_config_file(use_cache=False, verbose=False)
        >>> print(config.sections())
        ['Logging', 'Simulation', 'API', ...]
    """
    global _config
    if use_cache and _config is not None:
        #  если есть кэшированная конфигурация и она принимается, возвращаем ее
        return _config
    
    else:
        config = configparser.ConfigParser()

        #  чтение значений по умолчанию в каталоге модуля
        config_file_path = Path(__file__).parent.absolute() / 'config.ini'
        logger.debug(f"Поиск конфигурации по умолчанию: {config_file_path}") if verbose else None
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Не удалось найти конфигурацию по умолчанию: {config_file_path}")

        #  переопределение значений по умолчанию, если есть пользовательская конфигурация
        config_file_path = Path.cwd() / 'config.ini'
        if config_file_path.exists():
            logger.debug(f"Найдена пользовательская конфигурация: {config_file_path}") if verbose else None
            config.read(config_file_path) #  переопределение только значений, присутствующих в пользовательской конфигурации
            _config = config
            return config
        else:
            if verbose:
                logger.debug(f"Не удалось найти пользовательскую конфигурацию: {config_file_path}") if verbose else None
                logger.debug('Будут использоваться только значения по умолчанию. Если возникнут проблемы, попробуйте настроить MODEL, API TYPE и т.д.') if verbose else None
        
        return config

def pretty_print_config(config: configparser.ConfigParser) -> None:
    """
    Выводит текущую конфигурацию в удобочитаемом виде.

    Args:
        config (configparser.ConfigParser): Объект конфигурации.

    Example:
        >>> config = configparser.ConfigParser()
        >>> config['Section'] = {'key1': 'value1', 'key2': 'value2'}
        >>> pretty_print_config(config)
        <BLANKLINE>
        =================================
        Current TinyTroupe configuration
        =================================
        [Section]
        key1 = value1
        key2 = value2
        <BLANKLINE>
    """
    print()
    print('=================================')
    print('Текущая конфигурация TinyTroupe')
    print('=================================')
    for section in config.sections():
        print(f'[{section}]')
        for key, value in config.items(section):
            print(f'{key} = {value}')
        print()

def start_logger(config: configparser.ConfigParser) -> None:
    """
    Инициализирует логгер с уровнем, заданным в конфигурации.

    Args:
        config (configparser.ConfigParser): Объект конфигурации.

    Example:
        >>> import configparser
        >>> config = configparser.ConfigParser()
        >>> config['Logging'] = {'LOGLEVEL': 'DEBUG'}
        >>> start_logger(config)

    """
    # создание логгера
    logger = logging.getLogger('tinytroupe')
    log_level = config['Logging'].get('LOGLEVEL', 'INFO').upper()
    logger.setLevel(level=log_level)

    # создание обработчика консоли и установка уровня debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # создание форматтера
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # добавление форматтера к ch
    ch.setFormatter(formatter)

    # добавление ch к логгеру
    logger.addHandler(ch)

class JsonSerializableRegistry:
    """
    Миксин-класс, предоставляющий сериализацию и десериализацию JSON, а также регистрацию подклассов.
    """
    
    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Возвращает JSON представление объекта.

        Args:
            include (list, optional): Атрибуты, которые нужно включить в сериализацию.
            suppress (list, optional): Атрибуты, которые нужно исключить из сериализации.
            file_path (str, optional): Путь к файлу, куда будет записан JSON.

        Returns:
            dict: JSON представление объекта.

        Example:
            >>> class Example(JsonSerializableRegistry):
            ...     serializable_attributes = ['a', 'b']
            ...     def __init__(self, a, b, c):
            ...         self.a = a
            ...         self.b = b
            ...         self.c = c
            >>> obj = Example(1, 2, 3)
            >>> obj.to_json()
            {'json_serializable_class_name': 'Example', 'a': 1, 'b': 2}
        """
        # сбор всех сериализуемых атрибутов из иерархии классов
        serializable_attrs = set()
        suppress_attrs = set()
        for cls in self.__class__.__mro__:
            if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)
        
        #  переопределение атрибутов с помощью параметров метода, если они предоставлены
        if include:
            serializable_attrs = set(include)
        if suppress:
            suppress_attrs.update(suppress)
        
        result = {'json_serializable_class_name': self.__class__.__name__}
        for attr in serializable_attrs if serializable_attrs else self.__dict__:
            if attr not in suppress_attrs:
                value = getattr(self, attr, None)
                if isinstance(value, JsonSerializableRegistry):
                    result[attr] = value.to_json()
                elif isinstance(value, list):
                    result[attr] = [item.to_json() if isinstance(item, JsonSerializableRegistry) else copy.copy(item) for item in value]
                elif isinstance(value, dict):
                    result[attr] = {k: v.to_json() if isinstance(v, JsonSerializableRegistry) else copy.copy(v) for k, v in value.items()}
                else:
                    result[attr] = copy.copy(value)
        
        if file_path:
            # создание каталогов, если они не существуют
            import os
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                j_dumps(result, f, indent=4) #  использования j_dumps для сериализации json
        
        return result

    @classmethod
    def from_json(cls, json_dict_or_path: Union[dict,str], suppress: list = None, post_init_params: dict = None):
        """
        Загружает JSON представление объекта и создает экземпляр класса.

        Args:
            json_dict_or_path (Union[dict, str]): JSON словарь, представляющий объект, или путь к файлу для загрузки JSON.
            suppress (list, optional): Атрибуты, которые нужно исключить из загрузки.
            post_init_params (dict, optional): Параметры для передачи в метод _post_deserialization_init.

        Returns:
            Экземпляр класса, заполненный данными из json_dict_or_path.

        Example:
            >>> class Example(JsonSerializableRegistry):
            ...     serializable_attributes = ['a', 'b']
            ...     def __init__(self, a, b):
            ...         self.a = a
            ...         self.b = b
            >>> json_data = {'json_serializable_class_name': 'Example', 'a': 1, 'b': 2}
            >>> obj = Example.from_json(json_data)
            >>> print(obj.a, obj.b)
            1 2
        """
        if isinstance(json_dict_or_path, str):
            with open(json_dict_or_path, 'r') as f:
                json_dict = j_loads(f) #  использования j_loads для десериализации json
        else:
            json_dict = json_dict_or_path
        
        subclass_name = json_dict.get('json_serializable_class_name')
        target_class = cls.class_mapping.get(subclass_name, cls)
        instance = target_class.__new__(target_class)  #  создание экземпляра без вызова __init__
        
        #  сбор всех сериализуемых атрибутов из иерархии классов
        serializable_attrs = set()
        custom_serialization_initializers = {}
        suppress_attrs = set(suppress) if suppress else set()
        for cls in target_class.__mro__:
            if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, 'custom_serialization_initializers') and isinstance(cls.custom_serialization_initializers, dict):
                custom_serialization_initializers.update(cls.custom_serialization_initializers)
            if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)
        
        #  присваивание значений только для сериализуемых атрибутов, если они указаны, иначе присваиваем все
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    #  использование пользовательского инициализатора, если он предоставлен
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and 'json_serializable_class_name' in value:
                    #  предположение, что это другой объект JsonSerializableRegistry
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    #  обработка коллекций, рекурсивная десериализация, если элементы являются объектами JsonSerializableRegistry
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and 'json_serializable_class_name' in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.copy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.copy(value))
        
        #  вызов инициализации после десериализации, если она доступна
        if hasattr(instance, '_post_deserialization_init') and callable(instance._post_deserialization_init):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)
        
        return instance

    def __init_subclass__(cls, **kwargs):
        """
        Регистрирует подкласс в `class_mapping` и автоматически расширяет атрибуты
        из родительских классов.
        """
        super().__init_subclass__(**kwargs)
        #  регистрация подкласса с использованием его имени в качестве ключа
        JsonSerializableRegistry.class_mapping[cls.__name__] = cls
        
        # автоматическое расширение сериализуемых атрибутов и пользовательских инициализаторов из родительских классов
        if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
            for base in cls.__bases__:
                if hasattr(base, 'serializable_attributes') and isinstance(base.serializable_attributes, list):
                    cls.serializable_attributes = list(set(base.serializable_attributes + cls.serializable_attributes))
        
        if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
            for base in cls.__bases__:
                if hasattr(base, 'suppress_attributes_from_serialization') and isinstance(base.suppress_attributes_from_serialization, list):
                    cls.suppress_attributes_from_serialization = list(set(base.suppress_attributes_from_serialization + cls.suppress_attributes_from_serialization))
        
        if hasattr(cls, 'custom_serialization_initializers') and isinstance(cls.custom_serialization_initializers, dict):
            for base in cls.__bases__:
                if hasattr(base, 'custom_serialization_initializers') and isinstance(base.custom_serialization_initializers, dict):
                    base_initializers = base.custom_serialization_initializers.copy()
                    base_initializers.update(cls.custom_serialization_initializers)
                    cls.custom_serialization_initializers = base_initializers

    def _post_deserialization_init(self, **kwargs):
        """
        Вызывается после десериализации для выполнения дополнительных действий.
        """
        #  если есть метод _post_init, вызываем его после десериализации
        if hasattr(self, '_post_init'):
            self._post_init(**kwargs)


def post_init(cls):
    """
    Декоратор для принудительного вызова метода post-initialization в классе, если он есть.
    Метод должен называться `_post_init`.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        if hasattr(self, '_post_init'):
            self._post_init()

    cls.__init__ = new_init
    return cls

################################################################################
# Other
################################################################################
def name_or_empty(named_entity: AgentOrWorld) -> str:
    """
    Возвращает имя указанного агента или среды, или пустую строку, если агент равен None.

    Args:
        named_entity (AgentOrWorld): Агент или среда.

    Returns:
        str: Имя агента или среды, или пустая строка.

    Example:
        >>> class MockAgent:
        ...     def __init__(self, name):
        ...         self.name = name
        >>> agent = MockAgent('TestAgent')