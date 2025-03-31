## Анализ кода модуля `dict`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Модуль предоставляет набор функций для преобразования данных между форматами (dict, SimpleNamespace, XML, CSV, XLS, HTML, PDF).
    - Код достаточно хорошо структурирован и содержит docstrings для большинства функций.
- **Минусы**:
    - Не все функции имеют примеры использования в docstrings.
    - Отсутствует обработка исключений в некоторых функциях (например, при записи в файл).
    - Не используется модуль `logger` для логирования ошибок.
    - Есть функции, которые, вероятно, не используются (например, `example_json2xml`).
    - В docstring встречаются конструкции с двойными кавычками

**Рекомендации по улучшению:**

1.  **Документация**:
    *   Добавить примеры использования для всех функций, чтобы облегчить понимание их работы.
    *   Уточнить docstrings, где это необходимо, чтобы они были более понятными и информативными.
2.  **Обработка ошибок**:
    *   Добавить обработку исключений во все функции, которые могут вызывать ошибки (например, при записи в файл, преобразовании данных).
    *   Использовать модуль `logger` для логирования ошибок и предупреждений.
3.  **Использование `j_loads` и `j_loads_ns`**:
    *   В данном модуле не используются функции для чтения JSON-файлов, поэтому замена `json.load` на `j_loads` или `j_loads_ns` не требуется.
4.  **Удаление неиспользуемого кода**:
    *   Удалить функцию `example_json2xml`, если она не используется.
5.  **Соответствие стандартам PEP8**:
    *   Проверить и исправить код на соответствие стандартам PEP8 (например, добавить пробелы вокруг операторов, использовать snake_case для именования функций и переменных).
6.  **Переименовать функцию**
    *   `replace_key_in_json` переименовать в `replace_key_in_dict` для сохранения консистентности.

**Оптимизированный код:**

