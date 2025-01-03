# tinytroupe.utils

## Обзор

Модуль `tinytroupe.utils` содержит общие утилиты и вспомогательные функции, используемые в проекте TinyTroupe. Он включает функции для обработки ввода и вывода модели, управления моделями, валидации, обработки строк, рендеринга, ввода-вывода, сериализации JSON, а также другие вспомогательные функции.

## Оглавление

- [Функции](#Функции)
  - [`compose_initial_LLM_messages_with_templates`](#compose_initial_llm_messages_with_templates)
  - [`extract_json`](#extract_json)
  - [`extract_code_block`](#extract_code_block)
  - [`repeat_on_error`](#repeat_on_error)
  - [`check_valid_fields`](#check_valid_fields)
  - [`sanitize_raw_string`](#sanitize_raw_string)
  - [`sanitize_dict`](#sanitize_dict)
  - [`add_rai_template_variables_if_enabled`](#add_rai_template_variables_if_enabled)
  - [`inject_html_css_style_prefix`](#inject_html_css_style_prefix)
  - [`break_text_at_length`](#break_text_at_length)
  - [`pretty_datetime`](#pretty_datetime)
  - [`dedent`](#dedent)
  - [`read_config_file`](#read_config_file)
  - [`pretty_print_config`](#pretty_print_config)
  - [`start_logger`](#start_logger)
  - [`name_or_empty`](#name_or_empty)
  - [`custom_hash`](#custom_hash)
  - [`fresh_id`](#fresh_id)
- [Классы](#Классы)
    - [`JsonSerializableRegistry`](#jsonserializableregistry)

## Функции

### `compose_initial_LLM_messages_with_templates`

**Описание**:
Составляет начальные сообщения для вызова языковой модели, предполагая, что всегда есть системное сообщение (общее описание задачи) и необязательное сообщение пользователя (конкретное описание задачи). Эти сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

**Параметры**:
- `system_template_name` (str): Имя файла шаблона системного сообщения.
- `user_template_name` (str, optional): Имя файла шаблона пользовательского сообщения. По умолчанию `None`.
- `rendering_configs` (dict, optional): Словарь с конфигурациями для рендеринга шаблонов. По умолчанию `{}`.

**Возвращает**:
- `list`: Список словарей, представляющих сообщения для языковой модели.

### `extract_json`

**Описание**:
Извлекает объект JSON из строки, игнорируя любой текст до первой открывающей фигурной скобки и любые открывающие или закрывающие теги Markdown (```json, ```).

**Параметры**:
- `text` (str): Строка, из которой нужно извлечь JSON.

**Возвращает**:
- `dict`: Словарь, представляющий извлеченный JSON объект. Возвращает пустой словарь (`{}`), если извлечение не удалось.

### `extract_code_block`

**Описание**:
Извлекает блок кода из строки, игнорируя любой текст до первого открывающего тройного обратного апострофа и любой текст после закрывающего тройного обратного апострофа.

**Параметры**:
- `text` (str): Строка, из которой нужно извлечь блок кода.

**Возвращает**:
- `str`: Строка, представляющая извлеченный блок кода. Возвращает пустую строку (`""`), если извлечение не удалось.

### `repeat_on_error`

**Описание**:
Декоратор, который повторяет вызов указанной функции, если возникает исключение из списка указанных исключений, до указанного количества повторных попыток. Если это количество попыток превышено, исключение вызывается. Если исключения не происходит, функция возвращается нормально.

**Параметры**:
- `retries` (int): Количество повторных попыток.
- `exceptions` (list): Список классов исключений, которые нужно перехватывать.

**Возвращает**:
- `function`: Декорированная функция.

### `check_valid_fields`

**Описание**:
Проверяет, являются ли поля в указанном словаре допустимыми, в соответствии со списком допустимых полей. Если нет, вызывает ValueError.

**Параметры**:
- `obj` (dict): Словарь, поля которого нужно проверить.
- `valid_fields` (list): Список допустимых полей.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если в словаре есть недопустимые ключи.

### `sanitize_raw_string`

**Описание**:
Очищает указанную строку, удаляя любые недопустимые символы и гарантируя, что ее длина не превышает максимальную длину строки Python.

**Параметры**:
- `value` (str): Строка, которую нужно очистить.

**Возвращает**:
- `str`: Очищенная строка.

### `sanitize_dict`

**Описание**:
Очищает указанный словарь, удаляя любые недопустимые символы и гарантируя, что словарь не является слишком глубоко вложенным.

**Параметры**:
- `value` (dict): Словарь, который нужно очистить.

**Возвращает**:
- `dict`: Очищенный словарь.

### `add_rai_template_variables_if_enabled`

**Описание**:
Добавляет переменные шаблона RAI к указанному словарю, если включены отказ от ответственности RAI. Эти переменные могут быть настроены в файле `config.ini`. Если они включены, переменные будут загружать отказ от ответственности RAI из соответствующих файлов в каталоге `prompts`. В противном случае переменные будут установлены в `None`.

**Параметры**:
- `template_variables` (dict): Словарь переменных шаблона, к которому нужно добавить переменные RAI.

**Возвращает**:
- `dict`: Обновленный словарь переменных шаблона.

### `inject_html_css_style_prefix`

**Описание**:
Вставляет префикс стиля ко всем атрибутам стиля в заданной HTML-строке.

**Параметры**:
- `html` (str): HTML-строка.
- `style_prefix_attributes` (str): Строка префикса стиля.

**Возвращает**:
- `str`: HTML-строка с добавленными префиксами стиля.

### `break_text_at_length`

**Описание**:
Разбивает текст (или JSON) на указанной длине, вставляя строку "(...)" в точке разрыва. Если максимальная длина равна `None`, содержимое возвращается как есть.

**Параметры**:
- `text` (str | dict): Текст или JSON для разбиения.
- `max_length` (int, optional): Максимальная длина текста. По умолчанию `None`.

**Возвращает**:
- `str`: Разбитый текст.

### `pretty_datetime`

**Описание**:
Возвращает строковое представление указанного объекта `datetime` в формате "YYYY-MM-DD HH:MM".

**Параметры**:
- `dt` (datetime): Объект `datetime`.

**Возвращает**:
- `str`: Строковое представление даты и времени.

### `dedent`

**Описание**:
Удаляет отступы из указанного текста, удаляя любые начальные пробелы и отступы.

**Параметры**:
- `text` (str): Текст, из которого нужно удалить отступы.

**Возвращает**:
- `str`: Текст без отступов.

### `read_config_file`

**Описание**:
Считывает файл конфигурации `config.ini` из текущего каталога или каталога модуля.

**Параметры**:
- `use_cache` (bool, optional): Использовать ли кэшированную конфигурацию. По умолчанию `True`.
- `verbose` (bool, optional): Выводить ли отладочную информацию. По умолчанию `True`.

**Возвращает**:
- `configparser.ConfigParser`: Объект конфигурации.

**Вызывает исключения**:
- `ValueError`: Если не удалось найти файл конфигурации по умолчанию.

### `pretty_print_config`

**Описание**:
Выводит текущую конфигурацию TinyTroupe в консоль.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации.

**Возвращает**:
- `None`

### `start_logger`

**Описание**:
Инициализирует и запускает логгер TinyTroupe.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации.

**Возвращает**:
- `None`

### `name_or_empty`

**Описание**:
Возвращает имя указанного агента или среды, или пустую строку, если агент равен `None`.

**Параметры**:
- `named_entity` (AgentOrWorld): Агент или среда, имя которого нужно получить.

**Возвращает**:
- `str`: Имя агента или среды, или пустая строка.

### `custom_hash`

**Описание**:
Возвращает хэш для указанного объекта. Объект сначала преобразуется в строку, чтобы сделать его хэшируемым. Этот метод является детерминированным, в отличие от встроенной функции `hash()`.

**Параметры**:
- `obj` (Any): Объект, для которого нужно получить хэш.

**Возвращает**:
- `str`: Хэш объекта.

### `fresh_id`

**Описание**:
Возвращает новый уникальный ID для нового объекта.

**Параметры**:
- `None`

**Возвращает**:
- `int`: Уникальный ID.

## Классы

### `JsonSerializableRegistry`

**Описание**:
Миксин, который обеспечивает сериализацию, десериализацию и регистрацию подклассов в формате JSON.

**Методы**:
- `to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict`:
  - **Описание**: Возвращает JSON-представление объекта.
  - **Параметры**:
      - `include` (list, optional): Атрибуты, которые нужно включить в сериализацию.
      - `suppress` (list, optional): Атрибуты, которые нужно исключить из сериализации.
      - `file_path` (str, optional): Путь к файлу, куда будет записан JSON.
  - **Возвращает**:
      - `dict`: JSON-представление объекта.
- `from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None)`:
  - **Описание**: Загружает JSON-представление объекта и создает экземпляр класса.
  - **Параметры**:
      - `json_dict_or_path` (dict или str): JSON-словарь, представляющий объект, или путь к файлу, из которого нужно загрузить JSON.
      - `suppress` (list, optional): Атрибуты, которые нужно исключить при загрузке.
      - `post_init_params` (dict, optional): Дополнительные параметры для вызова `_post_deserialization_init`.
  - **Возвращает**:
      - `An instance of the class populated with the data from json_dict_or_path`: Экземпляр класса, заполненный данными из `json_dict_or_path`.
- `__init_subclass__(cls, **kwargs)`:
  - **Описание**: Регистрирует подкласс и автоматически расширяет сериализуемые атрибуты и пользовательские инициализаторы из родительских классов.
- `_post_deserialization_init(self, **kwargs)`:
    - **Описание**:  Вызывает метод `_post_init`, если он присутствует в классе, после десериализации.

**Статические атрибуты**:
- `class_mapping` (dict): Словарь, хранящий соответствия между именами классов и самими классами.