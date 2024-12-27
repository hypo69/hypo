# Анализ кода модуля `utils.py`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки с комментариями, что облегчает понимание.
    - Используются `typing` для аннотации типов, что улучшает читаемость и помогает в отладке.
    - Присутствуют docstring для функций и классов, объясняющие их назначение и параметры.
    - Код использует `configparser` для чтения конфигурационных файлов, что является хорошей практикой.
    - Реализован механизм повторных попыток при ошибках с помощью декоратора `repeat_on_error`.
    - Есть класс `JsonSerializableRegistry`, который обеспечивает сериализацию и десериализацию объектов.
-  Минусы
    - Используется стандартный модуль `json` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Некоторые комментарии не соответствуют стандарту reStructuredText (RST).
    - Присутствуют избыточные блоки try-except, которые могут быть заменены логированием с помощью `logger.error`.
    - В некоторых функциях используются прямые вызовы `print`, которые должны быть заменены на логирование через `logger.debug` или `logger.info`.
    - В некоторых местах используются `...` как точки остановки, но они не документированы.
    - Не все функции имеют подробные RST комментарии.

**Рекомендации по улучшению**

1.  **Использовать `j_loads` и `j_loads_ns`**: Замените все `json.load` и `json.loads` на `j_loads` и `j_loads_ns` из `src.utils.jjson`.
2.  **Форматирование комментариев**: Перепишите все комментарии в формате RST, включая docstring функций и классов.
3.  **Логирование ошибок**: Замените блоки `try-except` на логирование ошибок через `logger.error` и убрать `...` .
4.  **Заменить `print` на `logger`**: Замените прямые вызовы `print` на `logger.debug` или `logger.info`.
5.  **Удалить неиспользуемый импорт**: Удалить неиспользуемые импорты.
6.  **Документировать `...`**: Документируйте использование `...` в коде.
7.  **Добавить импорты**: Добавить недостающие импорты.

**Оптимизированный код**

```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль содержит набор общих утилит, которые используются в проекте TinyTroupe.
Он включает в себя функции для работы с JSON, текстом, файлами конфигурации, логирования,
а также для сериализации и десериализации объектов.

Пример использования
--------------------

Пример использования функции ``compose_initial_LLM_messages_with_templates``:

.. code-block:: python

    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.txt',
        user_template_name='user_prompt.txt',
        rendering_configs={'var': 'value'}
    )
"""
import re
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
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

AgentOrWorld = Union["TinyPerson", "TinyWorld"]


################################################################################
# Утилиты для ввода модели
################################################################################
def compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}) -> list:
    """
    Составляет начальные сообщения для вызова LLM модели, предполагая, что всегда
    имеется системное сообщение (общее описание задачи) и опциональное сообщение пользователя
    (конкретное описание задачи). Эти сообщения составляются с использованием указанных
    шаблонов и конфигураций рендеринга.

    :param system_template_name: Имя файла шаблона системного сообщения.
    :type system_template_name: str
    :param user_template_name: Имя файла шаблона сообщения пользователя (опционально).
    :type user_template_name: str, optional
    :param rendering_configs: Словарь с параметрами для рендеринга шаблонов.
    :type rendering_configs: dict, optional
    :return: Список сообщений для LLM модели.
    :rtype: list
    """
    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    messages.append({"role": "system",
                         "content": chevron.render(
                             open(system_prompt_template_path).read(),
                             rendering_configs)})
    
    # опционально добавляет сообщение пользователя
    if user_template_name is not None:
        messages.append({"role": "user",
                            "content": chevron.render(
                                    open(user_prompt_template_path).read(),
                                    rendering_configs)})
    return messages


################################################################################
# Утилиты для вывода модели
################################################################################
def extract_json(text: str) -> dict:
    """
    Извлекает объект JSON из строки, игнорируя любой текст до первой открывающей
    фигурной скобки и любые открывающие (```json) или закрывающие (```) теги Markdown.

    :param text: Строка для извлечения JSON.
    :type text: str
    :return: Извлеченный объект JSON или пустой словарь в случае ошибки.
    :rtype: dict
    """
    try:
        # удаляет любой текст до первой открывающей фигурной или квадратной скобки, используя regex. Оставляет скобки.
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последней закрывающей фигурной или квадратной скобки, используя regex. Оставляет скобки.
        text = re.sub(r'(}|\])(?!.*(\]|})).*$', r'\1', text, flags=re.DOTALL)
        
        # удаляет недопустимые escape-последовательности, которые иногда появляются
        # заменяет \\\' на просто \'
        text =  re.sub("\\\\\'", "\'", text)

        # возвращает разобранный JSON объект
        return j_loads(text)
    
    except Exception as e:
        logger.error(f"Ошибка при извлечении JSON из текста: {e}")
        return {}

def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя любой текст до первого открывающего
    тройного обратного апострофа и любой текст после закрывающего тройного обратного апострофа.

    :param text: Строка для извлечения блока кода.
    :type text: str
    :return: Извлеченный блок кода или пустая строка в случае ошибки.
    :rtype: str
    """
    try:
        # удаляет любой текст до первого открывающего тройного обратного апострофа, используя regex. Оставляет апострофы.
        text = re.sub(r'^.*?(```)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последнего закрывающего тройного обратного апострофа, используя regex. Оставляет апострофы.
        text = re.sub(r'(```)(?!.*```).*$', r'\1', text, flags=re.DOTALL)
        
        return text
    
    except Exception as e:
        logger.error(f"Ошибка при извлечении блока кода из текста: {e}")
        return ""