```python
## \file /src/utils/convertors/dict.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для преобразования между dict и SimpleNamespace объектами.
==============================================================

Модуль содержит функции для рекурсивного преобразования словарей в объекты SimpleNamespace и наоборот,
а также для экспорта данных в различные форматы.
"""

import json
import xml.etree.ElementTree as ET
from types import SimpleNamespace
from typing import Any, Dict, List
from pathlib import Path
from xml.dom.minidom import getDOMImplementation

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.utils.xls import save_xls_file
from src.utils.csv import save_csv_file # import save_csv_file
from src.logger import logger # import logger

def replace_key_in_dict(data: dict | list, old_key: str, new_key: str) -> dict | list:
    """
    Рекурсивно заменяет ключ в словаре или списке.

    Args:
        data (dict | list): Словарь или список, в котором происходит замена ключа.
        old_key (str): Ключ, который нужно заменить.
        new_key (str): Новый ключ.

    Returns:
        dict | list: Обновленный словарь с замененными ключами.

    Example:
        >>> data = {'old_key': 'value'}
        >>> updated_data = replace_key_in_dict(data, 'old_key', 'new_key')
        >>> print(updated_data)
        {'new_key': 'value'}
    """
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key == old_key:
                data[new_key] = data.pop(old_key)
            if isinstance(data[new_key], (dict, list)): # change `data[key]` to `data[new_key]` because the key already changed
                replace_key_in_dict(data[new_key], old_key, new_key) # change `data[key]` to `data[new_key]` because the key already changed
    elif isinstance(data, list):
        for item in data:
            replace_key_in_dict(item, old_key, new_key)
    
    return data


def dict2pdf(data: Dict[str, Any] | SimpleNamespace, file_path: str | Path) -> None:
    """
    Сохраняет данные словаря в PDF-файл.

    Args:
        data (Dict[str, Any] | SimpleNamespace): Словарь для преобразования в PDF.
        file_path (str | Path): Путь к выходному PDF-файлу.

    Raises:
        Exception: Если возникает ошибка при создании или сохранении PDF-файла.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> dict2pdf(data, 'example.pdf')
    """
    try:
        if isinstance(data, SimpleNamespace):
            data = data.__dict__

        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        pdf.setFont('Helvetica', 12)

        for key, value in data.items():
            line = f'{key}: {value}'
            pdf.drawString(x, y, line)
            y -= 20

            if y < 50:  # Создать новую страницу, если места недостаточно
                pdf.showPage()
                pdf.setFont('Helvetica', 12)
                y = height - 50

        pdf.save()
    except Exception as ex:
        logger.error('Error while converting dict to PDF', ex, exc_info=True)


def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """
    Рекурсивно преобразует словари в SimpleNamespace.

    Args:
        data (Dict[str, Any] | List[Any]): Данные для преобразования.

    Returns:
        Any: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> ns_data = dict2ns(data)
        >>> print(ns_data.name)
        John
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = dict2ns(value)
            elif isinstance(value, list):
                data[key] = [dict2ns(item) if isinstance(item, dict) else item for item in value]
        return SimpleNamespace(**data)
    elif isinstance(data, list):
        return [dict2ns(item) if isinstance(item, dict) else item for item in data]
    return data


def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Генерирует XML-строку из словаря.

    Args:
        data (Dict[str, Any]): Данные для преобразования в XML.
        encoding (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

    Returns:
        str: XML-строка, представляющая входной словарь.

    Raises:
        Exception: Если предоставлено более одного корневого узла.

    Example:
        >>> data = {'root': {'name': 'John', 'age': 30}}
        >>> xml_string = dict2xml(data)
        >>> print(xml_string)
        <?xml version="1.0" encoding="UTF-8"?>
        <root><name>John</name><age>30</age></root>
    """
    def _process_simple(doc, tag, tag_value):
        """
        Генерирует узел для простых типов (int, str).

        Args:
            doc (xml.dom.minidom.Document): XML document object.
            tag (str): Имя тега для XML-элемента.
            tag_value (Any): Значение тега.

        Returns:
            xml.dom.minidom.Element: Узел, представляющий тег и значение.
        """
        node = doc.createElement(tag)
        node.appendChild(doc.createTextNode(str(tag_value)))
        return node

    def _process_attr(doc, attr_value: Dict[str, Any]):
        """
        Генерирует атрибуты для XML-элемента.

        Args:
            doc (xml.dom.minidom.Document): XML document object.
            attr_value (Dict[str, Any]): Словарь атрибутов.

        Returns:
            List[xml.dom.minidom.Attr]: Список атрибутов для XML-элемента.
        """
        attrs = []
        for attr_name, value in attr_value.items():
            attr = doc.createAttribute(attr_name)
            attr.nodeValue = value if not isinstance(value, dict) else value.get('value', '')
            attrs.append(attr)
        return attrs

    def _process_complex(doc, children):
        """
        Генерирует узлы для сложных типов, таких как списки или словари.

        Args:
            doc (xml.dom.minidom.Document): XML document object.
            children (List[Tuple[str, Any]]): Список пар тег-значение.

        Returns:
            Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]: Список дочерних узлов и атрибутов.
        """
        nodelist = []
        attrs = []
        for tag, value in children:
            if tag == 'attrs':
                attrs = _process_attr(doc, value)
            else:
                nodes = _process(doc, tag, value)
                nodelist.extend(nodes if isinstance(nodes, list) else [nodes])
        return nodelist, attrs

    def _process(doc, tag, tag_value):
        """
        Генерирует XML DOM объект для тега и его значения.

        Args:
            doc (xml.dom.minidom.Document): XML document object.
            tag (str): Имя тега для XML-элемента.
            tag_value (Any): Значение тега.

        Returns:
            xml.dom.minidom.Element | List[xml.dom.minidom.Element]: Узел или список узлов для тега и значения.
        """
        if isinstance(tag_value, dict) and list(tag_value.keys()) == ['value']:
            tag_value = tag_value['value']

        if tag_value is None:
            tag_value = ''

        if isinstance(tag_value, (float, int, str)):
            return _process_simple(doc, tag, tag_value)

        if isinstance(tag_value, list):
            return _process_complex(doc, [(tag, x) for x in tag_value])[0]

        if isinstance(tag_value, dict):
            node = doc.createElement(tag)
            nodelist, attrs = _process_complex(doc, tag_value.items())
            for child in nodelist:
                node.appendChild(child)
            for attr in attrs:
                node.setAttributeNode(attr)
            return node

    doc = getDOMImplementation().createDocument(None, None, None)
    if len(data) > 1:
        raise Exception('Only one root node allowed')
    
    root, _ = _process_complex(doc, data.items())
    doc.appendChild(root[0])
    return doc.toxml(encoding)


def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные словаря или SimpleNamespace в CSV-файл.

    Args:
        data (dict | SimpleNamespace): Данные для сохранения в CSV-файл.
        file_path (str | Path): Путь к CSV-файлу.

    Returns:
        bool: True, если файл был успешно сохранен, False в противном случае.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> result = dict2csv(data, 'example.csv')
        >>> print(result)
        True
    """
    try:
        return save_csv_file(data, file_path)
    except Exception as ex:
        logger.error('Error while converting dict to CSV', ex, exc_info=True)
        return False


def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные словаря или SimpleNamespace в XLS-файл.

    Args:
        data (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
        file_path (str | Path): Путь к XLS-файлу.

    Returns:
        bool: True, если файл был успешно сохранен, False в противном случае.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> result = dict2xls(data, 'example.xls')
        >>> print(result)
        True
    """
    try:
        return save_xls_file(data, file_path)
    except Exception as ex:
        logger.error('Error while converting dict to XLS', ex, exc_info=True)
        return False


def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Генерирует HTML-таблицу из словаря или объекта SimpleNamespace.

    Args:
        data (dict | SimpleNamespace): Данные для преобразования в HTML.
        encoding (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

    Returns:
        str: HTML-строка, представляющая входной словарь.

    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> html_string = dict2html(data)
        >>> print(html_string)
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>Dictionary to HTML</title>
        </head>
        <body>
        <table border="1" cellpadding="5" cellspacing="0">
        <tr><td><strong>name</strong></td><td>John</td></tr>
        <tr><td><strong>age</strong></td><td>30</td></tr>
        </table>
        </body>
        </html>
    """
    def dict_to_html_table(data: dict, depth: int = 0) -> str:
        """
        Рекурсивно преобразует словарь в HTML-таблицу.

        Args:
            data (dict): Данные словаря для преобразования.
            depth (int, optional): Глубина рекурсии, используется для вложенных таблиц. По умолчанию 0.

        Returns:
            str: HTML-таблица в виде строки.
        """
        html = ['<table border="1" cellpadding="5" cellspacing="0">']
        
        if isinstance(data, dict):
            for key, value in data.items():
                html.append('<tr>')
                html.append(f'<td><strong>{key}</strong></td>')
                if isinstance(value, dict):
                    html.append(f'<td>{dict_to_html_table(value, depth + 1)}</td>')
                elif isinstance(value, list):
                    html.append('<td>')
                    html.append('<ul>')
                    for item in value:
                        html.append(f'<li>{item}</li>')
                    html.append('</ul>')
                    html.append('</td>')
                else:
                    html.append(f'<td>{value}</td>')
                html.append('</tr>')
        else:
            html.append(f'<tr><td colspan="2">{data}</td></tr>')
        
        html.append('</table>')
        return '\n'.join(html)
    
    # Convert data to dictionary if it's a SimpleNamespace
    if isinstance(data, SimpleNamespace):
        data = data.__dict__
    
    html_content = dict_to_html_table(data)
    return f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="{encoding}">\n<title>Dictionary to HTML</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>'


# def example_json2xml():
#
#     # Example usage
#     json_data = {
#         "product": {
#             "name": {
#                 "language": [
#                     {
#                         "@id": "1",
#                         "#text": "Test Product"
#                     },
#                     {
#                         "@id": "2",
#                         "#text": "Test Product"
#                     },
#                     {
#                         "@id": "3",
#                         "#text": "Test Product"
#                     }
#                 ]
#             },
#             "price": "10.00",
#             "id_tax_rules_group": "13",
#             "id_category_default": "2"
#         }
#     }
#
#     xml_output = json2xml(json_data)
#     print(xml_output)


if __name__ == '__main__':
    ...
    #example_json2xml()
```