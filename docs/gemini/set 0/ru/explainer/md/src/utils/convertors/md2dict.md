# <input code>

```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-\
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
            return eval(json_match.group())
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```

# <algorithm>

1. **Вход:** Строка Markdown (`md_string`).
2. **Извлечение JSON:**
   - Вызывается функция `extract_json_from_string` для поиска JSON в `md_string`.
   - Если JSON найден, возвращается словарь с ключом "json" и найденным JSON.
3. **Обработка Markdown:**
   - Если JSON не найден, строка Markdown преобразуется в HTML с помощью `markdown`.
   - Создается пустой словарь `sections` для хранения секций.
   - `current_section` инициализируется как `None`.
4. **Парсинг HTML:**
   - Цикл по каждой строке HTML:
     - Если строка начинается с `<h...>` (заголовок):
       - Определяется уровень заголовка.
       - Если уровень 1, создается новая секция в `sections` с названием заголовка.
       - Иначе, добавляется заголовок в текущую секцию.
     - Иначе, если строка не пустая и `current_section` определен, добавляется очищенная от HTML строка в текущую секцию.
5. **Возврат:** Возвращается словарь `sections`.
6. **Обработка ошибок:** Блок `try...except` обрабатывает потенциальные ошибки при парсинге и извлечении JSON, логгируя их в `logger`.


**Примеры:**

- Вход: `# Заголовок 1\nТекст\n## Заголовок 2`
- Выход: `{'Заголовок 1': ['Текст'], 'Заголовок 2': []}`

- Вход: `# Заголовок 1\n```json\n{"key": "value"}\n````
- Выход: `{'json': {'key': 'value'}}`


# <mermaid>

```mermaid
graph TD
    A[md_string] --> B{JSON?};
    B -- Да --> C[{"json": json_content}];
    B -- Нет --> D[markdown(md_string)];
    D --> E[sections = {}];
    E --> F[current_section = null];
    F --> G(for line in html.splitlines());
    G -- line.startswith('<h') --> H{heading_level};
    H -- 1 --> I[current_section = section_title, sections[current_section] = []];
    H -- >1 --> J[sections[current_section].append(section_title)];
    G -- line.strip() and current_section --> K[clean_text = re.sub(r'<.*?>', '', line).strip()];
    K --> L[sections[current_section].append(clean_text)];
    G -- else --> G;
    G --> M[return sections];
    C --> M;
    M --> N(except);
    N --> O[logger.error];
    B -- Нет --> O;
    subgraph extract_json_from_string
        Z[text] --> AA{json_match?};
        AA -- Да --> BB[eval(json_match.group())];
        AA -- Нет --> CC[None];
        BB --> AA;
        CC --> AA;
        AA --> DD(except);
        DD --> O;
        end
```

**Зависимости:**

- `markdown2`: используется для преобразования Markdown в HTML.
- `re`: используется для регулярных выражений, которые необходимы для поиска JSON и HTML-тегов.
- `typing`: обеспечивает типы данных, что делает код более читабельным и поддерживаемым.
- `src.logger`: логгер для вывода сообщений об ошибках.
- `import re`: используется для обработки регулярных выражений, необходимых для извлечения JSON из строки.


# <explanation>

- **Импорты:**
  - `markdown2`: библиотека для парсинга Markdown в HTML.
  - `src.logger`: предположительно, собственный логгер проекта, позволяющий выводить подробные сообщения об ошибках и отслеживать работу.


- **Классы:** Нет классов.


- **Функции:**
  - `md2dict(md_string)`:  принимает строку Markdown, пытается извлечь JSON, если он найден, возвращает словарь с ключом "json". Если JSON не найден, преобразует строку в HTML, анализирует HTML, группируя текст по заголовкам и возвращает словарь, в котором ключи - заголовки, а значения - списки строк текста.  Обрабатывает ошибки и возвращает пустой словарь при проблемах.
  - `extract_json_from_string(text)`: ищет JSON в строке, используя регулярные выражения, и возвращает извлеченный JSON или None. Использует `eval()` для непосредственного преобразования извлеченной строки в словарь Python.  Важное замечание: `eval()` может быть небезопасным, если вы не контролируете входные данные. В реальных приложениях лучше использовать `json.loads()` для разбора JSON,  чтобы избежать потенциальных проблем безопасности.


- **Переменные:**
  - `MODE`, `sections`, `current_section`, `json_content`, `html`, `line`, `heading_level_match`, `heading_level`, `section_title`, `clean_text` и т.д.  Обычно они имеют типы данных, соответствующие их назначению (строки, словари, списки).

- **Возможные ошибки и улучшения:**
  - **Безопасность:**  Использование `eval()` для парсинга JSON небезопасно, особенно с неконтролируемыми входными данными. Лучше использовать `json.loads(json_match.group())`, это предотвратит потенциальные атаки с кодом.
  - **Обработка ошибок:** Логирование ошибок в `logger` полезно.  Дополнительно можно добавить обработку более конкретных типов ошибок (например, `json.JSONDecodeError`).
  - **Читабельность:**  Можно использовать более ясные имена переменных (например, `extracted_json` вместо `json_content`).
  - **Универсальность:**  Можно добавить обработку разных типов данных (например, списков, кортежей) внутри JSON.

**Взаимосвязи с другими частями проекта:**

Функция `md2dict` использует функцию `extract_json_from_string` и логгер из пакета `src.logger`.  Это указывает на то, что `md2dict` является частью модуля `utils.convertors` и взаимодействует с `logger` для логирования и обработки ошибок.  Также, вероятно, существуют другие модули в проекте, которые могут использовать `md2dict` для преобразования строк Markdown в структурированные данные.