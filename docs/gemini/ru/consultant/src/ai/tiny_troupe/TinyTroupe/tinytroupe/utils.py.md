# Анализ кода модуля utils.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, разделен на логические блоки с комментариями.
    - Используются декораторы для повторения операций при ошибках.
    - Присутствует обработка исключений.
    - Есть функции для работы с JSON, строками, датами, конфигурацией и логированием.
    - Реализован класс `JsonSerializableRegistry` для сериализации и десериализации объектов.
    - Используются `configparser` для работы с конфигурационными файлами.
-  Минусы
    - Не все функции имеют docstring в формате reStructuredText.
    - Используются стандартные `json.load` и `json.dumps` вместо `j_loads` и `j_dumps` из `src.utils.jjson`.
    - Есть избыточное использование стандартных блоков `try-except`, вместо `logger.error`.
    - Не везде используется `from src.logger.logger import logger` для логирования.
    - Есть `print` для отладочной печати, лучше использовать logger.debug/info.
    - В некоторых местах нужно более подробное описание выполняемых действий в комментариях после `#`.

**Рекомендации по улучшению**

1.  **Формат документации**:
    - Добавить docstring в формате RST для всех функций, методов и классов.
    - Переписать все существующие комментарии в формате reStructuredText.

2.  **Импорты**:
    - Добавить `from src.utils.jjson import j_loads, j_dumps` и использовать их вместо стандартных `json.load` и `json.dumps`.
    - Добавить `from src.logger.logger import logger` и использовать его для логирования ошибок.

3.  **Обработка ошибок**:
    - Заменить избыточные блоки `try-except` на `logger.error`.

4.  **Логирование**:
    - Заменить `print` на `logger.debug` или `logger.info` для отладочной печати.
    - Добавить подробное описание действий в комментариях после `#`.

5.  **Рефакторинг**:
    - Переименовать `_config` в `_CONFIG` как константу.
    - Переименовать `config_file_path` в `CONFIG_FILE_PATH`.

