```MD
# <input code>

```python
"""
General utilities and convenience functions.
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
AgentOrWorld = Union["TinyPerson", "TinyWorld"]

# logger
logger = logging.getLogger("tinytroupe")


################################################################################
# Model input utilities
################################################################################
def compose_initial_LLM_messages_with_templates(system_template_name:str, user_template_name:str=None, rendering_configs:dict={}) -> list:
    """
    Composes the initial messages for the LLM model call, under the assumption that it always involves 
    a system (overall task description) and an optional user message (specific task description). 
    These messages are composed using the specified templates and rendering configurations.
    """

    system_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{system_template_name}')
    user_prompt_template_path = os.path.join(os.path.dirname(__file__), f'prompts/{user_template_name}')

    messages = []

    messages.append({"role": "system", 
                         "content": chevron.render(
                             open(system_prompt_template_path).read(), 
                             rendering_configs)})\n    
    # optionally add a user message
    if user_template_name is not None:\n        messages.append({"role": "user", 
                            "content": chevron.render(
                                    open(user_prompt_template_path).read(), 
                                    rendering_configs)})\n    return messages
```
```
# <algorithm>

**Шаг 1:** Функция `compose_initial_LLM_messages_with_templates` принимает имя шаблона для системного сообщения, имя шаблона для пользовательского сообщения (необязательно) и словарь конфигурации для рендеринга.

**Шаг 2:** Строятся пути к файлам шаблонов.


**Шаг 3:** Создается пустой список сообщений.


**Шаг 4:**  Шаблон системного сообщения считывается и рендерится с использованием библиотеки `chevron` и переданных конфигураций. Результат добавляется в список сообщений.


**Шаг 5:**  Если задано имя шаблона для пользовательского сообщения, то аналогично происходит чтение и рендеринг шаблона пользовательского сообщения, и результат добавляется в список сообщений.


**Шаг 6:** Возвращается список сообщений.

**Пример:**

Если `system_template_name` = 'my_system_prompt',  `rendering_configs` = `{'task': 'summarize'}`, то будет считан файл `prompts/my_system_prompt` и в нем будут заменены `{{task}}` на `summarize`.


**Передача данных:**  Данные (имена шаблонов, конфигурация) передаются в функцию. Функция возвращает сформированный список сообщений.

# <mermaid>

```mermaid
graph TD
    A[compose_initial_LLM_messages_with_templates] --> B{system_template_name, user_template_name, rendering_configs};
    B --> C[Строится path to system prompt];
    B --> D[Строится path to user prompt];
    C --> E[Чтение system prompt];
    D --> F[Чтение user prompt (опционально)];
    E --> G[chevron.render];
    G --> H[{"role": "system", "content": ...}];
    H --> I[messages.append];
    F --> K[chevron.render];
    K --> L[{"role": "user", "content": ...}];
    L --> I;
    I --> M[return messages];
```

**Объяснение диаграммы:**

* `compose_initial_LLM_messages_with_templates` - функция, принимающая на вход параметры для генерации сообщений.
* `system_template_name`, `user_template_name`, `rendering_configs` - параметры, передаваемые в функцию.
* Функция строить пути к файлам с шаблонами.
* Функция считывает шаблоны и рендерит их с помощью `chevron.render`.
* Функция добавляет результаты в список `messages`.
* Функция возвращает список `messages`.


# <explanation>

**Импорты:**

* `re`, `json`, `os`, `sys`, `hashlib`, `textwrap`, `logging`, `chevron`, `copy`, `typing`, `datetime`, `pathlib`, `configparser`: Стандартные библиотеки Python, используемые для различных задач, таких как регулярные выражения, работа с файлами, обработка логов, форматирование строк, работа с временными метками и т. д.
* `Union`, `Any`, `TypeVar`: Из модуля `typing`, используются для указания типов.
* `Collection`: Из модуля `typing`,  используется для обозначения типов, которые представляют коллекции (списки, кортежи и др.).

**Связь с пакетами `src.`: **

Данные импорты не связаны напрямую с другими пакетами `src.`. Это базовые библиотеки Python.

**Классы:**

* `JsonSerializableRegistry`: Класс, обеспечивающий сериализацию и десериализацию объектов в JSON-формат.  Он имеет методы `to_json` для сериализации и `from_json` для десериализации.  Класс использует `class_mapping` для регистрации подклассов. Важно, что он также имеет механизм для рекурсивной сериализации/десериализации вложенных объектов.  Важным аспектом работы этого класса является рекурсивное обращение к подклассам и обработка списков и словарей, что позволяет обрабатывать сложные объекты.  

**Функции:**

* `compose_initial_LLM_messages_with_templates`: Формирует начальные сообщения для модели LLM, используя шаблоны и конфигурацию.
* `extract_json`: Извлекает JSON-объект из строки, игнорируя текст до первой фигурной скобки и маркеров ````json````.  Функция использует регулярные выражения для очистки входящего текста от ненужных частей, прежде чем обработать JSON.  Это защищает от потенциальных ошибок парсинга.
* `extract_code_block`:  Извлекает блок кода из строки, игнорируя текст до и после тройных обратных кавычек `````.
* `repeat_on_error`: Декоратор, который повторяет вызов функции до определенного количества попыток, если происходит указанное исключение.  Это позволяет обрабатывать потенциальные ошибки при работе с внешними ресурсами.
* `check_valid_fields`: Проверяет, что все ключи в словаре соответствуют списку допустимых ключей.
* `sanitize_raw_string`: Санітує рядок, видаляючи некоректні символи та перевіряючи максимальну довжину рядка.  Ця функція важлива для запобігання проблемам безпеки, пов’язаним із великими або некоректними рядками.
* `sanitize_dict`: Санітує словник, видаляючи некоректні символи і перевіряючи глибину вкладеності.
* `add_rai_template_variables_if_enabled`: Додає змінні шаблонів RAI до заданого словника, якщо включені застереження RAI.
* `inject_html_css_style_prefix`, `break_text_at_length`, `pretty_datetime`, `dedent`:  Функції для форматирования, обработки и рендеринга текста.
* `read_config_file`, `pretty_print_config`, `start_logger`:  Функции для работы с конфигурацией и инициализации логгера.
* `name_or_empty`: Возвращает имя агента или пустую строку, если агент равен None.
* `custom_hash`, `fresh_id`:  Функции для генерации уникальных идентификаторов.

**Переменные:**

* `logger`: Объект логгера, используемый для записи сообщений в лог.
* `_config`: Кэширует конфигурацию.

**Возможные ошибки/улучшения:**

* Необходимо убедиться, что все файлы шаблонов (`prompts/{system_template_name}`, `prompts/{user_template_name}`) существуют, иначе произойдёт исключение `FileNotFoundError`.
* Добавьте обработку ситуации, когда JSON-строка содержит синтаксические ошибки JSON.
* В функциях `extract_json` и `extract_code_block` можно улучшить обработку ошибок, чтобы возвращать более информативные сообщения об ошибках.
* В `JsonSerializableRegistry` можно добавить методы для проверки корректности входных JSON данных.
* В `read_config_file` обработка отсутствия `config.ini` может быть сделана более гибкой, например, возвращая специальное значение или используя значение по умолчанию.


**Цепочка взаимосвязей:**

Код в `utils.py` используется другими частями проекта, особенно в отношении работы с сообщениями для LLM, обработкой данных из внешних источников и настройкой приложения.  Он связан с другими компонентами проекта через вызовы функций и переменные, и его использование предполагает существование других классов (например, `TinyPerson`, `TinyWorld`), а также конфигураций, которые используются для работы с моделью.