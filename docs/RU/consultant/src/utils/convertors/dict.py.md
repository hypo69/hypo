# Анализ кода модуля `dict`

**Качество кода**
8
-   Плюсы
    - Код содержит docstring для функций, что облегчает понимание их назначения и использования.
    - Используются стандартные типы данных и структуры, такие как `dict`, `list`, `SimpleNamespace`, что способствует читаемости кода.
    - Присутствует обработка различных типов данных (int, str, list, dict) при преобразовании.
    - Разделение логики на мелкие функции (`_process_simple`, `_process_attr`, `_process_complex`, `_process`) упрощает понимание и отладку.
-   Минусы
    - Не хватает импорта `save_csv_file` из `src.utils.csv`,  необходимо добавить.
    - Присутствуют избыточные комментарии.
    - Используется `json`, но не используется `j_loads`, `j_loads_ns` из `src.utils.jjson`.
    - В `dict2pdf` нет обработки ошибок, что может привести к непредсказуемому поведению программы.
    - В `dict2xml` при возникновении исключения не используется `logger.error`.
    -  В функциях `dict2csv`, `dict2xls` нет обработки ошибок, лучше использовать `try/except` и логирование.
    - В функциях `dict2csv`, `dict2xls` не используется `from src.logger.logger import logger`.
    - Документация не соответствует RST стандарту.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить отсутствующие импорты из `src.utils.csv` и `src.utils.jjson`.
