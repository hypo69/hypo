# Модуль `tinytroupe.utils`

## Обзор

Этот модуль содержит общие утилиты и вспомогательные функции для проекта TinyTroupe, включая обработку входных данных LLM, извлечение данных из вывода модели, управление повторами на ошибках, валидацию полей, очистку строк и словарей, обработку шаблонов запросов, рендеринг HTML и текстов, а также управление вводом-выводом и начальной загрузкой конфигурации.

## Функции

### `compose_initial_LLM_messages_with_templates`

**Описание**: Создает начальные сообщения для вызова модели LLM, предполагая, что она всегда включает системное сообщение (общее описание задачи) и необязательное пользовательское сообщение (конкретное описание задачи). Сообщения создаются с использованием указанных шаблонов и настроек рендеринга.

**Параметры**:
- `system_template_name` (str): Имя шаблона для системного сообщения.
- `user_template_name` (Optional[str], optional): Имя шаблона для пользовательского сообщения. По умолчанию `None`.
- `rendering_configs` (dict, optional): Настройки для рендеринга шаблонов. По умолчанию `{}`.

**Возвращает**:
- `list`: Список словарей, представляющих сообщения для LLM. Каждый словарь имеет поля `role` (строка, "system" или "user") и `content` (строка, содержание сообщения).

### `extract_json`

**Описание**: Извлекает JSON-объект из строки, игнорируя текст перед первой открывающей фигурной скобкой и любые теги Markdown ````json````.

**Параметры**:
- `text` (str): Строка, содержащая JSON-объект.

**Возвращает**:
- `dict`: JSON-объект, извлеченный из строки. Возвращает пустой словарь `{}`, если JSON не найден или произошла ошибка.

**Вызывает исключения**:
- `Exception`: Любые ошибки при разборе JSON.

### `extract_code_block`

**Описание**: Извлекает блок кода из строки, игнорируя текст перед и после открывающих и закрывающих тройных обратных кавычек.

**Параметры**:
- `text` (str): Строка, содержащая блок кода.

**Возвращает**:
- `str`: Извлеченный блок кода. Возвращает пустую строку, если блок кода не найден или произошла ошибка.

**Вызывает исключения**:
- `Exception`: Любые ошибки при обработке текста.


### `repeat_on_error`

**Описание**: Декоратор, повторяющий указанный вызов функции, если возникает указанное исключение, до заданного числа попыток.

**Параметры**:
- `retries` (int): Максимальное число попыток.
- `exceptions` (list): Список типов исключений, которые следует перехватывать.

**Возвращает**:
- Функция: Декорированная функция.

**Вызывает исключения**:
- `Exception`: Заданное исключение, если после всех попыток оно не было обработано.


### `check_valid_fields`

**Описание**: Проверяет, являются ли поля в словаре допустимыми в соответствии со списком допустимых полей.

**Параметры**:
- `obj` (dict): Словарь, который нужно проверить.
- `valid_fields` (list): Список допустимых ключей.

**Возвращает**:
- None.

**Вызывает исключения**:
- `ValueError`: Если обнаружен недопустимый ключ.

### `sanitize_raw_string`

**Описание**: Очищает строку, удаляя недопустимые символы и гарантируя, что ее длина не превышает максимальную длину строки Python.

**Параметры**:
- `value` (str): Строка, которую нужно очистить.

**Возвращает**:
- str: Очищенная строка.

### `sanitize_dict`

**Описание**: Очищает словарь, удаляя недопустимые символы и гарантируя, что его вложенность не слишком глубокая.

**Параметры**:
- `value` (dict): Словарь, который нужно очистить.

**Возвращает**:
- dict: Очищенный словарь.

### `add_rai_template_variables_if_enabled`

**Описание**: Добавляет переменные шаблона RAI в указанный словарь, если флаги RAI включены в конфигурации.

**Параметры**:
- `template_variables` (dict): Словарь, в который нужно добавить переменные.

**Возвращает**:
- dict: Обновленный словарь переменных шаблонов.


### `inject_html_css_style_prefix`

**Описание**: Вставляет префикс в атрибуты style в строке HTML.

**Параметры**:
- `html` (str): Строка HTML.
- `style_prefix_attributes` (str): Префикс для атрибутов style.

**Возвращает**:
- str: Строка HTML со вставленным префиксом.

### `break_text_at_length`

**Описание**: Разбивает текст (или JSON) на заданную длину, вставляя "(...)" в точке разрыва.

**Параметры**:
- `text` (Union[str, dict]): Текст или JSON.
- `max_length` (int, optional): Максимальная длина. По умолчанию `None`.

**Возвращает**:
- str: Текст с возможным разрывом.

### `pretty_datetime`

**Описание**: Возвращает красивое строковое представление объекта datetime.

**Параметры**:
- `dt` (datetime): Объект datetime.

**Возвращает**:
- str: Строковое представление объекта datetime.

### `dedent`

**Описание**: Удаляет отступы из строки.

**Параметры**:
- `text` (str): Строка с отступами.

**Возвращает**:
- str: Строка без отступов.


### `read_config_file`

**Описание**: Читает файл конфигурации `config.ini`.  Ищет сначала в каталоге модуля, затем в текущем каталоге.

**Параметры**:
- `use_cache` (bool): Использовать кэш конфигурации. По умолчанию True.
- `verbose` (bool): Выводить сообщения об искомых файлах. По умолчанию True.

**Возвращает**:
- `configparser.ConfigParser`: Объект конфигурации.

**Вызывает исключения**:
- `ValueError`: Если файл конфигурации не найден.

### `pretty_print_config`

**Описание**: Красиво выводит содержимое объекта конфигурации.

**Параметры**:
- `config`: Объект конфигурации.


### `start_logger`

**Описание**: Настраивает и инициализирует логгер.

**Параметры**:
- `config`: Объект конфигурации.

### `JsonSerializableRegistry`

**Описание**: Класс-миксин для сериализации/десериализации объектов в JSON.

**Методы**:
- `to_json`: Сериализует объект в JSON.
- `from_json`: Десериализует объект из JSON.
- `__init_subclass__`: Регистрирует подклассы в словаре отображений.
- `_post_deserialization_init`: Вызывает метод `_post_init` после десериализации, если он существует.

### `post_init`

**Описание**: Декоратор для автоматического вызова метода `_post_init` после инициализации класса.


### `name_or_empty`

**Описание**: Возвращает имя сущности, или пустую строку, если сущность равна None.

**Параметры**:
- `named_entity`: Объект, содержащий имя.


### `custom_hash`

**Описание**: Возвращает детерминированный хеш для объекта.

**Параметры**:
- `obj`: Объект, для которого нужно посчитать хеш.


### `fresh_id`

**Описание**: Возвращает новое уникальное целое число.