# Анализ кода модуля `md2dict.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет поставленную задачу по конвертации Markdown в словарь, включая извлечение JSON.
    - Используется `logger` для логирования ошибок.
    - Код достаточно читаемый и понятный.
-  Минусы
    - Не используется `j_loads` для обработки JSON, а используется `eval`, что может быть небезопасным.
    - Отсутствует обработка возможных ошибок при парсинге JSON.
    - Отсутствуют подробные комментарии в формате reStructuredText (RST) для функций и модуля.
    - Есть магические константы, например `h(\\d)`.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить `from src.utils.jjson import j_loads`.
2.  **Безопасность JSON:** Использовать `j_loads` вместо `eval` для парсинга JSON,  обернув в try-except.
3.  **Комментарии RST:** Добавить docstring в формате RST для модуля и функций.
4. **Константы:**  Определить константу для  `h(\\d)`.
5.  **Улучшение логики:** Переработать логику разбора HTML, чтобы повысить читаемость.
6.  **Обработка ошибок:** Обернуть `j_loads` в блок `try-except` для обработки ошибок при парсинге JSON.

**Оптимизированный код**

```python
"""
Модуль для конвертации Markdown в словарь
=========================================================================================

Этот модуль предоставляет функции для преобразования строк Markdown в структурированные словари.
Он также обрабатывает JSON-контент, если он присутствует в строке Markdown.

Модуль включает в себя следующие функции:

- :func:`md2dict`: конвертирует строку Markdown в словарь.
- :func:`extract_json_from_string`: извлекает JSON контент из строки.

Пример использования
--------------------

.. code-block:: python

    from src.utils.convertors.md2dict import md2dict

    markdown_text = "# Заголовок 1\nТекст параграфа\n## Заголовок 2\nЕще текст"
    result = md2dict(markdown_text)
    print(result)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import re
from typing import Dict, List, Any
from markdown2 import markdown
from src.logger.logger import logger
from src.utils.jjson import j_loads # Добавлен импорт j_loads

_HEADING_PATTERN = r'h(\d)' # Определена константа для шаблона поиска заголовков

def md2dict(md_string: str) -> Dict[str, Any]:
    """
    Конвертирует строку Markdown в структурированный словарь с извлечением JSON содержимого, если оно присутствует.

    :param md_string: Строка Markdown для конвертации.
    :type md_string: str
    :return: Структурированное представление Markdown содержимого.
    :rtype: Dict[str, Any]
    :raises Exception: Если возникает ошибка при обработке Markdown или JSON.

    Возвращает словарь с ключом "json", если найден JSON контент, или словарь с секциями Markdown.
    """
    try:
        # Извлечение JSON из строки Markdown, если присутствует
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        # Если JSON не найден, обрабатываем Markdown
        html = markdown(md_string)
        sections: Dict[str, List[str]] = {}
        current_section: str | None = None

        # Парсим HTML строку, полученную из Markdown
        for line in html.splitlines():
            # Обработка заголовков секций
            if line.startswith('<h'):
                heading_level_match = re.search(_HEADING_PATTERN, line) # Используем константу _HEADING_PATTERN
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

    :param text: Строка для извлечения JSON контента.
    :type text: str
    :return: Извлеченный JSON контент или `None`, если JSON не найден.
    :rtype: dict | None
    :raises Exception: Если возникает ошибка при парсинге JSON.
    """
    try:
        json_pattern = r"\{.*?\}" # Уточнен шаблон для поиска JSON
        json_match = re.search(json_pattern, text, re.DOTALL)
        if json_match:
            try:
                return j_loads(json_match.group()) # Используем j_loads для безопасного парсинга JSON
            except Exception as json_ex:
                logger.error("Ошибка при парсинге JSON.", exc_info=True) # Логируем ошибку парсинга JSON
                return None
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```