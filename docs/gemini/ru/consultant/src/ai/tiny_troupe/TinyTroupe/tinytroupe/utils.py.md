# Анализ кода модуля tinytroupe.utils

**Качество кода**
7
-   Плюсы
    *   Код хорошо структурирован и разделен на логические блоки.
    *   Используются docstring для документирования функций.
    *   Присутствует обработка ошибок с использованием `try-except`.
    *   Реализована JSON сериализация и десериализация с поддержкой подклассов.
    *   Используется `configparser` для чтения конфигурационных файлов.
-   Минусы
    *   Не все функции и классы имеют reStructuredText (RST) docstring.
    *   Не везде используется `logger.error` для логирования ошибок, что приводит к избыточному использованию `try-except`.
    *   Используется стандартный `json.load` для чтения файлов, вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    *   Некоторые комментарии не соответствуют формату RST.
    *   Присутствует потенциальная проблема с циклическим импортом в `add_rai_template_variables_if_enabled`.

**Рекомендации по улучшению**

1.  **Документация**:
    *   Переписать все docstring в формате reStructuredText (RST), включая описания модулей, классов, функций и методов.
    *   Добавить подробные комментарии к коду, объясняющие логику и назначение каждого блока кода.
2.  **Импорты**:
    *   Добавить `from src.logger.logger import logger` для логирования.
    *   Заменить `import json` и `from json import JSONEncoder` на  `from src.utils.jjson import j_loads` и `from src.utils.jjson import j_dumps`.
    *   Использовать `Path` из `pathlib` вместо `os.path` там, где это уместно.
3.  **Обработка ошибок**:
    *   Заменить `try-except` блоки на использование `logger.error` для логирования ошибок и возврата значений по умолчанию или продолжения выполнения программы.
4.  **JSON обработка**:
    *   Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson`.
    *   Использовать `j_dumps` из `src.utils.jjson` для сериализации.
5.  **Рефакторинг**:
    *   Устранить потенциальный циклический импорт в `add_rai_template_variables_if_enabled`, перенеся импорт `config` из `tinytroupe` в начало файла.
    *   Улучшить читаемость кода, например, разделив длинные строки на несколько строк.
6. **Комментарии**:
    *   Переписать комментарии в коде, добавив подробные объяснения на русском языке.

**Оптимизированный код**
```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль содержит набор общих утилит, которые используются в проекте TinyTroupe.
Он включает функции для работы с текстовыми шаблонами, JSON, кодом, конфигурационными файлами,
а также для логирования и сериализации объектов.

Пример использования
--------------------

.. code-block:: python

    from tinytroupe.utils import compose_initial_LLM_messages_with_templates
    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.txt',
        user_template_name='user_prompt.txt',
        rendering_configs={'name': 'test'}
    )

    print(messages)
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
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger
from tinytroupe import config # Избегаем циклического импорта

AgentOrWorld = Union["TinyPerson", "TinyWorld"]

################################################################################
# Model input utilities
################################################################################
def compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}) -> list:
    """
    Составляет начальные сообщения для вызова LLM модели, предполагая, что всегда используется
    системное (общее описание задачи) и опциональное пользовательское сообщение (специфическое описание задачи).
    Эти сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

    :param system_template_name: Имя файла шаблона системного сообщения.
    :type system_template_name: str
    :param user_template_name: Имя файла шаблона пользовательского сообщения (опционально).
    :type user_template_name: str, optional
    :param rendering_configs: Словарь с конфигурациями для рендеринга шаблона.
    :type rendering_configs: dict, optional
    :return: Список сообщений, готовых для использования в LLM.
    :rtype: list
    """
    #  формирование пути к шаблону системного сообщения
    system_prompt_template_path = Path(__file__).parent / f'prompts/{system_template_name}'
    # формирование пути к шаблону пользовательского сообщения
    user_prompt_template_path = Path(__file__).parent / f'prompts/{user_template_name}'

    messages = []

    # добавление системного сообщения
    try:
        # открывает файл шаблона, выполняет рендеринг и добавляет сообщение
        with open(system_prompt_template_path, 'r') as f:
            messages.append({"role": "system",
                         "content": chevron.render(f.read(), rendering_configs)})
    except Exception as e:
        logger.error(f"Ошибка при чтении или рендеринге системного шаблона: {system_prompt_template_path}", exc_info=True)
        return []

    # опциональное добавление пользовательского сообщения
    if user_template_name is not None:
        try:
            # открывает файл шаблона, выполняет рендеринг и добавляет сообщение
            with open(user_prompt_template_path, 'r') as f:
                messages.append({"role": "user",
                            "content": chevron.render(f.read(), rendering_configs)})
        except Exception as e:
            logger.error(f"Ошибка при чтении или рендеринге пользовательского шаблона: {user_prompt_template_path}", exc_info=True)
            return messages  # Возвращаем только системное сообщение, если пользовательское не удалось добавить.
    return messages


