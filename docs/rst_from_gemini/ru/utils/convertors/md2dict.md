```python
## \file hypotez/src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.utils.convertors """
"""
module: src.utils.convertors

Модуль для конвертации строки Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.  Обрабатывает заголовки различных уровней и сохраняет текст внутри секций.
"""

import re
from typing import Dict, List
from markdown2 import markdown
from src.logger import logger
import json


def md2dict(md_string: str) -> Dict[str, dict | list]:
    """
    Конвертирует строку Markdown в структурированный словарь с извлечением JSON содержимого, если оно присутствует.

    Args:
        md_string (str): Строка Markdown для конвертации.

    Returns:
        Dict[str, dict | list]: Структурированное представление Markdown содержимого.
        Возвращает словарь с ключом "json", если найден JSON контент, или словарь с секциями Markdown.
        Возвращает пустой словарь в случае ошибки.
    """
    try:
        # Извлечение JSON из строки Markdown, если присутствует
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        # Если JSON не найден, обрабатываем Markdown
        html = markdown(md_string)
        sections: Dict[str, List[str]] = {}  # Используем List[str] для хранения текста
        current_section: str | None = None

        # Парсим HTML строку, полученную из Markdown
        for line in html.splitlines():
            line = line.strip()  # Удаляем лишние пробелы
            if not line:  # Пропускаем пустые строки
                continue
            
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
            elif line and current_section:
                # Приводим к строке и чистим теги
                clean_text = re.sub(r'<.*?>', '', line).strip()
                if clean_text:  # Проверяем, что очищенный текст не пустой
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
        json_pattern = r"\{.*\}"
        json_match = re.search(json_pattern, text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)  # Получаем полную строку json
            return json.loads(json_str)  # Используем json.loads для безопасной парсировки
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при декодировании JSON: {e}")
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None

```

**Изменения и улучшения:**

* **Тип данных:**  `sections` изменен на `Dict[str, List[str]]`, чтобы хранить списки строк, что более подходит для хранения текста.
* **Обработка пустых строк:** Добавлена проверка `if not line:` для пропуска пустых строк в `html.splitlines()`, что предотвращает ошибки и улучшает надежность.
* **Обработка пустых строк после очистки:** Добавлен `if clean_text:` для избежания добавления пустых элементов в список.
* **`json.loads`:**  Используется `json.loads(json_match.group(0))` вместо `eval`.  Это *критически важно* для безопасности, так как `eval` может быть уязвим к атакам типа выполнения произвольного кода.
* **Обработка ошибок JSON:** Добавлена обработка `json.JSONDecodeError`, чтобы программа не падала при некорректном JSON.  Это значительно улучшает устойчивость кода к различным проблемам входных данных.
* **Логирование:** Сообщения об ошибках из `extract_json_from_string` теперь содержат более информативную информацию.
* **Удаление лишних пробелов:** Добавлено `line.strip()` для удаления лишних пробелов.
* **Уточнения документации:** Документация дополнена, чтобы более точно отражать функциональность и возможные возвращаемые значения.


Эти изменения делают код более надежным, безопасным и удобным в использовании.  Теперь он правильно обрабатывает различные варианты входных данных и возвращает более информативные результаты.  Не забудьте установить `markdown2` и `json` в вашем проекте.


```bash
pip install markdown2 json
```