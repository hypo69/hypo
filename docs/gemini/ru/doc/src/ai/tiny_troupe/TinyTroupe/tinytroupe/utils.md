# Модуль `tinytroupe.utils`

## Обзор

Этот модуль содержит общие утилиты и вспомогательные функции, используемые в проекте TinyTroupe. Включает в себя функции для обработки входных и выходных данных моделей, управления моделями, проверки данных, обработки строк и JSON, а также для генерации уникальных идентификаторов.

## Оглавление

* [Функции](#функции)
    * [`compose_initial_LLM_messages_with_templates`](#compose_initial_llm_messages_with_templates)
    * [`extract_json`](#extract_json)
    * [`extract_code_block`](#extract_code_block)
    * [`repeat_on_error`](#repeat_on_error)
    * [`check_valid_fields`](#check_valid_fields)
    * [`sanitize_raw_string`](#sanitize_raw_string)
    * [`sanitize_dict`](#sanitize_dict)
    * [`add_rai_template_variables_if_enabled`](#add_rai_template_variables_if_enabled)
    * [`inject_html_css_style_prefix`](#inject_html_css_style_prefix)
    * [`break_text_at_length`](#break_text_at_length)
    * [`pretty_datetime`](#pretty_datetime)
    * [`dedent`](#dedent)
    * [`read_config_file`](#read_config_file)
    * [`pretty_print_config`](#pretty_print_config)
    * [`start_logger`](#start_logger)
* [Класс `JsonSerializableRegistry`](#класс-jsonserializableregistry)
    * [`to_json`](#to_json)
    * [`from_json`](#from_json)
    * [`__init_subclass__`](#__init_subclass__)
    * [`_post_deserialization_init`](#_post_deserialization_init)
* [Декоратор `post_init`](#декоратор-post_init)
* [`name_or_empty`](#name_or_empty)
* [`custom_hash`](#custom_hash)
* [`fresh_id`](#fresh_id)


## Функции

### `compose_initial_LLM_messages_with_templates`

**Описание**: Создает начальные сообщения для вызова модели LLM, предполагая, что она всегда включает системное сообщение (общее описание задачи) и необязательное пользовательское сообщение (конкретное описание задачи). Эти сообщения создаются с использованием указанных шаблонов и настроек рендеринга.

**Параметры**:
* `system_template_name` (str): Имя шаблона для системного сообщения.
* `user_template_name` (Optional[str], optional): Имя шаблона для пользовательского сообщения. По умолчанию `None`.
* `rendering_configs` (dict, optional): Словарь с конфигурациями рендеринга. По умолчанию `{}`.

**Возвращает**:
* list: Список словарей, представляющих сообщения для модели LLM.


### `extract_json`

**Описание**: Извлекает JSON-объект из строки, игнорируя текст перед первой открывающей фигурной скобкой и любые теги Markdown (````json````).

**Параметры**:
* `text` (str): Строка, содержащая JSON-объект.

**Возвращает**:
* dict: Словарь, представляющий извлеченный JSON-объект. Возвращает пустой словарь, если JSON не найден или произошла ошибка.


### `extract_code_block`

**Описание**: Извлекает блок кода из строки, игнорируя текст перед и после тройных обратных кавычек.

**Параметры**:
* `text` (str): Строка, содержащая код.

**Возвращает**:
* str: Строка, содержащая извлеченный код. Возвращает пустую строку, если код не найден или произошла ошибка.



### ... (и другие функции)


## Класс `JsonSerializableRegistry`

### `to_json`

**Описание**: Возвращает JSON-представление объекта.

**Параметры**:
* `include` (list, optional): Список атрибутов, которые нужно включить в сериализацию.
* `suppress` (list, optional): Список атрибутов, которые нужно исключить из сериализации.
* `file_path` (str, optional): Путь к файлу, куда будет записан JSON.

**Возвращает**:
* dict: JSON-представление объекта.

### `from_json`

**Описание**: Загружает JSON-представление объекта и создает экземпляр класса.

**Параметры**:
* `json_dict_or_path` (dict или str): JSON-словарь, представляющий объект, или путь к файлу для загрузки JSON.
* `suppress` (list, optional): Список атрибутов, которые нужно исключить при загрузке.
* `post_init_params` (dict, optional): Параметры для вызова метода `_post_deserialization_init`.


**Возвращает**:
* Экземпляр класса, заполненный данными из `json_dict_or_path`.


### ... (и другие методы класса)

### ... (и другие разделы)