################################################################################
# Model output utilities
################################################################################
def extract_json(text: str) -> dict:
    """
    Извлекает JSON объект из строки, игнорируя: любой текст перед первой
    открывающей фигурной скобкой; и любые Markdown открывающие (```json) или закрывающие (```) теги.

    :param text: Строка, из которой нужно извлечь JSON.
    :type text: str
    :return: Извлеченный JSON объект или пустой словарь в случае ошибки.
    :rtype: dict
    """
    try:
        # удаляет любой текст перед первой открывающей фигурной или квадратной скобкой
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последней закрывающей фигурной или квадратной скобки
        text = re.sub(r'(}|\])(?!.*(\]|}))*.?$', r'\1', text, flags=re.DOTALL)

        # удаляет недопустимые escape последовательности
        text = re.sub(r"\\\'", "\'", text)

        # возвращает распарсенный JSON объект
        return j_loads(text)
    except Exception as e:
        logger.error(f"Ошибка при извлечении JSON из текста: {text}", exc_info=True)
        return {}

def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя любой текст перед первыми
    открывающими тройными обратными кавычками и любой текст после закрывающих тройных обратных кавычек.

    :param text: Строка, из которой нужно извлечь блок кода.
    :type text: str
    :return: Извлеченный блок кода или пустая строка в случае ошибки.
    :rtype: str
    """
    try:
        # удаляет любой текст перед первыми открывающими тройными обратными кавычками
        text = re.sub(r'^.*?(```)', r'\1', text, flags=re.DOTALL)

        # удаляет любой текст после последней закрывающей тройной обратной кавычки
        text = re.sub(r'(```)(?!.*```).*$', r'\1', text, flags=re.DOTALL)

        return text
    except Exception as e:
        logger.error(f"Ошибка при извлечении блока кода из текста: {text}", exc_info=True)
        return ""

################################################################################
# Model control utilities
################################################################################
def repeat_on_error(retries: int, exceptions: list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из указанного списка,
    до указанного количества попыток. Если количество попыток превышено, исключение поднимается.
    Если исключение не возникает, функция возвращает значение нормально.

    :param retries: Количество попыток повторения.
    :type retries: int
    :param exceptions: Список классов исключений, которые нужно перехватывать.
    :type exceptions: list
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
    Проверяет, являются ли поля в указанном словаре допустимыми, согласно списку допустимых полей.
    Если нет, поднимает исключение ValueError.

    :param obj: Словарь для проверки.
    :type obj: dict
    :param valid_fields: Список допустимых полей.
    :type valid_fields: list
    :raises ValueError: Если найден недопустимый ключ в словаре.
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(f"Недопустимый ключ {key} в словаре. Допустимые ключи: {valid_fields}")

def sanitize_raw_string(value: str) -> str:
    """
    Очищает указанную строку путем:
      - удаления любых недопустимых символов.
      - гарантирования, что она не длиннее максимальной длины строки Python.

    Это делается для предосторожности и безопасности, чтобы избежать любых потенциальных проблем со строкой.

    :param value: Строка для очистки.
    :type value: str
    :return: Очищенная строка.
    :rtype: str
    """
    # удаляет недопустимые символы, убеждаясь, что это допустимая строка UTF-8
    value = value.encode("utf-8", "ignore").decode("utf-8")

    # гарантирует, что она не длиннее максимальной длины строки Python
    return value[:sys.maxsize]

def sanitize_dict(value: dict) -> dict:
    """
    Очищает указанный словарь путем:
      - удаления любых недопустимых символов.
      - гарантирования, что словарь не является слишком глубоко вложенным.

    :param value: Словарь для очистки.
    :type value: dict
    :return: Очищенный словарь.
    :rtype: dict
    """
    # очищает строковое представление словаря
    tmp_str = sanitize_raw_string(j_dumps(value, ensure_ascii=False))

    value = j_loads(tmp_str)

    # гарантирует, что словарь не является слишком глубоко вложенным
    return value


################################################################################
# Prompt engineering
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет RAI переменные шаблона в указанный словарь, если включены предупреждения RAI.
    Они могут быть настроены в файле config.ini. Если включено, переменные загрузят предупреждения RAI
    из соответствующих файлов в каталоге prompts. В противном случае переменные будут установлены в None.

    :param template_variables: Словарь переменных шаблона, в который нужно добавить переменные RAI.
    :type template_variables: dict
    :return: Обновленный словарь переменных шаблона.
    :rtype: dict
    """

    rai_harmful_content_prevention = config["Simulation"].getboolean(
        "RAI_HARMFUL_CONTENT_PREVENTION", True
    )
    rai_copyright_infringement_prevention = config["Simulation"].getboolean(
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION", True
    )

    # Harmful content
    try:
       # открывает файл и читает контент
        with open(Path(__file__).parent / "prompts/rai_harmful_content_prevention.md", "r") as f:
            rai_harmful_content_prevention_content = f.read()
    except Exception as e:
        logger.error("Ошибка при чтении файла rai_harmful_content_prevention.md", exc_info=True)
        rai_harmful_content_prevention_content = None
    template_variables['rai_harmful_content_prevention'] = rai_harmful_content_prevention_content if rai_harmful_content_prevention else None

    # Copyright infringement
    try:
       # открывает файл и читает контент
        with open(Path(__file__).parent / "prompts/rai_copyright_infringement_prevention.md", "r") as f:
            rai_copyright_infringement_prevention_content = f.read()
    except Exception as e:
        logger.error("Ошибка при чтении файла rai_copyright_infringement_prevention.md", exc_info=True)
        rai_copyright_infringement_prevention_content = None
    template_variables['rai_copyright_infringement_prevention'] = rai_copyright_infringement_prevention_content if rai_copyright_infringement_prevention else None

    return template_variables