################################################################################
# Утилиты для управления моделью
################################################################################
def repeat_on_error(retries: int, exceptions: list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из
    указанного списка, до указанного количества повторных попыток. Если это количество
    повторных попыток превышено, исключение вызывается. Если исключение не возникает,
    функция возвращается нормально.

    :param retries: Количество повторных попыток.
    :type retries: int
    :param exceptions: Список классов исключений для перехвата.
    :type exceptions: list
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as e:
                    logger.debug(f"Возникло исключение: {e}")
                    if i == retries - 1:
                        raise e
                    else:
                        logger.debug(f"Повторная попытка ({i+1}/{retries})...")
                        continue
        return wrapper
    return decorator
   

################################################################################
# Валидация
################################################################################
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Проверяет, являются ли поля в указанном словаре допустимыми, согласно списку
    допустимых полей. Если нет, вызывает ValueError.

    :param obj: Словарь для проверки.
    :type obj: dict
    :param valid_fields: Список допустимых полей.
    :type valid_fields: list
    :raises ValueError: Если в словаре есть недопустимые поля.
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(f"Недопустимый ключ {key} в словаре. Допустимые ключи: {valid_fields}")

def sanitize_raw_string(value: str) -> str:
    """
    Очищает указанную строку путем:
      - удаления любых недопустимых символов.
      - гарантируя, что она не длиннее максимальной длины строки Python.
    
    Это делается для предосторожности в целях безопасности, чтобы избежать любых
    потенциальных проблем со строкой.

    :param value: Строка для очистки.
    :type value: str
    :return: Очищенная строка.
    :rtype: str
    """

    # удаляет любые недопустимые символы, удостоверяясь, что это допустимая строка UTF-8
    value = value.encode("utf-8", "ignore").decode("utf-8")

    # гарантирует, что она не длиннее максимальной длины строки Python
    return value[:sys.maxsize]

def sanitize_dict(value: dict) -> dict:
    """
    Очищает указанный словарь путем:
      - удаления любых недопустимых символов.
      - гарантируя, что словарь не является слишком глубоко вложенным.

    :param value: Словарь для очистки.
    :type value: dict
    :return: Очищенный словарь.
    :rtype: dict
    """

    # очищает строковое представление словаря
    tmp_str = sanitize_raw_string(j_loads(str(value)))

    value = j_loads(tmp_str)

    # гарантирует, что словарь не является слишком глубоко вложенным
    return value
    
    
################################################################################
# Проектирование подсказок
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет переменные шаблона RAI в указанный словарь, если включены
    дисклеймеры RAI. Они могут быть настроены в файле config.ini. Если они включены,
    переменные будут загружать дисклеймеры RAI из соответствующих файлов
    в каталоге prompts. В противном случае переменные будут установлены в None.

    :param template_variables: Словарь переменных шаблона, к которому нужно добавить переменные RAI.
    :type template_variables: dict
    :return: Обновленный словарь переменных шаблона.
    :rtype: dict
    """

    from tinytroupe import config # позволяет избежать циклического импорта
    rai_harmful_content_prevention = config["Simulation"].getboolean(
        "RAI_HARMFUL_CONTENT_PREVENTION", True
    )
    rai_copyright_infringement_prevention = config["Simulation"].getboolean(
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION", True
    )

    # Вредный контент
    with open(os.path.join(os.path.dirname(__file__), "prompts/rai_harmful_content_prevention.md"), "r") as f:
        rai_harmful_content_prevention_content = f.read()

    template_variables['rai_harmful_content_prevention'] = rai_harmful_content_prevention_content if rai_harmful_content_prevention else None

    # Нарушение авторских прав
    with open(os.path.join(os.path.dirname(__file__), "prompts/rai_copyright_infringement_prevention.md"), "r") as f:
        rai_copyright_infringement_prevention_content = f.read()

    template_variables['rai_copyright_infringement_prevention'] = rai_copyright_infringement_prevention_content if rai_copyright_infringement_prevention else None

    return template_variables

################################################################################
# Рендеринг и разметка
################################################################################
def inject_html_css_style_prefix(html, style_prefix_attributes):
    """
    Вставляет префикс стиля ко всем атрибутам style в данной HTML-строке.

    Например, если вы хотите добавить префикс стиля ко всем атрибутам style в
    HTML-строке ``<div style="color: red;">Hello</div>``, вы можете использовать
    эту функцию следующим образом:
    ``inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')``

    :param html: HTML строка, в которую нужно вставить префикс.
    :type html: str
    :param style_prefix_attributes: Префикс стиля, который нужно вставить.
    :type style_prefix_attributes: str
    :return: HTML строка с вставленным префиксом.
    :rtype: str
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')

def break_text_at_length(text: Union[str, dict], max_length: int = None) -> str:
    """
    Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)"
    в точке разрыва. Если максимальная длина равна None, то содержимое возвращается как есть.

    :param text: Текст или JSON для разбиения.
    :type text: Union[str, dict]
    :param max_length: Максимальная длина текста.
    :type max_length: int, optional
    :return: Разбитый текст.
    :rtype: str
    """
    if isinstance(text, dict):
        text = j_loads(str(text), indent=4)

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + " (...)"

def pretty_datetime(dt: datetime) -> str:
    """
    Возвращает красивое строковое представление указанного объекта datetime.

    :param dt: Объект datetime.
    :type dt: datetime
    :return: Строковое представление даты и времени.
    :rtype: str
    """
    return dt.strftime("%Y-%m-%d %H:%M")

def dedent(text: str) -> str:
    """
    Удаляет отступ из указанного текста, удаляя любые начальные пробелы и отступы.

    :param text: Текст, из которого нужно удалить отступ.
    :type text: str
    :return: Текст без отступа.
    :rtype: str
    """
    return textwrap.dedent(text).strip()

################################################################################
# Утилиты ввода-вывода и запуска
################################################################################
_config = None

def read_config_file(use_cache=True, verbose=True) -> configparser.ConfigParser:
    """
    Читает файл конфигурации, используя кэш, если возможно.

    :param use_cache: Использовать ли кэшированную конфигурацию, defaults to True.
    :type use_cache: bool, optional
    :param verbose: Выводить ли подробную информацию, defaults to True.
    :type verbose: bool, optional
    :return: Объект конфигурации.
    :rtype: configparser.ConfigParser
    :raises ValueError: Если не удается найти файл конфигурации.
    """
    global _config
    if use_cache and _config is not None:
        # если есть кэшированная конфигурация и это приемлимо, возвращает её
        return _config
    
    else:
        config = configparser.ConfigParser()

        # считывает значения по умолчанию из каталога модуля.
        config_file_path = Path(__file__).parent.absolute() / 'config.ini'
        logger.debug(f"Поиск файла конфигурации по умолчанию: {config_file_path}") if verbose else None
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Не удалось найти файл конфигурации по умолчанию: {config_file_path}")

        # переопределяет любые конкретные значения по умолчанию, если есть пользовательская конфигурация .ini
        # проверяет каталог текущей основной программы
        config_file_path = Path.cwd() / "config.ini"
        if config_file_path.exists():
            logger.debug(f"Найдена пользовательская конфигурация: {config_file_path}") if verbose else None
            config.read(config_file_path) # это переопределяет только те значения, которые присутствуют в пользовательской конфигурации
            _config = config
            return config
        else:
            if verbose:
                logger.debug(f"Не удалось найти пользовательскую конфигурацию: {config_file_path}") if verbose else None
                logger.debug("Будут использоваться только значения по умолчанию. ЕСЛИ ЧТО-ТО НЕ РАБОТАЕТ, ПОПРОБУЙТЕ НАСТРОИТЬ МОДЕЛЬ, ТИП API и т.д.") if verbose else None
        
        return config

def pretty_print_config(config):
    """
    Выводит текущую конфигурацию в консоль.

    :param config: Объект конфигурации.
    :type config: configparser.ConfigParser
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
    Инициализирует логгер с уровнем, указанным в конфигурации.

    :param config: Объект конфигурации.
    :type config: configparser.ConfigParser
    """
    # создает логгер
    logger = logging.getLogger("tinytroupe")
    log_level = config['Logging'].get('LOGLEVEL', 'INFO').upper()
    logger.setLevel(level=log_level)

    # создает обработчик консоли и устанавливает уровень на debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # создает форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # добавляет форматтер к ch
    ch.setFormatter(formatter)

    # добавляет ch к логгеру
    logger.addHandler(ch)

class JsonSerializableRegistry:
    """
    Миксин-класс, обеспечивающий сериализацию, десериализацию JSON и регистрацию подклассов.
    """
    
    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Возвращает JSON представление объекта.
        
        :param include: Атрибуты для включения в сериализацию, defaults to None.
        :type include: list, optional
        :param suppress: Атрибуты для исключения из сериализации, defaults to None.
        :type suppress: list, optional
        :param file_path: Путь к файлу, куда будет записан JSON, defaults to None.
        :type file_path: str, optional
        :return: JSON представление объекта.
        :rtype: dict
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
            # создает каталоги, если они не существуют
            import os
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                j_loads(str(result), f, indent=4)
        
        return result

    @classmethod
    def from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None):
        """
        Загружает JSON представление объекта и создает экземпляр класса.
        
        :param json_dict_or_path: JSON словарь, представляющий объект, или путь к файлу для загрузки JSON.
        :type json_dict_or_path: dict or str
        :param suppress: Атрибуты, которые нужно исключить из загрузки, defaults to None.
        :type suppress: list, optional
        :param post_init_params: Параметры для передачи в метод post_init, defaults to None.
        :type post_init_params: dict, optional
        :return: Экземпляр класса, заполненный данными из json_dict_or_path.
        :rtype: JsonSerializableRegistry
        """
        if isinstance(json_dict_or_path, str):
            with open(json_dict_or_path, 'r') as f:
                json_dict = j_loads(f.read())
        else:
            json_dict = json_dict_or_path
        
        subclass_name = json_dict.get("json_serializable_class_name")
        target_class = cls.class_mapping.get(subclass_name, cls)
        instance = target_class.__new__(target_class)  # Создает экземпляр без вызова __init__
        
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
        
        # Назначает значения только для сериализуемых атрибутов, если они указаны, в противном случае назначает все
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    # Использует пользовательский инициализатор, если он предоставлен
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and 'json_serializable_class_name' in value:
                    # Предполагает, что это другой объект JsonSerializableRegistry
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    # обрабатывает коллекции, рекурсивно десериализует, если элементы являются объектами JsonSerializableRegistry
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and 'json_serializable_class_name' in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.deepcopy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.deepcopy(value))
        
        # вызывает инициализацию после десериализации, если она доступна
        if hasattr(instance, '_post_deserialization_init') and callable(instance._post_deserialization_init):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)
        
        return instance

    def __init_subclass__(cls, **kwargs):
        """
        Регистрирует подкласс при его создании.

        :param kwargs: Произвольные аргументы.
        :type kwargs: dict
        """
        super().__init_subclass__(**kwargs)
        # регистрирует подкласс, используя его имя в качестве ключа
        JsonSerializableRegistry.class_mapping[cls.__name__] = cls
        
        # автоматически расширяет сериализуемые атрибуты и пользовательские инициализаторы из родительских классов
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
        Вызывает метод _post_init после десериализации, если он существует.

        :param kwargs: Произвольные аргументы.
        :type kwargs: dict
        """
        # если есть метод _post_init, вызывает его после десериализации
        if hasattr(self, '_post_init'):
            self._post_init(**kwargs)


def post_init(cls):
    """
    Декоратор для принудительного вызова метода post-initialization в классе, если он есть.
    Метод должен называться `_post_init`.

    :param cls: Класс, к которому применяется декоратор.
    :type cls: type
    :return: Модифицированный класс.
    :rtype: type
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        if hasattr(self, '_post_init'):
            self._post_init()

    cls.__init__ = new_init
    return cls

################################################################################
# Другое
################################################################################
def name_or_empty(named_entity: AgentOrWorld):
    """
    Возвращает имя указанного агента или среды, или пустую строку, если агент равен None.

    :param named_entity: Агент или среда.
    :type named_entity: AgentOrWorld
    :return: Имя агента или пустая строка.
    :rtype: str
    """
    if named_entity is None:
        return ""
    else:
        return named_entity.name

def custom_hash(obj):
    """
    Возвращает хеш для указанного объекта. Объект сначала преобразуется в строку,
    чтобы сделать его хешируемым. Этот метод является детерминированным,
    в отличие от встроенной функции hash().

    :param obj: Объект для хеширования.
    :type obj: Any
    :return: Хеш объекта.
    :rtype: str
    """

    return hashlib.sha256(str(obj).encode()).hexdigest()

_fresh_id_counter = 0
def fresh_id():
    """
    Возвращает новый ID для нового объекта. Это полезно для создания уникальных ID
    для объектов.

    :return: Новый уникальный ID.
    :rtype: int
    """
    global _fresh_id_counter
    _fresh_id_counter += 1
    return _fresh_id_counter
```