**Оптимизированный код**
```python
"""
Общие утилиты и вспомогательные функции.
=========================================================================================

Этот модуль содержит набор общих утилит, используемых в проекте, включая функции для:

-   композиции сообщений для LLM моделей с использованием шаблонов,
-   извлечения JSON и блоков кода из текста,
-   повторного выполнения функций при ошибках,
-   проверки валидности полей,
-   санитарной обработки строк и словарей,
-   добавления RAI переменных в шаблоны,
-   инъекции CSS в HTML,
-   обрезки текста,
-   форматирования дат,
-   чтения и обработки конфигурационных файлов,
-   сериализации и десериализации JSON,
-   генерации хешей и уникальных ID.

Пример использования
--------------------

Пример использования функции ``compose_initial_LLM_messages_with_templates``:

.. code-block:: python

    messages = compose_initial_LLM_messages_with_templates(
        system_template_name='system_prompt.txt',
        user_template_name='user_prompt.txt',
        rendering_configs={'name': 'example'}
    )

"""
import re
# from src.utils.jjson import j_loads, j_dumps #TODO  Не используется
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
from src.logger.logger import logger  # импортируем logger
AgentOrWorld = Union["TinyPerson", "TinyWorld"]

# logger
# logger = logging.getLogger("tinytroupe") #TODO: Уже импортирован выше


################################################################################
# Model input utilities
################################################################################

def compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}) -> list:
    """
    Составляет начальные сообщения для вызова LLM-модели, предполагая, что всегда есть
    системное сообщение (общее описание задачи) и необязательное сообщение пользователя (конкретное описание задачи).
    Эти сообщения составляются с использованием указанных шаблонов и настроек рендеринга.

    :param system_template_name: Имя файла шаблона системного сообщения.
    :param user_template_name: Имя файла шаблона сообщения пользователя (необязательно).
    :param rendering_configs: Словарь с настройками для рендеринга шаблона.
    :return: Список сообщений для LLM-модели.
    """
    # формируем путь к файлу шаблона системного сообщения
    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    # формируем путь к файлу шаблона пользовательского сообщения
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    # добавляем системное сообщение в список сообщений
    messages.append({"role": "system",
                         "content": chevron.render(
                             open(system_prompt_template_path).read(),
                             rendering_configs)})

    # добавляем пользовательское сообщение в список сообщений если шаблон был передан
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
    Извлекает JSON-объект из строки, игнорируя любой текст до первой открывающей
    фигурной скобки и любые открывающие (```json) или закрывающие (```) теги Markdown.

    :param text: Строка, из которой нужно извлечь JSON.
    :return: Извлеченный JSON-объект или пустой словарь, если извлечение не удалось.
    """
    try:
        # Удаляет любой текст перед первой открывающей фигурной или квадратной скобкой, оставляя скобки
        text = re.sub(r'^.*?({|\[)', r'\1', text, flags=re.DOTALL)

        # Удаляет любой текст после последней закрывающей фигурной или квадратной скобки, оставляя скобки
        text = re.sub(r'(}|\])(?!.*(\]|}))', r'\1', text, flags=re.DOTALL)

        # Удаляет недопустимые escape-последовательности
        text = re.sub(r"\\\\'", "\'", text) # заменяет \\\' на \'

        # возвращаем распарсенный JSON-объект
        return json.loads(text)

    except Exception as e:
        logger.error(f'Ошибка при извлечении JSON: {e}')
        return {}


def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя любой текст до первых трех обратных кавычек
    и любой текст после закрывающих трех обратных кавычек.

    :param text: Строка, из которой нужно извлечь блок кода.
    :return: Извлеченный блок кода или пустая строка, если извлечение не удалось.
    """
    try:
        # Удаляет любой текст перед первыми тремя обратными кавычками, оставляя кавычки
        text = re.sub(r'^.*?(```)', r'\1', text, flags=re.DOTALL)

        # Удаляет любой текст после последних трех обратных кавычек, оставляя кавычки
        text = re.sub(r'(```)(?!.*```).*$', r'\1', text, flags=re.DOTALL)

        return text
    except Exception as e:
        logger.error(f'Ошибка при извлечении блока кода: {e}')
        return ""


################################################################################
# Model control utilities
################################################################################