################################################################################
# Rendering and markup
################################################################################
def inject_html_css_style_prefix(html: str, style_prefix_attributes: str) -> str:
    """
    Вставляет префикс стиля ко всем атрибутам стиля в заданной HTML строке.

    Например, если вы хотите добавить префикс стиля ко всем атрибутам стиля в HTML строке
    ``<div style="color: red;">Hello</div>``, вы можете использовать эту функцию следующим образом:
    inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')

    :param html: HTML строка для изменения.
    :type html: str
    :param style_prefix_attributes: Строка с префиксом стиля, который нужно добавить.
    :type style_prefix_attributes: str
    :return: HTML строка с добавленным префиксом стиля.
    :rtype: str
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')

def break_text_at_length(text: Union[str, dict], max_length: int = None) -> str:
    """
    Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)" в точке разрыва.
    Если максимальная длина равна `None`, контент возвращается как есть.

    :param text: Текст или JSON для разбиения.
    :type text: Union[str, dict]
    :param max_length: Максимальная длина текста (опционально).
    :type max_length: int, optional
    :return: Разбитый текст или исходный текст, если `max_length` равен None.
    :rtype: str
    """
    if isinstance(text, dict):
        text = j_dumps(text, indent=4)

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + " (...)"

def pretty_datetime(dt: datetime) -> str:
    """
    Возвращает красивое строковое представление указанного объекта datetime.

    :param dt: Объект datetime.
    :type dt: datetime
    :return: Строковое представление datetime.
    :rtype: str
    """
    return dt.strftime("%Y-%m-%d %H:%M")

def dedent(text: str) -> str:
    """
    Удаляет отступы из указанного текста, удаляя все начальные пробелы и отступы.

    :param text: Текст для удаления отступов.
    :type text: str
    :return: Текст без отступов.
    :rtype: str
    """
    return textwrap.dedent(text).strip()


################################################################################
# IO and startup utilities
################################################################################
_config = None

def read_config_file(use_cache: bool = True, verbose: bool = True) -> configparser.ConfigParser:
    """
    Читает конфигурационный файл, используя кеш, если это разрешено.

    :param use_cache: Использовать ли кешированную конфигурацию.
    :type use_cache: bool, optional
    :param verbose: Выводить ли сообщения в консоль.
    :type verbose: bool, optional
    :return: Объект configparser с загруженной конфигурацией.
    :rtype: configparser.ConfigParser
    :raises ValueError: Если не удается найти конфигурационный файл.
    """
    global _config
    if use_cache and _config is not None:
        # если есть кешированная конфигурация и это разрешено, возвращает ее
        return _config

    else:
        config = configparser.ConfigParser()

        # читает значения по умолчанию из каталога модуля
        config_file_path = Path(__file__).parent.absolute() / 'config.ini'
        if verbose:
            print(f"Поиск файла конфигурации по умолчанию: {config_file_path}")
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Не удалось найти файл конфигурации по умолчанию: {config_file_path}")

        # переопределение значений по умолчанию, если есть пользовательская конфигурация
        # пытается найти в директории текущей программы
        config_file_path = Path.cwd() / "config.ini"
        if config_file_path.exists():
            if verbose:
                print(f"Найдена пользовательская конфигурация: {config_file_path}")
            config.read(config_file_path) # переопределяет значения, которые есть в пользовательской конфигурации
            _config = config
            return config
        else:
            if verbose:
                print(f"Не удалось найти пользовательскую конфигурацию: {config_file_path}")
                print("Будут использоваться только значения по умолчанию. ЕСЛИ ЧТО-ТО НЕ РАБОТАЕТ, ПОПРОБУЙТЕ НАСТРОИТЬ МОДЕЛЬ, ТИП API и т.д.")

        return config


def pretty_print_config(config: configparser.ConfigParser):
    """
    Выводит конфигурацию в консоль в удобочитаемом формате.

    :param config: Объект configparser с конфигурацией.
    :type config: configparser.ConfigParser
    """
    print()
    print("=================================")
    print("Текущая конфигурация TinyTroupe ")
    print("=================================")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
        print()

def start_logger(config: configparser.ConfigParser):
    """
    Инициализирует и настраивает логгер.

    :param config: Объект configparser с конфигурацией.
    :type config: configparser.ConfigParser
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

    # добавляет форматтер в обработчик
    ch.setFormatter(formatter)

    # добавляет обработчик в логгер
    logger.addHandler(ch)


