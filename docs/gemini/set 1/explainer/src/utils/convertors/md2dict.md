# <input code>

```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors.md2dict 
	:platform: Windows, Unix
	:synopsis: Модуль для конвертации строки Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.
"""

import re
from typing import Dict
from markdown2 import markdown
from src.logger.logger import logger

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
        # Извлечение JSON из строки Markdown, если присутствует
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        # Если JSON не найден, обрабатываем Markdown
        html = markdown(md_string)
        sections: Dict[str, list] = {}
        current_section: str | None = None

        # Парсим HTML строку, полученную из Markdown
        for line in html.splitlines():
            # Обработка заголовков секций
            if line.startswith('<h'):
                heading_level_match = re.search(r'h(\d)', line)
                if heading_level_match:
                    heading_level = int(heading_level_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip()

                    # Создаем новую секцию для заголовков уровня 1
                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    # Добавляем заголовки уровней выше 1 в текущую секцию
                    elif current_section:
                        sections[current_section].append(section_title)

            # Добавляем текст в текущую секцию
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

**Алгоритм:**

1. **Вход:** Строка Markdown (`md_string`).
2. **Извлечение JSON:** Поиск JSON блока в строке (`extract_json_from_string`).
   - Если JSON найден, возвращается словарь с ключом `json` и найденным JSON.
3. **Обработка Markdown:**
   - Преобразование Markdown в HTML (`markdown`).
   - Инициализация пустого словаря `sections` для хранения секций.
   - Переменная `current_section` для хранения текущей секции (начальная секция `None`).
   - Проход по строкам HTML:
     - Если строка начинается с `<h...>`:
       - Извлечение уровня заголовка.
       - Извлечение текста заголовка.
       - Если уровень 1, создаем новую секцию в `sections`.
       - Если уровень > 1 и текущая секция существует, добавляем заголовок в текущую секцию.
     - Если строка не пустая и текущая секция существует, очищаем HTML-теги и добавляем очищенный текст в текущую секцию.
4. **Возврат:** Возвращается словарь `sections` с секциями Markdown.


**Примеры:**

* Вход: `# Заголовок 1\nТекст заголовка 1\n## Заголовок 2\nТекст заголовка 2`
* Выход: `{ 'Заголовок 1': ['Текст заголовка 1'], 'Заголовок 2': ['Текст заголовка 2'] }`

* Вход: `# Заголовок 1\n{ "ключ": "значение" }\nТекст заголовка 1`
* Выход: `{'Заголовок 1': ['Текст заголовка 1']} ` (JSON не является главной секцией)


# <mermaid>

```mermaid
graph TD
    A[md_string] --> B{extract_JSON?};
    B -- yes --> C[{"json": json_content}];
    B -- no --> D[markdown(md_string)];
    D --> E[sections = {}];
    E --> F{loop through html lines};
    F -- line startsWith <h...> --> G[heading_level, section_title];
    G -- heading_level = 1 --> H[sections[section_title] = []];
    G -- heading_level > 1 --> I[sections[current_section].append(section_title)];
    F -- line is not empty and current_section != null --> J[clean_text, sections[current_section].append(clean_text)];
    F -- else --> K[];
    K --> L[return sections];
    C --> L;
    subgraph "extract_JSON_from_string"
        B1[text] --> B2{json_pattern match?};
        B2 -- yes --> B3[eval(json_match)];
        B2 -- no --> B4[None];
        B3 --> B5[return json];
        B4 --> B5;
    end
```

**Описание диаграммы:**

Диаграмма описывает поток данных и вызовов функций.  `md2dict` принимает строку Markdown (`md_string`) и возвращает словарь с секциями (`sections`) или с JSON, если он присутствует.

- **extract_JSON_from_string**: Функция для поиска JSON в строке. Ищет совпадение с шаблоном JSON и возвращает его результат или None.
- **markdown(md_string)**: Преобразует Markdown в HTML.
- **loop through html lines**: Цикл, обрабатывающий каждую строку HTML.
- **sections[section_title] = []**: Создание новой секции в словаре.
- **sections[current_section].append(section_title/clean_text)**: Добавление заголовка или текста в текущую секцию.

**Подключаемые зависимости:**

- `re` - для работы с регулярными выражениями.
- `typing` - для типизации.
- `markdown2` - для преобразования Markdown в HTML.
- `src.logger.logger` - для работы с логированием.

# <explanation>

**Импорты:**

- `re`: Для работы с регулярными выражениями, необходимыми для поиска JSON и заголовков.
- `typing`: Для использования типов данных в аннотациях, что улучшает читаемость и поддержку кода.
- `markdown2`: Из пакета `markdown2` импортируется функция `markdown` для конвертации строки Markdown в HTML.
- `src.logger.logger`:  Импортируется из пакета `src.logger.logger` объект `logger`.  Это указывает на то, что для логирования ошибок используется внешняя система логирования, что полезно для отладки и контроля выполнения программы.

**Классы:**

Нет определённых классов.

**Функции:**

- `md2dict(md_string: str) -> Dict[str, dict | list]`:  
    - Принимает строку Markdown в качестве аргумента.
    - Возвращает словарь, содержащий извлеченный JSON, если он есть, или секции Markdown.
    - Обрабатывает исключения, предотвращая сбой при ошибках в Markdown или JSON.

- `extract_json_from_string(text: str) -> dict | None`:
    - Принимает строку в качестве аргумента.
    - Использует регулярное выражение для поиска JSON.
    - Возвращает JSON, если он найден, или `None`.
    - Обрабатывает исключения, связанные с некорректным JSON.


**Переменные:**

- `MODE`: Переменная, видимо, для настройки режима работы (возможно, debug/prod).
- `sections`: Словарь, хранящий секции Markdown с их заголовками и текстом.
- `current_section`:  Переменная, хранящая текущую секцию Markdown, используется для агрегирования текста в одну секцию.

**Возможные ошибки и улучшения:**

- **`eval()`**: Использование `eval()` для обработки JSON может быть небезопасно, особенно при работе с входными данными, полученными из сторонних источников. Лучше использовать `json.loads()`, так как `eval()` может быть уязвим к внедрению кода.

- **Более сложные форматы:** Код обрабатывает только простой JSON в виде блока. Для обработки более сложных структур данных, содержащих Markdown, понадобится более изощренный подход.


**Взаимосвязи с другими частями проекта:**

- Функция использует `logger`, что указывает на интеграцию с системой логирования проекта (`src.logger.logger`).  Это указывает на наличие логирования ошибок.  Функция `logger` нужна для логгирования ошибок при некорректном формате Markdown или JSON.