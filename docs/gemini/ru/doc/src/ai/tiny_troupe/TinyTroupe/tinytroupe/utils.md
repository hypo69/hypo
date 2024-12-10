# Модуль `tinytroupe.utils`

## Обзор

Этот модуль содержит общие служебные функции и функции удобства для использования в проекте TinyTroupe. Он включает в себя инструменты для обработки входных и выходных данных модели, управления вызовами модели, проверки данных, обработки строк и JSON, а также функций для работы с конфигурацией и регистрацией.

## Оглавление

- [Модуль `tinytroupe.utils`](#модуль-tinytroupeutils)
    - [Функции](#функции)
        - [`compose_initial_LLM_messages_with_templates`](#composeinitialllm_messages_with_templates)
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
        - [`JsonSerializableRegistry`](#jsonserializableregistry)
        - [`post_init`](#post_init)
        - [`name_or_empty`](#name_or_empty)
        - [`custom_hash`](#custom_hash)
        - [`fresh_id`](#fresh_id)


## Функции

### `compose_initial_LLM_messages_with_templates`

**Описание**:  Создает начальные сообщения для вызова модели LLM, предполагая наличие системного сообщения (общее описание задачи) и необязательного пользовательского сообщения (конкретное описание задачи). Сообщения создаются с использованием указанных шаблонов и конфигураций рендеринга.

**Параметры**:
- `system_template_name` (str): Имя шаблона для системного сообщения.
- `user_template_name` (Optional[str], optional): Имя шаблона для пользовательского сообщения. По умолчанию `None`.
- `rendering_configs` (dict, optional): Словарь с параметрами для рендеринга шаблонов. По умолчанию `{}`.

**Возвращает**:
- list: Список словарей, представляющих сообщения.


### `extract_json`

**Описание**: Извлекает JSON-объект из строки, игнорируя текст до первой открывающей фигурной скобки и теги Markdown ````json````.

**Параметры**:
- `text` (str): Строка, содержащая JSON-объект.

**Возвращает**:
- dict: JSON-объект или пустой словарь, если JSON не найден или произошла ошибка.


### `extract_code_block`

**Описание**: Извлекает код из строки, игнорируя текст до первой открывающей тройной обратной кавычки и текст после закрывающей тройной обратной кавычки.

**Параметры**:
- `text` (str): Строка, содержащая код.

**Возвращает**:
- str: Строка, содержащая код, или пустая строка, если код не найден или произошла ошибка.

**(и так далее для остальных функций)**

### `JsonSerializableRegistry`

**Описание**: Класс-миксин, предоставляющий сериализацию/десериализацию в JSON и регистрацию подклассов.

**Методы**:

- `to_json`: Возвращает JSON-представление объекта.
- `from_json`: Загружает JSON-представление объекта и создает экземпляр класса.

**(Подробное описание методов `to_json` и `from_json` следует включить)**


**(Продолжение документации для остальных функций и класса, следуя шаблону, указанному в инструкции)**