class JsonSerializableRegistry:
    """
    Миксин, который предоставляет сериализацию и десериализацию JSON, а также регистрацию подклассов.

    :ivar class_mapping: Словарь, содержащий соответствие имени класса классу.
    :vartype class_mapping: dict
    """
    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Возвращает JSON представление объекта.

        :param include: Атрибуты для включения в сериализацию (опционально).
        :type include: list, optional
        :param suppress: Атрибуты для исключения из сериализации (опционально).
        :type suppress: list, optional
        :param file_path: Путь к файлу, куда будет записан JSON (опционально).
        :type file_path: str, optional
        :return: JSON представление объекта.
        :rtype: dict
        """
        # сбор всех сериализуемых атрибутов из иерархии классов
        serializable_attrs = set()
        suppress_attrs = set()
        for cls in self.__class__.__mro__:
            if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)

        # переопределение атрибутов параметрами метода, если они переданы
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
            # создает каталоги, если их не существует
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                j_dumps(result, f, indent=4)

        return result


    @classmethod
    def from_json(cls, json_dict_or_path: Union[dict, str], suppress: list = None, post_init_params: dict = None):
        """
        Загружает JSON представление объекта и создает экземпляр класса.

        :param json_dict_or_path: JSON словарь или путь к файлу для загрузки JSON.
        :type json_dict_or_path: Union[dict, str]
        :param suppress: Атрибуты для исключения из загрузки (опционально).
        :type suppress: list, optional
        :param post_init_params: Параметры для передачи в метод пост-инициализации.
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
        instance = target_class.__new__(target_class)  # создает экземпляр без вызова __init__

        # сбор всех сериализуемых атрибутов из иерархии классов
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

        # присваивает значения только для сериализуемых атрибутов, если они указаны, иначе присваивает все
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    # использует кастомный инициализатор, если он есть
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and 'json_serializable_class_name' in value:
                    # предположение, что это другой объект JsonSerializableRegistry
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    # обрабатывает коллекции, рекурсивно десериализует элементы, если это объекты JsonSerializableRegistry
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and 'json_serializable_class_name' in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.deepcopy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.deepcopy(value))

        # вызывает пост-десериализационную инициализацию, если она есть
        if hasattr(instance, '_post_deserialization_init') and callable(instance._post_deserialization_init):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)

        return instance


    def __init_subclass__(cls, **kwargs):
        """
        Регистрирует подкласс при его создании.

        :param kwargs: Дополнительные именованные аргументы для передачи в родительский метод.
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
        Метод пост-десериализации инициализации, который вызывается после десериализации,
        если у класса есть метод `_post_init`.

        :param kwargs: Дополнительные именованные аргументы.
        """
        # если есть метод _post_init, вызывает его после десериализации
        if hasattr(self, '_post_init'):
            self._post_init(**kwargs)

def post_init(cls):
    """
    Декоратор для принудительного вызова метода пост-инициализации в классе, если он есть.
    Метод должен называться `_post_init`.

    :param cls: Класс для декорирования.
    :return: Декорированный класс.
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
    Возвращает имя указанного агента или окружения, или пустую строку, если агент равен None.

    :param named_entity: Агент или окружение.
    :type named_entity: AgentOrWorld
    :return: Имя агента или пустая строка.
    :rtype: str
    """
    if named_entity is None:
        return ""
    else:
        return named_entity.name

def custom_hash(obj: Any) -> str:
    """
    Возвращает хеш для указанного объекта. Объект сначала преобразуется
    в строку, чтобы сделать его хешируемым. Этот метод является детерминированным,
    в отличие от встроенной функции hash().

    :param obj: Объект для хеширования.
    :type obj: Any
    :return: Хеш объекта.
    :rtype: str
    """
    return hashlib.sha256(str(obj).encode()).hexdigest()

_fresh_id_counter = 0
def fresh_id() -> int:
    """
    Возвращает новый ID для нового объекта. Это полезно для генерации уникальных ID для объектов.

    :return: Уникальный ID.
    :rtype: int
    """
    global _fresh_id_counter
    _fresh_id_counter += 1
    return _fresh_id_counter