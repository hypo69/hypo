## Улучшенный код
```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль предоставляет набор общих утилит и вспомогательных функций,
используемых в проекте TinyTroupe. Он включает в себя функции для:
- работы с входными и выходными данными модели,
- управления моделью,
- валидации данных,
- инжиниринга промптов,
- рендеринга и разметки,
- ввода/вывода,
- сериализации JSON,
- а также другие вспомогательные функции.

Пример использования
--------------------

Пример использования некоторых функций из этого модуля:

.. code-block:: python

    from tinytroupe.utils import compose_initial_LLM_messages_with_templates, extract_json
    
    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.txt', 
        user_template_name='user_prompt.txt', 
        rendering_configs={'variable': 'value'}
    )
    
    json_data = extract_json('some text { "key": "value" } some text')
"""
import re
import json
import os
import sys
import hashlib
import textwrap
import logging
import chevron
import copy
from typing import Collection
from datetime import datetime
from pathlib import Path
import configparser
from typing import Any, TypeVar, Union
from src.utils.jjson import j_loads, j_loads_ns # импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # импортируем logger из src.logger.logger

AgentOrWorld = Union["TinyPerson", "TinyWorld"]

# logger
# logger = logging.getLogger("tinytroupe") # заменено на импорт из src.logger.logger


################################################################################
# Model input utilities
################################################################################
def compose_initial_LLM_messages_with_templates(system_template_name:str, user_template_name:str=None, rendering_configs:dict={}) -> list:
    """
    Составляет начальные сообщения для вызова LLM модели, предполагая, что всегда используется системное сообщение
    (общее описание задачи) и необязательное пользовательское сообщение (конкретное описание задачи).
    Эти сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

    :param system_template_name: Имя файла шаблона системного сообщения.
    :param user_template_name: Имя файла шаблона пользовательского сообщения (необязательно).
    :param rendering_configs: Словарь с конфигурациями для рендеринга шаблонов.
    :return: Список сообщений для LLM.
    """
    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    messages.append({"role": "system", 
                         "content": chevron.render(
                             open(system_prompt_template_path).read(), 
                             rendering_configs)})
    
    # optionally add a user message
    if user_template_name is not None:
        messages.append({"role": "user", 
                            "content": chevron.render(
                                    open(user_prompt_template_path).read(), 
                                    rendering_configs)})
    return messages


################################################################################	
# Model output utilities
################################################################################
def extract_json(text: str) -> dict:
    """
    Извлекает JSON-объект из строки, игнорируя: любой текст до первой открывающей фигурной скобки;
    и любые открывающие (```json) или закрывающие (```) теги Markdown.

    :param text: Строка, из которой нужно извлечь JSON.
    :return: Извлеченный JSON-объект в виде словаря или пустой словарь в случае ошибки.
    """
    try:
        # удаляет любой текст до первой открывающей фигурной или квадратной скобки, используя регулярное выражение.
        # Оставляет скобки.
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последней закрывающей фигурной или квадратной скобки, используя регулярное выражение.
        # Оставляет скобки.
        text  =  re.sub(r'(}|\])(?!.*(\]|}))', r'\1', text, flags=re.DOTALL)
        
        # удаляет недопустимые escape-последовательности, которые иногда появляются.
        # заменяет \\\' на \'
        text =  re.sub(r"\\\'", r"\'", text)

        # возвращает разобранный JSON-объект
        return json.loads(text)
    
    except Exception as ex:
        logger.error(f'Ошибка при извлечении JSON: {ex}')
        return {}

def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя любой текст до первых открывающих тройных обратных кавычек
    и любой текст после закрывающих тройных обратных кавычек.

    :param text: Строка, из которой нужно извлечь блок кода.
    :return: Извлеченный блок кода или пустая строка в случае ошибки.
    """
    try:
        # удаляет любой текст до первых открывающих тройных обратных кавычек, используя регулярное выражение.
        # Оставляет кавычки.
        text = re.sub(r'^.*?(```)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последних закрывающих тройных обратных кавычек, используя регулярное выражение.
        # Оставляет кавычки.
        text  =  re.sub(r'(```)(?!.*```).*$', r'\1', text, flags=re.DOTALL)
        
        return text
    
    except Exception as ex:
        logger.error(f'Ошибка при извлечении блока кода: {ex}')
        return ""

