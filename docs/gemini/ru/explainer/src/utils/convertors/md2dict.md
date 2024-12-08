# <input code>

```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors.md2dict 
	:platform: Windows, Unix
	:synopsis: Модуль для конвертации строки Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.
"""
MODE = 'dev'
import re
from typing import Dict
from markdown2 import markdown
from src.logger import logger

def md2dict(md_string: str) -> Dict[str, dict | list]:
    """
    Конвертирует строку Markdown в структурированный словарь с извлечением JSON содержимого, если оно присутствует.

    Args:
        md_string (str): Строка Markdown для конвертации.

    Returns:
        Dict[str, dict | list]: Структурированное представление Markdown содержимого.
        Возвращает словарь с ключом "json", если найден JSON контент, или словарь с секциями Markdown.
    """
    try:
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        html = markdown(md_string)
        sections: Dict[str, list] = {}
        current_section: str | None = None

        for line in html.splitlines():
            if line.startswith('<h'):
                heading_level_match = re.search(r'h(\d)', line)
                if heading_level_match:
                    heading_level = int(heading_level_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip()

                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    elif current_section:
                        sections[current_section].append(section_title)
            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip()
                sections[current_section].append(clean_text)

        return sections

    except Exception as ex:
        logger.error("Ошибка при парсинге Markdown в структурированный словарь.", exc_info=True)
        return {}


def extract_json_from_string(text: str) -> dict | None:
    """
    Извлекает JSON контент из строки, если он присутствует.

    Args:
        text (str): Строка для извлечения JSON контента.

    Returns:
        dict | None: Извлеченный JSON контент или `None`, если JSON не найден.
    """
    try:
        json_pattern = r'{.*}'
        json_match = re.search(json_pattern, text, re.DOTALL)
        if json_match:
            return eval(json_match.group())  # Используем eval для упрощения примера
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```

# <algorithm>

**Шаг 1:** Функция `md2dict` принимает строку Markdown (`md_string`).

**Пример:** `md_string = "# Заголовок 1\nТекст 1"`

**Шаг 2:** Функция `extract_json_from_string` ищет JSON в `md_string` используя регулярное выражение.

**Пример:** `json_content = {"key": "value"}`

**Шаг 3:** Если JSON найден, возвращается словарь `{"json": json_content}`.

**Пример:** `{"json": {"key": "value"}}`

**Шаг 4:** Если JSON не найден, выполняется парсинг Markdown с помощью `markdown`.

**Шаг 5:** Создание пустого словаря `sections` для хранения секций.

**Шаг 6:** Перебор строк HTML, полученных из Markdown.

**Пример:** (строка html) `<h1>Заголовок 1</h1><p>Текст 1</p>`

**Шаг 7:** Если строка начинается с `<h`, извлекается уровень заголовка и текст заголовка.

**Пример:** (`heading_level` = 1, `section_title` = "Заголовок 1")

**Шаг 8:** Если уровень заголовка равен 1, создается новая секция в словаре `sections` с именем заголовка.

**Пример:** `sections["Заголовок 1"] = []`

**Шаг 9:** Если текущая секция существует, добавляется заголовок в список секции.

**Пример:** `sections["Заголовок 1"].append("Заголовок 2")`

**Шаг 10:** Если строка не заголовок, но текущая секция существует, добавляется текст в список секции.

**Пример:** `sections["Заголовок 1"].append("Текст 1")`

**Шаг 11:** Возвращается словарь `sections`.

**Пример:** `{"Заголовок 1": ["Заголовок 2", "Текст 1"]} `


# <mermaid>

```mermaid
graph TD
    A[md2dict(md_string)] --> B{JSON в строке?};
    B -- Да --> C[extract_json_from_string];
    C --> D[Возврат {"json": json_content}];
    B -- Нет --> E[markdown(md_string)];
    E --> F[sections = {}];
    F --> G(Проход по строкам HTML);
    G --> H{Заголовок?};
    H -- Да --> I[Извлечение уровня и текста];
    I --> J{Уровень = 1?};
    J -- Да --> K[sections[заголовок] = []];
    J -- Нет --> L[sections[текущая секция].append(заголовок)];
    H -- Нет --> M{Текущая секция есть?};
    M -- Да --> N[sections[текущая секция].append(очищенный текст)];
    M -- Нет --> O[];
    G --> P[Возврат sections];
    D -.-> Q(Возврат);
    P -.-> Q(Возврат);
    
```

**Описание зависимостей:**

* `markdown`: Библиотека для парсинга Markdown.  Зависимость от внешней библиотеки `markdown2`.
* `logger`: Логирование ошибок. Зависимость от созданного модуля `src.logger`.
* `re`: Регулярные выражения, для поиска JSON.
* `typing`: Для типов данных.
* `str`, `dict`, `list` и т.д.: Стандартные типы данных Python.


# <explanation>

**Импорты:**

* `markdown2`: Библиотека для преобразования Markdown в HTML. Импортируется из `markdown2`.
* `logger`: Предполагается, что это собственный модуль, используемый для логирования, импортируется из `src.logger`.  Это указывает на структурированную архитектуру проекта, где логирование отделено от основного кода.

**Классы:**

Нет классов в данном коде.

**Функции:**

* `md2dict(md_string)`: Преобразует строку Markdown в словарь, содержащий секции или JSON.
    * Аргументы: `md_string` (строка Markdown).
    * Возвращаемое значение: словарь, содержащий либо JSON, либо секции Markdown.
    * Логика: Извлекает JSON, если он есть, в противном случае преобразует Markdown в HTML и извлекает заголовки и текст в словарь секций.  Обработка ошибок (try-except) предотвращает аварийный выход.
* `extract_json_from_string(text)`: Извлекает JSON из строки.
    * Аргументы: `text` (строка).
    * Возвращаемое значение: JSON в виде словаря или `None`, если JSON не найден.
    * Логика: Использует регулярное выражение для поиска JSON в строке.  `eval` используется для парсинга найденного JSON.  Обработка ошибок (try-except) предотвращает аварийный выход и обрабатывает исключения.

**Переменные:**

* `MODE`, `json_content`, `html`, `sections`, `current_section`, `heading_level`, `section_title`, `clean_text`:  Обычные переменные, используемые для хранения значений в процессе работы кода.

**Возможные ошибки и улучшения:**

* **`eval`:** Использование `eval` для парсинга JSON небезопасно, если входная строка не контролируется.  Вместо `eval` лучше использовать `json.loads`.
* **Более точное извлечение JSON:**  В `extract_json_from_string` регулярное выражение может быть усовершенствовано, чтобы извлекать только корректный JSON, а не любой текст в фигурных скобках.
* **Обработка ошибок:** Обработка ошибок в `md2dict` и `extract_json_from_string` может быть улучшена с использованием более специфичных обработчиков исключений.
* **Переменные типов:**  Использование типов данных с помощью `typing.Dict`, `typing.List` делает код более читаемым и наглядным, повышая его надежность.

**Взаимосвязи с другими частями проекта:**

Функция использует `src.logger` для вывода сообщений об ошибках, что предполагает существование модуля логирования в проекте.  Модуль `md2dict` является частью модуля `utils`, предполагая, что проект имеет структуру пакета.  Он конвертирует Markdown в структурированный формат, который, вероятно, используется другими частями приложения.