2.  **Логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок во всех функциях, где это необходимо, и заменить стандартный `Exception` на `logger.error`.
3.  **Обработка ошибок**: В функциях `dict2pdf`, `dict2csv`, `dict2xls` добавить обработку исключений с использованием `try-except` и логированием ошибок через `logger.error`.
4.  **Использование `j_loads`**: Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`, если это необходимо.
5.  **Форматирование**: Привести документацию к стандарту RST.
6.  **Рефакторинг**: Убрать лишние комментарии.
7.  **Переименование**: Привести имена переменных в соответствие с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для конвертации данных между форматом dict и SimpleNamespace.
=========================================================================================

Этот модуль предоставляет набор функций для рекурсивного преобразования словарей в объекты SimpleNamespace
и обратно, а также для экспорта данных в различные форматы.

Функции:
    - dict2ns: Рекурсивно преобразует словари в объекты SimpleNamespace.
    - dict2xml: Генерирует XML строку из словаря.
    - dict2csv: Сохраняет данные из словаря или SimpleNamespace в CSV файл.
    - dict2json: Сохраняет данные из словаря или SimpleNamespace в JSON файл.
    - dict2xls: Сохраняет данные из словаря или SimpleNamespace в XLS файл.
    - dict2html: Генерирует HTML таблицу из словаря или объекта SimpleNamespace.
    - dict2pdf: Сохраняет данные из словаря в PDF файл.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from types import SimpleNamespace

    data = {"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001"}}
    
    # Преобразование dict в SimpleNamespace
    ns_data = dict2ns(data)
    print(ns_data.name) # Выведет: John
    print(ns_data.address.city) # Выведет: New York
    
    # Сохранение в CSV файл
    csv_file = Path("output.csv")
    dict2csv(data, csv_file)

    # Сохранение в XLS файл
    xls_file = Path("output.xls")
    dict2xls(data, xls_file)

    # Сохранение в PDF файл
    pdf_file = Path("output.pdf")
    dict2pdf(data, pdf_file)
    
    # Преобразование в HTML
    html_string = dict2html(data)
    print(html_string) # Выведет HTML-таблицу
    
    # Преобразование в XML
    xml_string = dict2xml(data)
    print(xml_string)  # Выведет XML-строку
"""
import json
from types import SimpleNamespace
from typing import Any, Dict, List
from pathlib import Path
from xml.dom.minidom import getDOMImplementation
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.utils.xls import save_xls_file
from src.utils.csv import save_csv_file
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

def replace_key_in_dict(data: dict | list, old_key: str, new_key: str) -> dict:
    """Рекурсивно заменяет ключ в словаре или списке.

    :param data: Словарь или список, в котором происходит замена ключа.
    :type data: dict | list
    :param old_key: Ключ для замены.
    :type old_key: str
    :param new_key: Новый ключ.
    :type new_key: str
    :return: Обновленный словарь с замененными ключами.
    :rtype: dict

    :Example Usage:

        replace_key_in_json(data, 'name', 'category_name')

        # Example 1: Simple dictionary
        data = {"old_key": "value"}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"new_key": "value"}

        # Example 2: Nested dictionary
        data = {"outer": {"old_key": "value"}}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": {"new_key": "value"}}

        # Example 3: List of dictionaries
        data = [{"old_key": "value1"}, {"old_key": "value2"}]
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes [{"new_key": "value1"}, {"new_key": "value2"}]

        # Example 4: Mixed nested structure with lists and dictionaries
        data = {"outer": [{"inner": {"old_key": "value"}}]}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": [{"inner": {"new_key": "value"}}]}
    """
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key == old_key:
                data[new_key] = data.pop(old_key)
            if isinstance(data[key], (dict, list)):
                replace_key_in_dict(data[key], old_key, new_key)
    elif isinstance(data, list):
        for item in data:
            replace_key_in_dict(item, old_key, new_key)
    
    return data


def dict2pdf(data: Dict[str, Any] | SimpleNamespace, file_path: str | Path):
    """Сохраняет данные из словаря в PDF файл.

    :param data: Словарь для преобразования в PDF.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к выходному PDF файлу.
    :type file_path: str | Path
    """
    if isinstance(data, SimpleNamespace):
        data = data.__dict__

    try:
        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        pdf.setFont('Helvetica', 12)

        for key, value in data.items():
            line = f'{key}: {value}'
            pdf.drawString(x, y, line)
            y -= 20

            if y < 50:
                pdf.showPage()
                pdf.setFont('Helvetica', 12)
                y = height - 50

        pdf.save()
    except Exception as ex:
        logger.error(f'Ошибка при сохранении в PDF файл {file_path=}', exc_info=ex)


def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """Рекурсивно преобразует словари в SimpleNamespace.

    :param data: Данные для преобразования.
    :type data: Dict[str, Any] | List[Any]
    :return: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.
    :rtype: Any
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
    """Генерирует XML строку из словаря.

    :param data: Данные для преобразования в XML.
    :type data: Dict[str, Any]
    :param encoding: Кодировка данных, по умолчанию 'UTF-8'.
    :type encoding: str
    :return: XML строка, представляющая входной словарь.
    :rtype: str
    :raises Exception: Если предоставлено более одного корневого узла.
    """
    def _process_simple(doc, tag, tag_value):
        """Создает узел для простых типов (int, str).

        :param doc: Объект XML документа.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега XML элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел, представляющий тег и значение.
        :rtype: xml.dom.minidom.Element
        """
        node = doc.createElement(tag)
        node.appendChild(doc.createTextNode(str(tag_value)))
        return node

    def _process_attr(doc, attr_value: Dict[str, Any]):
        """Создает атрибуты для XML элемента.

        :param doc: Объект XML документа.
        :type doc: xml.dom.minidom.Document
        :param attr_value: Словарь атрибутов.
        :type attr_value: Dict[str, Any]
        :return: Список атрибутов для XML элемента.
        :rtype: List[xml.dom.minidom.Attr]
        """
        attrs = []
        for attr_name, value in attr_value.items():
            attr = doc.createAttribute(attr_name)
            attr.nodeValue = value if not isinstance(value, dict) else value.get('value', '')
            attrs.append(attr)
        return attrs

    def _process_complex(doc, children):
        """Создает узлы для сложных типов, таких как списки или словари.

        :param doc: Объект XML документа.
        :type doc: xml.dom.minidom.Document
        :param children: Список пар тег-значение.
        :type children: List[Tuple[str, Any]]
        :return: Список дочерних узлов и атрибутов.
        :rtype: Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]
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
        """Создает XML DOM объект для тега и его значения.

        :param doc: Объект XML документа.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега XML элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел или список узлов для тега и значения.
        :rtype: xml.dom.minidom.Element | List[xml.dom.minidom.Element]
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
        logger.error('Допускается только один корневой узел')
        raise Exception('Only one root node allowed')
    
    try:
        root, _ = _process_complex(doc, data.items())
        doc.appendChild(root[0])
        return doc.toxml(encoding)
    except Exception as ex:
        logger.error(f'Ошибка при преобразовании в XML', exc_info=ex)
        return ''


def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """Сохраняет данные из словаря или SimpleNamespace в CSV файл.

    :param data: Данные для сохранения в CSV файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к CSV файлу.
    :type file_path: str | Path
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    """
    try:
        return save_csv_file(data, file_path)
    except Exception as ex:
        logger.error(f'Ошибка при сохранении в CSV файл {file_path=}', exc_info=ex)
        return False


def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """Сохраняет данные из словаря или SimpleNamespace в XLS файл.

    :param data: Данные для сохранения в XLS файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к XLS файлу.
    :type file_path: str | Path
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    """
    try:
        return save_xls_file(data, file_path)
    except Exception as ex:
        logger.error(f'Ошибка при сохранении в XLS файл {file_path=}', exc_info=ex)
        return False


def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """Генерирует HTML таблицу из словаря или объекта SimpleNamespace.

    :param data: Данные для преобразования в HTML.
    :type data: dict | SimpleNamespace
    :param encoding: Кодировка данных, по умолчанию 'UTF-8'.
    :type encoding: str
    :return: HTML строка, представляющая входной словарь.
    :rtype: str
    """
    def dict_to_html_table(data: dict, depth: int = 0) -> str:
        """Рекурсивно преобразует словарь в HTML таблицу.

        :param data: Словарь для преобразования.
        :type data: dict
        :param depth: Глубина рекурсии, для вложенных таблиц, по умолчанию 0.
        :type depth: int
        :return: HTML таблица в виде строки.
        :rtype: str
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
    
    if isinstance(data, SimpleNamespace):
        data = data.__dict__
    
    html_content = dict_to_html_table(data)
    return f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="{encoding}">\n<title>Dictionary to HTML</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>'
```