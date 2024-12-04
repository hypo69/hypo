```MD
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

1. **Вход:** Строка Markdown (`md_string`).
2. **Извлечение JSON:**  Функция `extract_json_from_string` ищет JSON внутри `md_string`.
   - Если JSON найден, возвращает его в виде словаря.
   - Иначе переходит к следующему этапу.
3. **Обработка Markdown:**  
   - Используется библиотека `markdown2` для преобразования `md_string` в HTML (`html`).
   - Инициализируется пустой словарь `sections` для хранения секций.
   - Переменная `current_section` отслеживает текущую секцию.
4. **Парсинг HTML:**  Цикл по строкам HTML (`html.splitlines()`).
   - Если строка начинается с `<h...>` (заголовок):
     - Определяется уровень заголовка.
     - Если уровень 1, создается новая секция в `sections` с названием заголовка.
     - Если уровень > 1, добавляется заголовок в текущую секцию.
   - Если строка не пустая и `current_section` определена, добавляет очищенную строку (без HTML тегов) в текущую секцию.
5. **Возврат:** Возвращает словарь `sections`, содержащий секции и их содержимое.

**Пример:**

Вход: `md_string` содержащий заголовок уровня 1 "Секция 1" и подзаголовок уровня 2 "Подсекция 1" и текст "Текст секции 1".

Выход: `sections = {"Секция 1": ["Подсекция 1", "Текст секции 1"]}`


# <mermaid>

```mermaid
graph TD
    A[md_string] --> B{Extract JSON?};
    B -- Yes --> C[return {"json": json_content}];
    B -- No --> D[markdown(md_string)];
    D --> E[sections = {}];
    E --> F(current_section = null);
    F --> G[for line in html.splitlines()];
    G -- line.startswith('<h') --> H{heading_level};
    H -- level == 1 --> I[sections[section_title] = []];
    H -- level > 1 --> J[sections[current_section].append(section_title)];
    G -- line.strip() and current_section --> K[clean_text = re.sub(r'<.*?>', '', line).strip()];
    K --> L[sections[current_section].append(clean_text)];
    G -- else --> G;
    I --> G;
    J --> G;
    L --> G;
    G --> M[return sections];
    subgraph "extract_json_from_string"
        B1[text] --> B2{re.search(json_pattern)};
        B2 -- Yes --> B3[return eval(json_match.group())];
        B2 -- No --> B4[return None];
    end

    
```
**Зависимости**:
- `re`:  Для работы с регулярными выражениями при извлечении JSON и форматировании HTML.
- `typing`: Для использования типов данных, улучшающих читаемость и безопасность кода.
- `markdown2`: Для преобразования Markdown в HTML.
- `src.logger`:  Для логгирования ошибок.  Предполагается, что `logger` реализован в другом модуле `src`.

# <explanation>

**Импорты:**

- `re`:  Модуль для работы с регулярными выражениями, необходим для поиска JSON и HTML тегов.
- `typing`: Модуль для задания типов данных. Используется `from typing import Dict` для указания типа переменной `sections` как словаря.
- `markdown2`:  Библиотека для конвертации Markdown в HTML. Эта библиотека необходима для обработки входных данных Markdown.
- `src.logger`:  Логгер из подпапки `logger` в модуле `src`. Предполагается, что этот модуль содержит логирование в файлы или консоль, а также управление уровнями и форматами логов.

**Классы:**

Нет классов в коде.

**Функции:**

- `md2dict(md_string: str) -> Dict[str, dict | list]`: Функция для конвертации Markdown в словарь.
    - Принимает строку Markdown (`md_string`).
    - Возвращает словарь, содержащий секции Markdown или словарь с ключом "json" в случае, если в `md_string` найден JSON.
    - Обрабатывает возможные исключения при работе с Markdown или JSON.
- `extract_json_from_string(text: str) -> dict | None`: Функция для извлечения JSON из строки.
    - Принимает строку `text`.
    - Возвращает словарь с JSON или `None`, если JSON не найден.
    - Использует `eval()` для обработки найденного JSON. Необходимо понимать, что `eval()` может быть небезопасным, если входные данные не контролируются.

**Переменные:**

- `MODE`: Переменная для обозначения режима работы.
- `sections`: Словарь для хранения секций Markdown.
- `current_section`: Переменная, хранящая название текущей секции.
- `json_content`: Содержимое JSON, если оно найдено.

**Возможные ошибки и улучшения:**

- **Безопасность `eval()`**: Использование `eval()` для парсинга JSON может быть небезопасным, особенно если входные данные могут быть подменены злоумышленником.  Рекомендуется использовать `json.loads()` для безопасного парсинга JSON.
- **Обработка ошибок**: Обработка ошибок в `extract_json_from_string` и `md2dict` улучшена, но можно добавить проверку на наличие HTML ошибок.


**Цепочка взаимосвязей:**

Функция `md2dict` использует `extract_json_from_string` для поиска JSON, и обрабатывает полученные данные в соответствии с логикой. В случае отсутствия JSON, функция `md2dict` использует `markdown2` для конвертации входных данных Markdown в HTML и парсит HTML для извлечения данных в словарь `sections`. Всю работу логгирует `src.logger`.