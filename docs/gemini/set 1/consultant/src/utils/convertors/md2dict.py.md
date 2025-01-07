# Анализ кода модуля `md2dict.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что улучшает читаемость и поддержку.
    - Используются `logger` для логирования ошибок, что помогает в отладке и мониторинге.
    - Присутствует docstring для модуля и функций, что соответствует стандартам документации.
-  Минусы
    -  Используется `eval` для разбора JSON, что может быть небезопасным.
    -  Недостаточно обработки ошибок, например, при обработке HTML.
    -  Отсутствует проверка на корректность JSON перед использованием `eval`.
    -  Не используется `j_loads` или `j_loads_ns` для обработки JSON.

**Рекомендации по улучшению**

1.  **Безопасность JSON:** Заменить `eval` на `j_loads` для парсинга JSON. Это повысит безопасность кода и исключит возможность выполнения произвольного кода.
2.  **Улучшение обработки ошибок:** Добавить более точную обработку ошибок при парсинге HTML.
3.  **Улучшение документации:** Дополнить docstring информацией о возможных исключениях и особенностях работы функций.
4.  **Удалить магические строки:** Убрать `` и `#! venv/bin/python/python3.12` из начала файла, так как они не несут информационной нагрузки в текущем контексте.
5. **Привести имена переменных к общему стилю**: Переименовать `heading_level_match` в `heading_match`.
6.  **Добавить проверки на типы данных**: В функции `md2dict` при добавлении текста в секцию, необходимо убедится что секция существует, перед добавлением в нее данных.
7.  **Общая обработка исключений:** В функциях `md2dict` и `extract_json_from_string` добавить проверку на `None` для возвращаемого значения.
8.  **Улучшение форматирования:** Добавить пустые строки для лучшего разделения логических блоков в коде.
9.  **Улучшить именование переменных:** Переименовать `json_pattern` в `json_regexp`.
10. **Удалить неиспользуемую переменную**: Удалить неиспользуемую переменную `MODE`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для конвертации Markdown в словарь
=========================================================

Этот модуль предоставляет функции для преобразования строк в формате Markdown
в структурированный словарь Python. Он поддерживает извлечение JSON
содержимого и структурирование Markdown на основе заголовков.

Пример использования
--------------------

Пример использования функций `md2dict` и `extract_json_from_string`:

.. code-block:: python

    from src.utils.convertors.md2dict import md2dict, extract_json_from_string

    markdown_text = "# Заголовок 1\\nТекст раздела 1\\n## Заголовок 2\\nТекст раздела 2\\n{\"key\": \"value\"}"
    result = md2dict(markdown_text)
    print(result)

    json_text = "{\"key\": \"value\"}"
    json_result = extract_json_from_string(json_text)
    print(json_result)
"""
import re
from typing import Dict, Any
from markdown2 import markdown
from src.logger.logger import logger
from src.utils.jjson import j_loads # импортируем j_loads для безопасного парсинга JSON


def md2dict(md_string: str) -> Dict[str, dict | list]:
    """
    Преобразует строку Markdown в структурированный словарь.

    Функция извлекает JSON контент, если он есть, или структурирует Markdown
    на основе заголовков, создавая секции.

    :param md_string: Строка Markdown для конвертации.
    :type md_string: str
    :raises Exception: Если возникает ошибка при обработке Markdown или HTML.
    :returns: Словарь с ключом "json", если JSON найден, или словарь с секциями.
    :rtype: Dict[str, dict | list]
    """
    try:
        # Извлечение JSON из строки Markdown
        json_content = extract_json_from_string(md_string)
        if json_content:
            return {"json": json_content}

        # Преобразование Markdown в HTML
        html = markdown(md_string)
        sections: Dict[str, list] = {}
        current_section: str | None = None

        # Парсинг HTML
        for line in html.splitlines():
            # Проверка на заголовок
            if line.startswith('<h'):
                heading_match = re.search(r'h(\d)', line) # находим уровень заголовка
                if heading_match:
                    heading_level = int(heading_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip()

                    #  Создаем новую секцию для заголовков первого уровня
                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []

                    # Добавляем заголовки уровня выше 1 в текущую секцию
                    elif current_section:
                        sections[current_section].append(section_title)
            # Добавление текста в текущую секцию
            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip()
                if current_section in sections: # Проверка, что секция существует перед добавлением данных
                    sections[current_section].append(clean_text)


        return sections

    except Exception as ex:
        logger.error("Ошибка при парсинге Markdown в структурированный словарь.", exc_info=True)
        return {}



def extract_json_from_string(text: str) -> dict | None:
    """
    Извлекает JSON контент из строки.

    Ищет JSON контент в строке с помощью регулярного выражения.

    :param text: Строка для извлечения JSON контента.
    :type text: str
    :raises Exception: Если возникает ошибка при извлечении JSON.
    :returns: Извлеченный JSON контент или None, если JSON не найден.
    :rtype: dict | None
    """
    try:
        json_regexp = r"\{.*\}" # регулярное выражение для поиска JSON
        json_match = re.search(json_regexp, text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            try:
                return j_loads(json_str) # безопасный парсинг JSON
            except Exception as json_ex:
                logger.error(f"Ошибка при парсинге JSON: {json_ex}", exc_info=True)
                return None
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```