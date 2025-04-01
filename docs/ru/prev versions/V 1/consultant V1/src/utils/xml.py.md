## Анализ кода модуля `xml`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код выполняет полезную функцию очистки и сохранения XML данных.
    - Присутствуют docstring для функций, что облегчает понимание кода.
    - Используется `ElementTree` для парсинга и обработки XML.
- **Минусы**:
    - Отсутствуют импорты `logger` из `src.logger`.
    - Не используются одинарные кавычки в определениях строк.
    - Отсутствуют type hints для аргументов в функции `remove_empty_elements`.
    - Комментарии внутри функций не всегда соответствуют стилю, указанному в инструкции.
    - В примере использования не указаны типы для переменных.
    - Используются двойные кавычки для строк, необходимо заменить на одинарные.

**Рекомендации по улучшению:**

1.  **Импорт `logger`**: Добавить импорт `logger` из `src.logger` для логирования ошибок и информации.
2.  **Использовать одинарные кавычки**: Заменить все двойные кавычки на одинарные для определения строк, как указано в инструкции.
3.  **Type hints**: Добавить type hints для аргументов функции `remove_empty_elements`.
4.  **Форматирование комментариев**: Привести комментарии к единому стилю, указанному в инструкции.
5.  **Обработка исключений**: Добавить обработку исключений с использованием `logger.error`.
6.  **Примеры использования**: Привести примеры использования в docstring к требуемому формату.
7.  **Документация модуля**: Добавить документацию для модуля.

**Оптимизированный код:**

```python
## \file /src/utils/xml.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для работы с XML-данными.
=================================

Модуль содержит функции для очистки и сохранения XML-данных.

Пример использования:
----------------------

>>> from pathlib import Path
>>> xml_data = '<root><item>Value</item><item attr="test">Another</item></root>'
>>> file_path = Path('output.xml')
>>> save_xml(xml_data, str(file_path))
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import re
from pathlib import Path
from src.logger import logger  # Импортируем logger


def clean_empty_cdata(xml_string: str) -> str:
    """
    Очищает пустые CDATA секции и лишние пробелы в XML строке.

    Args:
        xml_string (str): XML контент.

    Returns:
        str: Очищенный и отформатированный XML контент.

    Raises:
        ET.ParseError: Если XML строка имеет неверный формат.

    Example:
        >>> xml_string = '<root><item></item><item>Value</item></root>'
        >>> clean_empty_cdata(xml_string)
        '<root><item>Value</item></root>'
    """
    try:
        root = ET.fromstring(xml_string)

        def remove_empty_elements(element: ET.Element) -> None:
            """
            Рекурсивно удаляет пустые элементы из XML.

            Args:
                element (ET.Element): XML элемент.
            """
            for child in list(element):
                remove_empty_elements(child)
                if not (child.text and child.text.strip()) and not child.attrib and not list(child):
                    element.remove(child)

        remove_empty_elements(root)
        cleaned_xml = ET.tostring(root, encoding='utf-8').decode('utf-8')
        cleaned_xml = re.sub(r'>\s+<', '><', cleaned_xml)  # Remove unnecessary whitespace
        return cleaned_xml
    except ET.ParseError as ex:
        logger.error('Ошибка при парсинге XML', ex, exc_info=True)
        return xml_string  # Или можно вызвать исключение, в зависимости от логики


def save_xml(xml_string: str, file_path: str | Path) -> None:
    """
    Сохраняет очищенные XML данные из строки в файл с отступами.

    Args:
        xml_string (str): XML контент в виде строки.
        file_path (str | Path): Путь к выходному файлу.

    Returns:
        None

    Raises:
        OSError: Если возникает ошибка при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> xml_string = '<root><item>Value</item></root>'
        >>> file_path = Path('output.xml')
        >>> save_xml(xml_string, str(file_path))
    """
    try:
        # Очистка XML от пустых элементов
        cleaned_xml = clean_empty_cdata(xml_string)

        # Парсим XML-строку
        xml_tree = ET.ElementTree(ET.fromstring(cleaned_xml))

        # Преобразуем в строку с отступами
        rough_string = ET.tostring(xml_tree.getroot(), encoding='utf-8')
        parsed_xml = minidom.parseString(rough_string)
        pretty_xml = parsed_xml.toprettyxml(indent='  ')

        # Записываем в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(pretty_xml)
    except OSError as ex:
        logger.error('Ошибка при записи XML в файл', ex, exc_info=True)


if __name__ == '__main__':
    ...
    # Пример использования
    # xml_data = '<root><item>Value</item><item attr="test">Another</item></root>'
    # save_xml(xml_data, 'output.xml')
```