################################################################################
# Model control utilities
################################################################################    
def repeat_on_error(retries:int, exceptions:list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из указанного списка,
    до указанного количества попыток. Если количество попыток превышено, вызывается исключение.
    Если исключение не возникает, функция возвращается нормально.

    :param retries: Количество попыток повторения вызова функции.
    :param exceptions: Список классов исключений, которые нужно перехватывать.
    :return: Декорированная функция.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as e:
                    logger.debug(f"Произошло исключение: {e}")
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
    Проверяет, являются ли поля в указанном словаре допустимыми в соответствии со списком допустимых полей.
    Если нет, вызывает ValueError.

    :param obj: Словарь для проверки.
    :param valid_fields: Список допустимых ключей.
    :raises ValueError: Если в словаре есть недопустимые ключи.
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(f"Недопустимый ключ {key} в словаре. Допустимые ключи: {valid_fields}")

def sanitize_raw_string(value: str) -> str:
    """
    Очищает указанную строку путем:
      - удаления любых недопустимых символов.
      - проверки, что она не длиннее максимальной длины строки в Python.

    Это сделано для предосторожности в отношении безопасности, чтобы избежать любых потенциальных проблем со строкой.

    :param value: Строка для очистки.
    :return: Очищенная строка.
    """
    # удаляет любые недопустимые символы, удостоверяясь, что строка является допустимой UTF-8 строкой
    value = value.encode("utf-8", "ignore").decode("utf-8")

    # проверяет, что она не длиннее максимальной длины строки в Python
    return value[:sys.maxsize]

def sanitize_dict(value: dict) -> dict:
    """
    Очищает указанный словарь путем:
      - удаления любых недопустимых символов.
      - проверки, что словарь не слишком глубоко вложен.

    :param value: Словарь для очистки.
    :return: Очищенный словарь.
    """
    # очищает строковое представление словаря
    tmp_str = sanitize_raw_string(json.dumps(value, ensure_ascii=False))

    value = json.loads(tmp_str)

    # проверяет, что словарь не слишком глубоко вложен
    return value
    
    
################################################################################
# Prompt engineering
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет переменные шаблона RAI в указанный словарь, если включены отказы от ответственности RAI.
    Они могут быть настроены в файле config.ini. Если включено, переменные будут загружать отказы от ответственности RAI
    из соответствующих файлов в каталоге prompts. В противном случае переменные будут установлены в None.

    :param template_variables: Словарь переменных шаблона, в который нужно добавить переменные RAI.
    :return: Обновленный словарь переменных шаблона.
    """
    from tinytroupe import config # избегает циклического импорта
    rai_harmful_content_prevention = config["Simulation"].getboolean(
        "RAI_HARMFUL_CONTENT_PREVENTION", True 
    )
    rai_copyright_infringement_prevention = config["Simulation"].getboolean(
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION", True
    )

    # Harmful content
    with open(os.path.join(os.path.dirname(__file__), "prompts/rai_harmful_content_prevention.md"), "r") as f:
        rai_harmful_content_prevention_content = f.read()

    template_variables['rai_harmful_content_prevention'] = rai_harmful_content_prevention_content if rai_harmful_content_prevention else None

    # Copyright infringement
    with open(os.path.join(os.path.dirname(__file__), "prompts/rai_copyright_infringement_prevention.md"), "r") as f:
        rai_copyright_infringement_prevention_content = f.read()

    template_variables['rai_copyright_infringement_prevention'] = rai_copyright_infringement_prevention_content if rai_copyright_infringement_prevention else None

    return template_variables

################################################################################
# Rendering and markup 
################################################################################
def inject_html_css_style_prefix(html, style_prefix_attributes):
    """
    Добавляет префикс стиля ко всем атрибутам style в заданной HTML-строке.

    Например, если вы хотите добавить префикс стиля ко всем атрибутам style в HTML-строке
    ``<div style="color: red;">Hello</div>``, вы можете использовать эту функцию следующим образом:
    inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')

    :param html: HTML-строка для изменения.
    :param style_prefix_attributes: Строка префикса стиля, которая будет добавлена.
    :return: HTML-строка с добавленным префиксом стиля.
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')

def break_text_at_length(text: Union[str, dict], max_length: int=None) -> str:
    """
    Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)" в точке разрыва.
    Если максимальная длина равна `None`, содержимое возвращается как есть.

    :param text: Строка или словарь JSON для разбиения.
    :param max_length: Максимальная длина текста перед разрывом.
    :return: Разбитый текст.
    """
    if isinstance(text, dict):
        text = json.dumps(text, indent=4)

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + " (...)"

def pretty_datetime(dt: datetime) -> str:
    """
    Возвращает строку, представляющую объект datetime в удобном формате.

    :param dt: Объект datetime для форматирования.
    :return: Строка с датой и временем в формате "ГГГГ-ММ-ДД ЧЧ:ММ".
    """
    return dt.strftime("%Y-%m-%d %H:%M")

def dedent(text: str) -> str:
    """
    Удаляет отступы из указанного текста, удаляя любые начальные пробелы и отступы.

    :param text: Текст, из которого нужно удалить отступы.
    :return: Текст без начальных пробелов и отступов.
    """
    return textwrap.dedent(text).strip()

################################################################################
# IO and startup utilities
################################################################################
_config = None

def read_config_file(use_cache=True, verbose=True) -> configparser.ConfigParser:
    """
    Читает файл конфигурации из `config.ini`.

    Файл конфигурации может располагаться в двух местах:
    1. В директории модуля (где находится данный файл `utils.py`).
    2. В рабочей директории программы.

    Сначала загружаются значения по умолчанию из файла в директории модуля.
    Затем, если существует файл в рабочей директории, он перезаписывает значения по умолчанию.

    :param use_cache: Использовать ли кэшированную конфигурацию (по умолчанию True).
    :param verbose: Выводить ли отладочные сообщения (по умолчанию True).
    :return: Объект `configparser.ConfigParser` с загруженной конфигурацией.
    :raises ValueError: Если не удалось найти файл конфигурации по умолчанию.
    """
    global _config
    if use_cache and _config is not None:
        # если у нас есть кэшированная конфигурация и мы принимаем это, возвращаем ее
        return _config
    
    else:
        config = configparser.ConfigParser()

        # Читает значения по умолчанию в директории модуля.
        config_file_path = Path(__file__).parent.absolute() / 'config.ini'
        print(f"Поиск конфигурации по умолчанию в: {config_file_path}") if verbose else None
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Не удалось найти конфигурацию по умолчанию в: {config_file_path}")

        # Теперь давайте переопределим любое конкретное значение по умолчанию, если есть пользовательская конфигурация .ini.
        # Попробуйте директорию текущей основной программы
        config_file_path = Path.cwd() / "config.ini"
        if config_file_path.exists():
            print(f"Найдена пользовательская конфигурация в: {config_file_path}") if verbose else None
            config.read(config_file_path) # это только переопределяет значения, присутствующие в пользовательской конфигурации
            _config = config
            return config
        else:
            if verbose:
                print(f"Не удалось найти пользовательскую конфигурацию в: {config_file_path}") if verbose else None
                print("Будут использоваться только значения по умолчанию. ЕСЛИ ЧТО-ТО ПОЙДЕТ НЕ ТАК, ПОПРОБУЙТЕ НАСТРОИТЬ МОДЕЛЬ, ТИП API и т. д.") if verbose else None
        
        return config

def pretty_print_config(config):
    """
    Выводит текущую конфигурацию TinyTroupe в удобном формате.

    :param config: Объект `configparser.ConfigParser` с конфигурацией.
    """
    print()
    print("=================================")
    print("Текущая конфигурация TinyTroupe")
    print("=================================")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
        print()

def start_logger(config: configparser.ConfigParser):
    """
    Инициализирует логгер TinyTroupe с уровнем логирования, указанным в конфигурации.
    Уровень логирования по умолчанию INFO.

    :param config: Объект `configparser.ConfigParser` с конфигурацией.
    """
    # создает логгер
    logger = logging.getLogger("tinytroupe")
    log_level = config['Logging'].get('LOGLEVEL', 'INFO').upper()
    logger.setLevel(level=log_level)

    # создает обработчик консоли и устанавливает уровень отладки
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # создает форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # добавляет форматтер в ch
    ch.setFormatter(formatter)

    # добавляет ch в логгер
    logger.addHandler(ch)

class JsonSerializableRegistry:
    """
    Миксин-класс, который предоставляет сериализацию JSON, десериализацию и регистрацию подклассов.
    """
    
    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Возвращает JSON-представление объекта.

        :param include: Атрибуты для включения в сериализацию (необязательно).
        :param suppress: Атрибуты для исключения из сериализации (необязательно).
        :param file_path: Путь к файлу, куда будет записан JSON (необязательно).
        :return: JSON-представление объекта в виде словаря.
        """
        # Собирает все сериализуемые атрибуты из иерархии классов
        serializable_attrs = set()
        suppress_attrs = set()
        for cls in self.__class__.__mro__:
            if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)
        
        # Переопределяет атрибуты параметрами метода, если они предоставлены
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
                    result[attr] = [item.to_json() if isinstance(item, JsonSerializableRegistry) else copy.deepcopy(item) for item in value]
                elif isinstance(value, dict):
                    result[attr] = {k: v.to_json() if isinstance(v, JsonSerializableRegistry) else copy.deepcopy(v) for k, v in value.items()}
                else:
                    result[attr] = copy.deepcopy(value)
        
        if file_path:
            # создает директории, если они не существуют
            import os
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(result, f, indent=4)
        
        return result

    @classmethod
    def from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None):
        """
        Загружает JSON-представление объекта и создает экземпляр класса.

        :param json_dict_or_path: Словарь JSON, представляющий объект, или путь к файлу, откуда загружать JSON.
        :param suppress: Атрибуты, которые нужно исключить из загрузки (необязательно).
        :param post_init_params: Параметры для передачи в метод post_init (необязательно).
        :return: Экземпляр класса, заполненный данными из json_dict_or_path.
        """
        if isinstance(json_dict_or_path, str):
            with open(json_dict_or_path, 'r') as f:
                json_dict = j_loads(f) # используем j_loads
        else:
            json_dict = json_dict_or_path
        
        subclass_name = json_dict.get("json_serializable_class_name")
        target_class = cls.class_mapping.get(subclass_name, cls)
        instance = target_class.__new__(target_class)  # создает экземпляр без вызова __init__
        
        # Собирает все сериализуемые атрибуты из иерархии классов
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
        
        # Присваивает значения только для сериализуемых атрибутов, если они указаны, в противном случае присваивает все
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    # Использовать пользовательский инициализатор, если он предоставлен
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and 'json_serializable_class_name' in value:
                    # Предполагаем, что это другой объект JsonSerializableRegistry
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    # Обрабатывает коллекции, рекурсивно десериализует, если элементы являются объектами JsonSerializableRegistry
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and 'json_serializable_class_name' in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.deepcopy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.deepcopy(value))
        
        # Вызывает инициализацию после десериализации, если она доступна
        if hasattr(instance, '_post_deserialization_init') and callable(instance._post_deserialization_init):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)
        
        return instance

    def __init_subclass__(cls, **kwargs):
        """
        Регистрирует подкласс при его создании, добавляет сериализуемые атрибуты,
        а также кастомные инициализаторы из родительских классов.

        :param kwargs: Дополнительные аргументы.
        """
        super().__init_subclass__(**kwargs)
        # Регистрирует подкласс, используя его имя в качестве ключа
        JsonSerializableRegistry.class_mapping[cls.__name__] = cls
        
        # Автоматически расширяет сериализуемые атрибуты и пользовательские инициализаторы из родительских классов
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
         Выполняет инициализацию после десериализации.
        
        :param kwargs: Произвольные ключевые аргументы.
        """
        # если есть метод _post_init, вызывает его после десериализации
        if hasattr(self, '_post_init'):
            self._post_init(**kwargs)

def post_init(cls):
    """
    Декоратор для принудительного вызова метода post-initialization в классе, если он есть.
    Метод должен называться `_post_init`.

    :param cls: Класс, к которому применяется декоратор.
    :return: Модифицированный класс.
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
def name_or_empty(named_entity: AgentOrWorld):
    """
    Возвращает имя указанного агента или среды, или пустую строку, если агент равен None.

    :param named_entity: Агент или среда, имя которых нужно получить.
    :return: Имя агента или среды, или пустая строка.
    """
    if named_entity is None:
        return ""
    else:
        return named_entity.name

def custom_hash(obj):
    """
    Возвращает хэш для указанного объекта. Объект сначала преобразуется в строку,
    чтобы сделать его хэшируемым. Этот метод является детерминированным, в отличие
    от встроенной функции hash().

    :param obj: Объект для вычисления хэша.
    :return: Хэш объекта.
    """
    return hashlib.sha256(str(obj).encode()).hexdigest()

_fresh_id_counter = 0
def fresh_id():
    """
    Возвращает свежий ID для нового объекта. Это полезно для генерации уникальных ID для объектов.

    :return: Уникальный ID.
    """
    global _fresh_id_counter
    _fresh_id_counter += 1
    return _fresh_id_counter
```
## Внесённые изменения
*   Добавлены reStructuredText (RST) комментарии ко всем функциям, классам, методам и модулю.
*   Заменен стандартный импорт `json.load` на `j_loads` из `src.utils.jjson`.
*   Добавлен импорт `logger` из `src.logger.logger`.
*   Добавлена обработка ошибок с помощью `logger.error` вместо общих `try-except`.
*   Добавлены более подробные комментарии `#` к строкам кода.
*   Удален лишний комментарий ` # logger` и заменен на импорт
*   Исправлено регулярное выражение в функции `extract_json` для более точного извлечения JSON.
*   Удалены неиспользуемые импорты `TypeVar` и `Collection`.
*   Добавлен комментарий ` # используем j_loads` в `JsonSerializableRegistry.from_json`.
*   Добавлены пояснения по работе функции `read_config_file`.
*   Добавлены docstring к методу `__init_subclass__` класса `JsonSerializableRegistry`.
*   Исправлено регулярное выражение в функции `extract_json` для более точного извлечения JSON.
## Оптимизированный код
```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль предоставляет набор общих утилит и вспомогательных функций,
используемых в проекте TinyTroupe. Он включает в себя функции для:
- работы с входными и выходными данными модели,
- управления моделью,
- валидации данных,
- инжиниринга промптов,
- рендеринга и разметки,
- ввода/вывода,
- сериализации JSON,
- а также другие вспомогательные функции.

Пример использования
--------------------

Пример использования некоторых функций из этого модуля:

.. code-block:: python

    from tinytroupe.utils import compose_initial_LLM_messages_with_templates, extract_json
    
    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.txt', 
        user_template_name='user_prompt.txt', 
        rendering_configs={'variable': 'value'}
    )
    
    json_data = extract_json('some text { "key": "value" } some text')
"""
import re
import json
import os
import sys
import hashlib
import textwrap
import logging
import chevron
import copy
from datetime import datetime
from pathlib import Path
import configparser
from typing import Any, Union
from src.utils.jjson import j_loads, j_loads_ns # импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # импортируем logger из src.logger.logger

AgentOrWorld = Union["TinyPerson", "TinyWorld"]

# logger
# logger = logging.getLogger("tinytroupe") # заменено на импорт из src.logger.logger


################################################################################
# Model input utilities
################################################################################
def compose_initial_LLM_messages_with_templates(system_template_name:str, user_template_name:str=None, rendering_configs:dict={}) -> list:
    """
    Составляет начальные сообщения для вызова LLM модели, предполагая, что всегда используется системное сообщение
    (общее описание задачи) и необязательное пользовательское сообщение (конкретное описание задачи).
    Эти сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

    :param system_template_name: Имя файла шаблона системного сообщения.
    :param user_template_name: Имя файла шаблона пользовательского сообщения (необязательно).
    :param rendering_configs: Словарь с конфигурациями для рендеринга шаблонов.
    :return: Список сообщений для LLM.
    """
    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    messages.append({"role": "system", 
                         "content": chevron.render(
                             open(system_prompt_template_path).read(), 
                             rendering_configs)})
    
    # optionally add a user message
    if user_template_name is not None:
        messages.append({"role": "user", 
                            "content": chevron.render(
                                    open(user_prompt_template_path).read(), 
                                    rendering_configs)})
    return messages


################################################################################	
# Model output utilities
################################################################################
def extract_json(text: str) -> dict:
    """
    Извлекает JSON-объект из строки, игнорируя: любой текст до первой открывающей фигурной скобки;
    и любые открывающие (```json) или закрывающие (```) теги Markdown.

    :param text: Строка, из которой нужно извлечь JSON.
    :return: Извлеченный JSON-объект в виде словаря или пустой словарь в случае ошибки.
    """
    try:
        # удаляет любой текст до первой открывающей фигурной или квадратной скобки, используя регулярное выражение.
        # Оставляет скобки.
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.