def repeat_on_error(retries: int, exceptions: list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из списка указанных,
    до указанного количества попыток. Если количество попыток превышено, исключение поднимается.
    Если исключение не возникает, функция возвращается нормально.

    :param retries: Количество попыток повтора.
    :param exceptions: Список классов исключений, которые нужно отлавливать.
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
                        logger.debug(f"Повторная попытка ({i + 1}/{retries})...")
                        continue
        return wrapper
    return decorator


################################################################################
# Validation
################################################################################
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Проверяет, являются ли поля в указанном словаре допустимыми, согласно списку допустимых полей.
    Если нет, вызывает ValueError.

    :param obj: Словарь для проверки.
    :param valid_fields: Список допустимых полей.
    :raises ValueError: Если обнаружено недопустимое поле.
    """
    for key in obj:
        if key not in valid_fields:
            raise ValueError(f"Недопустимый ключ {key} в словаре. Допустимые ключи: {valid_fields}")


def sanitize_raw_string(value: str) -> str:
    """
    Очищает указанную строку, удаляя недопустимые символы и гарантируя, что ее длина
    не превышает максимальную длину строки Python.

    :param value: Строка для очистки.
    :return: Очищенная строка.
    """

    # удаляем любые недопустимые символы, проверяя, что это допустимая строка UTF-8
    value = value.encode("utf-8", "ignore").decode("utf-8")

    # гарантируем, что она не длиннее максимальной длины строки Python
    return value[:sys.maxsize]


def sanitize_dict(value: dict) -> dict:
    """
    Очищает указанный словарь, удаляя недопустимые символы и гарантируя, что словарь не является
    слишком глубоко вложенным.

    :param value: Словарь для очистки.
    :return: Очищенный словарь.
    """
    # очищаем строковое представление словаря
    tmp_str = sanitize_raw_string(json.dumps(value, ensure_ascii=False))

    value = json.loads(tmp_str)

    # гарантируем, что словарь не является слишком глубоко вложенным
    return value


################################################################################
# Prompt engineering
################################################################################
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет RAI переменные шаблона в указанный словарь, если включены предупреждения RAI.
    Они могут быть настроены в файле config.ini. Если включены, переменные загрузят предупреждения RAI из
    соответствующих файлов в каталоге prompts. В противном случае переменные будут установлены в None.

    :param template_variables: Словарь переменных шаблона, к которому нужно добавить RAI переменные.
    :return: Обновленный словарь переменных шаблона.
    """
    from tinytroupe import config  # избегаем циклического импорта

    rai_harmful_content_prevention = config["Simulation"].getboolean(
        "RAI_HARMFUL_CONTENT_PREVENTION", True
    )
    rai_copyright_infringement_prevention = config["Simulation"].getboolean(
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION", True
    )

    # Загружаем содержимое файла для предотвращения вредоносного контента
    try:
        with open(os.path.join(os.path.dirname(__file__), "prompts/rai_harmful_content_prevention.md"), "r") as f:
            rai_harmful_content_prevention_content = f.read()
    except FileNotFoundError as e:
        logger.error(f"Не удалось найти файл rai_harmful_content_prevention.md: {e}")
        rai_harmful_content_prevention_content = None
    # Добавляем содержимое файла или None в зависимости от флага rai_harmful_content_prevention
    template_variables['rai_harmful_content_prevention'] = rai_harmful_content_prevention_content if rai_harmful_content_prevention else None


    # Загружаем содержимое файла для предотвращения нарушения авторских прав
    try:
        with open(os.path.join(os.path.dirname(__file__), "prompts/rai_copyright_infringement_prevention.md"), "r") as f:
            rai_copyright_infringement_prevention_content = f.read()
    except FileNotFoundError as e:
        logger.error(f"Не удалось найти файл rai_copyright_infringement_prevention.md: {e}")
        rai_copyright_infringement_prevention_content = None
    # Добавляем содержимое файла или None в зависимости от флага rai_copyright_infringement_prevention
    template_variables['rai_copyright_infringement_prevention'] = rai_copyright_infringement_prevention_content if rai_copyright_infringement_prevention else None

    return template_variables


################################################################################
# Rendering and markup
################################################################################
def inject_html_css_style_prefix(html, style_prefix_attributes):
    """
    Вставляет префикс стиля во все атрибуты стиля в заданной HTML-строке.

    :param html: HTML-строка для изменения.
    :param style_prefix_attributes: Префикс стиля, который нужно вставить.
    :return: HTML-строка с добавленным префиксом стиля.

    Пример:
       inject_html_css_style_prefix('<div style="color: red;">Hello</div>', 'font-size: 20px;')
    """
    return html.replace('style="', f'style="{style_prefix_attributes};')


def break_text_at_length(text: Union[str, dict], max_length: int = None) -> str:
    """
    Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)" в точке разрыва.
    Если максимальная длина равна `None`, содержимое возвращается как есть.

    :param text: Строка или словарь для разбиения.
    :param max_length: Максимальная длина текста.
    :return: Разбитый текст с добавлением "(...)".
    """
    if isinstance(text, dict):
        text = json.dumps(text, indent=4)

    if max_length is None or len(text) <= max_length:
        return text
    else:
        return text[:max_length] + " (...)"


def pretty_datetime(dt: datetime) -> str:
    """
    Возвращает строковое представление объекта datetime в формате "год-месяц-день час:минута".

    :param dt: Объект datetime.
    :return: Строковое представление даты и времени.
    """
    return dt.strftime("%Y-%m-%d %H:%M")


def dedent(text: str) -> str:
    """
    Удаляет отступы из текста, удаляя все начальные пробелы и отступы.

    :param text: Текст для удаления отступов.
    :return: Текст без отступов.
    """
    return textwrap.dedent(text).strip()


################################################################################
# IO and startup utilities
################################################################################
_CONFIG = None  # константа для хранения конфигурации


def read_config_file(use_cache=True, verbose=True) -> configparser.ConfigParser:
    """
    Читает конфигурационный файл. Сначала пытается найти файл `config.ini` в текущем рабочем каталоге,
    затем в директории модуля.

    :param use_cache: Использовать ли кэшированную конфигурацию, если она существует.
    :param verbose: Выводить ли отладочные сообщения.
    :return: Объект конфигурации ConfigParser.
    :raises ValueError: Если не удается найти конфигурационный файл.
    """
    global _CONFIG
    if use_cache and _CONFIG is not None:
        # возвращаем кэшированную конфигурацию, если она есть и это допустимо
        return _CONFIG

    else:
        config = configparser.ConfigParser()

        # Читаем значения по умолчанию из файла в каталоге модуля
        CONFIG_FILE_PATH = Path(__file__).parent.absolute() / 'config.ini' # константа для пути к файлу конфига
        if verbose:
            logger.debug(f"Ищем конфигурацию по умолчанию: {CONFIG_FILE_PATH}")
        if CONFIG_FILE_PATH.exists():
            config.read(CONFIG_FILE_PATH)
            _CONFIG = config
        else:
            raise ValueError(f"Не удалось найти конфигурацию по умолчанию: {CONFIG_FILE_PATH}")

        #  Переопределяем значения по умолчанию, если есть пользовательская конфигурация.
        # Ищем в текущем рабочем каталоге
        CONFIG_FILE_PATH = Path.cwd() / "config.ini"
        if CONFIG_FILE_PATH.exists():
            if verbose:
                logger.debug(f"Найдена пользовательская конфигурация: {CONFIG_FILE_PATH}")
            config.read(CONFIG_FILE_PATH)  # переопределяем значения, которые есть в пользовательской конфигурации
            _CONFIG = config
            return config
        else:
            if verbose:
                logger.debug(f"Не удалось найти пользовательскую конфигурацию: {CONFIG_FILE_PATH}")
                logger.info("Будут использоваться только значения по умолчанию. Если возникнут проблемы, попробуйте настроить модель, тип API и т.д.")

        return config

def pretty_print_config(config):
    """
    Выводит текущую конфигурацию TinyTroupe в консоль в удобном формате.

    :param config: Объект конфигурации ConfigParser.
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
    Запускает логгер с заданными настройками.

    :param config: Объект конфигурации ConfigParser.
    """
    # создаем логгер
    # logger = logging.getLogger("tinytroupe") #TODO: Уже импортирован выше
    log_level = config['Logging'].get('LOGLEVEL', 'INFO').upper()
    logger.setLevel(level=log_level)

    # создаем обработчик консоли и устанавливаем уровень на debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # создаем форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # добавляем форматтер к ch
    ch.setFormatter(formatter)

    # добавляем ch к логгеру
    logger.addHandler(ch)


class JsonSerializableRegistry:
    """
    Класс-миксин, предоставляющий JSON-сериализацию, десериализацию и регистрацию подклассов.
    """

    class_mapping = {}

    def to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict:
        """
        Возвращает JSON-представление объекта.

        :param include: Атрибуты для включения в сериализацию.
        :param suppress: Атрибуты для исключения из сериализации.
        :param file_path: Путь к файлу, куда будет записан JSON.
        :return: JSON-представление объекта.
        """
        # Собираем все сериализуемые атрибуты из иерархии классов
        serializable_attrs = set()
        suppress_attrs = set()
        for cls in self.__class__.__mro__:
            if hasattr(cls, 'serializable_attributes') and isinstance(cls.serializable_attributes, list):
                serializable_attrs.update(cls.serializable_attributes)
            if hasattr(cls, 'suppress_attributes_from_serialization') and isinstance(cls.suppress_attributes_from_serialization, list):
                suppress_attrs.update(cls.suppress_attributes_from_serialization)

        # Переопределяем атрибуты параметрами метода, если они предоставлены
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
            # Создаем каталоги, если они не существуют
            import os
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                json.dump(result, f, indent=4)

        return result

    @classmethod
    def from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None):
        """
        Загружает JSON-представление объекта и создает экземпляр класса.

        :param json_dict_or_path: JSON-словарь, представляющий объект, или путь к файлу для загрузки JSON.
        :param suppress: Атрибуты для исключения из загрузки.
        :param post_init_params: Параметры для передачи в метод `_post_deserialization_init`.
        :return: Экземпляр класса, заполненный данными из json_dict_or_path.
        """
        if isinstance(json_dict_or_path, str):
            with open(json_dict_or_path, 'r') as f:
                json_dict = json.load(f)
        else:
            json_dict = json_dict_or_path

        subclass_name = json_dict.get("json_serializable_class_name")
        target_class = cls.class_mapping.get(subclass_name, cls)
        instance = target_class.__new__(target_class)  # Создаем экземпляр без вызова __init__

        # Собираем все сериализуемые атрибуты из иерархии классов
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

        # Присваиваем значения только для сериализуемых атрибутов, если указаны, иначе присваиваем все
        for key in serializable_attrs if serializable_attrs else json_dict:
            if key in json_dict and key not in suppress_attrs:
                value = json_dict[key]
                if key in custom_serialization_initializers:
                    # Используем пользовательский инициализатор, если он предоставлен
                    setattr(instance, key, custom_serialization_initializers[key](value))
                elif isinstance(value, dict) and 'json_serializable_class_name' in value:
                    # Предполагаем, что это другой объект JsonSerializableRegistry
                    setattr(instance, key, JsonSerializableRegistry.from_json(value))
                elif isinstance(value, list):
                    # Обрабатываем коллекции, рекурсивно десериализуем, если элементы - объекты JsonSerializableRegistry
                    deserialized_collection = []
                    for item in value:
                        if isinstance(item, dict) and 'json_serializable_class_name' in item:
                            deserialized_collection.append(JsonSerializableRegistry.from_json(item))
                        else:
                            deserialized_collection.append(copy.deepcopy(item))
                    setattr(instance, key, deserialized_collection)
                else:
                    setattr(instance, key, copy.deepcopy(value))

        # Вызываем метод инициализации после десериализации, если он есть
        if hasattr(instance, '_post_deserialization_init') and callable(instance._post_deserialization_init):
            post_init_params = post_init_params if post_init_params else {}
            instance._post_deserialization_init(**post_init_params)

        return instance

    def __init_subclass__(cls, **kwargs):
        """
        Регистрирует подкласс и автоматически расширяет атрибуты сериализации и инициализаторы.
        """
        super().__init_subclass__(**kwargs)
        # Регистрируем подкласс, используя его имя в качестве ключа
        JsonSerializableRegistry.class_mapping[cls.__name__] = cls

        # Автоматически расширяем сериализуемые атрибуты и пользовательские инициализаторы из родительских классов
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
        Выполняет дополнительную инициализацию после десериализации.
        """
        # если есть метод _post_init, вызываем его после десериализации
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
    Возвращает имя указанного агента или среды или пустую строку, если агент равен None.

    :param named_entity: Агент или среда.
    :return: Имя агента или пустая строка.
    """
    if named_entity is None:
        return ""
    else:
        return named_entity.name


def custom_hash(obj):
    """
    Возвращает хеш для указанного объекта. Объект сначала преобразуется в строку,
    чтобы сделать его хешируемым. Этот метод является детерминированным, в отличие
    от встроенной функции hash().

    :param obj: Объект для хеширования.
    :return: Хеш объекта.
    """

    return hashlib.sha256(str(obj).encode()).hexdigest()


_fresh_id_counter = 0


def fresh_id():
    """
    Возвращает новый ID для нового объекта. Это полезно для создания уникальных ID для объектов.

    :return: Уникальный ID.
    """
    global _fresh_id_counter
    _fresh_id_counter += 1
    return _fresh_id_counter